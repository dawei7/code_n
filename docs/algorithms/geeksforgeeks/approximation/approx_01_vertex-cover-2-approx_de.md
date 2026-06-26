# Vertex-Cover (2-Approximation)

| | |
|---|---|
| **ID** | `approx_01` |
| **Kategorie** | approximation |
| **Komplexität (erforderlich)** | $O(V + E)$ |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **Wikipedia** | [Vertex cover](https://en.wikipedia.org/wiki/Vertex_cover) |

## Problemstellung

Eine **Knotenbedeckung** (Vertex Cover) eines ungerichteten Graphen ist eine Teilmenge seiner Knoten, sodass *jede Kante* im Graphen inzident zu (verbunden mit) mindestens einem Knoten in dieser Teilmenge ist.
Das Finden der absoluten *minimalen* Knotenbedeckung ist ein NP-vollständiges Problem. Man kann jedoch einen Approximationsalgorithmus schreiben, der garantiert eine Knotenbedeckung findet, die nicht größer als exakt das **Zweifache** der Größe der optimalen minimalen Knotenbedeckung ist.

**Eingabe:** Ein ungerichteter Graph, dargestellt als Adjacency List oder Edge List.
**Ausgabe:** Eine Liste von Knoten, die die approximierte Knotenbedeckung bilden.

## Wann man es verwendet

- Wenn Sie eine minimale Anzahl an Wachen/Kameras/Sensoren in einem Netzwerk von Fluren platzieren müssen, sodass jeder Flur überwacht wird.
- Um in fortgeschrittenen Algorithmen-Interviews ein Verständnis für Approximationsverhältnisse bei NP-schweren Problemen zu demonstrieren.

## Ansatz

Ein naiver Greedy-Ansatz bestünde darin, wiederholt den Knoten mit dem höchsten Grad (die meisten verbundenen Kanten) auszuwählen und ihn der Knotenbedeckung hinzuzufügen. Überraschenderweise garantiert dieser grad-basierte Greedy-Ansatz KEINE Approximation mit konstantem Faktor! Er kann eine Knotenbedeckung liefern, die $O(log V)$ mal größer als das Optimum ist.

**Die Kanten-Auswahl-Approximation ($O(V+E)$):**
Der einfachste und eleganteste 2-Approximationsalgorithmus wählt einfach zufällige Kanten aus, nicht Knoten!

1. Beginnen Sie mit einer leeren Menge `C` (unserer Knotenbedeckung).
2. Solange noch Kanten im Graphen vorhanden sind:
   - Wählen Sie eine beliebige Kante `(u, v)`.
   - Fügen Sie **beide** Endpunkte `u` und `v` zur Knotenbedeckung `C` hinzu.
   - Entfernen Sie `(u, v)` aus dem Graphen und entfernen Sie vollständig *alle anderen Kanten*, die an `u` oder `v` hängen.
3. Geben Sie `C` zurück.

**Warum ist es exakt eine 2-Approximation?**
Jedes Mal, wenn wir eine Kante `(u, v)` wählen, fügen wir *beide* Knoten unserer Knotenbedeckung hinzu.
Um diese spezifische Kante zu bedecken, *muss* die absolut optimale Lösung mindestens einen der Knoten `u` oder `v` wählen.
Indem wir beide wählen, zahlen wir höchstens einen Aufschlag vom Faktor 2 gegenüber der optimalen Wahl für diese spezifische Kante. Da wir sofort alle inzidenten Kanten löschen, zählen wir diesen Aufschlag niemals doppelt. Somit gilt für die Gesamtgröße unserer Knotenbedeckung \le 2 x OPT.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for approx_01: Vertex Cover (2-Approx).

Greedy: pick the max-degree vertex, drop its edges, repeat.
"""


def solve(n, edges):
    if n == 0:
        return set()
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    cover = set()
    edges_left = set()
    for u, v in edges:
        edges_left.add((min(u, v), max(u, v)))
    while edges_left:
        degrees = [0] * n
        for u, v in edges_left:
            degrees[u] += 1
            degrees[v] += 1
        v = max(range(n), key=lambda i: degrees[i])
        if degrees[v] == 0:
            break
        cover.add(v)
        edges_to_remove = [e for e in edges_left if v in e]
        for e in edges_to_remove:
            edges_left.discard(e)
    return sorted(cover)
```

</details>

## Durchlauf

Graph-Kanten: `[(1, 2), (2, 3), (3, 4), (4, 5)]` (Eine gerade Linie aus 5 Knoten).
*(Die optimale Knotenbedeckung hat die Größe 2: Knoten 2 und 4).*

1. Wähle eine beliebige Kante: Wir wählen `(2, 3)`.
   - Füge Knoten `2` und `3` zur `cover` hinzu. `cover = {2, 3}`.
   - Entferne `(2, 3)`.
   - Entferne Kanten, die `2` berühren: `(1, 2)`.
   - Entferne Kanten, die `3` berühren: `(3, 4)`.
   - Verbleibende Kanten: `[(4, 5)]`.
2. Wähle eine beliebige Kante: `(4, 5)`.
   - Füge Knoten `4` und `5` zur `cover` hinzu. `cover = {2, 3, 4, 5}`.
   - Entferne `(4, 5)`.
   - Verbleibende Kanten: Leer!

Die Schleife endet. Zurückgegebene Knotenbedeckung: `[2, 3, 4, 5]` (Größe 4).
Die optimale Größe war 2. Unsere Größe ist 4. 4 \le 2 x 2. Die 2-Approximationsschranke gilt! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(V + E)$ | $O(V + E)$ |
| **Durchschnittlicher Fall** | $O(V + E)$ | $O(V + E)$ |
| **Schlechtester Fall** | $O(V + E)$ | $O(V + E)$ |

Die Verwendung einer Adjacency List anstelle der Iteration über eine Menge von Kanten ermöglicht es uns, inzidente Kanten sofort zu finden. Die Verarbeitung jeder Kante und jedes Knotens benötigt konstante Zeit, was zu einer Zeitkomplexität von exakt $O(V + E)$ führt.
Die Platzkomplexität beträgt $O(V + E)$, um die Graphenstrukturen und die resultierende Knotenbedeckung zu speichern.

## Varianten & Optimierungen

- **Bipartite Graphen:** Für bipartite Graphen benötigen Sie keine Approximation! Nach dem Satz von König ist die Größe des maximalen Matchings exakt gleich der minimalen Knotenbedeckung. Sie können die exakte minimale Knotenbedeckung in Polynomialzeit mithilfe des Hopcroft-Karp-Algorithmus finden.

## Anwendungen in der Praxis

- **Cybersicherheit:** Identifizierung der minimalen Anzahl strategischer Netzwerk-Router, an denen Paket-Sniffer installiert werden müssen, sodass der Datenverkehr über jede physische Verbindung überwacht wird.
- **Biochemie:** Auswahl spezifischer struktureller Marker in Protein-Interaktionsnetzwerken, um evolutionäre Veränderungen zu verfolgen.

## Verwandte Algorithmen in cOde(n)

- **[approx_02 - Set Cover (Greedy)](approx_02_set-cover-greedy.md)** — Eine Verallgemeinerung des Knotenbedeckungsproblems.
- **[flow_03 - Bipartite Matching](../flow/flow_03_bipartite-matching.md)** — Die exakte Polynomialzeit-Lösung für die Knotenbedeckung, falls der Graph bipartit ist.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für Wettbewerbsprogrammierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*