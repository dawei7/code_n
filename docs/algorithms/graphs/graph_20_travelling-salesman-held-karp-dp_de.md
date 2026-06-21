# Travelling Salesperson (Held-Karp DP)

| | |
|---|---|
| **ID** | `graph_20` |
| **Kategorie** | graphs |
| **Komplexität (erforderlich)** | $O(V^2 * 2^V)$ Zeit, $O(V * 2^V)$ Platz |
| **Schwierigkeit** | 10/10 |
| **Relevanz für Vorstellungsgespräche** | 2/10 |
| **Wikipedia** | [Held-Karp-Algorithmus](https://en.wikipedia.org/wiki/Held%E2%80%93Karp_algorithm) |

## Problemstellung

Gegeben ist ein vollständiger gewichteter Graph (in dem jeder Knoten mit jedem anderen Knoten verbunden ist). Finde die absolut kürzestmögliche Route, die jeden Knoten genau einmal besucht und zum Startknoten zurückkehrt.
Dies ist das legendäre Travelling Salesperson Problem (TSP).

**Eingabe:** Anzahl der Knoten `V` und eine 2D-Adjazenzmatrix `matrix`.
**Ausgabe:** Eine Ganzzahl, die die minimalen Kosten der Tour repräsentiert.

## Wann man es verwendet

- Um TSP exakt für kleine Graphen zu lösen (V \le 20).
- *Hinweis:* Ein reiner Brute-Force-Ansatz über Permutationen prüft $O(V!)$ Pfade. 20! entspricht 2.4 x 10^{18} (unmöglich). Der Held-Karp-Algorithmus reduziert dies mit $O(V^2 2^V)$ auf 20^2 x 2^{20} ~= 4 x 10^8 Operationen, was weniger als eine Sekunde dauert!

## Ansatz

**1. Überlappende Teilprobleme (Warum DP funktioniert):**
Stellen wir uns V=5 vor. Wir starten bei Knoten 0.
Pfad A: 0 \rightarrow 1 \rightarrow 2 \rightarrow 3.
Pfad B: 0 \rightarrow 2 \rightarrow 1 \rightarrow 3.
Beachte, dass beide Pfade aktuell bei Knoten `3` stehen und beide Pfade exakt dieselbe Menge an Städten `{0, 1, 2, 3}` besucht haben!
Um die Tour zu beenden, müssen beide Pfade Knoten `4` besuchen und zu `0` zurückkehren. Die *zukünftigen optimalen Entscheidungen* von Knoten `3` aus sind vollkommen identisch! Wir sollten den optimalen Vervollständigungspfad von (Knoten `3`, Menge `{0,1,2,3}`) nur EINMAL berechnen und das Ergebnis zwischenspeichern (cachen)!

**2. Bitmasking der Menge:**
Wir repräsentieren die "Menge der besuchten Städte" als eine Ganzzahl-Bitmaske.
Wenn wir die Städte 0, 1 und 3 besucht haben, ist die Bitmaske `1011` (binär für 11).
Unser DP-Zustand ist `dp(mask, curr_node)`.
Dies repräsentiert: "Was sind die minimalen Kosten, um alle VERBLEIBENDEN unbesuchten Knoten im Graphen zu besuchen, ausgehend von `curr_node`, unter der Voraussetzung, dass wir bereits die Knoten in `mask` besucht haben?"

**3. Die Rekursionsgleichung:**
Von `curr_node` aus können wir versuchen, zu jedem `next_node` zu springen, der aktuell NICHT in der `mask` aktiviert ist.
Die Kosten dieser Wahl sind:
`weight(curr_node, next_node) + dp( mask | (1 << next_node), next_node )`
Wir wählen das absolute Minimum über alle gültigen Möglichkeiten für `next_node`.

**4. Der Induktionsanfang (Basis):**
Wenn alle Bits in `mask` auf 1 stehen (`mask == (1 << V) - 1`), bedeutet dies, dass wir jede Stadt genau einmal besucht haben.
Das Einzige, was noch zu tun ist, ist die Rückkehr zum Startknoten (Knoten 0).
Gib `matrix[curr_node][0]` zurück.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for graph_20: Travelling Salesman (Held-Karp DP).

dp[mask][i] = min cost to start at 0, visit exactly the
cities in ``mask``, and end at city i. Recurrence:
dp[mask][i] = min over j in mask of dp[mask ^ (1<<i)][j] + dist[j][i].
Final answer: min over i of dp[all][i] + dist[i][0].
"""


def solve(dist, n):
    if n <= 1:
        return 0
    INF = float("inf")
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0
    for mask in range(1, 1 << n):
        if not (mask & 1):
            continue
        for i in range(n):
            if not (mask & (1 << i)) or dp[mask][i] == INF:
                continue
            for j in range(n):
                if mask & (1 << j):
                    continue
                new_mask = mask | (1 << j)
                new_cost = dp[mask][i] + dist[i][j]
                if new_cost < dp[new_mask][j]:
                    dp[new_mask][j] = new_cost
    full = (1 << n) - 1
    best = INF
    for i in range(n):
        if dp[full][i] < INF:
            cycle = dp[full][i] + dist[i][0]
            if cycle < best:
                best = cycle
    return best
```

</details>

## Durchlauf

`V = 3`. Start bei Knoten 0. `VISITED_ALL = 7` (binär `111`).
`dp(1, 0)`: (Maske `001`, Aktuell `0`)
  - Versuche nächstes `1`. Kosten = `matrix[0][1] + dp(3, 1)`. (Maske `011`)
  - Versuche nächstes `2`. Kosten = `matrix[0][2] + dp(5, 2)`. (Maske `101`)

Evaluiere `dp(3, 1)`: (Maske `011`, Aktuell `1`)
  - Versuche nächstes `2`. Kosten = `matrix[1][2] + dp(7, 2)`. (Maske `111`)

Evaluiere `dp(7, 2)`: (Maske `111` == VISITED_ALL)
  - Induktionsanfang! Gib `matrix[2][0]` zurück.

Pfad `0 -> 1 -> 2 -> 0` Kosten werden aufgelöst.
Der Baum evaluiert alle Pfade und memoisiert identische Teilpfade (obwohl bei V=3 noch keine Überlappung auftritt; Überlappungen treten erst ab V \ge 4 auf).
Gib das Minimum zurück. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(V^2 * 2^V)$ | $O(V * 2^V)$ |
| **Durchschnittlicher Fall** | $O(V^2 * 2^V)$ | $O(V * 2^V)$ |
| **Schlechtester Fall** | $O(V^2 * 2^V)$ | $O(V * 2^V)$ |

Wie viele eindeutige Zustände befinden sich in der Memoization-Tabelle? Die `mask` kann jeden Wert von 0 bis 2^V - 1 annehmen, und `curr` kann jeder Knoten von 0 bis V - 1 sein. Gesamtzustände = V \cdot 2^V.
Innerhalb der `dp()`-Funktion benötigt die Berechnung eines Zustands $O(V)$ Zeit aufgrund der `for nxt in range(V)`-Schleife.
Daher ist die Gesamtzeit (V \cdot 2^V) \cdot V = $O(V^2 2^V)$.
Die Platzkomplexität beträgt $O(V \cdot 2^V)$, um die `memo`-Tabelle zu speichern.
Obwohl exponentiell, ist dies eine gewaltige Verbesserung gegenüber der $O(V!)$ Brute-Force-Logik.

## Varianten & Optimierungen

- **Christofides-Algorithmus (Approximation):** Für metrische Graphen (bei denen die Dreiecksungleichung gilt), garantiert der Christofides-Algorithmus mathematisch das Finden einer Route, die HÖCHSTENS 1.5x länger als die wahre optimale Route ist, und das in $O(V^3)$ polynomieller Zeit! (Er basiert auf der Suche nach einem MST und anschließendem Finden eines gewichtsminimalen perfekten Matchings auf den Knoten mit ungeradem Grad).
- **Genetische Algorithmen / Simulated Annealing:** Für massive Instanzen (V = 100.000) werden KI-Metaheuristiken verwendet, um schnell "gut genug" Routen zu finden, da sowohl V! als auch 2^V physikalisch unmöglich zu berechnen sind.

## Anwendungen in der Praxis

- **Logistik & Zustellung (FedEx/UPS):** Tägliche Routenplanung für Lieferwagen, die 15-20 Pakete ausliefern.
- **Leiterplattenfertigung (PCB):** Optimierung des Pfades des robotergesteuerten Laserbohrers, der hunderte Löcher in ein Motherboard bohren muss.

## Verwandte Algorithmen in cOde(n)

- **[dp_03 - Top-Down Memoization](../dynamic/dp_03_top-down-memoization.md)** — Die Grundlage der hier verwendeten exakten Technik.
- **[bit_01 - Check if i-th bit is set](../bit_manipulation/bit_01_check-if-i-th-bit-is-set.md)** — Die bitweise Arithmetik, die verwendet wird, um Bits in der `mask` zu flippen.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*