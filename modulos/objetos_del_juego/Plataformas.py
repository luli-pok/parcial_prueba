import pygame
from modulos.objetos_del_juego.objeto import*
from assets.imagenes.plataformas.plataformas import PLATAFORMA_0

class Plataformas(Objeto):
    def __init__(self, x, y, tamaño, imagen=""):
        super().__init__(x, y, tamaño, imagen=imagen)
        # Resto de tu código...

        self.plataformas = []

    def definir_plataformas(self):
        piso = Plataformas(0, 630, (1350, 20), PLATAFORMA_0)
        plataforma_1 = Plataformas(280, 375, (120, 20), PLATAFORMA_0)
        plataforma_2 = Plataformas(470, 520, (120, 20), PLATAFORMA_0)
        self.plataformas = [piso, plataforma_1, plataforma_2]
        return self.plataformas

        
        
        
    