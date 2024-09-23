from flask import Flask, render_template  # Importa Flask para permitirnos crear nuestra aplicación

app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente

def tab():

    paises = [

   {'pais': 'Argentina' , 'capital': 'Buenos Aires'},

   {'pais': 'Brasil' , 'capital': 'Brasilia'},

   {'pais': 'Chile' , 'capital': 'Santiago de Chile'},

   {'pais': 'Colombia' , 'capital': 'Bogotá'},

   {'pais': 'Costa Rica' , 'capital': 'San José'},

   {'pais': 'Paraguay' , 'capital': 'Asunción'},

   {'pais': 'Perú' , 'capital': 'Lima'}

    ]

    return render_template('pag.html', pais = paises)

if "__main__" == __name__:
    app.run(debug=True)