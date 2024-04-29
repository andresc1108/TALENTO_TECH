class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Carrera:", self.carrera)

    def leer_estudiantes():
        with open("estudiantes.txt, "r)  as archivo:
            lineas = archivo.readlines()
            for linea in lineas: 
                partes = linea.strip().split(",")
                nombre, edad, carrera = partes
                Estudiante = Estudiante(nombre, int (edad), carrera)
                Estudiante.mostrar_info()

    leer_estudiantes()
