from datetime import date, datetime
import random

def primera_vez():
    """
    Cuando un usuario ingresa por primera vez imprime una version reducida del menu
    con solo ingresar un nuevo usuario o ingresar con un usuario ya existente.
    () -> opcion_usuario:int
    """

    print('Bienvenido a tu lista de tareas!')
    print('1. Crear nuevo usuario')
    print('2. Ingresar con usuario ya existente')

    opcion_usuario = int(input('Ingresa el número de opcion que deseas: '))

    while opcion_usuario<1 or opcion_usuario >2:
        print('Opcion no valida, ingresa una opción posible')
        opcion_usuario = int(input('Ingresa el número de opcion que deseas: '))

    return opcion_usuario

def menu():
    """
    Imprimir en pantalla un menu con opciones, input para ingresar la opcion y la retorna
    () -> opcion_usuario: int
    """
    print('')
    print('MENU!')
    print('1. Crear nueva tarea')
    print('2. Actualizar estado tarea ya existente')
    print('3. Contar tareas en el mismo estado')
    print('4. Registrar nuevo usuario')
    print('5. Tiempo restante de tarea')
    print('6. Imprimir tareas')
    print('7. Salir del programa')
    
    print('')
    opcion_usuario = int(input('Ingresa la opción deseada: '))
    while opcion_usuario<1 or opcion_usuario>7:
        print('Ingresa una opcion valida')
        opcion_usuario = int(input('Ingresa la opción deseada: '))
    print('')
    return opcion_usuario

def busqueda_tarea(lista_tareas, correo_usuario):
    """
    Realiza la busqueda de una tarea dependiendo si el usuario decide hacer la busqueda
    por descripcion o por ID
    (lista_tareas:list, correo_usuario:str) -> posicion_tarea:int
    """
    print('Desea buscar con: \n1. Descripción de la tarea \n2. ID de la tarea')
    opcion_buscar = int(input('Ingrese el número de la opción que elige: '))
    while opcion_buscar <1 or opcion_buscar>2:
        print('Opción no valida')
        opcion_buscar = int(input('Ingrese el número de la opción que elige: '))
    print('')
    
    if opcion_buscar == 1: #Busqueda por descripcion
        descripcion_tarea = str(input('Ingresa la descripcion de tu tarea: '))
        encontrar_tarea = False
        posicion_tarea = 0
        while encontrar_tarea != True:
            for i in range(0,len(lista_tareas)):
                if correo_usuario == lista_tareas[i][0] and descripcion_tarea == lista_tareas[i][2]:
                    posicion_tarea = i
                    encontrar_tarea = True
            if encontrar_tarea == False:
                print('No se encontraron tareas con la descripcion ingresada, intenta con otra descripcion')
                id_tarea = str(input('Ingresa el la descripcion de tu tarea: '))
            
    elif opcion_buscar == 2: #Busqueda por id
        id_tarea = str(input('Ingresa el ID de tu tarea: '))
        encontrar_tarea = False
        posicion_tarea = 0
        while encontrar_tarea != True:
            for i in range(0,len(lista_tareas)):
                if correo_usuario == lista_tareas[i][0] and id_tarea == lista_tareas[i][1]:
                    posicion_tarea = i
                    encontrar_tarea = True
            if encontrar_tarea == False:
                print('No se encontraron tareas con el ID ingresado, intenta con otro ID')
                id_tarea = str(input('Ingresa el ID de tu tarea: '))
            
    
    return posicion_tarea

#VALIDACION DE CORREO
def revisar_correo_existente(lista_usuarios, correo):
    """
    Revisar si un correo existe con la lista de usuarios
    (lista_usuarios: lista, correo:str) -> Bool
    """
    for i in range(0, len(lista_usuarios)):
        if correo == lista_usuarios[i][1]:
            return True

