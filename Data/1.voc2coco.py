import sys
import os
import json
import xml.etree.ElementTree as ET

START_BOUNDING_BOX_ID = 1

PRE_DEFINE_CATEGORIES = {}


def get(root, name):
    vars = root.findall(name)
    return vars


def get_and_check(root, name, length):
    vars = root.findall(name)
    if len(vars) == 0:
        raise NotImplementedError('Can not find %s in %s.' % (name, root.tag))
    if length > 0 and len(vars) != length:
        raise NotImplementedError('The size of %s is supposed to be %d, but is %d.' % (name, length, len(vars)))
    if length == 1:
        vars = vars[0]
    return vars


def get_filename_as_int(filename):
    try:
        filename = os.path.splitext(filename)[0]
        return int(filename)
    except:
        raise NotImplementedError('Filename %s is supposed to be an integer.' % (filename))


def convert(anno_path, xml_dir, json_file):
    xmlFiles = open(xml_dir,"r")

    json_dict = {"info": {}, "images": [], "type": "instances", "annotations": [],
                 "categories": []}
    
    json_dict['info'] = {'version': '1.0', 'year': 2021, 'contributor': 'Guanru Tan', 'date_created': '2021/03/29'}
    categories = PRE_DEFINE_CATEGORIES
    bnd_id = START_BOUNDING_BOX_ID
    num = 0
    for line in xmlFiles:
        line = line.split('\n')[0]
        # print("Processing %s"%(line))
        num += 1
#         if num % 50 == 0:
#             print("processing ", num, "; file ", line)

        xml_f = anno_path + line + '.xml'
        tree = ET.parse(xml_f)
        root = tree.getroot()
        
        filename = line
        # image_id = get_filename_as_int(filename)
        image_id = filename
        size = get_and_check(root, 'size', 1)
        width = int(get_and_check(size, 'width', 1).text)
        height = int(get_and_check(size, 'height', 1).text)
        # image = {'file_name': filename, 'height': height, 'width': width,
        #          'id':image_id}
        image = {'file_name': (filename + '.jpg'), 'height': height, 'width': width,
                 'id': image_id}
        json_dict['images'].append(image)
        ## Cruuently we do not support segmentation
        #  segmented = get_and_check(root, 'segmented', 1).text
        #  assert segmented == '0'
        for obj in get(root, 'object'):
            category = get_and_check(obj, 'name', 1).text
            if category not in categories:
                new_id = len(categories)
                categories[category] = new_id
            category_id = categories[category]
            bndbox = get_and_check(obj, 'bndbox', 1)
            xmin = int(get_and_check(bndbox, 'xmin', 1).text) - 1
            ymin = int(get_and_check(bndbox, 'ymin', 1).text) - 1
            xmax = int(get_and_check(bndbox, 'xmax', 1).text)
            ymax = int(get_and_check(bndbox, 'ymax', 1).text)

            assert (xmax > xmin)
            assert (ymax > ymin)
            o_width = abs(xmax - xmin)
            o_height = abs(ymax - ymin)
            ann = {'area': o_width * o_height, 'iscrowd': 0, 'image_id':
                image_id, 'bbox': [xmin, ymin, o_width, o_height],
                   'category_id': category_id, 'id': bnd_id, 'ignore': 0,
                   'segmentation': []}
            json_dict['annotations'].append(ann)
            bnd_id = bnd_id + 1

    for cate, cid in categories.items():
        cat = {'supercategory': 'none', 'id': cid, 'name': cate}
        json_dict['categories'].append(cat)
        
    json_fp = open(json_file, 'w')
    json_str = json.dumps(json_dict)
    json_fp.write(json_str)
    json_fp.close()


if __name__ == '__main__':
    folder_list = ["train", "val", "test"]
    # ????????????VOC_dir??????????????????????????????????????????
    VOC_dir = "./VOC/"
    COCO_dir = "./COCO/"
    anno_path = './VOC/Annotations/'
    
    for i in folder_list:
        name_dir = VOC_dir + "ImageSets/Main/" + i + '.txt'
        folderName = 'instances_' + i + '2021'
        json_dir = COCO_dir + 'annotations/' + folderName + ".json"

        print("deal: ", folderName)
        print("xml dir: ", name_dir)
        print("json file: ", json_dir)
        
        # anno_path?????????VOC annotaions?????????
        # name_dir?????????????????????txt??????
        # json_dir??? ??????COCO json???????????????
        convert(anno_path, name_dir, json_dir)