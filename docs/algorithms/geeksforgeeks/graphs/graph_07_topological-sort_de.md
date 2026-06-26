# Topologische Sortierung

| | |
|---|---|
| **ID** | `graph_07` |
| **Kategorie** | Graphen |
| **Komplexität (erforderlich)** | $O(n²)$ |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **Wikipedia** | [Topological sorting](https://en.wikipedia.org/wiki/Topological_sorting) |

## Problemstellung

Gegeben sei ein **gerichteter azyklischer Graph (DAG)** `G = (V, E)`. Finde eine lineare Anordnung der Knoten `V`, sodass für jede Kante `(u, v)` der Knoten `u` in der Anordnung vor `v` erscheint. Dies nennt man eine **topologische Sortierung** (oder "topo sort").

**Eingabe:** Ein gerichteter azyklischer Graph.
**Ausgabe:** Eine Anordnung der Knoten, sodass alle Kanten in der Anordnung "vorwärts" verlaufen.

**Beispiel:**

```
Build dependencies (directed):
  compiler → linker → binary
  compiler → ast → ir
  ast    → linker (after type check)

Edges: compiler→linker, compiler→ast, ast→ir, ast→linker, linker→binary

Topo sorts: [compiler, ast, linker, ir, binary]
            or [compiler, ast, ir, linker, binary]
            (many valid orderings)
```

## Anwendungsbereiche

- Immer dann gefragt, wenn das Problem lautet: "Führe Aufgabe A vor B aus" unter Berücksichtigung von Abhängigkeiten. Das klassische Scheduling-Problem.
- Grundlage für **Build-Systeme** (Make, Bazel, npm), **Task-Scheduler**, **Deadlock-Erkennung** und die **Neuberechnungsreihenfolge in Tabellenkalkulationen**.

## Ansatz

Es gibt zwei äquivalente Ansätze.

### Ansatz A: Kahn-Algorithmus (BFS-basiert)

Entferne wiederholt Knoten mit einem **Eingangsgrad (in-degree) von 0**. Während wir diese entfernen, dekrementieren wir den Eingangsgrad ihrer Nachbarn; jeder Knoten, dessen Eingangsgrad 0 erreicht, wird der nächsten Gruppe hinzugefügt.

```
topo_sort_kahn(G):
    in_deg = [0] * n
    for (u, v) in G.edges: in_deg[v] += 1
    queue = [v for v in V if in_deg[v] == 0]
    order = []
    while queue:
        u = queue.pop()
        order.append(u)
        for v in G[u]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                queue.append(v)
    if len(order) != n: raise "cycle detected"
    return order
```

**Vorteile:** Erkennt Zyklen auf natürliche Weise. **Nachteile:** Erfordert ein zusätzliches Array für die Eingangsgrade.

### Ansatz B: DFS-basiert

Führe eine DFS durch; gib jeden Knoten in **umgekehrter Fertigstellungsreihenfolge** aus.

```
topo_sort_dfs(G):
    visited = set()
    order = []
    def go(u):
        visited.add(u)
        for v in G[u]:
            if v not in visited:
                go(v)
        order.append(u)            # post-order
    for v in V:
        if v not in visited: go(v)
    return reversed(order)
```

**Vorteile:** Minimaler Speicherbedarf. **Nachteile:** Erkennt ebenfalls Zyklen (eine Rückwärtskante bedeutet, dass keine gültige topologische Sortierung existiert).

## Algorithmus (Pseudocode, Kahn)

```
topo_sort(G):
    n = len(G)
    in_deg = [0] * n
    for u in range(n):
        for v in G[u]:
            in_deg[v] += 1
    queue = deque()
    for v in range(n):
        if in_deg[v] == 0:
            queue.append(v)
    order = []
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in G[u]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                queue.append(v)
    if len(order) != n:
        raise ValueError("graph has a cycle")
    return order
```

## Durchlauf

Graph (4 Knoten, Kanten: 0→1, 0→2, 1→3, 2→3).

Adjazenz: `0: [1, 2], 1: [3], 2: [3], 3: []`.

Initial: `in_deg = [0, 1, 1, 2]`. Queue: `[0]`.

| Iter | dequeue | update | queue nachher | order |
|---:|---|---|---|---|
| 1 | 0 | in_deg[1]=0, in_deg[2]=0, enqueue beide | [1, 2] | [0] |
| 2 | 1 | in_deg[3]=1 | [2] | [0, 1] |
| 3 | 2 | in_deg[3]=0, enqueue | [3] | [0, 1, 2] |
| 4 | 3 | (keine Nachbarn) | [] | [0, 1, 2, 3] |

Topologische Sortierung: `[0, 1, 2, 3]`. ✓ (Alle Kanten verlaufen vorwärts: 0→1 ✓, 0→2 ✓, 1→3 ✓, 2→3 ✓.)

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(V + E)$ | $O(V)$ |
| **Durchschnittlicher Fall** | $O(V + E)$ | $O(V)$ |
| **Schlechtester Fall** | $O(V + E)$ | $O(V)$ |

Für Adjazenzmatrix-Repräsentationen beträgt die erforderliche Komplexität $O(V²)$.

## Varianten & Optimierungen

- **Lexikographisch kleinste topologische Sortierung** — wenn mehrere Knoten mit Eingangsgrad 0 verfügbar sind, wähle den kleinsten zuerst. Verwende einen Min-Heap anstelle einer FIFO-Queue.
- **Alle topologischen Sortierungen** — Backtracking: Wähle einen Knoten mit Eingangsgrad 0, rekursiere, mache die Wahl rückgängig. Exponentiell im schlechtesten Fall (in der Praxis selten).
- **Parallele topologische Sortierung** — viele unabhängige Knoten mit Eingangsgrad 0 können parallel verarbeitet werden.
- **Topologische Sortierung mit Voraussetzungen** — gegeben als Bedingungen (a, b), was "a vor b" bedeutet; baue die Adjazenz auf und führe den Algorithmus aus.
- **Topologische Sortierung bei Zyklen** — erkenne den Zyklus (z. B. die verbleibenden Knoten mit Eingangsgrad ungleich 0) und melde ihn.

## Anwendungen in der Praxis

- **Build-Systeme** — Make, CMake, Bazel, npm, cargo verwenden alle die topologische Sortierung, um die Build-Reihenfolge zu bestimmen.
- **Task-Scheduling** — "führe A vor B aus" mit Abhängigkeiten.
- **Planung von Kursvoraussetzungen** — "belege recursion_01 vor dp_01".
- **Neuberechnung in Tabellenkalkulationen** — welche Zellen hängen von welchen anderen ab.
- **Linker** — Auflösung von Symbolen in Objektdateien.
- **Deadlock-Erkennung** — finde einen Zyklus im Ressourcen-Wartegraphen.
- **Instruction Scheduling** — der Compiler ordnet Befehle unter Berücksichtigung von Datenabhängigkeiten neu an.

## Verwandte Algorithmen in cOde(n)

- **[graph_03 — DFS](graph_03_dfs.md)** — die DFS-basierte topologische Sortierung nutzt dies. (d=4/10, r=8/10)
- **[graph_02 — BFS](graph_02_bfs.md)** — Kahns Algorithmus verwendet die schichtweise Verarbeitung im BFS-Stil. (d=4/10, r=8/10)
- **[graph_11 — Zykluserkennung](graph_11_cycle-detection.md)** — die topologische Sortierung schlägt bei zyklischen Graphen fehl; die Zykluserkennung geht der topologischen Sortierung voraus. (d=4/10, r=8/10)
- **[graph_15 — Tarjans SCC](graph_15_tarjans-scc.md)** — bei einem allgemeinen gerichteten Graphen findet man zuerst die SCCs und führt dann eine topologische Sortierung auf der Kondensation (DAG der SCCs) durch. (d=6/10, r=8/10)

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) erstellt wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den enzyklopädischen Standardeintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*