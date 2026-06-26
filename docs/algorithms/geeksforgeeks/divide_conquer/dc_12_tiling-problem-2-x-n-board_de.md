# Tiling Problem (2 x N Board)

| | |
|---|---|
| **ID** | `dc_12` |
| **Kategorie** | divide_conquer |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 3/10 |
| **Relevanz für Vorstellungsgespräche** | 5/10 |
| **GeeksForGeeks Äquivalent** | [Tiling Problem](https://www.geeksforgeeks.org/tiling-problem/) |

## Problemstellung

Gegeben ist ein `2 x N` Brett und Kacheln der Größe `2 x 1`. Bestimmen Sie die Anzahl der Möglichkeiten, das gegebene Brett mit diesen Kacheln zu füllen.
Eine Kachel kann entweder horizontal (benötigt `1 x 2` Platz) oder vertikal (benötigt `2 x 1` Platz) platziert werden.
Da das Ergebnis sehr groß sein kann, geben Sie es modulo 10^9 + 7 zurück.

**Eingabe:** Eine Ganzzahl `N`, die die Breite des Bretts repräsentiert.
**Ausgabe:** Eine Ganzzahl, die die Anzahl der Möglichkeiten repräsentiert, das Brett zu füllen.

## Wann man es verwendet

- Um zu erkennen, wann ein geometrisches Divide-and-Conquer-Problem mathematisch in eine einfache Fibonacci-Folge kollabiert.
- Das berühmteste "Trick"-Problem für den Einstieg in Dynamische Programmierung / Rekursion.

## Ansatz

**1. Die Divide-and-Conquer-Entscheidung:**
Stellen Sie sich vor, Sie füllen das Brett von links nach rechts. Sie betrachten aktuell die linke, leere Spalte. Sie haben genau zwei Möglichkeiten, die erste Kachel zu platzieren:
- **Wahl A (Vertikal):** Sie platzieren eine Kachel vertikal. Sie füllt die gesamte erste Spalte perfekt aus. Es verbleibt ein perfekt rechteckiges, leeres Brett der Größe `2 x (N - 1)`.
- **Wahl B (Horizontal):** Sie platzieren eine Kachel horizontal in der oberen linken Ecke. Aber Achtung! Der Platz direkt darunter in der unteren linken Ecke ist nun leer und kann NUR durch eine weitere horizontale Kachel gefüllt werden! Das Platzieren einer horizontalen Kachel zwingt Sie dazu, eine zweite direkt darunter zu platzieren. Dieser `2 x 2`-Block ist nun gefüllt. Es verbleibt ein perfekt rechteckiges, leeres Brett der Größe `2 x (N - 2)`.

**2. Die Rekursionsgleichung:**
Sei f(N) die Anzahl der Möglichkeiten, ein `2 x N` Brett zu füllen.
Basierend auf den obigen Entscheidungen können wir dies mathematisch definieren:
f(N) = f(N - 1) + f(N - 2)

Moment mal... das ist die **Fibonacci-Folge**!

**3. Basisfälle:**
- f(0) = 1: Es gibt genau 1 Möglichkeit, ein leeres Brett zu füllen (nichts tun).
- f(1) = 1: Ein `2 x 1` Brett kann nur mit 1 vertikalen Kachel gefüllt werden.
- f(2) = 2: Ein `2 x 2` Brett kann mit 2 vertikalen oder 2 horizontalen Kacheln gefüllt werden.

**4. Ausführung:**
Wir müssen nicht tatsächlich eine rekursive Divide-and-Conquer-Funktion schreiben (die $O(2^N)$ Zeit benötigen oder $O(N)$ Platz für Memoization erfordern würde). Wir können die N-te Fibonacci-Zahl einfach iterativ unter Verwendung von zwei Variablen in strikt $O(1)$ Platz berechnen!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dc_12: Tiling Problem (2 x N board).

Given a 2 x n board and tiles of size 2 x 1, count
"""


def solve(n):
    """Count the tilings of a 2 x n board with 2 x 1 dominoes.

    T(n) = T(n-1) + T(n-2), T(0) = 1, T(1) = 1 (Fibonacci).
    """
    if n <= 1:
        return 1
    a, b = 1, 1   # T(0), T(1)
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

</details>

## Durchlauf

`n = 4`. `MOD = 10^9 + 7`.
Initial: `prev2 = 1`, `prev1 = 1`.

1. **i = 2:**
   - `current = (1 + 1) % MOD = 2`.
   - `prev2 = 1`, `prev1 = 2`.
2. **i = 3:**
   - `current = (2 + 1) % MOD = 3`.
   - `prev2 = 2`, `prev1 = 3`.
3. **i = 4:**
   - `current = (3 + 2) % MOD = 5`.
   - `prev2 = 3`, `prev1 = 5`.

Das Ergebnis ist `5`. ✓
*(Die 5 Möglichkeiten: VVVV, VVHH, HHVV, VHHV, HHHH).*

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N)$ | $O(1)$ |

Die `for`-Schleife läuft N - 1 Mal und führt einfache Ganzzahladditionen durch. Die Zeitkomplexität ist strikt $O(N)$.
Es werden nur drei Ganzzahlvariablen verwaltet. Die Platzkomplexität ist strikt $O(1)$.

## Varianten & Optimierungen

- **Matrix-Exponentiation ($O(\log N)$):** Wenn N sehr groß ist (z. B. 10^{18}), führt die $O(N)$-Schleife zu einem TLE (Time Limit Exceeded)! Sie können die Fibonacci-Folge als Matrixmultiplikation schreiben: \begin{bmatrix} f(N) \\ f(N-1) \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}^{N-1} x \begin{bmatrix} f(1) \\ f(0) \end{bmatrix}. Sie können dann die schnelle Exponentiation (`dc_01`) auf die Matrix anwenden, um das Problem in exakt $O(\log N)$ Zeit zu lösen!
- **Domino and Tromino Tiling (LeetCode 790):** Was ist, wenn Sie `2x1` Dominosteine UND L-förmige Trominoes verwenden können? Der Zustandsraum verzweigt sich drastisch, da ein L-Tromino eine unregelmäßige Kante hinterlässt, die gefüllt werden muss! Die Rekursionsgleichung wird zu f(N) = 2 x f(N-1) + f(N-3).

## Anwendungen in der Praxis

- **Statistische Mechanik:** Analyse der thermodynamischen Eigenschaften von zweiatomigen Molekülen (Dimeren), die auf einer 2D-Kristallgitteroberfläche adsorbieren (mathematisch bekannt als das "Dimer Covering Problem").

## Verwandte Algorithmen in cOde(n)

- **[dp_01 - Climbing Stairs](../dynamic/dp_01_climbing-stairs.md)** — Die buchstäblich identische Fibonacci-Rekursionsgleichung, nur formuliert als das Nehmen von 1 oder 2 Stufen auf einer Treppe anstatt des Platzierens von Kacheln.
- **[dc_01 - Pow(x, n)](dc_01_power-x-to-the-n.md)** — Erforderlich für die $O(\log N)$ Matrix-Exponentiation-Optimierung.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*