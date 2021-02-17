import cv2
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

def domIntensity(im, k):
    #YOUR CODE STARTS HERE
    h = im.shape[0]
    w = im.shape[1]

    freq = np.array([0]*256)
    color_r=[[0]*3]*256

    # loop over the image, pixel by pixel
    for x in range(0, h):
        for y in range(0, w):
            index=int((im[x,y][0]+im[x,y][1]+im[x,y][2])/3)
            freq[index]+=1
            if(color_r[index]==0):
                color_r[index]=[im[x,y][0],im[x,y][1],im[x,y][2]]
            else:
                color_r[index]=[int((color_r[index][0]+im[x,y][0])/2),int((color_r[index][1]+im[x,y][1])/2),int((color_r[index][2]+im[x,y][2])/2)]

    intensities=np.argsort(freq)
    intensities=intensities[::-1]
    sorted_intensities=[[0]*3]*256

    for i in range (256):
        sorted_intensities[i]=color_r[intensities[i]]
        
    #YOUR CODE ENDS HERE
    return sorted_intensities[:k]

def displayIntensityPalette(im, dom_list):
    plt.figure()
    if len(im.shape) == 2:
        plt.imshow(im, cmap = "gray")
    else:
        plt.imshow(im)
    plt.xticks([])
    plt.yticks([])
    plt.title("Given input image")
    k = len(dom_list)
    # Most dominant intensity
    top_im = np.array([[list(dom_list[0])]])
    plt.figure(figsize = (0.75,0.75), frameon=False)
    plt.imshow(top_im)
    plt.title('Dominent intensity shade')
    plt.xticks([])
    plt.yticks([])
    # k most dominant intensity palette
    plt.figure(figsize = ((0.75*k),0.75), frameon=False)
    dom_inty_im = np.array([[list(dom_list[i]) for i in range(k)]])
    plt.imshow(dom_inty_im)
    plt.xticks([])
    plt.yticks([])
    plt.title("Top 10 intensity Palette ")

im = cv2.imread("C:\\Users\\Sanchita\\Desktop\\IVP_Assignment1\\lena_gray_256.tif")
dom_list = domIntensity(im,10)
displayIntensityPalette(im, dom_list)
