# Treppensteigen

| | |
|---|---|
| **ID** | `dp_02` |
| **Kategorie** | dynamisch |
| **Komplexität (erforderlich)** | $O(n)$ |
| **Schwierigkeitsgrad** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **Wikipedia** | [Fibonacci-Folge](https://en.wikipedia.org/wiki/Fibonacci_sequence) (gleiche Rekursion) |

## Aufgabenstellung

Du befindest dich am Fuß einer Treppe mit `n` Stufen. Du kannst
**jeweils 1 oder 2 Stufen** hinaufsteigen. Auf wie viele verschiedene Arten kannst
du die oberste Stufe erreichen?

**Eingabe:** eine ganze Zahl `n >= 0` (die Anzahl der Stufen).
**Ausgabe:** die Anzahl der verschiedenen Wege, um die oberste Stufe zu erreichen,
modulo 0 (oder modulo `10^9 + 7` in der schwierigeren Variante).

**Beispiel:**

| n | Möglichkeiten | Erklärung |
|---:|---:|---|
| 0 | 1 | Eine Möglichkeit: an Ort und Stelle bleiben. (Konvention für Randfälle.) |
| 1 | 1 | Ein Schritt. |
| 2 | 2 | `1+1` oder `2`. |
| 3 | 3 | `1+1+1`, `1+2`, `2+1`. |
| 4 | 5 | `1+1+1+1`, `1+1+2`, `1+2+1`, `2+1+1`, `2+2`. |
| 5 | 8 | (Wieder Fibonacci.) |

Die Folge `1, 1, 2, 3, 5, 8, 13, ...` ist genau die Fibonacci-Folge.

## Wann man sie verwendet

- Das klassische **erste DP-Problem** in den meisten Büchern zur Vorbereitung auf Vorstellungsgespräche
  . Der Zustand und die Rekursion sind offensichtlich, und der einzige
  Kniff besteht darin, die Optimierung durch den Raum mit rollierenden Variablen zu erkennen.
- Als **Aufwärmübung zum Erkennen von Fibonacci-Folgen**: Viele Probleme vom Typ „Du kannst
  Sache A oder Sache B in k Schritten tun“ lassen sich auf eine Fibonacci-
  Rekursion zurückführen.
- Die Verallgemeinerung „k Schritte auf einmal“ (1, 2, … oder k
  Schritte) lässt sich auf die k-Bonacci-Folge verallgemeinern und ist eine
  naheliegende Fortsetzung.

## Vorgehensweise

Sei `f(n)` die Anzahl der Möglichkeiten, `n` Stufen zu erklimmen. Der letzte
Schritt, den du machst, ist entweder ein 1-Schritt (wobei noch `n-1` Stufen übrig bleiben) oder
ein 2-Schritt (wobei noch `n-2` Stufen übrig bleiben). Diese Möglichkeiten
überschneiden sich nicht, daher gilt:

```
f(n) = f(n-1) + f(n-2)
```

mit `f(0) = 1` (die leere Folge ist „eine Möglichkeit“, zu bleiben) und
`f(1) = 1`. Dies ist die Fibonacci-Rekursion, um einen
Index verschoben — `f(n) = F(n+1)`.

Die Erkenntnis aus der dynamischen Programmierung: Die naive rekursive
Formulierung berechnet `f(k)` exponentiell oft neu; die
top-down-memorisierte oder bottom-up-tabellierte Version berührt jedes
`f(k)` genau einmal. Und die rollende Version benötigt nur die
letzten beiden Werte.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dp_02: Climbing Stairs.

Count the number of ways to climb n stairs taking 1 or 2 steps
at a time. Same recurrence as Fibonacci: ways(n) = ways(n-1) +
ways(n-2). O(n) time, O(1) space.
"""


def solve(n):
    if n <= 2:
        return max(n, 1)
    previous, current = 1, 2
    for _ in range(3, n + 1):
        previous, current = current, previous + current
    return current
```

</details>

## Schritt-für-Schritt-Anleitung

`n = 5`:

| Iteration | i | prev (f(i-2)) | curr (f(i-1)) | next (f(i)) |
|---|---:|---:|---:|---:|
| init | — | 1 | 1 | — |
| 1 | 2 | 1 | 1 | 2 |
| 2 | 3 | 1 | 2 | 3 |
| 3 | 4 | 2 | 3 | 5 |
| 4 | 5 | 3 | 5 | 8 |

Gibt 8 zurück. ✓ (8 verschiedene Möglichkeiten, 5 Stufen zu erklimmen.)

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ — `n < 2` |
| **Durchschnittlicher Fall** | $O(n)$ | $O(1)$ |
| **Schlechteste** | $O(n)$ | $O(1)$ |

Die erforderliche Komplexität beträgt $O(n)$; die „Rolling“-Implementierung
entspricht dieser genau. Die memoisierte rekursive Version beträgt ebenfalls
$O(n)$, benötigt jedoch $O(n)$ Stack-Speicherplatz (oder $O(n)$ zusätzlichen Heap-Speicher, wenn man
ein Dict verwendet).

## Varianten & Optimierungen

- **k Schritte auf einmal** — Ersetze das „1-oder-2“ durch „1-oder-2-oder-…-oder-k“.
  Die Rekursionsformel lautet dann `f(n) = f(n-1) + f(n-2) + … + f(n-k)`,
  die k-Bonacci-Folge. Der Speicherbedarf bleibt bei $O(1)$, aber die Konstante
  beträgt nun `O(k)` pro Iteration; wechsle zu einem gleitenden Fenster der
  Größe `k`, um den Speicherbedarf gering zu halten.
- **Unterschiedliche Schrittkosten** – statt „1 oder 2 Schritte“ zahlt man
  ein `cost[i]` für `i` Schritte. Rekursionsformel:
  `f(n) = max(f(n-1) + cost[1], f(n-2) + cost[2])`. Dies ist
  das Problem **„Min Cost Climbing Stairs“** (`dp_23`).
- **Memoisierte Rekursion** — sauberer Code, benötigt jedoch $O(n)$ Speicherplatz für
  den Aufrufstapel. Die cOde(n)-Engine akzeptiert dies, solange
  die Gesamtzahl der Operationen $O(n)$ beträgt (was der Fall ist, da jedes `f(k)`
  nur einmal berechnet wird).
- **Matrixpotenzierung** – bei sehr großen `n` (z. B. `n > 10^9`)
  und vielen Abfragen wird die 2×2-Übergangsmatrix in $O(log n)$ zur
  n-ten Potenz erhoben.

## Anwendungen in der Praxis

- **Zählen von Pfaden in einem DAG** — jedes DAG, bei dem der Eingangsgrad
  jedes Knotens begrenzt ist und die Kantenbeschriftungen 1 und 2 lauten, lässt sich
  auf diese Rekursion zurückführen. Wird in Compilern (Zählen von Pfaden in einem
  Kontrollflussgraphen) und beim Netzwerk-Routing verwendet.
- **Kacheln eines 1×n-Bretts mit 1×1- und 1×2-Kacheln** — genau dieselbe
  Rekursion, andere Formulierung. (Die 1×1-Kachel ist ein „1
  Schritt“, die 1×2-Kachel ist ein „2-Schritt“.)
- **Kombinatorische Identitäten** — beweist die Cassini-Identität
  `F(n-1)·F(n+1) − F(n)^2 = (−1)^n` und mehrere andere mittels
  der Matrix-Exponentiationsform.

## Verwandte Algorithmen in cOde(n)

- **[dp_01 — Fibonacci](dp_01_fibonacci.md)** — dieselbe
  Rekursion, auf die direkte Berechnung von Fibonacci-Zahlen ausgerichtet.
  (d=5/10, r=9/10)
- **[dp_23 — Treppensteigen mit minimalen Kosten](dp_23_min-cost-climbing-stairs.md)** —
  Verallgemeinerung mit schrittweisen Kosten. (d=3/10, r=9/10)
- **[dp_11 — Einbrecher](dp_11_house-robber.md)** — verwendet ebenfalls
  eine rollierende DP mit zwei Variablen, aber die Rekursionsformel lautet
  `f(n) = max(f(n-1), f(n-2) + a[n])` (Entscheidung, nicht Zählung).
  (d=5/10, r=9/10)

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
nach dem Vorbild der kanonischen Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Für den kanonischen Enzyklopädieeintrag
folgen Sie bitte dem Wikipedia-Link oben auf der Seite.
Quell-Repository: <https://github.com/dawei7/code_n>.*
