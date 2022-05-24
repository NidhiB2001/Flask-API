import os
from app import app
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import keras_ocr
import glob
from datetime import datetime

scopes = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name("flowing-radio-347411-f6b13db7738b.json", scopes)
file = gspread.authorize(credentials) 
sheet = file.open("Number plate Recognition").get_worksheet(15)
header = ["Date", "Number plate"]
sheet.insert_row(header)

pipeline = keras_ocr.pipeline.Pipeline()


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'mp4'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('Image successfully uploaded in postmanimg folder')
            
            listimg = os.listdir('postmanimg/')
            image = ''.join(map(str,listimg))
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            tlist=[]
            l = len(sheet.col_values(1))
            l += 1
            sheet.update('A'+str(l),dt_string)
            
            temp_NP_List = []
            images = [
                keras_ocr.tools.read(img) for img in ['postmanimg/'+image]
            ]
            prediction_groups = pipeline.recognize(images)
            for i in prediction_groups:
                for text, box in i:
                    print("text :::::::::", text)
                    temp_NP_List.append(text)
                temp_NP_List.remove('ind')
            print("temp_NP_List :::::::::::::::::",temp_NP_List)
            num = (''.join(temp_NP_List))
            print("Number plate:::",num)
            tlist.append(num)
            print(tlist)
            print("one plate detected")
            sheet.update('B'+str(l),[tlist])
            return redirect('/')
        else:
            flash('Allowed file types are png, jpg, jpeg, mp4')
            return redirect(request.url)

# if __name__ == "__main__":
#     app.run()
if __name__=="__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 8011)))