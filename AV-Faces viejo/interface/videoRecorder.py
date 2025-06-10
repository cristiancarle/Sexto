import numpy as np
import cv2

cap = cv2.VideoCapture(0)

framerate = int(cap.get(cv2.CAP_PROP_FPS))
videoFileName = 'video.avi'

fourcc = cv2.VideoWriter_fourcc(*'DIVX')


out = cv2.VideoWriter(videoFileName,
                      fourcc,
                      framerate,
                      (400, 400))

while True:
    success, frame = cap.read()

    if not success:
      print("Failed to read the frame")
      break
    cv2.imshow('Camera video', frame)
    out.write(frame)

    if cv2.waitKey(1) == ord('c'):
      break

out.release()
cap.release()
cv2.destroyAllWindows()