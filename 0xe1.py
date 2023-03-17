#Cuadrado mágico

def cuadrado_magico():
  try:
    n = int(input())
    if n<2 or n>100: raise Exception('Tamano invalido')
    matriz = []
    for i in range(0, n):
      arreglo=input().split()
      if n!=len(arreglo): raise Exception('El tamano del arreglo no coincide')
      arreglo = list(map(lambda x: int(x),arreglo))
      matriz.append(arreglo)
    suma = sum(matriz[i])
    diag_principal=0
    diag_secundaria=0
    for i in range(0, n):
      diag_secundaria += (matriz[i][n-1-i])
      diag_principal += (matriz[i][i])
      if(suma!= sum(matriz[i])):
        return ("No")

    if(suma!= diag_secundaria or suma!= diag_principal):
      return ("No")
    else:
      return("Yes")
  except Exception as error:
    print(error)

print(cuadrado_magico())