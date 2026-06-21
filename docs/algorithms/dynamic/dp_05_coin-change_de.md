# Coin Change

| | |
|---|---|
| **ID** | `dp_05` |
| **Kategorie** | dynamic |
| **Komplexität (erforderlich)** | $O(n²)$ |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **Wikipedia** | [Change-making problem](https://en.wikipedia.org/wiki/Change-making_problem) |

## Problemstellung

Gegeben ist ein Array von Münzwerten `coins` und ein Zielbetrag `amount`. Finde die **minimale Anzahl an Münzen**, die benötigt wird, um diesen Betrag zu erreichen. Jede Münze kann **unbegrenzt oft** verwendet werden (unbeschränktes Rucksackproblem). Falls der Betrag nicht erreicht werden kann, gib `-1` zurück (oder `+∞` in der cOde(n)-Engine).

**Eingabe:** `coins = [c1, c2, ..., cn]` (positive Ganzzahlen), `amount` (nicht-negative Ganzzahl).
**Ausgabe:** die minimale Anzahl an Münzen, die sich zu `amount` summieren, oder `-1`, falls dies unmöglich ist.

**Beispiel:**

| coins | amount | Ausgabe | Erklärung |
|---|---|---:|---|
| [1, 5, 10, 25] | 11 | 2 | 10 + 1 |
| [1, 5, 10, 25] | 30 | 2 | 25 + 5 |
| [2] | 3 | -1 | unmöglich |
| [1] | 0 | 0 | null Münzen für Betrag null |
| [1, 2, 5] | 11 | 3 | 5 + 5 + 1 |

## Anwendung

- Das kanonische Problem für **unbeschränkte Rucksackprobleme mit Minimierungsziel** in Vorstellungsgesprächen. Etwas häufiger anzutreffen als die Maximierungsvariante, da die Antwort (minimale Anzahl) eine kleine Zahl ist, die in einen `int` passt.
- Immer wenn man eine „**unendliche Verfügbarkeit jedes Elements bei Minimierung der Anzahl**“ mit einer eindimensionalen Ressourcenbeschränkung hat, ist dieser Ansatz anwendbar.

## Ansatz

Sei `dp[a]` = die minimale Anzahl an Münzen, um den Betrag `a` zu erreichen, oder `+∞`, falls dies unmöglich ist.

**Rekurrenz:** Für die letzte Münze mit dem Wert `c` gilt:
`dp[a] = 1 + dp[a - c]` (wir haben eine Münze `c` verwendet und müssen nun den Restbetrag bilden). Probiere jedes `c` aus und wähle das Minimum:

```
dp[a] = min(1 + dp[a - c])   over all c in coins with c <= a
```

**Induktionsanfang:** `dp[0] = 0` (null Münzen für Betrag null).
**Initialisierung:** `dp[a] = +∞` für `a > 0`.

**Iterationsreihenfolge:** `a` von `1` bis `amount` (jede Reihenfolge funktioniert, da alle Teilprobleme `a - c` kleiner sind; keine negativen Kanten).

**Rückgabe:** `dp[amount]`, falls endlich, sonst `-1`.

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

## Durchlauf

`coins = [1, 5, 10, 25]`, `amount = 11`.

`dp = [0, +∞, +∞, +∞, +∞, +∞, +∞, +∞, +∞, +∞, +∞, +∞]`.

| a | try c=1 | try c=5 | try c=10 | try c=25 | dp[a] |
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
| **Bestfall** | $O(n · amount)$ | $O(amount)$ |
| **Durchschnittlicher Fall** | $O(n · amount)$ | $O(amount)$ |
| **Schlechtester Fall** | $O(n · amount)$ | $O(amount)$ |

Pseudopolynomiell in `amount`, genau wie beim 0/1-Rucksackproblem. Bei sehr großen `amount`-Werten sollte ein Greedy-Ansatz in Betracht gezogen werden, sofern das Münzsystem kanonisch ist (US-Münzen sind dies; beliebige Münzsysteme sind es nicht – siehe den Wikipedia-Eintrag für die präzise Charakterisierung).

## Varianten & Optimierungen

- **Greedy für kanonische Münzsysteme** — wenn die Münzwerte die kanonische Eigenschaft erfüllen (jede Greedy-Wahl ist auch die optimale Wahl für einen bestimmten Betrag), kann man $O(amount / max\_denom)$ ohne DP erreichen. US-Münzen `[1, 5, 10, 25]` sind kanonisch.
- **Anzahl der Möglichkeiten zählen** — statt des Minimums die Anzahl der verschiedenen Möglichkeiten zählen, um den Betrag zu erreichen. Initial `dp[0] = 1`, `dp[a] += dp[a - c]` für jede Münze. (Siehe `dp_30`.)
- **Verwendete Münzen ausgeben** — eine `parent[a] = c` Tabelle parallel zu `dp` führen und durch Rückwärtsverfolgung von `parent[amount]` rekonstruieren.
- **BFS** — Beträge als Graph-Knoten betrachten, Kanten als „füge eine Münze hinzu“, BFS von `0` aus starten, bis `amount` erreicht ist. In der Praxis oft schneller, wenn die Antwort klein ist.

## Anwendungen in der Praxis

- **Kassensysteme** — einen Kaufbetrag in Scheine/Münzen zerlegen, wobei die Anzahl minimiert wird (oder eine gewünschte Stückelung erreicht wird).
- **Verkaufsautomaten** — das Wechselgeldproblem in umgekehrter Form (der Automat *gibt* Wechselgeld).
- **Währungsarbitrage** — Umrechnung zwischen Währungen über eine Kette von Konvertierungen.
- **U-Bahn-Tarifsysteme** — die minimale Anzahl an Tickets finden, um eine Reihe von Fahrten abzudecken.

## Verwandte Algorithmen in cOde(n)

- **[dp_03 — 0/1 Knapsack](dp_03_knapsack.md)** — beschränkte Variante (jedes Element einmal). (d=5/10, r=9/10)
- **[dp_30 — Coin Change (Count Ways)](dp_30_coin-change-count-ways.md)** — unbeschränkt, zählt Lösungen statt zu minimieren. (d=3/10, r=9/10)
- **[greedy_10 — Minimum Coins](greedy_10_minimum-coins.md)** — die Greedy-Version; funktioniert für kanonische Münzsysteme. (d=3/10, r=6/10)

---

*Diese Dokumentation ist ein Originalinhalt für cOde(n), modelliert nach der kanonischen Struktur, die von Referenzseiten für Wettbewerbsprogrammierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*