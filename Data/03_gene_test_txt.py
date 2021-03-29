<<<<<<< HEAD
import os,sys
path = './test'
test_list = os.listdir(path)

ftest = open('./ImageSets/Main/test.txt', 'w')
for test in test_list:
    test = test.split('.')[0]+'\n'
    ftest.write(test)
print('DONE!')
=======
import os,sys
path = './test'
test_list = os.listdir(path)

ftest = open('./ImageSets/Main/test.txt', 'w')
for test in test_list:
    test = test.split('.')[0]+'\n'
    ftest.write(test)
print('DONE!')
>>>>>>> 796f28161cba95a0360baad6bc32d165d7168b3c
