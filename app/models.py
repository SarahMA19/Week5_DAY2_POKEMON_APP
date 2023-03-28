from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash


db = SQLAlchemy()

catch = db.Table(
    'catch',
    db.Column('caught_by_id', db.Integer, db.ForeignKey('user.id'),nullable=False),
    db.Column('pokemon_id', db.Integer, db.ForeignKey('pokemon.id'),nullable=False)
)

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    base_experience = db.Column(db.String, nullable=False)
    front_shiny = db.Column(db.String, nullable=False)
    hp_base_stat = db.Column(db.String, nullable=False)
    attack_base_stat = db.Column(db.String, nullable=False)
    defense_base_stat = db.Column(db.String, nullable=False)

    def __init__(self, name, base_experience, front_shiny, hp_base_stat, attack_base_stat, defense_base_stat):
        self.name = name
        self.base_experience = base_experience
        self.front_shiny = front_shiny
        self.hp_base_stat = hp_base_stat
        self.attack_base_stat = attack_base_stat
        self.defense_base_stat = defense_base_stat


    def savePoke(self):
        db.session.add(self)
        db.session.commit()
                              


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    caught_poke = db.relationship('Pokemon',
        # primaryjoin = (catch.c.caught_by_id==id),
        # secondaryjoin = (catch.c.pokemon_id==id),
        secondary = "catch", 
        backref = "caught_poke",
        lazy = 'dynamic'
    )

    def catch(self, poke):
        self.caught_poke.append(poke)
        db.session.commit()

    def release(self, poke):
        self.caught_poke.remove(poke)
        db.session.commit()


    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password) 
        #self.password = password   ---OLD  not hashed

    def saveUser(self):
        db.session.add(self)
        db.session.commit()

    




