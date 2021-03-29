import os
import shutil

new_path_lists = ['./COCO/train2021/','./COCO/val2021/','./COCO/test2021/']
filename_lists = ['./VOC/ImageSets/Main/train.txt','./VOC/ImageSets/Main/val.txt','./VOC/ImageSets/Main/test.txt']

for new_path,filename in zip(new_path_lists,filename_lists):
    #print(new_path)
    f = open(filename,'r')
    for item in f:
        name = item.split('\n')[0]
        dst = new_path+name+'.jpg'
        print(dst)
        src = './VOC/JPEGImages/'+name+'.jpg'
        print(src)
        shutil.copyfile(src,dst)
print('ok')
