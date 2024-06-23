# models.py
from database import db

class MovieImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(80), nullable=False)
    movie_id = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(120), nullable=True)
    image_path = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<MovieImage {self.user_id}>'
