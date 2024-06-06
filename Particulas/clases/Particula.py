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