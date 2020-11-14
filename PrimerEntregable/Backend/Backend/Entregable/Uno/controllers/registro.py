from flask_restful import Resource, Api
from models.registro import RegistroModel


class RegistroController(Resource):
    def get(self):
        return {
            'ok': True,
            'message': None
        },

    def post(self):
        return {
            'ok': True,
            'message': 'Se guardo informacion'
        }

    def delete(self):
        return {
            'ok':True,
            'message': 'Se elimino exitosamente'
        }


class RegistrosController(Resource):
    def get(self, reg_nom):
        return 
            self.abort_if_doesnt_exist
            (reg_nom, False)
                    

    def post(self, reg_nom):
        self.abort_if_doesnt_exist
        (reg_nom, False)

    def delete(self, reg_nom):
        del Todo[reg_nom]
        return  
        self.abort_if_doesnt_exist(reg_nom, False)
        ,204
    
class TodoRegistroController(Resource):
    def get(self):
        return Todo
    
    def post(self):
        return Todo, 201

class EmailController(Resource):
    def get(self, reg_email):
        return 'ok'
    
    def post(self, reg_email):






