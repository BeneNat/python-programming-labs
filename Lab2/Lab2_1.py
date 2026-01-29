import os

#print(os.listdir("C:\\My_Designs"))
path = "C:\\My_Designs"
files = os.listdir(path)
print(f"Number of elements in {path}: {len(files)}")