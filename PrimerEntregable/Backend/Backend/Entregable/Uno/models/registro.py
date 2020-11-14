from basedatos import db
class RegistroModel(db.Model):
    __tablename__="t_registro"
    id = db.Column("reg_id",db.Integer, primary_key= True, nullable= False)
    nombre = db.Column("reg_nom",db.Integer, nullable=False)
    email = db.Column("reg_email", db.String(40))
    phone = db.Column("reg_phone", db.Integer, nullable=False)
    message = db.Column("reg_mess", db.String(100))

def __init__(self, nombre, email, phone, message):
    self.nombre = nombre
    self.email = email
    self.phone = phone
    self.message = message

def guardar_bd(self):
    db.session.add(self)
    db.session.commit()

def abort_if_doesnt_exist(self, reg_nom, json=True):
    registro = registro.query.get(reg_nom)
    if registro is None:
        abort(404, message="Registro {} no existe".format(reg_nom))
    if json:
        return self.registro_to_json(registro)
    
    return registro




