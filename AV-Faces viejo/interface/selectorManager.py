from tkinter import *
from PIL import ImageTk, Image #pip install pillow
from tkinter import messagebox
from tkinter import ttk
import pymysql
import cv2
import threading
import time
import mainWindow



def tkinterWindow():
  global window
  global label

  window = Tk()
  window.title("")


  #-------está porción de código va a centrar mi ventana---------
  w = 755
  h = 600
  ws = window.winfo_screenwidth()
  hs = window.winfo_screenheight()
  x = (ws/2) - (w/2)
  y = (hs/2) - (h/2)
  window.geometry('%dx%d+%d+%d' % (w, h, x, y))
  #----------------------------------------------------------


  

  window.mainloop()

tkinterWindow()
