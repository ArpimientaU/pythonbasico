from api.library import *

def main():

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
    print(f"Nombre: {persona['datospersonales']['nombre']}  {persona['datospersonales']['apellidos']}")
 

if __name__ == "__main__":
    main()