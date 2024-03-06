respuesta=input("Responde a estímulos?: ")
ambulancia="no"

if (respuesta) =="si":
    print("Valorar la necesidad de llevarlo al hospital mas cercano")
else:
    print("abrir las vias aéreas")
    respuesta2=input("Respira?:")
    if respuesta2=="si":
        print("permitirle posicion de suficiente ventilacion")
    else:
        print("Administrar 5 ventilaciones y llamar a Ambulancia")
        while ambulancia =="no":
            respuesta3=input("¿Signos de vida?")
            if respuesta3=="si":
                print("reevaluar a la espera de la ambulancia")    
            else:
                print("administrar compresiones toraccicas hasta que llegue la ambulancia")
            ambulancia=input("llego la ambulancia? ")
                    