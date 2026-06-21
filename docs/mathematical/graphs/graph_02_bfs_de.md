# Formale mathematische Spezifikation: Breitensuche (Breadth-First Search, BFS)

## 1. Definitionen und Notation

Sei $G = (V, E)$ ein ungewichteter, ungerichteter Graph, wobei $V = \{v_1, v_2, \dots, v_n\}$ die Menge der Knoten und $E \subseteq \{\{u, v\} : u, v \in V, u \neq v\}$ die Menge der Kanten ist. Wir bezeichnen die Adjazenzmenge eines Knotens $u$ als $\text{Adj}(u) = \{v \in V : \{u, v\} \in E\}$.

Der Algorithmus operiert auf dem folgenden Zustandsraum $\mathcal{S}$:
*   **Distanzfunktion:** $d: V \to \mathbb{N} \cup \{\infty\}$, wobei $d(v)$ die kürzeste Pfaddistanz von einem Startknoten $s \in V$ zu $v$ darstellt.
*   **Vorgängerfunktion:** $\pi: V \to V \cup \{\text{null}\}$, die jeden Knoten auf seinen unmittelbaren Vorgänger im BFS-Baum abbildet.
*   **Besucht-Menge:** $S \subseteq V$, die Menge der vom Algorithmus entdeckten Knoten.
*   **Queue:** $Q$, eine First-In-First-Out (FIFO) Sequenz von Knoten $Q = (q_1, q_2, \dots, q_k)$.

Die Eingabe ist das Paar $(G, s)$ und die Ausgabe ist das Tupel $(d, \pi, \mathcal{O})$, wobei $\mathcal{O}$ die Sequenz der Knoten in der Reihenfolge ihres Entfernens aus der Queue (dequeued) ist.

## 2. Algebraische Charakterisierung

Die Korrektheit der BFS basiert auf der Eigenschaft, dass der Graph in nicht-abnehmender Reihenfolge der Distanz von $s$ erkundet wird. Wir definieren die Distanz $d(v)$ als die Länge des kürzesten Pfades $\delta(s, v)$.

### Die BFS-Invariante
Zu jedem Zeitpunkt während der Ausführung gelte $Q = (v_1, v_2, \dots, v_k)$. Die folgenden Bedingungen sind erfüllt:
1.  $d(v_1) \leq d(v_2) \leq \dots \leq d(v_k)$.
2.  $d(v_k) \leq d(v_1) + 1$.

### Rekurrenz
Die Distanzfunktion $d(v)$ erfüllt die folgende Rekursionsgleichung:
$$d(v) = \begin{cases} 0 & \text{if } v = s \\ \min_{\{u, v\} \in E} \{d(u) + 1\} & \text{if } v \neq s \text{ and } v \text{ is reachable from } s \\ \infty & \text{otherwise} \end{cases}$$

### Übergangslogik
Für einen Knoten $u$, der aus der Queue $Q$ entfernt wurde, führt der Algorithmus für jeden Nachbarn $v \in \text{Adj}(u)$ das folgende Update durch:
Falls $v \notin S$:
1.  $S \leftarrow S \cup \{v\}$
2.  $d(v) \leftarrow d(u) + 1$
3.  $\pi(v) \leftarrow u$
4.  $Q \leftarrow Q \cdot (v)$ (wobei $\cdot$ die Konkatenation bezeichnet)

Dies stellt sicher, dass für jede Kante $\{u, v\} \in E$ die Dreiecksungleichung gilt: $d(v) \leq d(u) + 1$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität wird durch die Anzahl der Operationen bestimmt, die auf Knoten und Kanten ausgeführt werden.
*   **Knotenverarbeitung:** Jeder Knoten $v \in V$ wird genau einmal in die Queue eingefügt (enqueue) und entfernt (dequeue). Dies trägt $O(V)$ zur Komplexität bei.
*   **Kantenverarbeitung:** Bei einer Darstellung als Adjazenzliste iterieren wir für jeden Knoten $u$, der aus der Queue entfernt wird, über dessen Adjazenzliste $\text{Adj}(u)$. Über die gesamte Ausführung hinweg wird jede Kante $\{u, v\} \in E$ genau zweimal untersucht (einmal von $u$ und einmal von $v$). Dies trägt $O(E)$ zur Komplexität bei.

Die gesamte Zeitkomplexität $T(V, E)$ ergibt sich zu:
$$T(V, E) = \sum_{v \in V} (1 + \text{deg}(v)) = O(V + E)$$
Bei einer Darstellung als Adjazenzmatrix muss der Algorithmus für jeden der $|V|$ Knoten die gesamte Zeile der Länge $|V|$ durchsuchen, was zu $T(V) = O(V^2)$ führt.

### Platzkomplexität
Die Platzkomplexität $S(V)$ wird durch die Speicherung der Hilfsstrukturen dominiert:
1.  **Distanz- und Vorgänger-Arrays:** $O(V)$ zur Speicherung von $d(v)$ und $\pi(v)$ für alle $v \in V$.
2.  **Besucht-Menge:** $O(V)$ zur Speicherung des booleschen Status jedes Knotens.
3.  **Queue:** Im schlechtesten Fall (z. B. bei einem Stern-Graphen) kann die Queue $O(V)$ Knoten enthalten.

Somit ergibt sich die gesamte zusätzliche Platzkomplexität zu:
$$S(V) = O(V) + O(V) + O(V) = O(V)$$