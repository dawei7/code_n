# Artikulationspunkte (Schnittknoten)

| | |
|---|---|
| **ID** | `graph_13` |
| **Kategorie** | Graphen |
| **Komplexität (erforderlich)** | $O(V + E)$ Zeit, $O(V)$ Platz |
| **Schwierigkeit** | 8/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **GeeksForGeeks Äquivalent** | [Articulation Points (or Cut Vertices) in a Graph](https://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/) |

## Problemstellung

Gegeben ist ein ungerichteter Graph. Finden Sie alle Artikulationspunkte im Graphen.
Ein Artikulationspunkt (oder Schnittknoten) ist ein Knoten, dessen Entfernung (zusammen mit allen anliegenden Kanten) die Anzahl der Zusammenhangskomponenten im Graphen erhöhen würde. Mit anderen Worten: Seine Entfernung würde einen zusammenhängenden Graphen in zwei oder mehr separate Teile zerlegen.

**Eingabe:** Anzahl der Knoten `V` und eine Adjacency List `adj`.
**Ausgabe:** Eine Liste der Knoten, die Artikulationspunkte sind.

## Anwendung

- Zur Identifizierung von Single Points of Failure in einem Netzwerk (z. B. ein zentraler Router, dessen Ausfall das Internet partitionieren würde).
- Nutzt die Logik von Tarjans Discovery/Lowest Time (ein grundlegendes Konzept fortgeschrittener Graphentheorie).

## Ansatz

**1. Der DFS-Spanning-Tree:**
Stellen Sie sich vor, Sie führen eine Standard-DFS durch und zeichnen durchgezogene Linien für die Kanten, die wir durchlaufen. Dies bildet einen "DFS-Spanning-Tree".
Jede Kante im ursprünglichen Graphen, die wir NICHT durchlaufen haben (weil sie zu einem bereits besuchten Knoten führte), wird als **Back-Edge** bezeichnet. Back-Edges zeigen im Baum nach OBEN zu einem Vorfahren.

**2. Discovery Time (`tin`) und Lowest Time (`low`):**
Wir weisen jedem Knoten eine "Discovery Time" (`tin`) zu. Dies ist lediglich ein Zähler, der bei jedem Besuch eines neuen Knotens inkrementiert wird.
Zusätzlich weisen wir eine "Lowest Time" (`low`) zu. Diese repräsentiert die absolut niedrigste `tin`, die von diesem Knoten aus erreichbar ist, *unter Einbeziehung von genau EINER Back-Edge*.
Anfänglich gilt für jeden Knoten: `low[node] = tin[node]`.

**3. Die magische Bedingung:**
Angenommen, wir befinden uns am Knoten `U` und rufen rekursiv DFS für einen Nachbarn `V` auf.
Wenn `DFS(V)` zurückkehrt, aktualisieren wir die Lowest Time von `U`: `low[U] = min(low[U], low[V])`.
Wie erkennen wir nun, ob `U` ein Artikulationspunkt ist?
Wenn `low[V] >= tin[U]` gilt, bedeutet dies, dass der Teilbaum, der in `V` verwurzelt ist, KEINE Back-Edges besitzt, die höher als `U` zeigen! Das absolut Höchste, was er erreichen kann, ist `U` selbst. Wenn wir also `U` vollständig entfernen, wird der Teilbaum `V` komplett vom Rest des Graphen getrennt!
Daher ist **`U` ein Artikulationspunkt!**

**4. Der Sonderfall Wurzelknoten:**
Der Wurzelknoten unserer DFS hat keine Vorfahren, daher ist `tin[U]` gleich 1. Alle seine Kinder werden logischerweise `low[V] >= 1` haben. Macht das die Wurzel zu einem Artikulationspunkt? Nicht notwendigerweise!
Die Wurzel ist NUR DANN ein Artikulationspunkt, wenn sie **mehr als ein unabhängiges DFS-Kind** hat. (Wenn sie nur 1 Kind hat, entfernt das Löschen der Wurzel nur den Anfang einer Kette, es partitioniert nichts).

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for graph_13: Articulation Points.

Tarjan-style DFS on an undirected graph. A node u is an
articulation point iff one of its DFS-tree children v has
``low[v] >= disc[u]`` (and u is not the root, OR u is the
root with more than one DFS child). The result is the sorted
list of articulation point indices.
"""


def solve(num_nodes, edges):
    if num_nodes <= 0:
        return []
    adj = [set() for _ in range(num_nodes)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    disc = [-1] * num_nodes
    low = [0] * num_nodes
    parent = [-1] * num_nodes
    ap = set()

    def dfs(u, time):
        disc[u] = low[u] = time
        time += 1
        children = 0
        for v in sorted(adj[u]):
            if disc[v] == -1:
                parent[v] = u
                children += 1
                time = dfs(v, time)
                low[u] = min(low[u], low[v])
                if parent[u] == -1 and children > 1:
                    ap.add(u)
                if parent[u] != -1 and low[v] >= disc[u]:
                    ap.add(u)
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])
        return time

    dfs(0, 0)
    return sorted(ap)
```

</details>

## Durchlauf

`V = 5`. Kanten: `0-1`, `1-2`, `2-0`, `1-3`, `3-4`.
Der Graph ist ein Dreieck `{0, 1, 2}`, das mit einer Linie `1-3-4` verbunden ist.
Intuitiv sind `1` und `3` die Artikulationspunkte.

1. `dfs(0, -1)`. `tin[0]=1, low[0]=1`.
   - Nachbar `1`. `dfs(1, 0)`.
2. `dfs(1, 0)`. `tin[1]=2, low[1]=2`.
   - Nachbar `2`. `dfs(2, 1)`.
3. `dfs(2, 1)`. `tin[2]=3, low[2]=3`.
   - Nachbar `0`. Besucht! Back-Edge!
   - `low[2] = min(low[2], tin[0]) = min(3, 1) = 1`.
   - Rückkehr zu `dfs(1)`.
4. `dfs(1)` wird fortgesetzt:
   - Aktualisiert `low[1] = min(low[1], low[2]) = min(2, 1) = 1`.
   - Bedingung: `low[2] >= tin[1]` -> `1 >= 2`. FALSCH.
   - Nachbar `3`. `dfs(3, 1)`.
5. `dfs(3, 1)`. `tin[3]=4, low[3]=4`.
   - Nachbar `4`. `dfs(4, 3)`.
6. `dfs(4, 3)`. `tin[4]=5, low[4]=5`.
   - Keine Nachbarn. Rückkehr zu `dfs(3)`.
7. `dfs(3)` wird fortgesetzt:
   - Aktualisiert `low[3] = min(low[3], low[4]) = min(4, 5) = 4`.
   - Bedingung: `low[4] >= tin[3]` -> `5 >= 4`. WAHR!
   - `3` ist ein Artikulationspunkt! (Elternknoten ist nicht -1).
   - Rückkehr zu `dfs(1)`.
8. `dfs(1)` wird fortgesetzt:
   - Aktualisiert `low[1] = min(low[1], low[3]) = min(1, 4) = 1`.
   - Bedingung: `low[3] >= tin[1]` -> `4 >= 2`. WAHR!
   - `1` ist ein Artikulationspunkt!
9. `dfs(0)` wird fortgesetzt. `children = 1`. Wurzel-Bedingung schlägt fehl.

Ergebnis: `{1, 3}`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(V + E)$ | $O(V)$ |
| **Durchschnittlicher Fall** | $O(V + E)$ | $O(V)$ |
| **Schlechtester Fall** | $O(V + E)$ | $O(V)$ |

Dies entspricht exakt einem vollständigen DFS-Durchlauf. Wir führen bei jedem Schritt konstante $O(1)$ Berechnungen durch, um die `tin`- und `low`-Arrays zu pflegen. Daher ist die Zeitkomplexität strikt $O(V + E)$.
Die Platzkomplexität beträgt $O(V)$ für das `tin`-Array, das `low`-Array, das `visited`-Set und den Rekursions-Stack.

## Varianten & Optimierungen

- **Brücken (`graph_14`):** Wenn Sie Schnittkanten anstelle von Schnittknoten finden möchten, ist der Algorithmus zu 99 % identisch! Der einzige Unterschied besteht darin, dass die mathematische Bedingung strikt größer wird: `low[neighbor] > tin[curr]`.

## Anwendungen in der Praxis

- **Netzwerk-Schwachstellenanalyse:** Auffinden der exakten Server oder physischen Kabel, deren Zerstörung ein lokales LAN oder ein globales Stromnetz partitionieren würde, was Ingenieuren ermöglicht, gezielte Redundanzen aufzubauen.

## Verwandte Algorithmen in cOde(n)

- **[graph_14 - Bridges in a Graph](graph_14_bridges.md)** — Das kantenbasierte Äquivalent zu diesem Algorithmus.
- **[graph_15 - Tarjan's SCC](graph_15_tarjan-s-scc.md)** — Tarjans Hauptalgorithmus für gerichtete Graphen, der denselben `tin`- und `low`-Mechanismus verwendet, um stark zusammenhängende Komponenten zu finden.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den enzyklopädischen Standardeintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*