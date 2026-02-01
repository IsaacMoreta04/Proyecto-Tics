Estudiantes = []
Nota_Final = 10
Notas = []

Materias = [] 


print("------------Bienvenido-----------\n")
print("Sistema de Gestión de Estudiantes ") 

usuario_prof = "Alejandro_docente@esfot.edu.ec"
clave_prof = "Chicaiza2026"       


while True:
    usuario = input("Ingrese el usuario: ")
    clave = input("Ingrese la clave: ")

    if usuario == usuario_prof and clave == clave_prof:
        print("Acceso concedido")
        break   
    else:
        print("Acceso denegado, intente nuevamente")

def agg_estudiante():

    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    Estudiantes.append(nombre + " " + apellido)
    print(f"Estudiante {nombre}{apellido} agregado exitosamente.")
    nota = float(input("Ingrese la nota del estudiante: "))
    Notas.append(nota)
    if 7 <= nota <= Nota_Final:
        print(f"El estudiante {nombre} {apellido} ha aprobado con una nota de {nota}.\n")
    elif 0 < nota < 7:
        print(f"El estudiante {nombre} {apellido} ha reprobado con una nota de {nota}.\n")
    return

def mostrar_estudiantes():
    if Estudiantes:
        print("\n lista de estudiantes y notas ")

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
def buscar_estudiante():
    apellido = input("Ingrese el apellido del estudiante a buscar: ")
    encontrado = False

    for i, estudiante in enumerate(Estudiantes):
       
        partes = estudiante.split()
        apellido_estudiante = partes[-1]

        if apellido.lower() == apellido_estudiante.lower():
            print(f"El estudiante {estudiante} está registrado.")
            print(f"La nota es: {Notas[i]}\n")
            encontrado = True
            break

    if not encontrado:
        print(f"No se encuentra ningún estudiante con el apellido '{apellido}'.\n")

def promedio_general():
    total_notas = 0
    cantidad_estudiantes = len(Estudiantes)
    if cantidad_estudiantes == 0:
        print("No hay estudiantes para calcular el promedio.\n")
        return
    for estudiante in Estudiantes:
        nota = float(input(f"Ingrese la nota del estudiante {estudiante}: "))
        total_notas += nota
    promedio = total_notas / cantidad_estudiantes
    print(f"El promedio general de notas es: {promedio:.2f}\n")
    return

def estudiantes_aprobados():
    print("Los estudiantes aprovados son: .\n")
    for i in range(len(Estudiantes)):
        if Notas[i] >= Nota_Final:
            print(f"- {Estudiantes[i]} con nota {Notas[i]}")
    return

def estudiantes_reprobados():
    print("Los estudiantes reprovados son: .\n")
    for i in range(len(Estudiantes)):
        if Notas[i] < Nota_Final:
            print(f"- {Estudiantes[i]} con nota {Notas[i]}")
    return

def agregar_materia():          
    materia = input("Ingrese el nombre de la materia: ")
    Materias.append(materia)
    print(f"Materia '{materia}' agregada correctamente.\n")

def menu_profesor():           
    while True:
        print("\n--- MENÚ PROFESOR ---")
        print("1. Agregar Materia")
        print("2. Ver Materias")
        print("3. Salir")

        op = input("Seleccione una opción: ")

        if op == '1':
            agregar_materia()
        elif op == '2':
            print("Lista de Materias:")
            for m in Materias:
                print("-", m)
        elif op == '3':
            print("Saliendo del menú profesor...")
            break
        else:
            print("Opción inválida")


while True:
    
    print("Menú de Opciones:")
    print("1. Menu Profesores")       
    print("2. Agregar Estudiante")
    print("3. Mostrar Estudiantes")
    print("4. Buscar Estudiante")
    print("5. Promedio General")
    print("6. Salir")

    opcion = input("Seleccione una opción (1-5): ")

    if opcion == '1':
        menu_profesor()
    elif opcion == '2':
        agg_estudiante()
    elif opcion == '3':
        mostrar_estudiantes()
    elif opcion == '4':
        buscar_estudiante()
    elif opcion == '5':
        promedio_general()
    elif opcion == '6':
        print("Saliendo del sistema. ¡Hasta luego!")
        exit()
        break
     
    else:
        print("Opción inválida. Por favor, seleccione una opción")

