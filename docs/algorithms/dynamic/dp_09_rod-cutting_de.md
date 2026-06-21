# Rod Cutting

| | |
|---|---|
| **ID** | `dp_09` |
| **Kategorie** | dynamic |
| **Komplexität (erforderlich)** | $O(n²)$ |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **Wikipedia** | [Cutting stock problem](https://en.wikipedia.org/wiki/Cutting_stock_problem) |

## Problemstellung

Gegeben ist eine Stange der Länge `n` sowie eine Preistabelle `prices[i]` für ein Stangenstück der Länge `i + 1` (für `i = 0..n-1`). Bestimmen Sie den **maximalen Erlös**, der durch das Zerschneiden der Stange in Stücke und deren Verkauf erzielt werden kann.

**Eingabe:** eine Ganzzahl `n` und ein Array `prices` der Länge `n`.
**Ausgabe:** der maximale Erlös.

**Beispiel:**

| Länge | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Preis | 1 | 5 | 8 | 9 |10 |17 |17 |20 |

`n = 8`. Bestfall: Zerschneiden in 2 + 2 + 2 + 2 (Erlös 5+5+5+5 = 20)
ODER 6 + 2 (17+5 = 22) ODER 1+2+5+... — das Maximum ist **22** (6+2).

## Anwendung

- Der klassische Einstieg in die dynamische Programmierung für das Problem: „**Zerlegung in Teile zur Maximierung eines Wertes**“ — eine Variante des Unbounded Knapsack Problems, bei der jeder Schnitt zwischen Stücken erfolgt und Stücke wiederholt werden können.
- Eine kleine Variante („Zerschneide einen Stab der Länge N“) wird in Telefoninterviews manchmal als Aufwärmübung verwendet.

## Ansatz

Sei `dp[i]` = der maximale Erlös für eine Stange der Länge `i`.

**Rekurrenz:** Betrachten wir den ersten Schnitt. Wenn wir ein Stück der Länge `j` abschneiden (für `j = 1..i`), behalten wir `prices[j-1]` und haben eine verbleibende Stange der Länge `i - j` mit dem Wert `dp[i - j]`. Wir wählen das Maximum über alle möglichen ersten Schnitte:

```
dp[i] = max(prices[j-1] + dp[i - j])  for j = 1..i
```

**Induktionsanfang:** `dp[0] = 0` (keine Stange, kein Erlös).

**Antwort:** `dp[n]`.

Dies entspricht der Struktur des Unbounded Knapsack Problems — wir wählen „Stücke“ (Längen) mit Wiederholung, um den Wert zu maximieren.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dp_09: Rod Cutting.

dp[length] = max revenue for a rod of that length. For each
length, try every first-cut size.
"""


def solve(prices, n):
    dp = [0] * (n + 1)
    for length in range(1, n + 1):
        for cut in range(1, length + 1):
            revenue = prices[cut - 1] + dp[length - cut]
            if revenue > dp[length]:
                dp[length] = revenue
    return dp[n]
```

</details>

## Durchlauf

`prices = [1, 5, 8, 9, 10, 17, 17, 20]`, `n = 8`.

`dp = [0, 0, 0, 0, 0, 0, 0, 0, 0]`.

| i | try j=1 (1+dp[i-1]) | j=2 (5+dp[i-2]) | j=3 (8+dp[i-3]) | j=4 (9+dp[i-4]) | ... | dp[i] |
|---:|---:|---:|---:|---:|---|---:|
| 1 | 1+0=1 | — | — | — | — | 1 |
| 2 | 1+1=2 | 5+0=5 | — | — | — | 5 |
| 3 | 1+5=6 | 5+1=6 | 8+0=8 | — | — | 8 |
| 4 | 1+8=9 | 5+5=10 | 8+1=9 | 9+0=9 | — | 10 |
| 5 | 1+10=11 | 5+8=13 | 8+5=13 | 9+1=10 | 10+0=10 → **13** |
| 6 | 1+13=14 | 5+10=15 | 8+8=16 | 9+5=14 | 10+1=11, 17+0=17 → **17** |
| 7 | 1+17=18 | 5+13=18 | 8+10=18 | 9+8=17 | 10+5=15, 17+1=18, 17+0=17 → **18** |
| 8 | 1+18=19 | 5+17=22 | 8+13=21 | 9+10=19 | 10+8=18, 17+5=22, 17+1=18, 20+0=20 → **22** |

Antwort: `dp[8] = 22`. ✓ (Schnitte: 2 + 6, Erlös 5 + 17 = 22.)

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(n²)$ | $O(n)$ |
| **Durchschnittlicher Fall** | $O(n²)$ | $O(n)$ |
| **Schlechtester Fall** | $O(n²)$ | $O(n)$ |

Jedes `dp[i]` ist das Maximum über höchstens `i` Kandidaten, daher ist die verschachtelte Schleife $O(n²)$. Die Platzkomplexität beträgt $O(n)$ für das dp-Array.

## Varianten & Optimierungen

- **Rekonstruktion der Schnitte** — ein paralleles Array `cut_at[i]` führen, das speichert, welches `j` gewählt wurde; anschließend zurückverfolgen, um die Schnitte auszugeben.
- **Schnittkosten** — wenn jeder Schnitt `c` kostet, subtrahiere `c` vom Kandidatenwert. Einige Schnitte werden dadurch unwirtschaftlich.
- **Minimale Schnitte für einen Zielerlös** — anstatt den Erlös zu maximieren, die minimale Anzahl an Stücken finden, sodass der Erlös ≥ Zielwert ist. Erfordert eine andere DP-Struktur (beide Metriken verfolgen).
- **Generalisiertes Rod Cutting** — Stücke können neben der Länge auch eine *Breite* haben (z. B. 2D Cutting Stock). Das 1D-DP lässt sich zu einem 2D-DP verallgemeinern.

## Anwendungen in der Praxis

- **Cutting stock problem** — das Zerschneiden von Rohmaterialien (Stahl, Papier, Stoff, Holz) in verkaufbare Stücke, um Abfall zu minimieren. Allgemein NP-schwer; die einfache Version entspricht dem Rod-Cutting-DP.
- **Logistik** — „Wie teilt man einen 40-Fuß-Container in Standardpaletten auf, um den Wert zu maximieren?“
- **Druckwesen** — die beste Methode, um eine Papier- oder Stoffrolle in Druckaufträge zu zerschneiden.
- **Registerallokation in Compilern** — „Aufteilen einer langlebigen Variable in Register, um Cache-Treffer zu maximieren.“
- **Produktionsplanung** — Aufteilen einer langen Produktionsserie in Chargen, die der Nachfrage entsprechen.

## Verwandte Algorithmen in cOde(n)

- **[dp_03 — 0/1 Knapsack](dp_03_knapsack.md)** — beschränkte Variante, Maximierung. (d=5/10, r=9/10)
- **[dp_05 — Coin Change](dp_05_coin-change.md)** — unbeschränkt, Minimierung der Anzahl. (d=5/10, r=9/10)
- **[dp_07 — LIS](dp_07_longest-increasing-subsequence.md)** — ein weiteres klassisches 1D-DP, das ebenfalls häufig in Interviews abgefragt wird. (d=5/10, r=9/10)

---

*Diese Dokumentation ist ein Originalinhalt für cOde(n), modelliert nach der kanonischen Struktur, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den enzyklopädischen Standardeintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*