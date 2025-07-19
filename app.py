from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'blog.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(50), nullable=False, default='N/A')

    def __repr__(self):
        return f'<Post {self.title}>'
@app.route('/')
def home():
    all_posts = Post.query.all()
    return render_template('index.html', posts=all_posts)

if __name__=="__main__":
    app.run(debug=True)
