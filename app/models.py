from . import db
from datetime import datetime

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self): # JSON qaytarmaq üçün köməkçi metod
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "date_created": self.date_created.strftime("%Y-%m-%d %H:%M:%S")
        }