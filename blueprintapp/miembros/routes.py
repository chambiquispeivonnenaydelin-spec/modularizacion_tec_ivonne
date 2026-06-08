from flask import request, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from blueprintapp import db
from . import bp_miembro
from .models import Miembro

@bp_miembro.route("/")
@login_required
def index():
    miembros = Miembro.query.filter_by(user_id=current_user.id).all()
    return render_template('miembro/index.html', miembros=miembros)

@bp_miembro.route("/create", methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'GET':
        return render_template('miembro/create.html')
    elif request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        
        miembro = Miembro(
            nombre=nombre,
            email=email,
            user_id=current_user.id
        )
        db.session.add(miembro)
        db.session.commit()
        flash('Miembro creado exitosamente', 'success')
        return redirect(url_for('bp_miembro.index'))

@bp_miembro.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    miembro = Miembro.query.filter_by(id=id, user_id=current_user.id).first_or_404()

    if request.method == 'POST':
        miembro.nombre = request.form['nombre']
        miembro.email = request.form['email']
        
        db.session.commit()
        flash('Miembro actualizado exitosamente', 'success')
        return redirect(url_for('bp_miembro.index'))

    return render_template('miembro/edit.html', miembro=miembro)

@bp_miembro.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete(id):
    miembro = Miembro.query.filter_by(id=id, user_id=current_user.id).first_or_404()

    if request.method == 'POST':
        db.session.delete(miembro)
        db.session.commit()
        flash('Miembro eliminado exitosamente', 'success')
        return redirect(url_for('bp_miembro.index'))

    return render_template('miembro/delete.html', miembro=miembro)