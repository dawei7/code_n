# Formale mathematische Spezifikation: Zusammenführen zweier sortierter Linked Lists

## 1. Definitionen und Notation

Sei $\mathcal{L}$ die Menge aller einfach verketteten Linked Lists. Eine Linked List $L \in \mathcal{L}$ ist definiert als eine geordnete Sequenz von Knoten $N = (v, p)$, wobei $v \in \mathbb{R}$ der Wert und $p \in \mathcal{L} \cup \{\text{null}\}$ der Pointer auf den nachfolgenden Knoten ist.

Formal ist eine Liste $L$ der Länge $n$ eine Sequenz von Knoten $(n_0, n_1, \dots, n_{n-1})$, sodass für jedes $i \in \{0, \dots, n-2\}$ gilt: $n_i.next = n_{i+1}$ und $n_{n-1}.next = \text{null}$.

Wir definieren den Input als zwei sortierte Linked Lists:
- $L_1 = (a_0, a_1, \dots, a_{n-1})$ wobei $a_i.v \le a_{i+1}.v$ für alle $0 \le i < n-1$.
- $L_2 = (b_0, b_1, \dots, b_{m-1})$ wobei $b_j.v \le b_{j+1}.v$ für alle $0 \le j < m-1$.

Der Output ist eine Linked List $L_{merged} = (c_0, c_1, \dots, c_{n+m-1})$, sodass:
1. Die Menge der Knoten in $L_{merged}$ exakt die Vereinigung der Knotenmengen von $L_1$ und $L_2$ ist.
2. $c_k.v \le c_{k+1}.v$ für alle $0 \le k < n+m-1$.

## 2. Algebraische Charakterisierung

Der Algorithmus verwaltet einen Zustand, der durch das Tupel $(p_1, p_2, \text{tail})$ definiert ist, wobei $p_1$ und $p_2$ Pointer auf die aktuell betrachteten Knoten in $L_1$ und $L_2$ sind und $\text{tail}$ der letzte Knoten der konstruierten zusammengeführten Liste ist.

### Schleifeninvariante
Zu Beginn jeder Iteration des Zusammenführungsprozesses sei $S$ die Menge der Knoten, die bereits an die zusammengeführte Liste angehängt wurden. Die folgende Invariante gilt:
1. Die Knoten in $S$ sind sortiert: $\forall x, y \in S$, wenn $x$ in der zusammengeführten Liste vor $y$ steht, dann gilt $x.v \le y.v$.
2. Für jeden Knoten $x \in S$ und jeden Knoten $y \in \{p_1, p_2, \dots, \text{verbleibende Knoten von } L_1, L_2\}$ gilt $x.v \le y.v$.

### Übergangsfunktion
Der Zustandsübergang ist durch die Abbildung $f: (p_1, p_2) \to (p_1', p_2', \text{tail}')$ definiert:
$$
\text{tail}'.next = 
\begin{cases} 
p_1 & \text{falls } p_1.v \le p_2.v \\
p_2 & \text{sonst}
\end{cases}
$$
$$
(p_1', p_2') = 
\begin{cases} 
(p_1.next, p_2) & \text{falls } p_1.v \le p_2.v \\
(p_1, p_2.next) & \text{sonst}
\end{cases}
$$

Der Prozess terminiert, wenn $p_1 = \text{null}$ oder $p_2 = \text{null}$. Der letzte Schritt ist die Konkatenation des nicht-leeren Rests:
$$
\text{tail}_{final}.next = \begin{cases} p_1 & \text{falls } p_2 = \text{null} \\ p_2 & \text{falls } p_1 = \text{null} \end{cases}
$$

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus führt einen einzigen Durchlauf über die Knoten von $L_1$ und $L_2$ aus. Sei $T(n, m)$ die Anzahl der Operationen. In jeder Iteration der `while`-Schleife wird exakt ein Knoten an die zusammengeführte Liste angehängt und ein Pointer ($p_1$ oder $p_2$) weiterbewegt.

Die Gesamtzahl der Iterationen beträgt exakt $n + m$. Da jede Iteration eine konstante Anzahl an Pointer-Zuweisungen und Vergleichen beinhaltet, ist der Arbeitsaufwand pro Iteration $O(1)$. Somit gilt:
$$T(n, m) = \sum_{k=1}^{n+m} O(1) = O(n + m)$$
Die Zeitkomplexität ist $\Theta(n + m)$, da wir jeden Knoten mindestens einmal besuchen müssen, um die totale Ordnung herzustellen.

### Platzkomplexität
Der Algorithmus verwendet eine konstante Anzahl an zusätzlichen Pointern: `dummy`, `tail`, `p1` und `p2`.
- **Zusätzlicher Speicherplatz:** Der für diese Pointer benötigte Speicher ist unabhängig von der Inputgröße $n$ und $m$. Daher ist die zusätzliche Platzkomplexität $O(1)$.
- **Gesamter Speicherplatz:** Da der Algorithmus eine In-Place-Pointer-Umverkabelung (Splicing) durchführt und keine neuen Knoten instanziiert (mit Ausnahme des einzelnen `dummy`-Knotens), ist die gesamte Platzkomplexität $O(1)$ in Bezug auf die Input-Listen.