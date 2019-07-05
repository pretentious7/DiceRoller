from kivy.app import App

from kivmob import KivMob, TestIds
from kivy.core.text import LabelBase

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.text import FontContextManager as FCM

import random

class ScatterTextWidget(BoxLayout):
    APPID = 'ca-app-pub-4594686446272625~3110544260'
    BANNERID = 'ca-app-pub-4594686446272625/3787177591'
    ads = KivMob(APPID)
    ads.new_banner(BANNERID)
    ads.request_banner()
    ads.show_banner()

    pass

class DiceRollerApp(App):
    def build(self):
        LabelBase.register(name='roboto-thinitalic', fn_regular='Roboto-ThinItalic.ttf')

        return ScatterTextWidget()

if __name__ == "__main__":
    DiceRollerApp().run()