# Programación 1 - Trabajo Práctico Integrador
# Gestión de Datos de Países en Python: filtros, ordenamientos y estadísticas

# Importamos módulo csv para el manejo de archivos CSV
# Importamos módulo os para verificar la existencia de archivos
import csv
import os

# Función para cargar los países desde un archivo CSV
def cargar_paises():
    # Lista para almacenar los países
    paises = []

    # Si el archivo no existe, se crea uno nuevo
    if not os.path.exists("datos_paises.csv"):
        with open("datos_paises.csv", "w", newline="", encoding="utf-8") as archivo:
            # Difinimos los encabezados
            encabezados = csv.DictWriter(archivo, fieldnames=["nombre", "continente", "poblacion", "superficie"])
            encabezados.writeheader()
            return paises

    # Si el archivo existe, se abre para lectura
    with open("datos_paises.csv", newline="", encoding="utf-8") as archivo:
        # Cada fila del CSV se convierte en un diccionario
        lector = csv.DictReader(archivo)

        # Iterar sobre cada fila del CSV y agregar a la lista de países
        for fila in lector:
            # Manejo seguro de conversión
            # Población
            poblacion_str = fila.get("poblacion", "").strip()
            if poblacion_str.isdigit():
                fila["poblacion"] = int(poblacion_str)
            else:
                # Asignamos 0 si el valor es inválido o vacío
                fila["poblacion"] = 0

            # Superficie
            superficie_str = fila.get("superficie", "").strip()
            if superficie_str.isdigit():
                fila["superficie"] = int(superficie_str)
            else:
                # Asignamos 0 si el valor es inválido o vacío
                fila["superficie"] = 0

            paises.append(fila)

    return paises

