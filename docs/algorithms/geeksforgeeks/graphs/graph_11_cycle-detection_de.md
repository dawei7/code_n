# Zykluserkennung (Gerichtet und Ungerichtet)

| | |
|---|---|
| **ID** | `graph_11` |
| **Kategorie** | Graphen |
| **Komplexität (erforderlich)** | $O(V + E)$ Zeit, $O(V)$ Platz |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Course Schedule](https://leetcode.com/problems/course-schedule/) |

## Problemstellung

Gegeben ist ein Graph, der als Adjacency List repräsentiert wird. Bestimmen Sie, ob der Graph mindestens einen Zyklus enthält.
Die Implementierung unterscheidet sich grundlegend, je nachdem, ob der Graph **gerichtet** oder **ungerichtet** ist.

**Eingabe:** Anzahl der Knoten `V` und eine Adjacency List `adj`.
**Ausgabe:** Ein Boolean. `True`, falls ein Zyklus existiert, andernfalls `False`.

## Wann wird es verwendet?

- Zur Validierung von Abhängigkeitsbäumen (um zu prüfen, ob ein Lehrplan unmöglich zu absolvieren ist).
- Um zu prüfen, ob ein Graph ein gültiger Baum ist (ein Baum ist ein zusammenhängender, ungerichteter Graph mit exakt 0 Zyklen).

## Ansatz 1: Ungerichtete Graphen

In einem ungerichteten Graphen verläuft eine Kante A - B in beide Richtungen. Wenn Sie A \rightarrow B durchlaufen, enthält die Nachbarliste von B den Knoten A. Wenn Sie naiv zu A zurückkehren, könnten Sie fälschlicherweise "Zyklus!" melden.
**Die Regel:** Ein Zyklus in einem ungerichteten Graphen existiert nur, wenn Sie einen BEREITS BESUCHTEN Knoten erreichen, der **NICHT IHR UNMITTELBARER VORGÄNGER (PARENT)** ist.

1. Führen Sie eine DFS durch. Übergeben Sie den `curr` Knoten und dessen `parent`.
2. Bei der Auswertung eines `neighbor` von `curr`:
   - Falls `neighbor == parent`: Ignorieren (es ist die Kante, über die wir gerade gekommen sind).
   - Falls `neighbor` in `visited` enthalten ist: Wir haben einen Zyklus gefunden!
   - Falls `neighbor` nicht in `visited` enthalten ist: Als besucht markieren und rekursiv `dfs(neighbor, parent=curr)` aufrufen.

## Ansatz 2: Gerichtete Graphen (Die 3-Farben-Methode)

In einem gerichteten Graphen funktioniert die "Parent"-Regel nicht. Der Graph A \rightarrow B, A \rightarrow C, B \rightarrow C ist vollkommen gültig (eine Rautenform, kein Zyklus). Dennoch wird C zweimal besucht! Wenn wir nur ein einfaches `visited`-Set verwenden, würden wir fälschlicherweise einen Zyklus melden, wenn der zweite Pfad C erreicht.
**Die Regel:** Ein Zyklus in einem gerichteten Graphen existiert nur, wenn Sie einen Knoten erreichen, der sich **AKTUELL IN IHREM REKURSIONS-STACK** befindet.

Wir verwenden ein `state`-Array für jeden Knoten mit 3 Farben:
- `0` (Weiß): Nicht besucht.
- `1` (Grau): Aktuell in Bearbeitung (befindet sich im aktiven DFS-Aufruf-Stack).
- `2` (Schwarz): Vollständig abgeschlossen (alle Nachfolger wurden exploriert).

1. Führen Sie eine DFS durch.
2. Markieren Sie `state[curr] = 1`.
3. Für jeden `neighbor`:
   - Falls `state[neighbor] == 1`: Wir sind zu einem Knoten im aktiven Stack zurückgekehrt! **ZYKLUS ERKANNT!**
   - Falls `state[neighbor] == 0`: Rekursiver Aufruf `dfs(neighbor)`.
4. Nachdem alle Nachbarn geprüft wurden, markieren Sie `state[curr] = 2` und kehren zurück.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for graph_11: Cycle Detection (Undirected).

Iterative DFS with parent tracking. A back-edge to a non-parent
visited node is a cycle.
"""


def solve(num_nodes, edges):
    adj = [[] for _ in range(num_nodes)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    visited = [False] * num_nodes
    for start in range(num_nodes):
        if visited[start]:
            continue
        stack = [(start, -1)]
        visited[start] = True
        while stack:
            u, parent = stack.pop()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append((v, u))
                elif v != parent:
                    return True
    return False
```

</details>

## Durchlauf (Gerichtet)

`adj = {0: [1], 1: [2], 2: [0]}`.
`state = [0, 0, 0]`.

1. Schleife beginnt bei `i=0`. `state[0] == 0`. Aufruf `dfs(0)`.
2. `dfs(0)`: `state[0] = 1`.
   - Nachbar `1`. `state[1] == 0`. Aufruf `dfs(1)`.
3. `dfs(1)`: `state[1] = 1`.
   - Nachbar `2`. `state[2] == 0`. Aufruf `dfs(2)`.
4. `dfs(2)`: `state[2] = 1`.
   - Nachbar `0`. `state[0] == 1`!
   - `1 == 1`! Zyklus erkannt! Rückgabe `True`.
5. Rückgabewerte steigen nach oben. Ausgabe ist `True`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(V + E)$ | $O(V)$ |
| **Durchschnittlicher Fall** | $O(V + E)$ | $O(V)$ |
| **Schlechtester Fall** | $O(V + E)$ | $O(V)$ |

Da wir eine DFS verwenden, die bereits vollständig verarbeitete Knoten nicht erneut besucht (entweder über das `visited`-Set oder `state == 2`), wird jeder Knoten einmal verarbeitet und jede Kante einmal durchlaufen. Die Zeitkomplexität ist strikt $O(V + E)$.
Die Platzkomplexität beträgt $O(V)$ für das `state`-Array bzw. das `visited`-Set und $O(V)$ für den Rekursions-Stack im schlechtesten Fall (eine lineare Kette).

## Varianten & Optimierungen

- **Kahn-Algorithmus (Gerichtet):** Anstatt DFS zu verwenden, können Sie eine topologische Sortierung nach Kahn (`graph_07`) durchführen. Wenn der Algorithmus terminiert, aber nicht exakt V Elemente zum Ausgabe-Array hinzugefügt hat, existiert definitiv ein Zyklus! (Dies vermeidet Limits des Rekursions-Stacks).
- **Union-Find (Ungerichtet):** Sie können eine Disjoint-Set-Datenstruktur (`graph_09`) verwenden. Iterieren Sie über alle Kanten. Wenn `find(u) == find(v)`, haben Sie gerade eine Kante gefunden, die zwei Knoten verbindet, die bereits in derselben Zusammenhangskomponente liegen! Das ist ein Zyklus! (So funktioniert Kruskal).

## Anwendungen in der Praxis

- **Deadlock-Erkennung:** Im Design von Betriebssystemkernen bildet ein "Wait-For"-Graph ab, welche Prozesse auf Locks warten, die von anderen Prozessen gehalten werden. Wenn ein Zyklus erkannt wird, befindet sich das System in einem Deadlock und ein Prozess muss beendet werden.
- **Zirkelbezüge in Tabellenkalkulationen:** Excel erkennt, ob Zelle A = Zelle B + 1 und Zelle B = Zelle A + 1 gilt, indem eine gerichtete Zykluserkennung verwendet wird.

## Verwandte Algorithmen in cOde(n)

- **[graph_03 - Depth-First Search](graph_03_dfs.md)** — Die Grundlage der Traversierung.
- **[graph_07 - Topological Sort](graph_07_topological-sort.md)** — Der Kahn-Algorithmus, die Queue-basierte Alternative für gerichtete Graphen.
- **[graph_09 - Union-Find](graph_09_union-find.md)** — Die Alternative mittels Mengenvereinigung für ungerichtete Graphen.

---

*Diese Dokumentation ist ein Originalinhalt für cOde(n), modelliert nach der kanonischen Struktur, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*