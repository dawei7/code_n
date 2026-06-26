# Bipartite Graph Check

| | |
|---|---|
| **ID** | `graph_12` |
| **Category** | graphs |
| **Complexity (required)** | $O(V + E)$ Time, $O(V)$ Space |
| **Difficulty** | 4/10 |
| **Interview relevance** | 6/10 |
| **LeetCode Equivalent** | [Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/) |

## Problem statement

Gegeben ist ein ungerichteter Graph, der als Adjazenzliste dargestellt ist. Bestimmen Sie, ob der Graph bipartit ist.
Ein Graph ist bipartit, wenn seine Knoten in zwei unabhängige Mengen, U und V, unterteilt werden können, sodass jede Kante einen Knoten in U mit einem Knoten in V verbindet.
Äquivalent dazu: Können Sie jeden Knoten im Graphen mit genau 2 Farben so färben, dass keine zwei benachbarten Knoten die gleiche Farbe haben?

**Input:** Anzahl der Knoten `V` und eine Adjazenzliste `adj`.
**Output:** Ein Boolean. `True`, wenn der Graph bipartit ist, `False` andernfalls.

## Wann man es verwendet

- Wenn geprüft werden soll, ob Elemente in zwei sich gegenseitig ausschließende Gruppen unterteilt werden können (z. B. Zuordnung von Bewerbern zu Jobs oder die Prüfung, ob eine Gruppe von Personen in zwei rivalisierende Teams aufgeteilt werden kann, in denen keine Freunde im selben Team sind).
- *Mathematische Eigenschaft:* Ein Graph ist genau dann bipartit, wenn er KEINE Zyklen ungerader Länge enthält.

## Ansatz

**Die 2-Färbungsmethode (BFS oder DFS):**
Wir können dies einfach mittels Breadth-First Search (BFS) lösen.
Wir führen ein Array `colors[]`, das mit -1 (ungefärbt) initialisiert ist. Wir verwenden `0` für Rot und `1` für Blau.

1. Wählen Sie einen ungefärbten Knoten. Färben Sie ihn `0` (Rot) und fügen Sie ihn zur Queue hinzu.
2. Solange die Queue nicht leer ist, entnehmen Sie einen Knoten `curr`.
3. Betrachten Sie alle seine `neighbors`.
   - Wenn ein `neighbor` ungefärbt (`-1`) ist, färben Sie ihn mit der GEGENTEILIGEN Farbe von `curr` (`1 - colors[curr]`) und fügen Sie ihn zur Queue hinzu!
   - Wenn ein `neighbor` bereits gefärbt ist, prüfen Sie dessen Farbe! Wenn `colors[neighbor] == colors[curr]`, haben wir zwei benachbarte Knoten mit exakt derselben Farbe! Der Graph ist NICHT bipartit! Geben Sie `False` zurück.
4. Wenn die Queue leer ist und keine Konflikte aufgetreten sind, ist die Zusammenhangskomponente bipartit.
5. Da der Graph unzusammenhängend sein könnte, kapseln Sie diese Logik in eine `for`-Schleife über alle V Knoten.

## Algorithmus

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for graph_12: Bipartite Check.

