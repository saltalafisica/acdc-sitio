---
title: "Propagación de errores: Primeros pasos"
author: Martín Aramayo
subtitle: "⚖️🌡️⏱️"
tags:
  ["Distancias", "Mediciones", "Matemática", "Física", "Propagación de errores"]
date: 2023-04-14
math: true # si contiene ecuaciones poner true
image: false # a definir en el futuro que tipo de imagenes poner, por el momento queda false
# hidden: true
# show: false
banner: "img/incerteza/definicion.png"
---

Una breve explicación sobre propagación de errores, como funciona, como calcularlos a mano y qué herramientas modernas usar para obtenerlos.

<!--more-->

---

- **Dificultad:** ★★★★☆

- **Materiales:**
  - Papel y lapiz

- **Duración de preparación:** 30 min

- **Temas:** Distancias, Mediciones, Matemática, Física, Propagación de errores.

---

<!-- En la teoria de errores o incertezas de medida se formaliza la obtencion de mediciones indirectas a partir de mediciones directas.  -->

### ¿Por qué tanta matemática y tanta teoría para esto?

Para que lo que uno mida sea serio y comparable con las mediciones de otras personas, se debe reportar no solo la cantidad que se midió, sino que tan confiable es. Qué margen de error presupongo. Estas fuentes de error o incertezas en la medición provienen del aparato o herramienta que uso para medir. Pero también hay incertezas de redondeo al realizar cuentas manuales, con computadora o algún otro instrumento. Estas incertezas pueden tener muchos orígenes y tienen como resultado que lo que observe no siempre sea certero. Hay mediciones que al repetirlas múltiples veces dan números distintos. Por factores externos que no puedo controlar o porque mi herramienta no está bien construida. Inclusive hay casos en los que lo que quiero medir no está correctamente definido por la naturaleza del fenómeno o porque mi metodología no aísla correctamente esa variable. Finalmente, aun si todos los casos anteriores no ocurren, toda herramienta de medición tiene un límite de precisión y un rango de cobertura. Hay un límite a qué y que tan bien puede medir algo.

Por esto, cuando hay alguna incerteza en la medición, es importante saber qué tamaño tiene y cuáles son las fuentes. Para entender cuáles son los límites de nuestro resultado, que tanta confianza le tenemos y donde se puede mejorar el experimento. Para todo esto tenemos un par de definiciones y clasificaciones útiles.

### Como definir una medición

Cuando queremos detallar una medición \\({X}\\) experimental formalmente se usan estas dos notaciones:

$$
\begin{aligned}
    X &= (\overline{X} \pm \Delta X)
    & (\text{el error se representa total}) \\\
    X &= \overline{X}(\Delta X)
    & (\text{única cifra significativa}),
\end{aligned}
$$

donde:

- \\( X: \\) La medición completa

- \\(\overline{X}: \\) Valor medio, valor de expectación, valor reportado o _mejor valor_ (según mi sistema de medición).

- \\(\Delta X: \\) Incerteza

Visualmente se interpreta:

![](/img/incerteza/definicion.png)

En algunos libros \\(\overline{X}\\) lo suelen poner como \\(X_0\\). El valor de expectación es el valor resultado de nuestro proceso de medición y la incerteza es el margen de error absoluto que tenemos como resultado de nuestro proceso de medición. El proceso de medición incluye todo, nuestro entorno, el sistema que medimos, como lo hacemos y los criterios que seguimos.

**Ejemplos:**

\\(2.05(1)\\) m \\( \equiv (2.05 \pm 0.01) \\) m

\\(3.45(1)\\) mm \\( \equiv (3.45 \pm 0.01) \\) mm

O la medición de la permitividad eléctrica del vacío del _NIST_ <cite>[^1]</cite>:

$$
\begin{aligned}
\varepsilon_0 &=
8.8541878128(13) \times 10^{-12} \text{F} \cdot \text{m}^{-1} \\\
&= (8.8541878128 \pm 0.0000000013)
\times 10^{-12} \text{F} \cdot \text{m}^{-1}
\end{aligned}
$$

