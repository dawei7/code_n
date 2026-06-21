# Push-Relabel (Max Flow)

| | |
|---|---|
| **ID** | `flow_06` |
| **Kategorie** | flow |
| **Komplexität (erforderlich)** | $O(V^3)$ |
| **Schwierigkeit** | 9/10 |
| **Interview-Relevanz** | 2/10 |
| **Wikipedia** | [Push–relabel maximum flow algorithm](https://en.wikipedia.org/wiki/Push%E2%80%93relabel_maximum_flow_algorithm) |

## Problemstellung

Gegeben ist ein gerichteter Graph, der ein Netzwerk aus Rohren mit Kapazitäten darstellt. Finden Sie den maximal möglichen Fluss von einem Quellknoten S zu einem Senkenknoten T.
Sie müssen dies unter Verwendung des **Push-Relabel**-Frameworks lösen. Anstatt augmentierende Pfade von S nach T zu finden (wie bei Ford-Fulkerson oder Dinic), ignoriert dieser Algorithmus Pfade vollständig. Er arbeitet rein lokal und schiebt "überschüssiges Wasser" zwischen benachbarten Knoten wie eine Reihe kaskadierender Wasserfälle hin und her.

**Eingabe:** Ein gerichteter Graph mit Kapazitäten, ein Quellknoten `s` und ein Senkenknoten `t`.
**Ausgabe:** Eine Ganzzahl, die den maximalen Gesamtfluss repräsentiert.

## Wann man es verwendet

- Push-Relabel-Algorithmen (insbesondere die Variante "Highest-Label Preflow Push") sind empirisch die schnellsten existierenden Max-Flow-Algorithmen für dichte Graphen und übertreffen Dinic bei extremen realen Arbeitslasten.
- Der grundlegende Mechanismus wird häufig in verteilten Netzwerkflussberechnungen eingesetzt, da Knoten nur mit ihren unmittelbaren Nachbarn kommunizieren müssen.

## Ansatz

Stellen Sie sich die Knoten als Wassereimer vor, die in unterschiedlichen Höhen aufgehängt sind. Wasser fließt natürlicherweise bergab.

1. **Initialisierung (Höhen & Preflow):**
   - Jeder Knoten beginnt bei `height = 0`. Die Quelle S wird auf `height = V` (den höchsten Punkt) angehoben.
   - S flutet sofort alle ihre Nachbarn mit so viel Wasser, wie deren Rohre aufnehmen können (Sättigung der ausgehenden Kanten).
   - Diese Nachbarn haben nun einen "Überschuss" (Excess Flow) (sie haben Wasser in ihren Eimern, haben es aber noch nirgendwohin weitergeleitet).

2. **Die Operationen:**
   Wir verarbeiten jeden Knoten (außer S oder T), der aktuell einen `excess > 0` aufweist. Wir können zwei Dinge tun:
   - **PUSH:** Wenn der Knoten überschüssiges Wasser hat und einen Nachbarn besitzt, der strikt *bergab* liegt (`height[u] == height[v] + 1`), und das Rohr zwischen ihnen noch Restkapazität besitzt, "schieben" (Push) wir so viel Wasser wie möglich durch das Rohr.
   - **RELABEL:** Wenn der Knoten überschüssiges Wasser hat, aber ALLE seine Nachbarn mit verfügbarer Rohrkapazität auf der gleichen Höhe oder strikt *höher* liegen, ist das Wasser gefangen! Wir müssen den Knoten "umetikettieren" (Relabel/anheben). Wir erhöhen seine Höhe so, dass sie genau 1 über der des niedrigsten verfügbaren Nachbarn liegt.

3. **Terminierung:**
   Wir fahren mit dem Pushen und Relabeln fort, bis absolut kein Knoten mehr überschüssiges Wasser besitzt.
   - Alles Wasser, das T erreicht, bleibt in T. Das ist unser Max Flow!
   - Alles Wasser, das im Netzwerk gefangen bleibt, wird schließlich so hoch angehoben, dass es über die residualen Kanten den ganzen Weg zurück zur Quelle S fließt!

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

## Durchlauf

*(Konzeptionell)*
`S -> A (cap 10)`. `A -> T (cap 5)`.
1. **Initialisierung:** `height[S] = 4`. Alle anderen 0. `S` schiebt 10 zu `A`. `excess[A] = 10`.
2. **Push:** `A` ist aktiv. Nachbar `T` liegt bergab (`height[A]=0`, `height[T]=0` ... Moment! Sie sind auf der gleichen Höhe!). `A` kann nicht pushen!
3. **Relabel:** `A` ist gefangen. Der niedrigste Nachbar mit Kapazität ist `T` (Höhe 0). `A` wird auf `height = 1` angehoben.
4. **Push:** Jetzt ist `height[A]=1` und `height[T]=0`. `A` schiebt 5 Einheiten zu `T`.
   - `excess[T] = 5`.
   - `excess[A] = 5`. `A` ist immer noch aktiv!
5. **Relabel:** `A` versucht zu `T` zu pushen, aber das Rohr ist vollständig gesättigt. Der einzige Nachbar mit Restkapazität ist S (über die rückwärtige "Undo"-Kante). `height[S] = 4`.
   - `A` wird auf `height = 4 + 1 = 5` angehoben!
6. **Push:** Jetzt ist `height[A]=5` und `height[S]=4`. `A` schiebt seine verbleibenden 5 Einheiten Überschuss zurück zu S.
7. **Abschluss:** Keine aktiven Knoten mehr. Die Senke `T` hat genau 5 Einheiten. Max Flow = 5. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(V^2)$ | $O(V^2)$ |
| **Durchschnittlicher Fall** | Viel schneller als V^3 | $O(V^2)$ |
| **Schlechtester Fall** | $O(V^3)$ | $O(V^2)$ |

Die theoretische Zeitkomplexität im schlechtesten Fall für den generischen FIFO Push-Relabel-Algorithmus ist mathematisch auf genau $O(V^3)$ begrenzt (oder $O(V^2 \sqrt{E})$, wenn der Knoten mit dem höchsten Label ausgewählt wird). Dies macht ihn bei dichten Graphen, bei denen E ~= V^2 gilt, Edmonds-Karp ($O(V \cdot E^2)$) strikt überlegen.
Die Platzkomplexität beträgt $O(V^2)$, um die Kapazitäts- und Flussmatrizen zu speichern.

## Varianten & Optimierungen

- **Gap-Heuristik:** Die wichtigste Optimierung in produktivem Code. Wenn Sie während einer Relabel-Operation bemerken, dass *kein Knoten* im gesamten Graphen auf der `height = X` existiert, dann ist mathematisch bewiesen, dass jeder Knoten mit einer Höhe > X vollständig von der Senke getrennt ist! Sie können all diese Knoten sofort auf `height = V` anheben, was sie dazu zwingt, sofort zurück zu S abzufließen, wodurch Tausende nutzloser Zwischen-Relabel-Operationen übersprungen werden.

## Praxisanwendungen

- **Verteilte Systeme:** Berechnung von aggregierten Datendurchsätzen in massiven Peer-to-Peer-Torrent-Schwärmen, bei denen globales Pfadfinden unmöglich ist, lokales "Pushen" jedoch trivial ist.

## Verwandte Algorithmen in cOde(n)

- **[flow_04 - Dinic's Algorithm](flow_04_dinic-s-max-flow.md)** — Der Rivale der augmentierenden Pfade, der im Allgemeinen einfacher zu implementieren ist und in Standard-Programmierwettbewerben bevorzugt wird.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*