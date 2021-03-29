https://github.com/dataxujing/yolo-v5

1.把数据集放到./datasets/myData/里

2.进入./datasets/依次运行
2.1 01_check_img.py
2.2 02_check_box.py
2.4 04_myData_label.py：会把训练集,验证集和测试集的xml文件放到./datasets/score/labels/train/,./datasets/score/labels/val/
                    和./datasets/score/labels/test/里
                    并在./datasets/score/生成score_train.txt,score_val.txt和score_test.txt
                    （PS：记得修改class2id = {'Moderate stenosis':0,'Severe stenosis':1,'Occlusion':2,'Absence of signal':3}这一行）

3.进入./datasets/score/依次运行
copy_train_img.py(记得修改要存放照片的新目标路径)
copy_val_img.py (记得修改要存放照片的新目标路径)
copy_test_img.py (记得修改要存放照片的新目标路径)
把训练图片放到./datasets/score/images/train/和./datasets/score/images/val/
copy_detect_xml.py 把测试集的xml文件复制到./runs/detect/annotations/
copy_detect_img.py 把测试集的img文件复制到./runs/detect/images/

4.修改./data/相对应的yaml文件的参数nc、names、相应的数据集路径
  修改./models/相对应的yaml文件的参数nc

5.source activate yolov5medical进入环境

6.训练
python train.py --img-size 512 --batch-size 8 --epochs 300 --data ./data/score.yaml --cfg ./models/yolov5s.yaml --weights weights/yolov5s.pt

7.查看结果
python plot_results.py 得到mAP、recall等结果
python detect.py --source ./runs/detect/images/ --weights weights/best.pt --conf 0.5 生成预测图片./runs/detect/exp(x)/

进入./runs/detect/,新建output_groundtruth文件夹，输入python add_anhors.py把ground truth画上去







#################################################################
1.修改./utils/的plots.py文件
可以修改./utils/utils.py的cv2.rectangle(img, c1, c2, color, thickness=tl, lineType=cv2.LINE_AA和cv2.putText(img, label, (c1[0], c1[1] - 2), 0, tl / 3, [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)的thickness，因为太粗了
)

2.results.txt中每一列的含义：
0:'epoch', 1:'mem', 2:'train GIoU_loss', 3:'train Objectness_loss', 4:'train Classification_loss', 
5:'total', 6:'targets', 7:'img_size', 8:'Precision', 9:'Recall',10:'mAP@0.5', 11:'mAP@0.5:0.95',
12:'val GIoU_loss', 13:'val Objectness_loss', 14:'val Classification_loss', 
15:'ap[0]', 16:'ap[1]', 17:'ap[2]', 18:'ap[3]', 19:'FP(False Positive)'

3.计算ap：train.py(test())->test.py(ap_per_class())->utils.py(compute_ap())
'class1 AP':'Moderate stenosis'
'class2 AP':'Severe stenosis'
'class3 AP':'Occlusion'
'class4 AP':'Absence of signal'

4.如果./myData/数据集损坏，可以去Datasets/Brain_MRI里找



