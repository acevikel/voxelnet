import os
clear_dir="/home/acevikel/kitti_dataset/training/velodyne/"
ln =0
for fname in os.listdir(clear_dir):
    if len(fname)>=2 and fname[0:2]=="00": 
        os.remove(clear_dir+fname)
        ln+=1
print ("total : ",ln)