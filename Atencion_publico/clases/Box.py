from Atencion_publico.clases.Cliente import Cliente

class Box:
    """
    Representa un box de atención.
    
    Attributes:
        - ocupado (bool): Indica si el box está ocupado.
        - cliente_actual (Cliente|None): Cliente actualmente atendido en el box.
    """
    def __init__(self):
        self.ocupado = False
        self.cliente_actual:Cliente|None = None 