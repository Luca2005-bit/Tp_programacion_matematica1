# =========================
# VARIABLE MENU
# =========================

opcion = 0

# =========================
# MENU PRINCIPAL
# =========================

while opcion != 4:

    print("\n========================")
    print("TRABAJO PRACTICO")
    print("========================")

    print("1 - Consigna 1")
    print("2 - Consigna 2")
    print("3 - Consigna 3")
    print("4 - Salir")

    opcion = int(input("Seleccione una opcion: "))

    # =====================================================
    # CONSIGNA 1
    # =====================================================

    if opcion == 1:

        A = [101, 102, 103, 104, 105, 106]
        B = [104, 105, 106, 107, 108]
        C = [102, 105, 109]

        def usuario_critico(usuario):

            p = usuario in A
            q = usuario in B
            r = usuario in C

            return (p or q) and r

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

    # =====================================================
    # CONSIGNA 2
    # =====================================================

    elif opcion == 2:

        import matplotlib.pyplot as plt

        # FUNCIONES

        def A(x):
            return 40 * x + 200

        def B(x):
            return 70 * x + 50

        def C(x):
            return -2 * x**2 + 80 * x + 100

        # VALORES DE X

        x = list(range(0, 51))

        # LISTAS DE Y

        yA = []
        yB = []
        yC = []

        for i in x:
            yA.append(A(i))
            yB.append(B(i))
            yC.append(C(i))

        # GRAFICO

        plt.plot(x, yA, label="A(x)")
        plt.plot(x, yB, label="B(x)")
        plt.plot(x, yC, label="C(x)")

        plt.xlabel("Horas")
        plt.ylabel("Costo")
        plt.title("Planes de contratacion")

        plt.legend()
        plt.grid()

        plt.show()

        # EVALUAR FUNCIONES

        valores = [0, 5, 10, 15, 20, 25, 30, 40, 50]

        for v in valores:

            print("\nx =", v)
            print("A =", A(v))
            print("B =", B(v))
            print("C =", C(v))

        # PLAN MAS BARATO

        def plan_mas_barato(x):

            a = A(x)
            b = B(x)
            c = C(x)

            menor = min(a, b, c)

            if menor == a:
                return "Plan A"

            elif menor == b:
                return "Plan B"

            else:
                return "Plan C"

        print("\nPlan mas economico segun las horas:")

        for i in valores:
            print("x =", i, "->", plan_mas_barato(i))

        # INTERSECCION

        print("\nInterseccion entre A y B:")
        print("(5 , 400)")

        # VERTICE

        print("\nVertice de C:")
        print("(20 , 900)")

        # RAICES

        print("\nRaices de C:")
        print("x1 = -1.2")
        print("x2 = 41.2")

        # C NEGATIVA

        print("\nValores donde C es negativa:")

        for i in range(0, 51):

            if C(i) < 0:
                print("x =", i)

    # =====================================================
    # CONSIGNA 3
    # =====================================================

    elif opcion == 3:

        M = [
            [120, 150, 100],
            [200, 180, 220],
            [90, 110, 95]
        ]

        C = [
            [30, 20, 10],
            [15, 25, 20],
            [40, 10, 30]
        ]

        print("\nDIMENSIONES")

        filas_M = len(M)
        columnas_M = len(M[0])

        filas_C = len(C)
        columnas_C = len(C[0])

        print("M:", filas_M, "x", columnas_M)
        print("C:", filas_C, "x", columnas_C)

        if columnas_M == filas_C:
            print("Se puede realizar el producto M * C")
        else:
            print("No se puede realizar el producto M * C")

        # PROMEDIO POR FUNCION

        print("\nPROMEDIO POR FUNCION")

        for i in range(filas_M):

            suma = 0

            for j in range(columnas_M):
                suma = suma + M[i][j]

            promedio = suma / columnas_M

            print("Funcion", i + 1, ":", promedio)

        # MATRIZ TRANSPUESTA

        print("\nMATRIZ TRANSPUESTA")

        MT = []

        for j in range(columnas_M):

            fila = []

            for i in range(filas_M):
                fila.append(M[i][j])

            MT.append(fila)

        for fila in MT:
            print(fila)

        # PRODUCTO MATRICIAL

        print("\nPRODUCTO M * C")

        T = []

        for i in range(filas_M):

            fila = []

            for j in range(columnas_C):

                suma = 0

                for k in range(columnas_M):
                    suma = suma + M[i][k] * C[k][j]

                fila.append(suma)

            T.append(fila)

        for fila in T:
            print(fila)

        # DETERMINANTE

        a = M[0][0]
        b = M[0][1]
        c = M[0][2]

        d = M[1][0]
        e = M[1][1]
        f = M[1][2]

        g = M[2][0]
        h = M[2][1]
        i = M[2][2]

        determinante = (
            a * (e * i - f * h)
            - b * (d * i - f * g)
            + c * (d * h - e * g)
        )

        print("\nDeterminante:", determinante)

        if determinante != 0:
            print("La matriz es invertible")
        else:
            print("La matriz NO es invertible")

    # =====================================================
    # SALIR
    # =====================================================

    elif opcion == 4:

        print("\nSaliendo del programa...")

    # =====================================================
    # ERROR
    # =====================================================

    else:

        print("\nOpcion incorrecta")