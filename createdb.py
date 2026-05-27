from blueprintapp.app import create_app
from blueprintapp.miembros.models import db, Miembro
from blueprintapp.tareas.models import Tarea

app = create_app()

with app.app_context():
    db.create_all()
    print("Base de datos creada")