import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


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

         plt.imshow(self.image)
         plt.show()

         plt.imshow(self.tempalate)
         plt.show()
    def maching(self,method):
        threshold = 0.8
        method = eval(method)
        res =cv.matchTemplate(self.image, self.tempalate,method)
        loc = np.where(res >= threshold)
        w, h = self.tempalate.shape[::-1]
        for pt in zip(*loc[::-1]):
            cv.rectangle(self.image, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)
        # if (res > threshold):
        #     cv.rectangle(self.image, top_left, bottom_right, (0,255,0),6)
        plt.imshow(self.image)
        plt.show()
if __name__ == '__main__':    
    tamplate_maching = TemplateMarching("./tamplate.jpg","./img.jpg")
    tamplate_maching.read_show()
    methods =["cv.TM_CCOEFF" ,
     "cv.TM_CCOEFF_NORMED",
     "cv.TM_CCORR" ,
     "cv.TM_CCORR_NORMED" ,
     "cv.TM_SQDIFF" ,
     "cv.TM_SQDIFF_NORMED"]
    tamplate_maching.maching(methods[5])

