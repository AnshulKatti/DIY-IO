import cv2

cap=cv2.VideoCapture(0)
detector=cv2.QRCodeDetector()


while True:
    ret,img=cap.read()
    res,_,image2=detector.detectAndDecode(img)
    if res:
        print(res)
    if ret:
        cv2.imshow('video',img)
    cv2.waitKey(1)