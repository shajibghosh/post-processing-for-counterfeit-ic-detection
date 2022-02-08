"""Create a folder in the working directory called 'img_TIF' """
"""Put all the .TIF images that you want to convert to .PNG (or .JPG) in the 'img_TIF' folder."""
from PIL import Image
import os
import shutil 

shutil.rmtree('img_PNG', ignore_errors=True)
shutil.rmtree('img_JPG', ignore_errors=True)

print("\nPlease mention which one of the following operations you want (insert '1' or '2'): \n")
print("1. .TIF to .PNG (recommended).\n")
print("2. .TIF to .JPG.\n")

while True:
    try:
        choice = input()
    except ValueError:
        print("Sorry, Invalid Choice. Please try again.")
        continue
    if choice == '1':
        TargetFolderName = 'img_PNG'
        break
    elif choice == '2':
        TargetFolderName = 'img_JPG'
        break
    else: 
        print("Sorry, your response must be either '1' or '2'. Please try again.")
        continue 

SourceFolder="./img_TIF" 
TargetFolder="./" +  TargetFolderName 
if not os.path.exists(TargetFolder):
    os.makedirs(TargetFolder)

for file in os.listdir(SourceFolder):
    SourceFile=SourceFolder + "/" + file
    img = Image.open(SourceFile)
    TargetFileType = str("." + TargetFolderName.split('_')[1]) 
    TargetFile=TargetFolder + "/" + file.replace(".TIF",TargetFileType)
    img.save(TargetFile)
print("\nProcess Completed. Source images are converted to .TIF to "+  TargetFileType + " format.\n")