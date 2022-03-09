from api.library import *

def main():
    # Aplicacion de los Diccionarios
    #persona = {
    #   "nombre": "jaider",
    #  "apellidos": "quintero mendoza",
    # "edad": 45
    # }

    persona = {
        "datospersonales":{
            "nombre": "jaider",
            "apellidos": "quintero mendoza",
            "edad": 45
        },

        "salarial": {
            "salario": 2000000,
            "subtransporte": 50000,
            "subalimentacion": 60000
        }
    }

    # print(persona["nombre"]+ " " + persona["apellidos"])
    #persona["nombre"] = "Blas"
    #print(f"{persona['nombre']} {persona['apellidos']}")

    print(f"Nombre: {persona['datospersonales']['nombre']}  {persona['datospersonales']['apellidos']}")


if __name__ == "__main__":
    main()