[^1]: "2018 CODATA Value: vacuum magnetic permeability". The NIST Reference on Constants, Units, and Uncertainty. NIST. 20 May 2019. Retrieved 2019-05-20.

Otra cantidad interesante es el **error absoluto** y el **error relativo**. Aparecen bastante en las cuentas y nos ayudan a hacer unas consideraciones rápidas.

$$
\varepsilon_{abs} = X_{Real} - X_{Medido}
$$

$$
\varepsilon_{rel} = {\varepsilon_{abs} \over  X_{Real}}  \approx {\Delta{X} \over \overline{X}}
$$

La aproximación se vuelve igualdad si medimos exactamente el valor real. El error relativo se suele representar como porcentaje.

Más adelante veremos aplicaciones de estas dos definiciones. Pero, puedo adelantar que permiten descubrir, en una medición indirecta que depende de otras mediciones, cuál contribuye más al error final.

### Ejemplo, midiendo un palito con una regla barata

Veamos un par de casos prácticos de como decir qué es \\(\overline{X}\\) y qué es \\(\Delta X\\). Supongamos que hay un palito que tiene \\(8.65\\) cm. Supongamos también que no sé cuanto mide y me dispongo a medirlo con una regla casera. La regla la armó alguien que no me quiere, porque nomás me mide de a centímetros y no de a milímetros como la mayoría de reglas comerciales. Pero no tengo otra regla, me la banco. Con esta regla el extremo del palito está entre la raya de \\(8\\) cm y la de \\(9\\) cm. Según qué criterio siga voy a reportar distintas cosas. Podría decir bueno, la regla llega a \\(8\\) cm y no a \\(9\\) cm pimbi, el palito mide \\((8 \pm 1)\\) cm.

![](/img/incerteza/esquema-regla01.png)

![](/img/incerteza/esquema-detalle01.png)

La incerteza la considero de \\(1\\) cm porque es la mínima definición o apreciación de mi instrumento. ¿Tengo otras fuentes de error? Seguramente, la regla puede que no esté bien a escuadra. Quizás el extremo del palito que va a 0 no está exactamente en el medio de la marca del cero, quizás la separación entre divisiones no es exactamente \\(1\\) cm, o cualquier otra imperfección física. Pero en este caso es hilar demasiado fino, no es algo que se pueda ver a simple vista y en este caso no tiene tanto peso. Nos quedamos con \\(1\\) cm como la incerteza de medición. En este caso la regla parece estar bien construida, si fuese una regla defectuosa que me agrega de alguna forma algún error cercano a \\(1\\) cm, lo tengo que cuantificar y considerar.

---

Bueno, ya medí. Pero miro de vuelta para estar seguro y me pongo a pensar. A ojo veo que el palito está un poco más arriba del medio entre la raya de \\(8\\) cm y la de \\(9\\) cm. Entonces, si digo que mide \\(8.5\\) cm (el promedio de los extremos, para caer en el medio) y le doy un margen de error de \\(0.5\\) cm (la distancia entre el medio y un extremo) es razonable. Con esto el intervalo de medición contiene el largo real del palito, a ojo no sale de ese rango. Entonces digo ta, \\((8.5 \pm 0.5)\\) cm es la medición que voy a reportar. Mejoré la precisión al mirar en detalle y afinar el criterio.

![](/img/incerteza/esquema-regla02.png)

![](/img/incerteza/esquema-detalle02.png)

---

Pero sigo un poco más ambicioso, me doy cuenta de que la regla la puedo marcar con la uña o con algo filoso. Entonces marco una línea en el medio de las divisiones de \\(8\\) cm y \\(9\\) cm. Después marco una línea en el medio de las dos mitades que quedaron. Con las nuevas divisiones y mirando atentamente concluyo que el palito mide \\((8.5 \pm 0.25)\\) cm.

![](/img/incerteza/esquema-regla03.png)

