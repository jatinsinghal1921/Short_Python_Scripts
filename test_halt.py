import shutil
import os

src_path = r"\\10.66.80.163\share\jatin\nvmekit"
des_path = os.path.join(os.getcwd(),"nvmekit")
file = "20110006.fluf"


def copyFile(src, des):
	shutil.copyfile(os.path.join(src,file), os.path.join(des,file))


def copyDirectory(src, dest):
    try:
        shutil.copytree(src, dest)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)


def main():
	# Copying Directory
	copyDirectory(src_path,des_path)
	return


if __name__ == "__main__":
	main()