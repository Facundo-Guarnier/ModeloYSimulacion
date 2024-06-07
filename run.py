
import os


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


def atencion_publico( tp8:bool = False):
    """
    Función principal que ejecuta el TP de Atención al Público: Tp7 y Tp8
    """
    from Atencion_publico.App import App
    from Atencion_publico.clases.Modelo import Modelo
    
    num_boxes = int(input("Ingrese la cantidad de boxes: "))
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
    try:
        while True:
            tp = int(input("Ingrese el TP a ejecutar (6, 7, 8, 9): "))
            
            if tp not in [6, 7, 8, 9]:
                raise ValueError("El TP debe ser 6, 7, 8 o 9")
            
            #T* Tp1 al Tp6
            if tp == 6:
                print("\n\n+" + "-"*38 + "+")
                print("+    Tp1 al Tp6: Calentador de Agua    +")
                print("+" + "-"*38 + "+\n")
                
                calentador_agua()
                
                if input("\nTp1 al Tp6 finalizados.\n¿Desea continuar con otro TP? (s/n): ") != "s":
                    break
            
            # T* Tp7
            if tp == 7:
                print("\n\n+" + "-"*32 + "+")
                print("+    Tp7: Atención al público    +")
                print("+    (Distribución uniforme)     +")
                print("+" + "-"*32 + "+\n")
                
                atencion_publico()
                
                if input("\nTp7 finalizado.\n¿Desea continuar con otro TP? (s/n): ") != "s":
                    break
            
            #T* Tp8
            if tp == 8:
                print("\n\n+" + "-"*32 + "+")
                print("+    Tp8: Atención al público    +")
                print("+    (Distribución normal)       +")
                print("+" + "-"*32 + "+\n")
                
                atencion_publico(tp8=True)
                
                if input("\nTp8 finalizado.\n¿Desea continuar con otro TP? (s/n): ") != "s":
                    break
                
            #T* Tp9
            if tp == 9:
                print("\n\n+" + "-"*23 + "+")
                print("+    Tp9: Particulas    +")
                print("+" + "-"*23 + "+\n")
                
                particulas()
                
                if input("\nTp9 finalizado.\n¿Desea continuar con otro TP? (s/n): ") != "s":
                    break
    
    except ValueError as e:
        print("\n\n+" + "-"*42 + "+")
        print("+    Error en la ejecución del programa    +")
        print("+" + "-"*42 + "+\n")
        print(e)
        input("\n\nPresione Enter para salir...")
    
    os._exit(0)