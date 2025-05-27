import os
import time
import threading
import numpy as np
import imutils
import cv2
from tkinter.filedialog import askopenfilename
from tkinter import Tk, messagebox, ttk
from tkinter import *

# Stablishing global variables! 
window = any
label = any
cap = any
file_selected = any
def save_image(path, img):
    cv2.imwrite(path, img)
def change():
  quit_me()
  import loadingManager
def update():
  quit_me()
  import updateModel
def quit_me():
    print('quit')
    window.quit()
    window.destroy()
def create_fotograms(personName):
  personName = (personName.get()).lower()
  dataPath = f"./faces/{personName}"

  # Verificación de existencia de la carpeta
  if os.path.exists(dataPath):
      messagebox.showerror("Error", f"{personName} ya está registrado en ./faces")
      return "error:ya-registrado"
  else:
      print(f'Folder created: {dataPath}')
      os.mkdir(dataPath)

  # Iniciar captura de video
  inicio = time.time()
  cap = cv2.VideoCapture(file_selected)
  faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
  count = 0

  while True:
      ret, frame = cap.read()
      if not ret: 
          break

      # Redimensionar y convertir a escala de grises
      frame = imutils.resize(frame, width=640)
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

      # Detectar rostros
      faces = faceClassif.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

      if len(faces) > 0:
          # Convertir detecciones en arrays de numpy para procesamiento vectorizado
          faces = np.array(faces)

          # Filtrar rostros con dimensiones deseadas
          valid_faces = faces[(faces[:, 2] >= 100) & (faces[:, 3] >= 100)]

          for (x, y, w, h) in valid_faces:
              rostro = frame[y:y+h, x:x+w]
              rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)

              # Guardar la imagen del rostro
              threading.Thread(target=save_image, args=(os.path.join(dataPath, f'rostro_{count}.jpg'), rostro)).start()
              cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
              
              count += 1

          # Dibujar rectángulos rojos para rostros que no cumplen los requisitos
          invalid_faces = faces[(faces[:, 2] < 100) | (faces[:, 3] < 100)]
          for (x, y, w, h) in invalid_faces:
              cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

      cv2.imshow('frame', frame)

      k = cv2.waitKey(1)
      if k == 27 or count >= 500:
          break

  fin = time.time()
  print(f"Tiempo de ejecución: {fin - inicio} segundos")

  cap.release()
  cv2.destroyAllWindows()
def tkinterWindow():
  global window
  global label
  window = Tk()
  window.iconbitmap("./favicon.ico")
  window.resizable(0,0)
  window.protocol("WM_DELETE_WINDOW", quit_me)
  window.title("EduFaceAssist")
  #-----esta porción de código va a centrar la ventana-------
  w = 600
  h = 320
  ws = window.winfo_screenwidth()
  hs = window.winfo_screenheight()
  x = (ws/2) - (w/2)
  y = (hs/2) - (h/2)
  window.geometry('%dx%d+%d+%d' % (w, h, x, y))
  #----------------------------------------------------------

  def select_video():
    Tk().withdraw()
    filename = askopenfilename()
    if filename[-4:] == ".mp4":
      global file_selected
      file_selected = filename
      person_entry.focus()
      subject_name.set(f"({ file_selected.split('/')[-1] })")
      btn_nuevo.configure(state='normal')
    elif filename != "":
      btn_video.focus()
      messagebox.showerror("Error","Formato de archivo invalido. Prueba con (.mp4)")
  def add_person():
    if not (person_name.get()).isalpha():
      messagebox.showerror("Error","Nombre invalido")
      person_entry.focus()
      return

    btn_nuevo.configure(state='disabled')
    btn_video.configure(state='disabled')
    person_entry.configure(state='disabled')
    final_state = create_fotograms(person_name)
    
    btn_nuevo.configure(state='normal')
    btn_video.configure(state='normal')
    person_entry.configure(state='normal')

    if final_state == 'error:ya-registrado':
      person_name.set("")
      person_entry.focus()
      return
    messagebox.showinfo("Cara agregada", f"{person_name.get()} ha sido agregado exitosamente en ../faces !")
    person_name.set("")
    subject_name.set("(no seleccionado)")
    global file_selected
    file_selected = ""

  labelframe = ttk.Labelframe(window, width=300, height=195, text="Agregar persona")
  labelframe.pack()
  labelframe.place(x=35 ,y=100)
  labelframe = ttk.Labelframe(window, width=230, height=195, text="Visualización del modelo de IA")
  labelframe.pack()
  labelframe.place(x=345 ,y=100)

  subject_name = StringVar()
  subject_name.set("(no seleccionado)")

  Label(window, text="EduFaceAssist",  font=("Arial", 30) ).place(x=35,y=25)
  Label(window, textvariable=subject_name).place(x=160,y=130)

  btn_video = Button(window,text="Selecciona video", command=select_video, width=15, height=2)
  btn_video.pack()
  btn_video.place(x=45,y=120)

  Label(window, text="Nombre:", font=("Arial")).place(x=45,y=190)
  person_name = StringVar()
  person_entry = Entry(window , textvariable=person_name)
  person_entry.pack()
  person_entry.place(x=120, y=193)

  btn_nuevo = Button(window,text="Agregar", command=add_person, state=DISABLED, width=27, height=2)
  btn_nuevo.pack()
  btn_nuevo.place(x=45,y=240)

  btn_change = Button(window,text="Ir al modelo", command=change,width=27, height=2)
  btn_change.pack()
  btn_change.place(x=360,y=150)
  btn_change = Button(window,text="Actualizar modelo", command=update,width=27, height=2)
  btn_change.pack()
  btn_change.place(x=360,y=210)



  btn_video.focus()

  window.mainloop()

tkinterWindow()
