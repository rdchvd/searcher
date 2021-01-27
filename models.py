from flask_sqlalchemy import Model

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(240), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __str__(self):
        return 'Article: {}'.format(title)