def revisar_correo(lista_usuarios,opcion):
    """
    El usuario ingresa su correo y la funcion anterior evalua si ya existe
    (lista_usuarios: list, opcion:int) -> correo_usuario: str
    """
    correo_usuario = str(input('Ingresa tu correo: '))
    #Cuando se quiere verificar que el correo ya exista
    if opcion == 0:
        while revisar_correo_existente(lista_usuarios, correo_usuario) == True: 
            print('Ese correo ya existe, intenta un correo diferente')
            correo_usuario = str(input('Ingresa tu correo: '))

    #Cuando se quiere verificar que no exista
    elif opcion == 1:    
        while revisar_correo_existente(lista_usuarios, correo_usuario) != True: 
            print('Ese correo no existe, intenta un correo diferente')
            correo_usuario = str(input('Ingresa tu correo: '))

    return correo_usuario

#FUNCIONES RELACIONADAS CON ID
def verificar_si_id_existe(id, lista_ids):
    """
    Verificar si un id exista y cambiarlo por un id nuevo con la funcion de generador de ids
    (id: str, lista_ids: lista) -> Bool
    """
    for i in range(0, len(lista_ids)):
        if id == lista_ids[i]:
            return False #El id no existe, por ende es nuevo
        
def generador_id(opcion, lista_ids):
    """
    Generador de ids para usuario y para tareas
    (opcion: int, lista_ids: lista) -> id_generado: str
    """
    if opcion == 1: #Generar id para usuario
        valor_aleatorio = str(random.randint(0,9999999999))
        id_generado = "ID_"+valor_aleatorio
        id_nuevo = verificar_si_id_existe(id_generado, lista_ids)

        while id_nuevo == False:
            valor_aleatorio = str(random.randint(0,9999999999))
            id_generado = "ID_"+valor_aleatorio
            id_nuevo = verificar_si_id_existe(id_generado, lista_ids)

    elif opcion ==2: #Generar ID para tareas
        valor_aleatorio = str(random.randint(0,9999999999))
        id_generado = "ID_tarea_"+valor_aleatorio
        id_nuevo = verificar_si_id_existe(id_generado, lista_ids)

        while id_nuevo == False:
            valor_aleatorio = str(random.randint(0,9999999999))
            id_generado = "ID_tarea_"+valor_aleatorio
            id_nuevo = verificar_si_id_existe(id_generado, lista_ids)
    
    return id_generado

#FUNCION REGISTRAR NUEVOS USUARIOS
def registrar_nuevo_usuario(lista_usuarios, lista_ids_usuarios):
    """
    Registrar un nuevo usuario y devolver esa lista para agregarla despues en la lista de usuarios
    (lista_usuarios: list, lista_ids_usuarios: list) -> usuario_nuevo: list, id_generado:str
    """
    usuario_nuevo = ["" for i in range(0,3)] #usuario: "nombre", "correo", "ID_unico"

    usuario_nuevo[0] = str(input('Ingresa tu nombre: '))
        
    usuario_nuevo[1] = revisar_correo(lista_usuarios, 0)

    id_generado = generador_id(1, lista_ids_usuarios)
    usuario_nuevo[2] = id_generado

    return usuario_nuevo, id_generado

#FUNCIONES PARA CREAR TAREAS
def fecha_ingresada_posible(fecha_ingresada):
    """
    Revisar si la fecha ingresada es posible
    (fecha_ingresada: str) -> Bool
    """
    #Revisa longitud del str
    if len(fecha_ingresada) < 10 or len(fecha_ingresada) > 10:
        return False
    
    #Revisa el espaciado entre fecha
    if fecha_ingresada[4] != "-" or fecha_ingresada[7] != "-":
        return False
    
    fecha_tarea = datetime.strptime(fecha_ingresada, "%Y-%m-%d")
    fecha_hoy = datetime.strptime(str(date.today()), "%Y-%m-%d")

    #Revisa si la fecha ingresada es posterior a hoy
    if fecha_hoy >= fecha_tarea:
        return False
    else:
        return True

