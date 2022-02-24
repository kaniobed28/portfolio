import cv2 as cv
from cv2 import imread
img = imread(r"C:\Users\kanio\Desktop\iPortfolio\static\img\hero-bg.jpg")
img2 = imread(r"C:\Users\kanio\Desktop\iPortfolio\static\img\profile-img.jpg")

resize1 = cv.resize(img,(1920,1280))
resize2 = cv.resize(img,(600,600))

cv.imwrite(r"C:\Users\kanio\Desktop\iPortfolio\static\img\hero-bg.jpg",resize1)
cv.imwrite(r"C:\Users\kanio\Desktop\iPortfolio\static\img\profile-img.jpg",resize2)