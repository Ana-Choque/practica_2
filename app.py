from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inscripcion_curso', methods=['GET', 'POST'])
def inscripcion_curso():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        curso = request.form['curso']
        # Lógica para manejar los datos recibidos
    return render_template('inscripcion_curso.html')

@app.route('/registro_usuarios', methods=['GET', 'POST'])
def registro_usuarios():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        # Lógica para manejar los datos recibidos
    return render_template('registro_usuarios.html')

@app.route('/registro_productos', methods=['GET', 'POST'])
def registro_productos():
    if request.method == 'POST':
        producto = request.form['producto']
        categoria = request.form['categoria']
        existencia = request.form['existencia']
        precio = request.form['precio']
        # Lógica para manejar los datos recibidos
    return render_template('registro_productos.html')

@app.route('/registro_libros', methods=['GET', 'POST'])
def registro_libros():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        resumen = request.form['resumen']
        medio = request.form['medio']
        # Lógica para manejar los datos recibidos
    return render_template('registro_libros.html')

if __name__ == '__main__':
    app.run(debug=True)