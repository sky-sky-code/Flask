from app import db

class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key = True)
    rubrics = db.Column(db.String)
    text = db.Column(db.Text)
    created_date = db.Column(db.DateTime)

    def __init__(self, rubrics, text, created_date):
        self.rubrics = rubrics
        self.text = text
        self.created_date = created_date

    def __repr__(self):
        return f"Post(rubrics: {self.rubrics} text: {self.text} created_date: {self.created_date})"
