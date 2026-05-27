from flask import request, render_template, redirect, url_for, Blueprint

from blueprintapp.app import db
from blueprintapp.tareas.models import Tarea

bp_tarea = Blueprint('bp_tarea', __name__, template_folder='templates')


@bp_tarea.route("/")
def index():
    tareas = Tarea.query.all()
    return render_template('tareas/index.html', tareas=tareas)


@bp_tarea.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('tareas/create.html')

    descripcion = request.form.get('descripcion')
    completado = True if 'completado' in request.form.keys() else False

    tarea = Tarea(descripcion=descripcion, completado=completado)

    db.session.add(tarea)
    db.session.commit()

    return redirect(url_for('bp_tarea.index'))


@bp_tarea.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):

    tarea = Tarea.query.get_or_404(id)

    if request.method == 'POST':

        tarea.descripcion = request.form['descripcion']
        tarea.completado = True if request.form.get('completado') == '1' else False

        db.session.commit()

        return redirect(url_for('bp_tarea.index'))

    return render_template(
        'tareas/edit.html',
        tarea=tarea
    )


@bp_tarea.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):

    tarea = Tarea.query.get_or_404(id)

    if request.method == 'POST':

        db.session.delete(tarea)
        db.session.commit()

        return redirect(url_for('bp_tarea.index'))

    return render_template(
        'tareas/delete.html',
        tarea=tarea
    )