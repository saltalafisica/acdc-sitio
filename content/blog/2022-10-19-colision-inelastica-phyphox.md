---
title: "Colisión inelástica"
subtitle: 🎱💥🧱
math: true
author: Martín Aramayo, Alberto Villagran
# image: "/page/medir-distancias-con-trigonometria/regla-mano-izquierda-portrait.webp"
tags: ["Colisiones", "Colision inelastica", "Mecánica", "Smartphone", "Phyphox"]
date: 2022-10-19
# image: true
banner: "img/blog/2022-10-19-colision-inelastica-phyphox/phyphoxDrop.webp"
---

Calcula la perdida de energía de un objeto cuando cae y rebota.

<!--more-->

---

- **Dificultad:** ★★☆☆☆

- **Materiales:**
  - 1 Smartphones (con la app [Phyphox](https://phyphox.org/))
  - Una bolita
  - Una superficie

- **Duración de preparación:** 5 min

- **Temas:** Colisiones, Colisión inelástica, Mecánica.

---

La gente de Phyphox armo estos experimentos, los hacemos disponibles traducidos. Dejo link al [original](https://phyphox.org/wiki/index.php?title=Experiment:_Inelastic_Collision).

![](/img/blog/2022-10-19-colision-inelastica-phyphox/phyphoxDrop.webp)

En este experimento de colisión inelástica se graba con micrófono el sonido de una pelota. El tiempo entre rebotes permite calcular: la altura inicial de la bolita, la altura entre rebotes y la porción de energía disipada en cada rebote.

## Requisitos

Solo se requiere una pelota y una superficie lo mas a nivel posible. Es importante que la pelota suene al golepar la superficie.

**NOTA:** Si el teléfono que se usa no es lo suficientemente rápido para analizar el audio en tiempo real. Entonces, el reloj contará el tiempo muy lento.

## Análisis

Se utilizan unos módulos para decidir cuantos rebotes han ocurrido. Luego,
se analizan pedazos del audio, comparando su máximo con un umbral. Si se excede el umbra, calculamos el número de muestras del máximo y lo transformamos en tiempo.

<!-- (revisar este párrafo) -->

Si el análisis toma mas tiempo que el que se usa para llenar el buffer de audio, se perderán muestras y el reloj no va a funcionar bien.

Este experimento es idéntico al del **cronómetro acústico (acoustic stopwatch)** de Phyphox. A partir del temporizador el resto se calcula mediante:

- La relación de la energía cinética antes y después es igual a la relación de los cuadrados del tiempo entre este y el próximo rebote y este y el rebote anterior. La altura máxima entre dos rebotes es igual a \\({1 \over 8} \cdot {9.81} \ {\text{m} \over \text{s}^2 } \cdot dt^2\\) con \\(dt\\) el tiempo entre rebotes.

- Para obtener la altura inicial, el experimento asume que la energía perdida en el primer rebote es aproximadamente la misma que se pierde en el segundo rebote.

## Problemas y soluciones

- El tiempo medido es demasiado pequeño: Desafortunadamente, esto puede pasar si el teléfono no puede analizar datos tan rápido como se graban. Por el momento, no hay una solución a este problema, solo utilizar un teléfono más rápido.

- Cada rebote se registra múltiples veces: En este caso la duración del ruido es demasiado largo. El experimento espera al menos 100 ms antes de reconocer una activación. Si hay eco o algún tipo de campaneo, esto puede ser suficiente para detener el reloj otra vez. Se puede intentar aumentando el **delay mínimo (Minimum delay)**.

- Se pierden rebotes. En este caso, probablemente necesites bajar el **umbral (threshold)**, para que los ruidos del rebote estén por encima del umbral. Puedes usar el osciloscopio de audio para revisar amplitudes y estar seguro.

- El experimento se activa sin ningún rebote. Quizás haga falta incrementar el umbral por arriba del ruido de fondo. Podés utilizar el osciloscopio de audio de Phyphox para chequear amplitudes.

---

### Recomendaciones para aprender más

- [Colisión inelástica (Hyperphysics)](http://hyperphysics.phy-astr.gsu.edu/hbasees/inecol.html#c1)
- [Choque plastico (No me salen de Ricardo Cabrera)](https://ricuti.com.ar/no_me_salen/energia/AE_choques.html)
