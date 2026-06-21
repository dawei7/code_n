# Formale mathematische Spezifikation: Artikulationspunkte (Cut Vertices)

## 1. Definitionen und Notation

Sei $G = (V, E)$ ein ungerichteter, zusammenhängender Graph, wobei $V = \{v_1, v_2, \dots, v_n\}$ die Menge der Knoten und $E \subseteq \{\{u, v\} : u, v \in V, u \neq v\}$ die Menge der Kanten ist. Sei $n = |V|$ und $m = |E|$.

Ein **Artikulationspunkt** ist ein Knoten $v \in V$, sodass der Teilgraph $G' = (V \setminus \{v\}, E')$ mehr Zusammenhangskomponenten besitzt als $G$, wobei $E' = \{e \in E : v \notin e\}$.

Wir definieren die folgenden Abbildungen und Mengen, die während einer Tiefensuche (DFS) ausgehend von einem beliebigen Wurzelknoten $r \in V$ generiert werden:
*   $T = (V, E_T)$: Der DFS-Spannbaum, wobei $E_T \subset E$ die Menge der Baumkanten ist.
*   $E_B = E \setminus E_T$: Die Menge der Rückwärtskanten (Back-edges).
*   $tin(u) \in \mathbb{N}_0$: Der Entdeckungszeitpunkt des Knotens $u$, der die Reihenfolge repräsentiert, in der $u$ zum ersten Mal besucht wird.
*   $low(u) \in \mathbb{N}_0$: Der früheste Entdeckungszeitpunkt, der von $u$ aus in $T$ durch das Durchlaufen von null oder mehr Baumkanten im Teilbaum mit Wurzel $u$, gefolgt von höchstens einer Rückwärtskante, erreichbar ist.
*   $parent(u)$: Der Vorgänger von $u$ in $T$.
*   $children(u) = \{v \in V : (u, v) \in E_T\}$: Die Menge der Kinder von $u$ in $T$.

## 2. Algebraische Charakterisierung

Die Werte von $low(u)$ sind durch die folgende Rekursionsgleichung definiert:
$$low(u) = \min \left( \{tin(u)\} \cup \{low(v) : v \in children(u)\} \cup \{tin(v) : (u, v) \in E_B\} \right)$$

Ein Knoten $u \in V$ ist genau dann ein Artikulationspunkt, wenn er eine der folgenden zwei Bedingungen erfüllt:

1.  **Wurzelfall:** Wenn $u = r$, dann ist $u$ genau dann ein Artikulationspunkt, wenn $|children(r)| > 1$.
2.  **Nicht-Wurzelfall:** Wenn $u \neq r$, dann ist $u$ genau dann ein Artikulationspunkt, wenn es mindestens ein Kind $v \in children(u)$ gibt, sodass:
    $$low(v) \geq tin(u)$$

**Beweisskizze:**
Wenn $low(v) \geq tin(u)$ gilt, existiert kein Pfad vom Teilbaum mit Wurzel $v$ zu einem Vorfahren von $u$, der nicht durch $u$ verläuft. Somit führt das Entfernen von $u$ dazu, dass der Teilbaum $T_v$ vom Rest des Graphen $G \setminus T_v$ getrennt wird. Umgekehrt gilt: Wenn $u$ nicht die Wurzel ist und kein solches Kind besitzt, hat jeder Teilbaum $T_v$ eine Rückwärtskante zu einem Vorfahren von $u$, wodurch der Zusammenhang nach dem Entfernen von $u$ gewahrt bleibt.

## 3. Komplexitätsanalyse

### Zeitkomplexität: $O(V + E)$
Der Algorithmus führt eine einzelne DFS-Traversierung durch. 
*   Jeder Knoten $v \in V$ wird genau einmal besucht, was $O(1)$ zur Zuweisung des Entdeckungszeitpunkts beiträgt.
*   Jede Kante $e \in E$ wird genau zweimal untersucht (einmal von jedem Endpunkt aus).
*   Die Aktualisierungsoperationen für $low(u)$ und die bedingten Prüfungen für Artikulationspunkte sind $O(1)$ pro Kantenuntersuchung.
*   Die gesamte Zeitkomplexität ergibt sich aus der Summe der Arbeit über alle Knoten und Kanten:
    $$T(n, m) = \sum_{v \in V} O(deg(v)) = O(2m) = O(V + E)$$

### Platzkomplexität: $O(V)$
Der benötigte zusätzliche Speicherplatz wird primär durch die Speicherung des Graphen und der Zustands-Arrays bestimmt:
*   **Adjacency List:** $O(V + E)$ zur Speicherung der Graphenstruktur.
*   **Zustands-Arrays:** Die Arrays $tin$, $low$ und $parent$ benötigen jeweils $O(V)$ Speicherplatz.
*   **Rekursions-Stack:** Im Schlechtesten Fall (ein Pfadgraph) beträgt die DFS-Rekursionstiefe $O(V)$.
*   **Gesamtspeicher:** Ohne den Eingabegraphen beträgt der zusätzliche Speicherplatz $O(V)$. Unter Einbeziehung der Eingaberepräsentation beträgt die Platzkomplexität $O(V + E)$. Angesichts der Problemvorgaben ist der zusätzliche Speicherplatz strikt $O(V)$.