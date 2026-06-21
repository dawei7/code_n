# Graph-Repräsentationen

| | |
|---|---|
| **ID** | `graph_01` |
| **Kategorie** | Graphen |
| **Komplexität (erforderlich)** | Variiert je nach Repräsentation |
| **Schwierigkeit** | 2/10 |
| **Relevanz für Vorstellungsgespräche** | 10/10 |
| **GeeksForGeeks-Äquivalent** | [Graph and its representations](https://www.geeksforgeeks.org/graph-and-its-representations/) |

## Problemstellung

Bevor ein Graph-Algorithmus (BFS, DFS, Dijkstra) ausgeführt werden kann, muss die Graph-Datenstruktur zunächst aus einer gegebenen Liste von Kanten im Speicher konstruiert werden.
Gegeben sind $V$ Knoten und ein Array von $E$ Kanten, wobei `edges[i] = [u, v]` (was bedeutet, dass eine Verbindung zwischen Knoten `u` und Knoten `v` besteht). Erstellen Sie die grundlegende Graph-Repräsentation.

**Eingabe:** Anzahl der Knoten `V` und ein 2D-Integer-Array `edges`.
**Ausgabe:** Eine Datenstruktur, die den Graphen repräsentiert.

## Wann man sie verwendet

- Die obligatorischen ersten 5 Zeilen Code in 100 % aller Graph-Fragen in Vorstellungsgesprächen.
- Sie müssen basierend auf der Dichte des Graphen (dicht vs. dünn) zwischen einer Adjazenzmatrix und einer Adjazenzliste wählen.

## Ansatz

**1. Die Adjazenzmatrix:**
Ein 2D-Array der Größe V x V, wobei `matrix[u][v] = 1` gilt, wenn eine Kante von `u` nach `v` existiert, und `0` andernfalls.
- **Vorteile:** Die Überprüfung, ob eine Kante zwischen `u` und `v` existiert, benötigt absolute $O(1)$ Zeit. Das Entfernen einer Kante benötigt $O(1)$ Zeit.
- **Nachteile:** Es benötigt $O(V^2)$ Speicherplatz, unabhängig davon, wie viele Kanten tatsächlich existieren. Das Iterieren über die Nachbarn von `u` benötigt $O(V)$ Zeit, selbst wenn `u` nur einen Nachbarn hat!
- **Wann zu verwenden:** NUR, wenn der Graph extrem dicht ist (fast jeder Knoten ist mit jedem anderen Knoten verbunden, E ~= V^2) oder wenn V sehr klein ist (z. B. V \le 1000).

**2. Die Adjazenzliste:**
Ein Array von Listen (oder eine Hash Map, die einen Knoten auf eine Liste seiner Nachbarn abbildet). `adj[u] = [v1, v2, v3]`.
- **Vorteile:** Es benötigt nur $O(V + E)$ Speicherplatz. Das Iterieren über die Nachbarn von `u` benötigt nur Zeit proportional zur tatsächlichen Anzahl der Nachbarn, die `u` hat! Dies sorgt dafür, dass BFS/DFS in strikt $O(V + E)$ Zeit traversieren, anstatt in $O(V^2)$.
- **Nachteile:** Die Überprüfung, ob eine Kante zwischen `u` und `v` existiert, benötigt $O(\text{degree}(u)$) Zeit, da die Liste der Nachbarn durchsucht werden muss.
- **Wann zu verwenden:** Die Standardwahl für 99 % der Vorstellungsgespräche. Die meisten realen Graphen (soziale Netzwerke, Karten) sind extrem dünn (E \ll V^2).

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for graph_01: Graph Representation.

Build an adjacency list from a list of edges. The graph is
undirected, so each edge (u, v) adds v to u's list and u to v's.
The input may contain duplicate edges; using a per-node set
deduplicates them in O(1) each. O(n) where n is the number of
edges.
"""


def solve(num_nodes, edges):
    graph = {i: set() for i in range(num_nodes)}
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    return {node: sorted(neighbors) for node, neighbors in graph.items()}
```

</details>

## Durchlauf

`V = 4`, `edges = [[0, 1], [0, 2], [1, 2], [2, 3]]`. (Ungerichtet).

**Adjazenzmatrix:**
Anfangs ein 4 x 4 Gitter aus `0`en.
1. `[0, 1]`: `matrix[0][1] = 1`, `matrix[1][0] = 1`.
2. `[0, 2]`: `matrix[0][2] = 1`, `matrix[2][0] = 1`.
3. `[1, 2]`: `matrix[1][2] = 1`, `matrix[2][1] = 1`.
4. `[2, 3]`: `matrix[2][3] = 1`, `matrix[3][2] = 1`.
```text
[
  [0, 1, 1, 0],
  [1, 0, 1, 0],
  [1, 1, 0, 1],
  [0, 0, 1, 0]
]
```

**Adjazenzliste:**
1. `[0, 1]`: `adj[0] = [1]`, `adj[1] = [0]`.
2. `[0, 2]`: `adj[0] = [1, 2]`, `adj[2] = [0]`.
3. `[1, 2]`: `adj[1] = [0, 2]`, `adj[2] = [0, 1]`.
4. `[2, 3]`: `adj[2] = [0, 1, 3]`, `adj[3] = [2]`.
```text
{
  0: [1, 2],
  1: [0, 2],
  2: [0, 1, 3],
  3: [2]
}
```

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Adj Matrix** | $O(V^2)$ Init + $O(E)$ Add | $O(V^2)$ |
| **Adj Liste** | $O(E)$ | $O(V + E)$ |

Die Initialisierung einer Adjazenzmatrix benötigt $O(V^2)$, da ein 2D-Array physisch allokiert und mit Nullen initialisiert werden muss. Das Hinzufügen der Kanten benötigt $O(E)$. Die Gesamtzeit beträgt $O(V^2 + E)$. Der Platzbedarf ist strikt $O(V^2)$.
Die Initialisierung einer Adjazenzliste mittels einer Hash Map benötigt anfangs $O(1)$. Das Hinzufügen der Kanten benötigt $O(E)$. Die Gesamtzeit beträgt $O(E)$. Der Platzbedarf beträgt $O(V + E)$, um die Schlüssel und Listen zu speichern.

## Varianten & Optimierungen

- **Kantengewichte:** Wenn Kanten Gewichte `(u, v, weight)` haben, speichern Sie in einer Matrix `matrix[u][v] = weight` (und initialisieren Sie leere Felder mit `infinity` anstelle von `0`). In einer Adjazenzliste hängen Sie ein Tupel an: `adj[u].append((v, weight))`.
- **Set vs List:** Wenn der Graph doppelte Kanten enthält (Multigraph), fügt `adj[u].append(v)` den Wert `v` zweimal hinzu! Wenn Sie einfache Graphen erzwingen müssen, verwenden Sie `adj = defaultdict(set)` und `adj[u].add(v)`. Die Überprüfung der Existenz einer Kante wird zu $O(1)$ anstatt $O(\text{degree}(u)$), aber die Iteration wird aufgrund des Overheads von Sets etwas langsamer.

## Anwendungen in der Praxis

- **Routing-Tabellen:** Moderne Internet-Router verwenden hochoptimierte Adjazenzlisten (die die Netzwerktopologie repräsentieren), um Kürzeste-Wege-Algorithmen wie OSPF auszuführen.

## Verwandte Algorithmen in cOde(n)

- **[graph_02 - Breadth-First Search](graph_02_bfs.md)** — Der grundlegende Algorithmus, der die Adjazenzliste traversiert.
- **[graph_03 - Depth-First Search](graph_03_dfs.md)** — Die rekursive Alternative, die dieselbe Adjazenzliste traversiert.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für Wettbewerbsprogrammierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*