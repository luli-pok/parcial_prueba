import pygame
from assets.imagenes.fondo.fondos_juego import CIELO_1
from assets.imagenes.plataformas.plataformas import PLATAFORMA_0
from modulos.values.configuraciones_juego import Configuraciones
from modulos.objetos_del_juego.objeto import*
from modulos.objetos_del_juego.Plataformas import*
class Objeto_Juego(Configuraciones):
   def __init__(self, tamaño, FPS, título="Título", icono=""):
      super().__init__(tamaño, FPS, título, icono)

      #self.establecer_heroe()
      #self.establecer_enemigo()
      self.establecer_plataformas()

      self.teclas_presionadas = []
      
      self.set_background_image(CIELO_1,tamaño)


   def establecer_heroe(self):
      pass
      #self.objeto = self.get_rectangles(objeto)

   def establecer_plataformas(self):
      self.platafromas = Plataformas(0, 650, (1350, 30)).definir_plataformas()
      
      

   def establecer_enemigo(self):
      pass

   def manejar_comportamiento_heroe(self):
      # Obtener las teclas presionadas
      teclas = py.key.get_pressed()

      # if teclas[py.K_TAB]:
      #    cambiar_modo()
      # elif teclas[py.K_LEFT]:
      #    self.heroe.mover_izquierda()
      #    self.heroe.animacion_actual = self.heroe.animaciones["izquierda"]
      # elif teclas[py.K_RIGHT]:
      #    self.heroe.mover_derecha()
      #    self.heroe.animacion_actual = self.heroe.animaciones["derecha"]
      # elif teclas[py.K_UP]:
      #    self.heroe.saltar()
      #    self.heroe.animacion_actual = self.heroe.animaciones["arriba"]
      # else:
      #    self.heroe.detener()
      #    self.heroe.animacion_actual = self.heroe.animaciones["quieto"]

      # self.heroe.aplicar_gravedad(self.pantalla, lista_plataforma)
      # self.enemigo.verificar_colision_enemigo(lista_plataforma)
      # self.enemigo.aplicar_gravedad_enemigo(self.pantalla, lista_plataforma)
      # self.heroe.verificar_colision(lista_plataforma)

   def mostrar_plataformas(self,pantalla):
      for plataforma in self.platafromas:
         pantalla.blit(plataforma.objeto["superficie"], plataforma.objeto["rectangulo"])


   def mostrar_heroe(self):
      pass
      
      

    
                

   def get_rectangles(main:pygame.Rect):
      self.dictionary = {}
      if len(main) > 0 and isinstance(main, pygame.Rect):
         self.dictionary["main"] = main
         self.dictionary["bottom"] = pygame.Rect(main.left, main.bottom - 12, main.width, 12)
         self.dictionary["right"] = pygame.Rect(main.right - 10, main.top, 10, main.height)
         self.dictionary["left"] = pygame.Rect(main.left, main.top, 10, main.height)
         self.dictionary["top"] = pygame.Rect(main.left, main.top , main.width, 12)
      
   def move(self, rectangles: list[dict[pygame.Rect]], speed) -> None:
      for side in rectangles:
         rectangles[side].x += speed

   def init(self):
      pygame.init()

      while self.bandera_inicio:
         self.fill_screen()
         
         self.clock.tick(self.FPS)            

         for evento in pygame.event.get():
               if evento.type == pygame.QUIT:
                  self.bandera_inicio = False
               if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                  x, y = pygame.mouse.get_pos() 
                  print(f"POS X: {x} | POS Y: {y}")
         
         self.mostrar_plataformas(self.pantalla)
               
               
            
         

            
            
         pygame.display.flip()
        
      pygame.quit()