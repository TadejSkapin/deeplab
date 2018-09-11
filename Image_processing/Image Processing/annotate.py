import cv2
import os
import glob
import re
import numpy as np

class Binarize:

    def __init__(self):

        #Read options
        self.filtered = "D:\\Uni\\Python\\Filtered" #Save path for images that are suitable
        #Write options
        self.annotated = "D:\\Uni\\Python\\Annotated" #Save path for images to be annotated
        #This is the starting name. It increments.
        self.image_name = 0
        self.extension = '.png'
        #self.colour = [0, 0, 255]

##    def process(self, img):
##        if write:
##            # Save the image
##            imageName = '{num:08d}'.format(num = self.image_name) + self.extension
##            imageName = os.path.join(self.directory, imageName)
##            #print(imageName)
##            cv2.imwrite(imageName, th)
##        self.image_name += 1

    def getColour(self, num):
        if num < 80:
            #return [75, 0, 0]
            return 1
        elif num < 224:
            #return [150, 0, 0]
            return 2
        elif num < 296:
            #return [225, 0, 0]
            return 3
        elif num < 368:
            #return [0, 75, 0]
            return 4
        elif num < 384:
            #return [0, 150, 0]
            return 5
        elif num < 400:
            #return [0, 225, 0]
            return 6
        elif num < 440:
            #return [0, 0, 75]
            return 7
        elif num < 456:
            #return [0, 0, 150]
            return 8
        elif num < 488:
            #return [0, 0, 225]
            return 9
        elif num < 568:
            #return [75, 75, 0]
            return 10
        elif num < 736:
            #return [150, 75, 0]
            return 11
        elif num < 880:
            #return [225, 75, 0]
            return 12
        
    def binarize(self):
        filenames = glob.glob("Filtered/*jpg")
        images = [cv2.imread(img) for img in filenames]
        im_num = 0
        
        #for mask in images:
        for name in filenames:
            
            name = re.findall(r'\d+', name)
            num = int(name[0])
            mask = images[im_num]
            
            mask1 = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
            ret, mask1 = cv2.threshold(mask1, 127, 255, cv2.THRESH_BINARY)
            mask2 = mask1.copy()
            kernel = np.ones((5,5), np.uint8)
            mask2 = cv2.dilate(mask2, kernel, iterations = 2)
            #image = ims[num]
            #img = cv2.bitwise_and(image,image,mask = mask)
            annotated = mask2.copy()
            #annotated = cv2.cvtColor(annotated, cv2.COLOR_GRAY2BGR)
            #annotated[mask1 > 127] = self.colour
            #If we consider every box as a class
            #annotated[mask1 > 127] = self.getColour(num)
            #If we consider each lego as a class
            annotated[mask1 > 127] = np.floor(num/8) + 1
            '''
            cv2.imshow("Original mask", mask)
            cv2.imshow("Extended mask", mask2)
            '''
            cv2.imshow("Annotation area", annotated)
            cv2.waitKey(1)
            #'''
            imageName = '{num:08d}'.format(num = num) + self.extension
            imageName = os.path.join(self.annotated, imageName)
            print(imageName)
            cv2.imwrite(imageName, annotated)

            im_num += 1



if __name__ == "__main__":

    bina = Binarize()
    
    bina.binarize()
