class Cliente:
    """
    Representa un cliente en el sistema.
    
    Attributes:
        - tiempo_llegada (int): Tiempo en que el cliente llega al local.
        - tiempo_inicio_atencion (int): Tiempo en que el cliente comienza a ser atendido.
        - tiempo_salida (int): Tiempo en que el cliente abandona el local.
    """
    def __init__(self, tiempo_llegada:int):
        self.tiempo_llegada:int = tiempo_llegada
        self.tiempo_inicio_atencion:int = 0
        self.tiempo_salida:int = 0