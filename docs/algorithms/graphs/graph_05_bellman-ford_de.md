# Bellman-Ford-Algorithmus

| | |
|---|---|
| **ID** | `graph_05` |
| **Kategorie** | Graphen |
| **Komplexität (erforderlich)** | $O(V * E)$ Zeit, $O(V)$ Platz |
| **Schwierigkeit** | 6/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **Wikipedia** | [Bellman-Ford-Algorithmus](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm) |

## Problemstellung

Gegeben ist ein gewichteter Graph, der als Edge List dargestellt ist, sowie ein Startknoten `S`.
Finde die kürzesten Pfade vom Quellknoten `S` zu allen anderen Knoten.
Wichtig ist, dass der Graph **negative Kantengewichte** enthalten kann. Zudem muss erkannt werden, ob der Graph einen **negativen Zyklus** enthält.

**Eingabe:** Anzahl der Knoten `V`, eine Edge List `edges`, wobei jede Kante als `[u, v, weight]` definiert ist, und ein Startknoten `S`.
**Ausgabe:** Ein Array der minimalen Distanzen oder ein Flag, das anzeigt, dass ein negativer Zyklus gefunden wurde.

## Wann man ihn verwendet

- Um den kürzesten Pfad zu finden, wenn **negative Kanten** vorhanden sind.
- Um einen **negativen Zyklus** zu erkennen (ein Zyklus, bei dem die Summe der Kantengewichte strikt kleiner als null ist. Wenn ein solcher Zyklus existiert, kann man unendlich oft durch ihn hindurchlaufen, um eine Pfaddistanz von -\infty zu erreichen, was jede Pfadfindungslogik zerstört).

## Ansatz

**1. Die Schwäche von Dijkstra bei negativen Kanten:**
Der Dijkstra-Algorithmus geht davon aus, dass der kürzeste Pfad zu einem Knoten absolut feststeht, sobald dieser aus der Priority Queue entnommen wird. Er nimmt an, dass das Hinzufügen weiterer Kanten zu einem Pfad die Gesamtdistanz NUR ERHÖHEN kann.
Wenn A \rightarrow B 5 kostet und A \rightarrow C 10 kostet, finalisiert Dijkstra B sofort. Aber was, wenn C \rightarrow B -20 kostet? Der Pfad A \rightarrow C \rightarrow B kostet -10! Dijkstra wird niemals zurückkehren und B korrigieren.

**2. Der Brute-Force "Relaxations"-Durchlauf:**
Bellman-Ford ist im Grunde ein Algorithmus der Dynamischen Programmierung. Er verzichtet vollständig auf die Priority Queue.
Stattdessen durchläuft er JEDE EINZELNE KANTE im gesamten Graphen und versucht, sie zu relaxieren:
`distances[v] = min(distances[v], distances[u] + weight(u, v))`
Wenn wir dies einmal tun, garantieren wir, dass wir alle kürzesten Pfade gefunden haben, die aus genau 1 Kante bestehen.
Wenn wir diesen Durchlauf erneut durchführen, garantieren wir, dass wir alle kürzesten Pfade gefunden haben, die aus \le 2 Kanten bestehen.

**3. Wann man aufhört:**
Was ist die absolut längste Länge, die ein Pfad in einem Graphen haben kann, ohne unendlich in einem Zyklus zu kreisen? Ein Pfad, der jeden Knoten genau einmal besucht: V - 1 Kanten.
Wenn wir den Relaxationsdurchlauf also genau **V - 1 Mal** ausführen, ist mathematisch garantiert, dass wir den absolut kürzesten Pfad zu jedem Knoten gefunden haben!

**4. Erkennung negativer Zyklen:**
Nach Abschluss von V - 1 Durchläufen sind alle legitimen kürzesten Pfade finalisiert.
Was passiert, wenn wir den Durchlauf *ein weiteres Mal* (das V-te Mal) ausführen?
Wenn der kürzeste Pfad finalisiert ist, sollte KEINE Kante mehr relaxiert werden. `distances[v]` sollte bereits perfekt sein.
Wenn jedoch im V-ten Durchlauf eine Relaxation stattfindet, bedeutet dies, dass ein Pfad bei seinem V-ten Sprung kürzer wurde! Dies ist unmöglich, ohne einen Knoten erneut zu besuchen. Wir haben damit definitiv einen negativen Zyklus erkannt!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for graph_05: Bellman-Ford.

