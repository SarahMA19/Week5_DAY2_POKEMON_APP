import requests


def pokeNewb(poke):

        res = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke}/")
        data = res.json()
        #print(data)
        
        x = {}
        x["name"] = data["name"]
        x['ability_name'] = data['abilities'][0]['ability']['name']
        x['base_experience'] = data['base_experience']
        x['front_shiny'] = data['sprites']['front_shiny']
        x['hp_base_stat'] = data['stats'][0]['base_stat']
        x['attack_base_stat'] = data['stats'][1]['base_stat']
        x['defense_base_stat'] = data['stats'][2]['base_stat']
        return x
    