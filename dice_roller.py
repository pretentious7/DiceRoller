from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.text import FontContextManager as FCM

import random

class ScatterTextWidget(BoxLayout):
    pass

class DiceRollerApp(App):
    def build(self):
        return ScatterTextWidget()

if __name__ == "__main__":
    DiceRollerApp().run()