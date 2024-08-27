#Problema 1  / 8 ptos x4 pruebas / 32 puntos
#Concatenación de listas o tuplas
#--------------------------------
#Confeccione un programa que lea 2 tuplas sean t1 y t2
#La salida debe ser una tupla en el orden t2 t1 t2
#---------------------------------
#Ejemplo de entrada:
#         20 90 hola
#		  mundo 44
#La salida debe ser
#         ('mundo', 44, 20, 90, 'hola', 'mundo', 44)
#t = input()
#m = input()
#print(m)
t = input()
m = input()
union = tuple(m.split())+tuple(t.split())+tuple(m.split())
elementos_modif = []
for elemento in union:
  elemento = elemento.strip()
  if elemento.isdigit():
    elementos_modif.append(int(elemento))
  elif "." in elemento:
    try:
      elementos_modif.append(float(elemento))
    except ValueError:
      elementos_modif.append(f'{elemento}')
  else:
    elementos_modif.append(f'{elemento}')
tupla = tuple(elementos_modif)
print(tupla)
