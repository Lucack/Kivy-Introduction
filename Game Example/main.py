from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty,BooleanProperty,NumericProperty
from kivy.metrics import dp
from kivy.graphics import *

class MainWidget(Widget):
    perspective_x = NumericProperty(0)
    perspective_y = NumericProperty(0)
    V_LINES = 6
    V_LINES_SPACING = 0.3 # percentage in screen width
    v_lines = []

    H_LINES = 3

    H_LINES_SPACING = 0.2
    h_lines = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.init_vertical_lines()
        self.init_horizontal_lines()

    
    def on_size(self, *args):
        self.update_lines_v()
        self.update_lines_h()

    def on_perspective_x(self, widget, value):
        pass

    def on_perspective_y(self, widget, value):
        pass

    def init_vertical_lines(self):
        with self.canvas:
            Color(1,1,1)
            for i in range(self.V_LINES):
                self.v_lines.append(Line())

    def init_horizontal_lines(self):
        with self.canvas:
            Color(1,1,1)
            for i in range(self.H_LINES):
                self.h_lines.append(Line())

    def update_lines_v(self):
        central_line_x = int(self.width/2)
        spacing = self.V_LINES_SPACING*self.width
        count = int(-(self.V_LINES)/2)
        for i in range(self.V_LINES):
            line_x  = int(central_line_x + count*spacing+spacing/2)
            self.v_lines[i].points = [line_x,0,self.perspective_x,self.perspective_y]
            global deltax
            global deltay
            deltax = line_x-self.perspective_x
            deltay = self.perspective_y
            print("deltax:",deltax)
            count += 1

    def update_lines_h(self):
        central_line_y = int(self.perspective_y/2)
        spacingy = self.H_LINES_SPACING*self.height
        spacingx = self.V_LINES_SPACING*self.width
        county = int((self.H_LINES)/2)
        for i in range(self.H_LINES):
            line_y = int(central_line_y + county*spacingy)
            line_y = self.height-line_y
            print("liney",line_y)
            if 0 <= line_y < self.perspective_y:
                x = int(((self.perspective_y - line_y)*deltax)/deltay)
                print('x',x,'y',line_y)
                self.h_lines[i].points = [self.perspective_x-x,line_y,self.perspective_x+x,line_y]
            county -= 1
            print(line_y)

class GameApp(App):
    pass

GameApp().run()
