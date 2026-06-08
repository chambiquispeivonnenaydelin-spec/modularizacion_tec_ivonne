from flask import Blueprint

bp_tarea = Blueprint(
    'bp_tarea',
    __name__,
    template_folder='templates'
)

from . import routes   # ← AGREGA ESTA LÍNEA