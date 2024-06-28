"""
SENA centro de biotecnologia agropecuaria
Ficha:2877795
Aprendiz: Kevin Donato Jimenez Rocha
version: 1.0
fecha: 25/04/2024
"""

from random import randint
import os
from colorama import Fore, Back
import module.math_func as mf

def tablasMultiplicacion():
    #creamos una lista hasta 20 que son los datos posibles que usaran
    lista1 = [i for i in range(1, 21)]
    #definimos variables que utilizaremos en la funcion
    num1 = randint(1,20)
    #variables que controlan el ciclo
    i= 0
    n=0
    x=0
    #encerramos en una variable la cantidad de datos de la lista 
    #que se usaran segun el numero aleatorio
    tt= lista1[:num1]
    print(" el numero aleatorio es", num1)
    # al numero aleatorio le sumamos 1 para que el ciclo while
    # me pueda imprimir las tablas del 20 en caso dado
    num1 = num1+1
    #creamos un ciclo while que va a parar hasta que cree todas las tablas del numero aleatorio
    while x <  num1:
        # dentro del ciclo while, creamos un for para ubicar el primer numero que se va a multiplicar
        # ademas imprimimos un mensaje para diferencia el cambio de tabla
        for i in tt:
            print("****************************************")
            #usamos la biblioteca os para realizar la pausa entre tablas
            os.system("pause")
            # creamos un ultimo ciclo for para realizar la multiplicacion y imprimirla en pantalla
            # al final aumentamos el numero del while para darle continuidad a las tablas
            for n in range(1,11):
                resultado = mf.multiplicar(i,n)
                print(f'{Fore.RED}+{Back.BLUE}'," ", i,"*",n, "=",resultado)
                x +=1
 
   
    
    
    

         
    
    
            
    
                
                