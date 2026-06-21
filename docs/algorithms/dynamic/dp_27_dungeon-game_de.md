# Dungeon Game

| | |
|---|---|
| **ID** | `dp_27` |
| **Category** | dynamic |
| **Complexity (required)** | $O(M * N)$ Time, $O(N)$ Space |
| **Difficulty** | 7/10 |
| **Interview relevance** | 6/10 |
| **LeetCode Equivalent** | [Dungeon Game](https://leetcode.com/problems/dungeon-game/) |

## Problem statement

Die Dämonen haben die Prinzessin gefangen genommen und sie in der unteren rechten Ecke eines Dungeons eingesperrt. Der Dungeon besteht aus `m x n` Räumen, die in einem 2D-Gitter angeordnet sind. Unser tapferer Ritter startet im oberen linken Raum.
Der Ritter kann sich nur **nach unten** oder **nach rechts** bewegen.
Einige Räume enthalten Dämonen (negative Ganzzahlen), die die Lebensenergie des Ritters verringern. Andere Räume enthalten magische Kugeln (positive Ganzzahlen), die die Lebensenergie des Ritters erhöhen.
Die Lebensenergie des Ritters muss zu jedem Zeitpunkt $\ge 1$ sein. Wenn seine Lebensenergie auf 0 oder darunter fällt, stirbt er sofort.
Geben Sie die **minimale anfängliche Lebensenergie** zurück, die der Ritter benötigt, um die Prinzessin erfolgreich zu retten.

**Eingabe:** Eine `m x n` Ganzzahlmatrix `dungeon`.
**Ausgabe:** Eine Ganzzahl, die die erforderliche minimale Start-Lebensenergie darstellt.

## Wann man es verwendet

- Um die Beherrschung von **Backwards DP** (rückwärts gerichtete dynamische Programmierung) zu demonstrieren.
- Wenn ein Pfadfindungsproblem eine strikte Nicht-Negativitäts-Bedingung hat, schlägt Forward DP fehl, da lokale Maxima möglicherweise nicht zu einer globalen Gültigkeit führen.

## Ansatz

**1. Der Fehler von Forward DP:**
Wenn wir bei `(0,0)` starten und versuchen, die "minimale Lebensenergie, die benötigt wird, um `(i, j)` zu erreichen" zu verfolgen, stehen wir vor einem Paradoxon.
Wenn wir eine Zelle über zwei Pfade erreichen:
- Pfad A: Erfordert `10` anfängliche Lebensenergie, gibt aber aktuell `50` Bonus-Lebensenergie.
- Pfad B: Erfordert `5` anfängliche Lebensenergie, gibt aber aktuell `1` Bonus-Lebensenergie.
Welcher Pfad ist "besser"? Pfad B erfordert aktuell weniger Start-Lebensenergie, aber Pfad A bietet einen massiven Schutz gegen zukünftige Dämonen! Wir können hier keine lokale gierige Entscheidung (Greedy Choice) treffen!

**2. Backwards DP:**
Wir MÜSSEN bei der Prinzessin an `(M-1, N-1)` starten und uns rückwärts zum Ritter bei `(0,0)` vorarbeiten!
Sei `dp[i][j]` die **minimale Lebensenergie, die beim Betreten der Zelle `(i, j)` benötigt wird**, um die Prinzessin sicher zu erreichen.

**3. Den Induktionsanfang finden:**
In der Zelle der Prinzessin `(M-1, N-1)`:
- Wenn ihr Raum einen Dämon enthält (z. B. `-5`), benötigen wir genug Lebensenergie, um diesen zu überleben UND mindestens `1` Lebensenergie übrig zu haben. Wir benötigen also `6` Lebensenergie.
- Wenn ihr Raum eine Kugel enthält (z. B. `+5`), benötigen wir immer noch mindestens `1` Lebensenergie, um überhaupt lebend den Raum zu betreten.
Daher: `dp[M-1][N-1] = max(1, 1 - dungeon[M-1][N-1])`.

**4. Den Übergang finden (Die Rekursionsgleichung):**
Für jede interne Zelle `(i, j)` wird der Ritter diese Zelle zwangsläufig verlassen und sich entweder NACH UNTEN zu `(i+1, j)` oder NACH RECHTS zu `(i, j+1)` bewegen.
Um seine Start-Lebensenergie zu minimieren, sollte er den Pfad wählen, der WENIGER Lebensenergie erfordert!
Die Lebensenergie, die er *nach* dem Verlassen dieser Zelle benötigt, ist also: `min_health_on_exit = min(dp[i+1][j], dp[i][j+1])`.
Um die Lebensenergie zu berechnen, die *vor* dem Betreten von `(i, j)` benötigt wird, subtrahieren wir die Heilung/den Schaden von `(i, j)` von `min_health_on_exit`.
Wenn `dungeon[i][j]` ihn so stark heilt, dass die benötigte Lebensenergie negativ wird, setzen wir sie auf `1` fest (da er niemals $\le 0$ Lebensenergie haben darf).
`dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])`

**5. Platzoptimierung:**
Da die Berechnung der Zeile `i` nur die Zeile `i+1` erfordert, können wir die M x N Matrix in ein 1D-Array der Größe N+1 komprimieren.

## Algorithmus

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dp_27: Dungeon Game.

Backwards DP: dp[i][j] = min HP needed when entering (i,j)
to safely reach the princess. Fill from bottom-right to
top-left. Space-optimized to O(N) using a rolling 1D array.
"""


def solve(dungeon, m, n):
    INF = float("inf")
    dp = [INF] * (n + 1)
    dp[n - 1] = 1
    for i in range(m - 1, -1, -1):
        new_dp = [INF] * (n + 1)
        for j in range(n - 1, -1, -1):
            min_exit = min(dp[j], new_dp[j + 1])
            new_dp[j] = max(1, min_exit - dungeon[i][j])
        dp = new_dp
    return dp[0]
```

</details>

## Walk-through

`dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]`.
M=3, N=3. Initial `dp = [inf, inf, inf, inf]`.
Dummy setzen: `dp[2] = 1`. `dp = [inf, inf, 1, inf]`.

1. **i = 2 (Untere Zeile):**
   - `j=2` (Prinzessin, `-5`): `min_exit = min(1, inf) = 1`. `dp[2] = max(1, 1 - (-5)) = 6`. (Benötige 6 HP, um den -5 Dämon zu bekämpfen). `dp = [inf, inf, 6, inf]`.
   - `j=1` (`30`): `min_exit = min(inf, 6) = 6`. `dp[1] = max(1, 6 - 30) = 1`. (Kugel heilt 30, benötige nur 1 HP).
   - `j=0` (`10`): `min_exit = min(inf, 1) = 1`. `dp[0] = max(1, 1 - 10) = 1`.
   - `dp` Zustand: `[1, 1, 6, inf]`.

2. **i = 1 (Mittlere Zeile):**
   - `j=2` (`1`): `min_exit = min(6(unten), inf(rechts)) = 6`. `dp[2] = max(1, 6 - 1) = 5`.
   - `j=1` (`-10`): `min_exit = min(1(unten), 5(rechts)) = 1`. `dp[1] = max(1, 1 - (-10)) = 11`.
   - `j=0` (`-5`): `min_exit = min(1(unten), 11(rechts)) = 1`. `dp[0] = max(1, 1 - (-5)) = 6`.
   - `dp` Zustand: `[6, 11, 5, inf]`.

3. **i = 0 (Obere Zeile):**
   - `j=2` (`3`): `min_exit = min(5, inf) = 5`. `dp[2] = max(1, 5 - 3) = 2`.
   - `j=1` (`-3`): `min_exit = min(11, 2) = 2`. `dp[1] = max(1, 2 - (-3)) = 5`.
   - `j=0` (`-2`): `min_exit = min(6, 5) = 5`. `dp[0] = max(1, 5 - (-2)) = 7`.

Das Ergebnis `dp[0]` ist 7. ✓ (Der Ritter benötigt 7 HP als Startwert).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(M * N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(M * N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(M * N)$ | $O(N)$ |

Die verschachtelten Schleifen besuchen jede Zelle in der M x N Matrix genau einmal. Die Zeitkomplexität ist $O(M \times N)$.
Durch die Verwendung des 1D-Rolling-Arrays ist die Platzkomplexität $O(N)$ (wobei N die Anzahl der Spalten ist).

## Varianten & Optimierungen

- **Binäre Suche auf der Antwort:** Wenn es Ihnen schwerfällt, das Konzept der Backwards DP zu verstehen, können Sie dies tatsächlich mit Forward DP in Kombination mit Binärer Suche lösen! Sie führen eine binäre Suche auf der Start-Lebensenergie `H` durch (von 1 bis Unendlich). Für ein gegebenes `H` führen Sie eine Standard-Forward DP durch, um zu sehen, ob Sie das Ende erreichen können, ohne zu sterben. Dieser Ansatz benötigt $O(M \times N \times log(\text{MaxHealth}))$ Zeit, ist aber extrem intuitiv zu implementieren!

## Anwendungen in der Praxis

- **Logistik der Lieferkette:** Berechnung der minimalen anfänglichen Treibstoffmenge / des Kapitals, das für eine Fahrzeugflotte erforderlich ist, die durch ein Netzwerk von Städten reist, wobei einige Städte Mautgebühren (Dämonen) erheben und andere Tankzuschüsse (Kugeln) anbieten, um sicherzustellen, dass niemals ein Konkurs eintritt.

## Verwandte Algorithmen in cOde(n)

- **[dp_12 - Minimum Path Sum](dp_12_min-cost-path.md)** — Der grundlegende Forward DP-Algorithmus, den Sie bei diesem Problem umkehren müssen.
- **[searching_01 - Binary Search](../searching/search_01_binary-search.md)** — Der alternative $O(M \times N \times log(\text{Health}))$ Ansatz.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link oben auf der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*