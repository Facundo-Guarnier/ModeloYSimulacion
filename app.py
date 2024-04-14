class Calentador:
    def __init__(self, ) -> None:

print("\n++++++++++++ Punto 1 ++++++++++++")
m = 500            #! masa - g
c = 4.18            #! calor específico - J/g°C
dt1 = 70             #! cambio de temperatira - °C
tiempo = 300        #! tiempo - segundos
v = 220             #! voltaje - v

Q = m*c*dt1          #! energía - J

P = Q/tiempo        #! potencia - W

I = P/v             #! corriente - A

R = v/I             #! resistencia - Ω

print(f"Q = {Q} J")
print(f"P = {P} W")
print(f"I = {I} A") 
print(f"R = {R} Ω")

print("\n++++++++++++ Punto 2 ++++++++++++")

tiempo2 = 1          #! tiempo - segundos

Q = P*tiempo2        #! energía - J

dt2 = Q/(m*c)   #! cambio de temperatura - °C (convert to int)
print(f"El aumento de la temeratura en {tiempo2} segundos es de {dt2}° C")