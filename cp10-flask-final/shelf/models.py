from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from . import db

STATUSES = {"want": "Хочу прочитать", "reading": "Читаю", "done": "Прочитано"}


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    about = db.Column(db.String(300), default="")
    created = db.Column(db.DateTime, default=datetime.now)
    books = db.relationship("Book", back_populates="owner", cascade="all, delete-orphan", order_by="Book.updated.desc()")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(10), nullable=False, default="want")
    rating = db.Column(db.Integer)
    review = db.Column(db.Text, default="")
    updated = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    owner = db.relationship("User", back_populates="books")

    @property
    def status_name(self):
        return STATUSES[self.status]
