"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from api.functions import get_pokemons
import requests

api = Blueprint('api', __name__)

# url="https://pokeapi.co/api/v2/pokemon-form/"  

# def get_pokemons(url="https://pokeapi.co/api/v2/pokemon-form/",offset=0):
        
#         args={'offset':offset} if offset else {}
#         response=requests.get(url,params=args)
    
#         if response.ok:
#             response_json=response.json()
#             pokemons=response_json.get('results',[])
#             pokemons_name=[]

#             if pokemons:
                
#                 for pokemon in pokemons:
#                     name=pokemon['name']
#                     #añade un elemento a un array
#                     pokemons_name.append(name)
            
#             #elimina un elemento de un array
#             # pokemons_name.pop(1)

#             # print(pokemons_name)
#             # print(len(pokemons_name))
#             # print(response.url)

#             #   #funcion que continuar listando la funcion
#             #   next= input ("¿Do you want to continue listing [Y/N]?").lower()
#             #   if next=='y':
#             #     get_pokemons(offset=offset+20)

        
#         return pokemons_name



#API que llama a otra API
@api.route('/pokemons', methods=['GET'])
def handle_pokemons(): 

    pokemons=get_pokemons()
    
    return jsonify(pokemons), 200



    
