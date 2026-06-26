# Formale mathematische Spezifikation: Median zweier sortierter Arrays

## 1. Definitionen und Notation

Seien $A = \{a_0, a_1, \dots, a_{m-1}\}$ und $B = \{b_0, b_1, \dots, b_{n-1}\}$ zwei Folgen reeller Zahlen, sodass $a_i \le a_{i+1}$ für alle $0 \le i < m-1$ und $b_j \le b_{j+1}$ für alle $0 \le j < n-1$ gilt. Ohne Beschränkung der Allgemeinheit nehmen wir an, dass $m \le n$ gilt.

Sei $S = A \cup B$ die Multimengen-Vereinigung von $A$ und $B$, wobei $|S| = N = m + n$ ist. Der Median $\mu$ von $S$ ist definiert als:
- Wenn $N$ ungerade ist: $\mu = \text{select}(S, \lceil N/2 \rceil)$, wobei $\text{select}$ das $k$-te kleinste Element zurückgibt.
- Wenn $N$ gerade ist: $\mu = \frac{1}{2} (\text{select}(S, N/2) + \text{select}(S, N/2 + 1))$.

Wir definieren einen Partitionsindex $i \in \{0, \dots, m\}$ für $A$ und $j \in \{0, \dots, n\}$ für $B$. Diese Indizes definieren die linken und rechten Teilmengen:
$L_A = \{a_k \mid k < i\}, R_A = \{a_k \mid k \ge i\}$
$L_B = \{b_k \mid k < j\}, R_B = \{b_k \mid k \ge j\}$

## 2. Algebraische Charakterisierung

Das Ziel ist es, eine Partition $(i, j)$ zu finden, sodass die Vereinigung der linken Partitionen $L = L_A \cup L_B$ und der rechten Partitionen $R = R_A \cup R_B$ die folgenden Bedingungen erfüllt:

1. **Kardinalitätsbedingung:** $|L| = \lfloor \frac{m+n+1}{2} \rfloor$. Bei gegebenem $i$ ist $j$ eindeutig bestimmt als $j = \lfloor \frac{m+n+1}{2} \rfloor - i$.
2. **Randbedingung:** Jedes Element in $L$ muss kleiner oder gleich jedem Element in $R$ sein. Formal:
   $$\max(L_A \cup L_B) \le \min(R_A \cup R_B)$$
   
   Definition der Randwerte (mit $\pm \infty$ als Platzhalter für leere Mengen):
   - $\text{maxLeft}_A = a_{i-1}$ (falls $i>0$, sonst $-\infty$)
   - $\text{maxLeft}_B = b_{j-1}$ (falls $j>0$, sonst $-\infty$)
   - $\text{minRight}_A = a_i$ (falls $i<m$, sonst $+\infty$)
   - $\text{minRight}_B = b_j$ (falls $j<n$, sonst $+\infty$)

Die Partition ist genau dann gültig, wenn:
$$\text{maxLeft}_A \le \text{minRight}_B \quad \land \quad \text{maxLeft}_B \le \text{minRight}_A$$

Wenn $\text{maxLeft}_A > \text{minRight}_B$, dann ist $i$ zu groß; wir müssen $i$ verringern. Wenn $\text{maxLeft}_B > \text{minRight}_A$, dann ist $i$ zu klein; wir müssen $i$ erhöhen. Diese Monotonie ermöglicht eine binäre Suche über den Bereich $i \in [0, m]$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus führt eine binäre Suche über den Index $i \in [0, m]$ durch. In jeder Iteration der binären Suche führen wir eine konstante Anzahl an Vergleichen und arithmetischen Operationen durch, $O(1)$. 

Der Suchraum wird in jedem Schritt halbiert:
$$T(m) = T(m/2) + O(1)$$
Nach dem Master-Theorem, wobei $a=1, b=2, f(n)=O(1)$, erhalten wir $T(m) = \Theta(\log m)$. Da wir durch gegebenenfalls notwendiges Vertauschen sicherstellen, dass $m \le n$ gilt, ergibt sich die Komplexität zu:
$$T(m, n) = O(\log(\min(m, n)))$$

### Platzkomplexität
Der Algorithmus verwaltet eine feste Menge an skalaren Variablen ($i, j, \text{lo}, \text{hi}, \text{half}, \text{left\_max}, \text{right\_min}$), unabhängig von der Eingabegröße $m$ und $n$. Es werden keine zusätzlichen Datenstrukturen (wie Arrays oder Rekursions-Stacks) allokiert, die mit der Eingabegröße skalieren. Somit ist die zusätzliche Platzkomplexität:
$$S(m, n) = O(1)$$