import pygame
from Particulas.clases.Conducto import Conducto
from Particulas.clases.Particula import Particula

class Simulacion:
    def __init__(self, forma, dimensiones, lado_particula, distancia_final):
        self.conducto = Conducto(forma, dimensiones)
        self.lado_particula = lado_particula
        self.distancia_final = distancia_final
        self.particulas = []

    def ejecutar(self):
        pygame.init()
        pantalla = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Simulación de Crecimiento")
        reloj = pygame.time.Clock()

        # Generar partículas
        particula = Particula(self.conducto.centro_x, self.conducto.centro_y, self.lado_particula)
        self.particulas.append(particula)

        en_ejecucion = True
        while en_ejecucion:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    en_ejecucion = False

            # Actualizar partículas
            for particula in self.particulas:
                particula.mover()
                if not self.conducto.verificar_adherencia(particula):
                    self.particulas.remove(particula)
                    break  # Eliminar la partícula del ciclo actual

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
