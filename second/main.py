import cv2
from fer import FER  # Make sure 'fer' is installed: pip install fer

# Load pre-trained face detector and expression recognizer
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
# You can download a pre-trained emotion model or use a placeholder for demo
# For demo, we'll just show "Face Detected" as expression

cap = cv2.VideoCapture(0)
# ...existing code...
detector = FER()
# ...existing code...

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # Placeholder for expression recognition
        expression = "Face Detected"
        cv2.putText(frame, expression, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)

    cv2.imshow('Face Expression Recognizer', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
     # Facial expression recognition
    emotion, score = None, None
    try:
        result = detector.top_emotion(frame)
        if result:
            emotion, score = result
            cv2.putText(frame, f"Emotion: {emotion} ({score:.2f})", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)
    except Exception as e:
        result = detector.top_emotion(frame)
        if result:
            emotion, score = result
            cv2.putText(frame, f"Emotion: {emotion} ({score:.2f})", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)
# cv2.destroyAllWindows()
cv2.destroyAllWindows()