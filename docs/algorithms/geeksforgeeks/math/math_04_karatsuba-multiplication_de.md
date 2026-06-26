# Karatsuba-Multiplikation

| | |
|---|---|
| **ID** | `math_04` |
| **Kategorie** | math |
| **Komplexität (erforderlich)** | $O(N^{1.58})$ Zeit, $O(\log N)$ Platz |
| **Schwierigkeit** | 8/10 |
| **Relevanz für Vorstellungsgespräche** | 2/10 |
| **Wikipedia** | [Karatsuba-Algorithmus](https://en.wikipedia.org/wiki/Karatsuba_algorithm) |

## Problemstellung

Gegeben sind zwei massiv große Ganzzahlen X und Y mit N Ziffern. Berechnen Sie deren Produkt X x Y.
Die standardmäßige schriftliche Multiplikation benötigt $O(N^2)$ Zeit.
Optimieren Sie dies unter Verwendung des Divide-and-Conquer-Ansatzes von Anatoly Karatsuba.

**Eingabe:** Zwei Ganzzahlen X und Y (oder String-Repräsentationen massiver Zahlen).
**Ausgabe:** Eine Ganzzahl (oder ein String), die ihr Produkt repräsentiert.

## Wann ist dieser Algorithmus zu verwenden?

- Wenn zwei Zahlen multipliziert werden sollen, die die standardmäßigen 64-Bit-Grenzen überschreiten (z. B. 10.000 Ziffern lang), und dies schneller als mit dem Brute-Force-Ansatz mittels verschachtelter Schleifen geschehen soll.
- *Trivia:* Dieser 1960 entdeckte Algorithmus war der ERSTE Multiplikationsalgorithmus, der nachweislich asymptotisch schneller ist als die in der Schule gelehrte $O(N^2)$-Methode!

## Ansatz

**1. Der Divide-Schritt:**
Angenommen, wir möchten zwei 4-stellige Zahlen multiplizieren: X = 1234 und Y = 5678.
Wir können sie in der Mitte in 2-stellige Hälften teilen:
X = 12 \cdot 10^2 + 34 -> X = A \cdot 10^m + B
Y = 56 \cdot 10^2 + 78 -> Y = C \cdot 10^m + D
Wobei m = N / 2 (die Hälfte der Ziffern).

**2. Die Standard-Expansion ($O(N^2)$):**
Wenn wir sie algebraisch multiplizieren:
X x Y = (A \cdot 10^m + B) x (C \cdot 10^m + D)
X x Y = AC \cdot 10^{2m} + (AD + BC) \cdot 10^m + BD

Um dies zu lösen, müssen wir VIER separate rekursive Multiplikationen berechnen:
1. AC
2. AD
3. BC
4. BD
Da T(N) = 4T(N/2) + $O(N)$, ergibt das Master-Theorem $O(N^2)$. Wir haben also keine Verbesserung erzielt!

**3. Die Karatsuba-Erkenntnis (Der magische Schritt):**
Karatsuba erkannte, dass wir AD und BC gar nicht separat berechnen müssen! Uns interessiert nur ihre SUMME: (AD + BC).
Was passiert, wenn wir die Summe der Hälften miteinander multiplizieren?
(A+B) x (C+D) = AC + AD + BC + BD

Beachten Sie, dass dieses neue Produkt genau den Mittelterm (AD + BC) enthält, den wir benötigen, plus AC und BD, die wir ohnehin bereits berechnen müssen!
Daher können wir den Mittelterm durch Subtraktion isolieren:
(AD + BC) = (A+B) x (C+D) - AC - BD

Wir benötigen nun nur noch DREI rekursive Multiplikationen anstelle von vier:
1. Z_2 = AC
2. Z_0 = BD
3. Z_1 = (A+B) x (C+D)
Der Mittelterm ist einfach Z_1 - Z_2 - Z_0.
Die finale Gleichung lautet:
X x Y = Z_2 \cdot 10^{2m} + (Z_1 - Z_2 - Z_0) \cdot 10^m + Z_0

Da T(N) = 3T(N/2) + $O(N)$, ergibt das Master-Theorem $O(N^{log_2 3})$ ~= $O(N^{1.585})$.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for math_04: Karatsuba Multiplication.

Recursive divide and conquer: split each number into halves,
compute 3 half-sized products (instead of 4), combine.
"""


def solve(x, y):
    if x < 10 or y < 10:
        return x * y
    n = max(len(str(x)), len(str(y)))
    half = n // 2
    power = 10 ** half
    a, b = divmod(x, power)
    c, d = divmod(y, power)
    ac = solve(a, c)
    bd = solve(b, d)
    ad_bc = solve(a + b, c + d) - ac - bd
    return ac * (10 ** (2 * half)) + ad_bc * power + bd
```

</details>

## Durchlauf

X = 1234, Y = 5678. N=4, m=2.
A = 12, B = 34.
C = 56, D = 78.

1. Berechne Z_2 = AC = 12 x 56 = 672.
2. Berechne Z_0 = BD = 34 x 78 = 2652.
3. Berechne Z_1 = (A+B) x (C+D) = (46) x (134) = 6164.
4. Berechne den Mittelterm: Z_1 - Z_2 - Z_0 = 6164 - 672 - 2652 = 2840.

Zusammenfügen:
= 672 x 10^4 + 2840 x 10^2 + 2652
= 6720000 + 284000 + 2652
= 7006652.

Überprüfung: 1234 x 5678 = 7006652. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N^{\log_2 3})$ | $O(\log N)$ |
| **Durchschnittlicher Fall** | $O(N^{\log_2 3})$ \approx $O(N^{1.58})$ | $O(\log N)$ |
| **Schlechtester Fall** | $O(N^{\log_2 3})$ | $O(\log N)$ |

Durch die Reduzierung von 4 rekursiven Zweigen auf 3 sinkt die Zeitkomplexität gemäß dem Master-Theorem von $O(N^2)$ auf $O(N^{1.58})$.
Obwohl 1.58 nicht viel kleiner als 2.0 erscheint, sind bei einer 10.000-stelligen Zahl $O(N^2)$ etwa 100.000.000 Operationen, während $O(N^{1.58})$ kaum 2.100.000 Operationen erfordert (eine 50-fache Beschleunigung).
Die Platzkomplexität ist durch die Tiefe des Rekursions-Stacks begrenzt, der N bei jedem Schritt halbiert, was $O(\log N)$ Platz ergibt.

## Varianten & Optimierungen

- **Toom-Cook-Multiplikation:** Karatsuba teilt die Zahl in 2 Teile (reduziert 4 Multiplikationen auf 3). Toom-3 teilt die Zahl in 3 Teile (reduziert 9 Multiplikationen auf 5), was $O(N^{1.46})$ ergibt. Toom-Cook kann in eine beliebige Anzahl K von Teilen zerlegen.
- **Schönhage-Strassen-Algorithmus:** Für astronomisch große Zahlen (z. B. Millionen von Ziffern) wird die Fast Fourier Transform (FFT) verwendet, um Zahlen in $O(N log N log(log N)$) Zeit zu multiplizieren!

## Anwendungen in der Praxis

- **Interne Integer-Engine von Python:** Python unterstützt nativ beliebig große Ganzzahlen. Wenn Sie zwei Zahlen multiplizieren, die kleiner als 70 Dezimalstellen sind, verwendet Python unter der Haube die $O(N^2)$-Schulmathematik. Sobald die Zahlen jedoch die 70-Stellen-Grenze überschreiten, schaltet das C-Backend von Python automatisch auf den Karatsuba-Algorithmus um!

## Verwandte Algorithmen in cOde(n)

- **[math_05 - Big Integer Addition](math_05_big-integer-add-strings.md)** — Die stringbasierte Additionslogik, die zwingend erforderlich ist, um Karatsuba in Sprachen zu implementieren, die keine native Unterstützung für Ganzzahlen mit unendlicher Präzision bieten.
- **[divide_conquer_04 - Merge Sort](../divide_conquer/dc_04_merge-sort.md)** — Das klassische rekursive "Teile und Herrsche"-Paradigma, das Karatsuba sich zunutze macht.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*