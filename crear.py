# Crear una lista de numeros
numeros = [1, 2, 3, 4, 5]

# Crear un diccionario de nombres y edades
personas ={
    'Juan ' : 30,
    'Maria ' : 25,
    'Pedro ' : 28, 
}

#Guardar la lista en un archivo CSV
with open('numeros.csv', 'w') as archivo_csv:
    for numero in numeros:
        archivo_csv.write(f'{numero}\n')
                        
# Guardar el diccionario en un archivo txt 
with open("personas.txt", "w") as archivo_txt:
    for nombre, edad in personas.items():
        archivo_txt.write(f'{nombre}: {edad}\n')

print("Listo, los datos se han guardado en archivos 'numero.cvs' y 'personas.txt'") 
                      
