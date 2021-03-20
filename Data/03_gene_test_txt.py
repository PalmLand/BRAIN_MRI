import os,sys
path = './test'
test_list = os.listdir(path)

ftest = open('./ImageSets/Main/test.txt', 'w')
for test in test_list:
    test = test.split('.')[0]+'\n'
    ftest.write(test)
print('DONE!')
