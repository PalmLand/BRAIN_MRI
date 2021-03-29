<<<<<<< HEAD
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
    src = './images/test/%s.jpg'%(image_id)
    dst = '../../runs/detect/images/%s.jpg'%(image_id)
    shutil.copyfile(src,dst)
    print(image_id)
print('ok')
=======
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
    src = './images/test/%s.jpg'%(image_id)
    dst = '../../runs/detect/images/%s.jpg'%(image_id)
    shutil.copyfile(src,dst)
    print(image_id)
print('ok')
>>>>>>> 796f28161cba95a0360baad6bc32d165d7168b3c
