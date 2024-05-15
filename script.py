import os
import pandas as pd

# Definir la ruta de la carpeta
ruta_carpeta = "data"

# Listar archivos CSV en la carpeta
archivos_csv = [archivo for archivo in os.listdir(ruta_carpeta) if archivo.endswith(".csv")]

len_rows = 0

# Recorrer cada archivo CSV
for archivo_csv in archivos_csv:
    # Obtener la ruta completa del archivo
    ruta_archivo = os.path.join(ruta_carpeta, archivo_csv)

    # Leer el archivo CSV en un DataFrame de Pandas
    df = pd.read_csv(ruta_archivo)

    len_rows += len(df)    


print('total rows: ', + len_rows)


ruta_carpeta = "data"

# Listar archivos CSV en la carpeta
archivos_csv = [os.path.join(ruta_carpeta, archivo) for archivo in os.listdir(ruta_carpeta) if archivo.endswith(".csv")]

# Leer el primer archivo CSV en un DataFrame de Pandas
df1 = pd.read_csv(archivos_csv[0])

# Recorrer los demás archivos CSV
for archivo_csv in archivos_csv[1:]:
  # Leer el archivo CSV actual en un DataFrame de Pandas
  df2 = pd.read_csv(archivo_csv)

  # Sumar los DataFrames
  df1 = pd.concat([df1, df2], axis=0, ignore_index=True)

# Guardar el DataFrame combinado en un nuevo archivo CSV
print(len(df1))
df1.to_csv("data/all.csv", index=False, encoding='utf-8')