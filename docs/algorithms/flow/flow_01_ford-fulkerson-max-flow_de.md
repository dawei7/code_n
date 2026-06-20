# Ford-Fulkerson (Max Flow)

| | |
|---|---|
| **ID** | `flow_01` |
| **Kategorie** | Durchfluss |
| **Komplexität (erforderlich)** | $O(E * f)$ |
| **Schwierigkeitsgrad** | 6/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **Wikipedia** | [Ford–Fulkerson-Algorithmus](https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm) |

## Aufgabenstellung

Gegeben sei ein gerichteter Graph, der ein Rohrleitungsnetz darstellt, wobei jede Kante eine `capacity` aufweist. Bestimmen Sie den **maximal möglichen Fluss** von einem `source`-Knoten (S) zu einem `sink`-Knoten (T).
Sie müssen die **Ford-Fulkerson**-Methode unter Verwendung der Tiefensuche (DFS) implementieren, um augmentierende Pfade zu finden.

**Eingabe:** Ein gerichteter Graph mit Kapazitäten, einem Quellknoten `s` und einem Senkenknoten `t`.
**Ausgabe:** Eine ganze Zahl, die den maximalen Gesamtfluss angibt.

## Wann sollte man diese Methode anwenden?

- Die Grundlage aller Netzwerkflussprobleme. Verwenden Sie sie, um das Konzept des Restgraphen zu verstehen.
- Verwenden Sie sie NICHT in der Produktion, wenn die Kantenkapazitäten sehr groß sind (z. B. 10^9) oder wenn es sich bei den Kapazitäten um Gleitkommazahlen handelt, da die DFS-basierte Ford-Fulkerson-Methode extrem lange dauern oder bei irrationalen Kapazitäten sogar in eine Endlosschleife geraten kann! Verwenden Sie stattdessen Edmonds-Karp oder Dinic.

## Vorgehensweise

Stellen Sie sich vor, Sie gießen Wasser in ein Rohrnetz. Wir wollen so viel Wasser wie möglich durchleiten.
Ein naiver, gieriger Ansatz wäre: Finden Sie einen Pfad von S nach T. Finden Sie das kleinste Rohr auf diesem Pfad. Leiten Sie genau diese Wassermenge durch den gesamten Pfad. Wiederholen Sie dies, bis keine Pfade mehr existieren.
**Der Fehler des gierigen Ansatzes:** Wenn man Wasser gierig durch ein Rohr dusht, blockiert man möglicherweise einen späteren Pfad, der dieses Rohr eigentlich benötigt hätte, um einen höheren *Gesamt*durchfluss zu erreichen!

**Die Erkenntnis von Ford und Fulkerson (der Restgraph):**
Jedes Mal, wenn wir X Einheiten Wasser entlang einer Kante `u -> v` vorwärts leiten, müssen wir künstlich eine *rückwärts* verlaufende Kante `v -> u` mit der Kapazität X hinzufügen.
Diese rückwärts gerichtete Kante fungiert als „Rückgängig“-Schaltfläche! Wenn ein zukünftiger Pfad feststellt, dass er einen besseren Gesamtdurchfluss erzielen kann, indem er Wasser *rückwärts* entlang dieser Leitung leitet (wodurch unser vorheriger gieriger Fehler effektiv rückgängig gemacht und das Wasser anderweitig umgeleitet wird), lässt der Algorithmus dies zu!

1. **Restgraph:** Erstelle einen Graphen, der `capacity` speichert. Initialisiere `flow = 0`.
2. **Pfad finden:** Verwende eine einfache DFS, um *beliebige* Pfade von S nach T zu finden, bei denen jede Kante auf dem Pfad `capacity > 0` aufweist.
3. **Engpass:** Finde die minimale Kapazität entlang dieses Pfades. Nennen wir sie `bottleneck`.
4. **Fluss erhöhen:** 
   - Füge `bottleneck` zum Gesamtwert `flow` hinzu.
   - Für jede Kante `u -> v` auf dem Pfad:
     - Ziehe `bottleneck` von `capacity[u][v]` ab.
 - **Wichtig:** Addiere `bottleneck` zur rückwärtsgerichteten Kante `capacity[v][u]`!
