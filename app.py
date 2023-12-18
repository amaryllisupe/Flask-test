from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     username = db.Column(db.String(80), unique=True, nullable=False)
     password = db.Column(db.String(120), nullable=False)

@app.route('/')
def index():
     return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
     username = request.form['username']
     password = request.form['password']

     # Hash the password before saving it to the database
     hashed_password = generate_password_hash(password, method='sha256')

     new_user = User(username=username, password=hashed_password)
     db.session.add(new_user)
     db.session.commit()

     return redirect(url_for('index'))

if __name__ == '__main__':
     db.create_all()
     app.run(debug=True)
