from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), index=True)
    password_hash = db.Column(db.String(128))
    active = db.Column(db.Boolean, default=True)
    created_datetime = db.Column(db.DateTime, default=datetime.utcnow)
    updated_datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, email, username, password, created_by):
        self.email = email.lower()
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.created_by = created_by

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
