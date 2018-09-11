import cv2
import os
import glob
import re
import numpy as np

class Convert:

    def __init__(self):

        #Read options
        self.read = "D:\\Uni\\Python\\Annotated"
        #Save options
        self.directory = "D:\\Uni\\Python\\Converted"
        self.image_name = 0 #This is the starting name. It increments.
        self.extension = '.jpg'
        
    def convert(self, ext):
        filenames = glob.glob("Annotated/*jpg")
        images = [cv2.imread(img) for img in filenames]
        i = 0

        #for mask in images:
        for name in filenames:
            
            name = re.findall(r'\d+', name)
            num = int(name[0])
            
            imageName = '{num:08d}'.format(num = num) + ext
            imageName = os.path.join(self.directory, imageName)
            print(imageName)
            cv2.imwrite(imageName, images[i])
            i += 1
            



if __name__ == "__main__":

    conv = Convert()
    
    conv.convert('.png')
