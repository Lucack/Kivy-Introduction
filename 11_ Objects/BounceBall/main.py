from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty,BooleanProperty
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.graphics import *
import random

class BallBounce(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size=dp(50)
        with self.canvas:
            self.ball = Ellipse(pos=self.center, size=(self.ball_size, self.ball_size))
        Clock.schedule_interval(self.update , 1/60)
        start = [-4,-3,-2,2,3,4]
        self.vx = random.choice(start)
        self.vy = random.choice(start)

    def on_size(self, *args):
        # print('on size:', self.width, ',', self.height)
        self.ball.pos = self.center_x-self.ball_size/2 , self.center_y-self.ball_size/2

    def update(self, dt):
        # print("update")
        x,y = self.ball.pos
        self.ball.pos=(x+self.vx,y+self.vy)

        x,y = self.ball.pos
        if (x) < 0 or (x+self.ball_size) > self.width:
            self.vx*=-1
        if (y) < 0 or (y+self.ball_size) > self.height:
            self.vy*=-1


class ObjectsApp(App):
    pass

ObjectsApp().run()
