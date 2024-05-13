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
        self.modelo10 = modelo
    
    
    def punto_A(self) -> None:
        """
        Cuantos clientes ingresaron.
        """
        print(f"Punto A:\nClientes ingresados: {self.modelo10.clientes_totales}")
    
    
    def punto_B(self) -> None:
        """
        Cuantos clientes fueron atendidos.
        """
        print(f"Punto B:\nClientes atendidos: {self.modelo10.clientes_atendidos}")
    
    def punto_C(self) -> None:
        """
        Cuantos clientes no fueron atendidos.
        """
        print(f"Punto C:\nClientes no atendidos: {self.modelo10.clientes_no_atendidos}")
    
    
    def punto_D(self) -> None:
        """
        Costo total de la operación.
        """
        print(f"Punto D:\nCosto total de la operación: {self.modelo10.costo_total}")
    
    
    def punto_E(self) -> None:
        """
        Tiempo máximo de atención
        """
        print(f"Punto E:\nTiempo máximo de atención: {self.modelo10.tiempo_max_atencion / 60:.2f} minutos")    
    
    def punto_F(self) -> None:
        """
        Tiempo máximo de espera dentro del local.
        """
        print(f"Punto F:\nTiempo máximo de espera dentro del local: {self.modelo10.tiempo_max_espera_local / 60:.2f} minutos")
    
    
    def punto_G(self) -> None:
        """
        Graficar la distribución de personas en el local:
        - Tiempo T
        - Animación
        """
        tiempos, clientes_en_cola, clientes_en_atencion = zip(*self.modelo10.clientes_historico)
        fig, ax = plt.subplots()
        ax.plot(tiempos, clientes_en_cola, label="Clientes en Cola")
        ax.plot(tiempos, clientes_en_atencion, label="Clientes en Atención")
        ax.set_xlabel("Tiempo (segundos)")
        ax.set_ylabel("Número de Clientes")
        ax.legend()
        plt.show()
    
    
    def main(self) -> None:
        """
        Función principal que ejecuta el TP de Atención al Público: Tp7
        """
        
        self.modelo10.simular()
        self.punto_A()
        print("-"*15)
        self.punto_B()
        print("-"*15)
        self.punto_C()
        print("-"*15)
        self.punto_D()
        print("-"*15)
        self.punto_E()
        print("-"*15)
        self.punto_F()
        print("-"*15)
        self.punto_G()