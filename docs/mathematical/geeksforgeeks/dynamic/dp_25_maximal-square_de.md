# Formale mathematische Spezifikation: Maximales Quadrat

## 1. Definitionen und Notation

Seien $M$ und $N$ positive ganze Zahlen, die die Dimensionen einer binären Matrix $A \in \{0, 1\}^{M \times N}$ darstellen. Wir bezeichnen das Element in Zeile $i$ und Spalte $j$ als $A_{i,j}$, wobei $0 \le i < M$ und $0 \le j < N$ gilt.

Wir definieren den Zustandsraum $\mathcal{S}$ als eine Menge von Seitenlängen von Quadraten. Sei $f(i, j)$ eine Funktion $f: \{0, \dots, M-1\} \times \{0, \dots, N-1\} \to \mathbb{N}_0$, wobei $f(i, j)$ die Seitenlänge des größten quadratischen Teilmatrix-Quadrats von $A$ bezeichnet, dessen untere rechte Ecke am Index $(i, j)$ liegt.

Das Ziel ist die Berechnung des Flächeninhalts des maximalen Quadrats, definiert als:
$$\mathcal{A} = \left( \max_{0 \le i < M, 0 \le j < N} f(i, j) \right)^2$$

## 2. Algebraische Charakterisierung

Die Funktion $f(i, j)$ ist durch die folgende Rekursionsgleichung definiert:

**Induktionsanfang:**
Für die Randbedingungen, bei denen $i=0$ oder $j=0$ gilt:
$$f(i, j) = A_{i,j}$$

**Induktionsschritt:**
Für $i > 0$ und $j > 0$:
$$f(i, j) = \begin{cases} 
\min(f(i-1, j), f(i, j-1), f(i-1, j-1)) + 1 & \text{falls } A_{i,j} = 1 \\
0 & \text{falls } A_{i,j} = 0 
\end{cases}$$

**Korrektheitsinvariante:**
Die Rekursion gilt, da ein Quadrat der Seitenlänge $k > 1$, das bei $(i, j)$ endet, genau dann existiert, wenn Quadrate der Seitenlänge mindestens $k-1$ bei $(i-1, j)$, $(i, j-1)$ und $(i-1, j-1)$ enden. Der Wert $f(i, j)$ repräsentiert das größte $k$, sodass die Teilmatrix $A[i-k+1 \dots i][j-k+1 \dots j]$ vollständig aus Einsen besteht.

**Platzoptimierter Zustand:**
Um die Platzkomplexität zu reduzieren, definieren wir ein 1D-Array $D$ der Länge $N+1$. Sei $D^{(i)}_j$ der Wert von $f(i, j)$ in Zeile $i$. Der Übergang lautet:
$$D^{(i)}_j = \begin{cases} 
\min(D^{(i)}_j, D^{(i)}_{j-1}, \text{prev}) + 1 & \text{falls } A_{i,j} = 1 \\
0 & \text{falls } A_{i,j} = 0 
\end{cases}$$
wobei $\text{prev}$ den Wert von $f(i-1, j-1)$ vor der Aktualisierung von $D^{(i)}_j$ speichert.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus iteriert genau einmal über jede Zelle der $M \times N$ Matrix. Für jede Zelle $(i, j)$ führt der Algorithmus eine konstante Anzahl an Operationen aus: einen Vergleich, eine Minimum-Berechnung, eine Addition und eine Zuweisung.

Die gesamte Zeitkomplexität $T(M, N)$ ergibt sich aus der Summation:
$$T(M, N) = \sum_{i=1}^{M} \sum_{j=1}^{N} \Theta(1) = \Theta(M \cdot N)$$
Somit beträgt die Zeitkomplexität $O(M \cdot N)$.

### Platzkomplexität
Die naive Implementierung erfordert eine $M \times N$ Matrix, was zu einer Platzkomplexität von $O(M \cdot N)$ führt. Die optimierte Implementierung verwendet jedoch ein 1D-Array $D$ der Größe $N+1$ sowie eine skalare Variable $\text{prev}$, um den Zustand des diagonalen Elements $(i-1, j-1)$ beizubehalten.

Die zusätzliche Platzkomplexität $S(N)$ ist:
$$S(N) = \text{size}(D) + \text{size}(\text{prev}) = (N+1) \cdot \text{word\_size} + 1 \cdot \text{word\_size} = O(N)$$
Da die Eingabematrix bereits bereitgestellt ist, beträgt die zusätzliche Platzkomplexität $O(N)$, was die Anforderung erfüllt.