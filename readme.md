# Practica de la materia "Modelo y Simulacion" (2024)
Universidad de Mendoza, 5° año

## Consignas
### Tp1
Hola queridos alumnos y alumnas,

El día jueves 21 de marzo de 2024 tuvimos nuestro primer encuentro presencial en la Universidad de Mendoza.
Conversarmos acerca de los Modelos y la Simulación Estocástica, y de las técnicas que veremos para visualizar la performance de Sistemas Físicos, Mecánicos y Económicos a lo largo de este Curso.

Damos, entonces, por iniciadas las Actividades Teóricas y Prácticas de esta parte de la Materia.

Nuestro primer Trabajo Práctico, T.P. 1, consiste en que cada uno de Ustedes establezca los parámetros requeridos para simular un calentador de agua eléctrico, de acuerdo a sus preferencias. Deberán decidir:

Material (aislante) a emplear. Recuerden que,en particular para este diseño deben evitar la pérdida de calor.
Forma y capacidad del recipiente. Cúbica, cilíndrica, esférica, etc. Yo les sugiero entre 500 cc y 2.000 cc.
Propósito del calentador: calentar, hervir, cocinar, agua para el mate, etc.
Fluido a calentar. Agua, aceite, miel, alcohol, etc.
Tiempo en el que se desea alcanzar esa temperatura. Por lo general entre 100 y 10.000 segundos.
Tensión de alimentacion del dispositivo. 12 Volts, 220 Volts, otras.
Para ese diseño, qué valor de Resistencia Eléctrica debemos emplear?
Cuál será la temperatura inicial del fluido al conectarlo al calentador?
Cuál será la temperatura ambiente al iniciar el proceso?
Calcular el aumento de temperatura del fluido luego de 1 segundo de conectar la alimentación, suponiendo que no existe pérdida de calor.
Espero que me envíen sus avances antes del próximo encuentro presencial, que tendrá lugar el día 4 de abril de 2024 a las 13.30 en el Aula H. De todas maneras trabajaremos sobre todos estos temas y responderemos a las dudas que puedan tener a lo largo de la clase. Pero intenten avanzar en todo lo que puedan.

Les hago llegar un cordial saludo!

---
### Tp2, 3 y 4
Actividades Semana del 8 de abril
Estimados Alumnos,

A lo largo de las dos primeras semanas de trabajo, desarrollamos los TP 1 y 2.

Ellos consistieron en establecer condiciones de diseño de nuestros dispositivos para la simulación de calentadores de fluídos y realizar la curva de calentamiento de nuestros dispositivos, sin tener en cuenta las pérdidas de calor en el tiempo.

En esta tercera semana de actividades trabajaremos sobre los TP 3 y TP 4.

TP 3: Calcular la pérdida de calor de nuestro dispositivo, según las especificaciones de diseño. A modo de referencia, les comenté que un dispositivo de telgopor, de 1 litro de capacidad, y de espesor 1 mm, suele presentar pérdidas aproximadas de 2,1 Watts/grado Kelvin. Ello se calcula con la fórmula que vimos la clase pasada: 

Calor perdido en Watts/grado Kelvin=CCT W/m . grado Kelvin . Sup/Esp/m.

Siendo CCT: Coeficiente de Conductividad Térmica
Sup: Superficie total del dispositivo.
Esp: Espesor de las paredes del dispositivo
Unidades en metros y grados Kelvin.

TP 4: Graficar la temperatura del fluido dentro del calentador sin pérdidas y con pérdidas para cada tick de tiempo, hasta llegar al tiempo deseado para que el dispositivo cumpla su tarea.

Para realizar el gráfico con pérdidas, se debe considerar los vatios efectivos entregados al fuido restando al calor producido por la resistencia, el calor perdido por las paredes del recipiente. Con este calor efectivo se calcula la variación de temperatura del fluido para cada tick de tiempo.

Pueden enviarme los TP juntos o por separado, para que vayamos revisando sus valores.

En el próximo encuentro presencial trabajaremos sobre estos dos prácticos 3 y 4.

Saludos cordiales!

---
### Tp5 y 6
Actividades Semana del 22 de abril
Estimados Alumnos,

En esta cuarta semana de actividades trabajaremos sobre los TP 5 y TP 6.

TP 5: Generar familias de curvas con distribuciones normales y uniformes de parámetros iniciales:

5.A Distribución uniforme de 5 valores próximos de resistencias.
5.B Distribución normal de 5 temperaturas iniciales del agua. Media 10, desvío standard=5
5.C Distribución uniforme de 8 temperaturas iniciales del ambiente, entre -20 y 50 grados.
5.D Distribución normal de 5 valores de tension de alimentación Media 12 SD:4 o Media 220, SD 40.
5.E Simulaciones que contengan todas las familias de curvas previas.

TP 6: Simulación de un fenómeno estocástico que tiene una probabilidad de ocurrencia de 1/300 en cada tick de tiempo. Con variables aleatorias: si el fenómeno tiene lugar, ocurre un descenso de X grados, durante Y segundos. Variación máxima 50 grados en descenso. Rehacer el gráfico de temperaturas del TP 4.

En el próximo encuentro presencial, del 9 de mayo trabajaremos sobre estos dos prácticos 5 y 6.

Saludos cordiales!