BFS-based 2-coloring. A graph is bipartite iff no node is forced
to have the same color as an already-colored neighbor.
"""


def solve(num_nodes, edges):
    from collections import deque
    adj = [[] for _ in range(num_nodes)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    color = [-1] * num_nodes
    for start in range(num_nodes):
        if color[start] != -1:
            continue
        color[start] = 0
        q = deque([start])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    return False
    return True
```

</details>

## Walk-through

`V = 4`. Graph: `0-1`, `0-3`, `1-2`, `2-3`. (Ein quadratischer Zyklus).
`adj = {0:[1,3], 1:[0,2], 2:[1,3], 3:[0,2]}`.
`colors = [-1, -1, -1, -1]`.

1. Schleife `i=0`. Ungefärbt.
   - `colors[0] = 0`. `queue = [0]`.
2. `curr = 0`.
   - Nachbarn: `1`, `3`.
   - `1` ungefärbt. `colors[1] = 1 - 0 = 1`. `queue = [1]`.
   - `3` ungefärbt. `colors[3] = 1 - 0 = 1`. `queue = [1, 3]`.
3. `curr = 1`.
   - Nachbarn: `0`, `2`.
   - `0` gefärbt mit `0`. `colors[curr]` ist `1`. Alles in Ordnung.
   - `2` ungefärbt. `colors[2] = 1 - 1 = 0`. `queue = [3, 2]`.
4. `curr = 3`.
   - Nachbarn: `0`, `2`.
   - `0` gefärbt mit `0`. `colors[curr]` ist `1`. Alles in Ordnung.
   - `2` gefärbt mit `0`. `colors[curr]` ist `1`. Alles in Ordnung.
5. `curr = 2`.
   - Nachbarn: `1`, `3`.
   - `1` gefärbt mit `1`. `colors[curr]` ist `0`. Alles in Ordnung.
   - `3` gefärbt mit `1`. `colors[curr]` ist `0`. Alles in Ordnung.

Das Ergebnis ist `True`. (Die Mengen sind `{0, 2}` und `{1, 3}`).

*Was wäre, wenn wir die Kante `0-2` hinzufügen würden? (Erzeugung eines Dreiecks / ungeraden Zyklus).*
In Schritt 4, `curr=2` (Farbe 0). Nachbar `0` hat Farbe 0.
Konflikt! `0 == 0`. Gibt `False` zurück. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(V + E)$ | $O(V)$ |
| **Durchschnittlicher Fall** | $O(V + E)$ | $O(V)$ |
| **Schlechtester Fall** | $O(V + E)$ | $O(V)$ |

Dies ist buchstäblich nur eine Standard Breadth-First Search mit einem zusätzlichen $O(1)$ Array-Zugriff pro Nachbarn.
Jeder Knoten wird genau einmal in die Queue eingefügt und jede Kante wird zweimal durchlaufen. Die Zeitkomplexität ist strikt $O(V + E)$.
Die Platzkomplexität beträgt $O(V)$ für das `colors`-Array und die BFS-`queue`.

## Varianten & Optimierungen

- **DFS-Ansatz:** Sie können exakt dieselbe Logik einfach mittels rekursiver DFS implementieren. Anstatt Elemente in eine Queue einzufügen, rufen Sie einfach `if not dfs(neighbor, 1 - color): return False` auf. Zeit- und Platzkomplexität sind identisch.
- **Graphfärbung (NP-schwer):** Die Bestimmung, ob ein Graph bipartit ist, entspricht der Frage: "Ist dieser Graph 2-färbbar?". Das ist einfach! Die Frage jedoch, ob ein Graph 3-färbbar oder k-färbbar ist, ist das berühmte Graphfärbungsproblem, welches NP-vollständig ist und Backtracking (`graph_19`) erfordert!

## Anwendungen in der Praxis

- **Empfehlungs-Engines / Matching-Algorithmen:** Die Modellierung von Dating-Apps (Matching von Gruppe A zu Gruppe B) oder Ride-Sharing-Netzwerken (Matching von Fahrern zu Mitfahrern) erfordert mathematisch die Modellierung des Systems als bipartiter Graph, um den Hopcroft-Karp-Algorithmus für das maximale bipartite Matching auszuführen.

## Verwandte Algorithmen in cOde(n)

- **[graph_02 - Breadth-First Search](graph_02_bfs.md)** — Der grundlegende Traversierungsalgorithmus.
- **[graph_19 - M-Coloring Problem](graph_19_m-coloring-problem.md)** — Die Verallgemeinerung dieses Problems auf M Farben, was die Schwierigkeit sofort von $O(V+E)$ linear auf $O(M^V)$ exponentiell anhebt!

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*