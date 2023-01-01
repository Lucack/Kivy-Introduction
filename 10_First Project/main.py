from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.properties import StringProperty,BooleanProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.network.urlrequest import UrlRequest 
from kivy.uix.image import AsyncImage

import requests
from bs4 import BeautifulSoup

def search(textInput):
    # url = "https://www.pexels.com/pt-br/procurar/"+textInput+"/"
    # url = 'https://br.freepik.com/fotos/abacaxi'
    textInput = textInput.replace(' ','%20')
    url = 'https://www.istockphoto.com/br/search/2/image?istockcollection=&mediatype=photography&phrase='+textInput
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}
    data =  requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text,"html.parser")
    global links
    links = []
    for item in soup.find_all('source'): 
        if 'https://media.istockphoto.com/id/' in item['srcset']:
            links.append(item['srcset'])
    
class Widget1(GridLayout):

    my_text = StringProperty('0')
    count_enable = BooleanProperty(False)
    sliderEnable = BooleanProperty(False)
    value_text = StringProperty('Volume is OFF')
    textInput = StringProperty('Search your image')
    link1 = StringProperty('')
    link2 = StringProperty('')

    i=0 
    def on_button_click(self):
        if self.count_enable == True:
            self.i+=1
            self.my_text = str(self.i)
        
    def clear(self):
        if self.i == 0:
            self.my_text = "Alredy Clean!"
        else:
            self.i = 0
            self.my_text = str(self.i)

    def on_toggle_state(self,toggle_button):
        if toggle_button.state=="normal":
           toggle_button.text =  "OFF"
           self.count_enable = False
        else:
            toggle_button.text =  "ON"
            self.count_enable = True

    def on_switch_active(self,switch):
        if switch.active == True:
            self.sliderEnable=True
            self.value_text ="Volume is ON" 
        else:
            self.sliderEnable = False
            self.value_text ="Volume is OFF" 

    def slider_value(self,slider):
        
        self.value_text= "Volume: \n    " + str(int(slider.value))

    def on_text_validate(self,input):
        self.textInput = input.text
        search(self.textInput)
        try:
            self.link1 = links[0]
            self.link2 = links[1]
        except: 
            self.link1= 'https://static.vecteezy.com/system/resources/previews/005/337/799/original/icon-image-not-found-free-vector.jpg'
            self.link2= 'https://static.vecteezy.com/system/resources/previews/005/337/799/original/icon-image-not-found-free-vector.jpg'

class ProjectApp(App):
    pass

ProjectApp().run()