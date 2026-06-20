# 0/1 Rucksack

| | |
|---|---|
| **ID** | `dp_03` |
| **Kategorie** | dynamisch |
| **Komplexität (erforderlich)** | $O(n²)$ |
| **Schwierigkeitsgrad** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **Wikipedia** | [Rucksackproblem](https://en.wikipedia.org/wiki/Knapsack_problem) |

## Aufgabenstellung

Du hast `n` Gegenstände, von denen jeder ein `weight[i]` und ein `value[i]` hat.
Außerdem hast du einen Rucksack, der höchstens `W` Gewichtseinheiten
fassen kann. Jeder Gegenstand darf **höchstens einmal** mitgenommen werden (die „0/1“-
Einschränkung). Wähle eine Teilmenge aus, die den Gesamtwert maximiert,
ohne die Gewichtskapazität zu überschreiten.

**Eingabe:** `weights = [w1, w2, ..., wn]`,
`values = [v1, v2, ..., vn]`, Kapazität `W`.
**Ausgabe:** der maximal erreichbare Gesamtwert.

**Beispiel:**

| Gegenstand | Gewicht | Wert |
|---:|---:|---:|
| 0 | 2 | 3 |
| 1 | 3 | 4 |
| 2 | 4 | 5 |
| 3 | 5 | 6 |

`W = 5`. Beste Teilmenge: Artikel 0 + 1 (Gewicht 5, Wert 7) oder
Artikel 0 + 2 (Gewicht 6 – überschritten) – daher lautet die Antwort 7. Oder man nehme
Artikel 1 + 3 (Gewicht 8 – überschritten). Optimal: Elemente 0 + 1 = Wert 7.

## Wann man es anwendet

- Das am häufigsten zitierte **DP-Lehrbuchproblem** und eine der
  am häufigsten gestellten DP-Varianten in Vorstellungsgesprächen. Die Rekursion ist gering
  (zwei Entscheidungen pro Element: nehmen oder überspringen), aber der Zustandsraum
  (Element × verbleibende Kapazität) ist zweidimensional.
- Immer wenn ein Problem die Form **„Teilmenge von N Elementen mit jeweils
  zwei Attributen; wähle eine Teilmenge, die in ein Budget passt und
  eine bestimmte Metrik maximiert“** hat, handelt es sich um ein Rucksackproblem oder eine
  Rucksackvariante (Teilmengensumme, Partitionierung usw.).

## Vorgehensweise

Definiere `dp[i][w]` als den maximalen Wert, der nur mit
den ersten `i` Gegenständen (Gegenstände `0..i-1`) bei einer Kapazität von `w` erreichbar ist.

**Rekursion** (betrachte Element `i-1`):
- **Überspringen:** `dp[i][w] = dp[i-1][w]`.
- **Mitnehmen** (nur wenn `weights[i-1] <= w`):
  `dp[i][w] = dp[i-1][w - weights[i-1]] + values[i-1]`.
- Das Maximum nehmen: `dp[i][w] = max(skip, take)`.

**Basisfall:** `dp[0][w] = 0` für alle `w` (keine Elemente = kein Wert).
**Ergebnis:** `dp[n][W]`.

**Speicherplatzoptimierung:** Jede Zeile `i` hängt nur von der Zeile
`i-1` ab, daher können wir die 2D-Tabelle zu einem 1D-Array zusammenfassen,
das **von rechts nach links** durchlaufen wird, damit wir keine Werte überschreiben, die wir
noch benötigen:

```
for i in 0..n-1:
    for w in W down to weights[i]:
        dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
```

Dies ist die Produktionsimplementierung und diejenige, gegen die die Engine von cOde(n)
prüft ($O(n·W)$ Zeit, $O(W)$ Speicherplatz).

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dp_03: 0/1 Knapsack.

Classic DP table: dp[i][c] = max value using the first i items
with capacity c. O(n * capacity) time, O(n * capacity) space.
"""


def solve(weights, values, capacity, n):
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        w = weights[i - 1]
        v = values[i - 1]
        for c in range(capacity + 1):
            if w <= c:
                dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - w] + v)
            else:
                dp[i][c] = dp[i - 1][c]
    return dp[n][capacity]
```

</details>

## Schritt-für-Schritt-Anleitung

`weights = [2, 3, 4]`, `values = [3, 4, 5]`, `W = 5`.

`dp = [0, 0, 0, 0, 0, 0]` (Länge 6).

**Element 0 (w=2, v=3):** w von 5 bis 2 durchlaufen.

| w | dp[w] vorher | Kandidat | dp[w] nachher |
|---:|---:|---:|---:|
| 5 | 0 | dp[3]+3 = 3 | 3 |
| 4 | 0 | dp[2]+3 = 3 | 3 |
| 3 | 0 | dp[1]+3 = 3 | 3 |
| 2 | 0 | dp[0]+3 = 3 | 3 |

`dp = [0, 0, 3, 3, 3, 3]`.

**Punkt 1 (w=3, v=4):** w von 5 bis 3 absteigend durchlaufen.

| w | dp[w] vorher | Kandidat | dp[w] nachher |
|---:|---:|---:|---:|
| 5 | 3 | dp[2]+4 = 7 | **7** |
| 4 | 3 | dp[1]+4 = 4 | 4 |
| 3 | 3 | dp[0]+4 = 4 | 4 |

`dp = [0, 0, 3, 4, 4, 7]`.

**Punkt 2 (w=4, v=5):** w von 5 bis 4 absteigend durchlaufen.

| w | dp[w] vorher | Kandidat | dp[w] danach |
|---:|---:|---:|---:|
| 5 | 7 | dp[1]+5 = 5 | 7 |
| 4 | 4 | dp[0]+5 = 5 | 5 |

`dp = [0, 0, 3, 4, 5, 7]`. Antwort: `dp[5] = 7`. ✓

## Komplexität

| | Zeit | Speicher |
|---|---|---|
| **Best** | $O(n·W)$ | $O(W)$ |
| **Durchschnittlicher Fall** | $O(n·W)$ | $O(W)$ |
| **Schlechtester Fall** | $O(n·W)$ | $O(W)$ |

Anmerkung: Die Komplexität ist **pseudopolynomial in W** – sie
hängt von der *Größe* von W ab, nicht von der Anzahl der Bits.
Für `W = 10^9` ist dies nicht lösbar. Das 0/1-Rucksackproblem ist
im Allgemeinen NP-schwer; die dynamische Programmierung ist nur für kleine W exakt.

## Varianten & Optimierungen

- **Unbegrenzter Rucksack** – Elemente können mehrfach genommen werden.
  Ändere die innere Schleife so, dass `w` von links nach rechts durchlaufen wird.
  (`dp_05` – „Coin Change“ ist ein Sonderfall.)
- **Fraktioniertes Rucksackproblem** — Gegenstände können geteilt werden. Lösbar mit
  dem Greedy-Algorithmus: Nach Wert-Gewichts-Verhältnis sortieren, das höchste Verhältnis
  zuerst nehmen. (Nicht in der 0/1-Spezifikation von cOde(n) enthalten.)
- **Teilgraph / Zielsumme** — `dp_06` (Teilmenge-Summe) ist die
  Entscheidungsvariante (`values = weights` und das Ziel ist eine
  Summe, kein Maximum).
- **Meet-in-the-middle** — für große `W` und kleine `n` (n ≤ 40),
  Teile die Elemente in zwei Hälften auf, zähle die Teilmengen jeder Hälfte
  (jeweils 2^(n/2)) und kombinieren. Reduziert sich auf $O(2^(n/2)$ · n).

## Anwendungen in der Praxis

- **Investitionsplanung** — Wähle ein Projektportfolio aus, das
  dem Budget entspricht und die erwartete Rendite maximiert.
- **Ladungsbeladung** — Packen von Containern unterschiedlicher Größe und
  Priorität in den Laderaum eines Schiffes.
- **Ressourcenzuweisung in Compilern** — Auswahl von Registern,
  Auswahl von Befehlen für einen Verzögerungsslot usw.
- **Subset-Sum-Kryptografie** — das Merkle-Hellman-Knapsack-
  Kryptosystem basiert auf der Schwierigkeit des Subset-Sum-Problems.

## Verwandte Algorithmen in cOde(n)

- **[dp_05 — Münzwechsel](dp_05_coin-change.md)** — unbegrenzte
  Variante: Anzahl der Münzen minimieren, nicht den Wert maximieren. (d=5/10, r=9/10)
- **[dp_06 — Teilmenge-Summe](dp_06_subset-sum.md)** — Entscheidungsvariante
  (wahr/falsch), 0/1. (d=5/10, r=9/10)
- **[dp_17 — Partition Equal Subset Sum](dp_17_partition-equal-subset-sum.md)** —
  Kann man das Array in zwei Teilmengen mit gleicher Summe aufteilen?
  (d=5/10, r=9/10)
- **[dp_30 — Münzwechsel (Anzahl der Möglichkeiten)](dp_30_coin-change-count-ways.md)** —
  unbegrenzt, Zählen der Lösungen. (d=3/10, r=9/10)

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
in Anlehnung an die kanonische Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag
finden Sie unter dem Wikipedia-Link oben auf der Seite.
Quell-Repository: <https://github.com/dawei7/code_n>.*
