from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty,BooleanProperty
from kivy.metrics import dp
from kivy.graphics import *


class Canvas4(Widget):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(poits=(100,100,400,500), width=2)
            Color(1,0.5,1)
            Line(rectangle=(10,15,20,30), width = 2)
            self.rec = Rectangle(pos=(600,150),size=(80,80))
            
    def button_click(self):
        x,y=self.rec.pos
        if x+dp(90)<self.width:
            x+=dp(10)
            self.rec.pos = x,y


class ObjectsApp(App):
    pass

ObjectsApp().run()
