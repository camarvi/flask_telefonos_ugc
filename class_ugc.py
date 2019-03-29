from db_conn import ConexionBD

class Ugc:
    def __init__(self):
        self.id = 0
        self.cod_zbs = ''
        self.zbs = ''
        self.db = ConexionBD()

    #def crear(self):
    #    """ CREAR UN NUEVO REGISTRO"""
    #    query = "INSERT INTO ZONAS_BASICAS (id,cod_zbs, zbs) values (null, %s, %s)"
    #    valores = (self.cod_zbs, self.zbs)
    #    self.db.ejecutar(query, valores)

    #def update(self):
    #    """ ACTUALIZAR UN REGISTRO EXISTENTE"""
    #    query = "UPDATE ZONAS_BASICAS SET COD_ZBS= %s , ZBS= %s WHERE ID = %s"
    #    valores = (self.cod_zbs, self.zbs, self.id)
    #    return self.db.ejecutar(query, valores)

    def read_all(self):
        """ LEER TODOS LOS REGISTROS"""
        query = "SELECT * FROM ZONAS_BASICAS WHERE ESTADO=1"
        return self.db.ejecutar(query)

    #def eliminar(self):
    #    """ELIMINAR UN REGISTRO DE LA TABLA """
    #    query = "DELETE FROM ZONAS_BASICAS WHERE ID = %s"
    #    valores = self.id
    #    return self.db.ejecutar(query, valores)
