# Kruskal-Algorithmus (Minimaler Spannbaum)

| | |
|---|---|
| **ID** | `graph_08` |
| **Kategorie** | Graphen |
| **Komplexität (erforderlich)** | $O(E log E)$ Zeit, $O(V)$ Platz |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 7/10 |
| **Wikipedia** | [Kruskal-Algorithmus](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm) |

## Problemstellung

Gegeben ist ein zusammenhängender, ungerichteter und gewichteter Graph. Finden Sie einen minimalen Spannbaum (Minimum Spanning Tree, MST) für diesen Graphen.
Ein minimaler Spannbaum ist eine Teilmenge der Kanten, die alle $V$ Knoten miteinander verbindet, keine Zyklen enthält und deren Gesamtkantengewicht minimal ist.

**Eingabe:** Anzahl der Knoten `V` und eine Kantenliste `edges`, wobei jede Kante als `[u, v, weight]` definiert ist.
**Ausgabe:** Eine Ganzzahl, die das minimale Gesamtgewicht des MST repräsentiert, und/oder die Liste der Kanten im MST.

## Wann man ihn verwendet

- Zur Lösung des klassischen Problems des minimalen Spannbaums.
- Wenn der Graph **dünn besetzt (sparse)** ist (E ist relativ klein im Vergleich zu V^2), ist der Kruskal-Algorithmus etwas schneller und wesentlich einfacher zu implementieren als der Prim-Algorithmus.

## Ansatz

**1. Die gierige Intuition:**
Wenn wir das *minimale* Gesamtgewicht erreichen wollen, sollten wir dann nicht einfach die absolut günstigsten Kanten im gesamten Graphen priorisieren?
Ja! Sortieren wir einfach das gesamte `edges`-Array vom niedrigsten zum höchsten Gewicht.

**2. Aufbau des Baums:**
Wir iterieren durch unsere sortierten Kanten, beginnend mit der absolut günstigsten existierenden Kante.
Wir möchten diese Kante zu unserem MST hinzufügen. Dabei müssen wir jedoch eine strikte Regel befolgen: **Der MST darf keine Zyklen enthalten!**
Wenn das Hinzufügen dieser Kante zwei Knoten verbindet, die bereits durch zuvor hinzugefügte Kanten verbunden sind, entsteht ein Zyklus! Wir müssen diese Kante verwerfen und die nächstgünstigere betrachten.

**3. Zykluserkennung (Disjoint Set / Union-Find):**
Wie prüfen wir effizient, ob zwei Knoten bereits durch unser wachsendes Netz an MST-Kanten "verbunden" sind?
Wir verwenden eine **Disjoint Set (Union-Find)** Datenstruktur!
- Anfangs befindet sich jeder Knoten in seiner eigenen isolierten Menge.
- Wenn wir eine Kante `[u, v, weight]` betrachten, prüfen wir `find(u) == find(v)`.
- Wenn sie gleich sind, befinden sie sich bereits in derselben Zusammenhangskomponente. Das Hinzufügen dieser Kante würde einen Zyklus erzeugen. Verwerfen!
- Wenn sie unterschiedlich sind, wird kein Zyklus erzeugt! Wir fügen die Kante unserem MST hinzu und führen ihre Komponenten mittels `union(u, v)` zusammen.

**4. Terminierung:**
Ein Spannbaum, der $V$ Knoten verbindet, enthält IMMER genau $V - 1$ Kanten. Sobald wir erfolgreich genau $V - 1$ Kanten mittels `union` hinzugefügt haben, können wir vorzeitig abbrechen! Der MST ist vollständig.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for graph_08: Kruskal's MST.

