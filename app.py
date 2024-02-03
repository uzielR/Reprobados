from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt

app= Flask(__name__,  template_folder='templates')



@app.route('/')
def registro():

    return render_template('registro.html')

@app.route('/Calificaciones')
def Calificaciones():
    return render_template('Calificaciones.html')


#ejecución del servidor en el puerto 5000
if __name__ == '__main__':
    app.run(debug=True)