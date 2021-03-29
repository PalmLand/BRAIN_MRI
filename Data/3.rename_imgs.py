import os, sys

# rename images name
img_lists = ['./COCO/train2021/','./COCO/test2021/','./COCO/val2021/']
for img_path in img_lists:
    file_lists = os.listdir(img_path)
    # print(len(file_lists))
    for img_name in file_lists:
        img_name_new = img_name.split('_')
        if len(img_name_new)>1:
            img_name_new = img_name_new[0]+img_name_new[1]+img_name_new[2].split('d')[0]+'.jpg'
        else:
            img_name_new = img_name_new[0]
        # print(img_name_new)
        os.rename(img_path+img_name,img_path+img_name_new)
        
print('DONE!')        