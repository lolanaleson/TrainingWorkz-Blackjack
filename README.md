## Fuentes y justificación de las reglas del juego

Las reglas utilizadas en este proyecto se han definido combinando las **instrucciones del enunciado oficial del ejercicio** con las **normas clásicas del Blackjack**, contrastadas con fuentes fiables y simulaciones reales del juego.

---

### Reglas del dealer (turno de la banca)

El comportamiento del dealer se ha implementado siguiendo las normas tradicionales del Blackjack documentadas en Wikipedia:

> “Las propias reglas del blackjack obligan al crupier a pedir carta si tiene menos de 16 puntos y plantarse si cuenta con entre 17 y 21 puntos. Esto se conoce como turno de la banca. Finalmente, llega el turno de pago, donde se acaba la mano.”  
> — [Wikipedia: Blackjack](https://es.wikipedia.org/wiki/Blackjack#:~:text=Las%20propias%20reglas%20del%20blackjack,donde%20se%20acaba%20la%20mano.)

Por tanto, en esta versión:

- El **dealer pide cartas automáticamente** mientras su mano tiene un valor **inferior a 17**.  
- El **dealer se planta** cuando alcanza **entre 17 y 21 puntos**.  
- Si supera 21 puntos, **pierde automáticamente** la ronda.

Esta lógica se implementa en el método `viableCogerCarta()` dentro de la clase `Dealer`, y se ejecuta durante el turno del dealer (`Ronda.turnoDealer()`).

---

### Reparto y visibilidad de cartas

Según las reglas oficiales:

> “El crupier reparte dos cartas visibles a cada jugador. El valor del As es 11 o +1, las figuras valen 10, y las cartas numéricas su valor original.”  
> — [Wikipedia: Blackjack](https://es.wikipedia.org/wiki/Blackjack#:~:text=El%20crupier%20reparte%20dos%20cartas,cartas%20num%C3%A9ricas%20su%20valor%20original.)

En el proyecto:

- **Jugador y dealer reciben dos cartas iniciales.**  
- El **jugador ve una carta visible del dealer** y sus propias dos cartas completas.  
- Los **valores de las cartas** se calculan así:
  - As = 1 o 11 (a elección del jugador, o automáticamente si es el dealer).  
  - J, Q, K = 10 puntos.  
  - Cartas numéricas = su valor natural (2–10).

---

### Fuentes de aprendizaje y apoyo visual

Durante el desarrollo, se utilizaron materiales externos para comprender mejor la dinámica real del juego:

- **Wikipedia – Blackjack:**  
  [https://es.wikipedia.org/wiki/Blackjack](https://es.wikipedia.org/wiki/Blackjack)

- **Vídeo de aprendizaje:**  
  “Cómo jugar al Blackjack (tutorial completo en español)”  
  [https://www.youtube.com/watch?v=x_lLOq1dUt4&pp=ygUSdHV0b3JpYWwgYmxhY2tqYWNr](https://www.youtube.com/watch?v=x_lLOq1dUt4&pp=ygUSdHV0b3JpYWwgYmxhY2tqYWNr)  
  Este vídeo ayudó a comprender la dinámica real del reparto, el turno del jugador y la secuencia del dealer.

- **Simulador de Blackjack (uno contra uno):**  
  [https://www.blackjacksimulator.net/es/](https://www.blackjacksimulator.net/es/)  
  Se utilizó para observar la lógica de decisión del dealer y la estructura práctica de una partida completa.

---

### Aplicación práctica en el código

En el código fuente (`blackjack_models.py`):

- El **dealer** calcula el valor total de su mano mediante el método `valorCartasDealer()`.  
- La función `viableCogerCarta()` determina si el dealer debe pedir una nueva carta, basándose en su puntuación actual y la del jugador.  
- Durante el **turno del dealer**, implementado en `Ronda.turnoDealer()`, el dealer pide cartas automáticamente hasta alcanzar 17 puntos o superar al jugador sin pasarse de 21.  
- Estas decisiones reproducen el comportamiento descrito en las reglas oficiales y en el turno de la banca tradicional.
