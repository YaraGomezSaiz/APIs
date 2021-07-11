import requests
url="https://pokeapi.co/api/v2/pokemon-form/" 

def get_pokemons(url="https://pokeapi.co/api/v2/pokemon-form/",offset=0):
        
        args={'offset':offset} if offset else {}
        response=requests.get(url,params=args)
    
        if response.ok:
            response_json=response.json()
            pokemons=response_json.get('results',[])
            pokemons_name=[]

            if pokemons:
                
                for pokemon in pokemons:
                    name=pokemon['name']
                    #añade un elemento a un array
                    pokemons_name.append(name)
        
        return pokemons_name