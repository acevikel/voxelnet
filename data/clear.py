import os
clear_dir="/home/acevikel/kitti_dataset/training/velodyne/"
#remove all old files
for fname in os.listdir(clear_dir):
    if len(fname)>=2 and fname[0:2]=="00": 
        os.remove(clear_dir+fname)
        ln+=1
#rename all new files back to old name
for fname in os.listdir(clear_dir):
    new_name = ("0"*(10-len(fname)))+fname
    os.rename(clear_dir+fname,clear_dir+new_name)


