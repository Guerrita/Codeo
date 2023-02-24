try:
  num_elementos=int(input())
  arreglo=input().split()
  if num_elementos!=len(arreglo): raise Exception('El tamano del arreglo no coincide')
  arreglo = list(map(lambda x: int(x),arreglo))
  num_consultas = int(input())
  entradas=[]
  for i in range(0,num_consultas):
    n_entrada = int(input())
    entradas.append(n_entrada)
  for i in entradas:
    count = len(list(filter(lambda x: i<x, arreglo)))
    print(count)
except Exception as error:
  print(error)