
def calentador_agua():
    """
    Función principal que ejecuta los TPs del Calentador de Agua: Tp1, Tp2, Tp3, Tp4, Tp5, Tp6
    """
    from Calentador_agua.clases.Liquido import Liquido
    from Calentador_agua.clases.Material import Material
    from Calentador_agua.clases.Recipiente import Recipiente
    from Calentador_agua.clases.Calentador import Calentador
    from Calentador_agua.App import App
    
    agua = Liquido(
            nombre="Agua",
            densidad=1, 
            calor_especifico=4.186,
    )
    print(agua)
    print("-"*15)
    
    telgopor = Material(
        nombre="Telgopor",
        conductividad_térmica=0.035,
    )
    print(telgopor)
    print("-"*15)
    
    cilindro = Recipiente(
        altura=6.36619, 
        diametro=10, 
        material=telgopor, 
        espesor_aislante=0.01, 
        liquido=agua
    )
    print(cilindro)
    print("-"*15)
    
    calentador = Calentador(
        temperatura_liquido_inicial=30,
        temperatura_liquido_final=100,
        temperatura_ambiente=30,
        tiempo_objetivo=300,
        recipiente=cilindro,
        tension=220,
    )
    calentador.tension
    print(calentador)
    
    print("+"*15)
    print("+"*15)
    
    a = App(
        liquido=agua,
        material=telgopor,
        recipiente=cilindro,
        calentador=calentador,
    )
    
    a.main()


def atencion_publico(num_boxes:int, tp8:bool = False):
    """
    Función principal que ejecuta el TP de Atención al Público: Tp7 y Tp8
    """
    from Atencion_publico.App import App
    from Atencion_publico.clases.Modelo import Modelo
    
    modelo = Modelo(
        num_boxes=num_boxes,
    )
    
    a = App(modelo=modelo)
    a.main(tp8=tp8)

def particulas():
    """
    Función principal que ejecuta el TP de Partículas: Tp9
    """
    from Particulas.App import App
    a = App()
    a.main()


if __name__ == '__main__':
    # print("Calentador de Agua")
    #T* Tp1 al Tp6
    # print("Tp1 al Tp6")
    # calentador_agua()
    # print("+"*15,"\n")
    
    
    # print("Atención al público")
    # num_boxes:int = int(input("Ingrese la cantidad de boxes: "))
    #T* Tp7
    # print("Tp7")
    # atencion_publico(num_boxes=num_boxes)
    # print("+"*15,"\n")
    
    
    #T* Tp8
    # print("Tp8")
    # atencion_publico(num_boxes=num_boxes, tp8=True)
    # print("+"*15,"\n")
    
    
    #T* Tp9
    print("Tp9")
    particulas()