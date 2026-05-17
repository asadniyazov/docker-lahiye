from flask import Blueprint, request, render_template, redirect, url_for
from .models import Note
from . import db

notes_bp = Blueprint('notes', __name__)

@notes_bp.route('/')
def index():
    all_notes = Note.query.order_by(Note.date_created.desc()).all()
    return render_template('index.html', notes=all_notes)


@notes_bp.route('/add', methods=['POST'])
def add_note():
    title = request.form.get('title')
    content = request.form.get('content')
    if title and content:
        new_note = Note(title=title, content=content)
        db.session.add(new_note)
        db.session.commit()
    return redirect(url_for('notes.index'))


@notes_bp.route('/delete/<int:id>')
def delete_note(id):
    note = Note.query.get_or_404(id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('notes.index'))

@notes_bp.route('/update/<int:id>')
def update_note(id):
    note = Note.query.get_or_404(id)
    # Sadə bir "tamamlandı/tamamlanmadı" məntiqi
    note.title = "[TAMAMLANDI] " + note.title if "[TAMAMLANDI]" not in note.title else note.title.replace("[TAMAMLANDI] ", "")
    db.session.commit()
    return redirect(url_for('notes.index'))