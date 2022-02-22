from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import kivy

# python -m virtualenv kivy_venv
# kivy_venv\Scripts\activate

kivy.require('2.0.0')

class HelloWorld(App):
    def build(self):
        return Label(text='Hello World!')


HelloWorld().run()