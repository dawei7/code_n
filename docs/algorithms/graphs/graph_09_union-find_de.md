# Union-Find (Disjoint Set Union, DSU)

| | |
|---|---|
| **ID** | `graph_09` |
| **Kategorie** | Graphen |
| **Komplexität (erforderlich)** | $O(n)$ |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **Wikipedia** | [Disjoint-set data structure](https://en.wikipedia.org/wiki/Disjoint-set_data_structure) |

## Problemstellung

Verwaltung einer Partition von `n` Elementen in disjunkte Mengen unter zwei Operationen:
- `find(x)` — gibt den **Repräsentanten** (Wurzel) der Menge zurück, die `x` enthält.
- `union(x, y)` — vereinigt die Mengen, die `x` und `y` enthalten.

Beide Operationen sollten effizient sein (nahe an $O(1)$ amortisiert).
Nützlich für: Konnektivitätsanfragen, Kruskals MST, Netzwerkkomponenten, Bildverarbeitung usw.

**Eingabe:** ein Strom von union- und find-Anfragen auf `n` Elementen.
**Ausgabe:** für jedes find, der Repräsentant der Menge von `x`; für jedes union, der neue Repräsentant der vereinigten Menge.

**Beispiel:**

Initial: Jedes Element befindet sich in seiner eigenen Menge.
```
union(0, 1)     -> {0, 1}, {2}, {3}, {4}
union(2, 3)     -> {0, 1}, {2, 3}, {4}
find(0)         -> 0   (oder 1, abhängig von der Implementierung)
find(2)         -> 2   (oder 3)
union(1, 3)     -> {0, 1, 2, 3}, {4}
find(0)         -> 0   (oder 1, 2, 3 — alles dieselbe Menge)
```

## Wann man es verwendet

- Wird in irgendeiner Form in fast jedem Vorstellungsgespräch abgefragt. Oft als Teil von Kruskals MST oder als Teilproblem zum "**Zählen von Zusammenhangskomponenten**".
- Grundlage für den **Kruskal-Algorithmus**, **Offline-Konnektivitätsanfragen** und das **Perkolationsproblem**.

## Ansatz

Zwei klassische Optimierungen:

**Pfadkompression** (in `find`): Nachdem die Wurzel von `x` gefunden wurde, setze `parent[x] = root`. Dies flacht den Baum ab.
**Union by rank/size**: Hänge immer den kleineren Baum unter die Wurzel des größeren.

Mit beiden Optimierungen beträgt die amortisierte Zeitkomplexität pro Operation **$O(α(n)$)** (inverse Ackermann-Funktion, < 5 für jedes praktische `n`).

**Pfadkompression** (rekursiv):
```
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])    # compress
    return parent[x]
```

**Union by rank:**
```
def union(x, y):
    rx, ry = find(x), find(y)
    if rx == ry: return
    if rank[rx] < rank[ry]:
        parent[rx] = ry
    elif rank[rx] > rank[ry]:
        parent[ry] = rx
    else:
        parent[ry] = rx
        rank[rx] += 1
```

**Union by size** (alternativ; gleiche Komplexität):
```
def union(x, y):
    rx, ry = find(x), find(y)
    if rx == ry: return
    if size[rx] < size[ry]:
        rx, ry = ry, rx
    parent[ry] = rx
    size[rx] += size[ry]
```

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for graph_09: Union-Find (DSU).

Path compression + union by rank. Process a list of union/find
ops and return the find results in order.
"""


def solve(n, ops):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1

    results = []
    for op in ops:
        if op[0] == "union":
            union(op[1], op[2])
        elif op[0] == "find":
            results.append(find(op[1]) == find(op[2]))
    return results
```

</details>

## Durchlauf

`n = 5`. Operationen: `union(0,1)`, `union(1,2)`, `find(0)`, `union(3,4)`, `union(2,4)`, `find(0)`, `find(3)`.

Initial: `parent = [0, 1, 2, 3, 4]`, `rank = [0, 0, 0, 0, 0]`.

| Op | Aktion | parent danach | rank danach |
|---|---|---|---|
| `union(0, 1)` | r=0, r=1, rank[0]==rank[1], parent[1]=0, rank[0]=1 | `[0, 0, 2, 3, 4]` | `[1, 0, 0, 0, 0]` |
| `union(1, 2)` | r=find(1)=0, r=2, rank[0]=1 > rank[2]=0, parent[2]=0 | `[0, 0, 0, 3, 4]` | gleich |
| `find(0)` | parent[0]=0, return 0 | unverändert | gleich |
| `union(3, 4)` | r=3, r=4, rank[3]==rank[4], parent[4]=3, rank[3]=1 | `[0, 0, 0, 3, 3]` | `[1, 0, 0, 1, 0]` |
| `union(2, 4)` | r=find(2)=0, r=find(4)=3, rank[0]==rank[3], parent[3]=0, rank[0]=2 | `[0, 0, 0, 0, 3]` | `[2, 0, 0, 1, 0]` |
| `find(0)` | return 0 | unverändert | gleich |
| `find(3)` | parent[3]=0, return 0 (mit Pfadkompression) | unverändert | gleich |

Alle Elemente {0, 1, 2, 3, 4} befinden sich nun in einer Menge mit Wurzel 0. ✓

## Komplexität

| | Zeit (amortisiert) | Platz |
|---|---|---|
| **Bestfall** | $O(α(n)$) pro Op | $O(n)$ |
| **Durchschnittlicher Fall** | $O(α(n)$) pro Op | $O(n)$ |
| **Schlechtester Fall** | $O(α(n)$) pro Op | $O(n)$ |

`α(n)` ist die inverse Ackermann-Funktion — für alle praktischen `n` (n < 10^600) gilt `α(n) ≤ 5`. Daher ist DSU "effektiv $O(1)$ pro Operation".

Ohne die Optimierungen: $O(n)$ pro `find` im schlechtesten Fall (entarteter Baum).

## Varianten & Optimierungen

- **Union by size** — Alternative zu rank; etwas einfacher, gleiche Komplexität.
- **Gewichtete Union** — Wenn die Elemente Gewichte haben, ist das "kleinere" das mit dem geringeren Gewicht. Wird in Kruskals Algorithmus verwendet, um das "Gesamtgewicht der Kanten zu minimieren".
- **Persistente DSU** — Versionierte Historie von Unions; verwendet einen persistenten Segment Tree. $O(log n)$ pro Op.
- **DSU mit Rollback** — Rückgängigmachen der letzten Union-Operation. $O(log n)$ pro Op mit dem Half-Edge-Trick.
- **DSU auf Bäumen** (small-to-large) — effiziente Teilbaum-Anfragen auf Bäumen. $O(n log n)$ Vorverarbeitung, $O(1)$ Anfrage.

## Anwendungen in der Praxis

- **Kruskals MST** — Kanten nach Gewicht sortieren, zum MST hinzufügen, wenn ihre Endpunkte in verschiedenen DSU-Mengen liegen.
- **Netzwerkkonnektivität** — "Ist Computer A im selben Subnetz wie Computer B?" → DSU-Anfrage.
- **Bildverarbeitung** — Labeling von Zusammenhangskomponenten (Flood Fill ist im Wesentlichen DSU auf einem Gitter).
- **Perkolationstheorie** — Erreicht Wasser den Boden eines zufälligen porösen Mediums von oben? Modelliert als DSU.
- **Least Common Ancestor** (offline) — Tarjans Algorithmus verwendet DSU.
- **Soziale Netzwerke "Freund von Freund"** — Freundschaftsgruppen zusammenführen, Anfrage "Sind X und Y in derselben Gruppe?".

## Verwandte Algorithmen in cOde(n)

- **[graph_08 — Kruskal's MST](graph_08_kruskals-mst.md)** — Die berühmteste Anwendung von DSU. (d=6/10, r=8/10)
- **[graph_10 — Prim's MST](graph_10_prims-mst.md)** — Der alternative MST-Algorithmus (ohne DSU). (d=6/10, r=8/10)
- **[graph_11 — Cycle Detection](graph_11_cycle-detection.md)** — DSU erkennt Zyklen in $O(V + E)$. (d=4/10, r=8/10)
- **[graph_12 — Bipartite Check](graph_12_bipartite-check.md)** — Kann ebenfalls mit DSU durchgeführt werden (alternative Färbung). (d=4/10, r=8/10)

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) erstellt wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*