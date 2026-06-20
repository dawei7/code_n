# Wechselgeld

| | |
|---|---|
| **ID** | `dp_05` |
| **Kategorie** | dynamisch |
| **Komplexität (erforderlich)** | $O(n²)$ |
| **Schwierigkeitsgrad** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **Wikipedia** | [Problem der Münzrückgabe](https://en.wikipedia.org/wiki/Change-making_problem) |

## Problemstellung

Gegeben sei ein Array mit Münzwerten `coins` und ein Zielwert
`amount`, finde die **minimale Anzahl an Münzen**, die benötigt wird, um
diesen Betrag zusammenzustellen. Jede Münze kann **unbegrenzt oft** verwendet werden
(unbegrenzter Rucksack). Wenn der Betrag nicht zusammengestellt werden kann, gib
`-1` zurück (oder `+∞` in der Engine von cOde(n)).

**Eingabe:** `coins = [c1, c2, ..., cn]` (positive ganze Zahlen),
`amount` (nicht-negative ganze Zahl).
**Ausgabe:** die minimale Anzahl an Münzen, deren Summe `amount` ergibt,
oder `-1`, falls dies unmöglich ist.

**Beispiel:**

| Münzen | Betrag | Ausgabe | Erklärung |
|---|---|---:|---|
| [1, 5, 10, 25] | 11 | 2 | 10 + 1 |
| [1, 5, 10, 25] | 30 | 2 | 25 + 5 |
| [2] | 3 | -1 | unmöglich |
| [1] | 0 | 0 | null Münzen für den Betrag Null |
| [1, 2, 5] | 11 | 3 | 5 + 5 + 1 |

## Wann man es anwendet

- Das klassische Problem der **Minimierungsvarianten für den unbegrenzten Rucksack**
  in Vorstellungsgesprächen. Etwas häufiger als die Maximierungsvariante
  , da die Antwort (Mindestanzahl) eine kleine Zahl ist,
  die in ein `int` passt.
- Immer wenn es um „**unendlichen Vorrat an jedem Element, minimiere
  die Anzahl**“ mit einer eindimensionalen Ressourcenbeschränkung geht, gilt diese
  Form.

## Vorgehensweise

Sei `dp[a]` = die minimale Anzahl an Münzen, um den Betrag `a` zu erzielen,
oder `+∞`, falls dies unmöglich ist.

**Rekursion:** Für die letzte Münze der Stückelung `c`,
`dp[a] = 1 + dp[a - c]` (wir haben eine `c` verwendet und müssen nun
den Rest zusammenstellen). Probiere jedes `c` aus und wähle das Minimum:

```
dp[a] = min(1 + dp[a - c])   over all c in coins with c <= a
```

**Basisfall:** `dp[0] = 0` (null Münzen für den Betrag null).
**Initialisierung:** `dp[a] = +∞` für `a > 0`.

**Iterationsreihenfolge:** `a` von `1` bis `amount` (jede Reihenfolge ist zulässig,
da alle Teilprobleme `a - c` kleiner sind; keine negativen
Kanten).

**Rückgabe:** `dp[amount]`, falls endlich, andernfalls `-1`.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dp_05: Coin Change.

Minimum number of coins summing to the given amount.
"""


def solve(coins, amount):
    INF = float("inf")
    dp = [INF] * (amount + 1)
    dp[0] = 0
    for v in range(1, amount + 1):
        for c in coins:
            if c <= v and dp[v - c] + 1 < dp[v]:
                dp[v] = dp[v - c] + 1
    return dp[amount] if dp[amount] != INF else -1
```

</details>

## Schritt-für-Schritt-Anleitung

`coins = [1, 5, 10, 25]`, `amount = 11`.

`dp = [0, +∞, +∞, +∞, +∞, +∞, +∞, +∞, +∞, +∞, +∞, +∞]`.

| a | versuche c=1 | versuche c=5 | versuche c=10 | versuche c=25 | dp[a] |
|---:|---:|---:|---:|---:|---:|
| 1 | 1+dp[0]=1 | — | — | — | 1 |
| 2 | 1+dp[1]=2 | — | — | — | 2 |
| 3 | 1+dp[2]=3 | — | — | — | 3 |
| 4 | 1+dp[3]=4 | — | — | — | 4 |
| 5 | 1+dp[4]=5 | 1+dp[0]=1 | — | — | **1** |
| 6 | 1+dp[5]=2 | 1+dp[1]=2 | — | — | 2 |
| 7 | 1+dp[6]=3 | 1+dp[2]=3 | — | — | 3 |
| 8 | 1+dp[7]=4 | 1+dp[3]=4 | — | — | 4 |
| 9 | 1+dp[8]=5 | 1+dp[4]=5 | — | — | 5 |
| 10 | 1+dp[9]=6 | 1+dp[5]=2 | 1+dp[0]=1 | — | **1** |
| 11 | 1+dp[10]=2 | 1+dp[6]=3 | 1+dp[1]=2 | — | **2** |

Antwort: `dp[11] = 2` (10 + 1). ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Best** | $O(n · amount)$ | $O(amount)$ |
| **Durchschnittlicher Fall** | $O(n · amount)$ | $O(amount)$ |
| **Schlechteste** | $O(n · amount)$ | $O(amount)$ |

Pseudopolynomial in `amount`, genau wie beim 0/1-Rucksackproblem. Bei
sehr großen `amount` sollte man einen Greedy-Ansatz in Betracht ziehen, wenn das Münzsystem
kanonisch ist (US-Münzen sind es; beliebige Münzsysteme sind es nicht – siehe
den Wikipedia-Eintrag für die genaue Charakterisierung).

## Varianten & Optimierungen

- **Gierig für kanonische Münzsysteme** — wenn die Nennwerte
  die Eigenschaft kanonischer Münzen erfüllen (jede gierige Wahl ist
  auch die optimale Wahl für einen bestimmten Betrag), kann man
  $O(amount / max_denom)$ ohne DP lösen. US-Münzen `[1, 5, 10, 25]`
  sind kanonisch.
- **Anzahl der Möglichkeiten zählen** – statt des Minimums die Anzahl der
  unterschiedlichen Möglichkeiten zählen, den Betrag zu bilden. Anfangswert `dp[0] = 1`,
  `dp[a] += dp[a - c]` für jede Münze. (Siehe `dp_30`.)
- **Die verwendeten Münzen ausgeben** — führe neben `dp` eine `parent[a] = c`-Tabelle
  und rekonstruiere den Weg, indem du von
  `parent[amount]` aus zurückgehst.
- **BFS** — Betrachte Beträge als Knoten im Graphen, Kanten als „eine Münze hinzufügen“,
  führe BFS von `0` aus durch, bis du `amount` erreichst. In der
  Praxis oft schneller, wenn das Ergebnis klein ist.

## Anwendungen in der Praxis

- **Kassensoftware** – Zerlege einen Kaufbetrag in
  Banknoten und Münzen, um die Anzahl der Zählvorgänge zu minimieren (oder eine gewünschte
  Zusammensetzung zu erreichen).
- **Verkaufsautomaten** – das Münzwechselproblem in umgekehrter Richtung
  (der Automat *gibt* Wechselgeld aus).
- **Währungsarbitrage** – Umrechnung zwischen Währungen über
  eine Kette von Umrechnungen.
- **U-Bahn-Tarifsysteme** – Ermittlung der minimalen Anzahl an Fahrkarten,
  die für eine Reihe von Fahrten erforderlich ist.

## Verwandte Algorithmen in cOde(n)

- **[dp_03 — 0/1-Rucksackproblem](dp_03_knapsack.md)** — begrenzte
  Variante (jedes Element einmal). (d=5/10, r=9/10)
- **[dp_30 — Münzwechsel (Anzahl der Möglichkeiten)](dp_30_coin-change-count-ways.md)** —
  unbegrenzt, Zählen der Lösungen statt Minimierung.
  (d=3/10, r=9/10)
- **[greedy_10 — Minimum Coins](greedy_10_minimum-coins.md)** —
  die Greedy-Version; funktioniert für kanonische Münzsysteme.
  (d=3/10, r=6/10)

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
nach dem Vorbild der kanonischen Struktur, die von Referenzseiten zum
Wettbewerbsprogrammieren verwendet wird. Für den kanonischen Enzyklopädieeintrag
folgen Sie bitte dem Wikipedia-Link oben auf der Seite.
Quell-Repository: <https://github.com/dawei7/code_n>.*
