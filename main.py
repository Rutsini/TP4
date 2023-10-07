import funcs as func


def main():
    op = "-1"
    nom = "Archivo.tickets"
    nom2 = "peajes-tp4.csv"

    func.separacion_menu()
    print("Opción 1: - Crear archivo binario.")
    print("Opción 2: - Cargar por teclado los datos de un ticket.")
    print("Opción 3: - Mostrar todos los registros del archivo.")
    print("Opción 4: - Mostrar los datos de los registros igual a la patente ingresada.")
    print("Opción 5: - Mostrar los datos del registro igual al codigo ingresado.")
    print("Opción 6: - Determinar y mostrar la cantidad de vehiculos.")
    print("Opción 7: - Mostrar cantidad total de vehiculos por tipo y por pais de cabina.")
    print("Opción 8: - Crear y mostrar un arreglo con los registros mayores al promedio de la distancia total.")
    print("Opción 9: - Salir")

    func.separacion_menu()

    while op != "9":
        op = input("Ingrese la opción que desea: ")

        if op == "1":
            func.separacion_menu()
            print("Opcion 1.")

            func.leer_cargar_archivo(nom2)

            func.separacion_menu()
        elif op == "2":
            func.separacion_menu()
            print("Opcion 2.")

            func.cargar_vector(nom)

            func.separacion_menu()
        elif op == "3":
            func.separacion_menu()
            print("Opcion 3.")

            func.mostrar_op3(nom)

            func.separacion_menu()
        elif op == "4":
            func.separacion_menu()
            print("Opcion 4.")

            p = input("Ingrese la patente que desee buscar: ")
            while not func.verificar_patente(p):
                print("Ingrese una patente valida para buscar.")
                p = input("Ingrese la patente nuevamente de forma correcta.\n - : ")

            func.buscar_patente(nom, p.upper())

            func.separacion_menu()
        elif op == "5":
            func.separacion_menu()
            print("Opcion 5.")

            c = input("Ingrese el código que desee buscar: ")
            while not func.verificar_codigo(c):
                print("Ingrese un codigo valido para poder buscarlo.")
                c = input("Ingrese el codigo nuevamente de forma correcta.\n - : ")

            func.buscar_codigo(nom, c)

            func.separacion_menu()
        elif op == "6":
            func.separacion_menu()
            print("Opcion 6.")

            matrix = func.count(nom)
            if matrix != "-1":
                func.mostrar_matrix(matrix)
            else:
                print(
                    "La cantidad total de vehiculos no es mostrada debido a que el archivo no existe y todos los "
                    "resulados seran cero.")

            func.separacion_menu()
        elif op == "7":
            func.separacion_menu()
            print("Opcion 7.")

            matrix = func.count(nom)
            if matrix != "-1":
                func.total_tipo(matrix)
            else:
                print(
                    "La cantidad total de vehiculos por tipo y cabina no es mostrada debido a que el archivo"
                    " no existe y todos los resulados seran cero.")

            func.separacion_menu()
        elif op == "8":
            func.separacion_menu()
            print("Opcion 8.")

            prom = func.promedio(nom)
            if prom != "-1":
                vect = func.vector(nom, prom)
                func.ordenar(vect)
                func.mostrar_vector(vect)
            else:
                print("No se muestra ningun resultado debido a que el archivo aun no existe.")

            func.separacion_menu()
        elif op == "9":
            func.separacion_menu()
            print("Opcion 9.")

            print("Salio del programa.")

            func.separacion_menu()


if __name__ == "__main__":
    main()
