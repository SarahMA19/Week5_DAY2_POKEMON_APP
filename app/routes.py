from app import app

from flask import render_template, request, url_for, redirect, flash, session
from flask_login import login_required, current_user, login_user, logout_user

from .auth.forms import SignUpForm, LoginForm
from .forms import PokemonFinder
from .models import User, Pokemon, catch
from .services import pokeNewb

import requests
import json


@app.route('/')
def homePage():

    return render_template('index.html')


@app.route('/finder', methods=['GET', 'POST'])
@login_required
def pokemonfinderPage():
    poke_dic = {}
    p_form = PokemonFinder()
    full = False
    x = current_user.caught_poke.all()
    teamlist =[]
    for p in x:
        teamlist.append(p.name) 
    print(x)
    if len(x) > 4:
        full = True
    print(x, len(x))
    if request.method == 'POST':
        name = p_form.pokemon_name.data
        name = name.lower()
        p = Pokemon.query.filter_by(name=name).first()
        if p:
            return render_template('poke_description.html', p_form=p_form, p=p, x=x, teamlist=teamlist, full=full)
        else:
            poke_dic = pokeNewb(name)
        if poke_dic:
            name = poke_dic['name']
            base_experience = poke_dic['base_experience']
            front_shiny = poke_dic['front_shiny']
            hp_base_stat = poke_dic['hp_base_stat']
            attack_base_stat = poke_dic['attack_base_stat']
            defense_base_stat = poke_dic['defense_base_stat']

            p = Pokemon(name, base_experience, front_shiny,
                        hp_base_stat, attack_base_stat, defense_base_stat)
            p.savePoke()
            return render_template('poke_description.html', p_form=p_form, p=p, x=x, teamlist=teamlist, full=full)
    return render_template('finder.html', p_form=p_form, x=x, teamlist=teamlist, full=full)


@app.route('/catch/<int:poke_id>')
@login_required
def catch(poke_id):
    p = Pokemon.query.get(poke_id)
    if p:
        current_user.catch(p)
        print(current_user)
    else:
        pass
    return redirect(url_for('pokemonfinderPage'))


@app.route('/release/<int:poke_id>')
@login_required
def release(poke_id):
    p = Pokemon.query.get(poke_id)
    if p:
        current_user.release(p)
        flash(f"You no longer have on your team", category='warning')
    return redirect(url_for('pokemonfinderPage'))


@app.route('/myteam')
@login_required
def myteamPage():
    return render_template('myteam.html')
        
