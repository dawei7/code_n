# Eierfall (Mathematik $O(K log N)$)

| | |
|---|---|
| **ID** | `dp_22` |
| **Kategorie** | dynamisch |
| **Komplexität (erforderlich)** | $O(K log N)$ Zeit, $O(K)$ Speicherplatz |
| **Schwierigkeitsgrad** | 9/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **LeetCode-Äquivalent** | [Super Egg Drop](https://leetcode.com/problems/super-egg-drop/) |

## Aufgabenstellung

Du erhältst `k` identische Eier und ein Gebäude mit `n` Stockwerken. Ermitteln Sie die minimale Anzahl an Fallversuchen, die erforderlich ist, um im schlimmsten Fall garantiert die kritische Stockwerkhöhe zu ermitteln, in der das Ei zerbricht.
Der Standardansatz der dynamischen Programmierung (`dp_16`) löst diese Aufgabe in $O(K x N^2)$. Sie müssen diese Aufgabe optimal lösen und dabei Eingaben mit N = 10.000 berücksichtigen.

**Eingabe:** Zwei ganze Zahlen `k` (Eier) und `n` (Stockwerke).
**Ausgabe:** Eine ganze Zahl, die die minimale Anzahl an Fallversuchen angibt.

## Wann man es anwendet

- Um einen Interviewer zu beeindrucken, indem man den DP-Zustand eines klassischen Problems vollständig umkehrt, um die asymptotischen Grenzen drastisch zu reduzieren.
- Dies ist eine Meisterklasse in „Zustandsumkehr“.

## Vorgehensweise

**1. Der Fehler der Standard-DP:**
Der Standardansatz lautet: *„Bei `e` Eiern und `f` Etagen: Wie viele Fallvorgänge `m` sind mindestens erforderlich?“*
`dp[eggs][floors] = moves`.
Dies zwingt uns dazu, alle möglichen Stockwerke `x` durchzugehen, um den Worst-Case-Fall zu minimieren, was den $O(N^2)$ Engpass verursacht.

**2. Zustandsumkehr:**
Drehen wir die Frage einmal um:
*„Bei `m` Zügen und `e` Eiern: Wie viele Etagen `f` können wir maximal testen?“*
Sei `dp[m][e]` die maximale Anzahl an Etagen, die wir mit `m` Zügen und `e` Eiern testen können.

**3. Den Übergang finden (die Rekursionsbeziehung):**
Angenommen, wir lassen 1 Ei von einer beliebigen Etage fallen. Es gibt zwei mögliche Ergebnisse:
- **Wenn es zerbricht:** Wir haben 1 Zug verbraucht und 1 Ei verloren. Wir haben nun `m-1` Züge und `e-1` Eier. Die maximale Anzahl an Stockwerken, die wir sicher *unterhalb* von uns testen können, beträgt genau `dp[m-1][e-1]`.
- **Wenn es überlebt:** Wir haben 1 Zug verbraucht und das Ei behalten. Wir haben nun `m-1` Züge und `e` Eier. Die maximale Anzahl an Stockwerken, die wir sicher *über* uns testen können, beträgt genau `dp[m-1][e]`.

Daher ist die Gesamtzahl der Stockwerke, die wir testen können, die Summe aus den Stockwerken unter uns, den Stockwerken über uns und dem einen Stockwerk, von dem wir gerade heruntergefallen sind!
`dp[m][e] = dp[m-1][e-1] + dp[m-1][e] + 1`

**4. Die Strategie:**
Wir kennen die erforderliche Anzahl an Zügen `m` noch nicht! Also fangen wir einfach bei `m = 1` an und erhöhen `m` immer weiter.
Wir berechnen `dp[m][k]` für unsere Gesamtzahl von `k` Eiern.
In dem Moment, in dem `dp[m][k] >= n` eintritt, bedeutet das, dass wir endlich genug Züge erreicht haben, um alle `n` Stockwerke zu testen. Das `m` ist unsere Antwort!

**5. Speicherplatzoptimierung:**
Beachte, dass `dp[m]` nur von `dp[m-1]` abhängt. Wir können dies auf ein eindimensionales Array der Größe `K+1` komprimieren! Genau wie beim 0/1-Rucksack-Problem müssen wir die Eier `e` rückwärts durchlaufen.

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

## Schritt-für-Schritt-Anleitung

`k = 2` Eier, `n = 6` Etagen.
`dp = [0, 0, 0]` (Größe 3).

1. **Züge = 1:**
   - `e=2`: `dp[2] = dp[1] + dp[2] + 1 = 0 + 0 + 1 = 1`.
   - `e=1`: `dp[1] = dp[0] + dp[1] + 1 = 0 + 0 + 1 = 1`.
   - `dp = [0, 1, 1]`. (Max. 1 Etage getestet). `1 < 6`. Wiederholen!
2. **Züge = 2:**
   - `e=2`: `dp[2] = dp[1](old) + dp[2](old) + 1 = 1 + 1 + 1 = 3`.
   - `e=1`: `dp[1] = dp[0] + dp[1] + 1 = 0 + 1 + 1 = 2`.
   - `dp = [0, 2, 3]`. (Max. 3 Stockwerke getestet). `3 < 6`. Wiederholen!
3. **Züge = 3:**
   - `e=2`: `dp[2] = dp[1](old) + dp[2](old) + 1 = 2 + 3 + 1 = 6`.
   - `e=1`: `dp[1] = dp[0] + dp[1] + 1 = 0 + 2 + 1 = 3`.
   - `dp = [0, 3, 6]`. `6 >= 6`! Schleife abbrechen.

Ausgabe `moves = 3`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestwert** | $O(K log N)$ | $O(K)$ |
| **Durchschnittlicher Fall** | $O(K log N)$ | $O(K)$ |
| **Schlechtester Fall** | $O(K log N)$ | $O(K)$ |

Wie viele Züge m sind erforderlich? Im absolut schlimmsten Fall (k=1) gilt m=N. Für jedes K \ge 2 wächst das DP-Array jedoch exponentiell schnell! Die maximal erforderliche Anzahl an Zügen wird niemals etwa $O(\log N)$ oder \sqrt{N} überschreiten.
Innerhalb der while-Schleife führen wir eine innere Schleife der Größe K aus.
Somit ist die Zeitkomplexität phänomenal schnell: $O(K log N)$.
Die Platzkomplexität beträgt für das 1D-Array streng $O(K)$.

## Varianten & Optimierungen

- **Reine mathematische Kombinatorik ($O(K)$):** Die Zustandsübergänge `dp[e] = dp[e-1] + dp[e] + 1` lassen sich mathematisch perfekt auf Binomialkoeffizienten abbilden. Der Wert von `dp[m][k]` ist genau \sum_{i=1}^{k} \binom{m}{i}. Man kann den Wert m von 1 bis N binär suchen und für jedes m die Summe der Binomialkoeffizienten in $O(K)$-Zeit berechnen. Die Gesamtzeit beträgt $O(K log N)$, jedoch bei streng $O(1)$ Speicherplatz!

## Anwendungen in der Praxis

- **Algorithmus-Entwurfstheorie:** Hier geht es weniger um praktische Anwendungen, sondern ausschließlich darum, die Kunst der „Zustandsumkehr“ in der dynamischen Programmierung zu beherrschen, um Rechenengpässe zu überwinden.

## Verwandte Algorithmen in cOde(n)

- **[dp_16 – Eierfall-Rätsel](dp_16_egg-dropping.md)** — Der klassische $O(K x N^2)$ Min-Max-Ansatz, den dieser Algorithmus optimiert.
- **[dp_03 – 0/1-Rucksack](dp_03_knapsack.md)** – Vermittelt die hier verwendete 1D-Optimierung durch Rückwärtsiteration.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
in Anlehnung an die kanonische Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
