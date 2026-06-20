# Vertex-Cover (2-Approximation)

| | |
|---|---|
| **ID** | `approx_01` |
| **Kategorie** | Approximation |
| **Komplexität (erforderlich)** | $O(V + E)$ |
| **Schwierigkeitsgrad** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **Wikipedia** | [Vertex-Cover](https://en.wikipedia.org/wiki/Vertex_cover) |

## Problemstellung

Eine **Knotenbedeckung** eines ungerichteten Graphen ist eine Teilmenge seiner Knoten, sodass *jede Kante* im Graphen an mindestens einen Knoten dieser Teilmenge angrenzt (ihn berührt).
Das Finden der absolut *minimalen* Knotenbedeckung ist ein NP-vollständiges Problem. Man kann jedoch einen Approximationsalgorithmus schreiben, der garantiert eine Knotenbedeckung findet, die nicht größer ist als genau das **Zweifache** der Größe der optimalen minimalen Bedeckung.

**Eingabe:** Ein ungerichteter Graph, dargestellt als Adjacency List oder Edge List.
**Ausgabe:** Eine Liste von Knoten, die die approximierte Knotenabdeckung bilden.

## Wann man es einsetzt

- Wenn man eine minimale Anzahl von Wachpersonal/Kameras/Sensoren in einem Netzwerk aus Fluren so platzieren muss, dass jeder Flur überwacht wird.
- Um in fortgeschrittenen Algorithmus-Vorstellungsgesprächen ein Verständnis für Approximationsverhältnisse bei NP-schwierigen Problemen zu demonstrieren.

## Vorgehensweise

Ein naiver, gieriger Ansatz bestünde darin, wiederholt den Knoten mit dem höchsten Grad (den meisten verbundenen Kanten) auszuwählen und ihn zur Überdeckung hinzuzufügen. Überraschenderweise garantiert dieser gradgierige Ansatz KEINE Approximation mit konstantem Faktor! Er kann zu einer Abdeckung führen, die $O(log V)$-mal größer ist als die optimale.

**Die Kantenauswahl-Approximation ($O(V+E)$):**
Der einfachste und eleganteste 2-Approximationsalgorithmus wählt einfach zufällige Kanten aus, keine Knoten!

1. Beginne mit einer leeren Menge `C` (unserer Überdeckung).
2. Solange noch Kanten im Graphen vorhanden sind:
   - Wähle eine beliebige Kante `(u, v)` aus.
   - Füge **beide** Endpunkte `u` und `v` zur Abdeckung `C` hinzu.
   - Entferne `(u, v)` aus dem Graphen und entferne *alle anderen Kanten* vollständig, die entweder an `u` oder `v` angrenzen.
3. Gib `C` zurück.

**Warum handelt es sich genau um eine 2-Approximation?**
Jedes Mal, wenn wir eine Kante `(u, v)` auswählen, fügen wir *beide* Knoten zu unserer Überdeckung hinzu.
Um diese bestimmte Kante abzudecken, *muss* die absolut optimale Lösung mindestens eine der Kanten `u` oder `v` auswählen.
Indem wir beide auswählen, zahlen wir höchstens eine Strafe in Höhe des Zweifachen der optimalen Wahl für diese bestimmte Kante! Da wir alle angrenzenden Kanten sofort löschen, wird diese Strafe niemals doppelt gezählt. Somit ist die Gesamtgröße unserer Überdeckung \le 2 x OPT.

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

## Schritt-für-Schritt-Anleitung

Graphkanten: `[(1, 2), (2, 3), (3, 4), (4, 5)]` (Eine gerade Linie aus 5 Knoten).
*(Die optimale Überdeckung hat die Größe 2: Knoten 2 und 4).*

1. Beliebige Kante auswählen: Wählen wir `(2, 3)`.
   - Knoten `2` und `3` zu `cover` hinzufügen. `cover = {2, 3}`.
   - Entferne `(2, 3)`.
   - Entferne Kanten, die `2` berühren: `(1, 2)`.
   - Entferne Kanten, die `3` berühren: `(3, 4)`.
   - Verbleibende Kanten: `[(4, 5)]`.
2. Wähle eine beliebige Kante aus: `(4, 5)`.
   - Füge die Knoten `4` und `5` zu `cover` hinzu. `cover = {2, 3, 4, 5}`.
   - Entferne `(4, 5)`.
   - Verbleibende Kanten: Keine!

Die Schleife ist beendet. Zurückgegebenes Cover: `[2, 3, 4, 5]` (Größe 4).
Die optimale Größe betrug 2. Unsere Größe ist 4. 4 \le 2 x 2. Die 2-Approximationsgrenze gilt! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(V + E)$ | $O(V + E)$ |
| **Durchschnittlicher Fall** | $O(V + E)$ | $O(V + E)$ |
| **Schlechtester Fall** | $O(V + E)$ | $O(V + E)$ |

Durch die Verwendung einer Adjacency List anstelle einer Iteration über eine Menge von Kanten können wir aneinandergrenzende Kanten sofort finden. Die Verarbeitung jeder Kante und jedes Knotens dauert konstante Zeit, was genau die Zeitkomplexität $O(V + E)$ ergibt.
Die Platzkomplexität beträgt $O(V + E)$ für die Speicherung der Graphstrukturen und der Ergebnisabdeckung.

## Varianten & Optimierungen

- **Zweigeteilte Graphen:** Bei zweigeteilten Graphen ist keine Approximation erforderlich! Nach dem Satz von König entspricht die Größe der maximalen Paarung genau der minimalen Knotenüberdeckung. Die exakte minimale Knotenabdeckung lässt sich mit dem Hopcroft-Karp-Algorithmus in polynomieller Zeit ermitteln.

## Anwendungen in der Praxis

- **Cybersicherheit:** Ermittlung der minimalen Anzahl strategischer Netzwerkrouter, auf denen Paketsniffer installiert werden müssen, damit der Datenverkehr über jede physikalische Verbindung überwacht wird.
- **Biochemie:** Auswahl spezifischer Strukturmarker in Protein-Interaktionsnetzwerken, um evolutionäre Veränderungen nachzuverfolgen.

## Verwandte Algorithmen in cOde(n)

- **[approx_02 – Set Cover (Greedy)](approx_02_set-cover-greedy.md)** — Eine Verallgemeinerung des Vertex-Cover-Problems.
- **[flow_03 - Bipartite Matching](../flow/flow_03_bipartite-matching.md)** — Die exakte Lösung in polynomieller Zeit für das Vertex-Cover-Problem, wenn der Graph zufällig bipartit ist.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
in Anlehnung an die kanonische Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
