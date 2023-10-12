import os.path
import pickle
import clase as clasesita


def separacion_menu():
    print("<" + ("-" * 130) + ">")


def leer_cargar_archivo(nom):
    band = False
    m = open(nom, "rt")
    confir = input(
        "El archivo sera borrado por completo y creado desde cero.\n¿Desea seguir?\n(responda con: si o no): ")
    while not band:
        if confir == "si" or confir == "SI":
            band = True
            print("El archivo fue modificado y/o creado con exito.")
            m.readline()
            m.readline()
            archivo_b = open("Archivo.tickets", "wb")
            for linea in m:
                if linea[-1] == "\n":
                    linea = linea[:-1]
                campos = linea.split(",")
                tickets = clasesita.Tickets(campos[0], campos[1], int(campos[2]), int(campos[3]), int(campos[4]),
                                            int(campos[5]))
                pickle.dump(tickets, archivo_b)
            archivo_b.close()

        elif confir == "no" or confir == "NO":
            print("El archivo no ah sido modificado ni creado.")
            band = True
        else:
            print("Ingrese una respuesta valida.")
            confir = input("Ingrese una respuesta correcta: ")
    m.close()


def pais(patente):
    letras = (
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S",
        "T", "U", "V", "W", "X", "Y", "Z")
    n = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    if len(patente) == 7:

        # PAIS ARGENTINA
        if patente[0] in letras and patente[1] in letras and patente[2] in n and patente[3] in n and patente[4] \
                in n and patente[5] in letras and patente[6] in letras:
            return "Argentina"

        # PAIS BRASIL
        elif patente[0] in letras and patente[1] in letras and patente[2] in letras and patente[3] in n and patente[4] \
                in letras and patente[5] in n and patente[6] in n:
            return "Brasil"

        # PAIS BOLIVIA
        elif patente[0] in letras and patente[1] in letras and patente[2] in n and patente[3] in n and patente[4] \
                in n and patente[5] in n and patente[6] in n:
            return "Bolivia"

        # PAIS PARAGUAY
        elif patente[0] in letras and patente[1] in letras and patente[2] in letras and patente[3] in letras and \
                patente[4] \
                in n and patente[5] in n and patente[6] in n:
            return "Paraguay"

        # PAIS URUGUAY
        elif patente[0] in letras and patente[1] in letras and patente[2] in letras and patente[3] in n and patente[4] \
                in n and patente[5] in n and patente[6] in n:
            return "Uruguay"

    # PAIS CHILE
    elif len(patente) == 6:
        if patente[0] in letras and patente[1] in letras and patente[2] in letras and patente[3] \
                in letras and patente[4] in n and patente[5] in n:
            return "Chile"
    return "Otro"


def mostrar_op3(nom):
    if os.path.exists(nom):
        tamano = os.path.getsize(nom)
        archivo_b = open(nom, "rb")
        while archivo_b.tell() < tamano:
            ticket = pickle.load(archivo_b)

            print ("Codigo: ", ticket.codigo, "Patente: ", ticket.patente, "Pais patente: ", pais(ticket.patente),
                  "Tipo vehiculo: ", ticket.tipo_vehiculo, "Forma pago: ", ticket.forma_pago, "Pais cabina: ",
                  ticket.pais_cabina, "Distancia: ", ticket.distancia)
    else:
        print("El archivo no existe.")


def buscar_patente(nom, p):
    band = False
    if os.path.exists(nom):
        archivo_b = open(nom, "rb")
        tamano = os.path.getsize(nom)
        while archivo_b.tell() < tamano:
            ticket = pickle.load(archivo_b)
            if p == ticket.patente:
                print(ticket)
                band = True
        if not band:
            print("No se encontraron coincidencias.")
    else:
        print("El archivo aun no existe.")


def buscar_codigo(nom, c):
    band = False
    if os.path.exists(nom):
        archivo_b = open(nom, "rb")
        tamano = os.path.getsize(nom)
        while archivo_b.tell() < tamano:
            ticket = pickle.load(archivo_b)
            if c == ticket.codigo:
                print(ticket)
                band = True
                break
        if not band:
            print("No se encontraron coincidencias.")
    else:
        print("El archivo aun no existe.")


def count(nom):
    matrix = [[0] * 5 for i in range(3)]

    if os.path.exists(nom):
        archivo_b = open(nom, "rb")
        tamano = os.path.getsize(nom)
        while archivo_b.tell() < tamano:
            ticket = pickle.load(archivo_b)

            tipo_vehiculo = ticket.tipo_vehiculo
            pais_cabina = ticket.pais_cabina

            matrix[tipo_vehiculo][pais_cabina] += 1
        archivo_b.close()
        return matrix
    else:
        print("El archivo aun no existe.")
    return "-1"


def mostrar_matrix(matrix):
    for f in range(len(matrix)):
        for c in range(len(matrix[f])):
            if matrix[f][c] > 0:
                print("Tipo de vehiculo: ", matrix_vehiculos(f), "del pais :", matrix_paises(c), "Hubo", matrix[f][c],
                      "automoviles.")


def matrix_paises(f):
    if f == 0:
        return "Argentina"
    elif f == 1:
        return "Bolivia"
    elif f == 2:
        return "Brasil"
    elif f == 3:
        return "Paraguay"
    elif f == 4:
        return "Uruguay"


