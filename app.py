from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://user1:12345678@localhost/id22355996_latihan_movie'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the model
class MovieImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(80), nullable=False)
    movie_id = db.Column(db.String(80), nullable=False)
    file_path = db.Column(db.String(200), nullable=False)

@app.route('/upload', methods=['POST'])
def upload():
    user_id = request.form['userId']
    movie_id = request.form['movieId']
    file = request.files['file']
    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)

    # Save to database
    new_image = MovieImage(user_id=user_id, movie_id=movie_id, file_path=file_path)
    db.session.add(new_image)
    db.session.commit()

    return {'message': 'File uploaded successfully'}, 200

if __name__ == '__main__':
    app.run(debug=True)
