# Fibonacci

| | |
|---|---|
| **ID** | `dp_01` |
| **Kategorie** | dynamic |
| **Komplexität (erforderlich)** | $O(n)$ |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **Wikipedia** | [Fibonacci-Folge](https://en.wikipedia.org/wiki/Fibonacci_sequence) |

## Problemstellung

Berechne die *n*-te Fibonacci-Zahl. Die Fibonacci-Folge ist wie folgt definiert:

```
F(0) = 0,  F(1) = 1
F(n) = F(n-1) + F(n-2)   for n >= 2
```

Die ersten Werte lauten `0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...`.

**Eingabe:** eine nicht-negative Ganzzahl `n`.
**Ausgabe:** `F(n)`.

**Beispiel:**

| Eingabe | Ausgabe |
|---|---|
| 0 | 0 |
| 1 | 1 |
| 2 | 1 |
| 10 | 55 |
| 30 | 832040 |

## Wann man es verwendet

- Als **pädagogische Einführung in die dynamische Programmierung**: Sie besitzt den kleinstmöglichen Zustand (`prev`, `curr`) und die am leichtesten erkennbare Rekurrenz. Interviewer nutzen sie, um zu prüfen, ob man die richtige DP-Struktur erkennt (Top-Down-Memoization vs. Bottom-Up-Tabulation vs. $O(1)$-Platzkomplexität durch Rolling-Technik).
- Um den **Kontrast zwischen naiv und zwischengespeichert (cached)** zu verdeutlichen: Die wörtliche rekursive Formulierung ist $O(2^n)$ und erschöpft den Call Stack bei etwa `n=50`; derselbe Code mit Memoization ist $O(n)$.
- Als **Erzeuger großer Zahlen für Tests**: Bei `n=1000` ist `F(n)` eine 209-stellige Ganzzahl, daher eignet es sich hervorragend für Aufgaben zu Big-Int oder modularer Arithmetik.

Verwenden Sie es nicht in Produktivcode — die naive Rekursion ist katastrophal langsam, und die geschlossene Form (Binet-Formel) verliert bei `n > 70` an Präzision.

## Ansatz

Die naive rekursive Definition `F(n) = F(n-1) + F(n-2)` berechnet dasselbe Teilproblem exponentiell oft neu: `F(2)` wird für jedes Blatt im Rekursionsbaum einmal neu berechnet.

**Memoization** (Top-Down-DP) speichert jeden berechneten Wert in einer Tabelle, die mit `n` indiziert ist. Der erste Aufruf von `F(k)` berechnet den Wert; alle nachfolgenden Aufrufe sind $O(1)$-Zugriffe. Dies reduziert die Rekursion von $O(2^n)$ auf $O(n)$ Zeitkomplexität und $O(n)$ Platzkomplexität.

**Tabulation** (Bottom-Up-DP) beginnt bei den kleinsten Teilproblemen (`F(0)`, `F(1)`) und arbeitet sich bis `F(n)` hoch, wobei eine Tabelle gefüllt wird. Dies ergibt ebenfalls $O(n)$ Zeitkomplexität und $O(n)$ Platzkomplexität.

**Rolling / $O(1)$-Platzkomplexität** nutzt die Beobachtung, dass `F(n)` nur von den zwei vorherigen Werten abhängt, sodass die gesamte Tabelle auf zwei Variablen `prev` und `curr` reduziert werden kann. In jeder Iteration gilt: `prev, curr = curr, prev + curr`. Dies ist die Implementierung für den Produktionseinsatz und diejenige, gegen die die Engine von cOde(n) prüft (die erforderliche Komplexität ist $O(n)$).

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dp_01: Fibonacci.

Compute the n-th Fibonacci number bottom-up. O(n) time, O(1)
space.
"""


def solve(n):
    if n <= 1:
        return n
    previous, current = 0, 1
    for _ in range(2, n + 1):
        previous, current = current, previous + current
    return current
```

</details>

## Durchlauf

Berechne `F(6)`:

| Iteration | i | prev | curr | next = prev + curr |
|---|---:|---:|---:|---:|
| init | — | 0 | 1 | — |
| 1 | 2 | 0 | 1 | 1 |
| 2 | 3 | 1 | 1 | 2 |
| 3 | 4 | 1 | 2 | 3 |
| 4 | 5 | 2 | 3 | 5 |
| 5 | 6 | 3 | 5 | 8 |

Nach `i = 6` ist `curr = 8`, was `F(6)` entspricht. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ — `n < 2` Short-Circuit |
| **Durchschnittlicher Fall** | $O(n)$ | $O(1)$ |
| **Schlechtester Fall** | $O(n)$ | $O(1)$ |

Die Rekurrenz lautet `T(n) = T(n-1) + O(1)`, was zu $O(n)$ führt. Die Platzkomplexität beträgt $O(1)$ bei der Rolling-Implementierung; $O(n)$ bei den memoisierten/tabulierten Varianten.

## Varianten & Optimierungen

- **Naive Rekursion** — `def f(n): return f(n-1) + f(n-2) if n > 1 else n`.
  $O(2^n)$ Zeitkomplexität, $O(n)$ Stack-Platzkomplexität. **Reichen Sie dies nicht in Vorstellungsgesprächen ein**, aber erwähnen Sie es als Kontrast, um zu zeigen, dass Sie die Optimierung verstehen.
- **Memoized Rekursion** — Top-Down mit einem Dictionary. $O(n)$ Zeitkomplexität, $O(n)$ Platzkomplexität. Nützlich, wenn nicht alle Teilprobleme benötigt werden.
- **Matrix-Exponentiation** — `[[1,1],[1,0]]^n` ergibt `F(n+1)` in $O(log n)$ Zeitkomplexität. Die richtige Antwort, wenn das Problem viele Anfragen stellt und `n` groß ist.
- **Verdopplungsidentitäten** — `F(2k) = F(k) * (2*F(k+1) - F(k))`,
  `F(2k+1) = F(k+1)^2 + F(k)^2`. In Kombination mit schneller Exponentiation ergibt dies $O(log n)$ Zeitkomplexität und ist der Standard für sehr große `n` (z. B. `n = 10^18`).

## Anwendungen in der Praxis

- **Fibonacci-Suche** — ein Suchalgorithmus auf sortierten Arrays, der Fibonacci-Zahlen anstelle der Halbierung der binären Suche verwendet. Auf mancher Hardware geringfügig schneller als die binäre Suche, da ein Überlauf bei `(low+high)//2` vermieden wird.
- **Fibonacci-Heap** — eine Priority Queue mit $O(1)$ amortisiertem Einfügen und $O(log n)$ für `extract-min`. Wird in einigen Implementierungen für kürzeste Pfade und minimale Spannbäume verwendet.
- **Finanzkennzahlen** — Fibonacci-Retracement-Level (23,6 %, 38,2 %, 61,8 %) werden in der technischen Aktienanalyse verwendet. (Gut zu wissen, dass es sie gibt; wissenschaftlich nicht robust.)
- **Rätsel zur modularen Arithmetik** — `F(n) mod m` ist ein Standard-Aufwärmtraining bei Programmierwettbewerben, das einen sorgfältigen Umgang mit großen `n` und Periodizität (Pisano-Periode) erfordert.

## Verwandte Algorithmen in cOde(n)

- **[dp_02 — Climbing Stairs](dp_02_climbing-stairs.md)** — gleiche Rekurrenzform (`F(n) = F(n-1) + F(n-2)`), anderer Kontext. (d=5/10, r=9/10)
- **[dp_11 — House Robber](dp_11_house-robber.md)** — Ausschluss benachbarter Elemente, ebenfalls eine 2-Zustands-Rolling-DP. (d=5/10, r=9/10)
- **[dp_23 — Min Cost Climbing Stairs](dp_23_min-cost-climbing-stairs.md)** —
  gleiche Fibonacci-artige Rekurrenz mit einer Kostendimension.
  (d=3/10, r=9/10)

---

*Diese Dokumentation ist ein Originalinhalt für cOde(n), modelliert nach der kanonischen Struktur, die von Referenzseiten für Wettbewerbsprogrammierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*