def configurar_tarea(lista_ids_tareas):
    """
    Establecer la informacion restante de la tarea: id, descripcion, estado y fecha limite
    (lista_ids_tareas: list) -> id_tarea: str, descripcion_tarea: str, estado_tarea: str, fecha_limite: str
    """
    ESTADOS_TAREA = ["To-Do", "In-Progress", "Pending", "Done"]
    
    #ID_TAREA
    id_tarea = generador_id(2, lista_ids_tareas)
    print(f'ID asignado a tu tarea: {id_tarea}')

    #DESCRIPCION TAREA
    descripcion_tarea = str(input('Ingresa una descripcion para tu tarea: '))
    print('')
    
    #ESTADO TAREAS
    print('Estados de tarea: \n1. To-Do \n2. In-Progress \n3. Pending \n4. Done')
    opcion_tarea_estado = int(input('Ingresa la opción de estado de tarea que deseas: '))
    while opcion_tarea_estado <1 or opcion_tarea_estado>4:
        print('Estado no valido, ingresa un valor posible')
        opcion_tarea_estado = int(input('Ingresa la opción de estado de tarea que deseas: '))
    
    if opcion_tarea_estado == 1:
        estado_tarea = ESTADOS_TAREA[0]
    elif opcion_tarea_estado == 2:
        estado_tarea = ESTADOS_TAREA[1]
    elif opcion_tarea_estado == 3:
        estado_tarea = ESTADOS_TAREA[2]
    elif opcion_tarea_estado == 4:
        estado_tarea = ESTADOS_TAREA[3]

    print('')

    #FECHA LIMITE
    print('Escribe la fecha limite de tu tarea en el siguiente formato (AAAA-MM-DD)')
    fecha_limite = str(input('Ingresa la fecha limite: '))
    while fecha_ingresada_posible(fecha_limite) != True:
        print('Fecha ingresada no valida, ingresa otra fecha posterior a Hoy')
        fecha_limite = str(input('Ingresa la fecha limite: '))

    return id_tarea, descripcion_tarea, estado_tarea, fecha_limite

def crear_tarea(lista_usuarios, lista_ids_tareas):
    """
    Funcion para crear una tarea nueva y retorna la lista con la informacion de la misma con su id respectivo
    (lista_usuarios: list, lista_ids_tareas: list) -> tarea:list, id_tarea:str
    """
    tarea = ["" for i in range(0,5)] #tarea: "correo", "ID_tarea", "Descripcion_tarea", "Estado_tarea", "Fecha Limite (DD-MM-AAAA)"
    
    correo_usuario = revisar_correo(lista_usuarios, 1)
    tarea[0] = correo_usuario
    
    id_tarea, descripcion_tarea, estado_tarea, fecha_limite = configurar_tarea(lista_ids_tareas)
    
    tarea[1] = id_tarea
    tarea[2] = descripcion_tarea
    tarea[3] = estado_tarea
    tarea[4] = fecha_limite

    print('')
    print('Tarea ingresada de manera exitosa')
    
    return tarea, id_tarea

#FUNCIONES PARA CAMBIAR ESTADO TAREA
def actualizar_tarea(lista_usuarios, lista_tareas): 
    """
    Funcion que retorna la posicion en la lista de tareas y el nuevo estado de la tarea
    (lista_usuarios: list, lista_tareas: list) ->posicion_tarea:int, nuevo_estado_tarea: str
    """
    correo_usuario = revisar_correo(lista_usuarios, 1)
    posicion_tarea = busqueda_tarea(lista_tareas, correo_usuario)
        
    nuevo_estado_tarea = cambiar_estado_tarea(lista_tareas, posicion_tarea)
    
    return posicion_tarea, nuevo_estado_tarea

