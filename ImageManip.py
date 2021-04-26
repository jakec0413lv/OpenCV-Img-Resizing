import cv2
from pathlib import Path
import glob

#img = cv2.imread("galaxy.jpg",  0) #1 = rgb, 0 = grey-scale, -1 = rgba [transparency capabilities]

#print(img)#Numpy array of pixels
#print(img.shape) #Img resolution

#resized_image = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2))) #Resize with ratio relative to original
#cv2.imshow("Galaxy", resized_image) #Window Title, img object
#cv2.imwrite("Galaxy_resized.jpg", resized_image) #Save new image
#cv2.waitKey(0) #Any button will close window
#cv2.waitKey(2000) #Destroy after 2 seconds
#cv2.destroyAllWindows()

#Extract File Names
filenames = glob.glob("Photos/*.jpg") 

#Resize and Save All Photos to 100 x 100 Resolution

for file in filenames:
    #Import Img
    img = cv2.imread(file, 1)

    #Parse photo name for renaming
    photoName = file[7:]

    #Resize Img
    resized_image = cv2.resize(img, (100, 100)) #Resize to 100 x 100
    
    #Show Original Img
    cv2.imshow(photoName, img)
    cv2.waitKey(2000) 
    cv2.destroyAllWindows()
    
    #Show preview of resized image
    cv2.imshow(photoName, resized_image)

    #Save photo under new folder /ResizedPhotos
    cv2.imwrite("ResizedPhotos/resized_" + photoName, resized_image) 

    #Display Img for 2 Seconds
    cv2.waitKey(2000) 
    cv2.destroyAllWindows()

