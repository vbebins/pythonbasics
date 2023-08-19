import os

#to get the current directory
print('current working directory is',os.getcwd())

#to list all files in the directory
print(os.listdir())

#to check file/pth exists or not
print(os.path.exists("osmoduleeg.py"))

#to check file/path size
print(os.path.getsize("osmoduleeg.py"))