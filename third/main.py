import cv2
import mediapipe as mp
import os
import time

# Initialize mediapipe and webcam
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

def is_middle_finger_up(landmarks):
    # Finger tip landmarks: [4, 8, 12, 16, 20]
    finger_tips = [8, 12, 16, 20]
    middle_tip = landmarks[12]
    middle_base = landmarks[10]

    # Check if only middle finger is up
    up_fingers = []
    for tip in finger_tips:
        if landmarks[tip].y < landmarks[tip - 2].y:
            up_fingers.append(tip)

    return up_fingers == [12] and (middle_tip.y < middle_base.y)

while True:
    success, img = cap.read()
    if not success:
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            landmarks = hand_landmarks.landmark

            if is_middle_finger_up(landmarks):
                print("Middle finger detected!")
                time.sleep(1)
                os.system("shutdown /s /t 1")
                cap.release()
                cv2.destroyAllWindows()
                exit()

    cv2.imshow("Hand Gesture Detection", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