# Función para actualizar el archivo CSV con la lista de países
def actualizar_paises(paises):
    # Guardamos los cambios en el archivo CSV
    with open("datos_paises.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor_csv = csv.DictWriter(archivo, fieldnames=["nombre", "continente", "poblacion", "superficie"])
        escritor_csv.writeheader()
        escritor_csv.writerows(paises)

# Función para guardar país en una nueva línea del archivo CSV
def guardar_pais(pais):
    with open("datos_paises.csv", "a", newline="", encoding="utf-8") as archivo:
        escritor_csv = csv.DictWriter(archivo, fieldnames=["nombre", "continente", "poblacion", "superficie"])
        escritor_csv.writerow(pais)

    print(f"\nEl país '{pais['nombre']}' ha sido agregado exitosamente.")

# Función para mostrar nombre de países
def mostrar_nombres_paises(paises):
    print("\nLista de Países:")
    for pais in paises:
        print(f"- {pais['nombre']}")

# ------------------
# Funciones del menú
# ------------------

# 1) Buscar país por nombre
def buscar_pais():
    """Función para buscar un país por su nombre parcial o completo."""
    print("Opción seleccionada: 1 - Buscar país por nombre")

    # Solicitamos al usuario el nombre del país a buscar
    nombre_pais = input("\nIngrese el nombre del país que desea buscar (o 'salir' para volver al menú): ").strip()
    # Verificamos si el usuario desea salir
    if nombre_pais.lower() == "salir":
        print("Regresando al menú principal...")
        return

    # Cargamos los países desde el archivo CSV
    paises = cargar_paises()
    # Si la lista de países está vacía
    if not paises:
        print("\nNo hay países registrados.")
        return

    # Buscamos si el nombre ingresado coincide con algún país
    resultados = []
    for pais in paises:
        if nombre_pais.lower() in pais["nombre"].lower():
            resultados.append(pais)

    # Mostramos los resultados encontrados o un mensaje si no hay coincidencias
    if resultados:
        print(f"\nSe encontraron {len(resultados)} país(es) que coinciden con '{nombre_pais}':\n")
        for pais in resultados:
            print(f"Nombre: {pais['nombre']}")
            print(f"Continente: {pais['continente']}")
            print(f"Población: {pais['poblacion']}")
            print(f"Superficie: {pais['superficie']} km²")
            print("-" * 20)
    else:
        print(f"\nNo se encontraron países que coincidan con '{nombre_pais}'.")

# 2) Filtrar países
def filtrar_paises():
    """Funcion para filtrar países según el continente, población o superficie"""
    print("Opción seleccionada: 2 - Filtrar países")

    # Cargamos la lista de paises
    lista_paises = cargar_paises()
    if not lista_paises:
        print("\nLa lista de países está vacía.")
        return []

    # Población
    print("\nSeleccione el tamaño de población o deje vacio para ignorar\n")
    poblacion_min_str = input("Población mínima: ").strip()
    poblacion_max_str = input("Población máxima: ").strip()

    # Comprobamos que los datos ingresados sean válidos
    if poblacion_min_str and poblacion_min_str.isdigit():
        poblacion_min = int(poblacion_min_str)
    elif not poblacion_min_str:
        poblacion_min = 0  # valor si se deja vacio
    else:
        print("La población mínima ingresada no es válida")
        return []

    if poblacion_max_str and poblacion_max_str.isdigit():
        poblacion_max = int(poblacion_max_str)
    elif not poblacion_max_str:
        poblacion_max = float("inf")  # valor infinito si se deja vacio
    else:
        print("La población máxima ingresada no es válida")
        return []

    # Validar si la poblacion_min es menor o igual a poblacion_max
    if poblacion_min > poblacion_max:
        print("La población mínima no puede ser mayor que la población máxima.")
        return []
    
    # Superficie
    print("\nSeleccione el temaño de la superficie o deje vacio para ignorar\n")
    superficie_min_str = input("Superficie mínima: ").strip()
    superficie_max_str = input("Superficie máxima: ").strip()

    # Comprobamos que los datos ingresados sean válidos
    if superficie_min_str and superficie_min_str.isdigit():
        superficie_min = int(superficie_min_str)
    elif not superficie_min_str:
        superficie_min = 0  # valor si se deja vacio
    else:
        print("La superficie mínima ingresada no es válida")
        return []

    if superficie_max_str and superficie_max_str.isdigit():
        superficie_max = int(superficie_max_str)
    elif not superficie_max_str:
        superficie_max = float("inf")  # valor infinito si se deja vacio
    else:
        print("La superficie máxima ingresada no es válida")
        return []

    # Validar si la superficie_min es menor o igual a superficie_max
    if superficie_min > superficie_max:
        print("La superficie mínima no puede ser mayor que la superficie máxima.")
        return []
    
    # Continente
    print("\nSeleccione continente o deje vacio para ignorar\n")
    continente_filtro = input("Continente: ").strip().lower()
    if continente_filtro.isdigit():
        print("El continente ingresado no es válido")
        return []

    # Lista para almacenar los países que cumplen con los filtros
    paises_filtrados = []

    # Recorremos la lista de países y aplicamos los filtros
    for pais in lista_paises:
        # Obtenemos los valores del país actual
        poblacion = pais.get("poblacion", 0) # Si no existe, asignamos 0
        superficie = pais.get("superficie", 0)
        continente = pais.get("continente", "").strip().lower()

        # Verificamos si el país cumple con los criterios de filtrado
        filtro_poblacion = (poblacion >= poblacion_min) and (poblacion <= poblacion_max)
        filtro_superficie = (superficie >= superficie_min) and (superficie <= superficie_max)
        filtro_continente = (not continente_filtro) or (continente == continente_filtro)

        # Si cumple con todos los filtros, lo agregamos a la lista de filtrados
        if filtro_poblacion and filtro_superficie and filtro_continente:
            paises_filtrados.append(pais)

    print("\n::: Resultados del Filtro :::\n")
    if len(paises_filtrados) > 0:
        # Se muestran los países que cumplen con los filtros
        for pais in paises_filtrados:
            print(f"✅ {pais['nombre']} ({pais['continente']}) - Pob: {pais['poblacion']:,}, Sup: {pais['superficie']:,} km²")
    else:
        print("No se encontraron países que coincidan con los criterios.")

# 3) Ordenar países
def ordenar_paises():
    """Función para ordenar países según nombre, población o superficie"""
    print("Opción seleccionada: 3 - Ordenar países")

    # Funciones auxiliares de ordenamiento
    def ordenar_por_nombre(pais):
        return pais["nombre"].lower()
    def ordenar_por_poblacion(pais):
        return pais["poblacion"]
    def ordenar_por_superficie(pais): 
        return pais["superficie"]

    # Cargamos la lista de paises
    lista_paises = cargar_paises()
    if not lista_paises:
        print("\nLa lista de países está vacía.")
        return []

    # Solicitamos al usuario el tipo de ordenamiento
    while True:
        print("\n::: Seleccione una opción :::\n")
        print("1. Ordenar por Nombre")
        print("2. Ordenar por Población")
        print("3. Ordenar por Superficie")
        print("4. Salir")

        opcion = input("Selecciona un tipo de ordenamiento (1-4): ").strip()

        match opcion:
            case "1":
                # Ordenamos por nombre y guardamos en variables
                clave_ordenamiento = ordenar_por_nombre
                tipo_str = "Nombre"
                break
            case "2":
                # Ordenamos por poblacion y guardamos en variables
                clave_ordenamiento = ordenar_por_poblacion
                tipo_str = "Población"
                break
            case "3":
                # Ordenar por superficie u guardamos en variables
                clave_ordenamiento = ordenar_por_superficie
                tipo_str = "Superficie"
                break
            case "4":
                print("\nSaliendo...\n")
                return lista_paises
            case _:
                print("Selección inválida. Selecciona una opción del 1 al 4")

    orden = input("\nSeleccione orden (A) para ascendente o (D) para descendente: ").strip().lower()
    # Validamos la entrada del usuario
    if orden not in ["a", "d"]:
        print("El orden ingresado no es válido.")
        return
    # Determinamos si es ascendente o descendente mediante un booleano
    orden_descendente = orden == "d"

    # Ordenamos la lista de países según la clave y el orden seleccionado, mediante el método sorted()
    lista_ordenada = sorted(lista_paises, key=clave_ordenamiento, reverse=orden_descendente)

    if lista_ordenada:
        print(f"\nLista ordenada por {tipo_str} ({'Descendente' if orden_descendente else 'Ascendente'}).")
        print("\n::: Vista Previa de la Lista Ordenada (Top 5) :::\n")
        # Mostramos los primeros 5 países como vista previa
        for i, pais in enumerate(lista_ordenada[:5]):
            print(f"{i+1}. {pais['nombre']} | Pob: {pais['poblacion']:,} | Sup: {pais['superficie']:,} km²")

        # Si hay más de 5, indica cuántos más
        if len(lista_ordenada) > 5:
            print(f"... y {len(lista_ordenada) - 5} países más.\n")
    else:
        print("No se pudo ordenar la lista de países.")

# 4) Estadísticas de países
def estadisticas_paises():
    """Función para calcular y mostrar estadísticas de países"""
    print("Opción seleccionada: 4 - Estadísticas de países")

    # Cargamos la lista de paises
    lista_paises = cargar_paises()
    if not lista_paises:
        print("\nLa lista de países está vacía. No se pueden calcular estadísticas.")
        return

    print("\n:::: Estadísticas Generales ::::\n")

    # Inicialización de variables de cálculo
    poblacion_total = 0
    superficie_total = 0

    # Diccionario para contar países por continente
    paises_por_continente = {}

    # Inicialización para encontrar máximos y mínimos (asumimos el primer país como base)
    # Usamos .copy() para evitar modificar la lista original
    pais_mas_poblado = lista_paises[0].copy()
    pais_menos_poblado = lista_paises[0].copy()
    pais_mas_grande = lista_paises[0].copy()
    pais_mas_pequeno = lista_paises[0].copy()

    # Recorremos la lista de países para calcular totales y encontrar máximos/mínimos
    for pais in lista_paises:
        nombre = pais["nombre"]
        continente = pais["continente"]
        poblacion = pais["poblacion"]
        superficie = pais["superficie"]

        # Totales
        poblacion_total += poblacion
        superficie_total += superficie

        # Conteo por Continente
        # Usamos .title() para asegurar que la clave del continente sea uniforme (ej: 'Europa')
        continente_clave = continente.strip().title()
        paises_por_continente[continente_clave] = (
            paises_por_continente.get(continente_clave, 0) + 1
        )

        # País más/menos Poblado (Población)
        if poblacion > pais_mas_poblado["poblacion"]:
            pais_mas_poblado = pais.copy()
        if poblacion < pais_menos_poblado["poblacion"]:
            pais_menos_poblado = pais.copy()

        # País más/menos Grande (Superficie)
        if superficie > pais_mas_grande["superficie"]:
            pais_mas_grande = pais.copy()
        if superficie < pais_mas_pequeno["superficie"]:
            pais_mas_pequeno = pais.copy()

    # Cantidad de países
    cantidad_paises = len(lista_paises)

    # Promedios
    poblacion_promedio = poblacion_total / cantidad_paises
    superficie_promedio = superficie_total / cantidad_paises

    # Estadísticas Generales
    print(f"Número total de países: {cantidad_paises:,}")
    print(f"Población Total : {poblacion_total:,} habitantes")
    print(f"Población Promedio por País: {poblacion_promedio:,.0f} habitantes")
    print(f"Superficie Total: {superficie_total:,} km²")
    print(f"Superficie Promedio por País: {superficie_promedio:,.0f} km²")

    # Distribución por Continente
    print("\n:::: Distribución por Continente ::::\n")
    for continente, conteo in sorted(paises_por_continente.items()):
        print(f"  - {continente}: {conteo} países")

    ## Máximos y Mínimos
    print("\n::: Máximos y Mínimos :::\n")

    # Población
    print(f"  - País más poblado: {pais_mas_poblado['nombre']} ({pais_mas_poblado['poblacion']:,} habitantes.)")
    print(f"  - País menos poblado: {pais_menos_poblado['nombre']} ({pais_menos_poblado['poblacion']:,} habitantes.)")

    # Superficie
    print(f"  - País más grande: {pais_mas_grande['nombre']} ({pais_mas_grande['superficie']:,} km²)")
    print(f"  - País más pequeño: {pais_mas_pequeno['nombre']} ({pais_mas_pequeno['superficie']:,} km²)")
    print(":" * 45)

# 5) Agregar nuevo país
def agregar_pais():
    """Función para agregar un nuevo país a la lista"""
    print("Opción seleccionada: 5 - Agregar nuevo país")

    # Solicitamos al usuario el nombre del país a actualizar
    nombre_pais = input("\nIngrese el nombre del país que desea agregar (o 'salir' para volver al menú): ").strip()
    
    if nombre_pais.lower() == "salir":
        print("Regresando al menú principal...")
        return
    
    if nombre_pais == "" or nombre_pais.isdigit():
        print("Entrada inválida. El nombre del país no puede estar vacío o ser un número.")
        return

    # Verificamos si el país ya existe
    paises = cargar_paises()
    for pais in paises:
        if pais["nombre"].lower() == nombre_pais.lower():
            print(f"\nEl país '{nombre_pais}' ya existe en la lista.")
            return

    # Solicitamos los datos del nuevo país
    continente = input("Ingrese el continente del país: ").strip()
    poblacion = input("Ingrese la población del país: ").strip()
    superficie = input("Ingrese la superficie del país: ").strip()

    # Validamos que población y superficie sean números enteros
    if not (poblacion.isdigit() and superficie.isdigit()):
        print("Entrada inválida. La población y superficie deben ser números enteros.")
        return

    # Creamos un nuevo diccionario para el país
    nuevo_pais = {
        "nombre": nombre_pais,
        "continente": continente,
        "poblacion": int(poblacion),
        "superficie": int(superficie),
    }
    # Agregamos el nuevo país a la lista
    guardar_pais(nuevo_pais)

# 6) Actualizar datos de país
def actualizar_pais():
    """Función para actualizar los datos de un país existente"""
    print("Opción seleccionada: 6 - Actualizar datos de país")
    # Cargamos los países desde el archivo CSV
    paises = cargar_paises()
    # Mostramos los países disponibles
    mostrar_nombres_paises(paises)

    # Solicitamos al usuario el nombre del país a actualizar
    nombre_pais = input("\nIngrese el nombre del país que desea actualizar (o 'salir' para volver al menú): ").strip()
    # Verificamos si el usuario desea salir
    if nombre_pais.lower() == "salir":
        print("Regresando al menú principal...")
        return

    # Buscamos el país en la lista
    pais_encontrado = False
    for pais in paises:
        if pais["nombre"].lower() == nombre_pais.lower():
            pais_encontrado = True

            print(f"\nActualizando datos para el país: {pais['nombre']}")
            # Solicitamos nuevos datos al usuario
            nueva_poblacion = input(f"Ingrese la nueva población (actual: {pais['poblacion']}): ").strip()
            nueva_superficie = input(f"Ingrese la nueva superficie (actual: {pais['superficie']}): ").strip()

            # Actualizamos los datos si se proporcionaron nuevos valores
            if nueva_poblacion.isdigit() and nueva_superficie.isdigit():
                pais["poblacion"] = int(nueva_poblacion)
                pais["superficie"] = int(nueva_superficie)
            else:
                print("Entrada inválida. Los datos no fueron actualizados.")
                return

            # Actualizamos el archivo CSV
            actualizar_paises(paises)
            print(f"\nLos datos del país '{pais['nombre']}' han sido actualizados exitosamente.")
            break

    if not pais_encontrado:
        print(f"\nEl país '{nombre_pais}' no se encontró en la lista.")

# 7) Eliminar país
def eliminar_pais():
    """Función para eliminar un país de la lista"""
    print("Opción seleccionada: 7 - Eliminar país")
    # Cargamos los países desde el archivo CSV
    paises = cargar_paises()

    # Mostramos los países disponibles
    mostrar_nombres_paises(paises)

    # Solicitamos al usuario el nombre del país a eliminar
    nombre_pais = input("\nIngrese el nombre del país que desea eliminar (o 'salir' para volver al menú): ").strip()
    # Verificamos si el usuario desea salir
    if nombre_pais.lower() == "salir":
        print("Regresando al menú principal...")
        return

    # Buscamos el país en la lista
    pais_encontrado = False
    for pais in paises:
        if pais["nombre"].lower() == nombre_pais.lower():
            paises.remove(pais)
            pais_encontrado = True

            # Actualizamos el archivo CSV
            actualizar_paises(paises)
            print(f"\nEl país '{pais['nombre']}' ha sido eliminado exitosamente.")
            break

    if not pais_encontrado:
        print(f"\nEl país '{nombre_pais}' no se encontró en la lista.")

# Función para mostrar el menú y obtener la opción del usuario
def mostrar_menu():
    # Opciones del menú
    opciones_menu = [
        "1) Buscar país por nombre",
        "2) Filtrar países",
        "3) Ordenar países",
        "4) Estadísticas de países",
        "5) Agregar nuevo país",
        "6) Actualizar datos de país",
        "7) Eliminar país",
        "8) Salir",
    ]

    while True:
        print("\n --- Menú de Gestión de Países --- \n")
        # Mostramos las opciones del menú
        for opcion in opciones_menu:
            print(opcion)

        # Solicitamos la opción al usuario
        opcion_elegida = input("\nSeleccione una opción (1-8): ").strip()

        # Validamos si la opción ingresada es numérica
        if opcion_elegida.isdigit():
            # Convertimos la opción a entero
            opcion_elegida = int(opcion_elegida)

            # Estructura match-case para manejar las opciones del menú
            match opcion_elegida:
                case 1: buscar_pais()
                case 2: filtrar_paises()
                case 3: ordenar_paises()
                case 4: estadisticas_paises()
                case 5: agregar_pais()
                case 6: actualizar_pais()
                case 7: eliminar_pais()
                case 8:
                    print("Saliendo del programa...")
                    break
                case _:
                    print("Opción inválida. Por favor, seleccione una opción del 1 al 8.")
        else:
            print("Entrada inválida. Por favor, ingrese un número del 1 al 8.")

# Mostramos el menú al usuario
mostrar_menu()