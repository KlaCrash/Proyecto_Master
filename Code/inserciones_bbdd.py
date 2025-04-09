import csv
import sqlite3

# Ruta del archivo CSV
csv_file = 'alojamientos.csv'

# Conectar a la base de datos SQLite
db_file = 'Proyecto_Master.sqlite'  # Cambia esto por la ruta de tu base de datos
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Abrir el archivo CSV y generar las inserciones
with open(csv_file, 'r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)  # Saltar la cabecera del CSV

    for row in reader:
        nombre = row[0]
        tipo = row[1]
        valoracion = row[2]
        ciudad = row[4]
        localizacion = row[3]
        distancia = row[5]
        cercanias = row[6]
        descripcion = row[7]

        # Generar la consulta SQL con parámetros
        sql = """
        INSERT INTO Alojamientos (nombre, tipo, valoracion, ciudad, localizacion, distancia, cercanias, descripcion)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        """
        try:
            # Ejecutar la consulta con los valores
            cursor.execute(sql, (nombre, tipo, valoracion, ciudad, localizacion, distancia, cercanias, descripcion))
        except sqlite3.Error as e:
            print(f"Error al insertar: {e}")
            print(f"Fila fallida: {row}")

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()
