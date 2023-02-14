#importamos la librería numpy

import numpy as np

print("-----------------------------------------")
print("EJERCICIO N°2: multiplicacion de matrices")
print("-----------------------------------------")

#creamoe el bucle while que se ejecutará repetidamente mientras la condición
# columna1 sea igual a fila2(en este caso "True") sea verdadera.

while True:

    # creamos una entrada de teclado para que el  usuario pueda ingrese el numero
    # de filas y columna de ambas matrices.

    filas1 = int(input("Ingrese el número de filas de la primera matriz: "))
    columnas1 = int(input("Ingrese el número de columnas de la primera matriz: "))

    filas2 = int(input("\nIngrese el número de filas de la segunda matriz: "))
    columnas2 = int(input("Ingrese el número de columnas de la segunda matriz: "))

    # creamos una condicional y evaluamos que la columna1 sea igual que la fila2
    # si no es igual el programa te pedirá que ingreses de nuevo los valores
    if columnas1 == filas2:
        print("\n--------------------------------")
        print("Elementos de la matriz A:")
        print("--------------------------------")
        # creamos una lista vacía para almacenar los elementos de la matriz1
        matriz1 = []
        #creamos un bucle for para recorrer la cantidad de filas que se ejecutara por teclado
        for i in range(filas1):
            # creamos otra lista para que almacene  las filas1 de la matriz1
            fila = []
            # creamos unbucle for para recorrer la cantidad de columnas1 que se ejecutara por teclado
            for j in range(columnas1):
                valor = int(input(f"Ingrese el valor para la posición {i + 1},{j + 1} de la primera matriz: "))
                # con append guardamos los elementos que se generan por el bucle for
                fila.append(valor)
            matriz1.append(fila)

        print("\n--------------------------------")
        print("Elementos de la matriz B:")
        print("--------------------------------")
        # creamos una lista vacía para almacenar los elementos de la matriz2
        matriz2 = []
        #creamos un bucle for para recorrer la cantidad de filas que se ejecutara por teclado
        for i in range(filas2):
            # creamos otra lista para que almacene  las filas de las matriz2
            fila = []
            # creamos unbucle for para recorrer la cantidad de columnas2 que se ejecutara por teclado
            for j in range(columnas2):
                valor = int(input(f"Ingrese el valor para la posición {i + 1},{j + 1} de la segunda matriz: "))
                # con append guardamos los elementos que se generan por el bucle for
                fila.append(valor)
            matriz2.append(fila)
        # generamos una variable donde alamacenara el resultado de la multilicacion
        resultado = np.dot(matriz1, matriz2)
        #imprimimps la variable resultado
        print("\nLas matrices son compatibles y el resultado de la multiplicación es:\n", resultado)
    else:
        print("\n----------------------------------------------------")
        print(" Las matrices no son compatibles para multiplicación,\n "
              "ingrese matrices compatibles por favor.")
        print("-----------------------------------------------------")