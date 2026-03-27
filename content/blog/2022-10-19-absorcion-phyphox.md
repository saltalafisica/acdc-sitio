---
title: "Absorción de luz visible"
subtitle: 💡📃📱
math: true
author: Martín Aramayo, Juan Pablo Carbajal, Alberto Villagran, Alejandra Mendez
# image: "/img/blog/2022-10-19-absorcion-phyphox/lamina.jpg"
tags: ["Absorción", "Luz", "Smartphone", "Phyphox", "Sensores", "Óptica"]
date: 2022-10-19
# image: false
banner: "img/blog/2022-10-19-absorcion-phyphox/lamina.jpg"
---

El objetivo de este experimento es observar como la [luminosidad](https://es.wikipedia.org/wiki/Luminosidad?oldformat=true) detectada por un sensor decrece a medida que se incrementa la cantidad de material entre el sensor y una fuente de luz.

<!--more-->

---

- **Dificultad:** ★★☆☆☆

- **Materiales:**
  - Smartphone
  - App [Phyphox](https://phyphox.org/download/) instalada en tu teléfono
  - Una lámpara o linterna para usar como fuente de luz
  - Láminas de plástico transparente u hojas de papel delgado.
    Las láminas u hojas tienen que ser del mismo material (por ejemplo, podes
    cortar o doblar un folio, o usar plástico para forrar).

- **Duración de preparación:** 40 minutos

- **Temas:** Luz, Absorción, Óptica.

---

![Fuente: http://opentp.fr/en/smart/absorption/](/img/blog/2022-10-19-absorcion-phyphox/lamina.jpg)

Este experimento se basa en el contenido publicado por [Open TP](http://opentp.fr).
Acá tenés un link al [artículo original](http://opentp.fr/en/smart/absorption/) en inglés.

## Luminosidad en condiciones de luz completa

1.  Iniciá Phyphox en el smartphone y elegí "Luz" en la sección "Sensores" del menú principal.

    ![Datos crudos de luminosidad](/img/blog/2022-10-19-absorcion-phyphox/absorcionkst.jpg)

    <!-- ![datos crudos de luminosidad](/img/blog/2022-10-19-absorcion-phyphox/part2.jpg) -->

    Este sensor ofrece dos funcionalidades:
    - GRÁFICO: muestra un gráfico de tus mediciones, y
    - SIMPLE: muestra el valor medido por el sensor.

    Phyphox nos avisa con una nota al pie que en algunos teléfonos el sensor solo se actualiza cuando la luminosidad cambia.
    Mové tu mano por encima de tu teléfono y descubrí cómo se comporta.

    > _¿Tenés problemas con Phyphox? La solución puede estar en nuestra [Ayuda phyphox](/random/physphox)_

2.  Ilumina el teléfono con luz directa usando tu fuente de luz elegida.
    El valor que aparece en la app es la _luminosidad de referencia_ en condiciones de _luz completa_. Una vez tengas tu referencia, mantén la distancia entre el sensor y la fuente de luz. Es importante darle estabilidad a la configuración para tener una luminosidad de referencia sólida.

    > ▸ _¿Podés determinar dónde está el sensor de Luz en tu teléfono?_
    >
    > ▸ _¿Usarías una fuente de luz o algo opaco para determinar su ubicación?_
    >
    > _Ayuda: No es la cámara frontal._

## Experimento de absorción

3.  Una vez que confíes en tu valor de referencia (hacé varias pruebas tapando y destapando el teléfono),
    empezá a colocar las láminas sobre tu teléfono, una encima de la otra: primero ninguna, luego 1, luego 2, y así sucesivamente.

    > _¿Qué sucede con el valor de la luminosidad en la app?_

    El material de las láminas **absorbe** (y _dispersa_ si usaste papel) la luz.
    Esto reduce la cantidad de luz que llega al sensor y baja la luminosidad medida por el smartphone.

## Luminosidad y grosor del material absorbente (avanzado)

4.  Ahora vamos a determinar cómo el valor de la luminosidad varía con el número de láminas colocadas sobre el sensor.
    Es decir, como decrece la luminosidad con el grosor del material absorbente.

    Para hacer esto vamos a descargar los datos del experimento.
    Te recomiendo que repitas el experimento varias veces, registrando en un papel el tiempo al que agregas una lámina.
    Esto último va a ser útil a la hora de analizar los datos.

    Los datos los podés descargar usando el menú desplegable (el símbolo ⋮ en la esquina superior derecha), y eligiendo "Export data".
    Ahí podés seleccionar el formato de los datos.
    Te recomiendo que uses "CSV (Comma, decimal point)", porque es un formato que lo puede leer
    cualquier programa para procesar datos.
    En particular, podés abrir el archivo utilizando [LibreOffice Calc](https://es.libreoffice.org/descubre/calc/).

5.  Los datos se bajan (o envían) en un archivo comprimido `.zip`, que debes extraer.
    El contenido consiste en un archivo `Raw data.csv` y una carpeta `meta`.
    Sólo nos interesa el archivo `Raw data.csv`.
    Al abrir el archivo en mi versión de Calc, las primeras filas de datos se ven así:

    ![datos crudos de luminosidad](/img/blog/2022-10-19-absorcion-phyphox/phyphox_data_absorcion.png)

    La primera columna es el tiempo en segundos y la segunda el valor de luminosidad medida por el sensor.
    Quizás podés notar que mis datos de luminosidad varían un mónton.
    Incluso en los primeros segundos, que son para la referencia, el valor cambia entre 9 y 34.
    Utilizando tus notas del tiempo al que agregaste el material, podés reducir tus datos. Haciendo esto, mi tabla queda:

    ![datos reducidos de luminosidad ](/img/blog/2022-10-19-absorcion-phyphox/phyphox_data_absorcion_reduc.png)

    Podés agregar una columna "Nro. De Láminas" para indicar cuantas láminas fuiste agregando sobre el sensor. Además, podés usar una columna extra (sin nombre, columna D) para anotar el promedio de todas las mediciones en esa condición.

6.  Otra forma de ver nuestros datos es mediante un gráfico. Usando Calc, podés hacer graficar la luminosidad en función del número de láminas. En mi caso, obtengo:

    ![plot de luminosidad](/img/blog/2022-10-19-absorcion-phyphox/phyphox_data_absorcion_plot.png)

    ¿Obtenés algo parecido?

    > _¿Qué ocurre si graficas el logaritmo de la luminosidad en función del número de láminas? Podés investigar sobre la [Ley de Beer-Lambert](https://es.wikipedia.org/wiki/Ley_de_Beer-Lambert) para entender este gráfico._

## El desafío definitivo

Si te quedaste con ganas de seguir jugando con este experimento, podemos sacarle el jugo analizando la variación de la luminosidad cuando el medio absorbente es agua con pintura. Es decir, en vez de usar láminas, vamos a usar un recipiente (transparente) con agua.
Podés ver qué ocurre con la luminosidad si:

- cambiamos la concentración del agua: le ponemos colorante al agua poco a poco, o
- cambiamos el espesor del líquido: agregamos más recipientes de agua, entre el sensor y nuestra fuente de luz.

Repetí los ítems 4, 5 y 6.

---

### Recomendaciones para aprender más

- [Absorción de luz (Hyperphysics)](http://hyperphysics.phy-astr.gsu.edu/hbasees/phyopt/absorb.html#c1)
- [Intensidad de luz (Hyperphysics)](http://hyperphysics.phy-astr.gsu.edu/hbasees/vision/photom.html#c1)
- [Sobre los sensores del teléfono](https://andro4all.com/tecnologia/sensores-movil)
