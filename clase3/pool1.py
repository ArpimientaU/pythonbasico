



def main():
    
    class Persona():
        nombre = "Jaider"
        apellido = "Quintero"
        direccion = "Km 1"
        telefono = "3176548810"

        def mostrarPersona(self):
            print(f"Nombre: {self.nombre} {self.apellido}")
    persona1 = Persona()   #Crear una instancia de la clase
    print(persona1.nombre)

    persona2 = Persona()
    persona2.nombre = "Sandy Elena"
    persona2.apellido = "Romero Cuello"
    persona2.direccion = "Calle 24"
    persona2.telefono = "3103032030"
    persona2.mostrarPersona()

if __name__ == "__main__":
    main()