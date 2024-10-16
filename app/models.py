from datetime import datetime
from app import db

class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Strind(100), nullable=False)
    email = db.Column(db.Strind(200), nullable=False)
    password = db.Column(db.Strind(24), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(datetime.timezone.utc))
    user = db.relationship('Task', back_populates='Users')

    def __repr__(self):
        return f'<User {self.name}>'

class Task(db.Model):
    __tablename__ = 'Tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Strind(100), nullable=False)
    description = db.Column(db.Strind(200), nullable=False)
    is_done = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    user = db.relationship('User', back_populates='Tasks')

    def __repr__(self):
        return f'<Task {self.title}>'