![](/img/incerteza/esquema-detalle03.png)

---

Bien, logramos tres mediciones distintas de la misma magnitud usando tres criterios distintos. ¿Cuál es la correcta? ¿Cuál reporto? ¿Le creo más a una que la otra? ¿Son compatibles?

### Comparar y combinar

Cuando tenemos la incerteza de una medición (suponiendo que están bien puestas), podemos comparar la calidad de la medición con otras siguiendo un criterio de error relativo. Y si hay alguna que no sea consistente con las demás.

En el caso de los palitos, podría elegir quedarme con la medición que tiene el menor error relativo. Que sería la tercera medición porque:

$$
\begin{aligned}
  \varepsilon_{1} = {1    \over 8   }&, \quad
  \varepsilon_{2} = {0.5  \over 8.5 } \approx 0.0588, \quad \\\
  \varepsilon_{3} &= {0.25 \over 8.5 } \approx 0.0294
\end{aligned}
$$

$$
% \varepsilon_{1} > \varepsilon_{2} > \varepsilon_{3}
\varepsilon_{3} < \varepsilon_{2} < \varepsilon_{1}
$$

como \\(\varepsilon\_{3}\\) es la más chica, me puedo quedar con la medición \\(X_3\\).

Ahora, supongamos que para tener un resultado más completo elijo **combinar** todas las mediciones \\( (X_1, X_2, \cdots X_N) \\) que recopile. No voy a realizar una demostración de porque, pero lo más apropiado es hacer una suma ponderada de las inversas de las incertezas <cite>[^2]</cite>:

[^2]: Fernández, J. M. (n.d.). Errores. Retrieved April 7, 2023, from https://www.lawebdefisica.com/apuntsfis/errores/

$$
\sigma(\overline{X}) =
\frac{1}{\sqrt{\frac{1}{\sigma_{1}^2}+\frac{1}{\sigma_{2}^2}+\cdots+\frac{1}{\sigma_{n}^2}}}
$$

$$
\begin{aligned}
\overline{X} &= \left({1 \over \sigma(\overline{X})^2}\right)
\sum_{i=1}^N {\overline{X_i} \over \sigma_i^2}\\\
&= \frac{
  \frac{\overline{X_1}}{\sigma_{1}^2}
  +\frac{\overline{X_2}}{\sigma_{2}^2}
  +\cdots
  +\frac{\overline{X_n}}{\sigma_n^2}
}{
  \frac{1}{\sigma_{1}^2}+\frac{1}{\sigma_{2}^2}
  +\cdots
  +\frac{1}{\sigma_{n}^2}
}
\end{aligned}
$$

## <!--

Finalmente, notamos que este formalismo nos permite:

1. Llegar a un conseso sobre un resultado. Tenemos un rango donde podria estar el _valor real_. Esto nos da **objetividad**.
2. Otra persona con otro equipamiento puede tener un resultado que sea compatible con el que reporte. Esto hace que lo que hagamos sea **reproducible** y **comparable** con otros experimentos.
3. Nos permite dar una idea mas precisa cuando tengamos mediciones incompatibles. -->

### Tipos de errores

**Errores sistemáticos:** Son los mismos a lo largo de mi experimento:

