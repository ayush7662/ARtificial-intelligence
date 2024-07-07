import cv2
#import imutils
img = cv2.imread("sample4.jpg")
#resizeImg = imutils.resize(img,width = 20)
#cv2.imwrite("resizedImage.jpg",resizeImg)
#gaussianBlurImg = cv2.GaussianBlur(img,(21,21),0)
#cv2.imwrite("gaussianBlurImg.jpg",gaussianBlurImg)

grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thresImg = cv2.threshold(grayImg,80,225,cv2.THRESH_BINARY)[1]
cv2.imwrite("thresholdImage.jpg",thresImg)