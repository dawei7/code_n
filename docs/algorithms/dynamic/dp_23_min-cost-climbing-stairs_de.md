# Minimale Kosten beim Treppensteigen

| | |
|---|---|
| **ID** | `dp_23` |
| **Kategorie** | dynamisch |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(1)$ Speicherplatz |
| **Schwierigkeitsgrad** | 2/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) |

## Aufgabenstellung

Gegeben ist ein Array aus ganzen Zahlen `cost`, wobei `cost[i]` die Kosten für die `i`-te Stufe einer Treppe angibt. Sobald du die Kosten bezahlt hast, kannst du entweder eine oder zwei Stufen hinaufsteigen.
Du kannst entweder von der Stufe mit dem Index 0 oder von der Stufe mit dem Index 1 aus starten.
Gib die minimalen Kosten zurück, um die oberste Stufe zu erreichen (die den Index `N` hat und streng außerhalb des Arrays liegt).

**Eingabe:** Ein Ganzzahl-Array `cost`.
**Ausgabe:** Eine Ganzzahl, die die minimalen Kosten angibt.

## Wann man es verwendet

- Die gewichtete/kostenbasierte Variante von `dp_02 - Climbing Stairs`.
- Ein absolut perfektes Einführungsproblem, um Minimierungsübergänge in 1D-Arrays zu vermitteln.

## Vorgehensweise

**1. Definieren Sie den Zustand:**
Sei `dp[i]` die minimalen Gesamtkosten, um Schritt `i` zu *erreichen*.
*(Hinweis: Um „die oberste Etage zu erreichen“, müssen wir Schritt `N` erreichen, der einen Index hinter dem Ende des Arrays `cost` liegt).*

**2. Die Basisfälle ermitteln:**
Die Aufgabenstellung besagt, dass wir kostenlos bei Schritt 0 oder Schritt 1 beginnen können. Wir zahlen die Kosten erst, wenn wir den Schritt *verlassen*.
Daher betragen die Kosten für das *Erreichen* von Schritt 0 0. Die Kosten für das *Erreichen* von Schritt 1 betragen 0.
`dp[0] = 0`, `dp[1] = 0`.

**3. Den Übergang (die Rekursionsbeziehung) ermitteln:**
Wie könnten wir überhaupt zu Schritt `i` gelangen?
- Wir könnten von Schritt `i-1` gekommen sein. Dazu mussten wir Schritt `i-1` erreichen (was `dp[i-1]` gekostet hat) und anschließend die Maut bezahlen, um Schritt `i-1` zu verlassen (was `cost[i-1]` beträgt).
- Wir könnten von Schritt `i-2` gekommen sein. Dazu mussten wir Schritt `i-2` erreichen (was `dp[i-2]` gekostet hat) und anschließend die Maut `cost[i-2]` bezahlen.

Wir wollen das absolute Minimum!
`dp[i] = min( dp[i-1] + cost[i-1], dp[i-2] + cost[i-2] )`

**4. Speicherplatz optimieren:**
Beachte, dass `dp[i]` sich nur auf die beiden vorherigen Schritte (`dp[i-1]` und `dp[i-2]`) stützt. Genau wie bei Fibonacci können wir das Array $O(N)$ verwerfen und einfach zwei gleitende Variablen verwenden!

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

## Schritt-für-Schritt-Anleitung

`cost = [10, 15, 20]`. N = 3.
Initialisiere `prev2 = 0`, `prev1 = 0`.

1. **i = 2 (Erreichen von Schritt 2):**
   - Aus Schritt 1: `prev1 + cost[1]` = 0 + 15 = 15.
   - Aus Schritt 0: `prev2 + cost[0]` = 0 + 10 = 10.
   - `current_cost = min(15, 10) = 10`.
   - Verschiebung: `prev2 = 0`, `prev1 = 10`.
2. **i = 3 (Erreichen des Endes, N):**
   - Aus Schritt 2: `prev1 + cost[2]` = 10 + 20 = 30.
   - Aus Schritt 1: `prev2 + cost[1]` = 0 + 15 = 15.
   - `current_cost = min(30, 15) = 15`.
   - Verschiebung: `prev2 = 10`, `prev1 = 15`.

Das Ergebnis `prev1` ist 15. ✓ (Der Pfad lautet: Start bei Index 1, 15 zahlen, 2 Schritte nach oben springen).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(1)$ |
| **Schlimmster Fall** | $O(N)$ | $O(1)$ |

Die Schleife wird genau N-1 Mal durchlaufen. Die Berechnung innerhalb der Schleife lautet $O(1)$. Die Gesamtzeit beträgt $O(N)$.
Die Platzkomplexität beträgt genau $O(1)$, da wir anstelle eines Arrays nur zwei ganzzahlige Variablen verwenden.

## Varianten & Optimierungen

- **Änderung des Eingabe-Arrays:** Man kann diese Aufgabe tatsächlich lösen, indem man das `cost`-Array direkt vor Ort ändert! Schleife von `i=2` bis `N-1`: `cost[i] += min(cost[i-1], cost[i-2])`. Anschließend `min(cost[N-1], cost[N-2])` zurückgeben. Dies hat ebenfalls eine Speicherplatzkomplexität von $O(1)$, vermeidet jedoch zusätzliche Variablen. Allerdings gilt das Ändern von Eingabeparametern in der Produktionsentwicklung allgemein als schlechte Praxis.

## Anwendungen in der Praxis

- **Netzwerk-Routing-Protokolle:** Eine stark vereinfachte 1D-Version zur Berechnung des Weges mit dem geringsten Widerstand/der geringsten Latenz für ein Paket, das eine lineare Folge von Routern durchläuft, wobei beim Hopping ein Knoten übersprungen wird.

## Verwandte Algorithmen in cOde(n)

- **[dp_02 – Treppensteigen](dp_02_climbing-stairs.md)** — Die ungewichtete, kombinatorische Variante.
- **[dp_11 – House Robber](dp_11_house-robber.md)** – Ein weiteres eindimensionales DP, das dieselbe Raumoptimierung wie `prev1`/`prev2` verwendet.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
in Anlehnung an die kanonische Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
