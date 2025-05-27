import openpyxl
import datetime

from openpyxl import Workbook
path = "./asistencias.xlsx"
wb = openpyxl.load_workbook(path)

# grab the active worksheet
ws = wb.active
def add_assist(fullname):
  fulldate = str(datetime.datetime.now()).split(" ")
  fecha = fulldate[0]
  hora = fulldate[1]
  # if len(str(dni)) != 8:
  #   return ["dni incorrecto"]
  # if type(dni) != int and dni.isnumeric() == False:
  #   return ["dni contiene letras"]
  print(datetime.datetime.now())
  register = [fecha, hora, fullname]
  ws.append(register)
  wb.save("asistencias.xlsx")
  print(ws.max_row)
  return ["success", register]

# Data can be assigned directly to cells


# Rows can also be appended
# print(add_assist("gaspar"))
# Python types will automatically be converted

# Save the file
# wb.save("asistencias.xlsx")