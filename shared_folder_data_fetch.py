import os 
import time
from os import listdir
from os.path import isdir, join

src_dir = r"\\10.0.56.14\Images\PlatformTesting\FW_Versions\Quattro"

dir_list = []


for f in listdir(src_dir):
	sub_file = join(src_dir, f)
	if isdir(sub_file):
		dir_list.append(sub_file)


def sort_on_time(sub_file):
	return time.time() - os.path.getctime(sub_file)

dir_list.sort(key = sort_on_time)  

for folder in dir_list:
	print(folder)
	print(time.time() - os.path.getctime(folder))