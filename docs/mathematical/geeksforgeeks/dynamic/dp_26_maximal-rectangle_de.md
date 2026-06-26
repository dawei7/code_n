# Formale mathematische Spezifikation: Maximales Rechteck

## 1. Definitionen und Notation

Sei $M$ eine binäre Matrix der Dimension $m \times n$, wobei $M_{i,j} \in \{0, 1\}$ für $0 \le i < m$ und $0 \le j < n$ gilt. Wir definieren die Menge aller möglichen Teilrechtecke $R$ als die Menge der Quadrupel $(r_1, c_1, r_2, c_2)$, sodass $0 \le r_1 \le r_2 < m$ und $0 \le c_1 \le c_2 < n$ gilt.

Ein Teilrechteck wird genau dann als "gültig" betrachtet, wenn:
$$\forall r \in [r_1, r_2], \forall c \in [c_1, c_2] : M_{r,c} = 1$$

Das Ziel ist es, die maximale Fläche $\mathcal{A}^*$ zu finden, definiert als:
$$\mathcal{A}^* = \max_{(r_1, c_1, r_2, c_2) \in \mathcal{R}_{valid}} (r_2 - r_1 + 1) \times (c_2 - c_1 + 1)$$

Wir definieren einen Zustandsvektor $H^{(i)} \in \mathbb{N}^n$, der das "Histogramm" der aufeinanderfolgenden Einsen repräsentiert, die in Zeile $i$ enden:
$$H^{(i)}_j = \begin{cases} 0 & \text{if } M_{i,j} = 0 \\ H^{(i-1)}_j + 1 & \text{if } M_{i,j} = 1 \end{cases}$$
wobei $H^{(-1)}_j = 0$ für alle $j$ gilt.

## 2. Algebraische Charakterisierung

Das Problem wird in $m$ unabhängige Instanzen des Problems "Größtes Rechteck im Histogramm" zerlegt. Sei für eine feste Zeile $i$ $f(H^{(i)})$ die Fläche des größten Rechtecks im Histogramm, das durch den Vektor $H^{(i)}$ definiert ist.

### Rekursionsgleichung
Die globale maximale Fläche ergibt sich aus dem Supremum über alle zeilenweisen Histogramm-Lösungen:
$$\mathcal{A}^* = \max_{0 \le i < m} f(H^{(i)})$$

### Histogramm-Invariante
Sei für eine feste Zeile $i$ $S$ ein monotoner Stack, der Indizes $k$ enthält, sodass $H^{(i)}_{S_t} \le H^{(i)}_{S_{t+1}}$ gilt. Für jeden Index $k$, der verarbeitet wird:
1. Wenn $H^{(i)}_k < H^{(i)}_{S_{top}}$, führen wir ein `pop` auf $S_{top}$ aus und berechnen die Fläche des Rechtecks mit der Höhe $H^{(i)}_{S_{top}}$.
2. Die Breite $W$ dieses Rechtecks wird durch die nächstgelegenen Indizes links und rechts bestimmt, die strikt kleiner als $H^{(i)}_{S_{top}}$ sind. Spezifisch gilt:
   $$W = k - S_{top-1} - 1$$
3. Der Flächenbeitrag ist $\mathcal{A}_{pop} = H^{(i)}_{S_{top}} \times (k - S_{top-1} - 1)$.

Die Korrektheit beruht auf der Invariante, dass der Stack für jeden Balken $H^{(i)}_j$ die Grenzen des größten Rechtecks der Höhe $H^{(i)}_j$ beibehält, das die Spalte $j$ einschließt.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus besteht aus zwei verschachtelten Prozessen:
1. **Histogramm-Konstruktion:** Für jede Zeile $i \in \{0, \dots, m-1\}$ aktualisieren wir $n$ Elemente. Dies erfordert $\sum_{i=0}^{m-1} n = O(mn)$ Operationen.
2. **Monotone Stack-Verarbeitung:** Für jede Zeile führen wir einen linearen Scan von $n$ Elementen durch. Jeder Index $j \in \{0, \dots, n-1\}$ wird genau einmal auf den Stack `push`ed und höchstens einmal `pop`ed. Die amortisierten Kosten pro Zeile betragen $O(n)$.

Die gesamte Zeitkomplexität $T(m, n)$ ist:
$$T(m, n) = \sum_{i=0}^{m-1} (O(n) + O(n)) = O(mn)$$
Somit gilt $T(m, n) \in \Theta(mn)$.

### Platzkomplexität
Die Platzkomplexität $S(m, n)$ wird von den Hilfsstrukturen dominiert:
1. **Histogramm-Array:** $H$ benötigt $O(n)$ Platz.
2. **Monotoner Stack:** Im Schlechtesten Fall (ein streng monoton steigendes Histogramm) speichert der Stack $O(n)$ Indizes.

Die gesamte Platzkomplexität $S(m, n)$ ist:
$$S(m, n) = O(n) + O(n) = O(n)$$
Die Platzkomplexität ist unabhängig von der Anzahl der Zeilen $m$, vorausgesetzt, die Matrix wird zeilenweise verarbeitet, was $S(m, n) \in \Theta(n)$ ergibt.