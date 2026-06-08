from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from . import main_bp


# Ruta de inicio (pública)
@main_bp.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('miembros.index'))
    return render_template('index.html')

# Dashboard protegido
@main_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)