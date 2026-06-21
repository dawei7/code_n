# Formale mathematische Spezifikation: Exponential Search (Galloping Search)

## 1. Definitionen und Notation

Sei $A$ eine sortierte Sequenz von Elementen $A = \{a_0, a_1, a_2, \dots, a_{n-1}\}$, wobei $a_i \in \mathcal{D}$ und $\mathcal{D}$ eine total geordnete Menge ist. Wir definieren das Suchproblem als das Finden eines Index $k \in \{0, 1, \dots, n-1\}$, sodass $a_k = \tau$, wobei $\tau \in \mathcal{D}$ der Zielwert ist. Falls kein solches $k$ existiert, gibt der Algorithmus $\perp$ (undefiniert/null) zurück.

- **Eingabebereich:** Ein sortiertes Array $A$ der Länge $n \in \mathbb{N}_0$ und ein Zielwert $\tau$.
- **Zustandsraum:** Der Suchraum ist durch das Intervall $[L, R] \subseteq \mathbb{N}_0$ definiert.
- **Galloping-Variable:** Sei $b_j$ die Schranke in Iteration $j$, wobei $b_0 = 1$ und $b_j = 2^j$.
- **Ausgabe:** Der Index $k = \text{argmin}_{i} \{a_i = \tau\}$ oder $\perp$, falls $\forall i, a_i \neq \tau$.

## 2. Algebraische Charakterisierung

Der Algorithmus verläuft in zwei distinkten Phasen, die durch die folgende Logik gesteuert werden:

### Phase I: Exponential Galloping
Wir suchen die kleinste ganze Zahl $j$, sodass $a_{2^j} \ge \tau$ oder $2^j \ge n$. Sei $b$ die kleinste Zweierpotenz, für die $b \ge \text{index}(\tau)$ gilt. Die während der Galloping-Phase aufrechterhaltene Invariante lautet:
$$\forall i < \frac{b}{2}, a_i < \tau$$
Die Phase endet beim ersten $b = 2^j$, für das $b \ge n$ oder $a_b \ge \tau$ gilt. Dies legt das Suchintervall $I = [\frac{b}{2}, \min(b, n-1)]$ fest.

### Phase II: Binary Search
Gegeben das Intervall $I = [L, R]$ mit $L = \frac{b}{2}$ und $R = \min(b, n-1)$, wenden wir das Prädikat der Binary Search an. Sei $m = \lfloor \frac{L+R}{2} \rfloor$. Die Übergangsfunktion lautet:
$$f(L, R, \tau) = \begin{cases} 
m & \text{falls } a_m = \tau \\
f(m+1, R, \tau) & \text{falls } a_m < \tau \\
f(L, m-1, \tau) & \text{falls } a_m > \tau 
\end{cases}$$
Die Korrektheit wird durch die Monotonie von $A$ garantiert, welche sicherstellt, dass $\tau \in [L, R]$ gilt, sofern $\tau \in A$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Sei $i$ der Index, für den $a_i = \tau$ gilt.

1. **Galloping-Phase:** Die Schleife terminiert, wenn $2^j \ge i$. Die Anzahl der Iterationen $j$ erfüllt $2^j \approx i$, folglich $j \approx \log_2 i$. Der Arbeitsaufwand beträgt $O(\log i)$.
2. **Binary-Search-Phase:** Das Suchintervall hat die Länge $R - L \approx 2^j - 2^{j-1} = 2^{j-1} \approx \frac{i}{2}$. Die Anzahl der Vergleiche in der Binary Search beträgt $\log_2(\text{Länge des Intervalls}) = \log_2(\frac{i}{2}) = \log_2 i - 1$.

Die gesamte Zeitkomplexität $T(i)$ ist die Summe der beiden Phasen:
$$T(i) = O(\log i) + O(\log i - 1) = O(\log i)$$
Im Schlechtesten Fall, bei dem $i = n-1$, beträgt die Komplexität $O(\log n)$.

### Platzkomplexität
Der Algorithmus verwendet eine konstante Anzahl an skalaren Variablen ($bound, low, high, mid$). Es werden keine zusätzlichen Datenstrukturen allokiert, die mit der Eingabegröße $n$ skalieren.

Die zusätzliche Platzkomplexität beträgt:
$$S(n) = O(1)$$
Die gesamte Platzkomplexität, einschließlich des Speichers für die Eingabe, beträgt $O(n)$, jedoch arbeitet der Algorithmus selbst mit $O(1)$ zusätzlichem Speicherplatz.