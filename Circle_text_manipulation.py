import cv2

# use webcam capture
cap = cv2.VideoCapture(0)

# keep the capturing on
while True:
    ret, frame = cap.read()
    # cap.read value 3 is width
    width = int(cap.get(3))
    # cap.read Value 4 is height
    height = int(cap.get(4))
    # Draw the lines
    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 10)
    # Draw rectangle
    img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 1)
    # Draw Circle
    img = cv2.circle(img, (300, 300), 60, (0, 0, 255), -1)
    # Put Text on the Screen
    font = cv2.FONT_HERSHEY_COMPLEX
    img = cv2.putText(img, 'Shahriar is Coooooool', (10, height - 10), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow('Frame ', img)
    # how to quit by pressing "Q" on keyboard
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
