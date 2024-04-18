from clases.Calentador import Calentador
from clases.Liquido import Liquido
from clases.Material import Material
from clases.Recipiente import Recipiente


if __name__ == '__main__':
    
    agua = Liquido(
        nombre="Agua",
        densidad=1, 
        calor_especifico=4.186,
    )
    
    telgopor = Material(
        nombre="Telgopor",
        conductividad_térmica=0.035,
    )
    
    cilindro = Recipiente(
        altura=6.36619, 
        diametro=10, 
        material=telgopor, 
        espesor_aislante=0.01, 
        liquido=agua
    )
    
    calentador = Calentador(
        temperatura_liquido_inicial=30,
        temperatura_liquido_final=100,
        temperatura_ambiente=30,
        tiempo_objetivo=300,
        recipiente=cilindro,
        tension=220,
    )
    
    
    print(agua)
    print("-"*10)
    print(telgopor)
    print("-"*10)
    print(cilindro)
    print("-"*10)
    
    
    print(calentador.tp1_a())
    print("-"*10)
    print(calentador.tp1_b())
    print("-"*10)
    print(calentador.tp2())
    print("-"*10)
    print(calentador.tp3())
    print("-"*10)
    print(calentador.tp4())
    print("-"*10)