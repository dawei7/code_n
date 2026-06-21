# Ford-Fulkerson (Max Flow)

| | |
|---|---|
| **ID** | `flow_01` |
| **Kategorie** | flow |
| **Komplexität (erforderlich)** | $O(E * f)$ |
| **Schwierigkeit** | 6/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **Wikipedia** | [Ford–Fulkerson algorithm](https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm) |

## Problemstellung

Gegeben ist ein gerichteter Graph, der ein Leitungsnetzwerk repräsentiert, wobei jede Kante eine `capacity` besitzt. Finde den **maximal möglichen Fluss** von einem `source`-Knoten (S) zu einem `sink`-Knoten (T).
Du musst die **Ford-Fulkerson**-Methode unter Verwendung einer Tiefensuche (DFS) implementieren, um augmentierende Pfade zu finden.

**Eingabe:** Ein gerichteter Graph mit Kapazitäten, ein `source`-Knoten `s` und ein `sink`-Knoten `t`.
**Ausgabe:** Eine Ganzzahl, die den maximalen Gesamtfluss darstellt.

## Wann man es verwendet

- Die Grundlage aller Netzwerkflussprobleme. Verwende es, um das Konzept des Residualgraphen zu verstehen.
- Verwende es NICHT in der Produktion, wenn die Kantenkapazitäten massiv sind (z. B. 10^9) oder wenn die Kapazitäten Fließkommazahlen sind, da Ford-Fulkerson auf Basis von DFS extrem lange dauern oder bei irrationalen Kapazitäten sogar in eine Endlosschleife geraten kann! Verwende stattdessen Edmonds-Karp oder Dinic.

## Ansatz

Stell dir vor, du gießt Wasser in ein Leitungsnetz. Wir wollen so viel Wasser wie möglich hindurchleiten.
Ein naiver gieriger Ansatz wäre: Finde einen Pfad von S nach T. Finde die kleinste Leitung auf diesem Pfad. Leite genau diese Menge an Wasser durch den gesamten Pfad. Wiederhole dies, bis keine Pfade mehr existieren.
**Der Fehler des gierigen Ansatzes:** Wenn du gierig Wasser durch eine Leitung schickst, könntest du einen späteren Pfad blockieren, der diese Leitung eigentlich benötigt hätte, um einen höheren *Gesamtfluss* zu erreichen!

**Die Erkenntnis von Ford-Fulkerson (Der Residualgraph):**
Jedes Mal, wenn wir X Einheiten Wasser entlang einer Kante `u -> v` vorwärts schicken, müssen wir künstlich eine Kante *rückwärts* `v -> u` mit der Kapazität X hinzufügen.
Diese Rückwärtskante fungiert als "Rückgängig"-Button! Wenn ein zukünftiger Pfad entdeckt, dass er einen besseren Gesamtfluss erzielen kann, indem er Wasser *rückwärts* entlang dieser Leitung leitet (was effektiv unseren vorherigen gierigen Fehler aufhebt und das Wasser anderswohin umleitet), erlaubt der Algorithmus dies!

1. **Residualgraph:** Erstelle einen Graphen, der `capacity` speichert. Initialisiere `flow = 0`.
2. **Pfad finden:** Verwende eine einfache DFS, um *irgendeinen* Pfad von S nach T zu finden, bei dem jede Kante auf dem Pfad eine `capacity > 0` hat.
3. **Flaschenhals:** Finde die minimale Kapazität entlang dieses Pfades. Nennen wir sie `bottleneck`.
4. **Fluss augmentieren:** 
   - Addiere `bottleneck` zum gesamten `flow`.
   - Für jede Kante `u -> v` auf dem Pfad:
     - Subtrahiere `bottleneck` von `capacity[u][v]`.
     - **Entscheidend:** Addiere `bottleneck` zur Rückwärtskante `capacity[v][u]`!
5. Wiederhole die Schritte 2-4, bis die DFS keinen Pfad mehr von S nach T finden kann.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for flow_01: Ford-Fulkerson Max Flow.

