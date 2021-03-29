<<<<<<< HEAD
import os
import random

xmlfilepath = './train'
txtsavepath = './ImageSets/Main'
total_xml = os.listdir(xmlfilepath)

#trainval_percent=0.9# 表示余下的百分之十用于test 
#train_percent=1 # 表示训练集中用于训练，没有用于验证
train_percent = 0.9     

num = len(total_xml)
lists = range(num)

tr = int(num*train_percent)         
train = random.sample(lists,tr)  

ftrain = open('./ImageSets/Main/train.txt', 'w')
fval = open('./ImageSets/Main/val.txt', 'w')
 
for i in lists:
    name = total_xml[i][:-4] + '\n'
    if i in train:
        ftrain.write(name)
    else:
        fval.write(name)

ftrain.close()  
fval.close()  

# voc Main/train,val 图像名生成
=======
import os
import random

xmlfilepath = './train'
txtsavepath = './ImageSets/Main'
total_xml = os.listdir(xmlfilepath)

#trainval_percent=0.9# 表示余下的百分之十用于test 
#train_percent=1 # 表示训练集中用于训练，没有用于验证
train_percent = 0.9     

num = len(total_xml)
lists = range(num)

tr = int(num*train_percent)         
train = random.sample(lists,tr)  

ftrain = open('./ImageSets/Main/train.txt', 'w')
fval = open('./ImageSets/Main/val.txt', 'w')
 
for i in lists:
    name = total_xml[i][:-4] + '\n'
    if i in train:
        ftrain.write(name)
    else:
        fval.write(name)

ftrain.close()  
fval.close()  

# voc Main/train,val 图像名生成
>>>>>>> 796f28161cba95a0360baad6bc32d165d7168b3c
