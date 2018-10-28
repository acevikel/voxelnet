import os
import sys

#CHANGE THIS
data_dir = "/home/acevikel/kitti_dataset/"
########################################


def make_directory_safe(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def split_subdir(subdir,protocol):
    cur_dir = data_dir+"training/"+subdir+"/"
    for fname in os.listdir(cur_dir):
        if fname.split(".")[0] in protocol: 
            os.rename(cur_dir+fname,data_dir+"validation/"+subdir+"/"+fname)



#create directories accordingly
make_directory_safe(data_dir+"validation")
make_directory_safe(data_dir+"validation/image_2")
make_directory_safe(data_dir+"validation/label_2")
make_directory_safe(data_dir+"validation/velodyne")

#exit if val.txt not present
try:
    val = open("val.txt","r").read().split()
except:
    print "Split protocol file val.txt does not exists or invalid, please put that file in to voxelnet/data folder"
    sys.exit()

split_subdir("image_2",val)
split_subdir("label_2",val)
split_subdir("velodyne",val)