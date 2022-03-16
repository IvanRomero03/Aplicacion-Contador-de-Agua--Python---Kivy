import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from ConectorDB import BaseDeDatos


kivy.require('2.0.0')

class EntradaDeTexto(Widget):

    def __init__(self):
        super().__init__()
        self.DB = BaseDeDatos()
        self.OCULTO = ''
        self.texto = 'Introduzca su correo'
        self.TextoChilo = Label(text=self.texto)
        self.add_widget(self.TextoChilo)

        self.TextoChilo.center_x = self.center_x + 250
        self.TextoChilo.center_y = self.center_y + 150

        self.textReciber = ''

        self.texto_entrada = TextInput(text='asd', multiline=False)

        self.texto_entrada.bind(text=self.on_text)

        self.add_widget(self.texto_entrada)
        
        self.texto_entrada.center_x = self.center_x + 250
        self.texto_entrada.center_y = self.center_y + 50

    def on_text(self, *args):
        self.textReciber = self.texto_entrada.text
        self.TextoChilo.text = self.textReciber
        self.OCULTO = self.textReciber

class AppS(App):
    def build(self):
        return EntradaDeTexto()

AppS().run()