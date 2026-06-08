from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_login import LoginManager

# Crear las instancias AQUÍ
db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bd_equipo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'mi-clave-secreta-12345'
    
    # Inicializar con la app
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Por favor inicia sesión para acceder a esta página'  # ← Este mensaje
    login_manager.login_message_category = 'warning'
    login_manager.login_message = 'Por favor inicia sesión'
    
    @login_manager.user_loader
    def load_user(user_id):
        from blueprintapp.core.auth.models import User
        return User.query.get(int(user_id))
    
    # Importar blueprints (después de definir db)
    from blueprintapp.miembros import bp_miembro
    from blueprintapp.tareas import bp_tarea
    from blueprintapp.core.auth import auth_bp
    
    # Registrar blueprints
    app.register_blueprint(bp_miembro, url_prefix="/miembros")
    app.register_blueprint(bp_tarea, url_prefix="/tareas")
    app.register_blueprint(auth_bp, url_prefix="/auth")
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    return app