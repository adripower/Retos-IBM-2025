while True:

    # Menu 

    print("******Gestor de usuarios******\n")
    print("-1- Añadir Usuario")
    print("-2- Buscar Usuario")
    print("-3- Editar Usuario")
    print("-4- Borrar Usuario")
    print("-5- Salir de la aplicacion\n")
    
    #Entrada para el usuario
    opcion = input("Introduce una opcion: ")

    #Menu de opciones
    match opcion:
        case "1":
            print("Anadimos Usuario")
            pass
        case "2":
            print("Buscamos Usuario")
            pass
        case "3":
            print("Editar Usuario")
            pass
        case "4":
            print("Borrar Usuario")
            pass
        case "5":
            print ("Adios")
            break
        case _:
            print("ERROR")