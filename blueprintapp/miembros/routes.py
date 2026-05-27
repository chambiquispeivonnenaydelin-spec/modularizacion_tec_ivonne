# Librerias a usar en el modulo
from flask import request,render_template,redirect,url_for,Blueprint

# Referencia a la base de datos
from blueprintapp.app import db
# Modelos con los que interactura el modulo
from blueprintapp.miembros.models import Miembro

bp_miembro = Blueprint('bp_miembro',__name__,template_folder='templates')

@bp_miembro.route("/")
def index():
    miembros = Miembro.query.all()
    return render_template('miembro/index.html',miembros=miembros)

@bp_miembro.route("/create",methods=['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('miembro/create.html')
    elif request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        # Crear un objeto miembro
        miembro = Miembro(nombre=nombre,email=email)
        # Insertar en la bd a traves del ORM
        db.session.add(miembro)
        db.session.commit()
        # Redireccion al listado de miembros
        return redirect(url_for('bp_miembro.index'))
        
@bp_miembro.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):

    miembro = Miembro.query.get_or_404(id)

    if request.method == 'POST':

        miembro.nombre = request.form['nombre']
        miembro.email = request.form['email']

        db.session.commit()

        return redirect(url_for('bp_miembro.index'))

    return render_template(
        'miembro/edit.html',
        miembro=miembro
    )



@bp_miembro.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):

    miembro = Miembro.query.get_or_404(id)

    if request.method == 'POST':

        db.session.delete(miembro)

        db.session.commit()

        return redirect(url_for('bp_miembro.index'))

    return render_template(
        'miembro/delete.html',
        miembro=miembro
    )
