# The Original data 
1. Containing 200 patients' MRI images and its annotations.
2. 4 labels: Absence of signal, Moderate stenosis, Occlusion, and Severe stenosis.
3. **Generate VOC format dataset:** 
  3.1 We selected 2815 images with xml files, including 727 Absence of signal images and its xml, 841 Moderate stenosis images and its xml, 657 Occlusion images and its xml, and 668 Severe stenosis images and its xml.
  3.2 Copy these files to ./Annotations and ./JPEGImages, respectivly. 
  3.3 Running `00_count_labels.py` to compute each labels's account.
  3.4 Running `01_check_img.py` to check images and xml files.
    ![Category distribution](./imgs/labels.jpg)
  3.5 Then we splited taining set and testing set mannually to ensure a balanced distribution of labels.
    3.5.1 Training set(180 patients, 2545 images and xml files): Absence of signal(650), Moderate stenosis(760), Occlusion(609), and Severe stenosis(598).
    3.5.2 Testing set(20 patients, 270 images and xml files): Absence of signal(77), Moderate stenosis(81), Occlusion(48), and Severe stenosis(70).
    3.5.3 Training set and testing set stored in ./train and ./test, respectively.
  3.6 Running `02_train_val_split.py` to split training set(90%) and validation set(10%) randomly from training set.
  3.7 Running `03_gene_test_txt.py` to generate test.txt in ./ImageSets/Main
