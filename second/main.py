import cv2
import mediapipe as mp
import pyautogui
import math
import subprocess

cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

screen_width, screen_height = pyautogui.size()
click_down = False
vscode_opened = False

def fingers_up(hand_landmarks):
    tips = [8, 12, 16, 20]
    fingers = []
    for tip in tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)
    return fingers

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            # Index finger tip
            x = int(hand_landmarks.landmark[8].x * img.shape[1])
            y = int(hand_landmarks.landmark[8].y * img.shape[0])
            # Thumb tip
            thumb_x = int(hand_landmarks.landmark[4].x * img.shape[1])
            thumb_y = int(hand_landmarks.landmark[4].y * img.shape[0])

            # Move cursor
            screen_x = int(hand_landmarks.landmark[8].x * screen_width)
            screen_y = int(hand_landmarks.landmark[8].y * screen_height)
            pyautogui.moveTo(screen_x, screen_y)

            # Click gesture (thumb + index)
            distance = math.hypot(x - thumb_x, y - thumb_y)
            if distance < 40 and not click_down:
                pyautogui.click()
                click_down = True
                cv2.putText(img, "Click!", (x, y-30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
            elif distance >= 40:
                click_down = False

            # Middle finger up gesture to open YouTube song
            fingers = fingers_up(hand_landmarks)
            # Only middle finger up: [0,1,0,0]
            if fingers == [0,1,0,0] and not vscode_opened:
                subprocess.Popen(r'start https://www.youtube.com/watch?v=bPk9bSvQQoc', shell=True)
                vscode_opened = True
                cv2.putText(img, "YouTube Song Opened!", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
            elif fingers != [0,1,0,0]:
                vscode_opened = False

    cv2.imshow("Hand Tracking", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()