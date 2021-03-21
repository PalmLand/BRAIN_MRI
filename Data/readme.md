# The Original data 
1. Containing 200 patients' MRI images and its annotations.
2. 4 labels: Absence of signal, Moderate stenosis, Occlusion, and Severe stenosis.
3. **Generate VOC format dataset:** 
  * We selected 2815 images with xml files, including 727 Absence of signal images and its xml, 841 Moderate stenosis images and its xml, 657 Occlusion images and its xml, and 668 Severe stenosis images and its xml.
  * Copy these files to ./Annotations and ./JPEGImages, respectivly. 
  * Running `00_count_labels.py` to compute each labels's account.
  * Running `01_check_img.py` to check images and xml files.
    ![Category distribution](./imgs/labels.jpg =50*50)
  * Then we splited taining set and testing set mannually to ensure a balanced distribution of labels.
    * Training set(180 patients, 2545 images and xml files): Absence of signal(650), Moderate stenosis(760), Occlusion(609), and Severe stenosis(598).
    * Testing set(20 patients, 270 images and xml files): Absence of signal(77), Moderate stenosis(81), Occlusion(48), and Severe stenosis(70).
    * Training set and testing set stored in ./train and ./test, respectively.
  * Running `02_train_val_split.py` to split training set(90%) and validation set(10%) randomly from **training set**, generating train.txt and test.txt in ./ImageSets/Main.
  * Running `03_gene_test_txt.py` to generate test.txt in ./ImageSets/Main

**file tree**
```
./Annotations
./ImagesSets
    |__Main
        |_train.txt,val.txt,test.txt
./JPEGImages
./train
./test
```
