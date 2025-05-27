import cv2
import os
import numpy as np

from tkinter import *
from tkinter import messagebox
import cv2
import threading
import time


# Stablishing global variables! 
window = any
label = any
cap = any

def threePointer():
  pointsAmmount = 1
  while cap == any:
    pointsAmmount+=1
    if pointsAmmount > 3:
      pointsAmmount = 1
    label.config(text=("Entrenando"+str("."*pointsAmmount)))
    time.sleep(.5)
  if cap != any:
    print("ready")
def close_window():
    window.destroy()
def cargar_archivo():
  dataPath = './faces' #Cambia a la ruta donde hayas almacenado Data
  peopleList = os.listdir(dataPath)
  print('Lista de personas: ', peopleList)
  labels = []
  facesData = []
  label_interno = 0

  for nameDir in peopleList:
    personPath = os.path.join(dataPath, nameDir)
    print('Leyendo las imágenes')

    # Obtener la lista de archivos en la carpeta
    fileNames = os.listdir(personPath)

    # Crear las etiquetas correspondientes para cada imagen
    labels.extend([label_interno] * len(fileNames))

    # Leer todas las imágenes en la carpeta y convertirlas en una lista usando numpy
    faces = [cv2.imread(os.path.join(personPath, fileName), 0) for fileName in fileNames]

    # Añadir las imágenes a la lista facesData
    facesData.extend(faces)

    # Incrementar la etiqueta interna para la siguiente persona
    label_interno += 1
  print("hizop todo")

  # Métodos para entrenar el reconocedor
  face_recognizer = cv2.face.LBPHFaceRecognizer_create()
  # Entrenando el reconocedor de rostros
  print("Entrenando...")
  face_recognizer.train(facesData, np.array(labels))
  # Almacenando el modelo obtenido
  face_recognizer.write('modeloLBPHFace.xml')
  print("Modelo almacenado!")

  # Simulación de carga de archivo
  # time.sleep(2)
  # cap = 1
  global label
  label.config(text="¡Modelo almacenado!")
  time.sleep(.5)


  thread_carga = threading.Thread(target=close_window)
  thread_carga.start()

  window.quit()
def tkinterWindow():
  global window
  global label

  window = Tk()
  window.iconbitmap("./favicon.ico")
  window.title("Face Detector")


  #-------está porción de código va a centrar mi ventana---------
  w = 600
  h = 600
  ws = window.winfo_screenwidth()
  hs = window.winfo_screenheight()
  x = (ws/2) - (w/2)
  y = (hs/2) - (h/2)
  window.geometry('%dx%d+%d+%d' % (w, h, x, y))
  #----------------------------------------------------------


  label = Label(window, text = "Loading...", font=("Arial", 40) )
  label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

  thread_carga = threading.Thread(target=cargar_archivo)
  thread_carga.start()
  
  thread_pointer = threading.Thread(target=threePointer)
  thread_pointer.start()

  window.mainloop()

tkinterWindow()
