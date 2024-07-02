import os
import csv
import time
os.system("cls")
import json

from funcionestienda import *

ventas = []

while True:
    print("Bienvenido a la aplicación de tienda Wolf")
    print("------------------------------------------")
    print("1. Registrar nueva venta")
    print("2. Reporte de ventas histórico")
    print("3. Reporte de ventas por producto")
    print("4. Reports por forma de pago")
    print("5. Salir del programa")

    while True:
        try:
            opc = int(input("Ingrese una opción: "))
            if opc in (1,2,3,4,5):
                break
            else:
                print("Ingrese una opción correcta")
        except:
            print("Ingrese un número entero")
    
    os.system("cls")
    if opc == 1:
        registrar_venta()


    elif opc == 2:
        reporte()

                

    elif opc == 3:
            registroproducto()

    elif opc == 4:
        registroformadepago()

    else:
        print("Muchas gracias por ocupar la aplicación")
        break

