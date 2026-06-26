# Formale mathematische Spezifikation: Bipartite Graph-Prüfung

## 1. Definitionen und Notation

Sei $G = (V, E)$ ein ungerichteter Graph, wobei $V = \{v_1, v_2, \dots, v_n\}$ die Menge der Knoten und $E \subseteq \{\{u, v\} : u, v \in V, u \neq v\}$ die Menge der Kanten ist. Sei $n = |V|$ und $m = |E|$. Der Graph wird durch eine Adjacency List $Adj: V \to \mathcal{P}(V)$ repräsentiert, wobei $Adj(u) = \{v \in V : \{u, v\} \in E\}$.

Ein Graph $G$ ist **bipartit**, wenn eine Partition von $V$ in zwei disjunkte Mengen $U$ und $W$ existiert, sodass $V = U \cup W$, $U \cap W = \emptyset$ und für jede Kante $\{u, v\} \in E$ entweder ($u \in U$ und $v \in W$) oder ($u \in W$ und $v \in U$) gilt.

Wir definieren eine Färbungsfunktion $c: V \to \{0, 1, \perp\}$, wobei $\perp$ einen ungefärbten Zustand bezeichnet. Der Algorithmus versucht zu bestimmen, ob eine Funktion $c$ existiert, sodass für alle $\{u, v\} \in E$ gilt:
1. $c(u) \neq \perp$ und $c(v) \neq \perp$
2. $c(u) \neq c(v)$

## 2. Algebraische Charakterisierung

Die Korrektheit des Algorithmus beruht auf folgendem Theorem: *Ein Graph $G$ ist genau dann bipartit, wenn er keine Zyklen ungerader Länge enthält.*

### Schleifeninvariante
Sei $Q$ die Queue, die in der Breadth-First Search (BFS) verwendet wird, und $c_k$ der Färbungszustand nach $k$ Iterationen. Für jeden Knoten $v$ mit $c(v) \in \{0, 1\}$ gilt die folgende Invariante:
$$\forall u \in Adj(v), \text{ if } c(u) \neq \perp \implies c(u) = 1 - c(v)$$
Wenn zu einem beliebigen Schritt $k$ eine Kante $\{u, v\} \in E$ existiert, für die $c(u) = c(v) \neq \perp$ gilt, terminiert der Algorithmus und gibt $\text{False}$ zurück. Diese Bedingung impliziert die Existenz eines ungeraden Zyklus, da der Pfad von der Wurzel des BFS-Baums zu $u$ und $v$ zusammen mit der Kante $\{u, v\}$ einen Zyklus der Länge $d(root, u) + d(root, v) + 1$ bildet. Da $c(u) = c(v)$ gilt, müssen die Abstände $d(root, u)$ und $d(root, v)$ die gleiche Parität aufweisen, was die Zykluslänge zu $2k + 1$ macht, was ungerade ist.

### Zustandsübergang
Der Algorithmus führt eine Traversierung durch, bei der für einen aktuellen Knoten $u$ und einen Nachbarn $v$ gilt:
$$c(v) = \begin{cases} 1 - c(u) & \text{if } c(v) = \perp \\ c(v) & \text{if } c(v) \neq \perp \end{cases}$$
Der Algorithmus gibt $\text{False}$ zurück, falls $\exists \{u, v\} \in E$ mit $c(u) = c(v)$. Andernfalls gibt er $\text{True}$ zurück.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus besucht jeden Knoten $v \in V$ genau einmal und traversiert jede Kante $\{u, v\} \in E$ genau zweimal (einmal von $u$ und einmal von $v$).
Der Gesamtaufwand $T(n, m)$ lässt sich ausdrücken als:
$$T(n, m) = \sum_{v \in V} \Theta(1) + \sum_{v \in V} \sum_{u \in Adj(v)} \Theta(1)$$
Da $\sum_{v \in V} |Adj(v)| = 2m$ gilt, ist die Komplexität:
$$T(n, m) = \Theta(n + 2m) = O(V + E)$$
Dies ist optimal, da der Algorithmus jeden Knoten und jede Kante mindestens einmal untersuchen muss, um die Bipartit-Eigenschaft zu verifizieren.

### Platzkomplexität
Die Platzkomplexität $S(n)$ wird durch die für die Traversierung erforderlichen Hilfsstrukturen dominiert:
1. Das `colors` Array: $O(V)$, um den Zustand jedes Knotens zu speichern.
2. Die `queue` für BFS: Im Schlechtesten Fall (ein Stern-Graph) speichert die Queue $O(V)$ Knoten.
3. Die Adjacency List: $O(V + E)$, um den Graphen zu repräsentieren.

Unter Ausschluss der Speicherung des Eingabegraphen beträgt die zusätzliche Platzkomplexität:
$$S(n) = O(V)$$
Dies ist optimal für einen Graphentraversierungsalgorithmus, der eine Zustandsverfolgung für jeden Knoten erfordert.