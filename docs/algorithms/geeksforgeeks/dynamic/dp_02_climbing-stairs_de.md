# Climbing Stairs

| | |
|---|---|
| **ID** | `dp_02` |
| **Kategorie** | dynamic |
| **Komplexität (erforderlich)** | $O(n)$ |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **Wikipedia** | [Fibonacci-Folge](https://en.wikipedia.org/wiki/Fibonacci_sequence) (gleiche Rekurrenz) |

## Problemstellung

Sie befinden sich am Fuß einer Treppe mit `n` Stufen. Sie können **1 oder 2 Stufen auf einmal** steigen. Auf wie viele verschiedene Arten können Sie das oberste Ende erreichen?

**Eingabe:** eine Ganzzahl `n >= 0` (die Anzahl der Stufen).
**Ausgabe:** die Anzahl der verschiedenen Wege, um das Ende zu erreichen, ohne Modulo (oder modulo `10^9 + 7` in der schwierigeren Variante).

**Beispiel:**

| n | Wege | Erklärung |
|---:|---:|---|
| 0 | 1 | Ein Weg: stehen bleiben. (Konvention für Randfälle.) |
| 1 | 1 | Ein 1-Stufen-Schritt. |
| 2 | 2 | `1+1` oder `2`. |
| 3 | 3 | `1+1+1`, `1+2`, `2+1`. |
| 4 | 5 | `1+1+1+1`, `1+1+2`, `1+2+1`, `2+1+1`, `2+2`. |
| 5 | 8 | (Wieder Fibonacci.) |

Die Folge `1, 1, 2, 3, 5, 8, 13, ...` entspricht exakt der Fibonacci-Folge.

## Wann man es verwendet

- Das kanonische **erste DP-Problem** in den meisten Büchern zur Vorbereitung auf Vorstellungsgespräche. Der Zustand und die Rekurrenz sind offensichtlich, und der einzige Kniff besteht darin, die Platzoptimierung durch mitlaufende Variablen zu erkennen.
- Als **Aufwärmübung zur Fibonacci-Erkennung**: Viele Probleme des Typs „Sie können in k Schritten Aktion A oder Aktion B ausführen“ lassen sich auf eine Fibonacci-Rekurrenz reduzieren.
- Die Verallgemeinerung auf „k Stufen auf einmal“ (1, 2, ..., oder k Stufen) führt zur k-bonacci-Folge und ist eine natürliche Erweiterung.

## Ansatz

Sei `f(n)` die Anzahl der Möglichkeiten, `n` Stufen zu erklimmen. Der letzte Schritt, den Sie machen, ist entweder ein 1-Stufen-Schritt (es verbleiben `n-1` Stufen) oder ein 2-Stufen-Schritt (es verbleiben `n-2` Stufen). Diese Möglichkeiten überschneiden sich nicht, daher gilt:

```
f(n) = f(n-1) + f(n-2)
```

mit `f(0) = 1` (die leere Folge ist „ein Weg“, um stehen zu bleiben) und `f(1) = 1`. Dies ist die Fibonacci-Rekurrenz, verschoben um einen Index — `f(n) = F(n+1)`.

Die Erkenntnis der dynamischen Programmierung: Die naive rekursive Formulierung berechnet `f(k)` exponentiell oft neu; die Top-Down-Variante mit Memoization oder die Bottom-Up-Tabellierung greift auf jedes `f(k)` exakt einmal zu. Die Version mit mitlaufenden Variablen benötigt zudem nur die letzten zwei Werte.

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

## Durchlauf

`n = 5`:

| Iteration | i | prev (f(i-2)) | curr (f(i-1)) | next (f(i)) |
|---|---:|---:|---:|---:|
| init | — | 1 | 1 | — |
| 1 | 2 | 1 | 1 | 2 |
| 2 | 3 | 1 | 2 | 3 |
| 3 | 4 | 2 | 3 | 5 |
| 4 | 5 | 3 | 5 | 8 |

Gibt 8 zurück. ✓ (8 verschiedene Wege, um 5 Stufen zu erklimmen.)

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ — `n < 2` |
| **Durchschnittlicher Fall** | $O(n)$ | $O(1)$ |
| **Schlechtester Fall** | $O(n)$ | $O(1)$ |

Die erforderliche Komplexität ist $O(n)$; die Implementierung mit mitlaufenden Variablen erreicht dies exakt. Die memoized rekursive Version ist ebenfalls $O(n)$, benötigt aber $O(n)$ Platz für den Stack (oder $O(n)$ zusätzlichen Heap-Speicher, falls ein Dictionary verwendet wird).

## Varianten & Optimierungen

- **k Stufen auf einmal** — ersetzen Sie 1-oder-2 durch 1-oder-2-oder-…-oder-k. Die Rekurrenz wird zu `f(n) = f(n-1) + f(n-2) + … + f(n-k)`, der k-bonacci-Folge. Der Platzbedarf bleibt $O(1)$, aber die Konstante beträgt nun `O(k)` pro Iteration; verwenden Sie ein gleitendes Fenster der Größe `k`, um die Effizienz zu wahren.
- **Unterschiedliche Schrittkosten** — anstatt „1 oder 2 Stufen“ zahlen Sie `cost[i]` für das Gehen von `i` Stufen. Rekurrenz: `f(n) = max(f(n-1) + cost[1], f(n-2) + cost[2])`. Dies ist das Problem **Min Cost Climbing Stairs** (`dp_23`).
- **Memoized Rekursion** — sauberer Code, verbraucht aber $O(n)$ Platz für den Aufruf-Stack. Die cOde(n)-Engine akzeptiert dies, solange die Gesamtzahl der Operationen $O(n)$ beträgt (was der Fall ist, da jedes `f(k)` nur einmal berechnet wird).
- **Matrix-Exponentiation** — für sehr große `n` (z. B. `n > 10^9`) und viele Anfragen kann die 2×2-Übergangsmatrix in $O(log n)$ auf die n-te Potenz erhoben werden.

## Anwendungen in der Praxis

- **Zählen von Pfaden in einem DAG** — jeder DAG, bei dem der Eingangsgrad jedes Knotens beschränkt ist und die Kantenbeschriftungen 1 und 2 sind, reduziert sich auf diese Rekurrenz. Wird in Compilern (Zählen von Pfaden in einem Kontrollflussgraphen) und im Netzwerk-Routing verwendet.
- **Parkettierung eines 1×n-Bretts mit 1×1- und 1×2-Fliesen** — exakt dieselbe Rekurrenz, nur anders formuliert. (Die 1×1-Fliese ist ein „1-Stufen-Schritt“, die 1×2-Fliese ist ein „2-Stufen-Schritt“.)
- **Kombinatorische Identitäten** — beweist die Cassini-Identität `F(n-1)·F(n+1) − F(n)^2 = (−1)^n` und einige andere durch die Form der Matrix-Exponentiation.

## Verwandte Algorithmen in cOde(n)

- **[dp_01 — Fibonacci](dp_01_fibonacci.md)** — dieselbe Rekurrenz, formuliert für die direkte Berechnung von Fibonacci-Zahlen. (d=5/10, r=9/10)
- **[dp_23 — Min Cost Climbing Stairs](dp_23_min-cost-climbing-stairs.md)** — Verallgemeinerung mit Kosten pro Schritt. (d=3/10, r=9/10)
- **[dp_11 — House Robber](dp_11_house-robber.md)** — verwendet ebenfalls eine DP mit 2 mitlaufenden Variablen, aber die Rekurrenz lautet `f(n) = max(f(n-1), f(n-2) + a[n])` (Entscheidung, kein Zählen). (d=5/10, r=9/10)

---

*Diese Dokumentation ist ein Originalinhalt für cOde(n), modelliert nach der kanonischen Struktur, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*