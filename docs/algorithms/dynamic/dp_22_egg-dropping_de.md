# Egg Dropping (Mathematisch $O(K log N)$)

| | |
|---|---|
| **ID** | `dp_22` |
| **Kategorie** | dynamic |
| **Komplexität (erforderlich)** | $O(K log N)$ Zeit, $O(K)$ Platz |
| **Schwierigkeit** | 9/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **LeetCode-Äquivalent** | [Super Egg Drop](https://leetcode.com/problems/super-egg-drop/) |

## Problemstellung

Gegeben sind `k` identische Eier und ein Gebäude mit `n` Stockwerken. Finden Sie die minimale Anzahl an Würfen, die erforderlich ist, um im Schlechtesten Fall das kritische Stockwerk zu bestimmen, ab dem ein Ei zerbricht.
Der Standard-DP-Ansatz (`dp_16`) löst dies in $O(K x N^2)$. Sie müssen dieses Problem optimal lösen und Eingaben bis zu N = 10.000 effizient verarbeiten.

**Eingabe:** Zwei Ganzzahlen `k` (Eier) und `n` (Stockwerke).
**Ausgabe:** Eine Ganzzahl, die die minimale Anzahl an Würfen repräsentiert.

## Wann man diesen Ansatz verwendet

- Um einen Interviewer zu beeindrucken, indem der DP-Zustand eines klassischen Problems vollständig transformiert wird, um die asymptotischen Schranken drastisch zu reduzieren.
- Dies ist eine Meisterklasse in "Zustandsinversion" (State Inversion).

## Ansatz

**1. Der Fehler des Standard-DP:**
Der Standardansatz fragt: *"Gegeben `e` Eier und `f` Stockwerke, was ist die minimale Anzahl an Würfen `m`?"*
`dp[eggs][floors] = moves`.
Dies zwingt uns dazu, jedes mögliche Stockwerk `x` zu iterieren, um den Schlechtesten Fall zu minimieren, was den $O(N^2)$-Flaschenhals verursacht.

**2. Zustandsinversion:**
Drehen wir die Fragestellung um:
*"Gegeben `m` Würfe und `e` Eier, was ist die MAXIMALE Anzahl an Stockwerken `f`, die wir testen können?"*
Sei `dp[m][e]` die maximale Anzahl an Stockwerken, die wir mit `m` Würfen und `e` Eiern testen können.

**3. Finden des Übergangs (Die Rekurrenz):**
Angenommen, wir führen 1 Wurf von einem bestimmten Stockwerk aus. Es gibt zwei Ergebnisse:
- **Wenn es zerbricht:** Wir haben 1 Wurf verbraucht und 1 Ei verloren. Wir haben nun `m-1` Würfe und `e-1` Eier übrig. Die maximale Anzahl an Stockwerken, die wir sicher *unter* uns testen können, ist genau `dp[m-1][e-1]`.
- **Wenn es überlebt:** Wir haben 1 Wurf verbraucht und das Ei behalten. Wir haben nun `m-1` Würfe und `e` Eier übrig. Die maximale Anzahl an Stockwerken, die wir sicher *über* uns testen können, ist genau `dp[m-1][e]`.

Daher ist die gesamte maximale Anzahl an Stockwerken, die wir testen können, die Anzahl der Stockwerke unter uns, PLUS die Stockwerke über uns, PLUS das 1 Stockwerk, von dem wir gerade geworfen haben!
`dp[m][e] = dp[m-1][e-1] + dp[m-1][e] + 1`

**4. Die Strategie:**
Wir kennen die erforderlichen Würfe `m` noch nicht! Also beginnen wir bei `m = 1` und erhöhen `m` kontinuierlich.
Wir berechnen `dp[m][k]` für unsere Gesamtzahl an `k` Eiern.
In dem Moment, in dem `dp[m][k] >= n` gilt, haben wir genug Würfe erreicht, um alle `n` Stockwerke zu testen. Dieses `m` ist unsere Antwort!

**5. Platzoptimierung:**
Beachten Sie, dass `dp[m]` nur von `dp[m-1]` abhängt. Wir können dies auf ein 1D-Array der Größe `K+1` komprimieren! Genau wie beim 0/1 Knapsack müssen wir die Eier `e` rückwärts iterieren.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dp_22: Egg Dropping.

Return the minimum number of trials needed in the worst
case to find the critical floor. dp[e][f] = min trials for
e eggs and f floors. Drop from floor x -> 1 + worst(
dp[e-1][x-1], dp[e][f-x]).
"""


def solve(eggs, floors):
    if floors == 0:
        return 0
    if eggs == 1:
        return floors
    dp = [[0] * (floors + 1) for _ in range(eggs + 1)]
    for f in range(1, floors + 1):
        dp[1][f] = f
    for e in range(2, eggs + 1):
        for f in range(1, floors + 1):
            best = f
            for x in range(1, f + 1):
                worst = 1 + max(dp[e - 1][x - 1], dp[e][f - x])
                if worst < best:
                    best = worst
            dp[e][f] = best
    return dp[eggs][floors]
```

</details>

## Durchlauf

`k = 2` Eier, `n = 6` Stockwerke.
`dp = [0, 0, 0]` (Größe 3).

1. **moves = 1:**
   - `e=2`: `dp[2] = dp[1] + dp[2] + 1 = 0 + 0 + 1 = 1`.
   - `e=1`: `dp[1] = dp[0] + dp[1] + 1 = 0 + 0 + 1 = 1`.
   - `dp = [0, 1, 1]`. (Max 1 Stockwerk getestet). `1 < 6`. Schleife fortsetzen!
2. **moves = 2:**
   - `e=2`: `dp[2] = dp[1](alt) + dp[2](alt) + 1 = 1 + 1 + 1 = 3`.
   - `e=1`: `dp[1] = dp[0] + dp[1] + 1 = 0 + 1 + 1 = 2`.
   - `dp = [0, 2, 3]`. (Max 3 Stockwerke getestet). `3 < 6`. Schleife fortsetzen!
3. **moves = 3:**
   - `e=2`: `dp[2] = dp[1](alt) + dp[2](alt) + 1 = 2 + 3 + 1 = 6`.
   - `e=1`: `dp[1] = dp[0] + dp[1] + 1 = 0 + 2 + 1 = 3`.
   - `dp = [0, 3, 6]`. `6 >= 6`! Schleife abbrechen.

Ausgabe `moves = 3`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(K log N)$ | $O(K)$ |
| **Durchschnittlicher Fall** | $O(K log N)$ | $O(K)$ |
| **Schlechtester Fall** | $O(K log N)$ | $O(K)$ |

Wie viele Würfe `m` sind erforderlich? Im absoluten Schlechtesten Fall (k=1) ist `m=N`. Für jedes $K \ge 2$ wächst das DP-Array jedoch exponentiell schnell! Die maximale Anzahl an benötigten Würfen wird niemals etwa $O(\log N)$ oder $\sqrt{N}$ überschreiten.
Innerhalb der while-Schleife führen wir eine innere Schleife der Größe `K` aus.
Daher ist die Zeitkomplexität phänomenal schnell: $O(K log N)$.
Die Platzkomplexität beträgt strikt $O(K)$ für das 1D-Array.

## Varianten & Optimierungen

- **Reine mathematische Kombinatorik ($O(K)$):** Die Zustandsübergänge `dp[e] = dp[e-1] + dp[e] + 1` lassen sich mathematisch perfekt auf Binomialkoeffizienten abbilden. Der Wert von `dp[m][k]` ist exakt $\sum_{i=1}^{k} \binom{m}{i}$. Sie können den Wert `m` von 1 bis `N` binär suchen und für jedes `m` die Summe der Binomialkoeffizienten in $O(K)$ Zeit berechnen. Die Gesamtzeit beträgt dann $O(K log N)$, jedoch mit strikt $O(1)$ Platz!

## Anwendungen in der Praxis

- **Algorithmen-Theorie:** Hier geht es weniger um praktische Anwendungen, sondern vielmehr darum, die Kunst der "Zustandsinversion" in der Dynamischen Programmierung zu meistern, um rechnerische Flaschenhälse zu durchbrechen.

## Verwandte Algorithmen in cOde(n)

- **[dp_16 - Egg Dropping Puzzle](dp_16_egg-dropping.md)** — Der klassische $O(K x N^2)$ Min-Max-Ansatz, den dieser Algorithmus optimiert.
- **[dp_03 - 0/1 Knapsack](dp_03_knapsack.md)** — Vermittelt die hier verwendete 1D-Platzoptimierung durch Rückwärts-Iteration.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) erstellt wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*