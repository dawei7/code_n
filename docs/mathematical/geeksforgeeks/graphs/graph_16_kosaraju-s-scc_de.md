# Formale mathematische Spezifikation: Kosaraju-Algorithmus (SCC)

## 1. Definitionen und Notation

Sei $G = (V, E)$ ein gerichteter Graph, wobei $V = \{v_1, v_2, \dots, v_n\}$ die Menge der Knoten und $E \subseteq V \times V$ die Menge der gerichteten Kanten ist. Sei $|V| = n$ und $|E| = m$.

*   **Stark zusammenhängende Komponente (SCC):** Eine Teilmenge $S \subseteq V$ ist eine SCC, wenn für jedes Paar $u, v \in S$ ein gerichteter Pfad von $u$ nach $v$ und ein gerichteter Pfad von $v$ nach $u$ existiert, und $S$ bezüglich dieser Eigenschaft maximal ist.
*   **Transponierter Graph:** Die Transponierte von $G$, bezeichnet als $G^T = (V, E^T)$, ist definiert durch $E^T = \{(v, u) \mid (u, v) \in E\}$.
*   **Erreichbarkeit:** Sei $u \rightsquigarrow v$ die Notation für die Existenz eines gerichteten Pfades von $u$ nach $v$.
*   **Finish Time:** Sei $f(u)$ der Zeitstempel, zu dem die Tiefensuche (DFS) die Exploration des Teilbaums mit Wurzel $u$ abschließt.
*   **Zustandsraum:** Der Algorithmus operiert auf dem Zustandsraum $\mathcal{S} = (V, E, E^T, \text{visited}, \text{stack}, \mathcal{C})$, wobei $\text{visited}: V \to \{0, 1\}$, $\text{stack}$ eine geordnete Sequenz von $V$ ist und $\mathcal{C} = \{S_1, S_2, \dots, S_k\}$ die Partitionierung von $V$ in SCCs darstellt.

## 2. Algebraische Charakterisierung

Der Kosaraju-Algorithmus beruht auf den Eigenschaften des Kondensationsgraphen $G^{SCC}$, welcher ein gerichteter azyklischer Graph (DAG) ist, in dem jeder Knoten eine SCC von $G$ repräsentiert.

### Durchlauf 1: Topologische Sortierung
Der erste Durchlauf führt eine DFS auf $G$ aus, um die Finish Times $f(u)$ zu berechnen. Sei $L$ die Liste der Knoten, sortiert nach $f(u)$ in absteigender Reihenfolge.
**Lemma:** Wenn es eine Kante $(S_i, S_j)$ im Kondensationsgraphen $G^{SCC}$ gibt, dann gilt $\max_{u \in S_i} f(u) > \max_{v \in S_j} f(v)$.
Folglich ist garantiert, dass das erste Element von $L$ zu einer "Quell"-SCC in $G^{SCC}$ gehört.

### Durchlauf 2: Transposition und Traversierung
Der zweite Durchlauf führt eine DFS auf $G^T$ aus. Durch das Umkehren der Kanten invertieren wir die Erreichbarkeit: Wenn $S_i \to S_j$ in $G^{SCC}$ gilt, dann gilt $S_j \to S_i$ in $(G^T)^{SCC}$.
Sei $u$ der Knoten mit der größten $f(u)$ in der verbleibenden Menge unbesuchter Knoten. Die Menge der von $u$ in $G^T$ erreichbaren Knoten, bezeichnet als $Reach(u, G^T)$, erfüllt:
$$Reach(u, G^T) = \{v \in V \mid u \rightsquigarrow_{G^T} v\} = S_u$$
wobei $S_u$ die SCC ist, die $u$ enthält. Da $u$ aus der "Senken"-SCC des aktuellen Teilgraphen von $G^T$ gewählt wird (was einer "Quell"-SCC in $G$ entspricht), ist die DFS auf $S_u$ beschränkt und kann nicht in andere SCCs traversieren.

**Invariante:** Nach der $i$-ten Iteration des zweiten Durchlaufs bildet die Menge der besuchten Knoten $\bigcup_{j=1}^i S_j$ die Vereinigung der ersten $i$ SCCs, die in der topologischen Ordnung von $G^{SCC}$ identifiziert wurden.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus besteht aus drei unterschiedlichen Phasen:
1.  **Graph-Transposition:** Die Konstruktion von $G^T$ erfordert das Iterieren über alle Kanten $E$. Dies benötigt $\Theta(V + E)$ Zeit.
2.  **Durchlauf 1 (DFS auf $G$):** Eine Standard-DFS besucht jeden Knoten einmal und traversiert jede Kante einmal. Die Komplexität beträgt $\Theta(V + E)$.
3.  **Durchlauf 2 (DFS auf $G^T$):** Ebenso besucht eine DFS auf $G^T$ jeden Knoten und jede Kante genau einmal. Die Komplexität beträgt $\Theta(V + E)$.

Die gesamte Zeitkomplexität $T(n, m)$ ist die Summe dieser Phasen:
$$T(n, m) = \Theta(V + E) + \Theta(V + E) + \Theta(V + E) = O(V + E)$$

### Platzkomplexität
Die Platzkomplexität $S(n, m)$ wird durch die Speicheranforderungen bestimmt:
1.  **Adjacency Lists:** Das Speichern von $G$ und $G^T$ erfordert $O(V + E)$ Platz.
2.  **Hilfs-Arrays:** Das `visited`-Array und der `order`-Stack erfordern $O(V)$ Platz.
3.  **Rekursions-Stack:** Im Schlechtesten Fall (ein degenerierter Pfadgraph) beträgt die Rekursionstiefe der DFS $O(V)$.

Somit ergibt sich die gesamte Platzkomplexität zu:
$$S(n, m) = O(V + E) + O(V) + O(V) = O(V + E)$$