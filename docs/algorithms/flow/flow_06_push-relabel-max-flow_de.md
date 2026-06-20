# Push-Relabel (Max Flow)

| | |
|---|---|
| **ID** | `flow_06` |
| **Kategorie** | Durchfluss |
| **Komplexität (erforderlich)** | $O(V^3)$ |
| **Schwierigkeitsgrad** | 9/10 |
| **Relevanz für Vorstellungsgespräche** | 2/10 |
| **Wikipedia** | [Push–Relabel-Algorithmus für den maximum flow](https://en.wikipedia.org/wiki/Push%E2%80%93relabel_maximum_flow_algorithm) |

## Problemstellung

Gegeben sei ein gerichteter Graph, der ein Rohrleitungsnetz mit Kapazitäten darstellt. Finden Sie den maximal möglichen Fluss von einem Quellknoten S zu einem Senkenknoten T.
Sie müssen diese Aufgabe unter Verwendung des **Push-Relabel**-Ansatzes lösen. Anstatt augmentierende Pfade von S nach T zu finden (wie bei Ford-Fulkerson oder Dinic), ignoriert dieser Algorithmus Pfade vollständig. Er arbeitet ausschließlich lokal und schiebt „überschüssiges Wasser“ wie bei einer Reihe von ineinanderfließenden Wasserfällen zwischen benachbarten Knoten hin und her.

**Eingabe:** Ein gerichteter Graph mit Kapazitäten, einem Quellknoten `s` und einem Senkenknoten `t`.
**Ausgabe:** Eine ganze Zahl, die den maximalen Gesamtfluss angibt.

## Wann sollte man es verwenden?

- „Push-Relabel“-Algorithmen (insbesondere die Variante „Highest-Label Preflow Push“) sind empirisch gesehen die schnellsten Max-Flow-Algorithmen, die es für dichte Graphen gibt, und übertreffen den Dinic-Algorithmus bei extremen realen Arbeitslasten.
- Der grundlegende Mechanismus wird häufig bei verteilten Netzwerkflussberechnungen eingesetzt, da Knoten nur mit ihren unmittelbaren Nachbarn kommunizieren müssen.

## Vorgehensweise

Stellen Sie sich die Knoten als Eimer mit Wasser vor, die in unterschiedlichen Höhen aufgehängt sind. Wasser fließt naturgemäß bergab.

1. **Initialisierung (Höhen & Vorfluss):**
   - Jeder Knoten beginnt bei `height = 0`. Die Quelle S wird auf `height = V` (den höchsten Punkt) angehoben.
   - S überflutet sofort alle seine Nachbarn mit so viel Wasser, wie deren Leitungen aufnehmen können (wodurch die ausgehenden Kanten gesättigt werden).
   - Diese Nachbarn haben nun einen „Überschussfluss“ (sie haben Wasser in ihren Eimern, haben es aber noch nirgendwohin weitergeleitet).

2. **Die Operationen:**
   Wir bearbeiten jeden Knoten (außer S oder T), der derzeit `excess > 0` aufweist. Wir haben zwei Möglichkeiten:
   - **PUSH:** Wenn der Knoten überschüssiges Wasser hat, einen Nachbarn, der streng *unterhalb* liegt (`height[u] == height[v] + 1`), und die Leitung zwischen ihnen noch Restkapazität besitzt, „schieben“ wir so viel Wasser wie möglich durch die Leitung.
   - **UMBENENNEN:** Wenn der Knoten überschüssiges Wasser hat, aber ALLE seine Nachbarn mit verfügbarer Rohrkapazität auf derselben Höhe oder streng *höher* liegen, ist das Wasser eingeschlossen! Wir müssen den Knoten „umbenennen“ (anheben). Wir erhöhen seine Höhe so, dass sie genau 1 höher ist als die des niedrigsten verfügbaren Nachbarn.

3. **Beendigung:**
   Wir fahren mit dem „Push“ und dem „Relabel“ fort, bis absolut kein Knoten mehr überschüssiges Wasser hat.
   - Jegliches Wasser, das es bis nach T schafft, bleibt in T. Das ist unser Maximalfluss!
   - Jegliches im Netzwerk eingeschlossene Wasser wird schließlich so hoch angehoben, dass es *rückwärts* über die verbleibenden Kanten den ganzen Weg zurück zur Quelle S fließt!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for flow_06: Push-Relabel Max Flow.

Compute the max s-t flow using the Goldberg-Tarjan
"""


def solve(n, edges):
    """Goldberg-Tarjan push-relabel max flow.

    Generic O(V^3) variant. The residual capacity of an edge
    (u, v) is maintained as a direct value (not cap-flow),
    so a push that decreases residual[u][v] increases
    residual[v][u] by the same amount.
    """
    # residual[u][v] = remaining forward capacity from u to v.
    residual = [[0] * n for _ in range(n)]
    for u, v, c in edges:
        residual[u][v] += c
    height = [0] * n
    excess = [0] * n
    height[0] = n
    # Initial push from source: saturate every outgoing edge.
    for v in range(n):
        if residual[0][v] > 0:
            pushed = residual[0][v]
            residual[0][v] -= pushed
            residual[v][0] += pushed
            excess[v] += pushed

    def push(u, v):
        d = min(excess[u], residual[u][v])
        if d <= 0:
            return False
        residual[u][v] -= d
        residual[v][u] += d
        excess[u] -= d
        excess[v] += d
        return True

    def relabel(u):
        best = float("inf")
        for v in range(n):
            if residual[u][v] > 0 and height[v] < best:
                best = height[v]
        if best < float("inf"):
            height[u] = best + 1

    # Main loop: discharge active vertices (those with positive
    # excess that are not s or t). When a push creates new
    # excess at an inner vertex, add it to the active list.
    active = set()
    for i in range(1, n - 1):
        if excess[i] > 0:
            active.add(i)
    while active:
        # Highest-label selection.
        u = max(active, key=lambda x: height[x])
        old_h = height[u]
        # Discharge: try to push, or relabel.
        while excess[u] > 0:
            pushed = False
            for v in range(n):
                if residual[u][v] > 0 and height[u] == height[v] + 1:
                    if push(u, v):
                        pushed = True
                        if v != 0 and v != n - 1 and excess[v] > 0:
                            active.add(v)
                        break
            if not pushed:
                relabel(u)
        if excess[u] == 0:
            active.discard(u)
    return excess[n - 1]
```

</details>

## Schritt-für-Schritt-Anleitung

*(Konzeptionell)*
`S -> A (cap 10)`. `A -> T (cap 5)`.
1. **Initialisierung:** `height[S] = 4`. Alle anderen 0. `S` schiebt 10 auf `A`. `excess[A] = 10`.
2. **Einfügen:** `A` ist aktiv. Der Nachbar `T` liegt tiefer (`height[A]=0`, `height[T]=0` … Moment! Sie befinden sich auf derselben Höhe!). `A` kann nicht schieben!
3. **Neu kennzeichnen:** `A` ist eingeklemmt. Der niedrigste Nachbar mit Kapazität ist `T` (Höhe 0). `A` wird auf `height = 1` angehoben.
4. **Schieben:** Jetzt `height[A]=1` und `height[T]=0`. `A` schiebt 5 Einheiten zu `T`.
   - `excess[T] = 5`.
   - `excess[A] = 5`. `A` ist noch aktiv!
5. **Umbenennung:** `A` versucht, nach `T` zu schieben, aber die Leitung ist vollständig ausgelastet. Der einzige Nachbar mit Restkapazität ist S (über die rückwärts gerichtete „Undo“-Kante). `height[S] = 4`.
   - `A` wird nach `height = 4 + 1 = 5` verschoben!
6. **Schieben:** Nun `height[A]=5` und `height[S]=4`. `A` schiebt seine verbleibenden 5 Überschüsse zurück in S.
7. **Abgleich:** Keine aktiven Knoten. Der Senke `T` liegen genau 5 Einheiten vor. Maximum Flow = 5. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(V^2)$ | $O(V^2)$ |
| **Durchschnittlicher Fall** | Deutlich schneller als V^3 | $O(V^2)$ |
| **Schlechtester Fall** | $O(V^3)$ | $O(V^2)$ |

Die theoretische Laufzeit im schlimmsten Fall für den generischen FIFO-Push-Relabel-Algorithmus ist mathematisch genau auf $O(V^3)$ begrenzt (bzw. auf $O(V^2 \sqrt{E})$, wenn der Knoten mit der höchsten Aktivität ausgewählt wird). Dadurch ist er bei dichten Graphen, bei denen E ~= V^2 gilt, dem Edmonds-Karp-Algorithmus ($O(V \cdot E^2)$) streng überlegen.
Die Platzkomplexität beträgt $O(V^2)$ für die Speicherung der Kapazitäts- und Flussmatrizen.

## Varianten & Optimierungen

- **Gap-Heuristik:** Die entscheidende Optimierung im Produktionscode. Wenn du während einer Relabel-Operation feststellst, dass *kein Knoten* im gesamten Graphen bei `height = X` liegt, dann ist mathematisch bewiesen, dass jeder Knoten mit einer Höhe > X vollständig vom Sink getrennt ist! Sie können all diese Knoten sofort auf `height = V` anheben und so erzwingen, dass sie sofort zurück nach S fließen, wodurch Tausende nutzloser zwischengeschalteter „Relabel“-Operationen übersprungen werden.

## Praktische Anwendungen

- **Verteilte Systeme:** Berechnung aggregierter Datenflussdurchsätze in riesigen Peer-to-Peer-Torrent-Schwärmen, in denen eine globale Pfadfindung unmöglich, lokales „Pushing“ jedoch trivial ist.

## Verwandte Algorithmen in cOde(n)

- **[flow_04 – Dinics Algorithmus](flow_04_dinic-s-max-flow.md)** — Der Konkurrent des Augmenting-Path-Algorithmus, der im Allgemeinen einfacher zu programmieren ist und bei Standard-Algorithmuswettbewerben bevorzugt wird.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
nach dem Vorbild der kanonischen Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
