import os
import time
import pygame
from Particulas.clases.Conducto import Conducto
from Particulas.clases.Particula import Particula
from threading import Thread
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

    def __init__(self, forma: str, dimensiones: list[int], lado_particula: int, distancia_final: int, tolerancia: int):
        self.conducto = Conducto(forma=forma, dimensiones=dimensiones, tolerancia=tolerancia, distancia_final=distancia_final)
        self.lado_particula = lado_particula
        self.tolerancia = tolerancia
        self.distancia_final = distancia_final
        self.particulas: list[Particula] = []

    def generarParticula(self) -> None:
        """
        Genera una partícula en el centro del conducto.
        """
        while True:
            particula = Particula(
                x=self.conducto.centro_x,
                y=self.conducto.centro_y,
                lado=self.lado_particula
            )
            self.particulas.append(particula)
            time.sleep(1)

    def ejecutar(self):
        pygame.init()
        pantalla = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Simulación de movimiento de partículas")
        reloj = pygame.time.Clock()

        particula = Particula(
            x=self.conducto.centro_x,
            y=self.conducto.centro_y,
            lado=self.lado_particula
        )
        self.particulas.append(particula)

        hilo = Thread(target=self.generarParticula)
        hilo.start()

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
                        self.conducto.particulas_adheridas.append(particula)

                    for adherida in self.conducto.particulas_adheridas:
                        if particula.colisiona_con_lados(adherida):
                            particula.adesion = True
                            self.conducto.particulas_adheridas.append(particula)
                            break

            #! Dibujar
            pantalla.fill((255, 255, 255))
            self.conducto.dibujar(pantalla)
            self.dibujar_circulo(pantalla)
            for particula in self.particulas:
                particula.dibujar(pantalla)
            pygame.display.flip()

            #! Verificar condición de finalización
            for particula in self.conducto.particulas_adheridas:
                if particula.distancia_al_centro(centro_x=self.conducto.centro_x, centro_y=self.conducto.centro_y) <= self.distancia_final:
                    en_ejecucion = False
                    break

            reloj.tick(60)

        time.sleep(100)
        pygame.quit()
        os._exit(0)

    def dibujar_circulo(self, pantalla):
        """
        Dibuja un círculo en el centro del conducto con el radio especificado.
        """
        pygame.draw.circle(pantalla, (0, 0, 255), (self.conducto.centro_x, self.conducto.centro_y), self.distancia_final, 1)
