from app import app

from flask import render_template, request, url_for, redirect, flash
from flask_login import login_required, current_user, login_user, logout_user

from .auth.forms import SignUpForm, LoginForm
from .forms import PokemonFinder
from .models import User, Pokemon
from .services import pokeNewb

import requests, json



# @app.route('/battle')
# def battlePage():
#     users = User.query.all()
#     catch_set = set()

#     if current_user.is_authenticated:
#         users_catch = current_user.catch.all()
#         print(users_catch)
#         for u in users_catch:
#             catch_set.add(u.id)
#         for u in users:
#             if u.id in catch_set:
#                 u.flag = True

#     return render_template('battle.html', users=users)



@app.route('/')
def homePage():

    return render_template('index.html')
    

@app.route('/finder', methods=['GET','POST'])
@login_required
def pokemonfinderPage():


    p_form = PokemonFinder()
    if request.method == 'POST':
        name = p_form.pokemon_name.data
        p = Pokemon.query.filter(Pokemon.name == name).first()
        if p:
            flash(f"hey theres p")
            return render_template('poke_description.html', p_form=p_form, p=p)
        else:
            poke_dic = pokeNewb(name)
            name = poke_dic['name']
            base_experience = poke_dic['base_experience']
            front_shiny = poke_dic['front_shiny']
            hp_base_stat = poke_dic['hp_base_stat']
            attack_base_stat = poke_dic['attack_base_stat']
            defense_base_stat = poke_dic['defense_base_stat']

            p = Pokemon(name, base_experience, front_shiny, hp_base_stat, attack_base_stat, defense_base_stat)
            p.savePoke()
            flash(f"poke saved")
            return render_template('poke_description.html', p_form=p_form, p=p)
    return render_template('finder.html', p_form=p_form)

  


@app.route('/catch/<int:poke_id>')
@login_required
def catch(poke_id):
    p = Pokemon.query.get(poke_id)
    print(p)
    if p:
        print('hello')
        current_user.catch(p)
        print('there')
        flash(f"You have now caught", category='success')
    else:
        flash(f"That pokemon has already been caught", category='danger')

    return redirect(url_for('homePage'))


@app.route('/release/<int:poke_id>')
@login_required
def release(poke_id):
    p = Pokemon.query.get(poke_id)
    if p:
        current_user.release(p)
        flash(f"You no longer have {p.name} on your team", category='warning')
    else:
        flash(f"That pokemon has already been caught", category='danger')

    return redirect(url_for('homePage'))



