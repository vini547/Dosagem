import xlwings as xw
import time

wb = xw.Book('Doses_PED.xlsx')
print("FINALIZADO wb = xw.Book('Doses_PED.xlsx')")
print("")
pid = xw.apps.keys()
print("FINALIZADO pid = xw.apps.keys()")
print("PID:",pid[0])
print("")
xw.apps[pid[0]].books['Doses_PED.xlsx']
print("FINALIZADO xw.apps[13144].books['Doses_PED.xlsx']")
print("")
sheet = wb.sheets['Medicamentos']
print("FINALIZADO sheet = wb.sheets['Medicamentos']")
print("")
x = 0
print("FINALIZADO x = 0")
print("")

a = sheet.range('A4:C13').value
b = sheet.range('A16:C17').value
c = sheet.range('A19:C26').value
d = sheet.range('A28:C35').value
e = sheet.range('A38:G38').value
f = sheet.range('A41:C45').value
g = sheet.range('A47:C49').value
h = sheet.range('A51:E53').value
i = sheet.range('A55:C56').value
j = sheet.range('A60:C62').value
k = sheet.range('A64:G64').value
l = sheet.range('A70:E74').value
m = sheet.range('A78:E90').value
n = sheet.range('A98:C108').value
o = sheet.range('A110:G111').value
p = sheet.range('A113:C115').value
q = sheet.range('A117:G117').value


print("FINALIZADO sheet.range.(A1:C1).value")
print("")

while x <= 10 :
 sheet.range('B2').value = x
 print("Calculando para Peso: ", x)
 time.sleep(0.2)
 x += 1
print("")

print(">>>>>>>>>>>>>>>  O Process ID 'PID' é: ", pid, "                     <<<<<<<<<<<<<<<")
print(">>>>>>>>>>>>>>>  O VALOR DE wb.sheets['Medicamentos'] : ", sheet," <<<<<<<<<<<<<<<")
print(">>>>>>>>>>>>>>>  O VALOR DE type(sheet) : ", type(sheet), "          <<<<<<<<<<<<<<<")
print("")

print(">>>>>>>>>>>>>>>  VALUES <<<<<<<<<<<<<<<")
print("")
print("O Valor de print(a) Analgésicos                                                          :",print(a))
print("")
print("O Valor de print(b) Antiácidos Minerais                                                  :", print(b))
print("")
print("O Valor de print(c) Antiácidos Inibidores de H2                                          :", print(c))
print("")
print("O Valor de print(d) Antiácidos Inibidores da Bomba Protônica                             :", print(d))
print("")
print("O Valor de print(e) ANTIMICROBIANOS Aminoglicosídeos                                     :", print(e))
print("")
print("O Valor de print(f) ANTIMICROBIANOS Anfenicois                                           :", print(f))
print("")
print("O Valor de print(g) ANTIMICROBIANOS Anaerobicida                                         :", print(g))
print("")
print("O Valor de print(h) ANTIMICROBIANOS Carbapênicos - Beta Lactâmicos                       :", print(h))
print("")
print("O Valor de print(i) ANTIMICROBIANOS Cefalosporinas (beta-lactâmicos) - Primeira Geração  :", print(i))
print("")
print("O Valor de print(j) ANTIMICROBIANOS Cefalosporinas (beta-lactâmicos) - Segunda Geração   :", print(j))
print("")
print("O Valor de print(k) ANTIMICROBIANOS Cefalosporinas (beta-lactâmicos) - Terceira Geração  :", print(k))
print("")
print("O Valor de print(l) ANTIMICROBIANOS Macrolídeos                                          :", print(l))
print("")
print("O Valor de print(m) ANTIMICROBIANOS Penicilinas - Beta Lactâmicos                        :", print(m))
print("")
print("O Valor de print(n) ANTIMICROBIANOS Quinolonas                                           :", print(n))
print("")
print("O Valor de print(o) ANTIMICROBIANOS sulfametoxazol + trimetoprin                         :", print(o))
print("")
print("O Valor de print(p) ANTIMICROBIANOS Tetraciclinas                                        :", print(p))
print("")
print("O Valor de print(q) ANTIMICROBIANOS ANTIFÚNGICOS SISTÊMICOS                              :", print(q))
print("")

print("")

print(">>>>>>>>>>>>>>>  TYPES <<<<<<<<<<<<<<<")
print("")
print("O Valor de type(a)   :", type(a))
print("O Valor de type(b)   :", type(b))
print("O Valor de type(c)   :", type(c))
print("O Valor de type(d)   :", type(d))
print("O Valor de type(e)   :", type(e))
print("O Valor de type(f)   :", type(f))
print("O Valor de type(g)   :", type(g))
print("O Valor de type(h)   :", type(h))
print("O Valor de type(i)   :", type(i))
print("O Valor de type(j)   :", type(j))
print("O Valor de type(k)   :", type(k))
print("O Valor de type(l)   :", type(l))
print("O Valor de type(m)   :", type(m))
print("O Valor de type(n)   :", type(n))
print("O Valor de type(o)   :", type(o))
print("O Valor de type(p)   :", type(p))
print("O Valor de type(h)   :", type(q))
print("O Valor de type(pid) :", type(pid))


print("")




