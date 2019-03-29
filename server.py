from flask import Flask, render_template, request, redirect, url_for, flash
from class_ugc import Ugc
from class_centros import Centros

#import pyodbc

app = Flask(__name__)


# CONEXION A LA BASE DE DATOS, 

#server = '10.8.65.17' 
#database = 'CMANDOS' 
#username = 'sa' 
#password = 'servidor' 
#cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)



# CONFIGURACIONES
app.secret_key = 'fdsfkdr343sdkfjsior343jksfksafasnkj434343'

@app.route('/')
def index():
    ugc = Ugc()
    lista_ugc = ugc.read_all()
    return render_template('index.html', lista_ugc = lista_ugc)
    # CODIGO SIN UTILIZAR OBJETOS
    #  cursor = cnxn.cursor()
    #  cursor.execute("SELECT * FROM ZONAS_BASICAS WHERE ESTADO=1;") 
    #  rows = cursor.fetchall() 
    #  cursor.close()
    #  return render_template('index.html', lista_ugc = rows ) 

@app.route('/centros', methods=['POST'])
def muestra_Centros():
    nombre = request.form['ugc']
    posicion = nombre.find('|')
    cod_ugc = nombre[0:posicion-1]
    nombre_ugc = nombre[posicion+1:]
    centros = Centros()
    #centros.cod_zbs = cod_ugc
    centros.setcod_ugc(cod_ugc)
    lista_centros = centros.leer_centros_ugc()
    del centros
    return render_template('centros.html',centros = lista_centros, cod_ugc = cod_ugc, nombre_ugc= nombre_ugc)
    # codigo para no utilizar objetoc
    #cursor = cnxn.cursor()
    #cursor.execute('''SELECT COD_CENTRO,CENTRO_NOMBRE FROM CENTROS WHERE COD_ZBS like ? ''', format(cod_ugc))
    #rows = cursor.fetchall() 
    #cursor.close()
    #return render_template('centros.html',centros = rows, cod_ugc = cod_ugc, nombre_ugc = nombre_ugc)



if __name__ == '__main__':
    app.run(port=5000, debug = True)