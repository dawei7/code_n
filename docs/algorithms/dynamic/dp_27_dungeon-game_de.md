# Dungeon-Spiel

| | |
|---|---|
| **ID** | `dp_27` |
| **Kategorie** | dynamisch |
| **Komplexität (erforderlich)** | $O(M * N)$ Zeit, $O(N)$ Speicherplatz |
| **Schwierigkeitsgrad** | 7/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **LeetCode-Äquivalent** | [Dungeon-Spiel](https://leetcode.com/problems/dungeon-game/) |

## Aufgabenstellung

Die Dämonen hatten die Prinzessin gefangen genommen und sie in der rechten unteren Ecke eines Verlieses eingesperrt. Das Verlies besteht aus `m x n` Räumen, die in einem 2D-Raster angeordnet sind. Unser tapferer Ritter befand sich anfangs im Raum oben links.
Der Ritter kann sich nur **nach unten** oder **nach rechts** bewegen.
In einigen Räumen befinden sich Dämonen (negative ganze Zahlen), die die Lebenspunkte des Ritters verringern. In anderen Räumen befinden sich magische Kugeln (positive ganze Zahlen), die die Lebenspunkte des Ritters erhöhen.
Die Lebenspunkte des Ritters MÜSSEN zu jedem Zeitpunkt \ge 1 sein. Fällt seine Gesundheit auf 0 oder darunter, stirbt er sofort.
Gib die **minimale Anfangsgesundheit** des Ritters zurück, damit er die Prinzessin erfolgreich retten kann.

**Eingabe:** Eine `m x n` ganzzahlige Matrix `dungeon`.
**Ausgabe:** Eine ganze Zahl, die die erforderliche minimale Anfangsgesundheit angibt.

## Wann man diese Methode anwendet

- Um die Beherrschung der **rückwärtsgerichteten dynamischen Programmierung (Backwards DP)** zu demonstrieren.
- Wenn ein Wegfindungsproblem eine strenge, nicht-negative Laufbedingung aufweist, versagt die vorwärtsgerichtete dynamische Programmierung (Forward DP), da lokale Maxima möglicherweise nicht zur globalen Gültigkeit führen.

## Vorgehensweise

**1. Der Fehler der vorwärtsgerichteten DP:**
Wenn wir bei `(0,0)` beginnen und versuchen, die „minimal erforderliche Gesundheit zum Erreichen von `(i, j)`“ zu ermitteln, stoßen wir auf ein Paradoxon.
Wenn wir eine Zelle mit zwei Pfaden erreichen:
- Pfad A: Erfordert `10` Startgesundheit, gewährt dir aber derzeit `50` Bonusgesundheit.
- Weg B: Erfordert `5` Startgesundheit, gewährt dir aber derzeit `1` Bonusgesundheit.
Welcher Weg ist „besser“? Weg B erfordert im Moment weniger Startgesundheit, aber Weg A verschafft dir einen massiven Schutzschild gegen zukünftige Dämonen! Wir können keine lokal optimierte, gierige Entscheidung für den weiteren Verlauf treffen!

**2. Rückwärts-DP:**
Wir MÜSSEN bei der Prinzessin bei `(M-1, N-1)` beginnen und rückwärts zum Ritter bei `(0,0)` vorgehen!
Sei `dp[i][j]` die **erforderliche Mindestgesundheit** beim Betreten der Zelle `(i, j)` sein, um die Prinzessin sicher zu erreichen.

**3. Den Basisfall finden:**
In der Zelle der Prinzessin `(M-1, N-1)`:
- Befindet sich in ihrem Raum ein Dämon (z. B. `-5`), benötigen wir genügend Lebenspunkte, um ihn zu überleben UND mindestens `1` Lebenspunkte übrig zu haben. Wir benötigen also `6` Lebenspunkte.
- Befindet sich in ihrem Raum eine Kugel (z. B. `+5`), benötigen wir immer noch mindestens `1` Lebenspunkte, um vor dem Betreten am Leben zu bleiben.
Daher gilt: `dp[M-1][N-1] = max(1, 1 - dungeon[M-1][N-1])`.

**4. Den Übergang finden (die Rekursionsrelation):**
Von jeder inneren Zelle `(i, j)` aus wird der Springer diese Zelle unweigerlich verlassen und sich entweder nach UNTEN zu `(i+1, j)` oder nach RECHTS zu `(i, j+1)` bewegen.
Um seine Startgesundheit zu minimieren, sollte er den Weg wählen, der WENIGER Gesundheit erfordert!
Die Gesundheit, die er also *nach* dem Verlassen dieser Zelle benötigt, beträgt: `min_health_on_exit = min(dp[i+1][j], dp[i][j+1])`.
Um die *vor* dem Betreten von `(i, j)` benötigte Gesundheit zu berechnen, ziehen wir die Heilung/den Schaden von `(i, j)` von `min_health_on_exit` ab.
Wenn `dungeon[i][j]` ihn so stark heilt, dass die erforderliche Gesundheit negativ wird, begrenzen wir sie auf `1` (da er niemals eine Gesundheit von \le 0 haben kann).
`dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])`

**5. Speicherplatzoptimierung:**
Da zur Berechnung der Zeile `i` nur die Zeile `i+1` benötigt wird, können wir die M × N-Matrix in ein eindimensionales Array der Größe N+1 komprimieren.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

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

## Schritt-für-Schritt-Anleitung

`dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]`.
M=3, N=3. Ausgangszustand `dp = [inf, inf, inf, inf]`.
Dummy setzen: `dp[2] = 1`. `dp = [inf, inf, 1, inf]`.

1. **i = 2 (untere Reihe):**
   - `j=2` (Prinzessin, `-5`): `min_exit = min(1, inf) = 1`. `dp[2] = max(1, 1 - (-5)) = 6`. (Man benötigt 6 HP, um gegen den -5-Dämon zu kämpfen). `dp = [inf, inf, 6, inf]`.
   - `j=1`(`30`): `min_exit = min(inf, 6) = 6`. `dp[1] = max(1, 6 - 30) = 1`. (Die Kugel heilt 30, man benötigt nur 1 HP).
   - `j=0`(`10`): `min_exit = min(inf, 1) = 1`. `dp[0] = max(1, 1 - 10) = 1`.
   - `dp`-Zustand: `[1, 1, 6, inf]`.

2. **i = 1 (mittlere Reihe):**
   - `j=2`(`1`): `min_exit = min(6(down), inf(right)) = 6`. `dp[2] = max(1, 6 - 1) = 5`.
   - `j=1`(`-10`): `min_exit = min(1(down), 5(right)) = 1`. `dp[1] = max(1, 1 - (-10)) = 11`.
   - `j=0`(`-5`): `min_exit = min(1(down), 11(right)) = 1`. `dp[0] = max(1, 1 - (-5)) = 6`.
   - `dp` Zustand: `[6, 11, 5, inf]`.

3. **i = 0 (oberste Zeile):**
   - `j=2`(`3`): `min_exit = min(5, inf) = 5`. `dp[2] = max(1, 5 - 3) = 2`.
   - `j=1`(`-3`): `min_exit = min(11, 2) = 2`. `dp[1] = max(1, 2 - (-3)) = 5`.
   - `j=0`(`-2`): `min_exit = min(6, 5) = 5`. `dp[0] = max(1, 5 - (-2)) = 7`.

Das Ergebnis `dp[0]` ist 7. ✓ (Der Ritter benötigt zu Beginn 7 HP).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestwert** | $O(M * N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(M * N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(M * N)$ | $O(N)$ |

Die verschachtelten Schleifen durchlaufen jede Zelle der M × N-Matrix genau einmal. Die Laufzeit beträgt $O(M \times N)$.
Durch die Verwendung des eindimensionalen rollenden Arrays beträgt der Speicherbedarf $O(N)$ (wobei N die Anzahl der Spalten ist).

## Varianten & Optimierungen

- **Binäre Suche nach der Lösung:** Wenn du Schwierigkeiten hast, die Rückwärts-DP zu verstehen, kannst du diese Aufgabe tatsächlich mit einer Vorwärts-DP in Kombination mit einer binären Suche lösen! Du führst eine binäre Suche auf die Startgesundheit `H` (von 1 bis unendlich). Für einen gegebenen `H` führst du eine standardmäßige Vorwärts-DP durch, um zu prüfen, ob du das Ziel erreichen kannst, ohne zu sterben. Dieser Ansatz benötigt $O(M x N x log(\text{MaxHealth})$) Zeit, ist aber äußerst intuitiv zu programmieren!

## Anwendungen in der Praxis

- **Lieferkettenlogistik:** Berechnung des minimalen Anfangsbedarfs an Kraftstoff bzw. Kapital für eine Fahrzeugflotte, die durch ein Netzwerk von Städten fährt, wobei in einigen Städten Mautgebühren (Dämonen) anfallen und andere Städte Tankzuschüsse (Kugeln) gewähren, um sicherzustellen, dass es niemals zu einer Insolvenz kommt.

## Verwandte Algorithmen in cOde(n)

- **[dp_12 – Minimale Pfadsumme](dp_12_min-cost-path.md)** — Der grundlegende Forward-DP-Algorithmus, den man bei diesem Problem umkehren muss.
- **[searching_01 – Binäre Suche](../searching/search_01_binary-search.md)** – Der alternative Ansatz $O(M x N log(\text{Health})$).

---

*Diese Dokumentation ist ein Originalbeitrag für cOde(n),
der sich an der kanonischen Struktur orientiert, die von Referenzseiten
zum Thema Wettbewerbsprogrammierung verwendet wird. Den kanonischen
Enzyklopädieeintrag finden Sie unter dem Wikipedia-Link oben auf der Seite.
Quell-Repository:
<https://github.com/dawei7/code_n>.*
