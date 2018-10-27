import os
clear_dir="/home/acevikel/kitti_dataset/training/velodyne/"
ln =0
for fname in os.listdir(clear_dir):
    new_name = ("0"*(10-len(fname)))+fname
    os.rename(clear_dir+fname,clear_dir+new_name)

print ("total : ",ln)