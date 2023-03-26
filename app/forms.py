from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PokemonFinder(FlaskForm):
    pokemon_name = StringField('Enter Pokemon Name Here', validators = [DataRequired()])
    submit = SubmitField()


    


