import cv2 as cv
import numpy as np



class TemplateMarching:

    def __init__(self,p_temp,p_img) -> None:
        self.temp = p_temp;
        self.img = p_img;
        pass

    def read_show (self):
         self.image=cv.imread(self.img)
         self.image = cv.cvtColor(self.image,cv.COLOR_BGR2GRAY)
         self.tempalate = cv.imread(self.temp)
         self.tempalate = cv.cvtColor(self.tempalate,cv.COLOR_BGR2GRAY)

         cv.imshow(self.image)
         cv.imshow(self.tempalate)





if __name__ == _