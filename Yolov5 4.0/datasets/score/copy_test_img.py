import os
import shutil

new_path = './images/test/'
filename = "score_test.txt"
f = open(filename,'r')
for item in f:
    src = item.split('\n')[0]
    jpg = item.split('.')[0].split('/')[-1]
    dst = new_path+jpg+'.jpg'
    shutil.copyfile(src,dst)
    print(item)
print('ok')
