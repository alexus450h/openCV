import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd=("D:/Tesseract/tesseract.exe")

img=cv2.imread('d:/22.png')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_data(img))
cv2.imshow('Result',img)
cv2.waitKey(0)

