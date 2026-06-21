# Formale mathematische Spezifikation: Maximum Subarray Sum (Divide and Conquer)

## 1. Definitionen und Notation

Sei $A = [a_0, a_1, \dots, a_{n-1}]$ eine Sequenz von $n$ Ganzzahlen, wobei $a_i \in \mathbb{Z}$. 
Ein zusammenhängendes Subarray $A[i..j]$ ist definiert als die Sequenz $(a_i, a_{i+1}, \dots, a_j)$ für $0 \le i \le j < n$.
Die Summe eines Subarrays $A[i..j]$ ist gegeben durch die Funktion $S(i, j) = \sum_{k=i}^{j} a_k$.

Das Ziel ist es, die maximale Subarray-Summe, bezeichnet als $\mathcal{M}(A)$, zu finden, welche definiert ist als:
$$\mathcal{M}(A) = \max_{0 \le i \le j < n} S(i, j)$$

Wir definieren den Definitionsbereich der rekursiven Funktion $f(lo, hi)$ als die maximale Subarray-Summe innerhalb des Indexbereichs $[lo, hi] \subseteq \{0, \dots, n-1\}$. Der Zustandsraum $\mathcal{S}$ besteht aus allen gültigen Indexpaaren $(lo, hi)$, sodass $0 \le lo \le hi < n$.

## 2. Algebraische Charakterisierung

Der Algorithmus basiert auf dem Optimalitätsprinzip für Divide and Conquer. Für jeden Bereich $[lo, hi]$ sei $mid = \lfloor \frac{lo + hi}{2} \rfloor$. Die maximale Subarray-Summe $\mathcal{M}(lo, hi)$ muss die folgende Rekursionsgleichung erfüllen:

$$\mathcal{M}(lo, hi) = \begin{cases} a_{lo} & \text{falls } lo = hi \\ \max\left( \mathcal{M}(lo, mid), \mathcal{M}(mid+1, hi), \mathcal{C}(lo, mid, hi) \right) & \text{falls } lo < hi \end{cases}$$

Wobei $\mathcal{C}(lo, mid, hi)$ die maximale Crossing-Summe ist, definiert als die maximale Summe eines Subarrays, das sowohl $a_{mid}$ als auch $a_{mid+1}$ enthält:

$$\mathcal{C}(lo, mid, hi) = \left( \max_{lo \le i \le mid} \sum_{k=i}^{mid} a_k \right) + \left( \max_{mid+1 \le j \le hi} \sum_{k=mid+1}^{j} a_k \right)$$

Sei $L(lo, mid) = \max_{lo \le i \le mid} \sum_{k=i}^{mid} a_k$ und $R(mid+1, hi) = \max_{mid+1 \le j \le hi} \sum_{k=mid+1}^{j} a_k$. Diese Werte werden in $O(mid - lo + 1)$ bzw. $O(hi - mid)$ Zeit berechnet, wodurch sichergestellt wird, dass die Crossing-Summe in linearer Zeit relativ zur Größe des aktuellen Bereichs bestimmt wird.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus folgt einem Divide-and-Conquer-Paradigma. Sei $T(n)$ die Zeitkomplexität für eine Eingabe der Größe $n$. Die Rekursionsgleichung für den durchgeführten Aufwand lautet:
$$T(n) = 2T\left(\frac{n}{2}\right) + f(n)$$
wobei $f(n)$ den Aufwand darstellt, der zur Berechnung der Crossing-Summe $\mathcal{C}$ und des abschließenden Vergleichs erforderlich ist. Da die Crossing-Summe zwei lineare Durchläufe über den Bereich $[lo, hi]$ erfordert, gilt $f(n) = \Theta(n)$.

Unter Anwendung des **Master-Theorems** für Rekursionsgleichungen der Form $T(n) = aT(n/b) + \Theta(n^k)$:
- Hier ist $a=2, b=2, k=1$.
- Da $\log_b a = \log_2 2 = 1$ und $k = \log_b a$ gilt, fallen wir in Fall 2 des Master-Theorems.
- Daher ist $T(n) = \Theta(n^1 \log n) = O(n \log n)$.

### Platzkomplexität
Die Platzkomplexität wird durch die maximale Tiefe des Rekursionsbaums und den zusätzlichen Speicherbedarf in jedem Stack-Frame bestimmt.
1. **Rekursions-Stack:** Der Rekursionsbaum hat eine Tiefe von $\lceil \log_2 n \rceil$. Jeder Frame speichert eine konstante Anzahl an Variablen ($lo, hi, mid, left\_best, right\_best, s, left\_sum, right\_sum$). Somit beträgt der Stack-Platz $O(\log n)$.
2. **Zusätzlicher Speicher:** Der Algorithmus arbeitet in-place auf dem Eingabe-Array $A$. Es werden keine zusätzlichen Datenstrukturen proportional zu $n$ allokiert.

Folglich beträgt die gesamte Platzkomplexität $O(\log n)$.