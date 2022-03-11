

def listas():
    lista1 = []
    lista2 = list()

    listaConElementos = [30, 2000000, "Andres Pimienta", "Docente", True, ["Magister", "Doctorado", "Especializacion", 20]]

    for i in range(len(listaConElementos)):
        print(listaConElementos[i])
    

    print("")
    print("Mostrando elementos con el ciclo while")
    j=0
    while j < len(listaConElementos):
        print(listaConElementos[j])
        #j=j+1
        j+=1
    
    listaConElementos[1]= listaConElementos[1] + 200000