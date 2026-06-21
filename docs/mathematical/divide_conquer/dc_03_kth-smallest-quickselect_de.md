# Formale mathematische Spezifikation: K-tes kleinstes Element (Quickselect)

## 1. Definitionen und Notation

Sei $A = [a_0, a_1, \dots, a_{n-1}]$ eine Sequenz von $n$ Elementen aus einer total geordneten Menge $(\mathcal{X}, \leq)$. Wir definieren das Problem als das Finden eines Elements $x \in A$, dessen Rang in der sortierten Permutation von $A$ gleich $k$ ist, wobei $1 \leq k \leq n$ gilt.

*   **Eingabe:** Ein Tupel $(A, k)$, wobei $A \in \mathcal{X}^n$ und $k \in \mathbb{Z}^+$.
*   **Ausgabe:** Ein Element $x^* \in A$, sodass $|\{a \in A : a < x^*\}| < k$ und $|\{a \in A : a \leq x^*\}| \geq k$ gilt.
*   **Partition-Funktion:** Sei $P(A, p)$ eine Funktion, die $A$ in $A'$ umordnet, sodass ein Index $m$ (die Pivot-Position) existiert, für den gilt:
    1. $\forall i < m, A'[i] \leq A'[m]$
    2. $\forall j > m, A'[j] \geq A'[m]$
    3. $A'[m]$ ist das Element, das ursprünglich am gewählten Pivot-Index stand.

## 2. Algebraische Charakterisierung

Der Algorithmus basiert auf der **Partition-Invariante**. Gegeben ein Subarray $A[lo \dots hi]$, erzeugt die Partition-Operation einen Pivot-Index $m \in [lo, hi]$, sodass $A[m]$ sich an seiner korrekten sortierten Position relativ zum Subarray befindet.

Der Algorithmus ist durch die folgende Rekursionsgleichung für die Selektionsfunktion $S(A, k, lo, hi)$ definiert:

$$
S(A, k, lo, hi) = 
\begin{cases} 
A[m] & \text{falls } m = k-1 \\
S(A, k, lo, m-1) & \text{falls } m > k-1 \\
S(A, k, m+1, hi) & \text{falls } m < k-1 
\end{cases}
$$

Hierbei ist $m$ der Index, der von der Partition-Operation auf dem Bereich $[lo, hi]$ zurückgegeben wird. Die Korrektheit wird durch die Tatsache garantiert, dass nach der Partitionierung die Menge der Elemente $\{A[lo], \dots, A[m-1]\}$ nur Elemente $\leq A[m]$ enthält und $\{A[m+1], \dots, A[hi]\}$ nur Elemente $\geq A[m]$ enthält. Somit ist der Rang von $A[m]$ über alle rekursiven Aufrufe hinweg invariant.

## 3. Komplexitätsanalyse

### Zeitkomplexität

Die Zeitkomplexität wird durch die Rekursionsgleichung $T(n) = T(n') + O(n)$ bestimmt, wobei $n'$ die Größe des Subarrays nach der Partitionierung ist.

**Durchschnittlicher Fall:**
Unter der Annahme eines zufälligen Pivots teilt die Partitionierung das Array in zwei Teile der erwarteten Größe $n/2$. Die Rekursionsgleichung lautet:
$$T(n) = T(n/2) + cn$$
Nach dem Master-Theorem (Fall 3) oder durch Entwicklung der geometrischen Reihe ergibt sich:
$$T(n) = cn + c\frac{n}{2} + c\frac{n}{4} + \dots + c(1) = cn \sum_{i=0}^{\log n} \left(\frac{1}{2}\right)^i < 2cn$$
Daraus folgt $T(n) = O(n)$.

**Schlechtester Fall:**
Wenn der Pivot konsistent das kleinste oder größte Element ist (z. B. bei einem bereits sortierten Array mit schlechter Pivot-Wahl), wird die Rekursionsgleichung zu:
$$T(n) = T(n-1) + cn$$
Dies ist eine arithmetische Reihe:
$$T(n) = \sum_{i=1}^{n} ci = c \frac{n(n+1)}{2} = O(n^2)$$

### Platzkomplexität

**Zusätzlicher Speicherplatz (Auxiliary Space):**
Der Algorithmus arbeitet in-place auf dem Eingabe-Array $A$. Der zusätzliche Speicherplatz wird durch die Tiefe des Rekursions-Stacks $D$ definiert.
*   Im durchschnittlichen Fall beträgt die Stack-Tiefe $O(\log n)$ aufgrund der Halbierung des Suchraums.
*   Im schlechtesten Fall beträgt die Stack-Tiefe $O(n)$.
*   Bei iterativer Implementierung (Tail-Call-Optimierung) beträgt die Platzkomplexität für den zusätzlichen Speicher $O(1)$, da der Zustand über zwei Pointer ($lo, hi$) ohne zusätzliche Stack-Frames verwaltet werden kann.

**Gesamtspeicherplatz:**
Da der Algorithmus das Eingabe-Array $A$ in-place modifiziert, beträgt die Gesamtspeicherkomplexität $O(n)$ für die Speicherung der Eingabe, wobei $O(1)$ zusätzlicher Speicher für die Partitionierungs-Variablen und Pointer benötigt wird.