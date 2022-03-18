import os, sys
from modulos.persona import Persona, Empleado

list_personas = []
list_empleados = []
            

def adicionar_empleado():
    sw = 0
    while (sw == 0):
        os.system('cls')
        nombre = input("Digite el nombre del empleado ==> ")
        direccion = input("Digite la direccion ==> ")
        telefono = input("Digite el telefono ==> ")
        cedula = input("Digite la cedula ==> ")
        sueldo = input("Digite el sueldo ==> ")

        perso = Persona(nombre, direccion, telefono, cedula)
        list_personas.append(perso)

        emp = Empleado(nombre, direccion, telefono, cedula, sueldo)
        list_empleados.append(emp)

        print(""" 
        
        """)
        opc = str(input("Quiere seguir ? (s/n) ==> "))
        if(opc == 's'):
            sw = 0
        else: 
            sw = 1


def eliminar_empleado():
    os.system('cls')
    ced = input("Digite la cedula del Empleado ==> ") 

    for i in range(len(list_empleados)):
        if list_empleados[i].cedula == ced:
            list_empleados.pop(i)


def mostrar_empleado():
    os.system('cls')
    for empleado in list_empleados:
            print(f"{empleado.nombre} - {empleado.direccion} - {empleado.telefono} - {empleado.cedula} - {empleado.sueldo}")
    key=input("digite una tecla para continuar....")   


def salir():
    os.system('cls')
    sys.exit(0)