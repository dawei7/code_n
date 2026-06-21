# Brücken in einem Graphen (Cut Edges)

| | |
|---|---|
| **ID** | `graph_14` |
| **Kategorie** | Graphen |
| **Komplexität (erforderlich)** | $O(V + E)$ Zeit, $O(V)$ Platz |
| **Schwierigkeit** | 7/10 |
| **Relevanz für Vorstellungsgespräche** | 5/10 |
| **LeetCode-Äquivalent** | [Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/) |

## Problemstellung

Gegeben ist ein ungerichteter Graph. Finde alle Brücken im Graphen.
Eine Brücke (oder Cut Edge) ist eine Kante, deren Entfernung die Anzahl der Zusammenhangskomponenten im Graphen erhöhen würde.

**Eingabe:** Anzahl der Knoten `V` und eine Adjacency List `adj`.
**Ausgabe:** Eine Liste von Kanten `[u, v]`, die Brücken sind.

## Wann man es verwendet

- Zur Identifizierung von "kritischen Verbindungen" in einem Netzwerk.
- Wenn man nach Kanten sucht, die einen Single-Point-of-Failure darstellen, anstatt nach Knoten.

## Ansatz

Dieser Algorithmus ist im Wesentlichen identisch mit **Artikulationspunkten (`graph_13`)**. Du solltest diesen Algorithmus zuerst lesen und verstehen. Wir verwenden Tarjans Discovery Time (`tin`) und Lowest Time (`low`) Arrays.

**Die magische Bedingung (modifiziert):**
Angenommen, wir befinden uns am Knoten `U` und durchlaufen eine Kante, um rekursiv DFS auf einem Nachbarn `V` aufzurufen.
Wenn `DFS(V)` zurückkehrt, aktualisieren wir die Lowest Time von `U`: `low[U] = min(low[U], low[V])`.
Wie erkennen wir nun, ob die Kante U - V eine Brücke ist?

Bei Artikulationspunkten lautete die Bedingung `low[V] >= tin[U]`. Das bedeutete, dass der Teilbaum V bis zu U aufsteigen konnte, aber nicht höher. Das Entfernen von U partitioniert den Graphen.
Aber bei Brücken entfernen wir nicht U, sondern die Kante U - V selbst!
Wenn der Teilbaum V U erreichen kann (was bedeutet `low[V] == tin[U]`), bedeutet das, dass es eine alternative Back-Edge vom Teilbaum gibt, die direkt auf U zeigt! Wenn wir also die primäre Kante U - V entfernen, ist der Teilbaum IMMER NOCH über diese Back-Edge mit U verbunden! Der Graph wird nicht partitioniert.

Daher darf der Teilbaum V für eine Brücke U - V KEINE BACK-EDGES haben, die U oder höher erreichen können! Der absolut niedrigste Knoten, den er erreichen kann, muss strikt unter U liegen.
Die Bedingung lautet daher **strikt größer**: **`low[V] > tin[U]`**.

*(Bonus: Da wir es mit Kanten statt mit Knoten zu tun haben, verschwindet der lästige "Wurzelknoten"-Sonderfall von den Artikulationspunkten vollständig! Die Logik gilt universell für alle Knoten, einschließlich der Wurzel).*

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for graph_14: Bridges.

