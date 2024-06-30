import pygame
from configuraciones_personajes import*
from modulos.objetos_del_juego.Personajes import Personaje
class Heroe(Personaje):
    def __init__(self):
        super().__init__(animaciones,  velocidad)
        self.que_hace = "Quieto"
        self.contador_pasos = 0
        self.animacion_actual = self.animaciones["Quieto"]

        self.desplazamiento_y = 0
        self.potencia_salto = -15
        self.limite_velocidad_salto = 15
        self.gravedad = 1
        self.esta_saltando =False