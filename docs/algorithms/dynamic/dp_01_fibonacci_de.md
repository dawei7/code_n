# Fibonacci

| | |
|---|---|
| **ID** | `dp_01` |
| **Kategorie** | dynamisch |
| **Komplexität (erforderlich)** | $O(n)$ |
| **Schwierigkeitsgrad** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **Wikipedia** | [Fibonacci-Folge](https://en.wikipedia.org/wiki/Fibonacci_sequence) |

## Aufgabenstellung

Berechne die *n*-te Fibonacci-Zahl. Die Fibonacci-Folge ist
definiert durch:

```
F(0) = 0,  F(1) = 1
F(n) = F(n-1) + F(n-2)   for n >= 2
```

Die ersten paar Werte sind `0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...`.

**Eingabe:** eine nicht-negative ganze Zahl `n`.
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

- Als **pädagogische Einführung in die dynamische Programmierung**: Es
  hat den kleinstmöglichen Zustand (`prev`, `curr`) und die
  am leichtesten erkennbare Rekursion. Interviewer nutzen es, um zu prüfen, ob
  Sie die richtige DP-Form erkennen können (Top-Down-Memoisation
  vs. Bottom-Up-Tabellierung vs. $O(1)$-Space-Rolling).
- Zur Einführung des **Kontrasts zwischen naiver und zwischengespeicherter Variante**: Die wörtliche
  rekursive Formulierung lautet $O(2^n)$ und erschöpft den Aufrufstapel
  etwa bei `n=50`; der gleiche Code mit Memoisation lautet $O(n)$.
- Als **Quelle großer Zahlen für Testzwecke**: Bei `n=1000`
  ist `F(n)` eine 209-stellige Ganzzahl, sodass sie sich ideal für
  Folgeuntersuchungen zu „big-int“ oder modularer Arithmetik eignet.

Verwende sie nicht in Produktionscode – die naive Rekursion ist
katastrophal langsam, und die geschlossene Form (Binetsche Formel)
verliert bei `n > 70` an Genauigkeit.

## Vorgehensweise

Die naive rekursive Definition `F(n) = F(n-1) + F(n-2)`
berechnet dasselbe Teilproblem exponentiell oft neu:
`F(2)` wird für jedes Blatt im Rekursionsbaum einmal neu berechnet.

**Memoisation** (Top-Down-DP) speichert jeden berechneten Wert in einer
Tabelle, die nach `n` indiziert ist. Der erste Aufruf von `F(k)` berechnet diesen Wert; alle
folgenden Aufrufe sind $O(1)$-Nachschläge. Dadurch wird die Rekursion
von $O(2^n)$ in $O(n)$ Zeit und $O(n)$ Speicherplatz umgewandelt.

**Tabellierung** (Bottom-up-DP) beginnt mit den kleinsten
Teilproblemen (`F(0)`, `F(1)`) und arbeitet sich bis zu `F(n)` vor, wobei
eine Tabelle gefüllt wird. Gleiche $O(n)$-Zeit, $O(n)$-Speicherplatz.

**Rolling / $O(1)$-Raum** berücksichtigt, dass `F(n)` nur von
den beiden vorherigen Werten abhängt, sodass sich die gesamte Tabelle auf
zwei Variablen `prev` und `curr` reduzieren lässt. Jede Iteration:
`prev, curr = curr, prev + curr`. Dies ist die Produktionsimplementierung
und diejenige, gegen die die Engine von cOde(n) prüft
(die erforderliche Komplexität beträgt $O(n)$).

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

## Schritt-für-Schritt-Anleitung

Berechne `F(6)`:

| Iteration | i | prev | curr | next = prev + curr |
|---|---:|---:|---:|---:|
| init | — | 0 | 1 | — |
| 1 | 2 | 0 | 1 | 1 |
| 2 | 3 | 1 | 1 | 2 |
| 3 | 4 | 1 | 2 | 3 |
| 4 | 5 | 2 | 3 | 5 |
| 5 | 6 | 3 | 5 | 8 |

Nach `i = 6` folgt `curr = 8`, was `F(6)` ist. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ — `n < 2` Kurzschluss |
| **Durchschnittlicher Fall** | $O(n)$ | $O(1)$ |
| **Schlechtester Fall** | $O(n)$ | $O(1)$ |

Die Rekursionsformel lautet `T(n) = T(n-1) + O(1)`, was zu
$O(n)$ führt. Der Speicherbedarf beträgt $O(1)$ in der „Rolling“-Implementierung; $O(n)$ in
den memoisierten/tabellierten Varianten.

## Varianten & Optimierungen

- **Naive Rekursion** — `def f(n): return f(n-1) + f(n-2) if n > 1 else n`.
  $O(2^n)$ Zeit, $O(n)$ Stapelplatz. **Reichen Sie dies nicht in
  Vorstellungsgesprächen ein**, aber erwähnen Sie es als Gegenbeispiel, um zu zeigen, dass Sie
  die Optimierung verstehen.
- **Memoized Rekursion** — Top-Down mit einem Dict. $O(n)$ Zeit, $O(n)$
  Speicherplatz. Nützlich, wenn nicht alle Teilprobleme benötigt werden.
- **Matrixpotenzierung** — `[[1,1],[1,0]]^n` ergibt
  `F(n+1)` in $O(log n)$ Zeit. Die richtige Lösung, wenn das Problem
  viele Abfragen erfordert und `n` groß ist.
- **Verdopplungsidentitäten** — `F(2k) = F(k) * (2*F(k+1) - F(k))`,
  `F(2k+1) = F(k+1)^2 + F(k)^2`. In Kombination mit schneller Potenzierung
  ergibt dies eine Laufzeit von $O(log n)$ und ist der Standard für sehr große `n`
  (z. B. `n = 10^18`).

## Praktische Anwendungen

- **Fibonacci-Suche** — ein Suchalgorithmus für sortierte Arrays,
  der anstelle der Halbierung bei der binären Suche Fibonacci-Zahlen verwendet.
  Auf manchen Hardwareplattformen geringfügig schneller als die binäre Suche, da
  er den `(low+high)//2`-Überlauf vermeidet.
- **Fibonacci-Heap** – eine Priority Queue mit $O(1)$ amortisiertem
  Einfügen und $O(log n)$ Extrahieren des Minimalwerts. Wird in einigen Implementierungen von
  Kürzestweg- und Minimal-Spanning Tree-Algorithmen verwendet.
- **Finanzkennzahlen** — Fibonacci-Retracement-Niveaus (23,6 %,
  38,2 %, 61,8 %) werden in der technischen Aktienanalyse verwendet. (Es lohnt sich,
  zu wissen, dass es sie gibt; wissenschaftlich nicht fundiert.)
- **Rätsel zur modularen Arithmetik** — `F(n) mod m` ist eine klassische
  Aufwärmübung bei Programmierwettbewerben, die den sorgfältigen Umgang
  mit großen `n` und Periodizität (Pisano-Periode) erfordert.

## Verwandte Algorithmen in cOde(n)

- **[dp_02 — Treppensteigen](dp_02_climbing-stairs.md)** — gleiche
  Rekursionsform (`F(n) = F(n-1) + F(n-2)`), andere
  Rahmung. (d=5/10, r=9/10)
- **[dp_11 – Einbrecher](dp_11_house-robber.md)** – Ausschluss
  benachbarter Elemente, ebenfalls eine rollierende DP mit zwei Zuständen. (d=5/10, r=9/10)
- **[dp_23 – Treppensteigen mit minimalen Kosten](dp_23_min-cost-climbing-stairs.md)** –
  gleiche Fibonacci-förmige Rekursion mit einer Kostendimension.
  (d=3/10, r=9/10)

---

*Diese Dokumentation ist ein Originalbeitrag für cOde(n),
der sich an der kanonischen Struktur orientiert, die von Referenzseiten
zum Thema Wettbewerbsprogrammierung verwendet wird. Den kanonischen
Enzyklopädieeintrag finden Sie über den Wikipedia-Link oben auf der Seite.
Quell-Repository: <https://github.com/dawei7/code_n>.*
