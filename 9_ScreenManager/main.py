from kivy.app import App
from kivy.uix.screenmanager import (ScreenManager,Screen,NoTransition,SlideTransition,CardTransition,SwapTransition,FadeTransition,WipeTransition,FallOutTransition,RiseInTransition)

# Create the manager
sm = ScreenManager()

# Add few screens
for i in range(4):
    screen = Screen(name='Title ' +str(i))
    sm.add_widget(screen)

# By default, the first screen added into the ScreenManager will be
# displayed. You can then change to another screen.

# Let's display the screen named 'Title 2'
# A transition will automatically be used.

sm.current = 'Title 2'

class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class screenApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))

        return sm

screenApp().run()