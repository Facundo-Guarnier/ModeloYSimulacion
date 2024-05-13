
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
    
    def __init__(self) -> None:
        pass
    
    
    def punto_A(self) -> None:
        """
        Cuantos clientes ingresaron.
        """
        raise NotImplementedError("Punto A no implementado")
    
    
    def punto_B(self) -> None:
        """
        Cuantos clientes fueron atendidos.
        """
        raise NotImplementedError("Punto B no implementado")
    
    
    def punto_C(self) -> None:
        """
        Cuantos clientes no fueron atendidos.
        """
        raise NotImplementedError("Punto C no implementado")
    
    
    def punto_D(self) -> None:
        """
        Costo total de la operación.
        """
        raise NotImplementedError("Punto D no implementado")
    
    
    def punto_E(self) -> None:
        """
        Tiempo máximo de atención
        """
        raise NotImplementedError("Punto E no implementado")
    
    
    def punto_F(self) -> None:
        """
        Tiempo máximo de espera dentro del local.
        """
        raise NotImplementedError("Punto F no implementado")
    
    
    def punto_G(self) -> None:
        """
        Graficar la distribución de personas en el local:
        - Tiempo T
        - Animación
        """
        raise NotImplementedError("Punto G no implementado")