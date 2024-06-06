import pygame, math

from Particulas.clases.Particula import Particula

class Conducto:
    """
    Clase que modela un conducto por donde se desplazan las partículas.
    
    Args:
    
    Attributes:
    """
    
    
    def __init__(self, *, forma:str, dimensiones:list[int], tolerancia:int, distancia_final:int):
        self.forma = forma
        self.dimensiones = dimensiones
        self.toleracia = tolerancia
        self.distancia_final = distancia_final
        self.particulas_adheridas:list[Particula] = []
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


    def verificar_adherencia(self, particula) -> bool:
        """
        Verifica si la partícula se encuentra adherida al conducto.
        
        Returns:
            - bool: True si la partícula se encuentra adherida al conducto, False en caso contrario.
        """
        #! Circular
        if self.forma == "circular":
            radio = self.dimensiones[0] // 2
            distancia_centro = math.sqrt((particula.x - self.centro_x)**2 + (particula.y - self.centro_y)**2)
            return not (distancia_centro <= radio + particula.lado // 2 - self.toleracia)
        
        #! Cuadrada
        elif self.forma == "cuadrada":
            lado = self.dimensiones[0]
            return not(
                particula.x >= self.centro_x - lado // 2 + self.toleracia and \
                particula.x <= self.centro_x + lado // 2 - self.toleracia and \
                particula.y >= self.centro_y - lado // 2 + self.toleracia and \
                particula.y <= self.centro_y + lado // 2 - self.toleracia
            )
            
        #! Rectangular
        else:
            ancho = self.dimensiones[0]
            alto = self.dimensiones[1]
            return not(
                particula.x >= self.centro_x - ancho // 2 + self.toleracia and \
                particula.x <= self.centro_x + ancho // 2 - self.toleracia and \
                particula.y >= self.centro_y - alto // 2 + self.toleracia and \
                particula.y <= self.centro_y + alto // 2 - self.toleracia
            )