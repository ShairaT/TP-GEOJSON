from class_DB import DB
import pprint
import pymongo
db = DB()
class Aeropuertos(object):


    _id = None
    code = None
    lat = None
    lon = None
    name = None
    city = None
    state = None
    country = None
    woeid = None
    tz = None
    phone = None
    type = None
    email = None
    url = None
    runway_length = None
    elev = None
    icao = None
    direct_flights = None
    carriers = None

    def DeserializarAeropuertos(self, diccionario):
        self._id = diccionario["_id"]
        self.code = diccionario["code"]
        self.lat = diccionario["lat"]
        self.lon = diccionario["lon"]
        self.name = diccionario["name"]
        self.city = diccionario["city"]
        self.state = diccionario["state"]
        self.country = diccionario["country"]
        self.woeid = diccionario["woeid"]
        self.tz = diccionario["tz"]
        self.phone = diccionario["phone"]
        self.type = diccionario["type"]
        self.email = diccionario["email"]
        self.url = diccionario["url"]
        self.runway_length = diccionario["runway_length"]
        self.elev = diccionario["elev"]
        self.icao = diccionario["icao"]
        self.direct_flights = diccionario["direct_flights"]
        self.carriers = diccionario["carriers"]

    @staticmethod
    def SeleccionarTodosAeropuertos():
        listaPais = []
        listaCiudad = []
        listaNombre = []
        for post in db.collection.find({}):
            if post["country"] not in listaPais:
                listaPais.append(post["country"])
            if post["city"] not in listaCiudad:
                listaCiudad.append(post["city"])
            if post["name"] not in listaNombre:
                listaNombre.append(post["name"])
        return listaPais, listaCiudad, listaNombre

    @staticmethod
    def SeleccionarNombreAeropuerto(nombre_aeropuerto):
        select_cursor = db.collection.find({"name": str(nombre_aeropuerto)})
        d = select_cursor.fetchall()
        aeropuerto = Aeropuertos()
        aeropuerto.DeserializarAeropuertos(d)
        return aeropuerto

    @staticmethod
    def SelecionarPais(pais):
        lista = []
        for post in db.collection.find({"country": str(pais)}):
            aeropuerto = Aeropuertos()
            aeropuerto.DeserializarAeropuertos(post)
            if Aeropuertos.BuscarPais(lista, aeropuerto):
                lista.append(aeropuerto)
        return lista

    @staticmethod
    def SeleccionarCiudad(ciudad):
        lista = []
        for post in db.collection.find({"city": str(ciudad)}):
            aeropuerto = Aeropuertos()
            aeropuerto.DeserializarAeropuertos(post)
            if Aeropuertos.BuscarCosa(lista, aeropuerto) == True:
                lista.append(aeropuerto)
        return lista
    @staticmethod

    def BuscarCiudad(lista, nuevo):
        for item in lista:
            if item.city == nuevo.city:
                return False
        return True
    @staticmethod
    def BuscarPais(lista, nuevo):
        for item in lista:
            if item.country == nuevo.country:
                return False
        return True