import math
import pygame, random


class Particula:
    def __init__(self, *, x:int, y:int, lado:int):
        self.x = x
        self.y = y
        self.lado = lado
        self.adesion = False

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, (0, 0, 0), (self.x, self.y, self.lado, self.lado))

    def mover(self) -> None:
        """
        Mueve la partícula en una dirección aleatoria.
        """
        movimiento = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])
        self.x += movimiento[0]
        self.y += movimiento[1]
    
    def colisiona_con_lados(self, otra_particula):
        if (self.x == otra_particula.x and abs(self.y - otra_particula.y) == self.lado) or \
           (self.y == otra_particula.y and abs(self.x - otra_particula.x) == self.lado):
            return True
        return False
    
    def distancia_al_centro(self, *, centro_x:int, centro_y:int):
        return math.sqrt((self.x - centro_x)**2 + (self.y - centro_y)**2)