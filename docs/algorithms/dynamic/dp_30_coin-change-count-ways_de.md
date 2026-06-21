# Coin Change (Anzahl der Möglichkeiten)

| | |
|---|---|
| **ID** | `dp_30` |
| **Kategorie** | dynamic_programming |
| **Komplexität (erforderlich)** | $O(n * amount)$ |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **LeetCode-Äquivalent** | [Coin Change II](https://leetcode.com/problems/coin-change-ii/) |

## Problemstellung

Gegeben ist ein Array `coins` mit Ganzzahlen, das Münzen verschiedener Nennwerte repräsentiert, sowie eine Ganzzahl `amount`, die einen Gesamtbetrag darstellt.
Geben Sie die **Anzahl der eindeutigen Kombinationen** zurück, die diesen Betrag ergeben.
Sie können davon ausgehen, dass von jeder Münzart eine unendliche Anzahl zur Verfügung steht.

**Input:** Ein Array `coins` und eine Ganzzahl `amount`.
**Output:** Eine Ganzzahl, die die Gesamtzahl der Möglichkeiten repräsentiert.

**Beispiel:**
`amount = 5`, `coins = [1, 2, 5]`.
Kombinationen: `5`, `2+2+1`, `2+1+1+1`, `1+1+1+1+1`.
Output: `4`.

## Wann man es verwendet

- Im Gegensatz zum Standard-Coin-Change-Problem (`dp_05`), bei dem nach der *minimalen Anzahl an Münzen* gefragt wird (Optimierung), geht es hier um die *Gesamtzahl der Möglichkeiten* (Kombinatorik).
- Es ist eine direkte Anwendung des **Unbounded Knapsack Problem** (Rucksackproblem mit unbegrenzter Anzahl an Gegenständen).

## Ansatz

Wir können ein 1D-DP-Array verwenden.
Sei `dp[j]` die Anzahl der Möglichkeiten, den Betrag `j` zu bilden.

Wenn wir nacheinander durch jeden Münznennwert iterieren, können wir fragen: "Wie viele *zusätzliche* Möglichkeiten habe ich, den Betrag `j` zu bilden, wenn ich diese aktuelle Münze einbeziehe?"
Die Antwort lautet: So viele Möglichkeiten, wie ich den Betrag `j - coin` bilden konnte!

Für jede `coin` iterieren wir also durch alle Beträge `j` von `coin` bis `amount` und aktualisieren:
`dp[j] = dp[j] + dp[j - coin]`

**Warum iterieren wir in der äußeren Schleife über die Münzen und in der inneren über die Beträge?**
Weil wir **Kombinationen** suchen, keine **Permutationen**. Wir behandeln `2+1` und `1+2` als exakt dieselbe Möglichkeit.
Indem wir in der äußeren Schleife strikt über die `coins` iterieren, erzwingen wir mathematisch eine Reihenfolge (z. B. fügen wir `2`er erst hinzu, nachdem wir das Hinzufügen aller `1`er vollständig abgeschlossen haben). Dies garantiert, dass wir niemals `1+2` und `2+1` separat generieren!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dp_30: Coin Change (Count Ways).

dp[a] = number of ways to make a. For each coin c, walk
forward: dp[a] += dp[a - c].
"""


def solve(coins, n, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for c in coins:
        for a in range(c, amount + 1):
            dp[a] += dp[a - c]
    return dp[amount]
```

</details>

## Durchlauf

`amount = 5`, `coins = [1, 2, 5]`.
`dp = [1, 0, 0, 0, 0, 0]` (Größe 6).

**Coin = 1:**
- `j=1`: `dp[1] += dp[0]` -> `1`.
- `j=2`: `dp[2] += dp[1]` -> `1`.
- ... `dp` wird zu `[1, 1, 1, 1, 1, 1]`. (1 Möglichkeit, jeden Betrag nur mit 1ern zu bilden).

**Coin = 2:**
- `j=2`: `dp[2] += dp[0]` -> `1 + 1 = 2`.
- `j=3`: `dp[3] += dp[1]` -> `1 + 1 = 2`.
- `j=4`: `dp[4] += dp[2]` -> `1 + 2 = 3`.
- `j=5`: `dp[5] += dp[3]` -> `1 + 2 = 3`.
- `dp` wird zu `[1, 1, 2, 2, 3, 3]`.

**Coin = 5:**
- `j=5`: `dp[5] += dp[0]` -> `3 + 1 = 4`.

Output: `dp[5] = 4`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(n * amount)$ | $O(amount)$ |
| **Durchschnittlicher Fall** | $O(n * amount)$ | $O(amount)$ |
| **Schlechtester Fall** | $O(n * amount)$ | $O(amount)$ |

Wir iterieren durch n Münzen. Für jede Münze iterieren wir durch bis zu `amount` Werte. Die gesamte Zeitkomplexität beträgt strikt $O(n x \text{amount})$.
Die Platzkomplexität beträgt $O(\text{amount})$ für das 1D-DP-Array.

## Varianten & Optimierungen

- **Permutationen zählen (Climbing Stairs):** Was wäre, wenn uns die Reihenfolge wichtig wäre? Wenn `1+2` und `2+1` als zwei verschiedene Möglichkeiten gelten würden? Tauschen Sie einfach die **verschachtelten Schleifen!** Setzen Sie die `amount`-Schleife nach außen und die `coins`-Schleife nach innen. Dies erlaubt es, jede Münze zu jedem Zeitpunkt hinzuzufügen, wodurch alle Permutationen generiert werden! Dies ist die exakte Logik hinter `dp_02_climbing-stairs`.

## Anwendungen in der Praxis

- **Kassensysteme:** Bestimmung, ob in einem gegebenen Satz von Währungsnennwerten genügend mathematische Liquidität vorhanden ist, um für beliebige Transaktionen das exakte Wechselgeld bereitzustellen.

## Verwandte Algorithmen in cOde(n)

- **[dp_05 - Coin Change](dp_05_coin-change.md)** — Die Optimierungsvariante, die nach der minimalen Anzahl an Münzen fragt.
- **[dp_03 - 0/1 Knapsack](dp_03_knapsack.md)** — Die beschränkte Variante, bei der jeder Gegenstand nur einmal verwendet werden kann (was eine rückwärts gerichtete Iteration der inneren Schleife anstelle einer vorwärts gerichteten verwendet).

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*