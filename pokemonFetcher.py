from guizero import App, TextBox, PushButton, Picture,error
from pokebase import pokemon
from requests import get
from PIL import Image
from io import BytesIO

def fetch_pokemon():
    name = (input_box.value).lower()
    if name == True:
        poke = pokemon(name)
        pic = get(poke.sprites.front_default).content
        image = Image.open(BytesIO(pic))
        image.save('poke.gif')
        icon.value = 'poke.gif'
    else:
         error("warning", "Invalid char....")

app = App(title='Pokemon Fetcher', width=400, height=300)
input_box = TextBox(app, text='Name')
icon = Picture(app, image="poke.gif")
submit = PushButton(app, command=fetch_pokemon, text='Submit')

app.display()
