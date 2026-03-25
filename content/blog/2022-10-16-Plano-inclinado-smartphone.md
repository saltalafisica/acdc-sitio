---
title: "Plano inclinado con Smartphone"
subtitle: 📐📱🎢
math: true
author: Martín Aramayo, Alberto Villagran
# image: "/page/medir-distancias-con-trigonometria/regla-mano-izquierda-portrait.webp"
tags: ["Presión", "Física", "Unidades", "Smartphone", "Phyphox"]
date: 2022-10-15
# image: true
banner: "img/plano.webp"
---

Medición de velocidad de un tubo rodando por un plano inclinado usando Phyphox

<!--more-->

---

- **Dificultad:** ★★★☆☆

- **Materiales:**
  - Smartphone (con la app [Phyphox](https://phyphox.org/))
  - Plano inclinado
  - Tubo de papas fritas (~~Pringles~~)
  - Papel para rellenar
  - Balanza
  - Calibre

- **Duración de preparación:** 30 min

- **Temas:** Presión, experimento práctico.

---

La gente de Phyphox armo estos experimentos, los hacemos disponibles traducidos. Dejo link al [original](https://phyphox.org/experiment/pressure-in-a-bag/) con los [ejercicios](https://phyphox.org/material/pressure-in-a-bag.pdf).

## Preparación

![](/img/plano.webp)

Video ilustrativo: https://youtu.be/gPq4Le9kXWE

1. Prepara un plano inclinado y un cilindro para el experimento como se ve en la figura.
2. Instalar Phyphox en tu smartphone.
3. Dentro de Phyphox, entrar a Mecánica → Rodar.
4. Medir el radio / diámetro del tubo y la altura inicial con el criterio del dibujo.
5. Colocar el radio del tubo en Phyphox en el campo `Radio del tubo`.

![Fuente: http://opentp.fr/en/smart/absorption/](/img/rodar/absorcionPhyphox.png)

### Experimento

Una vez completados los requisitos de la sección anterior, es importante fijar el teléfono dentro del tubo de alguna manera. Podés rellenar el tubo con papel de diario o lo que veas mas conveniente. Es importante que el teléfono no se mueva mucho dentro del tubo porque esto afecta a la medición. Queremos medir como se comporta el tubo al rodar. No el movimiento del teléfono dentro del tubo.

Es preferible que el teléfono tenga accesible el botón de inicio de experimento ►. Una vez presionado empezarán a guardarse las mediciones de los sensores del smartphone.

Luego de activar la medición, con el teléfono en el tubo, se lo larga a rodar. Una vez tocó el piso, se detiene la medición y se evalúa el experimento.

<!--
### Notas sobre sensores

Hay dos sensores que permiten el seguimiento de el smartphone.

1. Acelerómetro:
2. Giroscopio: Permite determinar la orientacion respecto a un eje fijo.

Muchos smartphones tienen giroscopios de 3 ejes con los cuales se puede medir la rotación del teléfono. Junto con el acelerómetro, el software en el teléfono reconoce los cambios en movimiento. Esto se usa al navegar con GPS, rotar la pantalla o para controlar algunos juego. El acelerómetro es capaz de medir la rotación al rededor de 3 ejes \\(x\\), \\(y\\) \\(z\\). El acelerómetro suele tener un tamaño de unos 2 mm x 2 mm y consiste en un sistema oscilador que es influenciado por el efecto Coriolis al ser rotado. Esto es medido a través de capacitores y es transferido como dato de velocidad angular. -->

### Preguntas y tareas

1. Explica como el programa determina la velocidad de desplazamiento utilizando datos específicos y la medición de la velocidad angular.
2. Transfiere pares seleccionados de mediciones de la forma más precisa posible en un gráfico \\(v\\) vs. \\(t\\). Determinar la aceleración del tubo rodando a lo largo del plano. (Podés acceder a los datos medidos si los exportas, podés abrirlos con Excel, Google sheets o algo similar (inclusive podés analizarlo con Python usando pandas)).
3. Ingresar la velocidad del tubo al final del plano inclinado.
4. Determinar la energía cinética y potencial del tubo antes de largarlo por el plano inclinado. Comparar los valores y evaluar el resultado.
   Además de la energía cinética traslacional \\(E_T = {1 \over 2} m v^2\\), el tubo tiene energía cinética rotacional que se calcula mediante \\(E_R = {1 \over 2} I_Z \omega^2\\) con \\(I_Z = {1 \over 2} m r^2\\) (Ojo eso es para este caso en el que gira paralelo a su eje). La energía cinética total del tubo se puede calcular usando \\(E_K = E_T + E_R\\).
5. Determinar la energía rotacional \\(E_R\\) a partir de los datos medidos y determinar la energía cinética real \\(E_K\\). Comparar el resultado con la energía potencial y evaluar el resultado.

¿Se te ocurre otro experimento con estos elementos?

### Recomendaciones para aprender más

- [Energía potencial (Hyperphysics)](http://hyperphysics.phy-astr.gsu.edu/hbasees/gpot.html#mgh)

- [Energía cinética (Hyperphysics)](http://hyperphysics.phy-astr.gsu.edu/hbasees/ke.html#ke)

- [Teoría y ejercicios resueltos en español (No me salen de Ricardo Cabrera)](https://ricuti.com.ar/no_me_salen/energia/index_energia.html)

CC BY-SA Mirko Zeppmeisel (paper original)
