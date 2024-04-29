def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    carrera = input("Ingrese la carrera del estudiante: ")

    with open("estudiantes.txt", "a") as archivo:
        archivo.write(f"{nombre},{edad},{carrera}\n")

agregar_estudiante
