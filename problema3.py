#Problema 2  / 7 ptos x4 pruebas / 28 puntos
#Ingreso de valores en árbol TRI-nario
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios números y cree un árbol trinario con listas
# esto es igual que el binario, pero los elementos que son iguales van en una lista
# centro, de la forma [numero, [subarbol IZQ], [mismo NUM], [subarbol DER] ]
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 30 90 90 8 5 90
#La salida debe ser
#         [20, [8, [5, [], [], []], [], []], [], [30, [], [], [90, [], [90, [], [90, [], [], []], []], []]]]
#t = input()
#print(t)
def arbolTrinario(numero):
  return [numero, [], [], []]

def insertaEnArbolTrinario(arbol, numero):
  if arbol == []:
    arbol += arbolTrinario(numero)
  elif numero < arbol[0]:
    insertaEnArbolTrinario(arbol[1], numero)
  elif numero == arbol[0]:
    insertaEnArbolTrinario(arbol[2], numero)
  else:
    insertaEnArbolTrinario(arbol[3], numero)

def estaEnArbolTrinario(arbol, numero):
  if arbol == []:
    return False
  elif numero == arbol[0]:
    return True
  elif numero < arbol[0]:
    return estaEnArbolTrinario(arbol[1], numero)
  elif numero == arbol[0]:
    return estaEnArbolTrinario(arbol[2], numero)
  else:
    return estaEnArbolTrinario(arbol[3], numero)
#uso
t = input()
m = t.split()
num = int(m[0])
w = arbolTrinario(num)
for i in range(1,len(m)):
  n = int(m[i])
  insertaEnArbolTrinario(w, n)
print(w)
