def calcularsueldo():
    nombre = input("Digite el nombre: ")
    salario = int(input("Digite el salario mensual: "))
    diastrabajados = int(input("digite los dias trabajadas: "))
    sueldopagar = salario/30 * diastrabajados
    print(f"mi nombre es: {nombre} y mi sueldo es {sueldopagar:.0f}")


def main():
    calcularsueldo()



if __name__ == "__main__":
    main()