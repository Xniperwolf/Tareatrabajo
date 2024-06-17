import os
import time
import csv
from Funciones import *
os.system("cls")

contactos = []
nombrecontactos = []
numerosdecontacto = []
correosdecontactos = []

while True:
    print("Bienvenido al programa de contactos")
    print("-----------------------------------")
    print("1. Agregar contactos a la lista")
    print("2. Mostrar contactos de la lista")
    print("3. Guardar contactos en CSV")
    print("4. Salir")

    while True:
        try:
            opc = int(input("Ingrese opción: "))
            if opc in (1,2,3,4):
                break
            else:
                print("Ingrese una opción correcta entre 1 y 4")
        except:
            print("Debe ser un número entero")
    os.system("cls")

    if opc == 1:
        agregarcontacto()
        time.sleep(2)
        os.system("cls")

    elif opc == 2:
        mostrarlista_contractos()
    elif opc == 3:
        imprimirencsvlalista()
    else:
        print("Muchas gracias por ocupar el programa")
        break