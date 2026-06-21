# Min Cost Climbing Stairs

| | |
|---|---|
| **ID** | `dp_23` |
| **Kategorie** | dynamic |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 2/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) |

## Problemstellung

Gegeben ist ein Integer-Array `cost`, wobei `cost[i]` die Kosten für den `i`-ten Schritt auf einer Treppe darstellt. Sobald man die Kosten bezahlt hat, kann man entweder einen oder zwei Schritte nach oben steigen.
Man kann entweder bei dem Schritt mit dem Index 0 oder bei dem Schritt mit dem Index 1 beginnen.
Geben Sie die minimalen Kosten zurück, um das Ende der Treppe zu erreichen (dies entspricht dem Index `N`, der strikt außerhalb des Arrays liegt).

**Eingabe:** Ein Integer-Array `cost`.
**Ausgabe:** Ein Integer, der die minimalen Kosten repräsentiert.

## Wann man es verwendet

- Die gewichtete bzw. kostenbasierte Variante von `dp_02 - Climbing Stairs`.
- Ein absolut perfektes Einstiegsproblem, um Minimierungsübergänge in 1D-Arrays zu lehren.

## Ansatz

**1. Den Zustand definieren:**
Sei `dp[i]` die minimalen Gesamtkosten, um den Schritt `i` zu *erreichen*.
*(Hinweis: Um "das Ende der Treppe zu erreichen", müssen wir den Schritt `N` erreichen, welcher einen Index hinter dem Ende des `cost`-Arrays liegt).*

**2. Die Basisfälle finden:**
Das Problem besagt, dass wir bei Schritt 0 oder Schritt 1 kostenlos starten können. Wir zahlen die Kosten nur, wenn wir den Schritt *verlassen*.
Daher sind die Kosten, um Schritt 0 zu *erreichen*, 0. Die Kosten, um Schritt 1 zu *erreichen*, sind 0.
`dp[0] = 0`, `dp[1] = 0`.

**3. Den Übergang finden (Die Rekurrenz):**
Wie könnten wir möglicherweise bei Schritt `i` ankommen?
- Wir könnten von Schritt `i-1` gekommen sein. Um das zu tun, mussten wir Schritt `i-1` erreichen (was `dp[i-1]` kostete) und dann die Gebühr bezahlen, um Schritt `i-1` zu verlassen (was `cost[i-1]` entspricht).
- Wir könnten von Schritt `i-2` gekommen sein. Um das zu tun, mussten wir Schritt `i-2` erreichen (was `dp[i-2]` kostete) und dann die Gebühr `cost[i-2]` bezahlen.

Wir wollen das absolute Minimum!
`dp[i] = min( dp[i-1] + cost[i-1], dp[i-2] + cost[i-2] )`

**4. Platzkomplexität optimieren:**
Beachten Sie, dass `dp[i]` nur von den vorherigen zwei Schritten (`dp[i-1]` und `dp[i-2]`) abhängt. Genau wie bei Fibonacci können wir das $O(N)$-Array verwerfen und einfach zwei gleitende Variablen verwenden!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dp_23: Min Cost Climbing Stairs.

Minimum cost to reach the top of a staircase where you
may climb 1 or 2 steps at a time. cost[i] is the cost of
step i. dp[i] = cost[i] + min(dp[i-1], dp[i-2]). The
answer is min(dp[n-1], dp[n-2]).
"""


def solve(cost, n):
    if n == 0:
        return 0
    if n == 1:
        return cost[0]
    prev2 = cost[0]
    prev1 = cost[1]
    for i in range(2, n):
        cur = cost[i] + min(prev1, prev2)
        prev2, prev1 = prev1, cur
    return min(prev1, prev2)
```

</details>

## Durchlauf

`cost = [10, 15, 20]`. N = 3.
Initialisiere `prev2 = 0`, `prev1 = 0`.

1. **i = 2 (Schritt 2 erreichen):**
   - Von Schritt 1: `prev1 + cost[1]` = 0 + 15 = 15.
   - Von Schritt 0: `prev2 + cost[0]` = 0 + 10 = 10.
   - `current_cost = min(15, 10) = 10`.
   - Verschiebung: `prev2 = 0`, `prev1 = 10`.
2. **i = 3 (das Ende erreichen, N):**
   - Von Schritt 2: `prev1 + cost[2]` = 10 + 20 = 30.
   - Von Schritt 1: `prev2 + cost[1]` = 0 + 15 = 15.
   - `current_cost = min(30, 15) = 15`.
   - Verschiebung: `prev2 = 10`, `prev1 = 15`.

Das Ergebnis `prev1` ist 15. ✓ (Der Pfad ist: Starte bei Index 1, zahle 15, springe 2 Schritte zum Ende).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N)$ | $O(1)$ |

Die Schleife iteriert exakt N-1 Mal. Die mathematische Berechnung innerhalb der Schleife ist $O(1)$. Die gesamte Zeitkomplexität ist $O(N)$.
Die Platzkomplexität ist strikt $O(1)$, da wir nur zwei Integer-Variablen anstelle eines Arrays verwenden.

## Varianten & Optimierungen

- **Mutation des Eingabe-Arrays:** Man kann dies tatsächlich lösen, indem man das `cost`-Array in-place mutiert! Schleife von `i=2` bis `N-1`: `cost[i] += min(cost[i-1], cost[i-2])`. Geben Sie dann `min(cost[N-1], cost[N-2])` zurück. Dies ist ebenfalls $O(1)$ Platz, vermeidet aber zusätzliche Variablen. Allerdings gilt die Mutation von Eingabeparametern in der Softwareentwicklung im Allgemeinen als schlechte Praxis.

## Anwendungen in der Praxis

- **Netzwerk-Routing-Protokolle:** Eine stark vereinfachte 1D-Version zur Berechnung des Pfades mit dem geringsten Widerstand bzw. der geringsten Latenz für ein Paket, das eine lineare Sequenz von Routern durchläuft, wobei Sprünge einen Knoten überspringen können.

## Verwandte Algorithmen in cOde(n)

- **[dp_02 - Climbing Stairs](dp_02_climbing-stairs.md)** — Die ungewichtete, kombinatorische Variante.
- **[dp_11 - House Robber](dp_11_house-robber.md)** — Ein weiteres 1D-DP-Problem, das die identische `prev1`/`prev2`-Platzoptimierung verwendet.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*