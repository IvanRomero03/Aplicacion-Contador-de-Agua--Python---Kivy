import kivy
from kivy.app import App
from ConectorDB import BaseDeDatos
from inicioApp import PaginaInicio

class AppMain(App):
    def build(self):
        PaginaInicio()
        