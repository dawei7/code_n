# Karger's Min-Cut (Monte Carlo)

| | |
|---|---|
| **ID** | `randomized_05` |
| **Kategorie** | randomized |
| **Komplexität (erforderlich)** | $O(V^2 E)$ Erwartungswert |
| **Schwierigkeit** | 7/10 |
| **Relevanz für Vorstellungsgespräche** | 3/10 |
| **Wikipedia** | [Karger-Algorithmus](https://en.wikipedia.org/wiki/Karger%27s_algorithm) |

## Problemstellung

Gegeben ist ein zusammenhängender, ungerichteter Graph mit $V$ Knoten und $E$ Kanten. Gesucht ist der **globale minimale Schnitt** (Global Minimum Cut).
Ein Schnitt ist eine Partitionierung der Knoten in zwei disjunkte Mengen. Die Größe des Schnitts entspricht der Anzahl der Kanten, die diese Partitionierung kreuzen.
Der minimale Schnitt ist derjenige Schnitt, bei dem die absolut minimale Anzahl an Kanten entfernt werden muss, um den Graphen in zwei separate Zusammenhangskomponenten zu zerlegen.

**Eingabe:** Eine Adjazenzliste, die den Graphen repräsentiert.
**Ausgabe:** Eine Ganzzahl, die die minimale Anzahl der Kanten im Schnitt repräsentiert.

## Anwendung

- Zur Partitionierung von Clustern in der Netzwerktopologie.
- Er ist das definierende Beispiel für einen **Monte-Carlo-Algorithmus**. Im Gegensatz zu Las-Vegas-Algorithmen (die korrekte Antworten garantieren, aber zufällige Laufzeiten haben, wie z. B. Quicksort), haben Monte-Carlo-Algorithmen streng begrenzte Laufzeiten, besitzen jedoch eine gewisse Wahrscheinlichkeit, ein *falsches* Ergebnis zu liefern! Man führt sie mehrfach aus, um die Wahrscheinlichkeit der Korrektheit auf nahezu 100 % zu erhöhen.

## Ansatz

**Die Kernidee (Kantenkontraktion):**
1. Wähle eine völlig zufällige Kante aus dem Graphen aus.
2. "Kontrahiere" diese Kante. Das bedeutet, die beiden durch die Kante verbundenen Knoten werden zu einem einzigen "Super-Knoten" verschmolzen.
3. Alle Kanten, die mit den ursprünglichen zwei Knoten verbunden waren, führen nun zum Super-Knoten.
4. Entferne alle Selbstschleifen (Kanten, die nun den Super-Knoten mit sich selbst verbinden).
5. Wiederhole diesen Prozess, bis genau 2 Super-Knoten übrig bleiben!
6. Die Anzahl der Kanten, die diese beiden finalen Super-Knoten verbinden, ist ein *Kandidat* für den minimalen Schnitt.

**Warum funktioniert das?**
Sei $C$ die Menge der Kanten des tatsächlichen minimalen Schnitts.
Wenn wir Kanten zufällig kontrahieren, solange wir *niemals* eine Kante aus $C$ auswählen, werden die Kanten in $C$ bis zum Ende überleben, und wir finden den perfekten minimalen Schnitt!
Da $C$ per Definition der absolut kleinste Engpass im Graphen ist, ist es statistisch *sehr unwahrscheinlich*, dass bei der Auswahl einer völlig zufälligen Kante in den frühen Phasen $C$ getroffen wird!

**Verstärkung (Amplification):**
Ein einzelner Durchlauf des Karger-Algorithmus hat nur eine Wahrscheinlichkeit von $\ge \frac{2}{V(V-1)}$, den korrekten minimalen Schnitt zu finden. Das ist sehr gering!
Wenn wir den Algorithmus jedoch $V^2 \log V$ Mal ausführen und das Minimum aller Ergebnisse wählen, sinkt die Wahrscheinlichkeit, *jedes Mal* zu scheitern, auf $\le \frac{1}{V}$, was die Korrektheit praktisch garantiert!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for randomized_05: Karger's Min-Cut (Monte Carlo).

Given an undirected unweighted graph (with
"""


def solve(edges, n, trials):
    """Karger's min-cut algorithm with multiple trials.

    Each trial: randomly contract edges until 2 vertices
    remain. The number of remaining edges is the cut size
    for that trial. Return the minimum cut across all
    trials.
    """
    import random
    if n <= 1:
        return 0
    if n == 2:
        return len(edges)
    best = float("inf")
    for _ in range(max(1, trials)):
        # Union-Find: each vertex has a parent representative.
        parent = list(range(n))
        rank = [0] * n
        def find(x):
            r = x
            while parent[r] != r:
                r = parent[r]
            # Path compression.
            while parent[x] != r:
                parent[x], x = r, parent[x]
            return r
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1
        # Run one trial: shuffle edges and contract until
        # 2 components remain. The contracted multigraph
        # has parallel edges; we model it by keeping all
        # edges and counting "alive" ones.
        live_edges = list(edges)
        random.shuffle(live_edges)
        # Number of components = number of distinct roots.
        num_components = n
        for u, v in live_edges:
            if num_components <= 2:
                break
            ru, rv = find(u), find(v)
            if ru == rv:
                # Self-loop in the contracted graph; ignore.
                continue
            union(ru, rv)
            num_components -= 1
        # Count cut edges: edges (u, v) with find(u) != find(v).
        cut = 0
        for u, v in edges:
            if find(u) != find(v):
                cut += 1
        if cut < best:
            best = cut
    return best
```

</details>

## Beispiel-Durchlauf

Der Graph ist ein Quadrat: `A-B, B-C, C-D, D-A`.
Der wahre minimale Schnitt ist 2 (z. B. `A-B` und `C-D` schneiden, um `A,D` von `B,C` zu trennen).

**Durchlauf 1:**
- Wähle Kante `B-C`. Kontrahiere `C` in `B`. Der Graph ist nun ein Dreieck: `A-B, B-D` (dies ist die alte Kante `C-D`) und `D-A`.
- Wähle Kante `A-B`. Kontrahiere `B` in `A`.
- Nur `A` und `D` bleiben übrig.
- Kanten zwischen `A` und `D`: Die ursprüngliche Kante `A-D` und die Kante `B-D` (die ursprünglich `C-D` war).
- Schnittgröße = 2. Der optimale Schnitt wurde gefunden!

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(V^2 E)$ Erwartungswert | $O(V + E)$ |
| **Durchschnittlicher Fall** | $O(V^2 E)$ Erwartungswert | $O(V + E)$ |
| **Schlechtester Fall** | $O(V^2 E)$ Erwartungswert | $O(V + E)$ |

Eine einzelne Kontraktion benötigt $O(E)$ Zeit. Den gesamten Graphen auf 2 Knoten zu kontrahieren, benötigt $O(V \cdot E)$. Wir wiederholen dies $V^2$ Mal zur Verstärkung. Die Gesamtlaufzeit beträgt $O(V^3 E)$.
Die Platzkomplexität beträgt $O(V + E)$, um den Multigraphen während der Kontraktion im Speicher zu halten.

## Varianten & Optimierungen

- **Karger-Stein-Algorithmus ($O(V^2 \log^3 V)$):** Karger bemerkte, dass die Wahrscheinlichkeit, versehentlich eine Kante des minimalen Schnitts auszuwählen, zu Beginn extrem niedrig ist, aber gegen Ende, wenn nur noch wenige Knoten übrig sind, gefährlich hoch wird. Karger-Stein führt die Kontraktion bis auf $V / \sqrt{2}$ Knoten durch und verzweigt dann in *zwei* separate rekursive Kopien. Dies reduziert die notwendigen Verstärkungsiterationen drastisch und senkt die Zeitkomplexität erheblich!
- **Stoer-Wagner-Algorithmus:** Die deterministische $O(V E + V^2 \log V)$ Alternative, die ohne Randomisierung auskommt.

## Anwendungen in der Praxis

- **Bildsegmentierung:** Wird in der Computer Vision verwendet, um ein Bild in Vorder- und Hintergrund zu unterteilen, indem der minimale Schnitt in einem Pixel-Ähnlichkeitsgraphen gefunden wird.

## Verwandte Algorithmen in cOde(n)

- **[randomized_01 - Randomized Quicksort](randomized_01_randomized-quicksort.md)** — Las-Vegas-Randomisierung (garantiert Korrektheit, variable Zeit). Karger ist Monte Carlo (garantiert Zeit, variable Korrektheit).

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) erstellt wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*