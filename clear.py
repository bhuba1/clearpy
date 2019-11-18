import shutil
import os
import getpass

# Name of the current user
user = getpass.getuser()

# Path for temp directory
path = f'C:/Users/{user}/AppData/Local/Temp'


def getDirs():
	return [x[0] for x in os.walk(path)]


def deleteFolder(folder):
	if (os.path.isdir(folder)):
		shutil.rmtree(folder)


def deleteFile(file):
	if (os.path.isfile(file)):
		os.remove(file)


def deleteAll(path):
	#dirs = [x[0] for x in os.walk(path)]
	for root, dirs, files in os.walk(path, topdown=True):
		for name in files:
			try:
				deleteFile(os.path.join(root, name))
			except Exception as e:
				continue

		for name in dirs:
			try:
				deleteFolder(os.path.join(root, name))
			except Exception as e:
				continue

	
def main():
	deleteAll(path)
	print(f'Done cleaning for user: {user}')

	os.startfile(path)


if __name__ == '__main__':
	main()