Greedy edge-by-edge union with DSU. Returns sorted MST edges or
[] if the graph is not connected.
"""


def solve(num_nodes, edges):
    parent = list(range(num_nodes))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[ra] = rb
        return True

    mst = []
    for u, v, w in sorted(edges, key=lambda e: e[2]):
        if union(u, v):
            mst.append((u, v, w))
    if len(mst) != num_nodes - 1:
        return []
    return sorted(mst)
```

</details>

## Durchlauf

`V = 4`. Kanten: `0-1 (10)`, `0-2 (6)`, `0-3 (5)`, `1-3 (15)`, `2-3 (4)`.

1. **Kanten sortieren:**
   `2-3 (4)`, `0-3 (5)`, `0-2 (6)`, `0-1 (10)`, `1-3 (15)`.
2. **Kante 2-3 (4):** `find(2)!=find(3)`. Vereinige sie.
   `mst_weight = 4`. Mengen: `{2, 3}`, `{0}`, `{1}`. `edges_added = 1`.
3. **Kante 0-3 (5):** `find(0)!=find(3)`. Vereinige sie.
   `mst_weight = 4+5 = 9`. Mengen: `{0, 2, 3}`, `{1}`. `edges_added = 2`.
4. **Kante 0-2 (6):** `find(0) == find(2)`! Sie sind bereits in derselben Menge! Würden wir diese hinzufügen, entstünde der Zyklus 0-2-3-0. Kante verwerfen!
5. **Kante 0-1 (10):** `find(0)!=find(1)`. Vereinige sie.
   `mst_weight = 9+10 = 19`. Mengen: `{0, 1, 2, 3}`. `edges_added = 3`.
6. `edges_added == 4 - 1 = 3`. Vorzeitiger Abbruch!

Ergebnis `mst_weight = 19`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(E log E)$ | $O(V + E)$ |
| **Durchschnittlicher Fall** | $O(E log E)$ | $O(V + E)$ |
| **Schlechtester Fall** | $O(E log E)$ | $O(V + E)$ |

Das Sortieren des Kanten-Arrays benötigt $O(E log E)$.
Das Iterieren durch die Kanten benötigt $O(E)$. Innerhalb der Schleife benötigen die Union-Find-Operationen aufgrund von Pfadkompression und Union-by-Rank praktisch $O(1)$ Zeit (genauer gesagt die inverse Ackermann-Funktion \alpha(V)).
Daher dominiert das Sortieren den Algorithmus massiv. Die Zeitkomplexität beträgt $O(E log E)$. (Da $E \le V^2$ gilt, ist dies mathematisch äquivalent zu $O(E log V)$).
Die Platzkomplexität beträgt $O(V)$ für die Parent- und Rank-Arrays des Union-Find, plus $O(E)$, falls ein neues Array zur Speicherung der MST-Kanten erstellt wird.

## Varianten & Optimierungen

- **Maximaler Spannbaum:** Sortieren Sie die Kanten in *absteigender* statt in aufsteigender Reihenfolge! Alles andere bleibt vollkommen identisch.
- **Prim-Algorithmus (`graph_10`):** Die Alternative zu Kruskal. Anstatt alle Kanten global zu sortieren, wählen Sie einen Startknoten und verwenden eine Priority Queue (genau wie bei Dijkstra), um einen einzelnen Baum langsam nach außen wachsen zu lassen, indem Sie jeweils die günstigste angrenzende Kante wählen. Prim ist bei sehr dichten Graphen ($E \approx V^2$), bei denen das Sortieren von $E$ zu langsam ist, deutlich überlegen.

## Anwendungen in der Praxis

- **Netzwerkdesign:** Verlegung der minimalen Gesamtlänge teurer Glasfaserkabel, um sicherzustellen, dass $V$ Rechenzentren alle mit demselben Netz verbunden sind.

## Verwandte Algorithmen in cOde(n)

- **[graph_09 - Union-Find](graph_09_union-find.md)** — Die zwingend erforderliche Datenstruktur, um Zyklen in Kruskals Algorithmus zu erkennen.
- **[graph_10 - Prim's MST](graph_10_prim-s-mst.md)** — Die Alternative mittels Priority Queue zur Lösung desselben MST-Problems.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*