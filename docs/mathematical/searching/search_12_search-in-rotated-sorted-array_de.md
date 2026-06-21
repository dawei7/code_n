# Formale Mathematische Spezifikation: Suche in einem rotierten sortierten Array

## 1. Definitionen und Notation

Sei $A = [a_0, a_1, \dots, a_{n-1}]$ ein Array von $n$ verschiedenen ganzen Zahlen. Wir definieren $A$ als ein **rotiertes sortiertes Array**, wenn ein Pivot-Index $k \in \{0, 1, \dots, n-1\}$ existiert, sodass die Sequenz $S = [s_0, s_1, \dots, s_{n-1}]$ streng monoton steigend ist (d.h. $s_i < s_{i+1}$ für alle $0 \le i < n-1$), und die Elemente von $A$ eine zyklische Verschiebung von $S$ um $k$ Positionen sind:
$$a_i = s_{(i-k) \pmod n}$$

*   **Eingabe:** Ein rotiertes sortiertes Array $A$ der Länge $n$ und ein Zielwert $\tau \in \mathbb{Z}$.
*   **Ausgabe:** Ein Index $idx \in \{0, 1, \dots, n-1\}$ sodass $a_{idx} = \tau$, oder $-1$ falls $\tau \notin A$.
*   **Zustandsraum:** Der Algorithmus verwaltet ein Suchintervall, das durch die Indizes $[L, R]$ definiert ist, wobei $0 \le L \le R < n$.

## 2. Algebraische Charakterisierung

Die Korrektheit des Algorithmus beruht auf der **Eigenschaft der sortierten Hälfte**. Für jeden Mittelpunkt $M = \lfloor \frac{L+R}{2} \rfloor$ wird das Teilstück $A[L \dots R]$ in zwei Segmente unterteilt: $A[L \dots M]$ und $A[M+1 \dots R]$. 

**Lemma (Invariante der sortierten Hälfte):** In jedem rotierten sortierten Array ist mindestens eines der beiden Segmente $[L, M]$ oder $[M+1, R]$ monoton steigend.
*   Wenn $a_L \le a_M$, dann ist das Segment $A[L \dots M]$ sortiert.
*   Andernfalls muss das Segment $A[M+1 \dots R]$ sortiert sein.

**Entscheidungslogik:**
Sei $S_L$ das Prädikat, dass $A[L \dots M]$ sortiert ist, definiert als $a_L \le a_M$.
1. Wenn $S_L$ wahr ist:
   - Wenn $a_L \le \tau < a_M$, ist der Zielwert $\tau$ in $[L, M-1]$ enthalten.
   - Andernfalls muss $\tau$ in $[M+1, R]$ liegen.
2. Wenn $S_L$ falsch ist (was impliziert, dass $A[M+1 \dots R]$ sortiert ist):
   - Wenn $a_{M+1} \le \tau \le a_R$, ist der Zielwert $\tau$ in $[M+1, R]$ enthalten.
   - Andernfalls muss $\tau$ in $[L, M-1]$ liegen.

Diese Logik bewahrt die Invariante, dass, wenn $\tau \in A$, dann $\tau \in A[L \dots R]$ zu Beginn jeder Iteration.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus verwendet eine Divide-and-Conquer-Strategie, die den Suchraum in jeder Iteration um den Faktor 2 reduziert. Sei $T(n)$ die Anzahl der Vergleiche, die für ein Array der Größe $n$ erforderlich sind.

Die Rekursionsgleichung ist:
$$T(n) = T\left(\frac{n}{2}\right) + c$$
wobei $c$ die konstante Zeit ist, die für die Vergleichslogik in jedem Schritt benötigt wird. Nach dem Master-Theorem, wobei $a=1, b=2, f(n)=O(1)$, erhalten wir:
$$T(n) = \Theta(\log n)$$
Somit beträgt die Zeitkomplexität $O(\log n)$.

### Platzkomplexität
Der Algorithmus arbeitet in-place. Wir definieren den Hilfs-Platzbedarf $S_{aux}$ als den Speicher, der über das Eingabe-Array hinaus benötigt wird. Der Algorithmus verwendet eine feste Anzahl von Integer-Variablen ($L, R, M, \text{pivot}$), die jeweils $O(1)$ Platz benötigen. 
$$S_{aux} = O(1)$$
Da kein Rekursions-Stack oder Hilfs-Datenstrukturen verwendet werden, beträgt die Gesamt-Platzkomplexität $O(1)$.