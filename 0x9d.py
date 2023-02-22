n = int(input())
datos= input().split()

def ordernado(n, datos):
    for i in range(0,n):
        if(i<n-1):
            if(int(datos[i])>int(datos[i+1])):
                return("Desordenado")
    return("Ordenado")
print(ordernado(n, datos))