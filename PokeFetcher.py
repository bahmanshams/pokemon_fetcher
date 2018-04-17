from guizero import App, TextBox, PushButton, Picture,error 
from pokebase import pokemon 
from requests import get 
from PIL import Image 
from io import BytesIO
info=''
def fetch_pokemon():
 
     name = (input_box.value).lower()
     try:   
         poke = pokemon(name)
         info=poke.sprites
         pic = get(poke.sprites.front_default).content
         image = Image.open(BytesIO(pic))
         image.save('poke.gif')
         icon.value = 'poke.gif'
         info_box.value=info
     except:      
         error('warning','invalid name, plz enetr the name properly')
        
       

app = App(title='Pokemon Fetcher', width=400, height=300) 
input_box = TextBox(app, text='Name') 
icon = Picture(app, image="poke.gif") 
submit = PushButton(app, command=fetch_pokemon, text='Submit')
info_box = TextBox(app, text='', multiline=True, width=100, height=100) 

app.display()
