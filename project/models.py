from project import db, login_manager
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    username = db.Column(db.String(64), unique=True, index=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, password, **kwargs):
        # self.email = email
        # self.username = username
        super(User, self).__init__(**kwargs)
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

        def __repr__(self):
            return f"Welcome {self.username}"



class Article(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(126), nullable=False)
    body = db.Column(db.Text, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, title, body):
        self.title = title
        self.body = body

    def __repr(self, title):
        return str(self.title)