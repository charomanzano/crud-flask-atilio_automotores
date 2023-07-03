from flask import Flask, render_template, request
from PIL import Image
import pytesseract
import pandas as pd
from sqlalchemy import create_engine
from fuzzywuzzy import fuzz

app = Flask(__name__)

# Configuración de la conexión a la base de datos PostgreSQL
db_config = {
    'host': 'localhost',
    'port': '5435',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
}

# Crear el motor SQLAlchemy
engine = create_engine(
    f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}")


def normalizar_dato(dato):
    dato = dato.upper()

    if fuzz.partial_ratio(dato, 'DOMINIO') >= 70:
        return 'Dominio'
    elif fuzz.partial_ratio(dato, 'MARCA') >= 80:
        return 'Marca'
    elif fuzz.partial_ratio(dato, 'MODELO') >= 80:
        return 'Modelo'
    elif fuzz.partial_ratio(dato, 'TIPO') >= 80:
        return 'Tipo'
    elif fuzz.partial_ratio(dato, 'USO') >= 70:
        return 'Uso'
    elif fuzz.partial_ratio(dato, 'CHASIS') >= 80:
        return 'Chasis'
    elif fuzz.partial_ratio(dato, 'MOTOR') >= 80:
        return 'Motor'
    else:
        return dato


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    # Validar el archivo recibido
    file = request.files['file']
    if not file or not allowed_file(file.filename):
        return 'Archivo no válido'

    # Procesar la imagen y extraer los datos utilizando pytesseract
    img = Image.open(file)
    text = pytesseract.image_to_string(img)

    # Obtener el precio de toma y las observaciones del formulario
    precio_toma = request.form['precio_toma']
    observaciones = request.form['observaciones']

    # Dividir el texto en líneas y limpiar los espacios en blanco
    lines = [line.strip() for line in text.split('\n')]

    # Crear una lista de listas con las líneas de texto
    data = [line.split(':') for line in lines if line]

    # Agregar el precio de toma y las observaciones a los datos
    data.append(['Precio Toma', precio_toma])
    data.append(['Observaciones', observaciones])

    # Crear el DataFrame con los datos obtenidos
    df = pd.DataFrame(data, columns=['Dato', 'Valor'])

    # Eliminar filas con valores nulos o vacíos en las columnas 'Dato' y 'Valor'
    df.dropna(subset=['Dato', 'Valor'], inplace=True)
    df = df[(df['Dato'] != '') & (df['Valor'] != '')]

    # Validar los nombres de las columnas y actualizar el DataFrame si no hay coincidencia
    df['Dato'] = df['Dato'].apply(normalizar_dato)

    # Guardar el DataFrame en la tabla de la base de datos
    # Nombre de la tabla en la que deseas almacenar el DataFrame
    table_name = 'df'
    df.to_sql(table_name, engine, if_exists='append', index=False)

    # Renderizar resultados.html y obtener el HTML resultante
    resultados_html = render_template('resultados.html', data=df)

    return render_template('index.html', resultados_html=resultados_html, data=df)


def allowed_file(filename):
    # Verificar si la extensión del archivo es válida
    allowed_extensions = {'png', 'jpg', 'jpeg'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions


if __name__ == '__main__':
    app.run(debug=True, port=5001)
