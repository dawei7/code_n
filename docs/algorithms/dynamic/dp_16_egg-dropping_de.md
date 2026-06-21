# Egg Dropping Puzzle

| | |
|---|---|
| **ID** | `dp_16` |
| **Kategorie** | dynamic |
| **Komplexität (erforderlich)** | $O(K * N^2)$ Zeit, $O(K * N)$ Platz |
| **Schwierigkeit** | 8/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **LeetCode-Äquivalent** | [Super Egg Drop](https://leetcode.com/problems/super-egg-drop/) |

## Problemstellung

Gegeben sind `k` identische Eier und ein Gebäude mit `n` Stockwerken, die von `1` bis `n` nummeriert sind.
Es ist bekannt, dass es ein Stockwerk `f` ($0 \le f \le n$) gibt, sodass jedes Ei, das aus einem Stockwerk höher als `f` geworfen wird, zerbricht, während jedes Ei, das aus einem Stockwerk bei oder unter `f` geworfen wird, nicht zerbricht.
In jedem Zug darfst du ein unversehrtes Ei nehmen und es aus einem beliebigen Stockwerk `x` ($1 \le x \le n$) werfen.
Wenn das Ei zerbricht, kannst du es nicht mehr verwenden. Wenn das Ei jedoch nicht zerbricht, kannst du es in zukünftigen Zügen wiederverwenden.
Gib die **minimale Anzahl an Zügen** zurück, die du benötigst, um mit Sicherheit den Wert von `f` zu bestimmen.

**Eingabe:** Zwei Ganzzahlen `k` (Eier) und `n` (Stockwerke).
**Ausgabe:** Eine Ganzzahl, die die minimale Anzahl an Zügen im schlimmsten Fall darstellt.

## Wann man es verwendet

- Das kanonische "Minimax"-Problem der dynamischen Programmierung.
- Testet deine Fähigkeit, mit Worst-Case-Szenarien ("mit Sicherheit") umzugehen und gleichzeitig deine Strategie zu optimieren, um diesen Worst-Case zu minimieren.

## Ansatz

**1. Den Zustand definieren:**
Sei `dp[e][f]` die minimale Anzahl an Versuchen, die benötigt werden, um das kritische Stockwerk mit genau `e` Eiern und einem Gebäude mit genau `f` Stockwerken zu finden.

**2. Die Basisfälle finden:**
- Wenn du 1 Ei hast (`e = 1`), hast du keine andere Wahl, als bei Stockwerk 1 zu beginnen und dich Stockwerk für Stockwerk nach oben zu arbeiten. Im schlimmsten Fall benötigt dies `f` Würfe. `dp[1][f] = f`.
- Wenn du 0 oder 1 Stockwerk hast (`f = 0` oder `f = 1`), benötigt dies 0 bzw. 1 Wurf, unabhängig davon, wie viele Eier du hast. `dp[e][0] = 0` und `dp[e][1] = 1`.

**3. Den Übergang finden (Die Rekurrenz):**
Wenn du `e` Eier und `f` Stockwerke hast, kannst du wählen, dein nächstes Ei aus *einem beliebigen* Stockwerk `x` ($1 \le x \le f$) zu werfen.
Wenn du ein Ei aus Stockwerk `x` wirfst, gibt es genau zwei physikalische Ergebnisse:
- **Fall A (Das Ei zerbricht):** Das kritische Stockwerk MUSS strikt unter `x` liegen. Du hast nun `e - 1` Eier und es bleiben `x - 1` Stockwerke zu überprüfen. Die benötigten Versuche sind `dp[e - 1][x - 1]`.
- **Fall B (Das Ei überlebt):** Das kritische Stockwerk MUSS bei `x` oder darüber liegen. Du hast weiterhin `e` Eier und es bleiben `f - x` Stockwerke zu überprüfen. Die benötigten Versuche sind `dp[e][f - x]`.

Da wir die Antwort *mit Sicherheit* (Worst-Case) wissen müssen, wird uns die Natur immer in das schlechtere der beiden Ergebnisse zwingen!
Für ein spezifisches Stockwerk `x` sind die Versuche im schlimmsten Fall also: `1 + max(dp[e - 1][x - 1], dp[e][f - x])`.
Aber DU darfst wählen, aus welchem Stockwerk `x` du wirfst! Da du klug bist, wirst du das `x` wählen, das dieses Worst-Case-Szenario minimiert!
`dp[e][f] = 1 + min_{1 \le x \le f}( max(dp[e - 1][x - 1], dp[e][f - x]) )`

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dp_16: Egg Dropping.

dp[e][m] = max floors testable with e eggs and m moves.
Find smallest m with dp[k][m] >= n.
"""


def solve(k, n):
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    m = 0
    while dp[k][m] < n:
        m += 1
        for e in range(1, k + 1):
            dp[e][m] = dp[e - 1][m - 1] + dp[e][m - 1] + 1
    return m
```

</details>

## Durchlauf

`k = 2` Eier, `n = 4` Stockwerke.
Basisfälle sind bereits ausgefüllt:
- `dp[1][1..4] = [1, 2, 3, 4]` (1 Ei benötigt bis zu f Würfe).
- `dp[2][0] = 0, dp[2][1] = 1`.

Berechne `e = 2`, `f = 2`:
- Wurf bei x=1: `1 + max(dp[1][0], dp[2][1]) = 1 + max(0, 1) = 2`.
- Wurf bei x=2: `1 + max(dp[1][1], dp[2][0]) = 1 + max(1, 0) = 2`.
- `dp[2][2] = min(2, 2) = 2`.

Berechne `e = 2`, `f = 3`:
- Wurf x=1: `1 + max(dp[1][0], dp[2][2]) = 1 + max(0, 2) = 3`.
- Wurf x=2: `1 + max(dp[1][1], dp[2][1]) = 1 + max(1, 1) = 2`. (Optimal!)
- Wurf x=3: `1 + max(dp[1][2], dp[2][0]) = 1 + max(2, 0) = 3`.
- `dp[2][3] = min(3, 2, 3) = 2`.

Berechne `e = 2`, `f = 4`:
- Wurf x=1: `1 + max(dp[1][0], dp[2][3]) = 1 + max(0, 2) = 3`.
- Wurf x=2: `1 + max(dp[1][1], dp[2][2]) = 1 + max(1, 2) = 3`.
- Wurf x=3: `1 + max(dp[1][2], dp[2][1]) = 1 + max(2, 1) = 3`.
- Wurf x=4: `1 + max(dp[1][3], dp[2][0]) = 1 + max(3, 0) = 4`.
- `dp[2][4] = 3`.

Das Ergebnis ist 3. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(K * N^2)$ | $O(K * N)$ |
| **Durchschnittlicher Fall** | $O(K * N^2)$ | $O(K * N)$ |
| **Schlechtester Fall** | $O(K * N^2)$ | $O(K * N)$ |

Die Tabelle ist K x N groß. Für jede Zelle läuft die x-Schleife bis zu N-mal. Die Zeitkomplexität beträgt $O(K * N^2)$.
Der Platzbedarf beträgt exakt $O(K * N)$ für die DP-Matrix.

## Varianten & Optimierungen

- **Binäre Suche Optimierung ($O(K * N \log N)$):** Beachte, dass innerhalb der `x`-Schleife `dp[e - 1][x - 1]` strikt *ansteigend* ist, während `x` wächst, und `dp[e][f - x]` strikt *abnehmend* ist, während `x` wächst. Das optimale `x` liegt genau dort, wo sich diese beiden Funktionen schneiden! Du kannst eine binäre Suche anstelle eines linearen Scans verwenden, um `x` zu finden, was die Zeitkomplexität drastisch senkt.
- **Invertierte Zustands-DP ($O(K * \log N)$):** Die ultimative mathematische Optimierung. Anstatt `dp[eggs][floors] = moves` zu definieren, kehre die Definition um! Sei `dp[moves][eggs] = max_floors`. Du kannst bis zu `dp[m][e] = 1 + dp[m-1][e-1] + dp[m-1][e]` Stockwerke überprüfen. Du erhöhst einfach `m`, bis `dp[m][K] >= N`. Dies erfordert nur $O(K)$ Platz und läuft im Wesentlichen sofort!

## Anwendungen in der Praxis

- **Stresstests / Qualitätssicherung:** Bestimmung der maximalen sicheren Belastungsgrenze (Temperatur, Spannung, Druck) für eine physische Komponente, bei der die Zerstörung der Komponente während des Tests sehr teuer ist (begrenzte "Eier").

## Verwandte Algorithmen in cOde(n)

- **[dp_13 - Matrix Chain Multiplication](dp_13_matrix-chain-multiplication.md)** — Ein weiteres Problem, bei dem man eine dritte Variable `k` (oder `x`) innerhalb des DP-Zustands iterieren muss, um einen optimalen Teilungspunkt zu finden.
- **[searching_01 - Binary Search](../searching/search_01_binary-search.md)** — Das $O(\log N)$ Kernkonzept des sicheren Eliminierens der Hälfte des Suchraums, das das Egg Dropping unter begrenzten Ressourcen zu imitieren versucht.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Seiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*