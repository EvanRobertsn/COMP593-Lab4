import sys
import poke_api_call
import pastebin_api

#creates the contents of the paste
def get_paste_content(list):
    #multi-line string to store abilites
    mls=""""""
    abil_list=[]
    for i in list['abilities']:
        abil_list.append(i['ability']['name'])
    
    #create list of abil in mls
    for i in range(len(abil_list)):
        if(i<len(abil_list)-1):
            mls+="-"+abil_list[i]+"\n"
        elif(i==len(abil_list)-1):
            mls+="-"+abil_list[i]
        i+=1
    return mls
#get the name of the pokemon
def is_name():
    poke_name=sys.argv
    if(len(poke_name)==1):
        print("Param not provided, try again")
        exit()
    else:
        return poke_name
#gets the title of the paste 
def make_title(poke_name):
    title=(poke_api_call.clean_name(poke_name[1]).capitalize()+"'s abilities")
    return title
#main class
def main():
   
    poke_name=is_name()
    list=poke_api_call.poke_get_info(poke_name[1])
    mls=get_paste_content(list)
    title=make_title(poke_name[1])
    #creates pastebin, returns url of pastebin
    url=pastebin_api.make_pasty(title,mls)
    print(url)

#function call of main
main()