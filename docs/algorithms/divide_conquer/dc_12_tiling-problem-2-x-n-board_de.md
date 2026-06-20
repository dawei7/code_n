# Fliesenproblem (2 x N-Spielfeld)

| | |
|---|---|
| **ID** | `dc_12` |
| **Kategorie** | divide_conquer |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(1)$ Speicherplatz |
| **Schwierigkeitsgrad** | 3/10 |
| **Relevanz für Vorstellungsgespräche** | 5/10 |
| **GeeksForGeeks-Äquivalent** | [Kachelproblem](https://www.geeksforgeeks.org/tiling-problem/) |

## Aufgabenstellung

Gegeben sind ein `2 x N`-Spielfeld und Kacheln der Größe `2 x 1`. Bestimme die Anzahl der Möglichkeiten, das gegebene Spielfeld mit diesen Kacheln zu bedecken.
Ein Kachelstück kann entweder horizontal (und nimmt dabei `1 x 2` Platz ein) oder vertikal (und nimmt dabei `2 x 1` Platz ein) platziert werden.
Da das Ergebnis sehr groß sein kann, gib es modulo 10^9 + 7 zurück.

**Eingabe:** Eine ganze Zahl `N`, die die Breite des Spielbretts angibt.
**Ausgabe:** Eine ganze Zahl, die die Anzahl der Möglichkeiten angibt, das Spielbrett zu bedecken.

## Wann man dies anwenden sollte

- Um zu erkennen, wann sich ein räumliches „Teile und herrsche“-Geometrieproblem mathematisch auf eine einfache Fibonacci-Folge reduzieren lässt.
- Das bekannteste „Trick“-Problem zur Einführung in dynamische Programmierung und Rekursion.

## Vorgehensweise

**1. Die „Teile und herrsche“-Entscheidung:**
Stell dir vor, du füllst das Spielfeld von links nach rechts. Du betrachtest gerade die linkeste leere Spalte. Sie haben genau zwei Möglichkeiten, wie Sie die erste Kachel platzieren können:
- **Möglichkeit A (vertikal):** Sie platzieren eine Kachel vertikal. Sie füllt die gesamte erste Spalte perfekt aus. Sie haben nun ein perfekt rechteckiges, leeres Spielfeld der Größe `2 x (N - 1)`.
- **Option B (horizontal):** Sie platzieren einen Stein horizontal in der oberen linken Ecke. Aber Moment! Der Platz direkt darunter in der unteren linken Ecke ist nun leer und kann NUR durch einen weiteren horizontalen Stein gefüllt werden! Das Platzieren eines horizontalen Steins zwingt dich dazu, einen zweiten direkt darunter zu platzieren. Dieser `2 x 2`-Block ist nun gefüllt. Du hast nun ein perfekt rechteckiges, leeres Spielfeld der Größe `2 x (N - 2)`.

**2. Die Rekursionsbeziehung:**
Sei f(N) die Anzahl der Möglichkeiten, ein `2 x N`-Spielfeld zu verlegen.
Aus den obigen Möglichkeiten lässt sich dies mathematisch definieren:
f(N) = f(N - 1) + f(N - 2)

Moment mal … das ist doch die **Fibonacci-Folge**!

**3. Grenzfälle:**
- f(0) = 1: Es gibt genau eine Möglichkeit, ein leeres Spielfeld zu verlegen (nichts tun).
- f(1) = 1: Ein `2 x 1`-Spielfeld kann nur mit 1 vertikaler Kachel bedeckt werden.
- f(2) = 2: Ein `2 x 2`-Spielfeld kann mit 2 vertikalen Kacheln oder 2 horizontalen Kacheln bedeckt werden.

**4. Ausführung:**
Wir müssen keine rekursive „Teile und herrsche“-Funktion schreiben (die $O(2^N)$ Zeit in Anspruch nehmen oder $O(N)$ Memoization-Speicherplatz erfordern würde). Wir können die N-te Fibonacci-Zahl einfach iterativ mit zwei Variablen in streng $O(1)$ Speicherplatz berechnen!

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

## Schritt-für-Schritt-Anleitung

`n = 4`. `MOD = 10^9 + 7`.
Anfangswerte: `prev2 = 1`, `prev1 = 1`.

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
| **Bestwert** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N)$ | $O(1)$ |

Die `for`-Schleife wird N - 1 Mal durchlaufen und führt einfache Ganzzahladditionen durch. Die Zeitkomplexität beträgt streng $O(N)$.
Es werden nur drei Ganzzahlvariablen verwaltet. Die Platzkomplexität beträgt streng $O(1)$.

## Varianten & Optimierungen

- **Matrixpotenzierung ($O(\log N)$):** Wenn N sehr groß ist (z. B. 10^{18}), löst die $O(N)$-Schleife einen TLE aus! Man kann die Fibonacci-Folge als Matrixmultiplikation schreiben: \begin{bmatrix} f(N) \\ f(N-1) \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}^{N-1} x \begin{bmatrix} f(1) \\ f(0) \end{bmatrix}. Anschließend kannst du die schnelle Potenzierung (`dc_01`) auf die Matrix anwenden, um sie in genau $O(\log N)$ Zeit zu lösen!
- **Domino- und Tromino-Verlegung (LeetCode 790):** Was wäre, wenn man `2x1` Dominosteine UND L-förmige Trominos verwenden könnte? Der Zustandsbaum verzweigt sich drastisch, da ein L-Tromino eine unregelmäßige Kante hinterlässt, die gefüllt werden muss! Die Rekursionsbeziehung lautet nun f(N) = 2 x f(N-1) + f(N-3).

## Anwendungen in der Praxis

- **Statistische Mechanik:** Analyse der thermodynamischen Eigenschaften von zweiatomigen Molekülen (Dimeren), die sich an einer 2D-Kristallgitteroberfläche anlagern (mathematisch bekannt als das „Dimer-Covering-Problem“).

## Verwandte Algorithmen in cOde(n)

- **[dp_01 – Treppensteigen](../dynamic/dp_01_climbing-stairs.md)** — Es handelt sich um genau dieselbe Fibonacci-Rekursionsbeziehung, nur dass hier anstelle des Platzierens von Kacheln das Hinaufsteigen von 1 oder 2 Stufen auf einer Treppe betrachtet wird.
- **[dc_01 - Pow(x, n)](dc_01_power-x-to-the-n.md)** — Erforderlich für die Optimierung der Matrixpotenzierung $O(\log N)$.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde
und sich an der kanonischen Struktur orientiert, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
