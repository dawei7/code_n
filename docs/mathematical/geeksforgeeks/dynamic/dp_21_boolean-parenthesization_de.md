# Formale mathematische Spezifikation: Boolesche Klammerung

## 1. Definitionen und Notation

Sei die Eingabe ein String $S$ der Länge $N$, wobei $N$ ungerade ist. Der String ist definiert als eine Sequenz von Symbolen $s_0, s_1, \dots, s_{N-1}$, wobei $s_i \in \{T, F\}$ für gerades $i$ und $s_i \in \{\&, |, \wedge\}$ für ungerades $i$ gilt.

Wir definieren die Menge der Indizes der Operanden als $\mathcal{I} = \{0, 2, \dots, N-1\}$. Das Problem besteht darin, die Anzahl der Möglichkeiten zu berechnen, den Ausdruck so zu klammern, dass er zu einem booleschen Wert $v \in \{True, False\}$ evaluiert.

Wir definieren zwei Funktionen, $T(i, j)$ und $F(i, j)$, welche die Anzahl der Möglichkeiten repräsentieren, den Teilausdruck $S[i \dots j]$ so zu klammern, dass er zu $True$ bzw. $False$ evaluiert, für $i, j \in \mathcal{I}$ und $i \le j$.

Der Zustandsraum ist durch die Menge aller gültigen Teilintervalle $[i, j]$ definiert, wobei $i, j \in \mathcal{I}$. Die Gesamtzahl solcher Intervalle beträgt $\frac{(\frac{N+1}{2})(\frac{N+1}{2}+1)}{2} = O(N^2)$.

## 2. Algebraische Charakterisierung

Die Werte $T(i, j)$ und $F(i, j)$ sind durch die folgenden Rekursionsgleichungen definiert:

### Induktionsanfang
Für alle $i \in \mathcal{I}$:
$$T(i, i) = \begin{cases} 1 & \text{if } S[i] = 'T' \\ 0 & \text{if } S[i] = 'F' \end{cases}$$
$$F(i, i) = \begin{cases} 1 & \text{if } S[i] = 'F' \\ 0 & \text{if } S[i] = 'T' \end{cases}$$

### Induktionsschritt
Für $i < j$, sei $k \in \{i+1, i+3, \dots, j-1\}$ der Index des Operators, der den Ausdruck aufteilt. Die Werte werden wie folgt berechnet:
$$T(i, j) = \sum_{k=i+1, \text{step } 2}^{j-1} \text{Ways}_T(S[k], i, j, k)$$
$$F(i, j) = \sum_{k=i+1, \text{step } 2}^{j-1} \text{Ways}_F(S[k], i, j, k)$$

Wobei der Beitrag einer Aufteilung an der Stelle $k$ vom Operator $S[k]$ abhängt:

1. **Wenn $S[k] = \text{'&'}$:**
   $$\text{Ways}_T = T(i, k-1) \cdot T(k+1, j)$$
   $$\text{Ways}_F = T(i, k-1) \cdot F(k+1, j) + F(i, k-1) \cdot T(k+1, j) + F(i, k-1) \cdot F(k+1, j)$$

2. **Wenn $S[k] = \text{'|'}$:**
   $$\text{Ways}_T = T(i, k-1) \cdot T(k+1, j) + T(i, k-1) \cdot F(k+1, j) + F(i, k-1) \cdot T(k+1, j)$$
   $$\text{Ways}_F = F(i, k-1) \cdot F(k+1, j)$$

3. **Wenn $S[k] = \text{'^'}$:**
   $$\text{Ways}_T = T(i, k-1) \cdot F(k+1, j) + F(i, k-1) \cdot T(k+1, j)$$
   $$\text{Ways}_F = T(i, k-1) \cdot T(k+1, j) + F(i, k-1) \cdot F(k+1, j)$$

Die endgültige Lösung ist gegeben durch $T(0, N-1)$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus verwendet einen Bottom-up-Ansatz der dynamischen Programmierung über Intervalle zunehmender Länge $L = j - i$.
- Es gibt $O(N^2)$ mögliche Intervalle $[i, j]$.
- Für jedes Intervall iterieren wir über $O(N)$ mögliche Aufteilungspunkte $k$.
- Jeder Übergang beinhaltet eine konstante Anzahl an arithmetischen Operationen.
Die gesamte Zeitkomplexität ergibt sich aus der Summation:
$$\sum_{L=2, \text{step } 2}^{N-1} \sum_{i=0}^{N-L-1} \frac{L}{2} \approx \int_0^N \int_0^{N-x} \frac{x}{2} dy dx = O(N^3)$$
Somit ist die Zeitkomplexität $\Theta(N^3)$.

### Platzkomplexität
Der Algorithmus benötigt zwei $N \times N$ Matrizen, $T$ und $F$, um die Ergebnisse der Teilprobleme zu speichern.
- Der Speicherbedarf beträgt $2 \cdot N^2$ Ganzzahlen.
- Der zusätzliche Speicherbedarf für Schleifenindizes und temporäre Variablen ist $O(1)$.
Daher ist die gesamte Platzkomplexität $\Theta(N^2)$.