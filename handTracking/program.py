import cv2
import mediapipe as mp
import time

#Create video object
cap = cv2.VideoCapture(0);

#Create an object of hand
mpHands = mp.solutions.hands
hands = mpHands.Hands();
mpDraw = mp.solutions.drawing_utils

#Time
pTime = 0
cTime = 0

while True:
    
    # Reading video through camera
    success, img = cap.read();
    
    # hand landmarks
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    # Highlight landmarks
    if results.multi_hand_landmarks:
        for handLmk in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLmk, mpHands.HAND_CONNECTIONS)
                    
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    
          
    #print(results.multi_hand_landmarks)
    
    #Display video
    cv2.imshow("Image", img);
    key = cv2.waitKey(1);
    
    #Escape from the loop
    if  key == ord("q"):
        cap.release();
        cv2.destroyAllWindows();
        break;