def matrix_vehiculos(c):
    if c == 0:
        return "Motocicleta"
    elif c == 1:
        return "Automovil"
    elif c == 2:
        return "Camión"


def total_tipo(matrix):
    tipo, paises = len(matrix), len(matrix[0])

    for f_1 in range(tipo):
        ac_tipo = 0
        for c_1 in range(paises):
            ac_tipo += matrix[f_1][c_1]
        print('Tipo', matrix_vehiculos(f_1), "(", f_1, ")", '- Cantidad total vehiculos por fila:', ac_tipo)
    for c_2 in range(paises):
        ac_paises = 0
        for f_2 in range(tipo):
            ac_paises += matrix[f_2][c_2]
        print('paises', matrix_paises(c_2), "(", c_2, ")" '- Cantidad total paises por columna:', ac_paises)


def promedio(nom):
    acum = 0
    cont = 0
    if os.path.exists(nom):
        tamano = os.path.getsize(nom)
        archivo_b = open(nom, "rb")

        while archivo_b.tell() < tamano:
            ticket = pickle.load(archivo_b)
            acum += ticket.distancia
            cont += 1
        archivo_b.close()
        prom = acum // cont
        print("El promedio de la distancia recorrida por todo los autos desde la ultima cabina es: ", prom)
    else:
        print("El archivo aun no existe.")
        return "-1"
    return prom


def vector(nom, prom):
    v = []

    if os.path.exists(nom):
        tamano = os.path.getsize(nom)
        archivo_b = open(nom, "rb")
        while archivo_b.tell() < tamano:
            ticket = pickle.load(archivo_b)

            if ticket.distancia > prom:
                v.append(ticket)

    return v


def mostrar_vector(v):
    for i in v:
        print(i)


def ordenar(v):
    n = len(v)
    h = 1
    while h <= n // 9:
        h = 3 * h + 1
    while h > 0:
        for j in range(h, n):
            y = v[j].distancia
            k = j - h
            while k >= 0 and y < v[k].distancia:
                v[k + h].distancia = v[k].distancia
                k -= h
            v[k + h].distancia = y
        h //= 3


def cargar_vector(nom):
    codigo = input("Ingrese el numero del codigo: ")
    while not verificar_codigo(codigo):
        print("El codigo ingresado es incorrecto, ingreselo nuevamente.")
        codigo = input("Ingrese el codigo de forma correcta: ")

    patente = input("Ingrese la patente: ")
    while not verificar_patente(patente):
        print("La patente ingresada es incorrecta, ingresela nuevamente.")
        patente = input("Ingrese la patente de forma correcta: ")

    tipo_vehiculo = input("Ingrese el tipo de vehiculo: ")
    while not verificar_tipo_vehiculo(tipo_vehiculo):
        print("El tipo de vehiculo ingresado es incorrecto, ingreselo nuevamente.")
        tipo_vehiculo = input("Ingrese el tipo de vehiculo de forma correcta: ")

    forma_pago = input("Ingrese la forma de pago: ")
    while not verificar_forma_pago(forma_pago):
        print("La forma de pago ingresada es incorrecta, ingresela nuevamente.")
        forma_pago = input("Ingrese la forma de pago de forma correcta: ")

    pais_cabina = input("Ingrese el pais de la cabina: ")
    while not verificar_pais_cabina(pais_cabina):
        print("El pais de la cabina ingresado es incorrecto, ingreselo nuevamente.")
        pais_cabina = input("Ingrese el pais de la cabina de forma correcta: ")

    distancia = input("Ingrese la distancia desde la ultima cabina: ")
    while not verificar_distancia(distancia):
        print("La distancia ingresada es incorrecta, ingresela nuevamente.")
        distancia = input("Ingrese la distnacia forma correcta: ")

    ticket = clasesita.Tickets(codigo, patente.upper(), int(tipo_vehiculo), int(forma_pago), int(pais_cabina),
                               int(distancia))
    archivo_b = open(nom, "ab")
    pickle.dump(ticket, archivo_b)


def es_letra(valor):
    for i in valor:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            return True
    return False


def es_digito(num):
    for i in num:
        if i in "0123456789":
            return True
    return False


def verificar_codigo(codigo):
    if codigo > "0" and not es_letra(codigo.upper()):
        for i in codigo:
            if i in "1234567890":
                return True
    return False


def verificar_patente(patente):
    for i in patente:
        if i in "abcdefghijklmnopqrstuvwxyz" or i in "1234567890":
            return True
    return False


def verificar_tipo_vehiculo(tipo_vehiculo):
    tam = len(tipo_vehiculo)
    if "0" <= tipo_vehiculo <= "2" and es_digito(tipo_vehiculo) and tam == 1:
        return True
    return False


def verificar_forma_pago(forma_pago):
    tam = len(forma_pago)
    if "1" <= forma_pago <= "2" and es_digito(forma_pago) and tam == 1:
        return True
    return False


def verificar_pais_cabina(pais_cabina):
    tam = len(pais_cabina)
    if "0" <= pais_cabina <= "4" and es_digito(pais_cabina) and tam == 1:
        return True
    return False


def verificar_distancia(distancia):
    if distancia >= "0" and es_digito(distancia):
        return True
    return False

#agregar validación para patente.

def validar_patente(patente):
    if patente == " ":
        return True
    return False
