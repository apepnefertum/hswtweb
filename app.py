from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forum.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.String(500), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/forum', methods=['GET'])
def forum():
    posts = Post.query.all()
    return render_template('forum.html', posts=posts)

@app.route('/forum', methods=['POST'])
def new_post():
    title = request.form['title']
    body = request.form['body']
    post = Post(title=title, body=body)
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('forum'))

if __name__ == '__main__':
    app.run(debug=True)


