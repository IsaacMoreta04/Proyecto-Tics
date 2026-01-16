
#Modificar el login para intentos ilimitados
#Modificar para que la busqueda sea por apellido 
#Registrar los datos de profesor y las materias
#Agregar codigo para mostrar calificacion mas alta y baja 
#Modificar para que muestre el promedio general del curso 
#Sabado Nos organizamos para terminar el proyecto

Estudiantes = []
Nota_Final = 10
Notas = []


print("------------Bienvenido-----------\n")
print("Sistema de Gestión de Estudiantes ")

usuario = "admin"
clave = "890" 
intentos = 3

usuario = input("Ingrese el usuario:")
clave = input("Ingrese la clave:")

if usuario == "admin" and clave == "890":
        print("Acceso concedido")

else:
        print("Acceso denegado")

while (usuario != "admin" or clave != "890") and intentos > 1 :
        intentos -=1
        usuario = input("Ingrese el usuario:")
        clave = input("Ingrese la clave:")

if usuario == "admin" and clave == "890":
        print("Acceso concedido")       

else: 
        print("Acceso denegado ")

while (intentos == 1):
        print("Se han agotado los intentos. \n Acceso bloqueado.")
        exit()
        break


def agg_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    Estudiantes.append(nombre)
    print(f"Estudiante {nombre} agregado exitosamente.")
    nota = float(input("Ingrese la nota del estudiante: "))
    Notas.append(nota)
    if 7 <= nota <= Nota_Final:
        print(f"El estudiante {nombre} ha aprobado con una nota de {nota}.\n")
    elif 0 < nota < 7:
        print(f"El estudiante {nombre} ha reprobado con una nota de {nota}.\n")
    return

def mostrar_estudiantes():
    if Estudiantes:
        print("Lista de Estudiantes:")
        for estudiante in Estudiantes:
            print(f"- {estudiante}")
        for i in range(len(Estudiantes)):
            print(f"La nota de {Estudiantes[i]} es: {Notas[i]}")    

    else:
        print("No hay estudiantes registrados.\n")
    return

def buscar_estudiante():
    nombre = input("Ingrese el nombre del estudiante a buscar: ")
    if nombre in Estudiantes:
        print(f"El estudiante {nombre},está registrado.")
        print(f"La nota es: {Notas[Estudiantes.index(nombre)]}\n")
    else:
        print(f"El estudiante {nombre} no se encuentra en la lista.\n")
    return

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

while True:
    print("Menú de Opciones:")
    print("1. Agregar Estudiante")
    print("2. Mostrar Estudiantes")
    print("3. Buscar Estudiante")
    print("4. Promedio General")
    print("5. Salir")

    opcion = input("Seleccione una opción (1-5): ")

    if opcion == '1':
        agg_estudiante()
    elif opcion == '2':
        mostrar_estudiantes()
    elif opcion == '3':
        buscar_estudiante()
    elif opcion == '4':
        promedio_general()
    elif opcion == '5':
        print("Saliendo del sistema. ¡Hasta luego!")
        exit()
        break
     
    else:
        print("Opción inválida. Por favor, seleccione una opción del 1 al 5.\n")
