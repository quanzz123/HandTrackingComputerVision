import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm
# Previous time
pTime = 0
# current time
cTime = 0
cap = cv2.VideoCapture(0)
dectector = htm.handDetector()
while True:
    success, img = cap.read()
    img = dectector.fineHands(img)
    lmlist = dectector.findPosition(img, draw=False)

    if len(lmlist) != 0:
        print(lmlist[4])

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

    cv2.imshow('Image', img)
    # Bấm 'q' để thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng
cap.release()
cv2.destroyAllWindows()