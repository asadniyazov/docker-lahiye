import os
import sys
import pytest

# Python-a deyirik ki, test faylının olduğu yerdən bir addım yuxarıya (layihənin kökünə) baxsın
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# İNDİ İSƏ TAM DÜZGÜN İMPORT: Fayllar 'app' qovluğunun daxilindədir!
from app import create_app, db
from app.models import Note  # noqa: F401

@pytest.fixture
def app():
    # Test mühitini təmiz SQLite yaddasında (RAM) qururuq
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
    })

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

# ── Sənin Real Testlərin ──────────────────────────────────

def test_index_page(client):
    """Əsas səhifənin (index.html) uğurla açılmasını yoxlayırıq"""
    response = client.get('/')
    assert response.status_code == 200

def test_add_note(client):
    """Bazaya yeni qeyd əlavə etməyi və yönləndirməni yoxlayırıq"""
    response = client.post('/add', data={
        'title': 'Docker Test Başlıq',
        'content': 'Docker Test Kontent'
    })
    assert response.status_code == 302