- **Instrumentales (de [lo aparato](https://www.youtube.com/watch?v=JEdDaalYx0s)):** Deficiencias o límites de tu herramienta de medición. Cuantas divisiones podés leer con una regla, qué resolución tiene una balanza eléctrica, que tan preciso es un calibre, etc.
- **Dependen de la metodología:** La técnica que uno decida usar. No es lo mismo medir una vez, que medir \\(100\\) y promediar. Si medimos eventos de corta duracion, no es lo mismo medir eventos uno por uno y promediarlos, a medir la duración de \\(10\\) eventos y dividir esa duración por \\(10\\).
  - **Dependen de mi entorno:** Ruidos externos en las mediciones de un micrófono. Luz externa en un experimento de óptica. Vibraciones en algún experimento que requiera buena alineación o estabilidad.
- **Error humano:** Algunas cosas están limitadas por uno mismo, que tan bien puedo observar, que tan bien puedo escuchar, etc. Tomar una medición con un calibre es relativamente fácil con buena vista o con una lupa de aumento. Pero si uno tiene dificultades de visión se torna un desafío y puedo equivocarme.
- **Errores aleatorios:** Estos provienen de procesos aleatorios que interfieren con la medición. Algunos se pueden mitigar mediante estadística. Estos son en principio incontrolable por el observador.

### Cómo se hace y qué es la propagación de errores

Supongamos que queremos medir una magnitud \\(Z\\) que depende de magnitudes \\( X\\) e \\( Y\\) mediante una función \\(f\\) tal que \\(Z = f(X,Y)\\). Por ejemplo, la velocidad media se puede medir a partir de medir distancia recorrida y tiempo transcurrido. Si conozco las incertezas de \\(X\\) e \\(Y\\), puedo saber las de \\(Z\\) mediante propagación.

### Teoría superficial, para quedarse tranquilo

**No es necesario entender en detalle como uno obtiene la estrategia para la propagación, si te interesa ver las fórmulas y los resultados anda a la sección que sigue.**

Voy a dar una explicación breve e insatisfactoria para más detalle [visitar este link](https://www.wikiwand.com/en/Propagation_of_uncertainty). La explicación completa requiere un poco de álgebra lineal y de estadística. Cabe destacar que la teoría de propagación de errores es una teoría física, no matemática. Es un modelo de como se consideran las mediciones. Veamos como es y que presupone:

1. Suponemos que **la medición es una variable aleatoria con una distribución normal con su incerteza como desviación estándar**. Puede no ser el caso, puede que tenga una distribución asimétrica para mis mediciones. Sin embargo, una distribución normal aplica a la mayoría de los casos y habilita el próximo paso.
2. Luego se le aplica una transformación \\(f\\) a las muestras tal que **\\(f\\) se puede aproximar de forma lineal**. Trabajamos a partir de ahora con la aproximación.
3. Transformaciones lineales de una distribución normal tienen una distribución normal con una forma conocida.
4. Aprovechando ese resultado, obtengo la desviación estándar de la combinacion lineal, esta es mi incerteza final.

En resumen, asumo que tengo un fenómeno con distribución normal. Conozco como voy a transformar mis variables. Aproximo linealmente. Sé cómo obtener la desviación estándar de la combinación lineal de variables con distribución normal. [_Profit_](https://www.youtube.com/watch?v=tO5sxLapAts).

<!-- ### El resultado -->

Con todo esto, vamos a presentar el resultado final para el caso de dos variables. Para \\(Z = f(X,Y)\\) con \\(X\\) e \\(Y\\) dos mediciones _independientes_:

$$
\sigma^2(z)=\left(\frac{\partial f}{\partial x}\right)^2 \sigma^2(x)+\left(\frac{\partial f}{\partial y}\right)^2 \sigma^2(y).
$$

Interpretemos un poco lo que esta ecuación trata de decir. Primero podemos ver que cada término está modulado por la incerteza de su respectiva variable. Vemos que la variable que tenga mayor incerteza va a ser la que termine teniendo más peso en la incerteza final.
También es importante notar que cuanto más rápido cambie la función (esto va dado por \\( \frac{\partial f}{\partial x} \\)) más grande va a ser la incerteza final. Por esto, como la \\(f\\) es fija, la estrategia más óptima para reducir el error final es la de reducir la incerteza de cada variable y evitar medir en regiones donde los cambios de \\(f\\) sean muy rápidos.

¿Qué hago si las variables están correlacionadas? La respuesta está en [este link](https://www.wikiwand.com/en/Propagation_of_uncertainty). La demostración y la cuenta final es muy similar, pero se agregan términos con la correlación de \\(X\\) e \\(Y\\).

#### Vamos al hueso, cómo se calcula

Dejo una tabla resumida de estas propagaciones para casos sin correlación de distintas funciones:

$$
\begin{array}{|l|l|l|}
  \hline \text{Función}         & \text{Desviación estándar} \\\ \hline
  f = aX                        & \sigma_f =       |a|\sigma_X \\\ \hline
  f = a X+b Y                   & \sigma_f =       \sqrt{a^2 \sigma_X^2+b^2 \sigma_Y^2} \\\ \hline
  f = a X-b Y                   & \sigma_f =       \sqrt{a^2 \sigma_X^2+b^2 \sigma_Y^2} \\\ \hline
  f = X Y                       & \sigma_f \approx |f| \sqrt{\left(\frac{\sigma_X}{X}\right)^2+\left(\frac{\sigma_Y}{Y}\right)^2} \\\ \hline
  f = \frac{X}{Y}               & \sigma_f \approx |f| \sqrt{\left(\frac{\sigma_X}{X}\right)^2+\left(\frac{\sigma_Y}{Y}\right)^2} \\\ \hline
  f = a X^b                     & \sigma_f \approx \left|a b X^{b-1} \sigma_X\right|=\left|f b\right|\left|\frac{ \sigma_X}{X}\right| \\\ \hline
  f = a \ln (b X)               & \sigma_f \approx \left|a\right| \left|\frac{\sigma_X}{X}\right| \\\ \hline
  f = a \log _{c}(b X)          & \sigma_f \approx \left|{a \over \ln (c)} \right| \left| \frac{\sigma_X}{X }\right| \\\ \hline
  f = a e^{bX}                  & \sigma_f \approx \left| fb \right| \left| \sigma_X  \right| \\\ \hline
  f = a^{bX}                    & \sigma_f \approx \left| fb\ln(a) \right| \left| \sigma_X \right| \\\ \hline
  f = a \sin(bX)                & \sigma_f \approx \left| a b \cos(b X)   \right| \left| \sigma_X \right| \\\ \hline
  f = a \cos \left( b X \right) & \sigma_f \approx \left| a b \sin(b X)   \right| \left| \sigma_X \right| \\\ \hline
  f = a \tan \left( b X \right) & \sigma_f \approx \left| a b \sec^2(b X) \right| \left| \sigma_X \right| \\\ \hline
\end{array}
$$

Una de las más útiles:

$$
\begin{array}{|l|l|l|}
  \hline \text{Función} & \text{Desviación estándar} \\\ \hline
  f = X^m Y^n           & \sigma_f \approx |f| \sqrt{m^2\left(\frac{\sigma_X}{X}\right)^2+n^2\left(\frac{\sigma_Y}{Y}\right)^2} \\\ \hline
\end{array}
$$

Con esto ya exploramos la propagación con lápiz y papel. Pero esto no escala. Si tenemos muchas mediciones, o las queremos rápido, recomiendo [este post con herramientas para propagar](https://martinaramayo.gitlab.io/es/posts/propagaci%C3%B3n-de-errores-herramientas-de-software/).

### Mitigando errores aleatorios

Algunos equipos ya incorporan esta técnica. Consiste en sacarle el promedio a varias mediciones para mitigar el efecto que tengan los errores aleatorios. Si el error es genuinamente aleatorio el promedio permitirá independizarnos del ruido.

$$
\overline{X}=\frac{\sum_{i=1}^N \overline{X}_{i}}{N}
$$

$$
\begin{aligned}
\sigma(\overline{X})
&= \frac{\sigma(X)}{\sqrt{N}} \\\
&= \sqrt{\frac{\sum_{i=1}^N\left(
  \overline{X}_{i}-\overline{X}
\right)^2}{N \cdot(N-1)}}.
\end{aligned}
$$

<!-- ### Un poco de historia

La historia de la medida puede resumirse de la siguiente manera:

1. Luego de que la humanidad definio su sistema numerico, inicias midiendo cantidades de cosas discretas. Numero de bolsas de granos, numero de cabezas de ganado, etc.
2. Algunas cantidades, si queres conocerlas con mas precision por la razon que sea. Requieren tener una referencia. Por ejemplo, que tanto tiempo pasa entre una cosa y otra. Que tan lejos esta algo. Que tan pesado es algo. Como no es posible contarlo con los dedos o decirlo de forma certera. Usas patrones. Pesos patron, varas patron.
3. Con el avance del tiempo la demanda por precision aumenta. Hay tecnologias que la requieren y negocios que las aprovechan. Entonces se vuelve mas importante tener patrones mejor definidos, de mejor calidad. Para la masa patron se llegaron a guardar los pesos en bobedas lo mas aisladas posibles y con quimicos lo mas inertes posibles para que el peso no fluctue demasiado.
4. Eventualmente las tecnicas de medicion se volvieron mucho mas precisas que los patrones. Todos los cambios en estos patrones eran medibles. Se procede a armar un nuevo estandar. Fijar constantes fisicas, y medir esas constantes fisicas en experimentos para calibrarlos. Ya no calibrar en funcion de algo fisico sino en funcion de propiedades de la naturaleza que confiamos que son lo mas fijos posibles.

En fin, se cambio el enfoque, lo que calibra los aparatos de medicion son experimentos para medir propiedades de la naturaleza. Y ya no mediciones de cantidades físicas. -->

### Ejemplo: Medir la gravedad de la tierra dejando caer una pelota

Según cada error y aplicación específica hay distintas formas de estimar el error. Para errores instrumentales, los manuales suelen dar información sobre qué tipos de fuentes de error se pueden esperar. Pero como es uno el que mide es uno el que debe analizar detenidamente cada detalle y entender que puede afectar el resultado en su experimento.

Vamos a dar un ejemplo. Supongamos que queremos medir cuanto tiempo tarda en caer una pelota al piso desde una altura de \\(1.5\\) m arrancando quieta. Podemos hacerlo de la forma más simple posible, con un temporizador en una mano y con una pelota en la otra. Primero soltamos la pelota, si somos coordinados apretamos el temporizador al mismo tiempo. Después, cuando la veamos tocar el piso, apretamos el botón del temporizador nuevamente. ¿Qué cosas me pueden afectar la medición? Primero puede que no me sincronice bien. Capaz tiro la pelota y unos instantes después aprieto el botón de inicio del temporizador, o al revés. Puede que no le atine bien al momento en el que cae la pelota. Y parece que no es mucho tiempo, pero con una gravedad de \\(9.7 - 9.8 {\text{m} \over \text{s}^2}\\), despreciando el roce con el viento, la pelota tarda \\(553-556\\) ms en tocar el piso.
El tiempo de respuesta para estímulos visuales en personas está entre los \\(20-40\\) ms. Eso es un \\(7\%\\) de error relativo de origen humano solamente en mirar cuando cae la pelota.
¿Qué pasa si accidentalmente le agrego a la pelota un empujón hacia abajo o si no medí bien los \\(1.5\\) m y la deje caer de un poco más arriba? Tengo un error de metodología. Para controlarlo podría armarme un dispositivo a una altura fija que deje caer la pelota siempre de la misma manera. Me ahorraría fluctuaciones en los últimos dos errores de metodología que mencioné. Otra solución sería usar detectores, para ahorrarme los errores humanos al medir la caída. También podría grabar varios videos y medir el tiempo a partir de eventos del video.

<!-- Leer again -->

¿Pero cuánto es un \\(7\\)% de error relativo? ¿Es mucho? ¿Es poco? Depende de para que sea el experimento. Si en el experimento quiero hacerme una idea de cuanto tarda en caer la pelota no es mucho problema. Si quiero hacer este experimento para medir la aceleración gravitatoria, puedo estimar el orden de magnitud, pero, no me va a permitir determinar que tanto varía en distintas partes del mundo. Si supongo que puedo medir de alguna forma el tiempo de caída con un \\(7\\)% de error relativo, asumiendo que la altura inicial la medí perfecto y siempre la respete, voy a tener un error relativo del \\(14\\)% porciento en la medición. Esto me dice dos cosas, este no es un buen método para estimar (me duplica el error relativo de lo que mido en tiempo) y que no voy a poder capturar las sutiles diferencias en la superficie terrestre que corresponden a un \\(0.7\\)% <cite>[^3]</cite>.
Es más, si midiésemos la aceleración gravitatoria solamente con esta técnica, sería imposible saber que la aceleración gravitatoria varía en distintos puntos del planeta. Con este experimento necesitaríamos medir tiempos con \\(20\\) veces menos error relativo. Es decir, reducir nuestro tiempo de respuesta significativamente.

[^3]: Gravity of Earth. (n.d.). In Wikiwand. Retrieved April 7, 2023, from https://www.wikiwand.com/en/Gravity_of_Earth

Como pudimos ver en este simple ejemplo, los cálculos de errores me dicen mucho sobre mi experimento. Permite rápidamente descartar metodologías insuficientes. Permite Enfocarnos en cuáles son las principales fuentes de error para hacer mejoras sucesivas y nos permite informar a quien interprete esas mediciones sobre que tan bien conocemos el valor que estamos obteniendo. Siempre y cuando lo hagamos bien.

### Observaciones

<!-- Leer again -->

<!-- Hasta ahora hablamos de un valor "verdadero". No hay forma de determinar los valores "verdaderos". Todas las mediciones son comparaciones en términos de un patrón. Hay patrones físicos y patrones experimentales. Hay fenómenos que, tal y como los conocemos, tienen tan poca varianza que los usamos como referencia. Y durante una porción importante de la historia se utilizaban objetos físicos para definir los estándares de calibración y para definir que era cada medida. Medidas que luego se cuentan para obtener una medición. Pero todos estos métodos son indirectos. Si usan una cámara térmica, la cámara no mira la temperatura. Recibe una determinada señal que sabemos que está relacionada con la temperatura del cuerpo que estamos mirando. Esa señal la convierte en una señal eléctrica, se digitaliza y se muestra. Pero en estos procesos hay múltiples pasos intermedios. Cada uno agregando incertidumbre al proceso de medición. Lo cual nos aleja del ideal de conocer exactamente cuanto "mide" algo, pero es la única forma de hacerlo posible en el mundo real. -->

En resumen, todas las mediciones son indirectas. Y los valores "reales" son los valores que más confianza les tenemos con todo lo que sabemos. En la práctica es casi imposible tener un error cero. Las únicas cantidades que tienen un error cero son cantidades discretas (cantidad niveles de energia en un átomo) o constantes físicas que definimos como fijas. Por ejemplo, la velocidad de la luz, es una cantidad que fue definida como \\(299 \ 792 \ 458 {\text{m} \over \text{s}}\\)<cite>[^4]</cite> por consenso. Cualquier otra cantidad que midamos tiene la incerteza propia de nuestra metodología. Podemos controlar esa incerteza de alguna forma. Pero siempre hay una incerteza.

[^4]: CODATA Value: Speed of Light in Vacuum. (n.d.). In NIST Physics Laboratory. Retrieved April 7, 2023, from https://physics.nist.gov/cgi-bin/cuu/Value?c

### Recomendado para aprender más

- Video de veritasium sobre la redefinicion del kilogramo[https://www.youtube.com/watch?v=eWgbdCDAg6M](https://www.youtube.com/watch?v=eWgbdCDAg6M)
<!-- * [Intensidad de luz (Hyperphysics)](http://hyperphysics.phy-astr.gsu.edu/hbasees/vision/photom.html#c1) -->
- **Libro recomendado:** Hase, T., Hughes, I. (2010). Measurements and Their Uncertainties: A Practical Guide to Modern Error Analysis. Reino Unido: OUP Oxford.
<!-- * Otro post en este sitio (Si aplica) -->
