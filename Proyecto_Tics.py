# Listas Utilizadas

Estudiantes = []
Nota_Final = 10
Notas = []

Materias = [] 
datos_docente = []

# Ingreso de Credenciales del Docente

print("="*90)
print("                         Bienvenido      ")
print("="*90)
print("                 Sistema de Gestión de Estudiantes ") 
print("="*90)
usuario_prof = "Alejandro_docente@esfot.edu.ec"
clave_prof = "Chicaiza2026"       

while True:

    usuario = input("Ingrese el usuario: ")
    clave = input("Ingrese la clave: ")

    if usuario == usuario_prof and clave == clave_prof:
        print("Acceso concedido")
        print(f"Bienvenido docente {usuario_prof}")
        break 

    else:
        print("Acceso denegado, intente nuevamente")

# Registro de Estudiantes y Notas

def agg_estudiante():

    while True:

        nombre = input("Ingrese el nombre del estudiante: ")
        apellido = input("Ingrese el apellido del estudiante: ")
        nota = float(input("Ingrese la nota del estudiante: "))

        if nota < 0 or nota > Nota_Final:
            print(f"\nLa nota ingresada {nota} es inválida. Debe estar entre 0 y {Nota_Final}.\n")

        else:
            Estudiantes.append(nombre + " " + apellido)
            Notas.append(nota)
            print(f"Estudiante {nombre} {apellido} agregado exitosamente.")

            if 7 <= nota <= Nota_Final:
                print(f"\nEl estudiante {nombre} {apellido} ha aprobado con una nota de {nota}.\n")

            else:
                print(f"\nEl estudiante {nombre} {apellido} ha reprobado con una nota de {nota}.\n")

        print("Presione Enter para continuar o escriba 'salir' para volver al menú principal: ")
        salir = input()

        if salir.lower() == 'salir':
            break

# Mostrar Estudiantes y Desempeño

def mostrar_estudiantes():

    if Estudiantes:
        print("\n Lista de estudiantes y notas ")

        lista_ordenada = sorted(zip(Estudiantes, Notas), key=lambda x: x[1], reverse=True)
        
        for estudiante, nota in lista_ordenada:
            print(f"- {estudiante} | Nota: {nota}")
            
        nota_maxima = max(Notas)
        nota_minima = min(Notas)
        promedio = sum(Notas) / len(Notas)

        print("\n---------------------------------------")
        print(f"» Calificación más alta: {nota_maxima}")  
        print(f"» Calificación más baja: {nota_minima}")
        print(f"» Promedio General:      {promedio:.2f}")
        print("---------------------------------------\n")
        
    else:
        print("\nNo hay estudiantes registrados aún. Vaya a la Opción 1 primero.\n")
        return
    
# Busqueda de Estudiante por Apellido
    
def buscar_estudiante():

    while True:

        apellido = input("\nIngrese el apellido del estudiante a buscar: ")
        encontrado = False

        for i, estudiante in enumerate(Estudiantes):
            partes = estudiante.split()
            apellido_estudiante = partes[-1]

            if apellido.lower() == apellido_estudiante.lower():
                print(f"El estudiante {estudiante} está registrado.")
                print(f"La nota es: {Notas[i]}\n")
                encontrado = True

        if not encontrado:
            print(f"No se encuentra ningún estudiante con el apellido '{apellido}'.\n")

        print("Presione Enter para continuar o escriba 'salir' para volver al menú principal: ")
        salir = input()

        if salir.lower() == 'salir':
            break
# Visualizacion de Reportes

def estudiantes_aprobados():
    print("\nLos estudiantes aprobados son:\n")
    encontrado = False

    for i in range(len(Estudiantes)):
        if 7 <= Notas[i] <= Nota_Final:
            print(f"- {Estudiantes[i]} con nota {Notas[i]}")
            encontrado = True

    if not encontrado:
        print("No hay estudiantes aprobados.\n")


def estudiantes_reprobados():
    print("\nLos estudiantes reprobados son:\n")
    encontrado = False

    for i in range(len(Estudiantes)):
        if 0 <= Notas[i] < 7:
            print(f"- {Estudiantes[i]} con nota {Notas[i]}")
            encontrado = True

    if not encontrado:
        print("No hay estudiantes reprobados.\n")

# Registro de Materias        

def agregar_materia():

    while True:

        materia = input("Ingrese el nombre de la materia: ").strip()

        if materia == "":
            print("El nombre de la materia no puede estar vacío.\n")
        elif materia.lower() in [m.lower() for m in Materias]:
            print(f"La materia '{materia}' ya existe en la lista.\n")
        else:
            Materias.append(materia)
            print(f"Materia '{materia}' agregada correctamente.\n")

        print("Presione Enter para continuar o escriba 'salir' para volver al menú principal: ")
        salir = input()
        if salir.lower() == 'salir':
            break

# Registro y Menu del Docente

def menu_profesor():  

    while True:

        print("                 MÓDULO DEL DOCENTE ")
        print("="*90)
        print("1. Registrar datos del Docente")
        print("2. Registrar Materia")
        print("3. Ver datos y materias")
        print("4. Volver")
        op = input("Seleccione una opcion (1-4): ")
        print("="*90)
        
        if op == '1':
            nom = input("Nombre: ")
            ape = input("Apellido: ")
            datos_docente.append(f"{nom} {ape}")
            print("Datos guardados.")
            print("="*90)
        elif op == '2':
            agregar_materia()
        elif op == '3':
            prof = datos_docente[-1] if datos_docente else "No registrado"
            print(f"Docente: {prof}")
            print(f"Materias: {Materias}")
            print("="*90)
        elif op == '4': 
            break
        else:
            print("Opción inválida")

# Menú Principal

while True:
    
    print("="*90)
    print("                 Menú de Opciones")
    print("="*90)   
    print("1. Menu Profesores")       
    print("2. Agregar Estudiante")
    print("3. Mostrar Estudiantes")
    print("4. Buscar Estudiante")
    print("5. Reporte de Estudiantes")
    print("6. Salir")
    print("="*90)
    opcion = input("Seleccione una opción (1-6): ")
    print("="*90)

    if opcion == '1':
        menu_profesor()
    elif opcion == '2':
        agg_estudiante()
    elif opcion == '3':
        mostrar_estudiantes()
    elif opcion == '4':
        buscar_estudiante()
    elif opcion == '5':
        estudiantes_aprobados()
        estudiantes_reprobados()
    elif opcion == '6':
        print("Saliendo del sistema. ¡Hasta luego!")
        exit()
        break
     
    else:
        print("Opción inválida. Por favor, seleccione una opción")
