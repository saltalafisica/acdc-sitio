---
title: "Cómo medir distancias midiendo ángulos"
author: Martín Aramayo
subtitle: "📏➕📐"
# image: "/page/medir-distancias-con-trigonometria/regla-mano-izquierda-portrait.webp"
tags:
  [
    "Distancias",
    "Trigonometría",
    "Matemática",
    "Física",
    "Propagación de errores",
  ]
date: 2022-10-15
math: true
# image: true
banner: "img/blog/2022-10-08-Medir-distancias-con-trigonometria/regla-mano-izquierda.webp"
---

Como medir a ojo y mal, pero con criterio.

<!--more-->

---

- **Dificultad:** ★★☆☆☆

- **Materiales:**
  - Regla
  - Smartphone
  - Transportador

- **Duración de preparación:** 30 min

- **Temas:** Trigonometría, propagación de errores.

---

Un día aburrido, jugaba con una cinta roja de un metro que regalaban en la ferretería. Había una estantería alta y me preguntaba que tan alta podía ser.

Se me ocurrió rápidamente sacar la siguiente foto:

![](/img/blog/2022-10-08-Medir-distancias-con-trigonometria/scaloneta.webp)

Aprovechando la cinta roja me construyo un triángulo rectángulo.

![](/img/blog/2022-10-08-Medir-distancias-con-trigonometria/triangulito.webp)

Con una cuentita como esta, conociendo que se cumple:

$$
\tan(\alpha)  = {x \over b}
\Rightarrow
x = \tan(\alpha) \cdot b,
$$

donde el \\( x \\) es el lado que me interesa, puedo obtener el alto de la estantería.

A ojo uno podría decir que el ángulo está entre 70° y 80° grados usando la regla de la mano izquierda. Vamos a hacer la cuenta con 75°. Respecto a cuanto vale \\(b\\), la cinta roja era de 1 m asumo \\(b = \\) 1 m. Obtengo entonces (ojo con tener la calculadora en radianes, para chequear, asegúrate de que \\(\sin(30°)=0.5\\)):

$$
x = \tan(75°) \cdot 1 \text{m} = 3.7 \text{m}
$$

## Para los que quieran ir un paso más allá

Como no conocemos el ángulo con mucha precisión y para que tengamos una idea más clara de que margen de error puede tener esta cuenta vamos a realizar propagación de errores. Podemos usar una calculadora con propagación como [Qalculate!](https://qalculate.github.io/).
Le asignamos un error a \\(\alpha\\) de tal manera que quede:

$$
\alpha_{\text{a ojo}}  = (75 ± 5)°
$$

$$
x_{\text{a ojo}}
= \tan
    (\alpha_{\text{a ojo}})
= (3.7 \pm 1.3) m
$$

¿Por qué 5° grados de margen de error? Mi criterio me dice que está entre 70° y 80°, asique le vamos a dar un error igual a la mitad de diferencia de esos dos ángulos. Para ser consistentes con el intervalo. Uno puede hacerse una idea de que esto es correcto usando la regla de la mano derecha:

![](/img/blog/2022-10-08-Medir-distancias-con-trigonometria/regla-mano-izquierda.webp)

Este margen de error es grande y podemos hacerlo mejor. Vamos a ver como mejorar esta cuenta. Una vez en casa agarré [Inkscape](https://inkscape.org/) (un software de dibujo) dibujé un triangulito que más o menos calzaba y medí el ángulo preciso para ver que tanto le había errado. Obtengo:

$$
\alpha_{\text{de Inkscape}}  = (77.72 ± 2)° = (78 ± 2)°
$$

Ahora, ¿Por qué le invente un margen de error de 2°? Nuevamente es el criterio que tomo y considero que es el error de definición del triángulo que tome. ¿Por qué no 3°, 4° o 5°? Considero que está mejor tomado que lo que hice con la mano, pero el triángulo no está bien definido, la foto no está del todo alineada. No tendría sentido ponerle algo como 0.01°. Uno puede discutir todo el día cuál es el criterio correcto. Ver el pelo al huevo, o seguir leyendo y ver que pasa.

Con el \\(\alpha\_{\text{de Inkscape}}\\) obtengo:

$$
\begin{aligned}
\alpha_{\text{de Inkscape}}
&= (77.72 ± 2)° \\\ &= (78 ± 2)°
\end{aligned}
$$

$$
\begin{aligned}
    x_{\text{de Inkscape}}
    &= \tan
        (
            \alpha_{\text{de Inkscape}}
        ) \\\
    &= (4.70 \pm 0.81) m
\end{aligned}
$$

Con esto ya tenemos una buena idea de como calcularlo, en este caso, para este ángulo. Pero, que pasa si cambiamos la amplitud. ¿Como cambiaria el error?

Hagamos propagación de errores para ver que tanto afecta nuestro error de medición de ángulo a nuestra medición de distancia.

Vamos a ver en general como aumenta el error de un cálculo de este tipo:

$$
\begin{aligned}
    \Delta x
        &=
        \Delta \tan(\alpha) \\\
        &=
        \left|
            { d  \over d \alpha }
            \left( \tan( \alpha ) \right)
        \right| \Delta \alpha\\\
        &=
        \left| \sec^2(\alpha) \right| \Delta \alpha\\\
        &=
        \sec^2(\alpha) \Delta \alpha
\end{aligned}
$$

Armemos un gráfico de la secante cuadrada para mostrar como se porta, el codigo python para crear este gráfico lo encuentran en [errorAngulo.py](https://gitlab.com/acdc-hvm/experimentos/-/tree/master/static/img/blog/2022-10-08-Medir-distancias-con-trigonometria/plots/errorAngulo.py):

![](/img/blog/2022-10-08-Medir-distancias-con-trigonometria/plots/errorAngulo.png)

Podemos ver que el error \\(\Delta x \\) escala con el error \\(\Delta \alpha\\). Además, cuanto más aumenta el \\(\alpha\\), más alto es el error y explota cuando \\(\alpha = 90°\\). Esto es un problema, porque cuanto más lejano está lo que queremos medir, más grande es el ángulo. En estos casos el error aumenta. ¿Que soluciones uno puede ofrecer?
Podemos medir el ángulo de un lugar más alto, con altura conocida. Otra alternativa es medir ángulos pequeños pero catetos \\(b\\) largos. Entonces nuestra principal contribución al error de medición, vendrá del instrumento que usemos para medir el cateto \\(b\\). Aquí el análisis se complica porque hay que empezar a considerar el error de medición proveniente de \\(b\\).

## Palabras finales

Hay muchas configuraciones que uno puede probar. Pero una recomendación importante es tener en cuenta la alineación de la cámara con la que se va a tomar la foto. Se puede hacer con una aplicación o simplemente colocando un trípode y realizando ajustes. Muchos teléfonos tienen el acelerómetro y algunos hasta un giroscopio para poder determinar su orientación, con esto se lo puede dejar bien alineado.

¿Se te ocurre otra forma de estimar estas alturas?

---

### Recomendado para aprender más

- Para medir distancias astronómicas, también se miden triangulitos, mas info en este link sobre [paralaje (Hyperphysics)](http://hyperphysics.phy-astr.gsu.edu/hbasees/Astro/para.html#c1).
- Un poco más sobre calculadoras para propagar errores en [este link](https://martinaramayo.gitlab.io/es/posts/propagaci%C3%B3n-de-errores-herramientas-de-software/).
- [Sobre la teoría de propagación de errores](https://es.wikipedia.org/wiki/Propagaci%C3%B3n_de_errores?oldformat=true).
