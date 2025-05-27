import cv2
from matplotlib import pyplot as plt

print("1")
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 30)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 300)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
print("2")
while True:
  ret, frame = cap.read()
  print(cap.read)
  cv2.imshow('frame', frame)
  k= cv2.waitKey(30)
  if k==27:
    break
cap.release()
