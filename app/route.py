from werkzeug.utils import redirect
from app import app, db
from flask import render_template, url_for, request
from app.models import Post


@app.route('/', methods=['GET'])
def index():
    post = Post.query.all()
    text = request.args.get('text')
    post_id = request.args.get('id')
    if text:
        return redirect(url_for('search', text=text))
    elif post_id:
        Post.query.filter(Post.id == post_id).delete()
        db.session.commit()
        return redirect('/')
    else:
        return render_template('index.html', post=post)

@app.route('/search/<string:text>/')
def search(text):
    post = Post.query.filter(Post.text.contains(text)).order_by(Post.created_date.desc()).limit(20)
    return render_template('index.html', post=post)