Shortest paths from start. Supports negative edges, no negative
cycles (per the spec).
"""


def solve(num_nodes, edges, start):
    INF = float("inf")
    dist = [INF] * num_nodes
    dist[start] = 0
    for _ in range(num_nodes - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break
    return {i: (d if d != INF else -1) for i, d in enumerate(dist)}
```

</details>

## Durchlauf

Graph `V=3`. Kanten: `A->B (1)`, `B->C (-5)`, `C->A (2)`. Start bei `A`.
`distances = {A:0, B:inf, C:inf}`.

**Durchlauf 1:**
- `A->B (1)`: `dist[B] = 0 + 1 = 1`.
- `B->C (-5)`: `dist[C] = 1 - 5 = -4`.
- `C->A (2)`: `dist[A] = -4 + 2 = -2`.
`distances = {A:-2, B:1, C:-4}`.

**Durchlauf 2 (V-1):**
- `A->B (1)`: `dist[B] = -2 + 1 = -1`.
- `B->C (-5)`: `dist[C] = -1 - 5 = -6`.
- `C->A (2)`: `dist[A] = -6 + 2 = -4`.
`distances = {A:-4, B:-1, C:-6}`.

**Durchlauf 3 (Die Überprüfung):**
- `A->B (1)`: `dist[B] = -4 + 1 = -3`.
- Moment! `-3 < -1`! Eine Relaxation fand statt!
- RÜCKGABE "Negative Cycle Detected!". ✓
*(Tatsächlich: 1 - 5 + 2 = -2. Der Zyklus A->B->C->A verliert bei jedem Durchlauf 2 an Gewicht).*

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(E)$ | $O(V)$ |
| **Durchschnittlicher Fall** | $O(V * E)$ | $O(V)$ |
| **Schlechtester Fall** | $O(V * E)$ | $O(V)$ |

Die äußere Schleife läuft V - 1 Mal. Die innere Schleife iteriert über alle E Kanten. Die gesamte Zeitkomplexität ist strikt durch $O(V x E)$ begrenzt.
(Wenn die `updated`-Optimierung verwendet wird, kann der Algorithmus in $O(E)$ Zeit terminieren, falls der Graph extrem klein oder stark linear ist, aber der schlechteste Fall bleibt $O(VE)$).
Die Platzkomplexität beträgt strikt $O(V)$ für das `distances`-Array. Beachten Sie, dass wir im Gegensatz zu BFS/Dijkstra nicht einmal eine Adjacency List aufbauen müssen! Wir iterieren direkt über die rohe Edge List.

## Varianten & Optimierungen

- **SPFA (Shortest Path Faster Algorithm):** Eine auf einer Queue basierende Verbesserung des Standard-Bellman-Ford. Anstatt blind alle Kanten V-1 Mal zu durchlaufen, führen wir eine FIFO-Queue von Knoten, deren Distanzen kürzlich relaxiert wurden. Wir entnehmen einen Knoten, relaxieren seine ausgehenden Kanten und fügen erfolgreich relaxierte Nachbarn der Queue hinzu. Er arbeitet in der Praxis mit $O(E)$ bei zufälligen Graphen, behält aber den $O(VE)$ Worst-Case bei. Er ist der moderne Standard für die Pfadfindung mit negativen Kanten.

## Anwendungen in der Praxis

- **Distance-Vector Routing (RIP-Protokoll):** Frühe Internet-Router nutzten Bellman-Ford, um ihre Routing-Tabellen an Nachbarn zu übertragen. Das "Count-to-Infinity"-Problem in der Netzwerktechnik ist buchstäblich die physische Manifestation eines Bellman-Ford-Negativzyklus (Routing-Schleifen).
- **Arbitrage-Erkennung im Finanzwesen:** Wenn man Währungswechselkurse als Kantengewichte betrachtet (indem man den negativen Logarithmus des Kurses nimmt), entspricht das Finden eines Zyklus, der zu einem Multiplikator >1.0 führt (kostenloses Geld!), mathematisch exakt dem Finden eines negativen Zyklus mittels Bellman-Ford!

## Verwandte Algorithmen in cOde(n)

- **[graph_04 - Dijkstra-Algorithmus](graph_04_dijkstra.md)** — Die schnellere $O(E log V)$ Alternative für rein positive Gewichte.
- **[graph_06 - Floyd-Warshall](graph_06_floyd-warshall.md)** — Der $O(V^3)$ Algorithmus, um kürzeste Pfade zwischen ALLEN Knotenpaaren zu finden, nicht nur von einer einzelnen Quelle aus.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Seiten für kompetitive Programmierung verwendet wird. Für den enzyklopädischen Standardeintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*