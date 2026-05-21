opcion = 0

while opcion != 4:

    print("\n======================")
    print("        MENU")
    print("======================")
    print("1 - Opción 1")
    print("2 - Opción 2")
    print("3 - Opción 3")
    print("4 - Salir")

    opcion = int(input("Elegí una opción: "))

    if opcion == 1:
        print("\nEjecutando opción 1...\n")
        
         if opcion == 1:

        A = [101, 102, 103, 104, 105, 106]
        B = [104, 105, 106, 107, 108]
        C = [102, 105, 109]

        # Funcion logica
        def usuario_critico(usuario):

            p = usuario in A
            q = usuario in B
            r = usuario in C

            return (p or q) and r

        # Lista de usuarios sin repetir
        usuarios = []

        for x in A:
            if x not in usuarios:
                usuarios.append(x)

        for x in B:
            if x not in usuarios:
                usuarios.append(x)

        for x in C:
            if x not in usuarios:
                usuarios.append(x)

        # Clasificacion
        criticos = []
        no_criticos = []

        for u in usuarios:

            if usuario_critico(u):
                criticos.append(u)

            else:
                no_criticos.append(u)

        print("\nUsuarios criticos:")
        print(criticos)

        print("\nUsuarios no criticos:")
        print(no_criticos)

    elif opcion == 2:
        print("\nEjecutando opción 2...\n")
        
        # PEGÁ TU CÓDIGO ACÁ

    elif opcion == 3:
        print("\nEjecutando opción 3...\n")
        
        # PEGÁ TU CÓDIGO ACÁ

    elif opcion == 4:
        print("\nSaliendo del programa...")

    else:
        print("\nOpción inválida, intentá de nuevo.")