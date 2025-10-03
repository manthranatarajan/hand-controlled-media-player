import cv2 
import mediapipe as mp
import pyautogui
import time

# implement the logic to detect which finger is up
def count_fingers(lst):
    count = 0 # tracking the number of fingers up

    # wrist to middle finger MCP joint distance (accounts for distance from camera)
    thresh = (lst.landmark[0].y*100 - lst.landmark[9].y*100)/2

    # Check if each finger is up by comparing the y-coordinates of the fingertip and the PIP joint
    # pointer finger
    if (lst.landmark[5].y*100 - lst.landmark[8].y*100) > thresh:
        count += 1

    # middle finger
    if (lst.landmark[9].y*100 - lst.landmark[12].y*100) > thresh:
        count += 1

    # ring finger
    if (lst.landmark[13].y*100 - lst.landmark[16].y*100) > thresh:
        count += 1

    # pinky finger
    if (lst.landmark[17].y*100 - lst.landmark[20].y*100) > thresh:
        count += 1

    # thumb - simple heuristic: compare x coordinates because thumb extends sideways. instead of points 2 and 4, use 5 and 4
    if (lst.landmark[5].x*100 - lst.landmark[4].x*100) > 6:
        count += 1

    return count 

cap = cv2.VideoCapture(0)

drawing = mp.solutions.drawing_utils
hands = mp.solutions.hands
hand_obj = hands.Hands(max_num_hands=1)

# variables to control the delay between actions
start_init = False 

prev = -1

while True:
    end_time = time.time()
    _, frm = cap.read()
    frm = cv2.flip(frm, 1)

    res = hand_obj.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

    if res.multi_hand_landmarks:

        hand_keyPoints = res.multi_hand_landmarks[0]
        cnt = count_fingers(hand_keyPoints) # call the function to count fingers. i.e. there are so many 1s printed on the console if one finger is up, so if there are many 1s printed it'll take it as a right.
        print(cnt)

        if not(prev == cnt):
            if not(start_init):
                start_time = time.time()
                start_init = True

            elif (end_time-start_time) > 0.2:  #give them time to raise nessecary fingers
                if (cnt == 1):
                    pyautogui.press("right")
                
                elif (cnt == 2):
                    pyautogui.press("left")

                elif (cnt == 3):
                    pyautogui.press("up")

                elif (cnt == 4):
                    pyautogui.press("down")

                elif (cnt == 5):
                    pyautogui.press("space")

                prev = cnt
                start_init = False

        # create skeleton
        drawing.draw_landmarks(frm, hand_keyPoints, hands.HAND_CONNECTIONS)

    cv2.imshow("window", frm)

    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        cap.release()
        break