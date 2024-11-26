from datetime import datetime, date
import colores
import csv

# Crea la fecha con el formato de datetime
# Devuelve False si el formato es erróneo
def set_fecha(fecha):
    try:
        fecha_separada = fecha.split("-")
        dia = int(fecha_separada[0])
        mes = int(fecha_separada[1])
        anyo = int(fecha_separada[2])
    
        fecha_formateada = date(anyo, mes, dia)
    except IndexError:
        print(colores.RED + "Formato de fecha erróneo" + colores.RESET)
        return False
    except ValueError:
        print(colores.RED + "Formato de fecha erróneo" + colores.RESET)
        return False
    
    return fecha_formateada

# Formatea fecha al formato español DIA-MES-AÑO solo para visionar
def formatear_fecha(fecha):
    dia = fecha.day
    mes = fecha.month
    anyo = fecha.year

    fecha_formateada = str(dia) + "-" + str(mes) + "-" + str(anyo)

    return fecha_formateada

# Permite añadir nuevas tareas a la lista con el formato:
# Nombre, prioridad, fecha
def add_tarea():
    nombre_tarea = input(colores.CYAN + "Introduce un nombre para la tarea: " + colores.RESET)
    prioridad_tarea = input(colores.CYAN + "Introduce una prioridad para la tarea: " + colores.RESET)
    fecha_input = input(colores.CYAN + "Introduce una fecha para la tarea con el formato DIA-MES-AÑO: " + colores.RESET)

    # El numero de elementos en la lista en hexadecimal marca el ID de la tarea. +1 para que no empiece en 0
    num_tareas = len(lista_tareas) + 1
    
    # Si el formato es erróneo no se añade la tarea y termina la función
    fecha_tarea = set_fecha(fecha_input)
    if fecha_tarea == False:
        return

    nueva_tarea = {
        "id" : hex(num_tareas),
        "nombre" : nombre_tarea,
        "prioridad" : prioridad_tarea,
        "fecha" : fecha_tarea,
        "esta_completada" : False
    }
    lista_tareas.append(nueva_tarea)
    print(colores.GREEN + "¡Tarea añadida!\n" + colores.RESET)

# Lista las tareas por con sola con el formato:
            # <------------------------->
            # ID: Código hexadecimal
            # Nombre de la tarea: Ejemplo [] / [X] <- (Indica si está completada o no)
            # Prioridad: 4
            # Fecha: 14-12-2024
            # <------------------------->
def listar_tareas():
    print(colores.BRIGHT_YELLOW + "Listando Tareas\n" + colores.RESET)
    if len(lista_tareas) == 0:
        print(colores.BRIGHT_YELLOW + "Lista Vacía\n" + colores.RESET)
    else:
        for tarea in lista_tareas:
            tarea_id = tarea.get("id")
            tarea_nombre = tarea.get("nombre")
            tarea_prioridad = tarea.get("prioridad")

            tarea_fecha = formatear_fecha(tarea.get("fecha"))

            tarea_esta_completada = "[]"
            if tarea.get("esta_completada"):
                tarea_esta_completada = "[" + colores.GREEN + "X" + colores.RESET + "]"
            
            print(f"""
                <------------------------->
                    ID: {tarea_id}
                    Nombre de la tarea: {tarea_nombre} {tarea_esta_completada}
                    Prioridad: {tarea_prioridad}
                    Fecha: {tarea_fecha}
                <------------------------->
                """)

# Elimina tareas en función del nombre introducido CAMBIAR ESTO A ID UNICO
def eliminar_tarea():
    id_tarea = input(colores.CYAN + "Introduce el identificador (ID) de la tarea para borrar: " + colores.RESET)
    print(colores.RED + "¡ATENCION! Eliminar una tarea es una acción irreversible. Una vez lo hagas no podrás deshacer esta acción." + colores.RESET)

    opcion = ""
    while opcion != "S" and opcion != "N":
        opcion = input("¿Estás seguro de querer eliminar la tarea? (" + colores.GREEN + "S" + colores.RESET + "/" + colores.RED + "N" + colores.RESET +")").upper()

    if opcion == "N":
        print(colores.RED + "Operacion cancelada\n" + colores.RESET)
    else:
        encontrada = False

        for tarea in lista_tareas:
            if tarea.get("id") == id_tarea:
                encontrada = True
                lista_tareas.remove(tarea)

        print(colores.GREEN + "¡Tarea eliminada!\n" + colores.RESET if encontrada else colores.BRIGHT_RED + "No se encontró la tarea" + colores.RESET)

