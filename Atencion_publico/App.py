from matplotlib import pyplot as plt
from Atencion_publico.clases.Modelo import Modelo

class App:
    """
    Clase que representa un modelo de Atención al Público.
    Características:
    - El servicio abre a las 8 y cierra a las 12.
    - Los clientes que están en la cola o siendo atendidos pueden permanecer dentro del local despues del cierre.
    - Los que no están siendo atendidos abandonarán el local a los 30 minutos.
    - En cada segundo que transcurre, la probabilidad de que ingrese un cliente es de P = 1/144
    - Los boxes activos se establecen al iniciar la simulación (1 - 10).
    - Tiempo de atención en los boxes: µ = 10 minutos, sd = 5 minutos.
    - Cada box cuesta $1000.
    - Cada cliente no atendido se pierde, con un costo de $10.000.
    """
    
    def __init__(self, modelo:Modelo) -> None:
        self.modelo = modelo
    
    def __str__(self) -> str:
        return (
            "Modelo de Atención al Público\n" +
            f"Numero de Boxes: {str(self.modelo.num_boxes)}\n" +
            f"Tiempo de Simulación: {str(self.modelo.tiempo_simulacion / 60)} minutos\n"
        )
    
    
    def punto_1(self) -> str:
        """
        Cuantos clientes ingresaron.
        """
        return(f"Punto 1: Clientes ingresados: {self.modelo.clientes_totales}")
    
    
    def punto_2(self) -> str:
        """
        Cuantos clientes fueron atendidos.
        """
        return(f"Punto 2: Clientes atendidos: {self.modelo.clientes_atendidos}")
    
    
    def punto_3(self) -> str:
        """
        Cuantos clientes no fueron atendidos. Es decir abandonaron el local por demoras.
        """
        return(f"Punto 3: Clientes no atendidos: {self.modelo.clientes_no_atendidos}")
    
    
    def punto_4(self) -> str:
        """
        Tiempo mínimo de atención en box.
        """
        return(f"Punto 4: Tiempo mínimo de atención: {self.modelo.tiempo_min_atencion_historico / 60:.2f} minutos")
    
    
    def punto_5(self) -> str:
        """
        Tiempo máximo de atención
        """
        return(f"Punto 5: Tiempo máximo de atención: {self.modelo.tiempo_max_atencion_historico / 60:.2f} minutos")    
    
    
    def punto_6(self) -> str:
        """
        Tiempo mínimo de espera en salón.
        """
        return(f"Punto 6: Tiempo mínimo de espera en salón: {self.modelo.tiempo_min_espera_salón_historico / 60:.2f} minutos")
    
    def punto_7(self) -> str:
        """
        Tiempo máximo de espera dentro del local.
        """
        
        return(f"Punto 7: Tiempo máximo de espera dentro del local: {self.modelo.tiempo_max_espera_salón_historico / 60:.2f} minutos")
        
    def punto_8(self) -> str:
        """
        Costo total de la operación.
        """
        return(f"Punto 8: Costo total de la operación: ${self.modelo.costo_total}")
    
    def punto_9A(self) -> None:
        """
        Graficar la distribución de personas en el local.
        """
        print("Punto 9A: Gráfico de la distribución de personas en el local.")
        tiempos, clientes_en_cola, clientes_en_atencion = zip(*self.modelo.clientes_historico)
        fig, ax = plt.subplots()
        ax.plot(tiempos, clientes_en_cola, label="Clientes en Cola")
        ax.plot(tiempos, clientes_en_atencion, label="Clientes en Atención")
        ax.set_xlabel("Tiempo (segundos)")
        ax.set_ylabel("Número de Clientes")
        ax.legend()
        plt.show()
    
    
    def punto_9B(self, velocidad: int = 10):
        """
        Presentación gráfica animada de cada proceso simulado, con diversas velocidades. Archivo AVI.
        
        Args:
            velocidad: Velocidad de la animación (frames por segundo).
            nombre_archivo: Nombre del archivo AVI.
        """
        import pygame
        from moviepy.editor import ImageSequenceClip
        
        pygame.init()
        
        #! Lista para almacenar los fotogramas
        frames = []
        
        #! Configuraciones de la pantalla
        screen_width = 1200
        screen_height = 600
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption('Simulación de Atención al Público')
        
        #! Colores
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)
        
        #! Configuración de la simulación
        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 36)
        
        #! Extraer datos de la simulación
        tiempos, clientes_en_cola, clientes_en_atencion = zip(*self.modelo.clientes_historico)
        
        #! Posiciones y tamaños
        box_width = 80
        box_height = 50
        margin = 20
        tiempo_start_x = 50
        tiempo_start_y = 50
        cola_start_x = 50
        cola_start_y = 150
        box_start_x = 50
        box_start_y = 250
        
        #! Loop de animación
        running = True
        frame = 0
        
        while running and frame < len(tiempos):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            screen.fill(WHITE)
            
            #! Dibujar la cola de clientes
            cola_text = font.render(f"Clientes en cola: {clientes_en_cola[frame]}", True, BLACK)
            screen.blit(cola_text, (cola_start_x, cola_start_y - 50))
            for i in range(clientes_en_cola[frame]):
                pygame.draw.circle(screen, BLUE, (cola_start_x + (i * 25) + 15, cola_start_y), 10)
            
            #! Dibujar los clientes en los boxes
            text = font.render("Clientes en atención", True, BLACK)
            screen.blit(text, (box_start_x, box_start_y - 50))
            for i in range(self.modelo.num_boxes):
                box_x = box_start_x + i * (box_width + margin)
                pygame.draw.rect(screen, BLACK, (box_x, box_start_y, box_width, box_height), 2)
                if i < clientes_en_atencion[frame]:
                    pygame.draw.circle(screen, GREEN, (box_x + box_width // 2, box_start_y + box_height // 2), 10)
                    if i == self.modelo.num_boxes - 1:
                        text = font.render("Boxes llenos", True, RED)
                        screen.blit(text, (box_start_x + 270, box_start_y - 50))
            
            #! Mostrar tiempo
            tiempo_text = font.render(f"Tiempo: {tiempos[frame]}s", True, BLACK)
            screen.blit(tiempo_text, (tiempo_start_x, tiempo_start_y))
            
            #! Mostrar datos finales
            texts = [
                self.punto_1(),
                self.punto_2(),
                self.punto_3(),
                self.punto_4(),
                self.punto_5(),
                self.punto_6(),
                self.punto_7(),
                self.punto_8(),
            ]
            for i, t in enumerate(texts):
                text = font.render(t, True, BLACK)
                screen.blit(text, (box_start_x, box_start_y + 75 + (i * 30)))
            
            #! Capturar el fotograma para el video
            frame_surface = pygame.surfarray.array3d(screen)
            frames.append(frame_surface.swapaxes(0, 1))  # Swapping the axes to match the expected format
            
            #! Guardar frame
            pygame.display.flip()
            clock.tick(velocidad)
            frame += 1
        
        pygame.quit()
        
        #! Crear el video con MoviePy
        clip = ImageSequenceClip(frames, fps=velocidad)
        clip.write_videofile(f"Animacion_{self.modelo.num_boxes}-boxes.avi", codec='mpeg4')
    
    
    def main(self) -> None:
        """
        Función principal que ejecuta el TP de Atención al Público: Tp7
        """
        print(self.__str__())
        self.modelo.simular()
        print("-"*15)
        print(self.punto_1())
        print("-"*15)
        print(self.punto_2())
        print("-"*15)
        print(self.punto_3())
        print("-"*15)
        print(self.punto_4())
        print("-"*15)
        print(self.punto_5())
        print("-"*15)
        print(self.punto_6())
        print("-"*15)
        print(self.punto_7())
        print("-"*15)
        print(self.punto_8())
        print("-"*15)
        self.punto_9A()
        # print("-"*15)
        # self.punto_9B(velocidad=600)