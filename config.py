class Config:
    SECRET_KEY = 'mi-clave-secreta-para-desarrollo'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///bd_equipo.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False