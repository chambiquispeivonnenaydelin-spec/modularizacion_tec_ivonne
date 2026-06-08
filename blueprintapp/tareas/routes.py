from flask import request, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from blueprintapp import db
from . import bp_tarea
from .models import Tarea

@bp_tarea.route("/")
@login_required
def index():
    # Solo mostrar tareas del usuario actual
    tareas = Tarea.query.filter_by(user_id=current_user.id).all()
    return render_template('tareas/index.html', tareas=tareas)

@bp_tarea.route("/create", methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'GET':
        return render_template('tareas/create.html')

    descripcion = request.form.get('descripcion')
    completado = True if 'completado' in request.form.keys() else False

    tarea = Tarea(
        descripcion=descripcion,
        completado=completado,
        user_id=current_user.id  # ← ASOCIAR AL USUARIO
    )

    db.session.add(tarea)
    db.session.commit()
    flash('Tarea creada exitosamente', 'success')

    return redirect(url_for('bp_tarea.index'))

@bp_tarea.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    # Verificar que la tarea pertenece al usuario actual
    tarea = Tarea.query.filter_by(id=id, user_id=current_user.id).first_or_404()

    if request.method == 'POST':
        tarea.descripcion = request.form['descripcion']
        tarea.completado = True if request.form.get('completado') == '1' else False
        db.session.commit()
        flash('Tarea actualizada exitosamente', 'success')
        return redirect(url_for('bp_tarea.index'))

    return render_template('tareas/edit.html', tarea=tarea)

@bp_tarea.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete(id):
    # Verificar que la tarea pertenece al usuario actual
    tarea = Tarea.query.filter_by(id=id, user_id=current_user.id).first_or_404()

    if request.method == 'POST':
        db.session.delete(tarea)
        db.session.commit()
        flash('Tarea eliminada exitosamente', 'success')
        return redirect(url_for('bp_tarea.index'))

    return render_template('tareas/delete.html', tarea=tarea)