import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
import shutil
from scipy import ndimage
from skimage.filters import threshold_otsu
import scipy

debug = True

shutil.rmtree('outputs', ignore_errors=True)

output_folder = "./outputs" 
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#Plotting different histograms
def plothist(fnamePath, fnameList, method):
    plt.figure()
    for fname in fnameList:
        img = eval(method)
        hist, bin_edges = np.histogram(img.ravel(),256,[0,255])
        plt.plot(hist)
    plt.legend(fnames)

#grayscale conversion
def readImgAsGray(fnamePath, fname):
    return cv2.imread(fnamePath+fname, 0)

#median filtering
def getMedFilteredImg(fnamePath, fname, size=5):
    img = readImgAsGray(fnamePath, fname)
    h, w = img.shape
    img = cv2.resize(img, (w//2, h//2), interpolation=cv2.INTER_NEAREST)
    stdImg = ndimage.median_filter(img, size=size)
    medianFiltered = np.abs(img.astype('float32')-stdImg.astype('float32'))
    return medianFiltered.astype('uint8')

#edge detection (canny edge detector)
def edgeDetection(fnamePath, fnameList):
    for fname in fnameList: 
        img = readImgAsGray(fnamePath, fname)
        edges = cv2.Canny(img,100,200)
        plt.subplot(121),plt.imshow(img,cmap = 'gray')
        plt.title('Original Image' + '(' + str(fname.split('.png')[0]) + ')'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(edges,cmap = 'gray')
        plt.title('Edge Image' + '(' + str(fname.split('.png')[0]) + ')'), plt.xticks([]), plt.yticks([])
        plt.savefig('./outputs/edge_detection' + '_' + str(fname.split('.png')[0]) + '.png')
        plt.show()

#thresholding(Otsu's method)
def getThreshold(fnamePath, fnameList):
    for fname in fnameList:
        img = readImgAsGray(fnamePath, fname)
        thresh = threshold_otsu(img)
        binary = img > thresh 
        fig, axes = plt.subplots(ncols=3, figsize=(12, 5))
        ax = axes.ravel()
        ax[0] = plt.subplot(1, 3, 1, adjustable='box')
        ax[1] = plt.subplot(1, 3, 2)
        ax[2] = plt.subplot(1, 3, 3, sharex=ax[0], sharey=ax[0], adjustable='box')

        ax[0].imshow(img, cmap=plt.cm.gray)
        ax[0].set_title('Original' + '(' + str(fname.split('.png')[0]) + ')')
        ax[0].axis('off')

        ax[1].hist(img.ravel(), bins=256)
        ax[1].set_title('Histogram' + '(' + str(fname.split('.png')[0]) + ')')
        ax[1].axvline(thresh, color='r')
        ax[1].set_xlabel('Grayscale values')
        ax[1].set_ylabel('Pixel counts')

        ax[2].imshow(binary, cmap=plt.cm.gray)
        ax[2].set_title('Thresholded' + '(' + str(fname.split('.png')[0]) + ')')
        ax[2].axis('off')
        plt.savefig('./outputs/thresholding' + '_' + str(fname.split('.png')[0]) + '.png')
        plt.show()
        

imgPath = r'.\experiment\\'
fnames = [fname for fname in os.listdir(imgPath)]

method_0 = 'readImgAsGray(fnamePath, fname)'
plothist(imgPath, fnames, method_0)
plt.title('Histogram of Grayscale Values')
plt.xlabel('Grayscale values')
plt.ylabel('Pixel counts')
plt.savefig('./outputs/histogram_grayscale.png', dpi=300)
plt.show()


method_1 = 'getMedFilteredImg(fnamePath, fname)'
plothist(imgPath, fnames, method_1)
plt.title('Histogram of Median Filtered Image')
plt.xlabel('Grayscale values')
plt.ylabel('Pixel counts')
plt.savefig('./outputs/histogram_median_filtered.png', dpi=300)
plt.show()

getThreshold(imgPath, fnames)

edgeDetection(imgPath, fnames)