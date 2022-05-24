# fps=29
# fps_iter = []
# f = 1
# for p in range(fps):
#     # print(p)
#     if f <= fps:
#         fps_iter.append(p)
#         f += 1
# print(fps_iter)
# for f in fps_iter:
#     print(f)


# import numpy as np
# a = np.array([[1,2,3],[4,5,6]])
# print(a)

# REGEX 
import re
from re import match

from jmespath import search
# s = 'gjo3df2156c'
# s = ['gjo3df2156', 'gj03lf5462']
# s = ''.join(s)

# t = bool(re.search(r'^[a-zA-Z]{2}', s))
# r = bool(re.search(r'\d{4}$',s))

# # r = bool(re.search(r'[0-9]{4}$',s))
# print(t, r)

# if t and r is True:
#     print("y")
# else: 
#     print("n")

# tl = re.findall(r'^[a-zA-Z]{2}' ,s)
# rl = re.findall(r'\d{4}$',s)
# print(tl, rl)

# st = list(filter(lambda v: match('\D$', v), s))
# # sr = re.findall('\D$', s)
# print(st)

values = ['123', '234', 'foobar']
filtered_values = list(filter(lambda v: match('^\d+$', v), values))

print(filtered_values)

list1 = ['gjo3df2156', 'gj03lf5462']

n = list(filter(lambda b: re.search(r'\d{4}$', b), list1))
m = list(filter(lambda i: re.search(r'^a-zA-Z{2}', i), list1))
print(n,m)
# (1) concatination >>
# tl = tl +rl
# print(tl)

#(2) list comprehension >>
# res_list = [y for x in [tl, rl] for y in x]
# print(res_list)

#(3) for loop >>
# for i in rl:
#     tl.append(i)
# print("list", tl)

#(4) using list.extend() to concat >>
# tl.extend(rl)
# print(tl)

# (5) using * operator to concat >>
# res_list = [*tl, *rl]
# print(res_list)

# (6) using itertools.chain() to concat >>
# import itertools
# res_list = list(itertools.chain(tl, rl))
# print(res_list)

# from datetime import datetime
# now_vid = datetime.now()
# dt_string_vid = now_vid.strftime("%S")
# print(type(dt_string_vid))
# filename = dt_string_vid+".webm"
# VIDEO_NAME = 'VID_STORE/' + filename
# print(VIDEO_NAME)

# import cv2
# # Opens the Video file
# cap= cv2.VideoCapture('/home/rao/Flask/NPA/NPA_vid/VID_STORE/1.webm')
# fps = cap.get(cv2.CAP_PROP_FPS)
# print("fps >>> ",fps) 
# i=0
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if ret == False:
#         break
#     cv2.imwrite('kang'+str(i)+'.jpg',frame)
#     i+=1

# cap.release()
# cv2.destroyAllWindows()
# 194
