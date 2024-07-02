ventas = []
import os
import csv
import time
import json

def registrar_venta():
        os.system("cls")
        print("Registrar nueva venta")
        time.sleep(0.5)
        print("----------------------")
        time.sleep(0.5)
        nombreproducto = input("Ingrese nombre del producto: ")
        cantidadproducto = int(input("Ingrese cantidad de producto: "))
        valorunitarioproducto = int(input("Ingrese valor unitario del producto: "))
        formadepagoproducto = int(input("Ingrese forma de pago: (1 para Efectivo, 2 para debito, 3 para crédito, 4 para transferencia)"))

        preciototalventa = valorunitarioproducto*cantidadproducto
        print("El precio total de la venta es: ",preciototalventa)
        
        ventaregistrada = {"Producto": nombreproducto, "Cantidad": cantidadproducto, "Valor Unitario": valorunitarioproducto, "Pago": formadepagoproducto, "Total": preciototalventa}
        ventas.append(ventaregistrada)

        print("Venta registrada con éxito")
        time.sleep(2)
        os.system("cls")

def reporte():
        os.system("cls")
        if len(ventas) == 0:
            print("No hay productos registrados")
        else:
            print("Lista de Ventas Históricas")
            for x in ventas:
                print(f"Producto: {x['Producto']}\n Cantidad:{x['Cantidad']}\n Valor Unitario:{x['Valor Unitario']}\n Pago:{x['Pago']}\n Total:{x['Total']}")
                time.sleep(2)
                os.system("cls")

def registroproducto():
            nombreproducto = input("Ingrese nombre del producto a buscar: ")
            for x in ventas:
                if x['Producto'].lower() == nombreproducto.lower():
                    print(f"Producto: {x['Producto']}\nCantidad: {x['Cantidad']}\nValor Unitario: {x['Valor Unitario']}\nPago: {x['Pago']}\nTotal: {x['Total']}\n")
                    break
                else:
                    print("Producto no existe")

        
            with open("Archivo_ventas.csv","w", newline="") as archivo:
                secciones = ["Producto", "Cantidad", "Valor Unitario", "Pago", "Total"]
                escritor = csv.DictWriter(archivo, fieldnames=secciones)
                escritor.writeheader()
                escritor.writerows(ventas)

def registroformadepago():
        formadepagoproducto = int(input("Ingrese nombre del producto a buscar (1 para Efectivo, 2 para debito, 3 para crédito, 4 para transferencia): "))
        for x in ventas:
            if x['Pago'] == formadepagoproducto:
                print(f"Producto: {x['Producto']}\nCantidad: {x['Cantidad']}\nValor Unitario: {x['Valor Unitario']}\nPago: {x['Pago']}\nTotal: {x['Total']}\n")
                break
            else:
                print("No se ha pagado con ese medio de pago")
                

        
            with open("Archivo_mediosdepago.csv","w", newline="") as archivo:
                secciones = ["Producto", "Cantidad", "Valor Unitario", "Pago", "Total"]
                escritor = csv.DictWriter(archivo, fieldnames=secciones)
                escritor.writeheader()
                escritor.writerows(ventas)