def cambiar_estado_tarea(lista_tareas, posicion_tarea):
    """
    Mini menu para cambiar el estado de la tarea, segun el estado inicial
    (lista_tareas: list, posicion_tarea:int) -> estado_tarea_nuevo: str
    """
    ESTADOS_TAREA = ["To-Do", "In-Progress", "Pending", "Done"]

    if lista_tareas[posicion_tarea][3] == "To-Do":
        print(f'El estado actual de tu tarea es: {lista_tareas[posicion_tarea][3]}')
        print('Deseas cambiarlo a: \n1. In-Progress \n2. Pending \n3. Done')
        opcion_cambio = int(input('Ingresa el numero de opción que deseas: '))
        while opcion_cambio <1 or opcion_cambio>3:
            print('Opción no valida')
            opcion_cambio = int(input('Ingrese el número de la opción que elige: '))
        
        if opcion_cambio == 1:
            print('Su tarea a sido cambiada de estado "To-Do" a "In-Progress" de manera correcta! ')
            return ESTADOS_TAREA[1]
        elif opcion_cambio == 2:
            print('Su tarea a sido cambiada de estado "To-Do" a "Pending" de manera correcta! ')
            return ESTADOS_TAREA[2]
        elif opcion_cambio == 3:
            print('Su tarea a sido cambiada de estado "To-Do" a "Done" de manera correcta! ')
            return ESTADOS_TAREA[3]

    
    elif lista_tareas[posicion_tarea][3] == "In-Progress":
        print(f'El estado actual de tu tarea es: {lista_tareas[posicion_tarea][3]}')
        print('Deseas cambiarlo a: \n1. To-Do \n2. Pending \n3. Done')
        opcion_cambio = int(input('Ingresa el numero de opción que deseas: '))
        while opcion_cambio <1 or opcion_cambio>3:
            print('Opción no valida')
            opcion_cambio = int(input('Ingrese el número de la opción que elige: '))
        
        if opcion_cambio == 1:
            print('Su tarea a sido cambiada de estado "In-Progress" a "To-Do" de manera correcta! ')
            return ESTADOS_TAREA[0]
        elif opcion_cambio == 2:
            print('Su tarea a sido cambiada de estado "In-Progress" a "Pending" de manera correcta! ')
            return ESTADOS_TAREA[2]
        elif opcion_cambio == 3:
            print('Su tarea a sido cambiada de estado "In-Progress" a "Done" de manera correcta! ')
            return ESTADOS_TAREA[3]
    
    
    elif lista_tareas[posicion_tarea][3] == "Pending":
        print(f'El estado actual de tu tarea es: {lista_tareas[posicion_tarea][3]}')
        print('Deseas cambiarlo a: \n1. To-Do \n2. In-Progress \n3. Done')
        opcion_cambio = int(input('Ingresa el numero de opción que deseas: '))
        while opcion_cambio <1 or opcion_cambio>3:
            print('Opción no valida')
            opcion_cambio = int(input('Ingrese el número de la opción que elige: '))
        
        if opcion_cambio == 1:
            print('Su tarea a sido cambiada de estado "Pending" a "To-Do" de manera correcta! ')
            return ESTADOS_TAREA[0]
        elif opcion_cambio == 2:
            print('Su tarea a sido cambiada de estado "Pending" a "In-Progress" de manera correcta! ')
            return ESTADOS_TAREA[1]
        elif opcion_cambio == 3:
            print('Su tarea a sido cambiada de estado "Pending" a "Done" de manera correcta! ')
            return ESTADOS_TAREA[3]

    elif lista_tareas[posicion_tarea][3] == "Done":
        print(f'El estado actual de tu tarea es: {lista_tareas[posicion_tarea][3]}')
        print('Deseas cambiarlo a: \n1. To-Do \n2. In-Progress \n3. Pending')
        opcion_cambio = int(input('Ingresa el numero de opción que deseas: '))
        while opcion_cambio <1 or opcion_cambio>3:
            print('Opción no valida')
            opcion_cambio = int(input('Ingrese el número de la opción que elige: '))
        
        if opcion_cambio == 1:
            print('Su tarea a sido cambiada de estado "Done" a "To-Do" de manera correcta! ')
            return ESTADOS_TAREA[0]
        elif opcion_cambio == 2:
            print('Su tarea a sido cambiada de estado "Done" a "In-Progress" de manera correcta! ')
            return ESTADOS_TAREA[1]
        elif opcion_cambio == 3:
            print('Su tarea a sido cambiada de estado "Done" a "Pending" de manera correcta! ')
            return ESTADOS_TAREA[2]

