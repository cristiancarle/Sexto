import cv2
import os
import imutils

personName = "tommy"
dataPath = "C:/Users/rober/Desktop/carle-proyecto/faces/tommy"
counter =0
while os.path.exists(dataPath):
	dataPath = dataPath + "_" + str(counter)
	counter+=1
if not os.path.exists(dataPath):
  print('Folder created: ' + dataPath)
  os.mkdir(dataPath)

cap = cv2.VideoCapture('./faces/'+personName+'.mp4')

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
count = 0


while True:

	ret, frame = cap.read()
	if ret == False: break
	frame =  imutils.resize(frame, width=640)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	auxFrame = frame.copy()
	
	faces = faceClassif.detectMultiScale(gray,1.3,5)

	for (x,y,w,h) in faces:
		
		rostro = auxFrame[y:y+h,x:x+w]
		rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
		print(w,h, count)
		if w >= 100 and h >= 100:
			cv2.imwrite(dataPath+ '/rotro_{}.jpg'.format(count),rostro)
			cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
		else: cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0 ,255),2)
		
		count = count + 1
	cv2.imshow('frame',frame)

	k =  cv2.waitKey(1)
	if k == 27 or count >= 300:
		break

cap.release()
cv2.destroyAllWindows()