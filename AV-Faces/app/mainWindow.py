import cv2
import os
import datetime
import imutils
import pitonico

guys = {}
guyDetected = ""

# def addLog():
#   actual_time = datetime.datetime.now()
#   with open("./logs.txt", "a") as archivo:
#     archivo.write(f"[{actual_time}]: {guyDetected} asistio\n")


def appendArray(result, imagePaths):
  global guys
  global guyDetected

  currentGuy = format(imagePaths[result[0]])
  if( currentGuy not in guys):
    guys[currentGuy] = 0
    return
  
  guys[currentGuy]+=1  
  print(guys)
  if (guys[currentGuy] == 35):
    print("Guy Finded")
    # guyDetected = currentGuy
    # addLog()
    pitonico.add_assist(currentGuy)
    

def system(dataPath, cap):
  
  imagePaths = os.listdir(dataPath)
  print('imagePaths=',imagePaths)

  face_recognizer = cv2.face.LBPHFaceRecognizer_create()

  # Leyendo el modelo
  face_recognizer.read('./modeloLBPHFace.xml')

  cap = cv2.VideoCapture('./gaspar.mp4')

  faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

  while True:
    ret,frame = cap.read()
    frame = imutils.resize(frame, width=1000)

    if ret == False: break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()

    faces = faceClassif.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
      rostro = auxFrame[y:y+h,x:x+w]
      rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
      result = face_recognizer.predict(rostro)

      cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
      cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)

      if result[1] < 62 :
        appendArray(result, imagePaths)
        cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,100,0),1,cv2.LINE_AA)
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        
        if guyDetected != "":
          cv2.putText(frame, guyDetected+' is detected' ,(50, 50),2,1,(0,255,0),1)
        else: cv2.putText(frame,f'{guys}',(50, 50),2,1,(0,255,0),1)
      else:
        cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
      
    cv2.imshow('frame',frame)
    k = cv2.waitKey(1)
    if k == 27:
      break

  cap.release()
  cv2.destroyAllWindows()
system('./faces', 12)