def letraRepetida(palabra):
  letras =[]
  if len(palabra)<=50:
    for i in palabra:
      if i in letras:
        return("yes")
      else:
        letras.append(i)
    return("no")

if __name__ == "__main__":
  palabra = input()
  print(letraRepetida(palabra))