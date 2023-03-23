from app import app

from flask import render_template, request, url_for, redirect
from flask_login import login_required

from .forms import PokemonFinder

import requests, json


@app.route('/')
def homePage():
    return render_template('index.html')


@app.route('/finder', methods=['GET','POST'])
@login_required
def pokemonfinderPage():

    def pokeNewb(poke):

        res = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke}/")
        data = res.json()
        #print(data)
        
        x = dict()
        x['name'] = data['name'],
        x['ability name'] = data['abilities'][0],
        x['base experience'] = data['base_experience'],
        x['front shiny'] = data['sprites']['front_shiny'],
        x['hp base stat'] = data['stats'][0],
        x['attack base stat'] = data['stats'][1],
        x['defense base stat'] = data['stats'][2]
    
        return x
    
    p_form = PokemonFinder()
    if request.method == 'POST':
        name = p_form.pokemon_name.data
        poke_dic = pokeNewb(name)
        print(poke_dic)
        return render_template('poke_description.html', p_form=p_form, poke_dic=poke_dic)
    

    return render_template('finder.html', p_form=p_form)


