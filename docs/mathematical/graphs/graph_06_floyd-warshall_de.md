# Formale mathematische Spezifikation: Floyd-Warshall (All-Pairs Shortest Path)

## 1. Definitionen und Notation

Sei $G = (V, E)$ ein gerichteter, gewichteter Graph, wobei $V = \{v_1, v_2, \dots, v_n\}$ die Menge der $n$ Knoten und $E \subseteq V \times V$ die Menge der Kanten ist. Wir definieren eine Gewichtsfunktion $w: E \to \mathbb{R}$, die jeder Kante ein reellwertiges Gewicht zuweist.

Wir repräsentieren den Graphen mittels einer Adjacency Matrix $W \in (\mathbb{R} \cup \{\infty\})^{n \times n}$, wobei:
$$W_{ij} = \begin{cases} 0 & \text{if } i = j \\ w(v_i, v_j) & \text{if } (v_i, v_j) \in E \\ \infty & \text{if } (v_i, v_j) \notin E \text{ and } i \neq j \end{cases}$$

Das Ziel ist die Berechnung der Distanzmatrix $D^{(n)} \in (\mathbb{R} \cup \{\infty\})^{n \times n}$, wobei $D^{(n)}_{ij}$ das Gewicht des kürzesten Pfades vom Knoten $v_i$ zum Knoten $v_j$ bezeichnet. Ein Pfad $p = \langle v_{i_0}, v_{i_1}, \dots, v_{i_k} \rangle$ hat das Gewicht $w(p) = \sum_{m=1}^k w(v_{i_{m-1}}, v_{i_m})$.

## 2. Algebraische Charakterisierung

Der Floyd-Warshall-Algorithmus ist ein Ansatz der dynamischen Programmierung, der die Matrix der kürzesten Pfade konstruiert, indem er schrittweise eine größere Menge an Knoten als Zwischenknoten zulässt.

Sei $D^{(k)}_{ij}$ das Gewicht des kürzesten Pfades von $v_i$ nach $v_j$, sodass alle Zwischenknoten im Pfad aus der Menge $\{v_1, v_2, \dots, v_k\}$ gewählt werden.

**Induktionsanfang:**
Für $k=0$ sind keine Zwischenknoten erlaubt. Somit gilt $D^{(0)}_{ij} = W_{ij}$.

**Rekurrenz:**
Für $k \in \{1, \dots, n\}$ ist der kürzeste Pfad von $v_i$ nach $v_j$ unter Verwendung von Zwischenknoten aus $\{v_1, \dots, v_k\}$ entweder:
1. Der kürzeste Pfad unter Verwendung von Knoten aus $\{v_1, \dots, v_{k-1}\}$ (d. h. $D^{(k-1)}_{ij}$).
2. Ein Pfad, der durch den Knoten $v_k$ verläuft, zusammengesetzt aus dem kürzesten Pfad von $v_i$ nach $v_k$ und dem kürzesten Pfad von $v_k$ nach $v_j$, wobei beide nur Zwischenknoten aus $\{v_1, \dots, v_{k-1}\}$ verwenden.

Formal:
$$D^{(k)}_{ij} = \min(D^{(k-1)}_{ij}, D^{(k-1)}_{ik} + D^{(k-1)}_{kj})$$

**Korrektheitsinvariante:**
Nach $n$ Iterationen repräsentiert $D^{(n)}_{ij}$ den kürzesten Pfad zwischen $v_i$ und $v_j$ unter Verwendung einer beliebigen Teilmenge von $V$ als Zwischenknoten. Falls $D^{(n)}_{ii} < 0$ für ein beliebiges $i$ gilt, enthält der Graph einen negativen Zyklus, der von $v_i$ aus erreichbar ist.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus besteht aus drei verschachtelten Schleifen, die jeweils über die Menge der Knoten $V$ iterieren. Die Struktur ist wie folgt:
$$T(n) = \sum_{k=1}^{n} \sum_{i=1}^{n} \sum_{j=1}^{n} \Theta(1)$$
Da jede Iteration der innersten Schleife eine konstante Anzahl an Operationen (einen Vergleich und eine Addition) durchführt, ist die Gesamtzahl der Operationen:
$$T(n) = \sum_{k=1}^{n} n^2 = n \cdot n^2 = n^3$$
Somit beträgt die Zeitkomplexität $\Theta(n^3)$.

### Platzkomplexität
Der Algorithmus verwaltet eine Distanzmatrix $D \in \mathbb{R}^{n \times n}$. Obwohl die Rekurrenz über $k$ Stufen ($D^{(0)}, \dots, D^{(n)}$) definiert ist, kann der Zustand in-place aktualisiert werden, da $D^{(k)}_{ik} = D^{(k-1)}_{ik}$ und $D^{(k)}_{kj} = D^{(k-1)}_{kj}$ gilt. Daher benötigen wir nur $O(n^2)$ Platz, um die aktuelle Distanzmatrix zu speichern. Falls eine Pfadrekonstruktion erforderlich ist, wird eine zusätzliche Vorgängermatrix $P \in V^{n \times n}$ gepflegt, die ebenfalls $O(n^2)$ Platz beansprucht. Die gesamte Platzkomplexität beträgt $\Theta(n^2)$.