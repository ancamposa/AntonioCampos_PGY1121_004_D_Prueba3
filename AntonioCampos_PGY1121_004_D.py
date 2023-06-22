import random
from datetime import datetime

def verificar_patente(patente):
    vocales="AEIOU"
    if len(patente)!=6:
        return 0
    if patente[:4].isalpha() and patente[4:].isdigit() and not any(v in patente[:4].upper() for v in vocales):
        return 1
    if patente[:2].isalpha() and patente[2:].isdigit() and not any(v in patente[:2].upper() for v in vocales):
        return 1
    return 0

def grabar(datos,multas):
    registro=[]
    registro.append(datos["Tipo"])
    registro.append(datos["Patente"].upper())
    registro.append(datos["Marca"])
    registro.append(datos["Precio"])
    registro.append(datos["Duenio"])
    registro.append(datos["Fecha"])
    registro.append(multas)
    registro.append(random.randint(1500,3500))
    registro.append(random.randint(1500,3500))
    return registro

def buscar(patente,registros):
    patente=patente.upper()
    auto=0
    cont=1
    for x in registros:
        if patente==x[1]:
            auto=1
            print("\nTipo: ",x[0])
            print("Patente: ",x[1])
            print("Marca: ",x[2])
            print("Precio: ",x[3])
            print("Dueño: ",x[4])
            print("Fecha: ",x[5])
            if len(x[6])==0:
                print("\nNo se encontraron multas.")
            elif len(x[6])==1:
                print("\nSe encontró 1 multa:")
            else:
                print("\nSe encontraron",len(x[6]),"multas.")
            for multa in x[6]:
                if len(multa)>0:
                    print("\nMulta",cont)
                    print("\tMonto",multa[0])
                    print("\tFecha",multa[1])
                    cont+=1
    if auto==0:
        print("\nNo se encontraron registros")
        return 0
    
def certificados(patente,registros):
    patente=patente.upper()
    auto=0
    cont=1
    for x in registros:
        if patente==x[1]:
            auto=0
            print("\n")
            print("------------------------------")
            print("|Certificado de Emisión de contaminantes|")
            print("|Patente:",x[1])
            print("|Dueño:",x[4])
            print("|Valor:",x[7])
            print("|          APROBADO          |")
            print("------------------------------")
            print("\n")
            print("------------------------------")
            print("|Certificado de Anotaciones vigentes   |")
            print("|Patente:",x[1])
            print("|Dueño:",x[4])
            print("|Valor:",x[8])
            print("|          APROBADO          |")
            print("------------------------------")
            print("\n")
            print("------------------------------")
            if len(x[6])==0:
                print("\nNo se encontraron multas.")
            elif len(x[6])==1:
                print("\nSe encontró 1 multa:")
            else:
                print("\nSe encontraron",len(x[6]),"multas.")
            for multa in x[6]:
                if len(multa)>0:
                    print("\nMulta",cont)
                    print("\tMonto",multa[0])
                    print("\tFecha",multa[1])
                    cont+=1
    if auto==0:
        print("\nNo se encontraron registros")
        return 0

registros=[]
menu=0
while menu!=4:
    print("\n1. Grabar")
    print("2. Buscar")
    print("3. Imprimir certificados")
    print("4. Salir")
    menu=int(input("\nEscoja que desea hacer: "))
    
    if menu<1 or menu>4:
        print("\nOpción inválida")
        
    if menu==1:
        datos={"Tipo":"x","Patente":"x","Marca":"x","Precio":0,"Duenio":"x","Fecha":"x"}
        multas=[]
        pat=0
        datos["Tipo"]=input("\nIngrese el tipo de vehículo: ")
        while pat==0:
            datos["Patente"]=input("Ingrese patente del vehículo: ")
            pat=verificar_patente(datos["Patente"])
            if pat==0:
                print("Patente inválida")
        while len(datos["Marca"])<2 or len(datos["Marca"])>15:
            datos["Marca"]=input("Ingrese la marca del vehículo: ")
            if len(datos["Marca"])<2 or len(datos["Marca"])>15:
                print("La marca debe tener entre 2 a 15 caracteres")
        while datos["Precio"]<5000000:
            datos["Precio"]=int(input("Ingrese precio del vehículo: "))
            if datos["Precio"]<5000000:
                print("El precio debe ser mayor a $5.000.000")
        datos["Duenio"]=input("Ingrese el nombre del dueño: ")
        while True:
            datos["Fecha"]=input("Ingrese la fecha de registro del vehículo (aaaa/mm/dd): ")
            try:
                fecha=datetime.strptime(datos["Fecha"],'%Y/%m/%d').strftime('%d-%m-%Y')
                print("\nLa fecha de registro del vehiculo es: ")
                print(str(fecha))
            except ValueError:
                print("\nNo ha ingresado una fecha correcta...\n")
            else:
                break

        mult=0
        while mult<1 or mult>2:
            mult=int(input("\n¿Tiene multas?:\n1. Si\n2. No\n"))
        if mult<1 or mult>2:
            print("Opción inválida")
        while mult==1:
            multas2=[]
            multas2.append(int(input("Ingrese del monto de la multa: ")))
            while True:
                multas2.append(input("Ingrese la fecha de la multa (aaaa/mm/dd): "))
                try:
                    fecha=datetime.strptime(multas2[-1],'%Y/%m/%d').strftime('%d-%m-%Y')
                    print("\nLa fecha de la multa es: ")
                    print(str(fecha))
                except ValueError:
                    print("\nNo ha ingresado una fecha correcta...\n")
                else:
                    break
            multas.append(multas2)
            mult=-1
            while mult<1 or mult>2:
                mult=int(input("\n¿Tiene otra multa?:\n1. Si\n2. No\n"))
            if mult<1 or mult>2:
                print("Opción inválida")
        registros.append(grabar(datos,multas))
        
                
    if menu==2:
        patente=input("\nIngrese la patente que desea buscar: ")
        buscar(patente,registros)
        input("\nPresione enter para volver al menú ")

    if menu==3:
        patente=input("\nIngrese la patente que desea buscar: ")
        certificados(patente,registros)
        input("\nPresione enter para volver al menú ")

    if menu==4:
        print("\nGracias por usar el programa\nHecho por: Antonio Campos Álvarez\nVersión: 1.3.7")
                    



























            
            
    
    
