import psycopg2

# Establecer la conexión con la base de datos
conn = psycopg2.connect(
    host="localhost",
    port="5435",
    database="postgres",
    user="postgres",
    password="postgres"
)

# Crear un cursor para ejecutar consultas
cursor = conn.cursor()

# Definir el nombre de la tabla
tabla = "datos_imagenes"

# Crear la tabla si no existe
create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {tabla} (
        dominio TEXT,
        marca TEXT,
        modelo TEXT,
        tipo TEXT,
        uso TEXT,
        chasis TEXT,
        motor TEXT,
        vence TEXT
    )
"""
cursor.execute(create_table_query)
conn.commit()

# Insertar datos de ejemplo en la tabla
insert_query = f"""
    INSERT INTO {tabla} (dominio, marca, modelo, tipo, uso, chasis, motor, vence)
    VALUES ('FIV130', 'VOLKSWAGEN', 'FOX 1.6', 'SEDAN 3 PUERTAS', 'PRIVADO', '9BWKB05Z864062702', 'BAH265341', '15/10/2022')
"""
cursor.execute(insert_query)
conn.commit()

# Cerrar la conexión con la base de datos
cursor.close()
conn.close()
