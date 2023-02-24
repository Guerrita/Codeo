def greater(cw, ccw):
  if cw>= ccw: 
    return ccw
  else:
    return cw
def tortuga(n,x,y):
    if(x==y):
      return 0
    elif(x>y):
      cw = n-x+y
      ccw= abs(x-y)

    elif(x<y):
      cw = abs(y-x)
      
      ccw = x + n -y
    return greater(cw, ccw)

if __name__ == "__main__":
  n,x,y = input().split()
  print(tortuga(int(n),int(x),int(y)))