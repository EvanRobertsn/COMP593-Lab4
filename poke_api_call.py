import requests

#code pulls the info from poke api and takes command paramater
#cleans string up
def clean_name(poke_name):
    poke_name=poke_name.strip().lower()
    return poke_name

#pulls from pokeapi
def poke_get_info(poke_name):
    poke_name=clean_name(poke_name)
    url='https://pokeapi.co/api/v2/pokemon/'+poke_name
    print("Getting the information for "+poke_name +" at "+url)
    resp_msg=requests.get(url)
    if resp_msg.status_code == 200:
        resp_msg=resp_msg.json()
        print("Found the pokemon")
        return resp_msg
    else:
        print("That's not a pokemon dude")
        print("error code: ",resp_msg.status_code," Reason: "+resp_msg.reason)
        exit()













