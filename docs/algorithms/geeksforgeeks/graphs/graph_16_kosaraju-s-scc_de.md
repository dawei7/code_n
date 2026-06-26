# Kosaraju-Algorithmus (SCC)

| | |
|---|---|
| **ID** | `graph_16` |
| **Kategorie** | Graphen |
| **Komplexität (erforderlich)** | $O(V + E)$ Zeit, $O(V + E)$ Platz |
| **Schwierigkeit** | 6/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **Wikipedia** | [Kosaraju's algorithm](https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm) |

## Problemstellung

Gegeben ist ein gerichteter Graph. Finde alle seine stark zusammenhängenden Komponenten (Strongly Connected Components, SCCs).
Eine SCC ist eine maximale Teilmenge von Knoten, bei der jeder Knoten jeden anderen Knoten innerhalb dieser Teilmenge erreichen kann.
*Einschränkung:* Löse dies mit dem zweistufigen Kosaraju-Algorithmus anstelle des einstufigen Tarjan-Algorithmus.

**Eingabe:** Anzahl der Knoten `V` und eine Adjacency List `adj`.
**Ausgabe:** Eine Liste von Listen, wobei jede innere Liste die Knoten einer SCC enthält.

## Wann man ihn verwendet

- Um stark zusammenhängende Komponenten zu finden, wenn der Tarjan-Algorithmus (`graph_15`) zu schwer zu merken ist. Die Logik von Kosaraju ist wesentlich einfacher, da sie rein auf einer Standard-DFS basiert, allerdings auf Kosten von zwei Durchläufen und der Notwendigkeit, einen transponierten Graphen im Speicher zu halten.

## Ansatz

**1. Die Erkenntnis zur topologischen Sortierung (Durchlauf 1):**
Stell dir einen Graphen mit zwei SCCs vor: SCC_1 und SCC_2. Es gibt eine gerichtete Kante, die sie verbindet: SCC_1 \rightarrow SCC_2.
Wenn wir eine DFS ausgehend von einem Knoten in SCC_1 starten, wird sie die gesamte SCC_1 erkunden, die Brücke überqueren und die gesamte SCC_2 erkunden, bevor sie zurückkehrt.
Wenn wir Knoten nur dann auf einen `stack` legen, wenn ihre rekursive DFS-Funktion vollständig abgeschlossen ist (genau wie bei der topologischen Sortierung), landen die Knoten von SCC_1 ganz OBEN auf dem Stack und die Knoten von SCC_2 ganz UNTEN.
Warum? Weil die DFS in SCC_2 gefangen bleibt! SCC_2 hat keine Möglichkeit, zu SCC_1 zurückzukehren, daher müssen die DFS-Aufrufe von SCC_2 zuerst abgeschlossen sein.

**2. Graphentransposition (Umkehren der Kanten):**
Was passiert, wenn wir jede gerichtete Kante U \rightarrow V im Graphen nehmen und sie zu V \rightarrow U umkehren?
- Innerhalb einer SCC ändert das Umkehren aller Kanten nichts. Es bleibt ein Zyklus, und jeder Knoten kann immer noch jeden anderen Knoten erreichen.
- ABER die Brückenkante SCC_1 \rightarrow SCC_2 wird zu SCC_2 \rightarrow SCC_1 umgekehrt!

**3. Der zweite Durchlauf:**
Lassen wir nun Knoten vom `stack` herunter, den wir in Durchlauf 1 aufgebaut haben. Die Spitze des Stacks ist garantiert ein Knoten aus SCC_1.
Wir führen eine neue DFS ausgehend von diesem SCC_1-Knoten auf dem **transponierten** Graphen durch.
Da die Brückenkante umgekehrt wurde, ist die DFS nun innerhalb von SCC_1 *gefangen*! Sie kann SCC_2 nicht mehr erreichen!
Daher bilden alle Knoten, die diese zweite DFS erfolgreich besucht, genau eine reine SCC. Wir sammeln sie ein, markieren sie als besucht und nehmen den nächsten unbesuchten Knoten vom Stack, um die nächste SCC zu finden!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for graph_16: Kosaraju's SCC.

Two-pass DFS on a directed graph. Pass 1 walks the original
graph, pushing each node onto a stack when its DFS finishes.
Pass 2 walks the transpose graph in stack-pop order; each DFS
tree in pass 2 is one SCC. Outer list sorted by smallest
element.
"""


def solve(num_nodes, edges):
    if num_nodes <= 0:
        return []
    adj = [[] for _ in range(num_nodes)]
    radj = [[] for _ in range(num_nodes)]
    for u, v in edges:
        adj[u].append(v)
        radj[v].append(u)
    visited = [False] * num_nodes
    order = []

    def dfs1(u):
        visited[u] = True
        for v in sorted(adj[u]):
            if not visited[v]:
                dfs1(v)
        order.append(u)

    for u in range(num_nodes):
        if not visited[u]:
            dfs1(u)
    visited = [False] * num_nodes
    sccs = []

    def dfs2(u, comp):
        visited[u] = True
        comp.append(u)
        for v in sorted(radj[u]):
            if not visited[v]:
                dfs2(v, comp)

    for u in reversed(order):
        if not visited[u]:
            comp = []
            dfs2(u, comp)
            sccs.append(sorted(comp))
    return sorted(sccs, key=lambda c: c[0])
```

</details>

## Durchlauf

`V = 4`. Gerichtete Kanten: `0->1`, `1->2`, `2->0`, `1->3`.
Das Dreieck `{0, 1, 2}` ist SCC_1. `{3}` ist SCC_2. Die Brücke ist `1->3`.

**Durchlauf 1:**
1. `dfs_pass1(0)`: Ruft `dfs(1)` auf.
2. `dfs_pass1(1)`: Ruft `dfs(2)` und `dfs(3)` auf.
3. `dfs_pass1(3)`: Keine unbesuchten Nachbarn. Fertig! `stack = [3]`.
4. `dfs_pass1(2)`: Nachbar `0` ist besucht. Fertig! `stack = [3, 2]`.
5. `dfs(1)` fertig. `stack = [3, 2, 1]`.
6. `dfs(0)` fertig. `stack = [3, 2, 1, 0]`.

**Transponierung:**
Umgekehrte Kanten: `1->0`, `2->1`, `0->2`, `3->1`.
Beachte, dass die Brücke nun `3->1` ist. SCC_1 kann SCC_2 nicht mehr erreichen!

**Durchlauf 2:**
1. Pop `0`. Unbesucht. `dfs_pass2(0)` auf dem umgekehrten Graphen:
   - `0` erreicht `2`. `2` erreicht `1`. `1` versucht `0` zu erreichen (besucht).
   - Gefangen! Sammelt `[0, 2, 1]`. `sccs = [[0, 2, 1]]`.
2. Pop `1`. Besucht. Überspringen.
3. Pop `2`. Besucht. Überspringen.
4. Pop `3`. Unbesucht. `dfs_pass2(3)` auf dem umgekehrten Graphen:
   - `3` versucht `1` zu erreichen. `1` ist bereits besucht!
   - Gefangen! Sammelt `[3]`. `sccs = [[0, 2, 1], [3]]`.

Ergebnis: `[[0, 2, 1], [3]]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(V + E)$ | $O(V + E)$ |
| **Durchschnittlicher Fall** | $O(V + E)$ | $O(V + E)$ |
| **Schlechtester Fall** | $O(V + E)$ | $O(V + E)$ |

Wir führen genau zwei DFS-Durchläufe ($O(V+E)$ jeweils) und eine Schleife zum Aufbau des transponierten Graphen ($O(V+E)$) durch. Die gesamte Zeitkomplexität ist strikt $O(V + E)$.
Die Platzkomplexität beträgt $O(V + E)$, da wir zwingend eine komplett neue Adjacency List erstellen müssen, um die umgekehrten Kanten im Speicher zu halten. (Dies macht ihn speicherintensiver als den Tarjan-Algorithmus, der nur $O(V)$ Platz für Arrays benötigt).

## Varianten & Optimierungen

- **Kondensationsgraph:** Sobald du die SCCs mit Kosaraju gefunden hast, kannst du einen neuen "Kondensationsgraphen" erstellen, in dem jede gesamte SCC als ein einzelner massiver Knoten behandelt wird. Der resultierende Graph ist garantiert ein gerichteter azyklischer Graph (DAG), was topologische Sortierung und einfache DP-Pfadfindungslogik ermöglicht!

## Anwendungen in der Praxis

- **Twitter / Soziale Netzwerke:** Auffinden isolierter Gemeinschaften oder Echokammern. Wenn eine Gruppe von 100 Nutzern sich gegenseitig folgt (was eine SCC bildet), aber niemand außerhalb der Gruppe ihnen folgt, identifiziert Kosaraju das Cluster sofort.

## Verwandte Algorithmen in cOde(n)

- **[graph_15 - Tarjan's SCC](graph_15_tarjan-s-scc.md)** — Der einstufige Algorithmus, der keinen Aufbau eines transponierten Graphen erfordert.
- **[graph_07 - Topological Sort](graph_07_topological-sort.md)** — Die Grundlage für Durchlauf 1 (Ablegen von Knoten auf einem Stack basierend auf der Fertigstellungszeit).

---

*Diese Dokumentation ist ein Originalinhalt für cOde(n), modelliert nach der kanonischen Struktur, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link oben auf der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*