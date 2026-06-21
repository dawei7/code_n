# Tiefensuche (Depth-First Search, DFS)

| | |
|---|---|
| **ID** | `graph_03` |
| **Kategorie** | Graphen |
| **Komplexität (erforderlich)** | $O(n²)$ |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **Wikipedia** | [Depth-first search](https://en.wikipedia.org/wiki/Depth-first_search) |

## Problemstellung

Gegeben sei ein Graph `G = (V, E)` und ein Startknoten `s`. Durchlaufe den Graphen, indem du **so tief wie möglich** gehst, bevor du zum vorherigen Knoten zurückkehrst (Backtracking). Ausgabe: die DFS-Reihenfolge, die Entdeckungs- und Abschlusszeiten (in einem gerichteten Graphen), der Vorgänger (Parent) jedes Knotens sowie die von `s` aus erreichbaren Zusammenhangskomponenten.

**Eingabe:** ein Graph (Adjazenzliste oder Adjazenzmatrix), ein Startknoten `s`.
**Ausgabe:** DFS-Reihenfolge, Parent-Array, Zusammenhangskomponenten.

**Beispiel:**

```
    0 - 1 - 3
    |   |   |
    2 - 4   5
    |
    6

Adjazenz:
  0: [1, 2]
  1: [0, 3, 4]
  2: [0, 4, 6]
  3: [1, 5]
  4: [1, 2]
  5: [3]
  6: [2]

DFS ab 0:
  Reihenfolge (Entdeckungszeiten):  0(0), 1(1), 3(2), 5(3),
                            [Backtrack 5, 3] 4(4), [b 4] 2(5), 6(6)
  Parents: 0:None, 1:0, 3:1, 5:3, 4:1, 2:0, 6:2
```

## Wann man sie verwendet

- Die andere grundlegende Graphensuche. Wird in irgendeiner Form in fast jedem Vorstellungsgespräch abgefragt; oft gepaart mit BFS.
- Grundlage für **topologische Sortierung**, **Zyklenerkennung**, **stark zusammenhängende Komponenten**, **Bipartit-Test**, **Artikulationspunkte & Brücken**, **Labyrinth-Lösung** und Anfragen zur **Pfadexistenz**.

## Ansatz

DFS verwendet einen **LIFO-Stack** (oder Rekursion, welche den Call-Stack nutzt). Die Invariante: Wenn ein Knoten "abgeschlossen" ist, wurden alle seine Nachfahren vollständig erkundet.

Zwei äquivalente Formulierungen:

**Rekursiv** (sauberer, kann bei sehr tiefen Graphen zu einem Stack-Overflow führen):
```
dfs(u):
    mark u as visited
    time += 1; disc[u] = time
    for v in G[u]:
        if v not visited:
            parent[v] = u
            dfs(v)
    time += 1; finish[u] = time
```

**Iterativ** (expliziter Stack, kein Rekursionslimit):
```
push (s, 0)  # (vertex, neighbor-index)
while stack:
    u, i = stack[-1]
    if i < len(G[u]):
        v = G[u][i]
        stack[-1] = (u, i + 1)
        if v not visited:
            mark v as visited
            parent[v] = u
            push (v, 0)
    else:
        stack.pop()
        finish u
```

**Performance:** $O(V + E)$ bei Adjazenzliste, $O(V²)$ bei Matrix. Identisch zu BFS, aber DFS verbraucht in der Praxis deutlich weniger Speicher (der Stack ist durch die Tiefe begrenzt, während die Queue die gesamte Front halten kann).

**Warum DFS statt BFS verwenden:** DFS ist besser geeignet für:
- Topologische Sortierung (wir benötigen Abschlusszeiten).
- Zyklenerkennung (Rückwärtskanten).
- Baumstruktur-Probleme (Pfadsummen, etc.).
- Speichereffizienz, wenn der Graph "hoch" ist (ein langer Pfad vor der nächsten Verzweigung).

## Algorithmus (Pseudocode, rekursiv)

```
dfs(G, s):
    visited = set()
    parent = {}
    order = []
    def go(u):
        visited.add(u)
        order.append(u)
        for v in G[u]:
            if v not in visited:
                parent[v] = u
                go(v)
    go(s)
    return order, parent
```

Für **alle Zusammenhangskomponenten**, umschließe dies mit:
```
for v in G:
    if v not in visited:
        go(v)
```

## Ablauf

Graph aus dem Beispiel. DFS ab `s = 0`.

`go(0)`: besuche 0. Nachbarn: 1 (unbesucht), 2 (unbesucht).
Wähle 1.
- `go(1)`: besuche 1. Nachbarn: 0 (besucht), 3 (unbesucht), 4 (unbesucht).
  Wähle 3.
  - `go(3)`: besuche 3. Nachbarn: 1 (besucht), 5 (unbesucht). Wähle 5.
    - `go(5)`: besuche 5. Nachbarn: 3 (besucht). Backtrack.
  - Zurück bei 3, keine unbesuchten Nachbarn mehr. Backtrack.
- Zurück bei 1, nächster Unbesuchter: 4.
  - `go(4)`: besuche 4. Nachbarn: 1 (besucht), 2 (unbesucht). Wähle 2.
    - `go(2)`: besuche 2. Nachbarn: 0 (besucht), 4 (besucht), 6 (unbesucht). Wähle 6.
      - `go(6)`: besuche 6. Nachbarn: 2 (besucht). Backtrack.
    - Zurück bei 2, keine Unbesuchten mehr. Backtrack.
  - Zurück bei 4, keine Unbesuchten mehr. Backtrack.
- Zurück bei 1, keine Unbesuchten mehr. Backtrack.
- Zurück bei 0, nächster Unbesuchter: 2 (bereits besucht). Fertig.

DFS-Reihenfolge: `[0, 1, 3, 5, 4, 2, 6]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(V + E)$ | $O(V)$ |
| **Durchschnittlicher Fall** | $O(V + E)$ | $O(V)$ |
| **Schlechtester Fall** | $O(V + E)$ | $O(V)$ |

Rekursive DFS benötigt $O(Tiefe)$ Stack-Platz; iterative DFS benötigt ebenfalls $O(Tiefe)$ Platz für den expliziten Stack. Das "$O(V)$" bezieht sich auf das `visited`-Set und das `parent`-Array; der tatsächliche Stack kann in der Praxis deutlich kleiner sein (Schlechtester Fall: V).

Die erforderliche Komplexität ist $O(n²)$ für die Matrix-Variante von cOde(n).

## Varianten & Optimierungen

- **Topologische Sortierung** — DFS auf einem DAG, Ausgabe der Knoten in umgekehrter Abschlussreihenfolge. $O(V + E)$.
- **Zyklenerkennung** — in ungerichteten Graphen: jede Rückwärtskante ist ein Zyklus. In gerichteten Graphen: eine Rückwärtskante zu einem Vorfahren (unter Verwendung der Grau/Schwarz-Färbung) ist ein Zyklus.
- **Stark zusammenhängende Komponenten** — Tarjan- oder Kosaraju-Algorithmus, beide basieren auf DFS. $O(V + E)$. Siehe `graph_15` und `graph_16`.
- **Bipartit-Test** — 2-Färbung der Ebenen; wenn eine Rückwärtskante gleichfarbige Knoten verbindet, ist der Graph nicht bipartit.
- **Artikulationspunkte / Brücken** — DFS-Baum + Low-Link-Werte. Siehe `graph_13`, `graph_14`.
- **Iterative Deepening DFS (IDDFS)** — DFS mit Tiefenlimit, das in jeder Iteration erhöht wird. Kombiniert die Speichereffizienz von DFS mit der Vollständigkeit von BFS.

## Anwendungen in der Praxis

- **Labyrinth-Lösung** — DFS findet irgendeinen Pfad; BFS findet den kürzesten.
- **Topologische Planung** — Aufgabenreihenfolge bei Abhängigkeiten.
- **Stark zusammenhängende Komponenten** — Analyse von sozialen Netzwerken, Web-Graphen.
- **Zyklenerkennung in Abhängigkeitsgraphen** — Paketmanager (npm, pip) nutzen dies, um zirkuläre Abhängigkeiten zu finden.
- **Garbage Collection** — einige GCs verwenden DFS anstelle von BFS.
- **SCC-basierter 2-SAT-Solver** — Erfüllbarkeitsproblem für 2-CNF-Formeln.
- **Tarjans Brückensuche** — Analyse von Single-Points-of-Failure in Netzwerken.

## Verwandte Algorithmen in cOde(n)

- **[graph_02 — BFS](graph_02_bfs.md)** — die andere grundlegende Suche. (d=4/10, r=8/10)
- **[graph_07 — Topologische Sortierung](graph_07_topological-sort.md)** — DFS auf einem DAG. (d=5/10, r=8/10)
- **[graph_11 — Zyklenerkennung](graph_11_cycle-detection.md)** — DFS mit Erkennung von Rückwärtskanten. (d=4/10, r=8/10)
- **[graph_15 — Tarjans SCC](graph_15_tarjans-scc.md)** — DFS mit Low-Link-Werten. (d=6/10, r=8/10)

---

*Diese Dokumentation ist ein Originalinhalt für cOde(n), modelliert nach der kanonischen Struktur, die von Wettbewerbs-Programmierseiten verwendet wird. Für den enzyklopädischen Standardeintrag folge dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*