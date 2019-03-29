from db_conn import ConexionBD

class Centros:
    def __init__(self):
        self.__cod_centro = 0
        self.__centro_nombre = ""
        self.__cod_zbs = ""
        self.__db = ConexionBD()
    
    def leer_centros_ugc(self):
        query = 'SELECT COD_CENTRO,CENTRO_NOMBRE FROM CENTROS WHERE COD_ZBS like ? '
        valores = self.__cod_zbs
        return self.__db.ejecutar(query, valores)

    def setcod_ugc(self, codigo):
        self.__cod_zbs = codigo

    