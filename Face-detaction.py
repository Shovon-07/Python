import cv2

'''___ View image ___'''
# img = cv2.imread("/home/shovon/Pictures/My-Pic/clg-main-for-admit.jpg")

# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray,(99,99),0)

# # cv2.imshow("Gray image",imgGray)
# cv2.imshow("Blur image",imgBlur)
# cv2.waitKey(0)

'''___ View video ___'''
captureVideo = cv2.VideoCapture(0)

while True :
    myVid, img = captureVideo.read()
    cv2.imshow("Video",img)
    if(cv2.waitKey(1) & 0xFF == ord("q")) :
        break