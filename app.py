from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a_secret_super_key_that_should_be_changed'
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

@app.route('/add', methods=['GET', 'POST'])
def add_post():
    if request.method == "POST":
        post_title = request.form['title']
        post_content  = request.form['content']
        post_author = request.form['author']

        new_post= Post(title= post_title, author = post_author, content = post_content)

        db.session.add(new_post)
        db.session.commit()

        flash('Blog Post Created Successfully', 'success')
        return redirect(url_for('home'))

    return render_template('add_post.html')

@app.route('/delete/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    post_to_delete = Post.query.get_or_404(post_id)

    try:
        db.session.delete(post_to_delete)
        db.session.commit()
        flash('Post deleted successfully!', 'success')
    except:
        flash('Unexpected error occured, could not delete post!', 'danger')
    return redirect(url_for('home'))
    
if __name__=="__main__":
    app.run(debug=True)
