# Formale Mathematische Spezifikation: Range Minimum Query

## 1. Definitionen und Notation

Sei $A = [a_0, a_1, \dots, a_{n-1}]$ ein Array von Elementen aus einer total geordneten Menge $(\mathcal{X}, \le)$, wobei $\mathcal{X} \subseteq \mathbb{R} \cup \{\infty\}$.

Ein **Segment Tree** $\mathcal{T}$ ist ein gewurzelter Binärbaum, wobei jeder Knoten $u$ einem geschlossenen Intervall $[lo, hi] \subseteq [0, n-1]$ entspricht. Der Baum ist rekursiv definiert:
- **Blattknoten:** Für jedes $i \in [0, n-1]$ existiert ein Blattknoten, der $[i, i]$ repräsentiert, sodass sein Wert $v(u) = a_i$ ist.
- **Innere Knoten:** Für einen Knoten $u$, der $[lo, hi]$ abdeckt, wobei $lo < hi$, sei $mid = \lfloor \frac{lo + hi}{2} \rfloor$. Knoten $u$ hat zwei Kinder: $u_{left}$, das $[lo, mid]$ abdeckt, und $u_{right}$, das $[mid+1, hi]$ abdeckt. Der Wert des Knotens ist durch die assoziative binäre Operation $\min: \mathcal{X} \times \mathcal{X} \to \mathcal{X}$ definiert:
  $$v(u) = \min(v(u_{left}), v(u_{right}))$$

Die **Range Minimum Query (RMQ)** ist eine Funktion $f: [0, n-1] \times [0, n-1] \to \mathcal{X}$, definiert als:
$$f(l, r) = \min_{i \in [l, r]} a_i$$
wobei $0 \le l \le r \le n-1$. Falls $l > r$, definieren wir $f(l, r) = \infty$, wobei $\infty$ das neutrale Element für die $\min$-Operation ist, sodass $\forall x \in \mathcal{X}, \min(x, \infty) = x$.

## 2. Algebraische Charakterisierung

Die Korrektheit des RMQ-Algorithmus beruht auf der Zerlegung des Query-Intervalls $[l, r]$ in eine Menge kanonischer Knoten in $\mathcal{T}$. Sei $Q(u, l, r)$ die rekursive Query-Funktion für einen Knoten $u$, der $[lo, hi]$ abdeckt:

$$Q(u, l, r) = 
\begin{cases} 
\infty & \text{if } [lo, hi] \cap [l, r] = \emptyset \\
v(u) & \text{if } [lo, hi] \subseteq [l, r] \\
\min(Q(u_{left}, l, r), Q(u_{right}, l, r)) & \text{otherwise}
\end{cases}$$

**Invariante:** Für jeden Knoten $u$, der $[lo, hi]$ abdeckt, erfüllt der Wert $v(u)$ die Invariante $v(u) = \min_{i \in [lo, hi]} a_i$. Aufgrund der Assoziativität und Kommutativität des $\min$-Operators zerlegt die rekursive Zerlegung das Intervall $[l, r]$ korrekt in höchstens $O(\log n)$ disjunkte kanonische Subintervalle, deren Vereinigung genau $[l, r]$ ist.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität $T(n)$ wird durch die Anzahl der während der Traversierung besuchten Knoten bestimmt.
Auf jeder Tiefe $d$ des Baumes schneidet der Query-Bereich $[l, r]$ höchstens 4 Knoten. Insbesondere kann der Query-Bereich auf jeder Ebene mit höchstens zwei Knoten (denjenigen, die $l$ und $r$ enthalten) teilweise überlappen, während alle Knoten, die sich strikt dazwischen befinden, entweder vollständig enthalten oder vollständig disjunkt sind.

Da die Höhe des Baumes $H = \lceil \log_2 n \rceil$ ist und wir eine konstante Anzahl von Knoten $c \le 4$ pro Ebene besuchen:
$$T(n) = \sum_{d=0}^{\lceil \log_2 n \rceil} c = O(\log n)$$
Somit ist die Query-Operation strikt $O(\log n)$.

### Platzkomplexität
- **Gesamtplatzbedarf:** Der Segment Tree ist ein vollständiger Binärbaum mit $n$ Blattknoten. Die Anzahl der inneren Knoten beträgt $n-1$, was zu insgesamt $2n-1$ Knoten führt. In einer Heap-indizierten Array-Repräsentation weisen wir $4n$ Platz zu, um die Baumstruktur aufzunehmen, was eine Platzkomplexität von $O(n)$ ergibt.
- **Zusätzlicher Platzbedarf:** Die Rekursionstiefe der `query`-Funktion ist durch die Höhe des Baumes $H = \lceil \log_2 n \rceil$ begrenzt. Daher beträgt die für den Call Stack benötigte zusätzliche Platzkomplexität $O(\log n)$.