#FUNCIONES PARA CONTAR TAREAS POR ESTADO
def contador_tarea_por_estado(lista_tareas, correo_usuario, estado_tarea):
    """
    Funcion para contar la cantidad de tareas con un estado dado y un correo
    (lista_tareas: list, correo_usuario: str, estado_tarea:str) -> contador: str
    """
    ESTADOS_TAREA = ["To-Do", "In-Progress", "Pending", "Done"]
    
    contador = 0
    for i in range(0,len(lista_tareas)):
        if lista_tareas[i][0] == correo_usuario and lista_tareas[i][3] == estado_tarea:
            contador = contador + 1
    
    return contador

def cantidad_tareas_estado(lista_usuarios, lista_tareas):
    """
    Funcion que imprime un pequeño menu y cuenta la cantidad de tareas por un estado llamando la funcion anterior
    (lista_usuarios list, lista_tareas: list) -> None
    """
    ESTADOS_TAREA = ["To-Do", "In-Progress", "Pending", "Done"]
    
    correo_usuario = revisar_correo(lista_usuarios, 1)
    
    print('Estados de tarea: \n1. To-Do \n2. In-Progress \n3. Pending \n4. Done')
    opcion_tarea_estado = int(input('Ingresa la opción de estado de tarea que deseas saber la cantidad: '))
    while opcion_tarea_estado <1 or opcion_tarea_estado>4:
        print('Estado no valido, ingresa un valor posible')
        opcion_tarea_estado = int(input('Ingresa la opción de estado de tarea que deseas: '))
    
    if opcion_tarea_estado == 1:
        cantidad_tareas = contador_tarea_por_estado(lista_tareas, correo_usuario, "To-Do")
        print(f"La cantidad de tareas que tienes en estado: 'To-Do', es: {cantidad_tareas}")
    elif opcion_tarea_estado == 2:
        cantidad_tareas = contador_tarea_por_estado(lista_tareas, correo_usuario, "In-Progress")
        print(f"La cantidad de tareas que tienes en estado: 'In-Progress', es: {cantidad_tareas}")
    elif opcion_tarea_estado == 3:
        cantidad_tareas = contador_tarea_por_estado(lista_tareas, correo_usuario, "Pending")
        print(f"La cantidad de tareas que tienes en estado: 'Pending', es: {cantidad_tareas}")
    elif opcion_tarea_estado == 4:
        cantidad_tareas = contador_tarea_por_estado(lista_tareas, correo_usuario, "Done")
        print(f"La cantidad de tareas que tienes en estado: 'Done', es: {cantidad_tareas}")

#BONOS
def tarea_atrasada(lista_tareas, lista_usuarios):
    """
    Mostrarle al usuario cuantos dias faltan para la tarea, y si la fecha
    ya pasó, mostrarle que ya vencio su tarea
    (lista_tareas:list, lista_usuarios:list) -> ()
    """
    correo_usuario = revisar_correo(lista_usuarios, 1)
    posicion_tarea = busqueda_tarea(lista_tareas, correo_usuario)

    fecha_tarea = datetime.strptime(lista_tareas[posicion_tarea][4], "%Y-%m-%d")
    fecha_hoy = datetime.strptime(str(date.today()), "%Y-%m-%d")

    if fecha_hoy >= fecha_tarea:
        print('La tarea esta vencida!')
    else:
        diferencia = fecha_tarea - fecha_hoy
        print(f"Falta(n) {diferencia.days} dia(s) para la fecha limite!")

