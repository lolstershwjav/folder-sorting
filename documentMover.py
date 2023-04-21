import os
import shutil

source = "C:/Users/abhij/downloads"
destination = "C:/Users/abhij/desktop"

files = os.listdir(source)

for i in files:
    name, extention = os.path.splitext(i)
    if extention == "":
        continue
    if extention in [".pdf", ".doc", ".txt", ".docx"]:
        path1 = source + "/" + i
        createFile = destination + "/" + "Documents_Folder"
        moveFile =  destination + "/" + "Documents_Folder" + "/" + i
    
        if os.path.exists(createFile):
            print("Moving "+i)
            shutil.move(path1, moveFile)
            
        else:
            os.makedirs(createFile)
            print("Moving "+i)
            shutil.move(path1, moveFile)