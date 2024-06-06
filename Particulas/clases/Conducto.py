import pygame, math

class Conducto:
    def __init__(self, forma, dimensiones):
        self.forma = forma
        self.dimensiones = dimensiones
        self.centro_x = 800 // 2
        self.centro_y = 600 // 2

    def dibujar(self, pantalla):
        if self.forma == "circular":
            radio = self.dimensiones[0] // 2
            pygame.draw.circle(pantalla, (128, 128, 128), (self.centro_x, self.centro_y), radio, 2)
        elif self.forma == "cuadrada":
            lado = self.dimensiones[0]
            pygame.draw.rect(pantalla, (128, 128, 128), (self.centro_x - lado // 2, self.centro_y - lado // 2, lado, lado), 2)
        elif self.forma == "rectangular":
            ancho = self.dimensiones[0]
            alto = self.dimensiones[1]
            pygame.draw.rect(pantalla, (128, 128, 128), (self.centro_x - ancho // 2, self.centro_y - alto // 2, ancho, alto), 2)


    def verificar_adherencia(self, particula):
        TOLERANCIA_ADHERENCIA = 2
        
        if self.forma == "circular":
            radio = self.dimensiones[0] // 2
            distancia_centro = math.sqrt((particula.x - self.centro_x)**2 + (particula.y - self.centro_y)**2)
            return distancia_centro <= radio + particula.lado // 2 + TOLERANCIA_ADHERENCIA
        elif self.forma == "cuadrada":
            lado = self.dimensiones[0]
            return particula.x >= self.centro_x - lado // 2 - TOLERANCIA_ADHERENCIA and \
                   particula.x <= self.centro_x + lado // 2 + TOLERANCIA_ADHERENCIA and \
                   particula.y >= self.centro_y - lado // 2 - TOLERANCIA_ADHERENCIA and \
                   particula.y <= self.centro_y + lado // 2 + TOLERANCIA_ADHERENCIA
        elif self.forma == "rectangular":
            ancho = self.dimensiones[0]
            alto = self.dimensiones[1]
            return particula.x >= self.centro_x - ancho // 2 - TOLERANCIA_ADHERENCIA and \
                   particula.x <= self.centro_x + ancho // 2 + TOLERANCIA_ADHERENCIA and \
                   particula.y >= self.centro_y - alto // 2 - TOLERANCIA_ADHERENCIA and \
                   particula.y <= self.centro_y + alto // 2 + TOLERANCIA_ADHERENCIA
