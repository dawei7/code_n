# Strongly Connected Components (Tarjan's)

| | |
|---|---|
| **ID** | `graph_15` |
| **Kategorie** | graphs |
| **Komplexität (erforderlich)** | $O(V + E)$ Zeit, $O(V)$ Platz |
| **Schwierigkeit** | 9/10 |
| **Relevanz für Vorstellungsgespräche** | 3/10 |
| **Wikipedia** | [Tarjan's strongly connected components algorithm](https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm) |

## Problemstellung

Gegeben ist ein gerichteter Graph. Finde alle seine Strongly Connected Components (SCCs).
Eine SCC ist eine maximale Teilmenge von Knoten, bei der jeder Knoten jeden anderen Knoten innerhalb dieser Teilmenge erreichen kann. (In einem gerichteten Graphen bedeutet die Existenz von $A \rightarrow B$ nicht automatisch, dass $B$ auch $A$ erreichen kann).

**Eingabe:** Anzahl der Knoten `V` und eine Adjazenzliste `adj`.
**Ausgabe:** Eine Liste von Listen, wobei jede innere Liste die Knoten einer SCC enthält.

## Wann man es verwendet

- Wenn man einen gerichteten Graphen mit Zyklen in einen Directed Acyclic Graph (DAG) kondensieren möchte, indem man jeden Zyklus zu einem einzelnen "Super-Knoten" zusammenfasst.
- Um gegenseitig erreichbare Cluster von Knoten zu finden.

## Ansatz

Tarjan's Algorithmus verwendet exakt dieselben `tin` (Discovery Time) und `low` (Lowest Time) Arrays wie bei Artikulationspunkten/Brücken (`graph_13`), führt jedoch zusätzlich einen **Stack** ein.

**1. Die SCC-Wurzel:**
Bei einer DFS-Traversierung wird der erste Knoten einer SCC, den wir besuchen, als "Wurzel" dieser SCC betrachtet. Jeder andere Knoten in der SCC wird Teil des DFS-Teilbaums unter dieser Wurzel sein.
Da jeder Knoten in einer SCC jeden anderen Knoten erreichen kann, gibt es Rückwärtskanten (Back-edges), die sie miteinander verbinden!
Daher wird der `low`-Wert für JEDEN Knoten in der SCC schließlich auf den `tin`-Wert der SCC-Wurzel sinken!
Fazit: Ein Knoten `U` ist die Wurzel einer SCC genau dann, wenn **`low[U] == tin[U]`** gilt, nachdem sein gesamter Teilbaum erkundet wurde.

**2. Der Stack:**
Wenn wir einen Knoten besuchen, legen wir ihn auf einen `stack` und markieren ihn als `on_stack = True`.
Wenn wir einen Nachbarn `V` evaluieren:
- Wenn er unbesucht ist, führen wir eine DFS in ihn aus und setzen `low[U] = min(low[U], low[V])`.
- Wenn er bereits besucht wurde, prüfen wir, ob er `on_stack` ist. Falls ja, handelt es sich um eine Rückwärtskante! `low[U] = min(low[U], tin[V])`. (Beachte, dass wir `tin[V]` verwenden, nicht `low[V]`, um ein "Durchsickern" zwischen Komponenten zu verhindern).
- Wenn er besucht, aber NICHT `on_stack` ist, bedeutet dies, dass er zu einer völlig anderen SCC gehört, die bereits vollständig verarbeitet und abgeschlossen wurde. Wir ignorieren ihn komplett! (Cross-edge).

**3. Extrahieren der SCC:**
Wenn `DFS(U)` die Evaluierung aller Nachbarn abgeschlossen hat, prüfen wir, ob `low[U] == tin[U]` gilt.
Falls ja, ist `U` eine SCC-Wurzel! Das bedeutet, dass jeder Knoten, der sich aktuell über `U` auf dem `stack` befindet, zur SCC von `U` gehört!
Wir nehmen die Knoten nacheinander vom Stack und fügen sie unserem aktuellen SCC-Array hinzu, bis wir `U` selbst vom Stack nehmen.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for graph_15: Tarjan's SCC.

Single-pass DFS on a directed graph that maintains each node's
discovery time and low-link value. When low[u] == disc[u], u
is the root of an SCC; pop the stack until u is removed.
Returns a list of SCCs, each sorted; outer list sorted by
smallest element.
"""


def solve(num_nodes, edges):
    if num_nodes <= 0:
        return []
    adj = [[] for _ in range(num_nodes)]
    for u, v in edges:
        adj[u].append(v)
    disc = [-1] * num_nodes
    low = [0] * num_nodes
    on_stack = [False] * num_nodes
    stack = []
    sccs = []

    def dfs(u, time):
        disc[u] = low[u] = time
        time += 1
        stack.append(u)
        on_stack[u] = True
        for v in sorted(adj[u]):
            if disc[v] == -1:
                time = dfs(v, time)
                low[u] = min(low[u], low[v])
            elif on_stack[v]:
                low[u] = min(low[u], disc[v])
        if low[u] == disc[u]:
            component = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                component.append(w)
                if w == u:
                    break
            sccs.append(sorted(component))
        return time

    for start in range(num_nodes):
        if disc[start] == -1:
            dfs(start, 0)
    return sorted(sccs, key=lambda c: c[0])
```

</details>

## Durchlauf

`V = 4`. Gerichtete Kanten: `0->1`, `1->2`, `2->0`, `1->3`.
Das Dreieck `{0, 1, 2}` ist eine SCC. `{3}` ist eine eigene SCC.

1. `dfs(0)`. `tin[0]=1, low[0]=1`. `stack=[0]`.
2. `dfs(1)`. `tin[1]=2, low[1]=2`. `stack=[0, 1]`.
3. `dfs(2)`. `tin[2]=3, low[2]=3`. `stack=[0, 1, 2]`.
   - Nachbar `0`. Er ist besucht UND `on_stack`!
   - `low[2] = min(3, tin[0]) = 1`.
   - Rückkehr zu `dfs(1)`.
4. `dfs(1)` wird fortgesetzt:
   - Aktualisiert `low[1] = min(2, low[2]) = 1`.
   - Evaluiert nächsten Nachbarn `3`.
   - `dfs(3)`. `tin[3]=4, low[3]=4`. `stack=[0, 1, 2, 3]`.
5. `dfs(3)`:
   - Keine Nachbarn.
   - SCC-Check: `low[3] == tin[3]` (4 == 4). WAHR!
   - Stack leeren bis `3`. Wir nehmen `3` vom Stack.
   - `sccs.append([3])`. `stack = [0, 1, 2]`.
   - Rückkehr zu `dfs(1)`.
6. `dfs(1)` wird fortgesetzt:
   - Nachbarn erschöpft. SCC-Check: `low[1] == tin[1]` (1 == 2). FALSCH.
   - Rückkehr zu `dfs(0)`.
7. `dfs(0)` wird fortgesetzt:
   - Aktualisiert `low[0] = min(1, low[1]) = 1`.
   - Nachbarn erschöpft. SCC-Check: `low[0] == tin[0]` (1 == 1). WAHR!
   - Stack leeren bis `0`. Wir nehmen `2`, `1`, `0` vom Stack.
   - `sccs.append([2, 1, 0])`. `stack = []`.

Ergebnis: `[[3], [2, 1, 0]]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(V + E)$ | $O(V)$ |
| **Durchschnittlicher Fall** | $O(V + E)$ | $O(V)$ |
| **Schlechtester Fall** | $O(V + E)$ | $O(V)$ |

Dies ist eine DFS in einem einzigen Durchlauf. Jeder Knoten wird einmal besucht, einmal auf den Stack gelegt und einmal vom Stack genommen. Jede gerichtete Kante wird exakt einmal traversiert. Die Zeitkomplexität ist hochoptimiert $O(V + E)$.
Die Platzkomplexität beträgt $O(V)$, um die Strukturen `tin`, `low`, `on_stack` und `stack` zu speichern.

## Varianten & Optimierungen

- **Kosaraju's Algorithmus (`graph_16`):** Die Alternative zu Tarjan. Er führt eine Standard-DFS aus, kehrt physisch JEDE Kante im gesamten Graphen um und führt dann basierend auf der Exit-Reihenfolge des ersten Durchlaufs erneut eine DFS aus! Er ist konzeptionell deutlich einfacher zu verstehen, erfordert aber zwei vollständige Durchläufe und den Aufbau einer sekundären, umgekehrten Adjazenzliste.

## Anwendungen in der Praxis

- **2-SAT-Problem:** In der booleschen Logik wird die Erfüllbarkeit einer Gleichung wie `(A OR B) AND (!A OR C)` durch die Konstruktion eines Implikationsgraphen (`!A -> B, !B -> A...`) gelöst. Die Gleichung ist genau dann lösbar, wenn KEINE Variable und ihre Negation innerhalb derselben Strongly Connected Component existieren!

## Verwandte Algorithmen in cOde(n)

- **[graph_13 - Articulation Points](graph_13_articulation-points.md)** — Die Grundlage des `tin/low`-Konzepts für ungerichtete Graphen.
- **[graph_16 - Kosaraju's SCC](graph_16_kosaraju-s-scc.md)** — Der alternative Algorithmus mit zwei Durchläufen zur Bestimmung von SCCs.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*