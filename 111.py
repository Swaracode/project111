import os
import shutil
from_dir="C:/Users/sonal/Downloads"
list_of_files=os.listdir(from_dir)
print(list_of_files)


for file in list_of_files:
    root,extensions=os.path.splitext(file)
    print(root)
    print(extensions)