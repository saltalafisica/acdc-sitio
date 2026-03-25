---
title: "Experimento de Sonar"
subtitle: 📱📢🧱
math: true
author: Martín Aramayo, Alberto Villagran
# image: "/page/medir-distancias-con-trigonometria/regla-mano-izquierda-portrait.webp"
tags: ["Sonido", "Ondas", "Reflexión", "Señales", "Smartphone", "Phyphox"]
date: 2022-10-19
# image: false
banner: "img/sonar/sonar.png"
---

El experimento Sonar envía sonidos cortos a través de un parlante y graba el eco con un micrófono. Muestra un gráfico indicando donde rebotó el audio.

<!--more-->

---

- **Dificultad:** ★★☆☆☆

- **Materiales:**
  - Smartphone (con la app [Phyphox](https://phyphox.org/))
  - Aislantes (Recomendado)
  - Superficie plana que refleje bien el sonido: Baldosas, chapas metálicas, una pared.

- **Duración de preparación:** 40 min

- **Temas:** Sonido, cinemática.

---

La gente de Phyphox armo estos experimentos, los hacemos disponibles traducidos. Dejo link al [original](https://phyphox.org/wiki/index.php?title=Experiment:_Sonar). Para un video de ejemplo se puede acceder a [este link](https://www.youtube.com/watch?v=Ebj3v701HE0).

![](/img/sonar/sonar.png)

### Requisitos

En teoría, este experimento se puede hacer en cualquier lado. Pero es difícil interpretar los ecos generados en una habitación cualquiera. Cada objeto de la habitación puede reflejar el sonido y contribuir a que haya algún eco.

Es recomendable aislar el teléfono en todas las direcciones que no se van a usar en el experimento. Esto se puede conseguir con un aislante, ropa, o almohadas. Puedes construir una cavidad en la cual se pueda colocar el teléfono dejando un lado abierto a los ecos. En el lado abierto es preferible colocar un buen reflector como una baldosa.

No importa si la cavidad que preparas te dificulta acceder al teléfono. Podés usar la interfaz [remota](http://phyphox.org/remote-control/) en un segundo dispositivo (PC, Tablet, Smartphone, etc.) para controlar el experimento desde el segundo dispositivo y obtener los resultados.

Es importante reducir el ruido del ambiente durante el experimento. Hasta una conversación puede perturbar el experimento.

Se puede mejorar este experimento usando un micrófono y parlante externo bien direccionados y aislados. Un parlante bluetooth y un micrófono conectado con cable pueden dar más control sobre la configuracion y el aislamiento.

### El arreglo

Con el teléfono bien ubicado para escuchar el eco de interés, subi el volumen e inicia el experimento. Se escuchará un click en el teléfono y deberías ver datos de distancia en el gráfico. Puede que todavía veas picos de ecos irrelevantes. Si movés la superficie reflectante verás que el pico correcto también se mueve.

### Análisis

El sonido que se escucha no es cualquier click, es conocido como [chirp](https://www.wikiwand.com/en/Chirp). Es una función senoidal que carga su frecuencia rápidamente. En este caso va desde 1 kHz a 4 kHz por un periodo superior a 5 ms. Adicionalmente, una función de peso se agrega para que el [chirp](https://www.wikiwand.com/en/Chirp) inicie y termine de forma suave. El [chirp](https://www.wikiwand.com/en/Chirp) se repite 5 veces en un intervalo de 30 ms.

El grabado ocurre en simultáneo. Phyphox calcula la correlación cruzada de los cinco [chirps](https://www.wikiwand.com/en/Chirp) y la grabación. El resultado es una medida de que tan fuerte el [chirp](https://www.wikiwand.com/en/Chirp) y la grabación coinciden en cualquier instante de tiempo. La correlación más fuerte ocurre en el inicio del experimento. Este punto se considera como el \\(t=0\\) y el resto de la correlación cruzada se muestra al usuario.
Para que el gráfico se vea más bonito, se lo suaviza con un filtro gaussiano (ancho \\(\sigma\\) de 3 puntos de datos).

El tiempo en el eje \\(x\\) es multiplicado por la velocidad del sonido y dividido por 2 para dar la correspondiente distancia de los ecos.

### Problemas y soluciones

- Muchos picos al azar. Esto puede ser causado por un fuerte ruido de fondo: Se recomienda hacer el experimento en un ambiente sin ruido.
- Muchos picos en posiciones fijas: Si aparecen siempre a la misma distancia (mientras el teléfono se encuentra en el mismo lugar), debes mejorar el aislamiento. Muy posiblemente estos picos provengan de otros objetos reflectantes.

### Video Demostración

- Versión en inglés https://youtu.be/Ebj3v701HE0
- Versión en alemán <https://youtu.be/3JtJoJAAgKU>

### Recomendaciones para aprender más

- [Reflexión de sonido (Hyperphysics)](http://hyperphysics.phy-astr.gsu.edu/hbasees/Sound/reflec.html#c1)
<!-- * [Reflexión de ondas (No me salen de Ricardo Cabrera)](https://ricuti.com.ar/no_me_salen/ondas/Ap_luz_rerfac.html) -->

Fuente: Phyphox
