# Münzwechsel (Anzahl der Möglichkeiten)

| | |
|---|---|
| **ID** | `dp_30` |
| **Kategorie** | dynamische Programmierung |
| **Komplexität (erforderlich)** | $O(n * amount)$ |
| **Schwierigkeitsgrad** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **LeetCode-Äquivalent** | [Münzwechsel II](https://leetcode.com/problems/coin-change-ii/) |

## Aufgabenstellung

Gegeben sei ein Array aus ganzen Zahlen `coins`, das Münzen verschiedener Nennwerte darstellt, sowie eine ganze Zahl `amount`, die den Gesamtbetrag angibt.
Gib die **Anzahl der eindeutigen Kombinationen** zurück, die diesen Betrag ergeben.
Es darf davon ausgegangen werden, dass von jeder Münzsorte eine unendliche Anzahl vorhanden ist.

**Eingabe:** Ein Array `coins` und eine ganze Zahl `amount`.
**Ausgabe:** Eine ganze Zahl, die die Gesamtzahl der Möglichkeiten angibt.

**Beispiel:**
`amount = 5`, `coins = [1, 2, 5]`.
Kombinationen: `5`, `2+2+1`, `2+1+1+1`, `1+1+1+1+1`.
Ausgabe: `4`.

## Wann man es verwendet

- Im Gegensatz zum Standardproblem „Münzwechsel“ (`dp_05`), bei dem die *minimale Anzahl an Münzen* gefragt ist (Optimierung), geht es hier um die *Gesamtzahl der Möglichkeiten* (Kombinatorik).
- Es handelt sich um eine direkte Anwendung des **unbegrenzten Rucksackproblems**.

## Vorgehensweise

Wir können ein eindimensionales DP-Array verwenden.
Sei `dp[j]` die Anzahl der Möglichkeiten, den Betrag `j` zu bilden.

Wenn wir nacheinander alle Münzwerte durchgehen, können wir fragen: „Wie viele *zusätzliche* Möglichkeiten gibt es, den Betrag `j` zu bilden, wenn ich diese aktuelle Münze einbeziehe?“
Die Antwort lautet: genauso viele Möglichkeiten, wie ich den Betrag `j - coin` bilden könnte!

Für jedes `coin` durchlaufen wir also alle Beträge `j` von `coin` bis `amount` und aktualisieren:
`dp[j] = dp[j] + dp[j - coin]`

**Warum durchlaufen wir die Münzen in der äußeren Schleife und die Beträge in der inneren Schleife?**
Weil wir **Kombinationen** wollen, keine **Permutationen**. Wir behandeln `2+1` und `1+2` auf genau dieselbe Weise.
Indem wir in der äußeren Schleife streng durch `coins` iterieren, erzwingen wir mathematisch eine Reihenfolge (z. B. fügen wir `2`s erst dann hinzu, wenn wir mit dem Hinzufügen aller `1`s vollständig fertig sind). Dies garantiert, dass wir `1+2` und `2+1` niemals getrennt generieren!

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

## Schritt-für-Schritt-Anleitung

`amount = 5`, `coins = [1, 2, 5]`.
`dp = [1, 0, 0, 0, 0, 0]` (Größe 6).

**Münze = 1:**
- `j=1`: `dp[1] += dp[0]` -> `1`.
- `j=2`: `dp[2] += dp[1]` -> `1`.
- ... `dp` wird zu `[1, 1, 1, 1, 1, 1]`. (1 Möglichkeit, jeden Betrag nur mit 1ern zu bilden).

**Münze = 2:**
- `j=2`: `dp[2] += dp[0]` -> `1 + 1 = 2`.
- `j=3`: `dp[3] += dp[1]` -> `1 + 1 = 2`.
- `j=4`: `dp[4] += dp[2]` -> `1 + 2 = 3`.
- `j=5`: `dp[5] += dp[3]` -> `1 + 2 = 3`.
- `dp` wird zu `[1, 1, 2, 2, 3, 3]`.

**Münze = 5:**
- `j=5`: `dp[5] += dp[0]` -> `3 + 1 = 4`.

Ausgabe: `dp[5] = 4`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(n * amount)$ | $O(amount)$ |
| **Durchschnittlicher Fall** | $O(n * amount)$ | $O(amount)$ |
| **Schlechtester Fall** | $O(n * amount)$ | $O(amount)$ |

Wir durchlaufen n Münzen. Für jede Münze durchlaufen wir bis zu `amount` Werten. Die gesamte Zeitkomplexität beträgt streng $O(n x \text{amount})$.
Die Platzkomplexität beträgt $O(\text{amount})$ für das 1D-DP-Array.

## Varianten & Optimierungen

- **Permutationen zählen (Treppensteigen):** Was wäre, wenn uns die Reihenfolge *doch* wichtig wäre? Wenn `1+2` und `2+1` als zwei verschiedene Wege betrachtet würden? **Tauschen Sie einfach die verschachtelten Schleifen aus!** Setzen Sie die `amount`-Schleife nach außen und die `coins`-Schleife nach innen. So kann jede Münze zu jedem Zeitpunkt hinzugefügt werden, wodurch alle Permutationen erzeugt werden! Genau das ist die Logik hinter `dp_02_climbing-stairs`.

## Anwendungen in der Praxis

- **Kassensoftware:** Ermittlung, ob in einem gegebenen Satz von Münzwerten ausreichend mathematische Liquidität vorhanden ist, um bei beliebigen Transaktionen passendes Wechselgeld bereitzustellen.

## Verwandte Algorithmen in cOde(n)

- **[dp_05 – Münzwechsel](dp_05_coin-change.md)** — Die Optimierungsvariante, bei der die minimale Anzahl an Münzen ermittelt wird.
- **[dp_03 – 0/1-Rucksack](dp_03_knapsack.md)** – Die begrenzte Variante, bei der jeder Gegenstand nur einmal verwendet werden kann (hierbei wird eine rückwärtsgerichtete Iteration der inneren Schleife anstelle einer vorwärtsgerichteten verwendet).

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
in Anlehnung an die kanonische Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
