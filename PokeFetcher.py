from guizero import App, TextBox, PushButton, Picture,error ,Text
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
         height=poke.height
         weight=poke.weight
         type=poke.type
         pic = get(poke.sprites.front_default).content
         image = Image.open(BytesIO(pic))
         image.save('poke.gif')
         icon.value = 'poke.gif'
         info_box.value=info
         height_box.value=height
         weight_box.value=weight
         type_box.value=abilities
         
     except:      
         error('warning','invalid name, plz enetr the name properly')
        
       

app = App(title='Pokemon Fetcher', width=400, height=400, bg='#FFC300') 
input_box = TextBox(app, text='Name') 
icon = Picture(app, image="poke.gif") 
submit = PushButton(app, command=fetch_pokemon, text='Submit')
submit.bg="#FF5733"
info_box = TextBox(app, text='', multiline=True, width=30, height=5)
weight_lbl = Text(app, text="weight", bg='#FFC300')
weight_box = TextBox(app, text='')
height_lbl = Text(app, text="height",bg='#FFC300')
height_box = TextBox(app, text='')
type_lbl = Text(app, text="type", bg='#FFC300')
type_box = TextBox(app, text='',multiline=True )

app.display()


#poke.abilities
#poke.height
#poke.name
#poke.species
#poke.stats
#poke.type
#poke.weight
