# Formale mathematische Spezifikation: Intro Sort (Introspective Sort)

## 1. Definitionen und Notation

Es sei $A = [a_0, a_1, \dots, a_{n-1}]$ eine Sequenz von $n$ Elementen aus einer total geordneten Menge $(\mathcal{X}, \le)$. Das Ziel ist es, eine Permutation $A'$ von $A$ zu erzeugen, sodass $a'_0 \le a'_1 \le \dots \le a'_{n-1}$ gilt.

*   **Zustandsraum:** Der Algorithmus operiert auf der Menge aller Permutationen von $A$, bezeichnet als $\mathcal{S}_n$.
*   **Tiefenbegrenzung:** Es sei $d_{max} = 2 \lfloor \log_2 n \rfloor$ die maximal zulässige Rekursionstiefe für die Quicksort-Komponente.
*   **Partitionsfunktion:** Es sei $P(A, lo, hi)$ eine Funktion, die ein Pivot-Element $p \in A[lo \dots hi-1]$ auswählt und das Teil-Array so umordnet, dass $\forall x \in A[lo \dots p_{idx}-1], x \le A[p_{idx}]$ und $\forall y \in A[p_{idx}+1 \dots hi-1], y \ge A[p_{idx}]$ gilt.
*   **Heapify/Sift-Down:** Es sei $H(A, lo, hi)$ die Transformation, welche die Max-Heap-Eigenschaft $\forall i \in [lo, hi-1]: A[i] \ge A[2i+1]$ und $A[i] \ge A[2i+2]$ (relativ zum Offset $lo$) erfüllt.

## 2. Algebraische Charakterisierung

Intro Sort ist als rekursive Prozedur $I(lo, hi, d)$ definiert, wobei $d$ die verbleibende Rekursionstiefe darstellt. Der Algorithmus wird durch die folgende stückweise Übergangslogik gesteuert:

$$
I(lo, hi, d) = 
\begin{cases} 
\text{InsertionSort}(A, lo, hi) & \text{if } (hi - lo) < k \\
\text{HeapSort}(A, lo, hi) & \text{if } d = 0 \\
\text{let } p = P(A, lo, hi) \text{ in } \{I(lo, p, d-1); I(p+1, hi, d-1)\} & \text{otherwise}
\end{cases}
$$

Wobei $k$ eine kleine Konstante (typischerweise $16$) ist. 

**Invarianten:**
1. **Partitionsinvariante:** Nach der Ausführung von $P(A, lo, hi)$ befindet sich das Pivot-Element an seiner endgültigen sortierten Position $p_{idx}$.
2. **Heap-Invariante:** Nach $\text{HeapSort}(A, lo, hi)$ erfüllt das Teil-Array $A[lo \dots hi-1]$ die Bedingung $a_i \le a_j$ für alle $lo \le i < j < hi$.
3. **Terminierungsinvariante:** Da $d$ im rekursiven Zweig streng monoton fallend ist und $d_{max} \ge 0$ gilt, ist die Rekursionstiefe durch $2 \log_2 n$ beschränkt, was sicherstellt, dass die Stack-Tiefe $O(\log n)$ beträgt.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität $T(n)$ ist die Summe der Kosten der drei beteiligten Algorithmen. 

1. **Quicksort-Phase:** Im durchschnittlichen Fall hat der Rekursionsbaum eine Tiefe von $\log_2 n$. Jede Ebene verrichtet $O(n)$ Arbeit, was $O(n \log n)$ ergibt.
2. **Heap-Sort-Bailout:** Wenn die Rekursionstiefe $d_{max} = 2 \log_2 n$ überschreitet, ruft der Algorithmus Heap Sort auf. Heap Sort hat im schlechtesten Fall eine Komplexität von $T_{heap}(m) = O(m \log m)$ für ein Teil-Array der Größe $m$. 
3. **Gesamtkomplexität:** Da die Tiefenbegrenzung $d_{max}$ sicherstellt, dass der Quicksort-Rekursionsbaum eine Tiefe von $O(\log n)$ nicht überschreiten kann, und die Gesamtzahl der von Heap Sort über alle Zweige hinweg verarbeiteten Elemente durch $n$ beschränkt ist, beträgt die gesamte Zeitkomplexität:
   $$T(n) = \sum_{i=1}^{k} O(n_i \log n_i) \implies O(n \log n)$$
   wobei $\sum n_i = n$ gilt. Da $O(n \log n)$ die obere Schranke sowohl für die Quicksort-Phase (wenn balanciert) als auch für die Heap-Sort-Phase (wenn unbalanciert) ist, ist die Zeitkomplexität im schlechtesten Fall strikt $O(n \log n)$.

### Platzkomplexität
Die Platzkomplexität $S(n)$ wird durch den Rekursions-Stack und den Hilfsspeicher dominiert.

1. **Hilfsspeicher (Auxiliary Space):** Der Algorithmus arbeitet in-place und benötigt $O(1)$ Hilfsspeicher für Vertauschungen und Pointer.
2. **Stack-Speicher:** Die Rekursionstiefe ist explizit auf $d_{max} = 2 \log_2 n$ begrenzt. Jeder Stack-Frame belegt $O(1)$ Speicherplatz. Somit beträgt der gesamte Stack-Speicher:
   $$S_{stack} = O(d_{max}) = O(\log n)$$
3. **Gesamte Platzkomplexität:**
   $$S(n) = S_{aux} + S_{stack} = O(1) + O(\log n) = O(\log n)$$
Dies erfüllt die Anforderung an eine logarithmische Platzkomplexität und unterscheidet ihn von Merge Sort, welches $O(n)$ Speicherplatz benötigt.