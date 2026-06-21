# 0/1 Knapsack

| | |
|---|---|
| **ID** | `dp_03` |
| **Kategorie** | dynamic |
| **Komplexität (erforderlich)** | $O(n²)$ |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **Wikipedia** | [Knapsack problem](https://en.wikipedia.org/wiki/Knapsack_problem) |

## Problemstellung

Sie haben `n` Gegenstände, von denen jeder ein `weight[i]` und einen `value[i]` besitzt.
Zudem haben Sie einen Rucksack, der maximal `W` Gewichtseinheiten aufnehmen kann. Jeder Gegenstand darf **höchstens einmal** mitgenommen werden (die "0/1"-Einschränkung). Wählen Sie eine Teilmenge aus, die den Gesamtwert maximiert, ohne die Gewichtskapazität zu überschreiten.

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

`W = 5`. Beste Teilmenge: Gegenstände 0 + 1 (Gewicht 5, Wert 7) oder
Gegenstände 0 + 2 (Gewicht 6 — zu schwer) — die Antwort ist also 7. Oder man nimmt
Gegenstände 1 + 3 (Gewicht 8 — zu schwer). Beste Wahl: Gegenstände 0+1 = Wert 7.

## Wann man es verwendet

- Das am häufigsten zitierte **Lehrbuch-DP-Problem** und eine der
  am häufigsten gestellten DP-Varianten in Vorstellungsgesprächen. Die Rekurrenz ist klein
  (zwei Möglichkeiten pro Gegenstand: mitnehmen oder auslassen), aber der Zustandsraum (Gegenstand × verbleibende Kapazität) ist 2D.
- Immer wenn ein Problem die Form **"Teilmenge von N Gegenständen, jeder mit zwei Attributen, wähle eine Teilmenge, die in ein Budget passt und eine Metrik maximiert"** hat, handelt es sich um das Knapsack-Problem oder eine Variante davon (Subset Sum, Partition, etc.).

## Ansatz

Definiere `dp[i][w]` = der maximale Wert, der unter Verwendung der ersten `i` Gegenstände (Gegenstände `0..i-1`) bei einer Kapazität `w` erreichbar ist.

**Rekurrenz** (betrachte Gegenstand `i-1`):
- **Auslassen:** `dp[i][w] = dp[i-1][w]`.
- **Mitnehmen** (nur wenn `weights[i-1] <= w`):
  `dp[i][w] = dp[i-1][w - weights[i-1]] + values[i-1]`.
- Wähle das Maximum: `dp[i][w] = max(skip, take)`.

**Induktionsanfang:** `dp[0][w] = 0` für alle `w` (keine Gegenstände = kein Wert).
**Antwort:** `dp[n][W]`.

**Platzoptimierung:** Jede Zeile `i` hängt nur von der Zeile `i-1` ab, daher können wir die 2D-Tabelle in ein 1D-Array reduzieren, das **von rechts nach links** iteriert wird, damit wir keine Werte überschreiben, die wir noch benötigen:

```
for i in 0..n-1:
    for w in W down to weights[i]:
        dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
```

Dies ist die produktive Implementierung, gegen die die Engine von cOde(n) prüft ($O(n·W)$ Zeit, $O(W)$ Platz).

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

## Durchlauf

`weights = [2, 3, 4]`, `values = [3, 4, 5]`, `W = 5`.

`dp = [0, 0, 0, 0, 0, 0]` (Länge 6).

**Gegenstand 0 (w=2, v=3):** iteriere w von 5 abwärts bis 2.

| w | dp[w] vorher | Kandidat | dp[w] nachher |
|---:|---:|---:|---:|
| 5 | 0 | dp[3]+3 = 3 | 3 |
| 4 | 0 | dp[2]+3 = 3 | 3 |
| 3 | 0 | dp[1]+3 = 3 | 3 |
| 2 | 0 | dp[0]+3 = 3 | 3 |

`dp = [0, 0, 3, 3, 3, 3]`.

**Gegenstand 1 (w=3, v=4):** iteriere w von 5 abwärts bis 3.

| w | dp[w] vorher | Kandidat | dp[w] nachher |
|---:|---:|---:|---:|
| 5 | 3 | dp[2]+4 = 7 | **7** |
| 4 | 3 | dp[1]+4 = 4 | 4 |
| 3 | 3 | dp[0]+4 = 4 | 4 |

`dp = [0, 0, 3, 4, 4, 7]`.

**Gegenstand 2 (w=4, v=5):** iteriere w von 5 abwärts bis 4.

| w | dp[w] vorher | Kandidat | dp[w] nachher |
|---:|---:|---:|---:|
| 5 | 7 | dp[1]+5 = 5 | 7 |
| 4 | 4 | dp[0]+5 = 5 | 5 |

`dp = [0, 0, 3, 4, 5, 7]`. Antwort: `dp[5] = 7`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(n·W)$ | $O(W)$ |
| **Durchschnittlicher Fall** | $O(n·W)$ | $O(W)$ |
| **Schlechtester Fall** | $O(n·W)$ | $O(W)$ |

Hinweis: Die Komplexität ist **pseudo-polynomial in W** — sie hängt von der *Größe* von W ab, nicht von der Anzahl der Bits.
Für `W = 10^9` ist dies nicht praktikabel. Das 0/1 Knapsack-Problem ist im Allgemeinen NP-schwer; die DP-Lösung ist nur für kleine W exakt.

## Varianten & Optimierungen

- **Unbounded Knapsack** — Gegenstände können mehrfach genommen werden.
  Ändern Sie die innere Schleife so, dass `w` von links nach rechts iteriert wird.
  (`dp_05` — Coin Change ist ein Spezialfall.)
- **Fractional Knapsack** — Gegenstände können geteilt werden. Lösbar durch einen Greedy-Ansatz: Sortiere nach dem Verhältnis von Wert zu Gewicht, nimm zuerst das höchste Verhältnis. (Nicht in der 0/1-Spezifikation von cOde(n) enthalten.)
- **Subgraph / Target-Sum** — `dp_06` (Subset Sum) ist die Entscheidungsvariante (`values = weights` und das Ziel ist eine Summe, kein Maximum).
- **Meet-in-the-middle** — für große `W` und kleine `n` (n ≤ 40), teile die Gegenstände in zwei Hälften, zähle die Teilmengen jeder Hälfte auf (jeweils 2^(n/2)) und kombiniere sie. Reduziert auf $O(2^(n/2) · n)$.

## Anwendungen in der Praxis

- **Kapitalbudgetierung** — Auswahl eines Portfolios von Projekten, das in ein Budget passt und den erwarteten Ertrag maximiert.
- **Frachtverladung** — Packen von Containern unterschiedlicher Größe und Priorität in den Laderaum eines Schiffes.
- **Ressourcenallokation in Compilern** — Auswahl von Registern, Auswahl von Instruktionen für einen Delay-Slot, etc.
- **Subset-Sum-Kryptographie** — das Merkle-Hellman-Knapsack-Kryptosystem basiert auf der Schwierigkeit des Subset-Sum-Problems.

## Verwandte Algorithmen in cOde(n)

- **[dp_05 — Coin Change](dp_05_coin-change.md)** — Unbounded-Variante: minimiere Münzen, nicht maximiere Wert. (d=5/10, r=9/10)
- **[dp_06 — Subset Sum](dp_06_subset-sum.md)** — Entscheidungsvariante (wahr/falsch), 0/1. (d=5/10, r=9/10)
- **[dp_17 — Partition Equal Subset Sum](dp_17_partition-equal-subset-sum.md)** —
  kann man das Array in zwei Teilmengen mit gleicher Summe aufteilen?
  (d=5/10, r=9/10)
- **[dp_30 — Coin Change (Count Ways)](dp_30_coin-change-count-ways.md)** —
  Unbounded, Zählen der Lösungen. (d=3/10, r=9/10)

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) erstellt wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*