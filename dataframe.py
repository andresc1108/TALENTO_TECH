import pandas as pd 

# Crear un diccionario con los datos
datos = {
    'Nombre': ['Juan', 'Maria', 'Pedro'],
    'Edad': [30, 25. 35]
}

# Crear un DataFrame a partir del diccionario
df = pd.DataFrame(datos)

# Guardar el DataFrame em un archivo CSV
df.to_csv('datos.csv', index=False)
