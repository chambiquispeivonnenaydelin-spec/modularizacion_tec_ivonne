from flask import Blueprint

bp_miembro = Blueprint('bp_miembro', __name__, template_folder='templates')

from . import routes