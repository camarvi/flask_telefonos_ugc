
#CLASE QUE UTILIZAMOS PARA CONECTAR A LA BASE DE DATOS Y REALIZAR TODAS LAS OPERACIONES



import pyodbc  #""" Libreria acceso a Sql_Server"""

class ConexionBD:
    def __init__(self,server='xxxxx',database='xxxxx',usuario='xxx',password='xxxxx'):
        self.server = server
        self.database = database
        self.usuario = usuario
        self.password = password

    def conectar(self):
        #"""Crear la conexion a la base de datos """"
        self.db = pyodbc.connect('DRIVER={SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.usuario+';PWD='+self.password)

    def abrir_cursor(self):
        #"""Abrir un Cursor"""
        self.cursor = self.db.cursor()

    def ejecutar_consulta(self, query, parametros=''):
        #"""Ejecucion de consultas en la base de datos """
        if parametros != '': #"""CONSULTA SQL CON PARAMETROS """"
            self.cursor.execute(query, parametros)
        else:
            self.cursor.execute(query)

    def traer_datos(self):
        #"""TRAEMOS TODOS LOS REGISTROS DEVUELTOS POR LA CONSULTA """
        self.rows = self.cursor.fetchall()

    def enviar_commit(self, query):
        #"""ENVIAR COMMIT A LA BASE DE DATOS SOLO INSERT, DELETE Y UPDATE """
        sql =query.lower()
        es_select = sql.count('select')
        if es_select < 1 :
            self.db.commit()

    def cerrar_cursor(self):
        #"""Cerrar el cursor """
        self.cursor.close()

    def ejecutar(self, query, values=''):
        #"""Compilar todos los procesos """
        if (self.server and self.usuario and self.password and self.database and query):
            self.conectar()
            self.abrir_cursor()
            self.ejecutar_consulta(query, values)
            self.enviar_commit(query)
            self.traer_datos()
            self.cerrar_cursor()
            return self.rows


    
        
