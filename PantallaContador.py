import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from ConectorDB import BaseDeDatos
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from kivy.clock import Clock
from kivy.uix.image import AsyncImage
# from kivy.config import Config
# Config.set('graphics', 'width', '2000')
# Config.set('graphics', 'height', '2000')

class Pantalla(Widget):
    def __init__(self):
        super().__init__()
        # self.size = (1000, 1000)
        self.DB = BaseDeDatos()
        self.TextoFijo = Label(text='Contador')
        self.TextoCont = Label(text=str(self.calcularValor()))
        self.add_widget(self.TextoFijo)
        self.TextoFijo.center_x = self.center_x + 250
        self.TextoFijo.center_y = self.center_y + 300 + 100
        self.TextoFijo.font_size = 50
        self.add_widget(self.TextoCont)
        self.TextoCont.center_x = self.center_x + 250
        self.TextoCont.center_y = self.center_y + 200 + 125
        self.TextoCont.font_size = 50
        # self.BotonCont = Button(text='Actualizar \n contador', on_press=self.on_press)
        # self.add_widget(self.BotonCont)
        # self.BotonCont.center_x = self.center_x + 250
        # self.BotonCont.center_y = self.center_y + 50
        # self.BotonGrafica = Button(text='Graficar', on_press=self.on_press2)
        # self.add_widget(self.BotonGrafica)
        self.grafica()
        self.Histograma.center_x = self.center_x + 250
        self.Histograma.center_y = self.center_y + 150
        self.add_widget(self.Histograma)
        event = Clock.schedule_interval(self.on_update, .1)

    def on_press2(self, *args):
        self.grafica()
        self.add_widget(self.Histograma)
        self.Histograma.allow_stretch = True
        self.Histograma.center_x = self.center_x + 250
        self.Histograma.center_y = self.center_y + 50
    
    def on_update(self, *args):
        self.on_press()
        self.ActualizarGrafica()
        self.Histograma.reload()

    def ActualizarGrafica(self):
        registro = self.DB.selectRegistroUsuarioFecha(1, datetime.now() - timedelta(days=1), datetime.now())
        newTable = []
        for i in registro:
            newTable.append(i[2])
        plt.hist(newTable, bins=10)
        plt.savefig('histograma.png')
        plt.close()

    def grafica(self):
        registro = self.DB.selectRegistroUsuarioFecha(1, datetime.now() - timedelta(days=1), datetime.now())
        newTable = []
        for i in registro:
            newTable.append(i[2])
        plt.hist(newTable, bins=10)
        plt.savefig('histograma.png')
        plt.close()
        self.Histograma = Image(source='histograma.png',nocache=True)
        self.Histograma.allow_stretch = True
        self.Histograma.keep_ratio = True
        self.Histograma.size = (self.Histograma.get_norm_image_size()[0] + 250, self.Histograma.get_norm_image_size()[1] + 250)


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