def imprimir_tareas(lista_tareas, lista_usuarios):
    """
    Muestra al usuario sus tareas con descripcion, estado de tarea y fecha limite
    (lista_tareas:list, lista_usuarios:list) -> ()
    """
    correo_usuario = revisar_correo(lista_usuarios, 1)
    
    lista_posiciones = list()
    for posicion in range(0,len(lista_tareas)):
        if correo_usuario == lista_tareas[posicion][0]:
            lista_posiciones.append(posicion)
    
    print('')
    if len(lista_posiciones) == 0:
        print('No tienes tareas creadas!')
    
    else:
        for i in range(0, len(lista_posiciones)):
            print(f'Tarea Numero {i+1}:')
            print(f'Descripcion tarea: {lista_tareas[(lista_posiciones[i])][2]}')
            print(f'Estado tarea: {lista_tareas[lista_posiciones[i]][3]}')
            print(f'Fecha limite: {lista_tareas[lista_posiciones[i]][4]}')
            print('')
        
def main():
    """
    Funcion que organiza todas otras funciones
    ()->
    """
    #Valores iniciales
    usuarios = [["nombre_1", "correo_1", "ID_1"], ["nombre_2", "correo_2", "ID_2"]] #usuario: "nombre", "correo", "ID_unico"
    tareas = [["correo_1", "ID_tarea_1", "Calculo", "To-Do", "2025-11-25"]] #tarea: "correo", "ID_tarea", "Descripcion_tarea", "Estado_tarea", "Fecha Limite (AAAA-MM-D)"
    lista_id_usuarios = ["ID_1", "ID_2"]
    lista_id_tareas = ["ID_tarea_1"]

    opcion_primera_vez = primera_vez()
    if opcion_primera_vez == 1:
        usuario_nuevo, id_nuevo_usuario = registrar_nuevo_usuario(usuarios, lista_id_usuarios)
        usuarios.append(usuario_nuevo)
        lista_id_usuarios.append(id_nuevo_usuario)
 
        print('Usuario ingresado de manera correcta!')
        print('')
    
    elif opcion_primera_vez == 2:
        revisar_correo(usuarios, 1)

        print('Ingresas de manera correcta')
        print('')
    
    opcion_usuario_menu = menu()
    
    while opcion_usuario_menu != 7:
        #crear tarea
        if opcion_usuario_menu == 1:
            print('')
            tarea_nueva, id_generado_tarea = crear_tarea(usuarios, lista_id_tareas)
            tareas.append(tarea_nueva)
            lista_id_tareas.append(id_generado_tarea)
            print('')
        
        #cambiar estado tarea
        elif opcion_usuario_menu == 2:
            posicion, nuevo_estado = actualizar_tarea(usuarios, tareas)
            tareas[posicion][3] = nuevo_estado
        
        #Cantidad tareas en un estado dado
        elif opcion_usuario_menu == 3:
            cantidad_tareas_estado(usuarios, tareas)
        
        #Registrar nuevo usuario
        elif opcion_usuario_menu == 4:
            usuario_nuevo, id_nuevo_usuario = registrar_nuevo_usuario(usuarios, lista_id_usuarios)
            usuarios.append(usuario_nuevo)
            lista_id_usuarios.append(id_nuevo_usuario)
    
            print('Usuario ingresado de manera correcta!')
            print('')

        #Dias restantes
        elif opcion_usuario_menu == 5:
            tarea_atrasada(tareas, usuarios)
            print('')
        
        #Imprimir tarea
        elif opcion_usuario_menu == 6:
            imprimir_tareas(tareas, usuarios)
            print('')
            
        opcion_usuario_menu = menu()

    print('Saliste exitosamente del programa!')

main()