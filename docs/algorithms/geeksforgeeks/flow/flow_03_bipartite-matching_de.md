# Bipartite Matching (Max Flow)

| | |
|---|---|
| **ID** | `flow_03` |
| **Category** | flow |
| **Complexity (required)** | $O(V * E)$ |
| **Difficulty** | 4/10 |
| **Interview relevance** | 8/10 |
| **Wikipedia** | [Maximum bipartite matching](https://en.wikipedia.org/wiki/Matching_(graph_theory)#In_unweighted_bipartite_graphs) |

## Problem statement

Gegeben ist ein bipartiter Graph, der aus einer linken Menge von Knoten (z. B. Bewerber) und einer rechten Menge von Knoten (z. B. Jobs) besteht, wobei ungewichtete Kanten darstellen, welcher Bewerber für welchen Job qualifiziert ist.
Jeder Bewerber kann nur einen Job annehmen und jeder Job kann nur von einem Bewerber besetzt werden.
Finden Sie das **Maximum Bipartite Matching**: die maximale Anzahl an Bewerbern, die erfolgreich mit einem Job gepaart werden können.

Sie müssen dies lösen, indem Sie das Problem elegant auf ein **Max Flow Network** abbilden.

**Input:** Eine Adjazenzliste oder Matrix, die Kanten zwischen der linken Menge L und der rechten Menge R definiert.
**Output:** Eine Ganzzahl, die die maximale Anzahl an Paarungen repräsentiert.

## Wann ist es zu verwenden?

- Zur Lösung von ungewichteten Zuweisungs- und Planungsproblemen.
- Hinweis: Wenn die Kanten *Kosten* oder *Gewichte* haben (z. B. Bewerber A fordert 50k für Job 1), kann Max Flow dies nicht lösen! Sie müssen Min-Cost Max-Flow oder den Ungarischen Algorithmus (`bb_02`) verwenden.

## Ansatz

Wir können unseren bestehenden `Edmonds-Karp`- oder `Ford-Fulkerson`-Code fast ohne Änderungen übernehmen, um dies zu lösen!

**Die Abbildung:**
1. Erstellen Sie einen "Super Source"-Knoten S und einen "Super Sink"-Knoten T.
2. Zeichnen Sie eine gerichtete Kante von S zu jedem Knoten in der linken Menge (Bewerber). Geben Sie diesen Kanten eine Kapazität von genau `1`.
3. Zeichnen Sie eine gerichtete Kante von jedem Knoten in der rechten Menge (Jobs) zu T. Geben Sie diesen Kanten eine Kapazität von genau `1`.
4. Für jede existierende Qualifikationskante zwischen Bewerber A und Job J, machen Sie diese gerichtet A \to J und geben Sie ihr eine Kapazität von genau `1` (oder `Infinity`, mathematisch spielt es keine Rolle, da die Engpässe bei S und T es ohnehin auf 1 beschränken).

**Das Ergebnis:**
Da jeder Bewerber nur 1 Einheit Wasser von S erhalten kann, kann er nur 1 Einheit Wasser an einen Job weitergeben. Da jeder Job nur 1 Einheit Wasser an T weitergeben kann, kann er nur Wasser von 1 Bewerber empfangen!
Führen Sie Max Flow von S nach T aus. Der resultierende Fluss ist exakt das Maximum Bipartite Matching!

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

## Durchlauf

3 Bewerber (`A0, A1, A2`). 3 Jobs (`J0, J1, J2`).
`A0` möchte `J0`, `J1`.
`A1` möchte `J1`.
`A2` möchte `J1`.

1. **Netzwerk aufbauen:**
   - S \to A0 (1), S \to A1 (1), S \to A2 (1).
   - J0 \to T (1), J1 \to T (1), J2 \to T (1).
   - A0 \to J0 (1), A0 \to J1 (1).
   - A1 \to J1 (1).
   - A2 \to J1 (1).
2. **Edmonds-Karp ausführen:**
   - BFS findet `S -> A0 -> J0 -> T`. Schiebt 1.
   - BFS findet `S -> A1 -> J1 -> T`. Schiebt 1.
   - Nun möchte `A2` `J1`, aber die Leitung `J1 -> T` ist vollständig gesättigt (0 Restkapazität).
   - Es existieren keine weiteren Pfade!
3. **Ergebnis:** Max Flow = 2. Das optimale Matching ist (A0-J0, A1-J1). A2 bekommt nichts. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(V * E)$ | $O(V^2)$ |
| **Durchschnittlicher Fall** | $O(E * √V)$ | $O(V^2)$ |
| **Schlechtester Fall** | $O(V * E)$ | $O(V^2)$ |

Da jede Kapazität genau 1 beträgt (ein "Unit Network"), laufen Max-Flow-Algorithmen deutlich schneller als ihre theoretischen Schranken!
Edmonds-Karp garantiert auf einem Unit Network mathematisch eine Laufzeit von $O(V \times E)$ anstelle von $O(V \cdot E^2)$.
Die Platzkomplexität beträgt $O(V^2)$ bei Verwendung einer Adjazenzmatrix oder $O(V + E)$ bei Verwendung von Listen.

## Varianten & Optimierungen

- **Hopcroft-Karp-Algorithmus:** Ein hochspezialisierter Algorithmus, der ausschließlich für Bipartite Matching entwickelt wurde. Er verhält sich wie der Dinic-Algorithmus auf einem Unit Network und findet mehrere augmentierende Pfade gleichzeitig. Er läuft in einer erstaunlichen Zeit von $O(E \sqrt{V})$.

## Anwendungen in der Praxis

- **Dating-Apps:** Finden der maximalen Anzahl an gegenseitig akzeptablen Paarungen für ein Speed-Dating-Event.
- **Ressourcenallokation:** Zuweisung von IP-Adressen aus einem begrenzten DHCP-Pool an Geräte mit spezifischen Subnetz-Anfragen.

## Verwandte Algorithmen in cOde(n)

- **[flow_02 - Edmonds-Karp](flow_02_edmonds-karp.md)** — Die Kern-Engine, die diese Lösung antreibt.
- **[approx_01 - Vertex Cover](../approximation/approx_01_vertex-cover-2-approx.md)** — Nach dem Satz von König ist in jedem bipartiten Graphen die Größe des Maximum Matching exakt gleich der minimalen Knotenbedeckung!

---

*Diese Dokumentation ist ein Originalinhalt für cOde(n), modelliert nach der kanonischen Struktur, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*