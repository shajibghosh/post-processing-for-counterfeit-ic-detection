"""Create two folders in the working directory. The folders are: 1. img_TIF, 2. img_PNG (or img_JPG)."""
"""Put all the .TIF images that you want to convert to .PNG (or .JPG) in the 1st folder."""
from PIL import Image
import os

SourceFolder="./img_TIF" 
TargetFolder="./img_PNG" #if you want to convert from .tif to .png
#TargetFolder="./img_JPG" #if you want to convert from .tif to .jpg

for file in os.listdir(SourceFolder):
    SourceFile=SourceFolder + "/" + file
    img = Image.open(SourceFile)
    TargetFile=TargetFolder + "/" + file.replace(".TIF",".PNG") #if you want to convert from .tif to .png
    #TargetFile=TargetFolder + "/" + file.replace(".TIF",".JPG") #if you want to convert from .tif to .jpg
    img.save(TargetFile)