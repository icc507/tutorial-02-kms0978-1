#Problema 2  / 9 ptos x4 pruebas / 36 puntos
#Concatenación de listas o tuplas
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios elementos y los entregue de manera inversa
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 90 hola jiji 77
#La salida debe ser
#         (77, 'jiji', 'hola', 90, 20)
#t = input()
#print(t)
t = input()
secuencia = t.split()
secuencia.reverse()
elementos = []
for i in secuencia:
  i = i.strip() 
  if i.isdigit():
    elementos.append(int(i))
  elif "." in i:
    try:
      elementos.append(float(i))
    except ValueError:
      elementos.append(f'{i}')
  else:
    elementos.append(f'{i}')
secuencia_lista = tuple(elementos)
print(secuencia_lista)
