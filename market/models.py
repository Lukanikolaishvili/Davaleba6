from market import db, login_manager
from market import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.string(length=30), nullable=False, unique=True)
    email_address = db.Column(db.string(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.string(length=60), nullable=False,)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('item', backref='owned_user', lazy=True)

    @property
    def prettier_budget(self):
        if len(str(self.budget)) >= 4:
            return f'{str(self.budget)[:-3]},{str(self.budget)[-3:]}$'
        else:
            return f'{str(self.budget)}$'

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.string(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.string(length=12), nullable=False, unique=True)
    description = db.Column(db.string(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return f'Item {self.name}'



