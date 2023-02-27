from django.shortcuts import render #libreria para reconocer el request(front del usuario)
from django.http import HttpResponse #permite morstar en pantalla el resultado


#EJERCICIO 1:
#Hallar la suma de los 10 primeros numeros

def inicio(request,*cadena,**cadenaID):
    return render( request,'inicio.html')
def aplicaciones(request,*cadena,**cadenaID):
    #definiendo matrices
    matriz1=[[1,2],
        [3,4]]

    matriz2=[[5,6],
        [7,8]]

    resultado=[[0,0],
        [0,0]]
#i =fila , j=columna
#suma de matrices
    for i in range(2):
        for j in range(2):
            resultado[i][j]=matriz1[i][j]+matriz2[i][j]
        
    print("la suma de la matriz de 2x2 es:")
    print(resultado)

    return render(request,'aplicaciones.html',{'suma':resultado})
def nosotros(request,*cadena,**cadenaID):
    return render(request,'nosotros.html')
def vision(request,*cadena,**cadenaID):
    return render(request,'vision.html')