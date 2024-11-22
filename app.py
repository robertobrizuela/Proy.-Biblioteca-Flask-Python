import pymysql
from flask import Flask, render_template, request, redirect, url_for, flash
from pymysql.cursors import DictCursor

app = Flask(__name__)

# Establecer la clave secreta (esto es necesario para que funcione flash)
app.secret_key = 'tu_clave_secreta'

# Configuración de MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'biblioteca'
app.config['MYSQL_PORT'] = 3306  # Especifica el puerto en el que está corriendo MySQL

# Crear la conexión con la base de datos
def get_db_connection():
    connection = pymysql.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        db=app.config['MYSQL_DB'],
        port=app.config['MYSQL_PORT'],
        cursorclass=DictCursor  # Usar DictCursor para que los resultados sean diccionarios
    )
    return connection

# Ruta de inicio
@app.route('/')
def inicio():
    return render_template('index.html')

# Ruta de alta de libro (formulario)
@app.route('/alta/')
def alta():
    return render_template('alta.html')

# Ruta para insertar un libro en la base de datos
@app.route('/add_libro', methods=['POST'])
def alta_libro():
    try:
        # Recibir datos del formulario
        titulo = request.form['titulo']
        editorial = request.form['editorial']
        autor = request.form['autor']
        numero_paginas = request.form['numero_paginas']
        edicion = request.form['edicion']
        
        # Conectar a la base de datos
        connection = get_db_connection()
        cursor = connection.cursor()

        # Insertar el libro en la base de datos
        cursor.execute(
            "INSERT INTO libros (titulo, editorial, autor, numero_paginas, edicion) "
            "VALUES (%s, %s, %s, %s, %s)",
            (titulo, editorial, autor, numero_paginas, edicion)
        )

        # Confirmar que los cambios se guarden
        connection.commit()
        connection.close()
        
        # Mensaje flash de éxito
        flash("Libro almacenado en la base de datos correctamente.", "success")

    except Exception as e:
        flash(f"Error al almacenar el libro: {e}", "danger")

    # Redirige al formulario de alta de libro con el mensaje flash
    return redirect(url_for('alta'))

# Ruta para mostrar todos los libros
@app.route('/libros')
def libros():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM libros")
    libros = cursor.fetchall()
    connection.close()
    return render_template('libros.html', libros=libros)


@app.route('/almacenamiento')
def almacenamiento():
    try:
        # Usar pymysql para la conexión
        conn = get_db_connection()
        cursor = conn.cursor()  # DictCursor ya está configurado
        cursor.execute("SELECT * FROM libros")
        datos = cursor.fetchall()
        cursor.close()
        conn.close()
        
        # Los datos ya son un diccionario, no es necesario convertir manualmente
        return render_template('almacenamiento.html', libros=datos)
    except pymysql.MySQLError as err:
        flash(f"Error al obtener los datos: {err}")
        return redirect(url_for('alta'))


@app.route('/modificar/<int:id>', methods=['GET', 'POST'])
def modificar_libro(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # Obtener el libro que se desea modificar
    cursor.execute("SELECT * FROM libros WHERE id = %s", (id,))
    libro = cursor.fetchone()
    
    if not libro:
        flash("El libro no fue encontrado", "danger")
        return redirect(url_for('almacenamiento'))

    if request.method == 'POST':
        # Obtener los datos del formulario
        titulo = request.form['titulo']
        autor = request.form['autor']
        editorial = request.form['editorial']
        edicion = request.form['edicion']
        
        # Actualizar el libro en la base de datos
        cursor.execute("""
            UPDATE libros 
            SET titulo = %s, autor = %s, editorial = %s, edicion = %s 
            WHERE id = %s
        """, (titulo, autor, editorial, edicion, id))
        connection.commit()
        connection.close()
        
        flash("Libro actualizado correctamente.", "success")
        return redirect(url_for('almacenamiento'))

    # Si es un GET, mostrar el formulario de modificación con los datos del libro
    connection.close()
    return render_template('modificar.html', libro=libro)




# Ruta para eliminar un libro
@app.route('/eliminar_libro/<int:id>', methods=['GET'])
def eliminar_libro(id):
    try:
        # Conectar a la base de datos
        connection = get_db_connection()
        cursor = connection.cursor()

        # Ejecutar la consulta para eliminar el libro por su ID
        cursor.execute("DELETE FROM libros WHERE id = %s", (id,))
        connection.commit()
        connection.close()

        flash("Libro eliminado correctamente.", "success")
    except Exception as e:
        flash(f"Error al eliminar el libro: {e}", "danger")

    return redirect(url_for('almacenamiento'))



@app.route('/buscar', methods=['POST'])
def buscar_libros():
    # Obtener el término de búsqueda del formulario
    titulo = request.form['titulo']
    
    # Conectar a la base de datos y realizar la consulta
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM libros WHERE titulo LIKE %s", (f"%{titulo}%",))
    resultados = cursor.fetchall()
    connection.close()

    # Renderizar una página de resultados
    return render_template('resultados.html', resultados=resultados, termino=titulo)


# Manejo de errores 404
@app.errorhandler(404)
def page_not_found(err):
    return 'Página no encontrada!'

if __name__ == '__main__':
    app.run(debug=True)
