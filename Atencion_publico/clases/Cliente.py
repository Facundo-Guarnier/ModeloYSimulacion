class Cliente:
    """
    Representa un cliente en el sistema.
    """
    def __init__(self, tiempo_llegada:int):
        self.tiempo_llegada:int = tiempo_llegada
        self.tiempo_inicio_atencion:int = 0
        self.tiempo_salida:int = 0