DFS-based augmenting path. Find path, push bottleneck,
update residual. Repeat.
"""


def solve(n, edges):
    INF = float("inf")
    cap = [[0] * n for _ in range(n)]
    for u, v, c in edges:
        cap[u][v] += c
    max_flow = 0
    while True:
        parent = [-1] * n
        parent[0] = 0
        stack = [0]
        visited = [False] * n
        visited[0] = True
        found = -1
        while stack and found == -1:
            u = stack.pop()
            for v in range(n):
                if not visited[v] and cap[u][v] > 0:
                    visited[v] = True
                    parent[v] = u
                    if v == n - 1:
                        found = v
                        break
                    stack.append(v)
        if found == -1:
            break
        path_flow = float("inf")
        v = found
        while v != 0:
            u = parent[v]
            if cap[u][v] < path_flow:
                path_flow = cap[u][v]
            v = u
        v = found
        while v != 0:
            u = parent[v]
            cap[u][v] -= path_flow
            cap[v][u] += path_flow
            v = u
        max_flow += path_flow
    return max_flow
```

</details>

## Durchlauf

Graph:
`S(0) -> A(1)`: cap 10
`S(0) -> B(2)`: cap 10
`A(1) -> B(2)`: cap 1
`A(1) -> T(3)`: cap 10
`B(2) -> T(3)`: cap 10

**Iteration 1:**
- DFS findet Pfad `0 -> 1 -> 2 -> 3` (S -> A -> B -> T).
- Kapazitäten: 10, 1, 10. Flaschenhals = 1.
- Schiebe 1 Einheit.
- Vorwärtskanten `(0,1), (1,2), (2,3)` verlieren 1 Kapazität.
- Rückwärtskanten `(1,0), (2,1), (3,2)` gewinnen 1 Kapazität.
- Gesamtfluss = 1.

**Iteration 2:**
- DFS findet Pfad `0 -> 1 -> 3` (S -> A -> T).
- Kapazitäten: 9, 10. Flaschenhals = 9.
- Schiebe 9 Einheiten.
- Gesamtfluss = 1 + 9 = 10.

**Iteration 3:**
- DFS findet Pfad `0 -> 2 -> 3` (S -> B -> T).
- Kapazitäten: 10, 9. Flaschenhals = 9.
- Schiebe 9 Einheiten.
- Gesamtfluss = 10 + 9 = 19.

Es existieren keine weiteren Pfade mehr. Maximaler Fluss = 19. ✓ (Beachte, wie die DFS in Iteration 1 einen "Fehler" machte, indem sie die mittlere Leitung benutzte, aber später problemlos darum herumleitete).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(E)$ | $O(V^2)$ |
| **Durchschnittlicher Fall** | Abhängig | $O(V^2)$ |
| **Schlechtester Fall** | $O(E * f)$ | $O(V^2)$ |

*Wobei E die Anzahl der Kanten und f der maximale Fluss ist.*
Warum $O(E x f)$? Stell dir den obigen Graphen vor, aber die mittlere Leitung `A -> B` hat die Kapazität 1 und die anderen Leitungen haben die Kapazität 1.000.000.
Wenn die DFS unglücklicherweise zwischen dem Pfad `S->A->B->T` (schiebe 1) und `S->B->A->T` unter Verwendung der Rückwärtskante (schiebe 1) alterniert, wird sie pro Iteration genau 1 Einheit Fluss schieben! Es wären 2.000.000 DFS-Aufrufe erforderlich, um fertig zu werden!
Die Platzkomplexität beträgt $O(V^2)$, um die dichte Kapazitätsmatrix zu speichern (oder $O(V + E)$, wenn sie mit einer Adjazenzliste von Kantenobjekten implementiert wird).

## Varianten & Optimierungen

- **Edmonds-Karp ($O(V E^2)$):** Exakt derselbe Algorithmus, verwendet jedoch BFS anstelle von DFS. Dies verhindert mathematisch den pathologischen Fall $O(E x f)$ und stellt eine strikt polynomielle Laufzeit unabhängig von den Kantenkapazitäten sicher!
- **Capacity Scaling:** Berücksichtige nur Kanten mit einer Kapazität \ge \Delta. Starte mit \Delta als einer großen Zweierpotenz und halbiere diese jedes Mal. Dies reduziert die Zeit auf $O(E^2 log U)$.

## Anwendungen in der Praxis

- **Verkehrsleitung:** Berechnung der maximalen Anzahl von Autos, die während eines Hurrikans durch ein Autobahnnetz aus einer Stadt evakuiert werden können.

## Verwandte Algorithmen in cOde(n)

- **[flow_02 - Edmonds-Karp](flow_02_edmonds-karp.md)** — Das BFS-Upgrade für diesen Algorithmus.
- **[flow_03 - Bipartite Matching](flow_03_bipartite-matching.md)** — Ein Spezialfall des maximalen Flusses, bei dem jede Kantenkapazität genau 1 beträgt.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*