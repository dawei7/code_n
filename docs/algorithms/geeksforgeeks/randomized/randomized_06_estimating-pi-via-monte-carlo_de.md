# Schätzung von Pi mittels Monte-Carlo-Simulation

| | |
|---|---|
| **ID** | `randomized_06` |
| **Kategorie** | randomized |
| **Komplexität (erforderlich)** | $O(N)$ |
| **Schwierigkeit** | 1/10 |
| **Relevanz für Vorstellungsgespräche** | 3/10 |
| **Wikipedia** | [Monte-Carlo-Algorithmus](https://en.wikipedia.org/wiki/Monte_Carlo_method) |

## Problemstellung

Gegeben sei eine Ganzzahl `N`, die die Anzahl der Iterationen repräsentiert. Schätzen Sie die mathematische Konstante \pi (Pi) unter Verwendung rein randomisierter Geometrie.

**Eingabe:** Eine Ganzzahl `N` (z. B. 1.000.000).
**Ausgabe:** Eine Fließkommazahl zur Schätzung von \pi.

## Anwendungsbereich

- Das absolute "Hello World" der Monte-Carlo-Simulationen.
- Dient dazu, zu lehren, wie probabilistisches Sampling komplexe mathematische Integrale approximieren kann, die analytisch zu schwer zu lösen sind.

## Ansatz

Stellen Sie sich ein Quadrat mit der Seitenlänge 2 vor, das am Ursprung `(0, 0)` zentriert ist.
Der Flächeninhalt dieses Quadrats beträgt 2 x 2 = 4.
Zeichnen Sie nun einen Kreis mit dem Radius 1, der ebenfalls am Ursprung `(0, 0)` zentriert ist. Dieser Kreis berührt die Kanten des Quadrats exakt.
Der Flächeninhalt dieses Kreises beträgt \pi \cdot r^2 = \pi \cdot 1^2 = \pi.

Das Verhältnis des Flächeninhalts des Kreises zum Flächeninhalt des Quadrats ist exakt \frac{\pi}{4}.

**Die Monte-Carlo-Methode:**
Wenn wir Millionen von komplett zufälligen Punkten generieren, die gleichmäßig innerhalb des Quadrats verteilt sind, wird ein gewisser Prozentsatz davon innerhalb des Kreises landen.
Statistisch gesehen konvergiert das Verhältnis von (Punkte innerhalb des Kreises) / (Gesamtanzahl der Punkte) exakt gegen das Verhältnis ihrer Flächeninhalte!

\frac{\text{Punkte innerhalb}}{\text{Gesamtanzahl der Punkte}} ~= \frac{\text{Fläche Kreis}}{\text{Fläche Quadrat}} = \frac{\pi}{4}

Daraus folgt:
\pi ~= 4 x \frac{\text{Punkte innerhalb}}{\text{Gesamtanzahl der Punkte}}

**Wie prüft man, ob ein Punkt innerhalb des Kreises liegt?**
Unter Verwendung des Satzes des Pythagoras liegt ein Punkt `(x, y)` innerhalb des Einheitskreises, wenn sein Abstand vom Ursprung `(0, 0)` kleiner oder gleich dem Radius `1` ist.
x^2 + y^2 \le 1^2

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for randomized_06: Estimating Pi via Monte Carlo.

Estimate the value of pi using the Monte Carlo
"""


def solve(n, seed_value):
    """Estimate pi via Monte Carlo: count points (x, y) in
    [0, 1]^2 with x^2 + y^2 <= 1, return 4 * (count / n)."""
    import random
    rng = random.Random(seed_value)
    inside = 0
    for _ in range(n):
        x = rng.random()
        y = rng.random()
        if x * x + y * y <= 1.0:
            inside += 1
    return 4.0 * inside / n
```

</details>

## Durchlauf

`iterations = 4`

1. Zufälliger Punkt: `(0.5, 0.5)`. 0.5^2 + 0.5^2 = 0.25 + 0.25 = 0.5. `0.5 <= 1`. Innerhalb! `points = 1`.
2. Zufälliger Punkt: `(0.9, 0.9)`. 0.9^2 + 0.9^2 = 0.81 + 0.81 = 1.62. `1.62 > 1`. Außerhalb. `points = 1`.
3. Zufälliger Punkt: `(-0.1, 0.2)`. 0.01 + 0.04 = 0.05. Innerhalb! `points = 2`.
4. Zufälliger Punkt: `(0.8, -0.8)`. 0.64 + 0.64 = 1.28. Außerhalb. `points = 2`.

Schätzung = 4 x (2 / 4) = 2.0.
*(Extrem ungenau, da N=4, aber bei N=10^6 nähert es sich schnell 3.14159 an).*

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N)$ | $O(1)$ |

Die Schleife läuft exakt N-mal und führt dabei $O(1)$ arithmetische Operationen aus. Die Zeitkomplexität beträgt $O(N)$.
Es werden lediglich Ganzzahl-Zähler verwaltet. Die Platzkomplexität beträgt $O(1)$.

## Varianten & Optimierungen

- **Optimierung für den ersten Quadranten:** Da ein Kreis perfekt symmetrisch ist, muss man nur den oberen rechten Quadranten simulieren. Generieren Sie `x` und `y` zwischen `0.0` und `1.0`. Die Mathematik und die Verhältnisse bleiben identisch, aber das Generieren positiver Fließkommazahlen kann in einigen Sprachen geringfügig schneller sein.
- **Ray Tracing:** Monte-Carlo-Pfadverfolgung in modernen Videospielen nutzt genau diese probabilistische Logik, um Licht zu simulieren, das in einer Szene reflektiert wird. Anstatt die unendliche Komplexität von Milliarden von Photonen zu berechnen, werden einige hundert zufällige Strahlen pro Pixel ausgesendet und deren Farben gemittelt!

## Praxisanwendungen

- **Finanzrisikomodellierung:** Preisgestaltung exotischer Derivate (wie asiatische Optionen), bei denen die Auszahlung von der gesamten Historie des Aktienkurses abhängt, was analytisch unmöglich zu berechnen, aber mittels Monte-Carlo-Simulation stochastisch leicht zu simulieren ist.

## Verwandte Algorithmen in cOde(n)

- **[randomized_05 - Karger's Min-Cut](randomized_05_karger-s-min-cut-monte-carlo.md)** — Eine weitere Anwendung des Monte-Carlo-Paradigmas, angewandt auf Graphen anstelle von Geometrie.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für Wettbewerbsprogrammierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*