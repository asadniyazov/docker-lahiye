import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Bazanı burada müəyyən edirik ki, digər fayllarda da istifadə edə bilək
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # ── Peşəkar Konfiqurasiya ──────────────────────────────────────
    # Bazanı SQLite-ın rəsmi standartı olan 'instance' qovluğuna yönləndiririk
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, '../app.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'sənin-gizli-açarın-123'

    db.init_app(app)

    # Blueprint-ləri (Routları) burada qeydiyyatdan keçiririk
    from .routes import notes_bp
    app.register_blueprint(notes_bp)

    # Veritabanını avtomatik yaratmaq üçün təhlükəsiz app mühiti açırıq
    with app.app_context():
        db.create_all()

    return app