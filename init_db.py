from blueprintapp import create_app, db
from blueprintapp.core.auth.models import User
from blueprintapp.miembros.models import Miembro
from blueprintapp.tareas.models import Tarea

app = create_app()

with app.app_context():
    # Crear todas las tablas
    db.create_all()
    print("✅ Tablas creadas exitosamente")
    
    # Verificar tablas creadas
    print("\n📋 Tablas en la base de datos:")
    from sqlalchemy import inspect
    inspector = inspect(db.engine)
    for table in inspector.get_table_names():
        print(f"   - {table}")