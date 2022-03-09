from api.library import *

def main():
    SALARIO_MIN = 1000000
    SUB_ALIM = 120000
    SUB_TRANSP = 80000
    BONO = 50000
    nombre = input("Digite el nombre: ")
    salario = int(input("Digite el salario mensual: "))
    diastrabajados = int(input("digite los dias trabajados: "))
    sueldopagar = calcularsueldo(salario, diastrabajados)

    if salario < (SALARIO_MIN * 2):
        sueldopagar = sueldopagar + SUB_ALIM + SUB_TRANSP
    else:
        sueldopagar = sueldopagar + BONO

    print(f"mi nombre es: {nombre} y mi sueldo es {sueldopagar:.0f}")



if __name__ == "__main__":
    main()