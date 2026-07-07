import pymongo
import pymongo.errors

class conexionDB():
    def __init__(self):
        self.mongo_host = "localhost"
        self.mongo_puerto = 27017
        self.mongo_tiempo = 500
        self.mongo_db = "pruebaFinal"
        self.mongo_url = f"mongodb://{self.mongo_host}:{self.mongo_puerto}/"
        
    def conectarse(self):
        try:
            cliente = pymongo.MongoClient(self.mongo_url)
            db = cliente[self.mongo_db]
            print("conexion exitosa")
            return db
         #se ejecuta este mesaje en caso que el tiempo de conexion se exceda a los 1000  milisegundos  
        except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
            print("Tiempo excedido"+ errorTiempo)
        #se ejecuta este mensaje en caso ocurra un error de conexion     
        except pymongo.errors.ConnectionFailure as errorConexion:
            print("Fallo al conectarse a mongodb"+errorConexion)

        