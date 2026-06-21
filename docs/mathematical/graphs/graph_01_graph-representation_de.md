# Formale mathematische Spezifikation: Graphrepräsentationen

## 1. Definitionen und Notation

Sei $G = (V, E)$ ein ungerichteter Graph, wobei $V = \{0, 1, \dots, n-1\}$ eine endliche Menge von $n$ Knoten ist und $E \subseteq \{\{u, v\} : u, v \in V, u \neq v\}$ eine Menge von $m$ Kanten darstellt.

*   **Eingabebereich:** Die Eingabe ist definiert durch das Tupel $(n, \mathcal{E})$, wobei $n = |V| \in \mathbb{N}$ und $\mathcal{E} = \{e_1, e_2, \dots, e_m\}$ eine Sequenz von Kanten ist, sodass $e_i = (u_i, v_i) \in V \times V$ gilt.
*   **Adjacency Matrix Repräsentation:** Eine Abbildung $M: V \times V \to \{0, 1\}$, definiert als:
    $$M_{uv} = \begin{cases} 1 & \text{falls } \{u, v\} \in E \\ 0 & \text{sonst} \end{cases}$$
*   **Adjacency List Repräsentation:** Eine Abbildung $A: V \to \mathcal{P}(V)$, wobei $\mathcal{P}(V)$ die Potenzmenge von $V$ bezeichnet, definiert als:
    $$A(u) = \{v \in V : \{u, v\} \in E\}$$
    Die Repräsentation ist die Sammlung der Mengen $\{A(u) : u \in V\}$.

## 2. Algebraische Charakterisierung

Die Konstruktion der Graphrepräsentation ist eine Transformation von der Kantenmenge $\mathcal{E}$ in die strukturellen Abbildungen $M$ oder $A$.

**Konstruktion der Adjacency Matrix:**
Die Matrix $M$ wird als Nullmatrix $0_{n \times n}$ initialisiert. Für jede Kante $(u, v) \in \mathcal{E}$ lautet der Zustandsübergang:
$$M_{uv}^{(k)} = M_{vu}^{(k)} = 1$$
wobei $M^{(k)}$ den Zustand nach der Verarbeitung der $k$-ten Kante bezeichnet. Der Endzustand ist $M = \sum_{i=1}^m \delta_i$, wobei $\delta_i$ die Indikatormatrix für die Kante $e_i$ ist.

**Konstruktion der Adjacency List:**
Die Adjacency List ist durch die Vereinigung von Singleton-Mengen definiert. Sei $A_0(u) = \emptyset$ für alle $u \in V$. Für jede Kante $(u, v) \in \mathcal{E}$ lautet die Aktualisierungsregel:
$$A_{k}(u) = A_{k-1}(u) \cup \{v\}$$
$$A_{k}(v) = A_{k-1}(v) \cup \{u\}$$
Die Korrektheit der Repräsentation wird durch die Invariante garantiert, dass zum Schritt $k=m$ die Menge $A(u)$ exakt die Menge der zu $u$ benachbarten Knoten in $G$ enthält.

## 3. Komplexitätsanalyse

### Zeitkomplexität
*   **Adjacency Matrix:** Die Initialisierung erfordert das Füllen von $n^2$ Zellen, was $\Theta(n^2)$ ergibt. Die Verarbeitung von $m$ Kanten erfordert $O(m)$ Operationen. Die gesamte Zeitkomplexität beträgt $T(n, m) = \Theta(n^2 + m)$.
*   **Adjacency List:** Die Initialisierung der Hash Map oder des Array der Größe $n$ benötigt $\Theta(n)$. Das Einfügen von $m$ Kanten in Mengen (oder Listen) benötigt $O(m)$ Zeit, unter der Annahme von Einfügeoperationen in konstanter Zeit. Die gesamte Zeitkomplexität beträgt $T(n, m) = \Theta(n + m)$.

### Platzkomplexität
*   **Adjacency Matrix:** Der benötigte Speicherplatz wird strikt durch die Dimensionen der Matrix bestimmt, $S(n) = \Theta(n^2)$.
*   **Adjacency List:** Der benötigte Speicherplatz ist proportional zur Anzahl der Knoten und der Summe der Grade aller Knoten. Nach dem Handschlag-Lemma gilt $\sum_{v \in V} \text{deg}(v) = 2m$. Somit ergibt sich die Platzkomplexität zu:
    $$S(n, m) = \Theta\left(n + \sum_{v \in V} \text{deg}(v)\right) = \Theta(n + m)$$
    Dies zeigt, dass für dünn besetzte Graphen (sparse graphs), bei denen $m \ll n^2$ gilt, die Adjacency List hinsichtlich der Speicherausnutzung asymptotisch überlegen ist.