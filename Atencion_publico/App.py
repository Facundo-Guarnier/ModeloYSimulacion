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
    def punto_1(self) -> None:
        """
        Cuantos clientes ingresaron.
        """
        print(f"Punto 1:\nClientes ingresados: {self.modelo.clientes_totales}")
    
    
    def punto_2(self) -> None:
        """
        Cuantos clientes fueron atendidos.
        """
        print(f"Punto 2:\nClientes atendidos: {self.modelo.clientes_atendidos}")
    
    
    def punto_3(self) -> None:
        """
        Cuantos clientes no fueron atendidos. Es decir abandonaron el local por demoras.
        """
        print(f"Punto 3:\nClientes no atendidos: {self.modelo.clientes_no_atendidos}")
    
    
    def punto_4(self) -> None:
        """
        Tiempo mínimo de atención en box.
        """
        print(f"Punto 4:\nTiempo mínimo de atención: {self.modelo.tiempo_min_atencion_historico / 60:.2f} minutos")
    
    
    def punto_5(self) -> None:
        """
        Tiempo máximo de atención
        """
        print(f"Punto 5:\nTiempo máximo de atención: {self.modelo.tiempo_max_atencion_historico / 60:.2f} minutos")    
    
    
    def punto_6(self) -> None:
        """
        Tiempo mínimo de espera en salón.
        """
        print(f"Punto 6:\nTiempo mínimo de espera en salón: {self.modelo.tiempo_min_espera_salón_historico / 60:.2f} minutos")
    
    def punto_7(self) -> None:
        """
        Tiempo máximo de espera dentro del local.
        """
        
        print(f"Punto 7:\nTiempo máximo de espera dentro del local: {self.modelo.tiempo_max_espera_salón_historico / 60:.2f} minutos")
        
    def punto_8(self) -> None:
        """
        Costo total de la operación.
        """
        print(f"Punto 8:\nCosto total de la operación: {self.modelo.costo_total}")
    
    def punto_9A(self) -> None:
        """
        Graficar la distribución de personas en el local.
        """
        tiempos, clientes_en_cola, clientes_en_atencion = zip(*self.modelo.clientes_historico)
        fig, ax = plt.subplots()
        ax.plot(tiempos, clientes_en_cola, label="Clientes en Cola")
        ax.plot(tiempos, clientes_en_atencion, label="Clientes en Atención")
        ax.set_xlabel("Tiempo (segundos)")
        ax.set_ylabel("Número de Clientes")
        ax.legend()
        plt.show()
    
    
    def punto_9B(self, velocidad: int = 10, nombre_archivo: str = "animacion.avi"):
        """
        Presentación gráfica animada de cada proceso simulado, con diversas velocidades. Archivo AVI.
        
        Args:
            velocidad: Velocidad de la animación (frames por segundo).
            nombre_archivo: Nombre del archivo AVI.
        """
        import numpy as np
        import matplotlib.pyplot as plt
        from matplotlib.animation import FuncAnimation, writers
        tiempos, clientes_en_cola, clientes_en_atencion = zip(*self.modelo.clientes_historico)
        fig, ax = plt.subplots()
        line_cola, = ax.plot([], [], label="Clientes en Cola", marker='o', linestyle='-', color='blue')
        line_atencion, = ax.plot([], [], label="Clientes en Atención", marker='s', linestyle='-', color='red')
        ax.set_xlim(0, self.modelo.tiempo_simulacion)
        ax.set_ylim(0, max(clientes_en_cola) * 1.1)
        ax.set_xlabel("Tiempo (segundos)")
        ax.set_ylabel("Número de Clientes")
        ax.legend()
        
        def animate(i):
            line_cola.set_data(tiempos[:i], clientes_en_cola[:i])
            line_atencion.set_data(tiempos[:i], clientes_en_atencion[:i])
            return line_cola, line_atencion
        
        anim = FuncAnimation(fig, animate, frames=len(tiempos), interval=1000/velocidad, blit=True)
        
        # Guardar la animación en un archivo AVI
        Writer = writers['ffmpeg']
        writer = Writer(fps=velocidad, metadata=dict(artist='Me'), bitrate=1800)
        anim.save(nombre_archivo, writer=writer)
        
        plt.show()
    
    
    def main(self) -> None:
        """
        Función principal que ejecuta el TP de Atención al Público: Tp7
        """
        print(self.__str__())
        self.modelo.simular()
        print("-"*15)
        self.punto_1()
        print("-"*15)
        self.punto_2()
        print("-"*15)
        self.punto_3()
        print("-"*15)
        self.punto_4()
        print("-"*15)
        self.punto_5()
        print("-"*15)
        self.punto_6()
        print("-"*15)
        self.punto_7()
        print("-"*15)
        self.punto_8()
        print("-"*15)
        self.punto_9A()
        print("-"*15)
        # self.punto_9B(velocidad=10, nombre_archivo="animacion.avi")