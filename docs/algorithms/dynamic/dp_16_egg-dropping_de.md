# Eierfall-Rätsel

| | |
|---|---|
| **ID** | `dp_16` |
| **Kategorie** | dynamisch |
| **Komplexität (erforderlich)** | $O(K * N^2)$ Zeit, $O(K * N)$ Speicherplatz |
| **Schwierigkeitsgrad** | 8/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **LeetCode-Äquivalent** | [Super Egg Drop](https://leetcode.com/problems/super-egg-drop/) |

## Aufgabenstellung

Du erhältst `k` identische Eier und hast Zugang zu einem Gebäude mit `n` Stockwerken, die von `1` bis `n` nummeriert sind.
Du weißt, dass es eine Etage `f` (0 \le f \le n) gibt, sodass jedes Ei, das auf einer Etage oberhalb von `f` fallen gelassen wird, zerbricht, und jedes Ei, das auf oder unterhalb der Etage `f` fallen gelassen wird, nicht zerbricht.
Bei jedem Zug darfst du ein unzerbrochenes Ei nehmen und es von einer beliebigen Etage `x` (1 \le x \le n) fallen lassen.
Wenn das Ei zerbricht, kannst du es nicht mehr verwenden. Wenn das Ei jedoch nicht zerbricht, kannst du es in zukünftigen Zügen wiederverwenden.
Gib die **minimale Anzahl an Zügen** zurück, die du benötigst, um den Wert von `f` mit Sicherheit zu bestimmen.

**Eingabe:** Zwei ganze Zahlen `k` (Eier) und `n` (Stockwerke).
**Ausgabe:** Eine ganze Zahl, die die minimale Anzahl an Zügen im schlimmsten Fall angibt.

## Wann man es anwendet

- Das klassische „Minimax“-Problem der dynamischen Programmierung.
- Testet deine Fähigkeit, mit Worst-Case-Szenarien („mit Sicherheit“) umzugehen und gleichzeitig deine Strategie so zu optimieren, dass dieser Worst Case minimiert wird.

## Vorgehensweise

**1. Definiere den Zustand:**
Sei `dp[e][f]` die minimale Anzahl an Versuchen, die benötigt wird, um die kritische Etage zu finden, wobei genau `e` Eier und ein Gebäude mit genau `f` Etagen verwendet werden.

**2. Ermitteln der Basisfälle:**
- Wenn du 1 Ei (`e = 1`) hast, bleibt dir nichts anderes übrig, als im 1. Stock zu beginnen und Stockwerk für Stockwerk nach oben zu gehen. Im schlimmsten Fall sind `f` Versuche erforderlich. `dp[1][f] = f`.
- Wenn du 0 oder 1 Etage hast (`f = 0` bzw. `f = 1`), sind jeweils 0 oder 1 Fall erforderlich, unabhängig davon, wie viele Eier du hast. `dp[e][0] = 0` und `dp[e][1] = 1`.

**3. Finde den Übergang (die Rekursionsbeziehung):**
Wenn du `e` Eier und `f` Stockwerke hast, kannst du dein nächstes Ei von *jedem* beliebigen Stockwerk `x` (1 \le x \le f) fallen lassen.
Wenn du ein Ei von Etage `x` fallen lässt, gibt es genau zwei mögliche Ergebnisse:
- **Fall A (Das Ei zerbricht):** Die kritische Etage MUSS streng unterhalb von `x` liegen. Du hast nun `e - 1` Eier, und es sind noch `x - 1` Stockwerke zu überprüfen. Die Anzahl der erforderlichen Versuche beträgt `dp[e - 1][x - 1]`.
- **Fall B (Das Ei bleibt unversehrt):** Die kritische Etage MUSS auf `x` oder darüber liegen. Du hast noch `e` Eier, und es sind noch `f - x` Etagen zu überprüfen. Die benötigte Anzahl an Versuchen beträgt `dp[e][f - x]`.

Da wir die Antwort *mit Sicherheit* kennen müssen (Worst-Case-Szenario), zwingt uns die Natur immer zum schlechteren der beiden Ergebnisse!
Für eine bestimmte Etage `x` beträgt die Anzahl der Versuche im schlimmsten Fall also: `1 + max(dp[e - 1][x - 1], dp[e][f - x])`.
Aber DU darfst entscheiden, von welcher Etage `x` du dich fallen lässt! Du bist schlau, also wirst du die `x` wählen, die dieses Worst-Case-Szenario minimiert!
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

## Schritt-für-Schritt-Anleitung

`k = 2` Eier, `n = 4` Stockwerke.
Vorgegebene Basisfälle:
- `dp[1][1..4] = [1, 2, 3, 4]` (1 Ei benötigt bis zu f Stürze).
- `dp[2][0] = 0, dp[2][1] = 1`.

Berechne `e = 2`, `f = 2`:
- Fall bei x=1: `1 + max(dp[1][0], dp[2][1]) = 1 + max(0, 1) = 2`.
- Fall bei x=2: `1 + max(dp[1][1], dp[2][0]) = 1 + max(1, 0) = 2`.
- `dp[2][2] = min(2, 2) = 2`.

Berechne `e = 2`, `f = 3`:
- Fall bei x=1: `1 + max(dp[1][0], dp[2][2]) = 1 + max(0, 2) = 3`.
- Fall bei x=2: `1 + max(dp[1][1], dp[2][1]) = 1 + max(1, 1) = 2`. (Optimal!)
- Fall bei x=3: `1 + max(dp[1][2], dp[2][0]) = 1 + max(2, 0) = 3`.
- `dp[2][3] = min(3, 2, 3) = 2`.

Berechne `e = 2`, `f = 4`:
- x=1 verwerfen: `1 + max(dp[1][0], dp[2][3]) = 1 + max(0, 2) = 3`.
- x=2 verwerfen: `1 + max(dp[1][1], dp[2][2]) = 1 + max(1, 2) = 3`.
- x=3 weglassen: `1 + max(dp[1][2], dp[2][1]) = 1 + max(2, 1) = 3`.
- x=4 weglassen: `1 + max(dp[1][3], dp[2][0]) = 1 + max(3, 0) = 4`.
- `dp[2][4] = 3`.

Das Ergebnis ist 3. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(K * N^2)$ | $O(K * N)$ |
| **Durchschnittlicher Fall** | $O(K * N^2)$ | $O(K * N)$ |
| **Schlechtester Fall** | $O(K * N^2)$ | $O(K * N)$ |

Die Tabelle ist K x N groß. Für jede Zelle läuft die x-Schleife bis zu N-mal. Die Laufzeit beträgt $O(K x N^2)$.
Der Speicherbedarf beträgt genau $O(K x N)$ für die DP-Matrix.

## Varianten & Optimierungen

- **Optimierung durch binäre Suche ($O(K x N log N)$):** Beachte, dass innerhalb der `x`-Schleife `dp[e - 1][x - 1]` streng *monoton steigend* ist, wenn `x` wächst, und `dp[e][f - x]` streng *monoton fallend* ist, wenn `x` wächst. Der optimale Wert für x liegt genau am Schnittpunkt dieser beiden Funktionen! Du kannst anstelle eines linearen Durchlaufs die binäre Suche verwenden, um x zu finden, wodurch sich die Zeitkomplexität drastisch verringert.
- **DP mit invertiertem Zustand ($O(K x log N)$):** Die ultimative mathematische Optimierung. Anstelle von `dp[eggs][floors] = moves` kehrst du die Definition um! Sei `dp[moves][eggs] = max_floors`. Man kann bis zu `dp[m][e] = 1 + dp[m-1][e-1] + dp[m-1][e]` Etagen überprüfen. Man erhöht einfach `m` bis `dp[m][K] >= N`. Dies benötigt nur $O(K)$ Speicherplatz und läuft praktisch sofort!

## Anwendungen in der Praxis

- **Stresstests / Qualitätssicherung:** Ermittlung der maximalen sicheren Belastungsgrenze (Temperatur, Spannung, Druck) für eine physikalische Komponente, bei der eine Zerstörung der Komponente während des Tests mit hohen Kosten verbunden ist (begrenzte „Eier“).

## Verwandte Algorithmen in cOde(n)

- **[dp_13 – Matrixkettenmultiplikation](dp_13_matrix-chain-multiplication.md)** — Ein weiteres Problem, bei dem man eine dritte Variable `k` (oder `x`) innerhalb des DP-Zustands iterieren muss, um einen optimalen Teilungspunkt zu finden.
- **[searching_01 – Binäre Suche](../searching/search_01_binary-search.md)** — Das $O(\log N)$ Kernkonzept, die Hälfte des Suchraums sicher auszuschließen, das „Egg Dropping“ unter begrenzten Ressourcen nachzuahmen versucht.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
nach dem Vorbild der kanonischen Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
