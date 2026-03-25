---
title: "Como analizar datos usando promedios"
author: Martín Aramayo.
subtitle: "📊👥🧮" # tres emojis que tengan que ver con el post, podes sacarlos de https://emojipedia.org/
tags: ["Matemática", "Estadistica", "Física", "Promedio"] # Por lo general contienen lo mismo que los temas
date: 2024-05-21 # poner la fecha de creación del post
math: true # si contiene ecuaciones poner true
# image: false # a definir en el futuro que tipo de imagenes poner, por el momento queda false
banner: "img/medir-a-medianas/moda-2.png"
---

Breve explicación intuitiva y visual de como funcionan: La media aritmética, la media geométrica, la media harmónica, la mediana y la moda (No en ese orden je).

<!--more-->

---

- **Dificultad:** ★★☆☆☆

- **Materiales:**
  - Este es teórico, no necesitas nada, va una calculadora, ponele.

- **Duración de preparación:** 30 min

- **Temas:** Matemática, Estadistica, Física, Promedio <!-- Los temas separados por comas. Por ej:  -->

---

NOTA: Este post es una traducción libre de [este artículo de Better explained](https://betterexplained.com/articles/how-to-analyze-data-using-the-average/). Tanto este artículo como el suyo [se encuentra bajo la misma licencia creative commons](http://creativecommons.org/licenses/by-nc-sa/3.0/us/).

---

Si tenés un montón de valores y tenés que tratar de analizarlos, entenderlos u obtener algún dato agregado de ellos, se suelen usar distintas técnicas. Ahora vamos a hablar de los distintos tipos de promedios, ventajas, desventajas, aplicaciones y como se calculan. Hay un poco de interpretación según cada aplicación para poder agarrarle la mano.

Ejemplo rápido: Si manejo un tramo a 30\\({ m \over s}\\) y regreso a 60\\({ m \over s}\\). ¿Cuál fue mi velocidad promedio?

Pista: No son 45\\({ m \over s}\\). Y agárrate de la silla TESORO, no importa la distancia entre el punto de inicio y el punto final. Más adelante volvemos a esto 😎.

$$
\begin{array}{c|c|c}
    \hline
    \begin{array}{c}
    \textbf {Nombre \\&} \\\
    \textbf {Significado}
    \end{array}
     &
    \begin{array}{c}
    \textbf {Formula \\&} \\\
    \textbf {Ejemplo}
    \end{array}
     &
    \textbf {Uso} \\\
    \hline
    \begin{array}{c}
    \text {Media} \\\
    \text {Aritmética} \\\
    \text {[Promedio]}
    \end{array}
     &
    \frac{\text {Suma}}{\text {Tamaño}}=\frac{a+b+c}{3}
     &
    \begin{array}{c}
    \text {Mayoría de los casos} \\\
    \text {``Promedio de} \\\
    \text {la muestra"}
    \end{array} \\\
    \hline
    \begin{array}{c}
    \text {Mediana} \\\
    \text {[Valor del medio]}
    \end{array}
     &
    \begin{array}{c}
    \text {El medio de una} \\\
    \text {lista ordenada} \\\
    \text {(Promediar si son 2)}
    \end{array}
     &
    \begin{array}{c}
    \text {Muestras con grandes} \\\
    \text {variaciones} \\\
    \text {(Casas, Ingresos)}
    \end{array} \\\
    \hline
    \begin{array}{c}
    \text {Moda} \\\
    \text {[Mas popular]}
    \end{array}
     &
    \text {Valor mas popular}
     &
    \begin{array}{c}
    \text {Sin compromisos} \\\
    \text {(Gana uno)}
    \end{array} \\\
    \hline
    \begin{array}{c}
    \text {Media} \\\
    \text {geométrica} \\\
    \text {[Factor promedio]}
    \end{array}
     &
    \sqrt[3]{a b c}
     &
    \begin{array}{c}
    \text {Inversiones,} \\\
    \text {Crecimiento,} \\\
    \text {Área, Volumen}
    \end{array} \\\
    \hline
    \begin{array}{c}
    \text {Media} \\\
    \text {Armónica} \\\
    \text {[Tasa promedio]}
    \end{array}
     &
    {3 \over {\frac{1}{a}+\frac{1}{b}+\frac{1}{c}}}
     &
    \begin{array}{c}
    \text {Velocidad,} \\\
    \text {producción, costo}
    \end{array}\\\
    \hline
\end{array}
$$

<!-- $$S -->

## Pero pará flaco, ¿Qué significa calcular un promedio?

Para muchos de nosotros es "El número ese que está en el medio" o un número que está "balanceado". Esto no siempre aplica en todos los casos que vamos a mirar. Seguime con este punto de vista, el promedio es tal que:

**Si reemplazo a cada valor de mi muestra por su promedio en una operación, obtengo el mismo resultado.**

Es la respuesta a la pregunta: Si puedo agarrar a los elementos de mi muestra y reemplazarlos a cada uno por un valor "promedio", ¿Cuál sería?

Un objetivo del promedio es apoyarnos para entender a la muestra a través de tener un valor representativo. Esto es necesario porque si tenemos miles o millones de muestras, tratar de imaginarnos sus propiedades es muy difícil con solo mirarlas. Un detalle importante, el cálculo dependerá de como interactúan estos valores entre sí. Veamos la media aritmética.

## La media aritmética

Este es el tipo de promedio más común:

$$
\text{Media Aritmética} =
{
    \text{Suma de todos los elementos}
    \over
    \text{La cantidad de elementos}
}
$$

![](/img/medir-a-medianas/mean_arithmetic.png)

Supongamos que pesas 150 kg, y estás en un ascensor con una persona de 100 kg y con un animal marino de 350 kg (Sí, medio grande el ascensor, pero supongamos). ¿Cuál es el peso promedio?

En este contexto, la pregunta sería "Si reemplazo a este grupo por 3 personas idénticas y queremos que la carga sobre el ascensor sea la misma. ¿Cuánto deberían pesar cada una de estas personas?"

En este caso, si intercambiamos por tres personas que pesan 200 kg cada una \\(\left( (150 + 100 + 350) \over 3 \right)\\), engañaremos a este inocente y enorme ascensor.

Ventajas:

- Funciona bien para cantidades en las que la suma es una operación que tiene un sentido.
- Fácil de calcular: Solo se suma y se divide.
- Es intuitivo: Es un número "intermedio", agregar elementos grandes aumenta el valor del promedio. Agregar elementos pequeños nos arroja un promedio más bajo.

Desventajas:

- El promedio se puede mover con valores atípicos. Ejemplo, \\([1, 1, 1, 1]\\) tiene un promedio 1, y \\([1, 1, 1, 100]\\) vale 25.75.
- Si la muestra es demasiado variada, los resultados pueden ser extraños. Por ejemplo: El promedio de \\([100, 200,-300]\\) es 0.

## La Mediana

La mediana es el elemento en el medio. Uno se podría preguntar, ¿Y esto no es lo mismo que la media aritmética? No mi TERMOTANQUE DE ELEGANCIA, expliquemos la diferencia con el siguiente ejemplo:

$$[1, 2, 3, 4, 100]$$

Si ordenamos los números de menor a mayor, el valor en el medio de la lista es 3. Y la media aritmética es 22. Ojo con estos valores que son bien diferentes. La media aritmética no es tan buena representando como están distribuidos los elementos. Si saco elementos al azar es más probable que tome un valor más cercano a 3 que cercano a 22. Fijate que la media aritmética me quedó más arriba porque el valor atípico 100 me la corrió.

La mediana resuelve este problema tomando el número en el medio de una lista ordenada. Si hay dos valores en el medio (esto pasa cuanto la muestra tiene un número par de elementos), alcanza con tomar la media aritmética de los dos valores en el medio. Y tuki.

Por completitud veamos un caso par:

$$[1, 2, 3, 4]$$

La mediana en este caso es 2.5.

![](/img/medir-a-medianas/mediana.png)

Ventajas:

- Maneja bien los valores atípicos - Suele ser la mejor representación de un grupo.
- Divide la muestra en 2 grupos, cada uno con la misma cantidad de elementos.

Desventajas:

- Puede ser más difícil de calcular: Necesitas ordenar la lista primero.
- Es un valor menos reconocido y considerado. Por ejemplo, cuando uno habla de la "mediana" si uno no conoce la diferencia, puede creer que estamos hablando del "promedio" más común, la media aritmética.

Hay expresiones similares a "La mitad de los conductores se encuentran por debajo del promedio". Sin embargo, una expresión que contemple esta definición sería: "La mitad de los conductores se encuentran por debajo de la mediana".

Algunas cantidades como el precio de las viviendas y el nivel de ingresos de un país se deben reportar en términos de la mediana. Esto es porque queremos conocer cuanto ganan los que están en le medio de la distribución. Algo que puede pasar es que de un año a otro uno de los ciudadanos incrementa su patrimonio en varios billones de dólares. Si miramos la media aritmética nos podríamos creer que los ingresos de toda la población subieron porque me daría más alta. Esto no necesariamente así. Alcanza con subir mucho un valor para correr la media aritmética, esto no alcanza para subir la mediana. Vemos que en estos casos, no nos interesa "sumar" el valor de una casa o los ingresos de los habitantes de un país. Solo queremos un valor en el medio de todos los demás valores para orientarnos.

Nuevamente, el tipo de promedio que usamos depende de como usamos la muestra, depende de nuestro objetivo. Es 100% circunstancial. Circunstancial mi FORTUITA SERENDIPIA.

## Moda

Esta es simple, es el valor que más se repite. Similar a cuando se realiza una votación. En algunos casos, este valor es más representativo que realizar una cuenta. Ejemplos: en elecciones, en determinar la popularidad de distintos músicos, libro más leído, streamer con más visitas, influencer con más seguidores, etc. Ya vas viendo la relación con la frase "está a la moda" o "está de moda".

Supongamos que querés organizar una fiesta y necesitas elegir una fecha. La "mejor opción" será la que satisfaga a más personas. Un promedio en este caso no tendría sentido. (Si alguien quiere salir un viernes y otra persona quiere salir un domingo, la mejor opción no sería el sábado.)

Ahora podés ver que la moda es un buen método para elegir "al favorito". Aunque se pueda modelar con números preferencias a películas o colores. A la hora de elegir el más popular, nos sigue conviniendo tomar una moda y no un promedio.

Para ilustrar una última vez esta diferencia veamos este ejemplo:
$$[1, 1, 2, 10]$$

- El promedio es 7.5
- La mediana es 1.5
- La moda es 1

Imagínate si todos votaban por su número natural favorito y en lugar de tomar la moda tomamos otra cosa. Ni el promedio ni la mediana está entre los elementos que se votaron. Un disparate, cuchame una cosa.

Ventajas:

- Funciona bien para situaciones de voto excluyente. En estos casos es un resultado u otro. No pueden tomarse valores en el medio o fuera de la muestra.
- Dar una elección que la mayoría querría. Las otras cuentas puede dar una opción que nadie quiere o que simplemente no existe por el tipo de dato que es.
- Fácil de entender

![](/img/medir-a-medianas/moda.png)

Desventajas:

- Requiere esfuerzo (hace falta contar las repeticiones de cada valor).
- No te perdona una, el que gana se lleva todo.

El término "moda" no es tan común cuando vemos muestras en noticieros o diarios. Pero en el mundo de la estadística es bien conocido. Todo buen software de estadistica te lo puede tirar.

## Media geométrica

Como ya te vine insistiendo, el "elemento promedio" depende del uso de la muestra. Cuando los elementos se suman juntos, una media aritmética tiene sentido. Hay algunos casos donde esto no es suficiente. Cuando estamos en el mundo de las inversiones, áreas y volúmenes, los factores no se suman, se multiplican.

Intentemos un ejemplo. Dados dos portafolios de inversión, en el cual mostramos 4 años de resultados. ¿Cuál de los dos tiene mejores rendimientos medios anuales?

- Portfolio A:
  - \\(+10\\%, -10\\%, +10\\%, -10\\%\\)
- Portfolio B:
  - \\(+30\\%, -30\\%, +30\\%, -30\\%\\)

Se ven similares. Una media aritmética nos indica que ambas opciones son comparables, dan 0% de interés. No hay pérdidas ni ganancias. Uno podría pensar que el portafolio B es mejor porque parece tener más ingresos en los años donde si logra dar retorno.
Ojo con eso mi RELIQUIA SAGRADA, esto **NO** es así, ambos portafolios son muy diferentes.

Si hiciéramos las cuentas de ingresos de esa manera nos fundiríamos muy rápido. Las tasas de retornos de inversión se multiplican, no se suman. No debemos tomar inocentemente la media aritmética.

La tasa media de ingreso/egresos, son:

- Portafolio A:
  - Retornos: \\(1.1 \times 0.9 \times 1.1 \times 0.9 = 0.98\\) (2% de pérdidas)

  - Promedio año a año: \\( \sqrt[4]{0.98} \\) = 0.5% de pérdidas anuales.

- Portafolio B:
  - Retornos: \\(1.3 \times 0.7 \times 1.3 \times 0.7 = 0.83\\) (17% de pérdidas)

  - Promedio año a año: \\( \sqrt[4]{0.83} \\) = 4.6% de pérdidas anuales.

_Nota: Fijate como son los factores que multiplicamos. Son 1 + el porcentaje expresado como decimal y con su signo. Así es el mundo de las finanzas, mi LUZ DE VIDA. Esto es así porque estos cambios son respecto al valor con el que arrancaste, lo que los bros le llaman "Capital inicial"._

Un -2% Vs. -17% es una diferencia importante. Ambos portafolios dan pérdidas, pero B es claramente el peor.

Otra lección de este ejemplo es que no tiene sentido sumar y dividir retornos de inversión. Esto es, porque son crecimientos exponenciales y no se pueden operar entre sí de esa manera.

![](/img/medir-a-medianas/mean_geometric.png)

---

## Media armónica

La media armónica es más difícil de visualizar, pero sí se puede entender de donde viene y como se aplica. Primero vamos a aclarar que la palabra armónica viene de que los números \\( \frac{1}{2}, \frac{1}{3}, \frac{1}{4}, \dots \\), es decir, los recíprocos de los números naturales. Está relacionado con el mundo musical. Estos números están relacionados con la secuencia de armónicos o tonos musicales cuya frecuencia es un entero múltiple de la frecuencia fundamental de un instrumento. Aparte de que las secuencias armónicas aparecen en problemas donde también hay medias armónicas como el [problema del apilamiento de bloques](https://www.wikiwand.com/es/Problema_del_apilado_de_bloques).

En el mundo de la física, la resistencia equivalente a unas resistencias eléctricas en paralelo se calcula mediante una media armónica. Por otro lado, el cálculo de la llamada masa reducida también utiliza una media armónica. La masa reducida te permite, junto con el centro de masa, analizar dos masas como una sola en la dinámica newtoniana. Esto permite resolver el famoso _problema de los dos cuerpos_ (el de tres no tiene solución je). Faaaa altos ejemplos te tiré TROTAMUNDOS ELEVADO.

Volviendo al tema principal, la media armónica nos ayuda a calcular tasas promedio cuando hay elementos operando como un conjunto sobre una misma entrada. Vamos a un par de ejemplos para que no sea tan mística la cosa:

Si yo tengo una velocidad de 30\\({ m \over s}\\), significa que obtengo un resultado (avanzar 30 metros) por cada entrada (avanzar 1 segundo). Como este es un proceso de entrada y salida, es en esos términos que se debe calcular la tasa promedio cuando tengo elementos trabajando en conjunto. Esto es:

$$
\text{Tasa media del sistema } =
{\text{Resultado total} \over \text{Entrada total}}
$$

![](/img/medir-a-medianas/mean_harmonicc.png)

Si colocamos a un elemento con tasa representativa \\(X\\) y otro con tasa \\(Y\\). Cada uno realizando la misma cantidad de trabajo. ¿Cuál es la tasa promedio? Supongamos que \\(X\\) es 30\\({ m \over s}\\) y \\(Y\\) es 60\\({ m \over s}\\). Si los ponemos a hacer tareas similares (recorrer 1 metro) el razonamiento es:

- \\(X\\) tarda un tiempo \\(\frac{1}{X}\\) (1 metro = \\(\frac{1}{30}\\) segundos)
- \\(Y\\) tarda un tiempo \\(\frac{1}{Y}\\) (1 metro = \\(\frac{1}{60}\\) segundos)

Si combinamos las entradas y las salidas obtenemos:

- Salidas totales: 2 metros (\\(X\\) e \\(Y\\) contribuyen "1" metro)
- Entradas totales: \\(\frac{1}{X} + \frac{1}{Y}\\) (cada uno toma una cantidad de tiempo diferente; esto es parecido a una carrera de relevo)

La tasa media de entrada/salida, son:

$$
\frac{2}{\frac{1}{X}+\frac{1}{Y}}
$$

Si tuviésemos 3 elementos en esta mezcla \\(X, Y\\) y \\(Z\\) la tasa media sería:

$$
\frac{3}{\frac{1}{X}+\frac{1}{Y}+\frac{1}{Z}}
$$

Está bueno tener este atajo en vez de hacer álgebra cada vez que tengamos un problema así. Ojo que solo aplica si los dos tramos son iguales. Si los dos tramos son distintos, AGARRATE que la cuenta es distinta. Pero así como viene es cortito y al pie, inclusive si te meto 5 elementos se puede calcular tranqui.

Volviendo al ejemplo, si fuimos a 30\\({ m \over s}\\) y volvimos la MISMA distancia a 60\\({ m \over s}\\). Para encontrar la velocidad media simplemente usamos esta fórmula.

Uno podría preguntarse si esta velocidad media depende de cuanta distancia recorremos. Lo cierto es que no, la magia viene de que cada velocidad es fija cada tramo. No importa que tan larga sea la ruta, \\(X\\) e \\(Y\\) dan la misma salida. Esto es, si avanzamos \\(R\\) metros a la velocidad \\(X\\) y otros \\(R\\) metros a la velocidad \\(Y\\), la velocidad es la misma que cuando avanzamos 1 metro a velocidad \\(X\\) y 1 metro a la velocidad \\(Y\\). Nuevamente, OJO que si las velocidades varía de forma uniforme o de cualquier otra forma cambia la cosa. El resultado que estabas esperando es:

$$
\frac{2 R}{\frac{R}{30}+\frac{R}{60}}=\frac{2}{\frac{1}{30}+\frac{1}{60}}=40
$$

Tiene sentido que la velocidad media tienda a la más lenta (es más cercana a 30 que a 60). Después de todo, estamos el doble del tiempo viajando por el tramo a velocidad 30 que viajando por el tramo a velocidad 60. Si el destino está a 60 metros, son 2 horas de ida y 1 hora de vuelta.

La media armónica sirve para toda actividad donde haya cargas iguales y distintas tasas de "productividad". En procesos de fabricación en serie la cuenta es exactamente la misma. Múltiples procesos pasan por la misma materia prima. Algunos tienen tasas diferentes de procesamiento. La media armónica nos indica cuál es la tasa media.

Cabe destacar que siempre la media armónica es más baja que cada uno de los elementos que se consideran. Siempre el resultado se acerca al elemento más pequeño. Es por esto que en la manufactura y otros procesos en serie se habla de que el proceso más lento es el "cuello de botella", porque termina tirando abajo la tasa media de todo el sistema.

Detalle: Recordemos que el promedio es un elemento para reemplazarlos a todos. En nuestro ejemplo tenemos dos etapas de distintas velocidades y es importante recordar que se debe reemplazar cada "etapa" con una que rinda la tasa media.

Ejemplos:

- Transmisión de datos: Necesitamos enviar datos entre un cliente y un servidor. El cliente envía datos a 10 \\({gb \over \\$}\\), y el servidor recibe a 20 \\({gb \over \\$}\\). ¿Cuál es el costo promedio? Bien, la media es \\(2 \over {(\frac{1}{10} + \frac{1}{20})}\\) = 13.3 \\({gb \over \\$}\\) por cada parte. Esto es, podemos intercambiar el cliente y el servidor con dos máquinas que tienen un costo de 13.3 \\({gb \over \\$}\\). Porque los datos son enviados y recibidos (cada parte haciendo "la mitad del trabajo"), nuestra tasa final es \\({13.3 \over 2 }\\) = 6.65 \\({gb \over \\$}\\).

- Productividad de maquinaria: Para una máquina que prepara y termina partes. Durante la preparación corre a 25 \\({productos \over hora}\\). Al terminar, corre 10 \\({productos \over hora}\\). ¿Cuál es la tasa de todo el sistema? En este caso \\({2 \over {(\frac{1}{25} + \frac{1}{10})}}\\) = 14.28 \\({productos \over hora}\\) para cada etapa. Esto es, podemos replicar los mismos tiempos de producción, reemplazando el sistema por dos etapas corriendo a 14.28 \\({productos \over hora}\\). Como cada producto pasa por las dos etapas, la máquina completa \\(\frac{14.28}{2}\\) = 7.14 \\({productos \over hora}\\).

- Comprar acciones: Supongamos que compramos \\(\text{\textdollar} 1000\\) en un tipo de acción cada mes, lo compras sin importar el precio que tengan en ese mes. Si pagas \\( 25 {\text{\textdollar} \over accion}\\) en junio, \\( 30 {\text{\textdollar} \over acción}\\) en Febrero, y \\( 35 {\text{\textdollar} \over acción}\\) en marzo. ¿Cuál fue el precio promedio? Esto es \\(3 \over {(\frac{1}{25} + \frac{1}{30} + \frac{1}{35})}\\) = \\(\text{\textdollar} 29.43\\) (Esto ocurre porque se compraron más acciones a un precio más bajo y menos al precio más caro, porque el precio que pagaste es el mismo \\(\text{\textdollar} 1000\\)). Ahora ya gastaste \\(\text{\textdollar} 1000\\) y tenés \\({\text{\textdollar} 10003000 \over 29.43} = 101.94 \\) acciones. La carga de trabajo en este caso es un poco más abstracta - la entrada es la cantidad de acciones y la salida es el precio de esas acciones. Algunos meses usamos más dinero para comprar cada acción que en otros, y en este caso una tasa alta es algo malo.

Nuevamente, la media armónica ayuda a entender como diferentes tasas trabajan en conjunto hacia un resultado.

La media armónica es un poco engañosa. Ahí te va un ejemplo similar, pero en el que la media armónica no se usa y si se usa el promedio: si se tienen máquinas separadas e independientes que corren a 10 \\({partes \over hora}\\) y 20 \\({partes \over hora}\\), entonces su promedio es en realidad 15 \\({partes \over hora}\\). Esto es porque cada máquina es independiente y estas "sumando" directamente sus capacidades, trabajan en paralelo, no una con la salida de la otra, no están "en serie" como en el ejemplo donde se usa la media aritmética.

A veces es una buena idea asegurarse que la matemática esté funcionando correctamente. En el ejemplo de las máquinas "en serie", si el sistema produce a 7.14 \\({partes \over hora}\\) ¿Cuánto le tomaría producir 7.14 productos? Se supone que una hora. Bueno, revisemos si mirando cada etapa, esto es así:

- Preparación: \\({7.14 \over 25}\\) = 0.29 hora
- Finalización: \\({7.14 \over 10}\\) = 0.71 hora

Y si sumamos lo que tarda cada etapa, 0.29 + 0.71 = 1, los números cierran: toman una hora hacer 7.14 productos.

Fijate TITANICA DEIDAD, ante la duda, es buena idea probar un par de ejemplos para estar seguro. Revisa que tu tasa media sea realmente lo que estás buscando.

### Recomendado para aprender más

- [Un poco de media aritmética de fonemato](https://www.matematicasbachiller.com/libros/estadistica-descriptiva/tema-2-distribuciones-unidimensionales/202-media-aritmetica)
- [Un poco más sobre media armónica por fonemato](https://www.matematicasbachiller.com/libros/estadistica-descriptiva/tema-2-distribuciones-unidimensionales/204-media-armonica)
- [Todo el blog de Better explained, para más posts como este, pero en inglés](https://betterexplained.com/)
