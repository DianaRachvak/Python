#moves files from one directory to another

import os, glob, shutil

dest1 = 'C:/Users/diana_000/Python'
os.chdir("C:/Users/diana_000")
for file in glob.glob("*.py"):
	print(file) #just to see which files are being moved
	shutil.move(file, dest1)