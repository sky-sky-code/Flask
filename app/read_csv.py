import csv

from app import db
from app.models import Post

result = []

def read_post():
    with open('../posts.csv', encoding='utf8') as post:
        post_reader = csv.DictReader(post)
        for item in post_reader:
            result.append(item)

def insert_post():
    for i in range(len(result)):
        post = Post(result[i]['rubrics'], result[i]['text'], result[i]['created_date'])
        db.session.add(post)
    db.session.commit()

read_post()
insert_post()
