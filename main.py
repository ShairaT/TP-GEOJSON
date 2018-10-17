from pymongo import MongoClient
import pprint
from flask import request, jsonify, render_template, Flask, redirect, session
from class_DB import DB
from class_Aeropuertos import Aeropuertos

db = DB()

listaNombreAeropuertos = Aeropuertos.SeleccionarTodosAeropuertos()[2]
listaCiudades = Aeropuertos.SeleccionarTodosAeropuertos()[1]
listaPaises = Aeropuertos.SeleccionarTodosAeropuertos()[0]
listatodo = listaCiudades+listaPaises+listaNombreAeropuertos
aeropuertosDeLaCiudad = []
aeropuertosDelPais = []
aeropuerto = ""

app = Flask(__name__)

@app.route("/")
def PaginaPrincipal():
    return render_template("GeoPagina.html", listaPaises = listaPaises, listaCiudades = listaCiudades,
                           listaNombreAeropuertos = listaNombreAeropuertos, listaTodo=listatodo)

@app.route("/complete", methods=["POST", "GET"])
def complete():
    busque = request.form.get("Busqueda")
    if busque in listaCiudades:
        aeropuertosDeLaCiudad = Aeropuertos.SeleccionarCiudad(busque)
    if busque in listaPaises:
        aeropuertosDelPais = Aeropuertos.SelecionarPais(busque)
    if busque in listaNombreAeropuertos:
        aeropuerto = Aeropuertos.SeleccionarNombreAeropuerto(busque)

    return redirect("/buscado")

@app.route("/buscado")
def buscado():



if __name__ == "__main__":
    app.run(debug=True)