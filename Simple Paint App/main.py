import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color,Line
from kivy.uix.button import Button


class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(random.random(), random.random(), random.random())
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

class MyPaintApp(App):

    def build(self):
        
        parent = Widget()
        self.painter = MyPaintWidget()
        clearbtn = Button(text='Clear')
        clearbtn.bind(on_release = self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        return parent

    def clear_canvas(self, event):
        self.painter.canvas.clear()


if __name__ == '__main__':
    MyPaintApp().run()