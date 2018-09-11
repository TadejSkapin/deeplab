import cv2
import os
import glob
import re
import numpy as np

class Binarize:

    def __init__(self):

        #Read options
        self.read = "D:\\Uni\\Python\\Images"
        #Save options
        self.directory = "D:\\Uni\\Python\\Binarized"
        self.filtered = "D:\\Uni\\Python\\Filtered" #Save path for images that are suitable
        self.annotated = "D:\\Uni\\Python\\Annotated" #Save path for images to be annotated
        #This is the starting name. It increments.
        self.image_name = 0
        self.extension = '.jpg'

    def process(self, img):
        # Read image
        cv2.imshow('Image',img)
        cv2.waitKey(1)

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Convert to HLS
        image_hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
        #image_hls = cv2.GaussianBlur(image_hls,(3,3),0)
        hue, lightness, saturation = np.split(image_hls, 3, axis=2)
        #hue = hue.reshape((hue.shape[0], hue.shape[1]))

        '''
        cv2.imshow('Hue',hue)
        cv2.waitKey(1)

        cv2.imshow('Lightness',lightness)
        cv2.waitKey(1)

        cv2.imshow('Saturation',saturation)
        cv2.waitKey(1)
        '''
        
        th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        #gray = cv2.GaussianBlur(gray,(3,3),0)

        write = self.checkQuality(th)
        
        # Threshold the image
        #ret, th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        #th = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 2)
        cv2.imshow('Binary', th)
        cv2.waitKey(1)
        '''
        # Clean the image up using morphological operations
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(4,4))
        clean = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)
        cv2.imshow('Cleaned', clean)
        cv2.waitKey(1)
        '''
        if write:
            # Save the image
            imageName = '{num:08d}'.format(num = self.image_name) + self.extension
            imageName = os.path.join(self.directory, imageName)
            #print(imageName)
            cv2.imwrite(imageName, th)
        self.image_name += 1

    def binarize(self):
        #ret, frame = self.camera.read()
        #cv2.imshow(self.window_name, frame)
        #cv2.waitKey(1)
        #print(frame.shape)
        #frame_cut = frame[112:368, 192:448, :]
        #cv2.imshow('cut', frame_cut)
        #cv2.waitKey(1)
        '''
        if cv2.waitKey(1) == ord('p'):
            imageName = '{num:08d}'.format(num = self.image_name) + self.extension
            imageName = os.path.join(self.directory, imageName)
            print(imageName)
            cv2.imwrite(imageName, frame_cut)
            self.image_name += 1
        '''
        #filenames = glob.glob("Images/*.jpg")
        filenames = glob.glob("Binarized/*jpg")
        images = [cv2.imread(img) for img in filenames]

        
        for img in images:
            self.process(img)
        #    self.filter(img)

        #self.process(images[1])
        #print(self.checkQuality(images[777]))
        #manualImage = 680
        #self.filterManual(images[manualImage], manualImage) 

        return 0

    # Filters out unusable images
    def filter(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        pixelsIn = img.shape[0] * img.shape[1]
        pixelsWhite = sum(sum(img > 1))
        #print(pixelsIn, pixelsWhite, pixelsIn - pixelsWhite, pixelsWhite/pixelsIn)
        if (pixelsWhite/pixelsIn > 0.9):
            # Invert the mask
            img = np.ones((img.shape[0], img.shape[1]), dtype=np.int8)*255 - img
            # Save the image
            imageName = '{num:08d}'.format(num = self.image_name) + self.extension
            imageName = os.path.join(self.filtered, imageName)
            cv2.imwrite(imageName, img)
        elif (pixelsWhite/pixelsIn < 0.1):
            # Save the image
            imageName = '{num:08d}'.format(num = self.image_name) + self.extension
            imageName = os.path.join(self.filtered, imageName)
            cv2.imwrite(imageName, img)
        self.image_name += 1

    # Manual override on filter
    def filterManual(self, img, imgNum):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        pixelsIn = img.shape[0] * img.shape[1]
        pixelsWhite = sum(sum(img > 1))
        #print(pixelsIn, pixelsWhite, pixelsIn - pixelsWhite, pixelsWhite/pixelsIn)
        if (pixelsWhite/pixelsIn > 0.5):
            # Invert the mask
            img = np.ones((img.shape[0], img.shape[1]), dtype=np.int8)*255 - img
        # Save the image
        imageName = '{num:08d}'.format(num = imgNum) + self.extension
        imageName = os.path.join(self.filtered, imageName)
        cv2.imwrite(imageName, img)

    # Checks the ratio between black and white pixels in a gray-scale image
    def checkQuality(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        pixelsIn = img.shape[0] * img.shape[1]
        pixelsWhite = sum(sum(img > 1))
        print(pixelsIn, pixelsWhite, pixelsIn - pixelsWhite, pixelsWhite/pixelsIn)
        if (pixelsWhite/pixelsIn > 0.9):
            #print(True)
            return True
        elif (pixelsWhite/pixelsIn < 0.1):
            #print(True)
            return True
        else:
            #print(False)
            return False

if __name__ == "__main__":

    bina = Binarize()
    
    bina.binarize()
