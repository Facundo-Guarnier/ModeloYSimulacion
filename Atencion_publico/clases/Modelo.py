import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from Atencion_publico.clases.Box import Box
from Atencion_publico.clases.Cliente import Cliente

class Modelo:
    """
    Representa un modelo de atención al publico.
    """
    def __init__(self, num_boxes:int = 3, tiempo_simulacion=4*60*60): # tiempo en segundos
        self.hora_apertura:int = 8 * 60 * 60
        self.hora_cierre:int = 12 * 60 * 60
        self.tiempo_max_espera:int = 30 * 60
        self.probabilidad_llegada:float = 1 / 14
        self.num_boxes:int = num_boxes
        self.tiempo_simulacion:int = tiempo_simulacion
        self.costo_box:int = 1000
        self.costo_cliente_perdido:int = 10000
        self.tiempo_atencion_media:int = 10 * 60
        self.tiempo_atencion_sd:int = 5 * 60

        self.clientes_totales:int = 0
        self.clientes_atendidos:int = 0
        self.clientes_no_atendidos:int = 0
        self.tiempo_max_atencion:int = 0
        self.tiempo_max_espera_local:int = 0
        self.costo_total:int = 0

        self.boxes:list[Box] = [Box() for _ in range(self.num_boxes)]
        self.cola:list[Cliente] = []
        self.clientes_historico:list[tuple[int, int, int]] = []

    def simular(self) -> None:
        """
        Ejecuta la simulación del modelo.
        """
        print("Simulando...")
        for tiempo in range(self.tiempo_simulacion):
            self.procesar_llegadas(tiempo)
            self.procesar_atencion(tiempo)
            self.actualizar_cola(tiempo)
            self.registrar_estado(tiempo)

        self.calcular_estadisticas()

    def procesar_llegadas(self, tiempo: int) -> None:
        """
        Gestiona la llegada de nuevos clientes.
        """
        if random.random() < self.probabilidad_llegada:
            self.clientes_totales += 1
            cliente = Cliente(tiempo)
            self.cola.append(cliente)

    def procesar_atencion(self, tiempo: int) -> None:
        """
        Gestiona la atención de los clientes en los boxes.
        """
        for box in self.boxes:
            if box.ocupado and box.cliente_actual:
                if tiempo >= box.cliente_actual.tiempo_salida:
                    box.ocupado = False
                    self.clientes_atendidos += 1
            if not box.ocupado and self.cola:
                cliente = self.cola.pop(0)
                box.ocupado = True
                box.cliente_actual = cliente
                cliente.tiempo_inicio_atencion = tiempo
                tiempo_atencion = np.ceil(np.random.normal(self.tiempo_atencion_media, self.tiempo_atencion_sd))
                cliente.tiempo_salida = tiempo + int(tiempo_atencion)
                self.tiempo_max_atencion = max(self.tiempo_max_atencion, tiempo_atencion)
    
    
    def actualizar_cola(self, tiempo: int) -> None:
        """
        Elimina clientes de la cola si exceden el tiempo máximo de espera.
        """
        self.cola = [cliente for cliente in self.cola if tiempo - cliente.tiempo_llegada <= self.tiempo_max_espera]
    
    
    def registrar_estado(self, tiempo: int) -> None:
        """
        Guarda el estado actual del sistema.
        """
        self.clientes_historico.append((tiempo, len(self.cola), sum(box.ocupado for box in self.boxes)))
    
    def calcular_estadisticas(self) -> None:
        """
        Calcula las estadísticas del modelo.
        """
        self.clientes_no_atendidos = self.clientes_totales - self.clientes_atendidos
        self.costo_total = self.num_boxes * self.costo_box + self.clientes_no_atendidos * self.costo_cliente_perdido
        for _, _, num_clientes_en_local in self.clientes_historico:
            self.tiempo_max_espera_local = max(self.tiempo_max_espera_local, num_clientes_en_local)