Tarjan-style DFS on an undirected graph. An edge (u, v) is a
bridge iff, in the DFS tree, ``low[v] > disc[u]``. The result
is the sorted list of (u, v) bridge tuples with u < v.
"""


def solve(num_nodes, edges):
    if num_nodes <= 0:
        return []
    adj = [set() for _ in range(num_nodes)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    disc = [-1] * num_nodes
    low = [0] * num_nodes
    bridges = set()

    def dfs(u, parent, time):
        disc[u] = low[u] = time
        time += 1
        for v in sorted(adj[u]):
            if disc[v] == -1:
                time = dfs(v, u, time)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    bridges.add((min(u, v), max(u, v)))
            elif v != parent:
                low[u] = min(low[u], disc[v])
        return time

    dfs(0, -1, 0)
    return sorted(bridges)
```

</details>

## Durchlauf

`V = 5`. Kanten: `0-1`, `1-2`, `2-0`, `1-3`, `3-4`.
Der Graph ist ein Dreieck `{0, 1, 2}`, das mit einer Linie `1-3-4` verbunden ist.
Intuitiv sind `1-3` und `3-4` die Brücken. Das Dreieck hat redundante Kanten.

1. `dfs(0, -1)`. `tin[0]=1, low[0]=1`.
   - `dfs(1, 0)`. `tin[1]=2, low[1]=2`.
2. `dfs(1, 0)`:
   - `dfs(2, 1)`. `tin[2]=3, low[2]=3`.
3. `dfs(2, 1)`:
   - Nachbar `0`. Back-Edge! `low[2] = min(3, 1) = 1`.
   - Rückkehr zu `dfs(1)`.
4. `dfs(1)` wird fortgesetzt:
   - Aktualisiert `low[1] = min(2, 1) = 1`.
   - Bedingung: `low[2] > tin[1]` -> `1 > 2`. FALSCH. `1-2` ist KEINE Brücke.
   - Nachbar `3`. `dfs(3, 1)`.
5. `dfs(3, 1)`:
   - `dfs(4, 3)`. `tin[4]=5, low[4]=5`.
6. `dfs(4, 3)`:
   - Keine Nachbarn. Rückkehr zu `dfs(3)`.
7. `dfs(3)` wird fortgesetzt:
   - Aktualisiert `low[3] = min(4, 5) = 4`.
   - Bedingung: `low[4] > tin[3]` -> `5 > 4`. WAHR!
   - Füge `[3, 4]` zu den Brücken hinzu!
   - Rückkehr zu `dfs(1)`.
8. `dfs(1)` wird fortgesetzt:
   - Aktualisiert `low[1] = min(1, 4) = 1`.
   - Bedingung: `low[3] > tin[1]` -> `4 > 2`. WAHR!
   - Füge `[1, 3]` zu den Brücken hinzu!

Ergebnis: `[[3, 4], [1, 3]]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(V + E)$ | $O(V + E)$ |
| **Durchschnittlicher Fall** | $O(V + E)$ | $O(V + E)$ |
| **Schlechtester Fall** | $O(V + E)$ | $O(V + E)$ |

Genau wie bei Artikulationspunkten handelt es sich um einen vollständigen DFS-Durchlauf, bei dem jede Kante ausgewertet wird. Die Zeitkomplexität beträgt strikt $O(V + E)$.
Die Platzkomplexität beträgt $O(V)$ für die Arrays und den Rekursions-Stack, plus $O(E)$ im schlechtesten Fall, um das Ausgabe-Array der Brücken zu speichern.

## Varianten & Optimierungen

- **2-Edge-Connected Components:** Wenn man alle Brücken findet und sie physisch aus dem Graphen entfernt, werden die verbleibenden disjunkten Teilgraphen als "2-Edge-Connected Components" bezeichnet. Innerhalb dieser Komponenten gibt es mindestens 2 separate Pfade zwischen jedem Knotenpaar (was bedeutet, dass jede einzelne Kante ausfallen kann und die Komponente verbunden bleibt).

## Anwendungen in der Praxis

- **Verkehrstechnik:** Identifizierung von "Flaschenhals"-Straßen. Wenn eine Brückenkante aufgrund eines Unfalls gesperrt ist, gibt es mathematisch keine alternative Umleitung; die Stadt ist partitioniert.
- **Schaltungsdesign:** Auffinden kritischer Leitungen, deren Trennung die Schaltung vollständig unterbricht.

## Verwandte Algorithmen in cOde(n)

- **[graph_13 - Artikulationspunkte](graph_13_articulation-points.md)** — Das knotenbasierte Äquivalent dieses Algorithmus.
- **[graph_15 - Tarjans SCC](graph_15_tarjan-s-scc.md)** — Die Verallgemeinerung dieser Logik auf gerichtete Graphen, um Komponenten zu finden, die gegenseitig erreichbar sind.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*