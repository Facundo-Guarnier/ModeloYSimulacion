from Atencion_publico.clases.Cliente import Cliente


class Box:
    """
    Representa un box de atención.
    """
    def __init__(self):
        self.ocupado = False
        self.cliente_actual:Cliente|None = None 