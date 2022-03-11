


def main():
    
    class Persona():
        def __init__(self):
            self.nombre = input("Ingrese el nombre: ")
            self.apellido = input("Ingrese el apellido: ")
            self.direccion = input("Ingrese la direccion: ")
            self.telefono = input("Ingrese el telefono: ")

        def mostrarPersona(self):
            print(f"Nombre: {self.nombre} {self.apellido}")

    class Empleado(Persona):
        def __init__(self):
            super().__init__()
            self.__sueldo = float(input("Ingrese el sueldo: "))

            if self.__sueldo < 2000000:
                self.alimentacion = 80000
                self.transporte = 60000
            else:
                self.alimentacion = 0
                self.transporte = 0
            
            self.pension = self.__sueldo * 0.04
            self.salud = self.__sueldo * 0.0375

            self.dev = self.alimentacion + self.transporte

            self.ded = self.pension + self.salud

        def mostrarEmpleado(self):
            super().mostrarPersona()
            print(f"Sueldo: {self.__sueldo}")
            print(f"Devengado: {self.dev}")
            print(f"Deducciones: {self.ded}")
            print(f"Total a pagar: {self.__sueldo + self.dev + self.ded}")
            

    empleado1 = Empleado()
    # empleado1.__sueldo = 4000000
    empleado1.mostrarEmpleado()



if __name__ == "__main__":
    main()