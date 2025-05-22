import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0,maxHands=1)

while True:
    success, img = cap.read()
    # Detecting the hand
    img = detector.findHands(img)
    # Get the list of hand landmarks positions
    lmList, bbox = detector.findPosition(img,draw=False)
    if lmList:
        # Finding the hand type
        handType = detector.handType()
        cv2.putText(img,handType,(50,50),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)
    cv2.imshow("Camera Feed",img)
    cv2.waitKey(1)