---
### Tp 7
Actividades Semana del 9 de Mayo
Estimados Alumnos,

Nuestro próximo encuentro presencial tendrá lugar el 30 de Mayo, en el lugar y horario habitual.

En esta semanas de actividades trabajaremos sobre el TP 7.

TP 7: Modelo y Simulación de un Sistema de Atención al Público

Introducción.
Estamos presenciando un aumento de la competencia entre los diversos prestadores de servicios, que intentan captar más clientes y lograr mayor participación de mercado, manteniendo los clientes actuales, sin perderlos, con los perjuicios que ello ocasiona.

Por ello, este modelo tiende a demostrar cuál es la mejor alternativa de habilitación de boxes de atención, para lograr mayor cantidad de personas atendidas, en el menor tiempo posible.

El modelo es aplicable a cajas de supermercados, a bancos, locales de comida y, en general, en todos los centros de prestación en donde los clientes se ubican en colas que pueden derivar en pérdidas importante de tiempo. Como se dice habitualmente "time is money". Muchas veces las empresas pierden de vista el valor estratégico de la pronta y correcta atención de los clientes.
Un mal diseño de este servicio puede derivar en la pérdida de operaciones y en la lisa y llana pérdida del cliente, con todas las operaciones potenciales que no se realizarán nunca con estas personas.

Descripción.
Se trata de un local de servicios que puede contar con 1 a 10 boxes de atención de clientes,.
Al momento de iniciar la simulación se elige este parámetro.
Luego, la simulación responde a las siguientes reglas e hipótesis:
1) El local abre de 8 a 12 horas.
2) El cliente que ingresa es atendido en la zona de atención o pasa a una cola.
3) Los clientes que están en cola o siendo atendidos pueden permanecer luego de la hora de cierre.
4) Los clientes que no están siendo atendidos abandonarán el local a los 30 minutos.
5) En cada segundo que transcurre, desde la apertura del local, la probabilidad de que ingrese un cliente es p=1/144.
6) La cantidad de boxes activos se establece antes de correr la simulación.
7) El tiempo de atención en cada box responde a una distribución normal, con media=10 minutos y desvio estándar=5 minutos.
8) Mantener el box abierto durante toda la mañana cuesta $1000.
9) Cada cliente que se va sin ser atendido representa una pérdida de $10.000.
10) Todo dato requerido para diseñar y programar la simulación puede ser asumido o especificado adicionalmente por cada uno de Ustedes.

Resultados.
Al final de cada simulación, deberemos responder a los siguientes interrogantes:
1) Cuántos clientes ingresaron al local?
2) Cuántos clientes fueron atendidos?
3) Cuántos clientes no fueron atendidos? Es decir abandonaron el local por demoras.
4) Tiempo mínimo de atención en box.
5) Tiempo máximo de atención en box.
6) Tiempo mínimo de espera en salón.
7) Tiempo máximo de espera en salón.
8) Costo de la operación: costo del box+costo por pérdida de clientes.
9) Presentación gráfica animada de cada proceso simulado, con diversas velocidades. Archivo AVI.

Les hago llegar un cordial saludo!

---
### Tp8 y 9
Actividades Semana del 5 de Junio
Estimados Alumnos,

Nuestro próximo encuentro presencial tendrá lugar el 5 de Junio, en el lugar y horario habitual.
En estas semanas trabajaremos sobre los TP 8 y TP 9.

TP 8: Modelo y Simulación de un Sistema de Atención al Público. Distribución Normal de Afluencia.

Consiste en modificar el TP. 7 de modo que la afluencia del público responda a una distribución normal, con media 10 de la mañana, y desvío estándar de 2 horas. Despreciando las colas izquierda y derecha de la distribución normal por debajo de las 8 horas y por encima de las 12 horas de la mañana.

La esperanza matemática continúa siendo de 100 personas en el transcurso de la mañana.

Realizar los mismos informes y animaciones que para el TP 7 y comparar resultados de TP 7 y TP 8.

TP 9. Modelos Estocásticos de Crecimiento por Agregación en Confinamiento.

Estos modelos se utilizan para estudiar el depósito de partículas en conductos de diferentes formas y secciones. Se trabaja en el plano, simulando movimiento aleatorio de partículas que se adhieren a las paredes del conducto, o a otras partículas que ya se han depositado previamente.
La simulación a desarrollar debe:
1) Solicitar forma de la sección y dimensiones del conducto. Las formas pueden ser circulares, cuadradas o rectangulares. Y sus dimensiones deben estar comprendidas entre 1 y 1000 mm.
2) Las partículas serán de forma cuadrada y se establecerán sus dimensiones entre 1 y 10 mm de lado.
3) Las partículas se generan en el centro del conducto y están dotadas de movimiento aleatorio, hacia arriba, abajo, izquierda y derecha.
4) Cuando se encuentran suficientemente próximas, con cierta tolerancia, a las paredes del conducto, deben permanecer adheridas.
5) Cuando se encuentran suficientemente próximas, con cierta tolerancia, a otras partículas, previamente adheridas al conducto, también deben permanecer adheridas.
6) La simulación se detiene cuando el crecimiento de las partículas alcanza una cierta distancia al centro, establecida previamente.

Se debe animar la simulación, con diversas escalas de tiempo.

Los espero el jueves!
Saludos cordiales!
Prof. Mario Molina