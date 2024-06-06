import pygame, math

from Particulas.clases.Particula import Particula

class Conducto:
    """
    Clase que modela un conducto por donde se desplazan las partículas.
    
    Args:
        - forma (str): Forma del conducto (circular, cuadrada, rectangular).
        - dimensiones (list[int]): Dimensiones del conducto.
        - tolerancia (int): Tolerancia de adherencia.
        - distancia_final (int): Distancia final al centro del conducto para finalizar la simulacion.
    
    Attributes:
        - forma (str): Forma del conducto (circular, cuadrada, rectangular).
        - dimensiones (list[int]): Dimensiones del conducto.
        - tolerancia (int): Tolerancia de adherencia.
        - distancia_final (int): Distancia final al centro del conducto para finalizar la simulacion.
        - particulas_adheridas (list[Particula]): Partículas adheridas al conducto.
        - centro_x (int): Coordenada x del centro del conducto.
        - centro_y (int): Coordenada y del centro del conducto.
    """
    def __init__(self, *, forma:str, dimensiones:list[int], tolerancia:int, distancia_final:int) -> None:
        self.forma = forma
        self.dimensiones = dimensiones
        self.tolerancia = tolerancia
        self.distancia_final = distancia_final
        self.particulas_adheridas:list[Particula] = []
        self.centro_x = 1865 // 2
        self.centro_y = 1050 // 2
    
    
    def dibujar(self, pantalla:pygame.Surface) -> None:
        """
        Dibuja el conducto en la pantalla.
        
        Args:
            - pantalla (Surface): Pantalla de pygame.
        """
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
    
    
    def dibujar_zona_limite(self, pantalla:pygame.Surface) -> None:
        """
        Dibuja un círculo en el centro del conducto con el radio = distancia_final.
        
        Args:
            - pantalla (Surface): Pantalla de pygame.
        """
        pygame.draw.circle(pantalla, (0, 0, 255), (self.centro_x, self.centro_y), self.distancia_final, 2)
    
    
    def verificar_adherencia(self, particula:Particula) -> bool:
        """
        Verifica si la partícula se encuentra adherida al conducto.
        
        Args:
            - particula (Particula): Partícula a verificar.
        
        Returns:
            - bool: True si la partícula se encuentra adherida al conducto, False en caso contrario.
        """
        #! Circular
        if self.forma == "circular":
            radio = self.dimensiones[0] // 2
            distancia_centro = math.sqrt((particula.x - self.centro_x)**2 + (particula.y - self.centro_y)**2)
            return not (distancia_centro <= radio + particula.lado // 2 - self.tolerancia)
        
        #! Cuadrada
        elif self.forma == "cuadrada":
            lado = self.dimensiones[0]
            return not(
                particula.x >= self.centro_x - lado // 2 + self.tolerancia and \
                particula.x <= self.centro_x + lado // 2 - self.tolerancia and \
                particula.y >= self.centro_y - lado // 2 + self.tolerancia and \
                particula.y <= self.centro_y + lado // 2 - self.tolerancia
            )
        
        #! Rectangular
        else:
            ancho = self.dimensiones[0]
            alto = self.dimensiones[1]
            return not(
                particula.x >= self.centro_x - ancho // 2 + self.tolerancia and \
                particula.x <= self.centro_x + ancho // 2 - self.tolerancia and \
                particula.y >= self.centro_y - alto // 2 + self.tolerancia and \
                particula.y <= self.centro_y + alto // 2 - self.tolerancia
            )
    
    
    def en_zona_limite(self, *, particula:'Particula') -> bool:
        """
        Verifica si el perímetro de la partícula se encuentra en la zona límite del conducto.
            - Verifica si la partícula está adherida a algo.
            - Calcula la distancia del borde de la partícula al centro del conducto.
        
        Args:
            - particula (Particula): Partícula a verificar.
        
        Returns:
            - bool: True si la partícula se encuentra en la zona límite del conducto, False en caso contrario.
        """
        if not particula.adhesion:
            return False
        
        #! Calcula la distancia del borde de la partícula al centro del conducto
        distancia_centro = math.sqrt((particula.x - self.centro_x)**2 + (particula.y - self.centro_y)**2)
        #! Calcula la distancia del borde de la partícula al centro del conducto
        distancia_borde = distancia_centro - particula.lado / 2
        #! Verifica si el borde de la partícula está dentro de la distancia final
        return distancia_borde <= self.distancia_final