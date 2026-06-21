# Formale mathematische Spezifikation: Minimum S-T Cut

## 1. Definitionen und Notation

Sei $G = (V, E)$ ein gerichteter Graph, wobei $V$ eine endliche Menge von Knoten und $E \subseteq V \times V$ eine Menge von gerichteten Kanten ist. Wir definieren eine Kapazitätsfunktion $c: E \to \mathbb{R}_{\geq 0}$, die jeder Kante eine nicht-negative Kapazität zuweist. Gegeben eine Quelle $s \in V$ und eine Senke $t \in V$, ist ein **Flow Network** das Tripel $(G, c, s, t)$.

Ein **Flow** ist eine Funktion $f: E \to \mathbb{R}_{\geq 0}$, die folgende Bedingungen erfüllt:
1. **Kapazitätsbeschränkung:** $\forall (u, v) \in E, 0 \leq f(u, v) \leq c(u, v)$.
2. **Flusserhaltung:** $\forall v \in V \setminus \{s, t\}, \sum_{u:(u, v) \in E} f(u, v) = \sum_{w:(v, w) \in E} f(v, w)$.

Ein **$s-t$ cut** ist eine Partition von $V$ in zwei disjunkte Mengen $S$ und $T$, sodass $s \in S$ und $t \in T$, wobei $T = V \setminus S$ gilt. Die Kapazität des Schnitts $(S, T)$, bezeichnet als $c(S, T)$, ist definiert als:
$$c(S, T) = \sum_{u \in S, v \in T, (u, v) \in E} c(u, v)$$

Das Problem des **Minimum $s-t$ Cut** besteht darin, eine Partition $(S, T)$ zu finden, die $c(S, T)$ minimiert.

## 2. Algebraische Charakterisierung

Die Korrektheit des Algorithmus beruht auf dem **Max-Flow Min-Cut Theorem**, welches besagt, dass der Wert des maximalen Flusses $|f|$ gleich der Kapazität des minimalen $s-t$ cuts ist.

### Residualgraph
Gegeben ein Fluss $f$, ist die Restkapazität $c_f(u, v)$ für jedes Paar $(u, v) \in V \times V$ definiert als:
$$c_f(u, v) = \begin{cases} c(u, v) - f(u, v) & \text{if } (u, v) \in E \\ f(v, u) & \text{if } (v, u) \in E \\ 0 & \text{otherwise} \end{cases}$$
Der Residualgraph $G_f = (V, E_f)$ besteht aus Kanten mit $c_f(u, v) > 0$.

### Erreichbarkeit und Schnittidentifikation
Sei $f^*$ ein maximaler Fluss. Sei $S \subseteq V$ die Menge der Knoten, die von $s$ aus im Residualgraphen $G_{f^*}$ über Pfade mit strikt positiver Restkapazität erreichbar sind:
$$S = \{v \in V \mid \exists \text{ a path from } s \text{ to } v \text{ in } G_{f^*}\}$$
Per Definition gilt $s \in S$. Da $f^*$ ein maximaler Fluss ist, existiert kein augmentierender Pfad von $s$ nach $t$ in $G_{f^*}$, was impliziert, dass $t \notin S$. Somit bildet $(S, V \setminus S)$ einen $s-t$ cut.

Für jede Kante $(u, v) \in E$, bei der $u \in S$ und $v \notin S$ gilt:
1. $f^*(u, v) = c(u, v)$ (Die Kante ist gesättigt).
2. $f^*(v, u) = 0$ (Wäre $f^*(v, u) > 0$, dann wäre $u$ von $v$ aus in $G_{f^*}$ erreichbar, was $v \notin S$ widersprechen würde).

Folglich ist die Kapazität des Schnitts:
$$c(S, V \setminus S) = \sum_{u \in S, v \notin S} f^*(u, v) = |f^*|$$
Dies bestätigt, dass die Menge der Kanten $E_{cut} = \{(u, v) \in E \mid u \in S, v \notin S\}$ ein Minimum $s-t$ cut ist.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus besteht aus zwei Phasen:
1. **Max-Flow-Berechnung:** Sei $T_{maxflow}(V, E)$ die Zeitkomplexität des gewählten Max-Flow-Algorithmus. Für Edmonds-Karp gilt $T_{maxflow} = O(VE^2)$.
2. **Erreichbarkeitsanalyse:** Die Konstruktion der Menge $S$ mittels Breadth-First Search (BFS) oder Depth-First Search (DFS) auf dem Residualgraphen $G_{f^*}$ erfordert, dass jeder Knoten und jede Kante höchstens einmal besucht wird, was zu einer Zeitkomplexität von $O(V + E)$ führt.
3. **Schnittidentifikation:** Das Iterieren über die Kantenmenge $E$, um Kanten $(u, v)$ zu identifizieren, bei denen $u \in S$ und $v \notin S$ gilt, benötigt $O(E)$ Zeit.

Die gesamte Zeitkomplexität beträgt:
$$T(V, E) = O(T_{maxflow}(V, E) + V + E) = O(T_{maxflow}(V, E))$$

### Platzkomplexität
1. **Residualgraph:** Das Speichern der Kapazitätsmatrix erfordert $O(V^2)$ Platz.
2. **Hilfsstrukturen:** Das `parent`-Array, das `visited`-Array und die `reachable`-Menge erfordern jeweils $O(V)$ Platz.
3. **Gesamter Platzbedarf:** Die Platzkomplexität wird durch die Kapazitätsmatrix dominiert, was $O(V^2)$ ergibt.