# Marca la tarea como completada en función de un ID UNICO
def marcar_tarea():
    id_tarea = input(colores.CYAN + "Introduce el identificador (ID) de la tarea para marcarla como completada: " + colores.RESET)

    encontrada = False

    for tarea in lista_tareas:
        if tarea.get("id") == id_tarea:
            tarea["esta_completada"] = True
            encontrada = True
    
    print(colores.GREEN + "¡Tarea marcada como completada!\n" + colores.RESET if encontrada else colores.BRIGHT_RED + "No se encontró la tarea\n" + colores.RESET)

# Guarda la lista de tareas a un archivo CSV
def guardar_archivo():
    # Pregunta al usuario si está seguro de sobreescribir su archivo csv ya existente. Si escoge S (Si) lo guarda. Si escoge N (No) vuelve al menú inicial sin guardar nada.
    print(colores.RED + "¡ATENCION! Guardar el archivo sobreescribirá el archivo existente con las tareas que se encuentran actualmente en la lista." + colores.RESET)

    opcion = ""
    while(opcion != "S" and opcion != "N"):
        opcion = input("¿Estás seguro de querer guardar el archivo? (" + colores.GREEN + "S" + colores.RESET + "/" + colores.RED + "N" + colores.RESET +")").upper()

    if(opcion == "N"):
        print(colores.RED + "Operacion cancelada\n" + colores.RESET)
    else:
        with open('tareas.csv', mode='w', newline='') as fichero:
            fieldnames = ["id", "nombre", "prioridad", "fecha", "esta_completada"]
            escritor = csv.DictWriter(fichero, fieldnames = fieldnames)

            escritor.writeheader()
            for tarea in lista_tareas:
                escritor.writerow({"id" : tarea["id"], "nombre" : tarea["nombre"], "prioridad" : tarea["prioridad"], "fecha" : tarea["fecha"], "esta_completada" : tarea["esta_completada"]})

            print(colores.GREEN + "¡Achivo guardado!\n" + colores.RESET)

# Permite cargar un archivo csv
def cargar_archivo():
    ruta_archivo = input("Introduce la ruta del archivo .csv: ")

    try:
        with open(ruta_archivo) as fichero:
            lector = csv.DictReader(fichero, delimiter=',')
            for fila in lector:
                nueva_fecha = build_fecha(fila.get("fecha"))
                nueva_esta_completada = True if fila["esta_completada"] == "True" else False
                
                nueva_tarea = {"id": fila["id"], "nombre" : fila["nombre"], "prioridad" : fila["prioridad"], "fecha" : nueva_fecha, "esta_completada" : nueva_esta_completada}
                lista_tareas.append(nueva_tarea)
    except FileNotFoundError:
        print(colores.RED + "No se ha encontrado el archivo" + colores.RESET)
        
# Construye la fecha con el formato adecuado cuando se importa desde un csv
def build_fecha(fecha):
    nueva_fecha_cadena = ""
    fecha_separada = fecha.split("-")
    for i in fecha_separada[::-1]:
        nueva_fecha_cadena += str(i) + "-"
    
    nueva_fecha_cadena = nueva_fecha_cadena[0:10]
    # Hay que pasar la fecha en string a objeto date. Date no tiene un metodo para ello, así que hay que hacer el paso intermedio por medio de un datetime
    # y luego coger solo la parte de la fecha
    fecha_formato = datetime.strptime(nueva_fecha_cadena, "%d-%m-%Y")
    nueva_fecha = date(fecha_formato.year, fecha_formato.month, fecha_formato.day)  

    return nueva_fecha

# Evalua la opción elegida por el usuario y actúa en consecuencia
def evaluar_opcion (opcion):
    match opcion:
        case 1:
            add_tarea()
        case 2:
            eliminar_tarea()
        case 3:
            listar_tareas()
        case 4:
            marcar_tarea()
        case 5:
            guardar_archivo()
        case 6:
            cargar_archivo()
        case 0:
            print(colores.RED + "Fin de la aplicacion" + colores.RESET)
        case _:
            print("Introduce un número válido de la lista \n")


# Lista de Tareas
lista_tareas = []

# Pedirá una opción de las de la lista. Si no se proporciona una opción válida vuelve a pedir una opción
# Si la opción es 0 finalizará el programa.
opcion = -1
while(opcion != 0):
    print("""\
        1.- Añadir Tarea
        2.- Eliminar Tarea
        3.- Listar Tareas
        4.- Marcar Tarea Completada
        5.- Guardar Tareas en Archivo
        6.- Cargar Archivo
        0.- Salir
    """)

    try:
        opcion = int(input("Introduce un número para realizar una acción: "))
        evaluar_opcion(opcion)
        
    except ValueError:
        print("Solo puedes introducir un número entero como opción \n")

