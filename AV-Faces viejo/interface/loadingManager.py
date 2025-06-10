from tkinter import *
from PIL import ImageTk, Image #pip install pillow
from tkinter import messagebox
from tkinter import ttk
import cv2
import threading
import time
import mainWindow

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
    label.config(text=("Loading"+str("."*pointsAmmount)))
    time.sleep(.5)
  if cap != any:
    print("ready")


def close_window():
    window.destroy()

def cargar_archivo():
  global cap
  print("done")
  # Simulación de carga de archivo
  cap = cv2.VideoCapture(0)
  print(cap)
  # time.sleep(2)
  # cap = 1
  
  label.config(text="Done")
  time.sleep(.3)


  thread_carga = threading.Thread(target=close_window)
  thread_carga.start()


  mainWindow.system(r'D:\Python\Sexto\AV-Faces\faces', cap)
  window.quit()


def tkinterWindow():
  global window
  global label

  window = Tk()
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
