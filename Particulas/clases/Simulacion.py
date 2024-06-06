import pygame
from Particulas.clases.Conducto import Conducto
from Particulas.clases.Particula import Particula

class Simulacion:
    """
    Clase que modela la simulación de movimiento de partículas.
    
    Args:
        - forma (str): Forma del conducto por donde se desplazan las partículas.
        - dimensiones (list[int]): Dimensiones del conducto.
        - lado_particula (int): Tamaño de la particula cuadrada.
        - distancia_final (int): Distancia final al centro del conducto para finalizar la simulacion.
        - tolerancia (int): Tolerancia de adherencia.
    
    Attributes:
        - conducto (Conducto): Conducto por el cual se desplazan las partículas.
        - lado_particula (int): Tamaño de la particula cuadrada.
        - distancia_final (int): Distancia final al centro del conducto para finalizar la simulacion.
        - tolerancia (int): Tolerancia de adherencia.
        - particulas (list[Particula]): Partículas en la simulación.
    """
    
    def __init__(self, forma:str, dimensiones:list[int], lado_particula:int, distancia_final:int, tolerancia:int):
        self.conducto = Conducto(forma=forma, dimensiones=dimensiones, tolerancia=tolerancia)
        self.lado_particula = lado_particula
        self.distancia_final = distancia_final
        self.tolerancia = tolerancia 
        self.particulas:list[Particula] = []
    
    
    def ejecutar(self):
        pygame.init()
        pantalla = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Simulación de movimiento de partículas")
        reloj = pygame.time.Clock()

        #! Generar partículas
        particula = Particula(
            x=self.conducto.centro_x, 
            y=self.conducto.centro_y, 
            lado=self.lado_particula
        )
        self.particulas.append(particula)

        en_ejecucion = True
        while en_ejecucion:
            
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    en_ejecucion = False

            #! Mover partículas
            for particula in self.particulas:
                if not particula.adesion:
                    particula.mover()
                    if self.conducto.verificar_adherencia(particula):
                        particula.adesion = True

            # Dibujar
            pantalla.fill((255, 255, 255))
            self.conducto.dibujar(pantalla)
            for particula in self.particulas:
                particula.dibujar(pantalla)
            pygame.display.flip()

            # Verificar condición de finalización
            if any(abs(particula.x - self.conducto.centro_x) >= self.distancia_final for particula in self.particulas) or \
               any(abs(particula.y - self.conducto.centro_y) >= self.distancia_final for particula in self.particulas):
                en_ejecucion = False

            reloj.tick(60)  # Limitar la frecuencia de actualización

        pygame.quit()
