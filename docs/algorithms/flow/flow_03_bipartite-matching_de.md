# Zweigeteilte Zuordnung (Maximalfluss)

| | |
|---|---|
| **ID** | `flow_03` |
| **Kategorie** | Fluss |
| **Komplexität (erforderlich)** | $O(V * E)$ |
| **Schwierigkeitsgrad** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **Wikipedia** | [Maximale bipartite Zuordnung](https://en.wikipedia.org/wiki/Matching_(graph_theory)#In_unweighted_bipartite_graphs) |

## Aufgabenstellung

Gegeben ist ein bipartiter Graph, bestehend aus einer linken Menge von Knoten (z. B. Bewerber) und einer rechten Menge von Knoten (z. B. Stellen), mit ungewichteten Kanten, die angeben, welcher Bewerber für welche Stelle qualifiziert ist.
Jeder Bewerber kann nur eine Stelle annehmen, und jede Stelle kann nur von einem Bewerber besetzt werden.
Ermitteln Sie die **maximale bipartite Zuordnung**: die maximale Anzahl an Bewerbern, die erfolgreich einer Stelle zugeordnet werden können.

Sie müssen dies lösen, indem Sie das Problem elegant in ein **Max-Flow-Netzwerk** abbilden.

**Eingabe:** Eine Adjacency List oder Matrix, die Kanten zwischen der linken Menge L und der rechten Menge R definiert.
**Ausgabe:** Eine ganze Zahl, die die maximale Anzahl an Paarungen angibt.

## Wann man es verwendet

- Zur Lösung ungewichteter Zuordnungs- und Terminierungsprobleme.
- Hinweis: Wenn die Kanten *Kosten* oder *Gewichte* haben (z. B. Bewerber A verlangt 50k für Stelle 1), kann das Max-Flow-Verfahren das Problem nicht lösen! Sie müssen den Min-Cost-Max-Flow-Algorithmus oder den ungarischen Algorithmus (`bb_02`) verwenden.

## Vorgehensweise

Wir können unseren bestehenden Code aus `Edmonds-Karp` oder `Ford-Fulkerson` fast unverändert übernehmen, um dieses Problem zu lösen!

**Die Zuordnung:**
1. Erstelle einen „Super-Quelle“-Knoten S und einen „Super-Senke“-Knoten T.
2. Zeichne eine gerichtete Kante von S zu jedem Knoten der linken Menge (Bewerber). Weise diesen Kanten eine Kapazität von genau `1` zu.
3. Zeichne eine gerichtete Kante von jedem Knoten der rechten Menge (Stellen) zu T. Weise diesen Kanten eine Kapazität von genau `1` zu.
4. Machen Sie jede vorhandene Qualifikationskante zwischen Bewerber A und Stelle J zu einer gerichteten Kante A \to J und weisen Sie ihr eine Kapazität von genau `1` zu (oder `Infinity`, mathematisch spielt das keine Rolle, da die Engpässe bei S und T sie ohnehin auf 1 beschränken).

**Das Ergebnis:**
Da jeder Bewerber nur 1 Einheit Wasser von S erhalten kann, kann er nur 1 Einheit Wasser an einen Job weitergeben. Da jeder Job nur 1 Einheit Wasser an T weitergeben kann, kann er Wasser nur von 1 Bewerber erhalten!
Führe „Max Flow“ von S nach T aus. Der resultierende Durchfluss entspricht genau der maximalen bipartiten Zuordnung!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for flow_03: Bipartite Matching.

Reduce to max flow: source -> left (cap 1) -> right (cap 1) -> sink.
Max flow = max matching size.
"""


def solve(left_n, right_n, edges):
    from collections import deque
    n = left_n + right_n + 2
    source = 0
    sink = n - 1
    cap = [[0] * n for _ in range(n)]
    for u, v in edges:
        cap[1 + u][1 + left_n + v] += 1
    for u in range(left_n):
        cap[source][1 + u] += 1
    for v in range(right_n):
        cap[1 + left_n + v][sink] += 1
    flow = 0
    while True:
        parent = [-1] * n
        parent[source] = source
        q = deque([source])
        visited = [False] * n
        visited[source] = True
        while q and parent[sink] == -1:
            u = q.popleft()
            for v in range(n):
                if not visited[v] and cap[u][v] > 0:
                    visited[v] = True
                    parent[v] = u
                    q.append(v)
        if parent[sink] == -1:
            break
        path_flow = float("inf")
        v = sink
        while v != source:
            u = parent[v]
            if cap[u][v] < path_flow:
                path_flow = cap[u][v]
            v = u
        v = sink
        while v != source:
            u = parent[v]
            cap[u][v] -= path_flow
            cap[v][u] += path_flow
            v = u
        flow += path_flow
    return flow
```

</details>

## Schritt-für-Schritt-Anleitung

3 Bewerber (`A0, A1, A2`). 3 Stellen (`J0, J1, J2`).
`A0` möchte `J0`, `J1`.
`A1` möchte `J1`.
`A2` möchte `J1`.

1. **Netzwerk aufbauen:**
   - S \to A0 (1), S \to A1 (1), S \to A2 (1).
   - J0 \to T (1), J1 \to T (1), J2 \to T (1).
   - A0 \to J0 (1), A0 \to J1 (1).
   - A1 \to J1 (1).
   - A2 → J1 (1).
2. **Edmonds-Karp-Algorithmus ausführen:**
   - BFS findet `S -> A0 -> J0 -> T`. Schiebt 1 auf den Stack.
   - BFS findet `S -> A1 -> J1 -> T`. Schiebt 1 auf den Stack.
   - Nun möchte `A2` `J1` erreichen, aber die Leitung `J1 -> T` ist vollständig ausgelastet (0 Restkapazität).
   - Es gibt keine weiteren Pfade mehr!
3. **Ergebnis:** Maximaler Durchfluss = 2. Die optimale Zuordnung lautet (A0-J0, A1-J1). A2 erhält nichts. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Best** | $O(V * E)$ | $O(V^2)$ |
| **Durchschnittlicher Fall** | $O(E * √V)$ | $O(V^2)$ |
| **Schlechtester Fall** | $O(V * E)$ | $O(V^2)$ |

Da jede Kapazität genau 1 beträgt (ein „Einheitsnetzwerk“), laufen Max-Flow-Algorithmen deutlich schneller als ihre theoretischen Grenzen!
Für Edmonds-Karp in einem Einheitsnetzwerk ist mathematisch garantiert, dass es in $O(V \times E)$ statt in $O(V \cdot E^2)$ läuft.
Die Platzkomplexität beträgt $O(V^2)$, wenn eine Adjacency Matrix verwendet wird, oder $O(V + E)$, wenn Listen verwendet werden.

## Varianten & Optimierungen

- **Hopcroft-Karp-Algorithmus:** Ein hochspezialisierter Algorithmus, der *ausschließlich* für die bipartite Zuordnung entwickelt wurde. Er verhält sich wie der Dinic-Algorithmus in einem Einheitsnetzwerk und findet gleichzeitig mehrere augmentierende Pfade. Er läuft in einer erstaunlichen Zeit von O(E \sqrt{V})$.

## Praktische Anwendungen

- **Dating-Apps:** Ermittlung der maximalen Anzahl gegenseitig akzeptabler Paarungen für eine Speed-Dating-Veranstaltung.
- **Ressourcenzuweisung:** Zuweisung von IP-Adressen aus einem begrenzten DHCP-Pool an Geräte mit spezifischen Subnetz-Anforderungen.

## Verwandte Algorithmen in cOde(n)

- **[flow_02 – Edmonds-Karp](flow_02_edmonds-karp.md)** — Die Kern-Engine, die diese Lösung antreibt.
- **[approx_01 – Vertex-Cover](../approximation/approx_01_vertex-cover-2-approx.md)** — Nach dem Satz von König ist in jedem bipartiten Graphen die Größe der maximalen Paarung genau gleich der des minimalen Vertex-Covers!

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde
und sich an der kanonischen Struktur orientiert, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
