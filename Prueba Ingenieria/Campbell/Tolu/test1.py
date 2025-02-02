import pandas as pd

# Ruta al archivo de datos
file_path = 'prueba tolu.txt'

# Leer el archivo saltando la primera línea y tomando la segunda y tercera como nombres de columnas
df_o = pd.read_csv(file_path, delimiter='\t', skiprows=1, header=1)
names = ['Fecha','RadAlb',
 'RadRef',
 'RadSolar1',
 'Temperature_HV',
 'RadSolar2',
 'Humidity_HV',
 'lluvia_total',
 'Direccion_Viento',
 'Albedo',
 'Pressure',
 'Velocidad_Viento']

# Read the file at file_path starting from position 2 and assign the columns using names
df_o = pd.read_csv(file_path, delimiter='\t', skiprows=1, header=1, names=names)
df_o.head()