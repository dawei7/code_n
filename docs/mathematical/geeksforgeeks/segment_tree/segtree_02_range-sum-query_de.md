# Formale Mathematische Spezifikation: Range Sum Query

## 1. Definitionen und Notation

Sei $A = [a_0, a_1, \dots, a_{n-1}]$ ein Array von Elementen, wobei $a_i \in \mathbb{R}$ (oder ein beliebiges additives Monoid). Ein Segment Tree $\mathcal{T}$ ist ein gewurzelter Binärbaum, wobei jeder Knoten $v$ einem geschlossenen Intervall $[tl, tr] \subseteq [0, n-1]$ entspricht.

*   **Zustandsraum:** Der Baum $\mathcal{T}$ ist durch eine Abbildung $f: V \to \mathbb{R}$ definiert, wobei $V$ die Menge der Knoten ist. Für einen Knoten $v$, der das Intervall $[tl, tr]$ abdeckt, ist der Wert $f(v)$ definiert als:
    $$f(v) = \sum_{i=tl}^{tr} a_i$$
*   **Query-Eingabe:** Eine Query ist durch ein Paar von Indizes $(l, r)$ definiert, sodass $0 \le l \le r \le n-1$.
*   **Query-Ausgabe:** Das Ziel ist es, die Funktion $Q(l, r) = \sum_{i=l}^{r} a_i$ zu berechnen.
*   **Neutrales Element:** Wir definieren das additive neutrale Element $e = 0$, sodass für jedes $x$ gilt: $x + e = x$.

## 2. Algebraische Charakterisierung

Die Query-Funktion $Q(v, tl, tr, l, r)$ ist rekursiv definiert, basierend auf der Schnittmenge des Intervalls des Knotens $[tl, tr]$ und des Query-Intervalls $[l, r]$. Sei $tm = \lfloor \frac{tl + tr}{2} \rfloor$. Die Rekursionsgleichung ist gegeben durch:

$$
Q(v, tl, tr, l, r) = 
\begin{cases} 
0 & \text{falls } [tl, tr] \cap [l, r] = \emptyset \\
f(v) & \text{falls } [tl, tr] \subseteq [l, r] \\
Q(2v, tl, tm, l, r) + Q(2v+1, tm+1, tr, l, r) & \text{andernfalls}
\end{cases}
$$

**Korrektheitsinvariante:**
Für jeden Knoten $v$, der das Intervall $[tl, tr]$ abdeckt, wird der Wert $f(v)$ als Invariante beibehalten:
$$f(v) = f(left\_child(v)) + f(right\_child(v))$$
Dies stellt sicher, dass die Summationseigenschaft über die Baumstruktur hinweg erhalten bleibt, was die Zerlegung des Bereichs $[l, r]$ in eine disjunkte Vereinigung kanonischer Knoten ermöglicht, deren Intervalle $[l, r]$ partitionieren.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität $T(n)$ wird durch die Anzahl der im Baum besuchten Knoten bestimmt.
Auf jeder Ebene des Baumes besuchen wir höchstens eine konstante Anzahl von Knoten. Insbesondere besucht der Algorithmus für jede Query $[l, r]$ höchstens 4 Knoten pro Ebene des Baumes.

Sei $H$ die Höhe des Baumes, wobei $H = \lceil \log_2 n \rceil$. Die Rekurrenz für die Anzahl der besuchten Knoten $W(n)$ ist:
$$W(n) \le 2W(n/2) + O(1)$$
Nach dem Master-Theorem (Fall 1), wobei $a=2, b=2, d=0$:
$$T(n) = O(n^{\log_2 2}) = O(n^0 \log n) = O(\log n)$$
Somit ist die Query-Operation streng durch $O(\log n)$ begrenzt.

### Platzkomplexität
*   **Speicherplatz für den Baum:** Der Segment Tree ist ein vollständiger Binärbaum (oder ein Heap-indiziertes Array), der $n$ Blätter repräsentiert. Die Anzahl der Knoten in einem vollständigen Binärbaum mit $n$ Blättern beträgt $2n - 1$. Bei Verwendung einer 1-indizierten Array-Darstellung benötigen wir ein Array der Größe $4n$, um die Baumstruktur aufzunehmen, was $O(n)$ Platz für die Datenstruktur ergibt.
*   **Hilfsspeicherplatz:** Die Rekursionstiefe entspricht der Höhe des Baumes, $H = \lceil \log_2 n \rceil$. Daher beträgt die Hilfsplatzkomplexität für den Aufruf-Stack $O(\log n)$.

Die Gesamtplatzkomplexität beträgt $O(n)$ für die Struktur und $O(\log n)$ für den Ausführungs-Stack.