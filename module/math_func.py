"""
SENA centro de biotecnologia agropecuaria
Ficha:2877795
Aprendiz: Kevin Donato Jimenez Rocha
version: 1.0
fecha: 25/04/2024
"""


def sumar(num1,num2):
    #devuleve la suma de 2 numeros
    return num1 + num2
 
 
#funcion restar realiza la resta de 2 numeros  
def restar(num1,num2):
    #devuelve la resta de 2 numeros  
    return num1 - num2


#funcion multiplicar realiza la multiplicacion de 2 numeros  
def multiplicar(num1,num2):
    #devuleve la multiplicacion de 2 numeros
    resultado = num1 * num2
    return resultado


#funcion dividir realiza la division de 2 numeros  
def dividir(num1,num2):
    #coloco una condicion en caso de que el divisor sea 0 dar un mensaje, ya que no se puede dividir entre 0
    if num2== 0:
        print("no se puede dividir entre 0")
    else: print("la division de los numeros es de", num1/num2)

     
def principal():
    print("aqui funciones al habla")    

    
if __name__=="__main__":
    principal()