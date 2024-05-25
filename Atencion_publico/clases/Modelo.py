import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from Atencion_publico.clases.Box import Box
from Atencion_publico.clases.Cliente import Cliente

class Modelo:
    """
    Representa un modelo de atención al publico.
    
    Attributes:
        - hora_apertura (int): Hora de apertura del local en segundos.
        - hora_cierre (int): Hora de cierre del local en segundos.
        - tiempo_max_espera (int): Tiempo máximo de espera en segundos de un cliente antes de irse sin ser atendido.
        - probabilidad_llegada (float): Probabilidad de que llegue un cliente en un segundo.
        - num_boxes (int): Número de boxes disponibles.
        - tiempo_simulacion (int): Duración de la simulación en segundos.
        - costo_box (int): Costo monetario de un box.
        - costo_cliente_perdido (int): Costo monetario de un cliente no atendido.
        - tiempo_atencion_media (int): Tiempo medio de atención en segundos.
        - tiempo_atencion_sd (int): Desviación estándar del tiempo de atención en segundos.
        
        - clientes_totales (int): Número total de clientes que ingresaron al local.
        - clientes_atendidos (int): Número de clientes que fueron atendidos.
        - clientes_no_atendidos (int): Número de clientes que no fueron atendidos.
        - costo_total (int): Costo monetario total de la operación.
        
        - boxes (list[Box]): Lista de boxes disponibles.
        - cola (list[Cliente]): Lista de clientes en espera.
        - clientes_historico (list[tuple[int, int, int]]): Tiempo transcurrido, cantidad de clientes en cola, cantidad de clientes en atención.
        
        - num_max_cliente_espera (int): Número máximo historico de clientes en espera.
        - tiempo_min_atencion_historico (int): Tiempo mínimo hitorico de atención en box.
        - tiempo_max_atencion_historico (int): Tiempo máximo historico de atención en box.
        - tiempo_min_espera_salón_historico (int): Tiempo mínimo historico de espera en salón.
        - tiempo_max_espera_salón_historico (int): Tiempo máximo historico de espera en salón.
    """
    def __init__(self, num_boxes:int = 3): # tiempo en segundos
        self.hora_apertura:int = 8 * 60 * 60
        self.hora_cierre:int = 12 * 60 * 60
        self.tiempo_max_espera:int = 30 * 60
        self.probabilidad_llegada:float = 1 / 144
        self.num_boxes:int = num_boxes
        self.tiempo_simulacion:int = self.hora_cierre - self.hora_apertura
        self.costo_box:int = 1000
        self.costo_cliente_perdido:int = 10000
        self.tiempo_atencion_media:int = 10 * 60
        self.tiempo_atencion_sd:int = 5 * 60
        
        self.clientes_totales:int = 0
        self.clientes_atendidos:int = 0
        self.clientes_no_atendidos:int = 0
        self.costo_total:int = 0
        
        self.boxes:list[Box] = [Box() for _ in range(self.num_boxes)]
        self.cola:list[Cliente] = []
        self.clientes_historico:list[tuple[int, int, int]] = []
        
        self.num_max_cliente_espera:int = 0
        self.tiempo_min_atencion_historico:int = 0 #! punto 4
        self.tiempo_max_atencion_historico:int = 0 #! punto 5
        self.tiempo_min_espera_salón_historico:int = 0 #! punto 6
        self.tiempo_max_espera_salón_historico:int = 0 #! punto 7
    
    
    def simular(self) -> None:
        """
        Ejecuta la simulación del modelo segundo a segundo.
        """
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
        #! Probabilidad de que llegue un cliente
        if random.random() < self.probabilidad_llegada:
            self.clientes_totales += 1
            cliente = Cliente(tiempo)
            self.cola.append(cliente)
    
    
    def procesar_atencion(self, tiempo: int) -> None:
        """
        Gestiona la atención de los clientes en los boxes.
        """
        for box in self.boxes:
            
            #! Verificar si el cliente actual terminó su atención 
            if box.ocupado and box.cliente_actual:
                if tiempo >= box.cliente_actual.tiempo_salida:
                    #! Liberar box
                    box.ocupado = False
                    box.cliente_actual = None
                    self.clientes_atendidos += 1
            
            #! Asignar un cliente a un box libre
            if not box.ocupado and self.cola:
                #! Asignar cliente a box
                cliente = self.cola.pop(0)
                box.ocupado = True
                box.cliente_actual = cliente
                
                #! Inicializar los tiempos
                cliente.tiempo_inicio_atencion = tiempo
                tiempo_atencion:int = max(np.ceil(np.random.normal(self.tiempo_atencion_media, self.tiempo_atencion_sd)), 0)     #! Max con 0 para evitar valores negativos
                cliente.tiempo_salida = tiempo + tiempo_atencion
                
                #! Actualizar tiempos históricos de atención
                self.tiempo_min_atencion_historico  = min(self.tiempo_min_atencion_historico, tiempo_atencion)
                self.tiempo_max_atencion_historico  = max(self.tiempo_max_atencion_historico, tiempo_atencion)
                
                #! Actualizar tiempos históricos de espera en salón
                self.tiempo_min_espera_salón_historico = min(self.tiempo_min_espera_salón_historico, tiempo - cliente.tiempo_llegada)
                self.tiempo_max_espera_salón_historico = max(self.tiempo_max_espera_salón_historico, tiempo - cliente.tiempo_llegada)
    
    
    def actualizar_cola(self, tiempo: int) -> None:
        """
        Elimina clientes de la cola si exceden el tiempo máximo de espera.
        
        Args:
            - tiempo (int): Tiempo actual en segundos.
        """
        self.cola = [cliente for cliente in self.cola if tiempo - cliente.tiempo_llegada <= self.tiempo_max_espera]
    
    
    def registrar_estado(self, tiempo: int) -> None:
        """
        Guarda el estado actual del sistema para su posterior análisis (gráfico). Lista de tuplas con la siguiente información:
        - tiempo : Tiempo transcurrido en segundos.
        - len(self.cola): Cantidad de clientes en cola.
        - sum(box.ocupado for box in self.boxes): Cantidad de clientes en atención.
        
        Args:
            - tiempo (int): Tiempo actual en segundos.
        """
        self.clientes_historico.append((tiempo, len(self.cola), sum(box.ocupado for box in self.boxes)))
    
    
    def calcular_estadisticas(self) -> None:
        """
        Calcula las estadísticas del modelo.
        """
        self.clientes_no_atendidos = self.clientes_totales - self.clientes_atendidos
        self.costo_total = self.num_boxes * self.costo_box + self.clientes_no_atendidos * self.costo_cliente_perdido
        for _, _, num_clientes_en_local in self.clientes_historico:
            self.num_max_cliente_espera = max(self.num_max_cliente_espera, num_clientes_en_local)