5. Wiederhole die Schritte 2–4, bis DFS keinen Pfad mehr von S nach T finden kann.

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

## Schritt-für-Schritt-Anleitung

Graph:
`S(0) -> A(1)`: Kapazität 10
`S(0) -> B(2)`: Kapazität 10
`A(1) -> B(2)`: Kapazität 1
`A(1) -> T(3)`: Kapazität 10
`B(2) -> T(3)`: Kapazität 10

**Iteration 1:**
- DFS findet den Pfad `0 -> 1 -> 2 -> 3` (S -> A -> B -> T).
- Kapazitäten: 10, 1, 10. Engpass = 1.
- 1 Einheit verschieben.
- Vorwärtskanten `(0,1), (1,2), (2,3)` verlieren 1 Kapazität.
- Rückwärtskanten `(1,0), (2,1), (3,2)` gewinnen 1 Kapazität.
- Gesamtfluss = 1.

**Iteration 2:**
- DFS findet den Pfad `0 -> 1 -> 3` (S -> A -> T).
- Kapazitäten: 9, 10. Engpass = 9.
- 9 Einheiten einfügen.
- Gesamtdurchfluss = 1 + 9 = 10.

**Iteration 3:**
- DFS findet den Pfad `0 -> 2 -> 3` (S -> B -> T).
- Kapazitäten: 10, 9. Engpass = 9.
- 9 Einheiten weiterleiten.
- Gesamtfluss = 10 + 9 = 19.

Es gibt keine weiteren Pfade mehr. Maximum Flow = 19. ✓ (Beachten Sie, wie DFS in Iteration 1 einen „Fehler“ gemacht hat, indem es die mittlere Leitung verwendet hat, diesen aber später problemlos umgangen hat).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(E)$ | $O(V^2)$ |
| **Durchschnittlicher Fall** | Hängt ab | $O(V^2)$ |
| **Schlechtester Fall** | $O(E * f)$ | $O(V^2)$ |

*Dabei ist E die Anzahl der Kanten und f der maximale Fluss.*
Warum $O(E x f)$? Stellen Sie sich den obigen Graphen vor, bei dem jedoch die mittlere Leitung `A -> B` eine Kapazität von 1 und die anderen Leitungen eine Kapazität von 1.000.000 haben.
Wenn DFS unglücklicherweise zwischen dem Pfad `S->A->B->T` (Push 1) und `S->B->A->T` unter Verwendung der Rückwärtskante (Push 1) wechselt, wird pro Iteration genau 1 Einheit Fluss gepusht! Es sind 2.000.000 DFS-Aufrufe erforderlich, um den Vorgang abzuschließen!
Die Platzkomplexität beträgt $O(V^2)$ für die Speicherung der dichten Kapazitätsmatrix (oder $O(V + E)$, wenn mit einer Adjacency List aus Kantenobjekten implementiert).

## Varianten & Optimierungen

- **Edmonds-Karp ($O(V E^2)$):** Genau derselbe Algorithmus, verwendet jedoch BFS anstelle von DFS. Dies verhindert mathematisch den $O(E x f)$ pathologischen Fall und gewährleistet eine streng polynomiale Laufzeit unabhängig von den Kantenkapazitäten!
- **Kapazitätsskalierung:** Es werden nur Kanten mit einer Kapazität \ge \Delta berücksichtigt. Man beginnt mit \Delta als großer Potenz von 2 und halbiert diesen Wert jedes Mal. Dadurch sinkt die Laufzeit auf $O(E^2 log U)$.

## Praktische Anwendungen

- **Verkehrsführung:** Berechnung der maximalen Anzahl von Autos, die während eines Hurrikans über ein Autobahnnetz aus einer Stadt evakuiert werden können.

## Verwandte Algorithmen in cOde(n)

- **[flow_02 – Edmonds-Karp](flow_02_edmonds-karp.md)** — Die BFS-Erweiterung dieses Algorithmus.
- **[flow_03 – Bipartite Matching](flow_03_bipartite-matching.md)** — Ein Sonderfall des Max-Flow-Algorithmus, bei dem die Kapazität jeder Kante genau 1 beträgt.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
in Anlehnung an die kanonische Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
