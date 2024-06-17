contactos = []
import csv

def menucontactos():
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

def agregarcontacto():
    nombreyapellido_contacto = input("Ingrese nombre de contacto: ")
    numerotelefono_contacto = int(input("Ingrese número de contacto: "))
    correoelectrónico_contacto = input("Ingrese correo: ")
    contacto = [nombreyapellido_contacto,numerotelefono_contacto,correoelectrónico_contacto]
    contactos.append(contacto)

    print("Datos registrados con éxito")

def mostrarlista_contractos():
    if len(contactos) == 0:
            print("No hay trabajadores registrados, ocupe la opción 1 del menú.")
    else:
        print("Lista de contactos")
        for x in contactos:
            print(f"Nombre: {x[0]}\n Numero:{x[1]}\n Correo:{x[2]}\n")

def imprimirencsvlalista():
    if len(contactos) == 0:
            print("No hay trabajadores en la lista, agregue para poder exportar a CSV")
    else:
        with open("Archivo_contactos.csv","w", newline="") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerows(contactos)
        

