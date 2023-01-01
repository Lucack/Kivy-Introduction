from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.properties import StringProperty,BooleanProperty
# from kivy.uix.screenmanager import ScreenManager, Screen


class Widget1(GridLayout):

    my_text = StringProperty('0')
    count_enable = BooleanProperty(False)
    sliderEnable = BooleanProperty(False)
    value_text = StringProperty('Volume is OFF')
    textInput = StringProperty('Search your image')
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

class ProjectApp(App):
    pass

ProjectApp().run()