from PIL import Image
from math import sqrt
import os
from math import fabs
def main():
    # inPath = raw_input("Enter the input image file path: ")

    # path to uncleaned images
    path = "C:\\Users\\Akash\\Desktop\\video_dance\\480\\"
    # path where to store cleaned images
    dest = "dataset\\480_cleaned_14k_800x480"



    # dest = "C:\\Users\\Akash\\Desktop\\video_dance\\480_cleaned\\"
    # path = "C:\\Users\\Akash\\Desktop\\video_dance\\temp\\"
    # dest = "C:\\Users\\Akash\\Desktop\\video_dance\\temp\\00"
    
    skip=0
    files = []
    i =0
    for file in os.listdir(path):

        i+=1
        if i>=skip:
            i=0
            img_path=path+file
            image = Image.open(img_path)
            if image.mode != 'RGB':
                image = image.convert('RGB')
            changeColor(image,dest,file)

def distance(p1,p2):
    # d = (p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2
    d = fabs((p1[0]-p2[0])+(p1[1]-p2[1])+(p1[2]-p2[2]))
    return d
    # return sqrt(d)

def changeColor(image, dest,file):
    # f=open('v.txt','w')
    pixels = image.load()
    black=(0,0,0)
    for row in range(image.size[0]):
        # f.write('\n')
        for col in range(image.size[1]):
            # f.write(str(sum(list(pixels[row,col]))/3)+str('\t'))
            if distance(pixels[row, col] ,black) >230: #if not total white
                pixels[row, col] = (255, 255, 255) #change to transparent
            else :
                pixels[row, col] = black
    print ("Saving Image")
    image.save(dest + file )
    print ("Image saved at " + dest + file)

if  __name__ =='__main__':
    main()
