from numpy.lib import index_tricks
import xlwings as xw
import time as tm
import numpy as np
from xlwings.utils import VersionNumber
import operator as op

wb = xw.Book('CALCULADORA4.xlsx')
print("FINALIZADO wb = xw.Book('CALCULADORA4.xlsx')")
print("")
pid = xw.apps.keys()
print("FINALIZADO pid = xw.apps.keys()")
print("PID:",pid[0])
print("")
xw.apps[pid[0]].books['CALCULADORA4.xlsx']
print("FINALIZADO xw.apps[13144].books['CALCULADORA4.xlsx']")
print("")
sheet = wb.sheets['Dados_2']
print("FINALIZADO sheet = wb.sheets['Dados_2']")
print("")

def cos(n):
  t = np.cos(n)
  return t

def sin(n):
  t = np.sin(n)
  return t

b = sheet.range('E2:E19').value
c = sheet.range('F2:F19').value

print("Lenght of variable b: ", len(b))
print("Lenght of variable c: ", len(c))

x = list()
y = list()

for i in b: 
 x.append(cos(i))

for i in c: 
 y.append(sin(i))

print("COS")    
for i in x: 
    print(i)

print("SIN")
for i in y:
    print(i)

teta = list(map(op.add,x, y))

print("TETA")
for i in teta:
    print(i)


sheet.range('D2').options(transpose=True).value = teta
sheet.range('E2').options(transpose=True).value = x    
sheet.range('F2').options(transpose=True).value = y

    
    

    
    
   


   





    










     
  
   



