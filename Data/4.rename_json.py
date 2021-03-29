import os
import json

json_dirs = ["./COCO/annotations/instances_train2021.json", "./COCO/annotations/instances_val2021.json", "./COCO/annotations/instances_test2021.json"]

for json_dir in  json_dirs:
    with open(json_dir,'r',encoding = 'utf-8') as jf:
        info = json.load(jf)

        # 找到位置进行修改[images][i][id]
        for i in range(len(info['images'])):
            id_raw = info['images'][i]['id']
            id_new = id_raw.split('_')
            if len(id_new)>1:
                id_new = id_new[0]+id_new[1]+id_new[2].split('d')[0]
            else:
                id_new = id_new[0]
            id_new = int(id_new)
            info['images'][i]['id'] = id_new
            
            file_name_raw = info['images'][i]['file_name']
            file_name_new = file_name_raw.split('_')
            if len(file_name_new)>1:
                file_name_new = file_name_new[0]+file_name_new[1]+file_name_new[2].split('d')[0]+'.jpg'
            else:
                file_name_new = file_name_new[0]
            info['images'][i]['file_name'] = file_name_new
            
        # 找到位置进行修改[annotations][i][image_id]
        for i in range(len(info['annotations'])):
            id_raw = info['annotations'][i]['image_id']
            id_new = id_raw.split('_')
            if len(id_new)>1:
                id_new = id_new[0]+id_new[1]+id_new[2].split('d')[0]
            else:
                id_new = id_new[0]
            id_new = int(id_new)
            info['annotations'][i]['image_id'] = id_new
            
        # 使用新字典替换修改后的字典
        json_dict = info
        # print(json_dict) 
    # set_trace()
    # 将替换后的内容写入原文件 
    with open(json_dir,'w') as new_jf:
        json.dump(json_dict,new_jf)       

print('change name over!')

