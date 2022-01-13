import os
import shutil

root='/home/student/workspace_Yufei/datasets/deepGlobe/train_original'
root_val = '/home/student/workspace_Yufei/datasets/deepGlobe/crossvali'
root_test = '/home/student/workspace_Yufei/datasets/deepGlobe/offical_crossvali'
root_train='/home/student/workspace_Yufei/datasets/deepGlobe/train'

fopen_test = open('./test.txt','r')
lines_test = fopen_test.readlines()
fopen_train = open('./train.txt','r')
lines_train=fopen_train.readlines()

for line in lines_train:
    line_train_image = os.path.join(root,line.strip("\n"))
    line_train_label = line_train_image.replace('_sat.jpg', '_mask.png')
    shutil.move(line_train_image,root_train)
    shutil.move(line_train_label, root_train)
    # print(line_train_image)
    # print(line_train_label)

for line in lines_test:
    line_test_image = os.path.join(root,line.strip("\n"))
    line_test_label = line_test_image.replace('_sat.jpg', '_mask.png')
    shutil.move(line_test_image,root_test)
    shutil.move(line_test_label, root_test)