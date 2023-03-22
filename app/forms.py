from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class PokemonFinder(FlaskForm):
    pokemon_name = StringField()
    ablility_name = StringField()
    base_experience = StringField()
    front_shiny = #url
    hp_base_stat = StringField()
    attack_base_stat = StringField() / #integers
    defence_base_stat = StringField() / #integers 
