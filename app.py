# app.py

from flask import Flask
from data.data_productos import productos, categorias

app = Flask(__name__)

@app.route("/")
def home():
    nombre = "Emanuel Cas"
    descripcion = "Soy alumno del curza. Me interesa la programación, desarrollo web y la enseñanza."
    return f"Hola! Soy {nombre}. {descripcion}"

@app.route("/productos")
def listar_productos():
    salida = "Lista de Productos:<br>"
    for p in productos:
        salida += f"ID: {p['id']} - Descripción: {p['descripcion']} - Categoría ID: {p['categoria_id']}<br>"
    return salida

@app.route("/categorias")
def listar_categorias():
    salida = "Lista de Categorías:<br>"
    for c in categorias:
        salida += f"ID: {c['id']} - Descripción: {c['descripcion']}<br>"
    return salida

if __name__ == "__main__":
    app.run(debug=True)
