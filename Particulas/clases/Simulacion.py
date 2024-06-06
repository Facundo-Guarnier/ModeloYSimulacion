import os, time, pygame
from threading import Thread

from Particulas.clases.Conducto import Conducto
from Particulas.clases.Particula import Particula

class Simulacion:
    """
    Clase que modela la simulación de movimiento de partículas dentro de un conducto.
    
    Args:
        - forma (str): Forma del conducto por donde se desplazan las partículas.
        - dimensiones (list[int]): Dimensiones del conducto.
        - lado_particula (int): Tamaño de la particula cuadrada.
        - distancia_final (int): Distancia final al centro del conducto para finalizar la simulacion.
        - tolerancia (int): Tolerancia de adherencia.
        - velocidad (int): Velocidad de la simulación.
    
    Attributes:
        - conducto (Conducto): Conducto por el cual se desplazan las partículas.
        - lado_particula (int): Tamaño de la particula cuadrada.
        - distancia_final (int): Distancia final al centro del conducto para finalizar la simulacion.
        - tolerancia (int): Tolerancia de adherencia.
        - particulas (list[Particula]): Partículas en la simulación.
        - velocidad (int): Velocidad de la simulación.
        - generar (bool): Indica si se generan partículas.
    """
    def __init__(self, *, forma:str, dimensiones:list[int], lado_particula:int, distancia_final:int, tolerancia:int, velocidad:int) -> None:
        self.conducto:Conducto = Conducto(forma=forma, dimensiones=dimensiones, tolerancia=tolerancia, distancia_final=distancia_final)
        self.lado_particula:int = lado_particula
        self.distancia_final:int = distancia_final
        self.tolerancia:int = tolerancia
        self.particulas: list[Particula] = []
        self.velocidad:int = velocidad
        
        self.generar:bool = True
    
    
    def generarParticula(self) -> None:
        """
        Genera particulas en el conducto cada 120/velocidad segundos (cada 2 segundos en simulacion).
        """
        while self.generar:
            time.sleep(120/self.velocidad) #! Una particula cada 2 segundos en la simulacion.
            particula = Particula(
                x=self.conducto.centro_x,
                y=self.conducto.centro_y,
                lado=self.lado_particula
            )
            self.particulas.append(particula)
    
    
    def ejecutar(self) -> None:
        """
        Ejecuta la simulación de movimiento de partículas.
        """
        
        pygame.init()
        ventana = pygame.display.set_mode((800, 450), pygame.RESIZABLE)  #! Ventana redimensionable
        pygame.display.set_caption("Simulación de movimiento de partículas")
        reloj = pygame.time.Clock()
        
        #! Superficie interna de dibujo
        superficie_interna = pygame.Surface((1865, 1050))
        
        #! Primera partícula
        particula = Particula(
            x=self.conducto.centro_x,
            y=self.conducto.centro_y,
            lado=self.lado_particula
        )
        self.particulas.append(particula)
        
        #! Hilo para generar partículas
        hilo = Thread(target=self.generarParticula)
        hilo.start()
        
        
        #! Tics de la simulacion
        tics = 0  # Contador de tics
        pygame.font.init()
        font = pygame.font.SysFont("Arial", 30)
        
        en_ejecucion = True
        
        while en_ejecucion:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    en_ejecucion = False
            
            if self.generar:
                #! Mover partículas
                for particula in self.particulas:
                    if not particula.adhesion:
                        particula.mover()
                        
                        #! Si la particula toca un lado del conducto
                        if self.conducto.verificar_adherencia(particula):
                            particula.adhesion = True
                            self.conducto.particulas_adheridas.append(particula)
                        
                        #! Si la particula colisiona con otra particula
                        else:
                            for adherida in self.conducto.particulas_adheridas:
                                if particula.colisiona_otra_particula(adherida):
                                    particula.adhesion = True
                                    self.conducto.particulas_adheridas.append(particula)
                                    break
                        
                        #! Verificar condición de finalización
                        if  self.conducto.en_zona_limite(particula=particula):
                            self.generar = False
                            particula.color = (255, 0, 0)
                            break
                tics += 1
            
            #! Dibujar
            superficie_interna.fill((255, 255, 255))
            self.conducto.dibujar(superficie_interna)
            for particula in self.particulas:
                particula.dibujar(superficie_interna)
            self.conducto.dibujar_zona_limite(superficie_interna)
            
            #! Dibujar texto
            texto = font.render(f'Partículas adheridas: {len(self.conducto.particulas_adheridas)}/{len(self.particulas)}', True, (0, 0, 0))
            superficie_interna.blit(texto, (10, 10))
            
            texto = font.render(f'Velocidad: {self.velocidad}', True, (0, 0, 0))
            superficie_interna.blit(texto, (10, 50))
            
            texto = font.render(f'Tics: {tics}', True, (0, 0, 0))
            superficie_interna.blit(texto, (10, 90))
            
            #! Escalar la superficie interna para que quepa en la ventana
            superficie_escalada = pygame.transform.scale(superficie_interna, ventana.get_size())
            ventana.blit(superficie_escalada, (0, 0))
            pygame.display.flip()
            
            #! Velocidad de la simulación
            reloj.tick(self.velocidad)
        
        pygame.quit()