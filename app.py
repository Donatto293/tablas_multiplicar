""""
Sena Centro de Biotecnologia Agropecuaria(CBA)
Ficha: 2877795
Aprendiz: Kevin Donato Jimenez Rocha
version: 1.0
fecha: 26/04/2024

"""
"""
El codigo genera tablas de multiplicar de un numero
generado pseudo aleatorio de 0 hasta 20, tabla por tabla
"""
import os
import module.funciones_generan as fg
os.system("cls")
            

# la funcion "iniciar()" dara el comienzo al programa, realizando una pregunta si y no,
def iniciar(): 
     texto="BIENVENIDOOOOO!!! :D"
     #centramos en texto de bienvenido"
     print( texto.center(80," "))    
     i=0
     while i <= 1:
          pregunta= input("quieres imprimir las tablas de multiplicacion de un numero aleatorio hasta 20, (responde si o no)").lower()
          # en caso de que la respuesta sea si llama a la funcion "tablasMultiplicacion()" que ejecutara las tablas
          if pregunta == "si":
               fg.tablasMultiplicacion()
          # si la respuesta es "no"  se finalizara el proceso
          elif pregunta == "no":
               print("cerrando maquinaria bai")
               i +=3
          # si la respuesta esat fuera de las opciones se enviara  un mensaje de error
          else:
               print("escriba una opcion valida")
   
          
# llamamos a la funcion iniciar() para comenzar
if __name__=="__main__":
    iniciar()

