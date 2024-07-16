import random
import csv

trabajadores = ["Juan Perez", "Maria Garcia", "Carlos Lopez", "Ana Martinez", "Pedro Rodriguez", "Laura Hernandez", "Miguel Sanchez", "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"]
trabajadoresDict = []
sueldos_ingresados = False


def sueldos():
    global sueldos_ingresados
    for trabajador in trabajadores:
        trabajaInfo = {}
        sueldo = random.randint(300000 , 2500000)
        trabajaInfo["nombre"] = trabajador
        trabajaInfo["sueldo"] = sueldo
        trabajadoresDict.append(trabajaInfo)
    print("\nSueldos asignados!")
    sueldos_ingresados = True

def clasificacion():
    if not sueldos_ingresados:
        print("Ingrese los sueldos antes de esta opcion")
        return
    
    menor_800k = []
    entre_800k_2M = []
    mayor_2M = []
    
    for trabajador in trabajadoresDict:
        if trabajador["sueldo"] < 800000:
            menor_800k.append(trabajador)
        elif 800000 <= trabajador["sueldo"] < 2000000:
            entre_800k_2M.append(trabajador)
        else:
            mayor_2M.append(trabajador)
            
    if menor_800k:  
        print(f"\nSueldos menores a $800.000. Total {len(menor_800k)}")
        print(f"{'Nombre empleado':<20}{'Sueldos'}")
        for trabajador in menor_800k:
            print(f"{trabajador['nombre']:<20}${trabajador['sueldo']:,}")
    
    if entre_800k_2M:
        print(f"\nSueldos entre $800.000 y $2.000.000. Total {len(entre_800k_2M)}")
        print(f"{'Nombre empleado':<20}{'Sueldos'}")
        for trabajador in entre_800k_2M:
            print(f"{trabajador['nombre']:<20}${trabajador['sueldo']:,}")
            
    if mayor_2M:        
        print(f"\nSueldos mayores a $2.000.000. Total {len(mayor_2M)}")
        print(f"{'Nombre empleado':<20}{'Sueldos'}")
        for trabajador in mayor_2M:
            print(f"{trabajador['nombre']:<20}${trabajador['sueldo']:,}")

def estadisticas():
    if not sueldos_ingresados:
        print("Ingrese los sueldos antes de esta opcion")
        return
    
    alto = 0
    bajo = 999999999
    promedio = 0
    for trabajador in trabajadoresDict:
        promedio += trabajador['sueldo']
        if trabajador['sueldo'] > alto:
            persona1 = trabajador['nombre']
            alto = trabajador['sueldo']
        
        if trabajador['sueldo'] < bajo:
            bajo = trabajador['sueldo']
            persona2 = trabajador['nombre']
    
    promedio = int(promedio / len(trabajadoresDict))
    
    print(f"\nEl sueldo mas alto es de {persona1} que es de ${alto:,}")
    print(f"El sueldo mas bajo es de {persona2} que es de ${bajo:,}")
    print(f"El promedio entre los sueldos es de ${promedio:,}")


def reporte():
    if not sueldos_ingresados:
        print("Ingrese los sueldos antes de esta opcion")
        return
    
    for trabajador in trabajadoresDict:
        descuentoSalud = int(round(trabajador["sueldo"] * 0.07, 0)) * -1
        descuentoAFP = int(round(trabajador["sueldo"] * 0.12, 0)) * -1
        sueldoLiquido = trabajador["sueldo"] + descuentoSalud + descuentoAFP
        trabajador["descuento salud"] = descuentoSalud ; trabajador["descuento AFP"] = descuentoAFP ; trabajador["sueldo liquido"] = sueldoLiquido

    print(f"{'Nombre empleado':<20}{'Sueldos':<20}{'Descuento Salud':<20}{"Descuento AFP":<20}{'Sueldo Liquido':<20}")
    for trabajador in trabajadoresDict:
        print(f"{trabajador['nombre']:<20}${trabajador['sueldo']:<20,}${trabajador['descuento salud']:<20,}${trabajador['descuento AFP']:<20,}${trabajador['sueldo liquido']:<20,}")
    
    archivoCSV()
    
    
def archivoCSV():
    for trabajador in trabajadoresDict:
        with open("Reporte.csv", "w", newline="") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(trabajadoresDict[0].keys())
            escritor.writerows(trabajador.values())
            


def menu():
    while True:
        try:
            opcion = int(input("\n1.Asignar Sueldos\n2.Clasificar Sueldos\n3.Ver estadisticas\n4.Reporte de Sueldos\n5.Salir del programa\nSeleccione una opcion: "))
            if opcion == 1:
                sueldos()
            elif opcion == 2:
                clasificacion()
            elif opcion == 3:
                estadisticas()
            elif opcion == 4:
                reporte()
            elif opcion == 5:
                print("Finalizando programa . . . ")
                print("\nDesarrollado por: Nicolas Salas\nRUT: 26.328.580-2")
                break
            else:
                print("Opcion invalida. Intentelo nuevamente")
        except ValueError:
            print("Valor ingresado erroreo. Intentelo nuevamente")

menu()