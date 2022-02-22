import kivy 
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class Contador(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.contador = 0
        self.texto = Label(text='asd ' + str(self.contador))
        self.texto.center_y = self.center_y - 25 
        self.texto.center_x = self.center_x + 50
        self.boton = Button(text='+1', on_press=self.incrementar)
        self.boton.center_y = self.center_y + 25
        self.boton.center_x = self.center_x
        self.add_widget(self.texto, index=0)
        self.add_widget(self.boton, index=50)
    def incrementar(self, *args):
        self.contador += 1
        self.texto.text = 'asd ' + str(self.contador)

class AppPrueba(App):
    def build(self):
        return Contador()

AppPrueba().run()