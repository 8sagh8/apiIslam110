from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from the frontend
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL') or 'sqlite:///data.db'
db = SQLAlchemy(app)


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100))
    # Add more columns for other fields


@app.route('/api/data', methods=['POST'])
def add_data():
    data = request.json
    new_data = Data(subject=data['subject'])
    # Set other fields here
    db.session.add(new_data)
    db.session.commit()
    return jsonify(message="Data added successfully"), 201


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
