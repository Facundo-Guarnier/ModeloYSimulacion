import pygame, random

class Particula:
    """
    Partícula que se mueve en una dirección aleatoria.
    
    Args:
        - x (int): Posición en x de la partícula.
        - y (int): Posición en y de la partícula.
        - lado (int): Tamaño de la partícula.
    
    Attributes:
        - x (int): Posición en x de la partícula.
        - y (int): Posición en y de la partícula.
        - lado (int): Tamaño de la partícula.
        - adhesion (bool): Indica si la partícula está adherida al conducto.
        - color (tuple[int, int, int]): Color de la partícula.
    """
    def __init__(self, *, x:int, y:int, lado:int) -> None:
        self.x = x
        self.y = y
        self.lado = lado
        self.adhesion = False
        self.color:tuple[int, int, int] = (139, 69, 19)
    
    
    def dibujar(self, pantalla:pygame.Surface) -> None:
        """
        Dibuja la partícula en la pantalla.
        
        Args:
            - pantalla (Surface): Pantalla de pygame.
        """
        pygame.draw.rect(
            surface=pantalla, 
            color=self.color, 
            rect=(self.x, self.y, self.lado, self.lado),
        )
    
    
    def mover(self) -> None:
        """
        Mueve la partícula en una dirección aleatoria.
        """
        movimiento = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])
        self.x += movimiento[0]
        self.y += movimiento[1]
    
    
    def colisiona_otra_particula(self, otra_particula:'Particula' ) -> bool:
        """
        Verifica si la partícula colisiona con otra partícula.
        
        Args:
            - otra_particula (Particula): Particula a comparar.
        
        Returns:
            - bool: True si colisiona con otra partícula, False en caso contrario.
        """
        return (
            self.x < otra_particula.x + otra_particula.lado and
            self.x + self.lado > otra_particula.x and
            self.y < otra_particula.y + otra_particula.lado and
            self.y + self.lado > otra_particula.y
        )