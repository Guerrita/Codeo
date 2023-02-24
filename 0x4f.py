
def maximaArea(edificio):
  areaMaxima = len(edificio)
  for i in range(2,max(edificio)+1):
    areas =[]
    areaParcial= 0
    for j in edificio:
      if j<i and areaParcial>0:
        areas.append(areaParcial)
        areaParcial =0
        continue
      if j<i:
        continue
      elif j>=i:
        areaParcial+=i
    if(len(areas)>0):
      areaParcial=max(areas)
    if areaParcial>areaMaxima:
      areaMaxima=areaParcial

  return(areaMaxima)


if __name__ == "__main__":
  n = input().split()
  edificios = input().split()
  edificios = list(map(lambda x: int(x),edificios))
  print(maximaArea(edificios))