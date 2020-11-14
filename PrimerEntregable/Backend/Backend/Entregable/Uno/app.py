from flask import Flask
from flask_restful import Api
from basedatos import db
# from models.registro import RegistroModel
from controllers.registro import RegistroController, RegistrosController, TodoRegistroController,EmailController


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@localhost/base_datos'
api = Api(app=app)

Todo = {
    'RegistroController':{},
    'RegistrosController':{},
    'TodoRegistroController':{},
    'EmailController':{}
}

@app.before_first_request
def iniciador():
    db.init_app(app)
    # db.drop_all(app=app)
    db.create_all(app=app)

@app.route('/')
def inicio():
    return 'El servidor esta online'


#@app.route("/")
#def enviado():
#    return "<h1 style='color:red'>Esta enviado</h1"

#@app.route("/temp")
#def template():
#    return render_template('index.html')

api.add_resource(RegistroController,'/registro')
api.add_resource(RegistrosController,'/registro/<int:reg_nom>')
api.add_resource(TodoRegistrosController,'/registro')
api.add_resource(EmailController,'/registro')

if __name__=='__main__':
    app.run(debug=True)

