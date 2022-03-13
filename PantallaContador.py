import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from ConectorDB import BaseDeDatos
from datetime import datetime, timedelta

class Pantalla(Widget):
    def __init__(self):
        super().__init__()
        self.DB = BaseDeDatos()
        self.TextoFijo = Label(text='Contador')
        self.TextoCont = Label(text=str(self.calcularValor()))
        self.add_widget(self.TextoFijo)
        self.TextoFijo.center_x = self.center_x + 250
        self.TextoFijo.center_y = self.center_y + 300
        self.add_widget(self.TextoCont)
        self.TextoCont.center_x = self.center_x + 250
        self.TextoCont.center_y = self.center_y + 150
        self.BotonCont = Button(text='Actualizar \n contador', on_press=self.on_press)
        self.add_widget(self.BotonCont)
        self.BotonCont.center_x = self.center_x + 250
        self.BotonCont.center_y = self.center_y + 50

    def calcularValor(self):
        self.DB = BaseDeDatos()
        registro = self.DB.selectRegistroUsuarioFecha(1, datetime.now() - timedelta(days=1), datetime.now())
        registro = len(registro)
        return registro

    def on_press(self, *args):
        self.TextoCont.text = str(self.calcularValor())

class Apps(App):
    def build(self):
        return Pantalla()

Apps().run()