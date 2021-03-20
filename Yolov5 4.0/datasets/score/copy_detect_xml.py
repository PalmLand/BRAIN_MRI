import os
import shutil

'''
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
'''

image_ids = open('../myData/ImageSets/Main/test.txt').read().strip().split()
for image_id in image_ids:
    src = '../myData/Annotations/%s.xml'%(image_id)
    dst = '../../runs/detect/annotations/%s.xml'%(image_id)
    shutil.copyfile(src,dst)
    print(image_id)
print('ok')
