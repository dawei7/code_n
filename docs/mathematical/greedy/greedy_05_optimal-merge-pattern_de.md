# Formale mathematische Spezifikation: Optimal Merge Pattern

## 1. Definitionen und Notation

Sei $S = \{s_1, s_2, \dots, s_n\}$ eine Multimenge von $n$ positiven Ganzzahlen, wobei jedes $s_i \in \mathbb{Z}^+$ die Größe einer Datei repräsentiert.

Wir definieren den Zustand des Systems zu einem beliebigen Zeitpunkt $t$ als eine Multimenge $\mathcal{M}_t$. Zu Beginn gilt $\mathcal{M}_0 = S$. Eine Merge-Operation $\phi$ auf zwei Elementen $a, b \in \mathcal{M}_t$ erzeugt eine neue Multimenge $\mathcal{M}_{t+1} = (\mathcal{M}_t \setminus \{a, b\}) \cup \{a + b\}$. Die Kosten dieser Operation werden durch die Funktion $c(\phi) = a + b$ definiert.

Das Ziel ist es, einen Endzustand $\mathcal{M}_{n-1} = \{\sum_{i=1}^n s_i\}$ durch eine Sequenz von $n-1$ Merge-Operationen $\Phi = (\phi_1, \phi_2, \dots, \phi_{n-1})$ zu erreichen. Die Gesamtkosten $C(\Phi)$ sind die Summe der Kosten der einzelnen Operationen:
$$C(\Phi) = \sum_{j=1}^{n-1} c(\phi_j)$$

## 2. Algebraische Charakterisierung

Das Problem ist isomorph zur Konstruktion eines Binary Tree, dessen Blätter die Elemente von $S$ sind. Sei $T$ ein Binary Tree mit $n$ Blättern, wobei jedes Blatt $l_i$ einem Element $s_i \in S$ entspricht. Sei $d_i$ die Tiefe des Blattes $l_i$ (die Anzahl der Kanten auf dem Pfad von der Wurzel zum Blatt).

Die Gesamtkosten des Mergens ergeben sich aus der gewichteten Pfadlänge des Baumes:
$$C(T) = \sum_{i=1}^n s_i \cdot d_i$$

**Theorem (Greedy-Optimalität):** Um $C(T)$ zu minimieren, müssen wir die Tiefe $d_i$ für die größten Werte von $s_i$ minimieren. Dies wird durch die Huffman-Kodierungskonstruktion erreicht, welche die folgende Rekurrenz für die minimalen Kosten $f(\mathcal{M})$ erfüllt:
$$f(\mathcal{M}) = \min_{a, b \in \mathcal{M}} \{ (a + b) + f((\mathcal{M} \setminus \{a, b\}) \cup \{a + b\}) \}$$
wobei der Induktionsanfang $f(\{x\}) = 0$ ist.

**Schleifeninvariante:** Zu Beginn jeder Iteration des Algorithmus entsprechen die akkumulierten Gesamtkosten der Summe aller inneren Knoten des bis dahin konstruierten Binary Tree, und die Priority Queue enthält die Wurzeln der Teilbäume, die aus den Elementen der aktuellen Multimenge $\mathcal{M}_t$ gebildet wurden.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus verwendet einen Min-Heap (Priority Queue), um die Multimenge $\mathcal{M}_t$ zu verwalten.

1. **Initialisierung:** Das Konstruieren des Heaps aus $n$ Elementen mittels `heapify` benötigt $T_{init} = O(n)$.
2. **Iteration:** Der Algorithmus führt $n-1$ Iterationen durch. In jeder Iteration:
   - Zwei `heappop`-Operationen werden durchgeführt: $2 \times O(\log n)$.
   - Eine `heappush`-Operation wird durchgeführt: $1 \times O(\log n)$.
   - Der Gesamtaufwand pro Iteration beträgt $O(\log n)$.
3. **Gesamtzeit:**
   $$T(n) = O(n) + \sum_{i=1}^{n-1} O(\log n) = O(n) + O(n \log n) = O(n \log n)$$
Somit beträgt die Zeitkomplexität $\Theta(n \log n)$.

### Platzkomplexität
1. **Zusätzlicher Speicher:** Der Min-Heap speichert zu Beginn genau $n$ Elemente. Während des Merge-Prozesses verringert sich die Anzahl der Elemente im Heap in jedem Schritt um 1. Der maximal benötigte Speicherplatz beträgt $O(n)$, um die Elemente der Multimenge $\mathcal{M}_t$ zu speichern.
2. **Gesamtspeicher:** Da der Algorithmus auf der Multimenge der Größe $n$ operiert, beträgt die Platzkomplexität $\Theta(n)$. Wenn das Eingabe-Array in-place modifiziert wird, bleibt der zusätzliche Speicherbedarf aufgrund der Anforderungen der Heap-Struktur $O(n)$, obwohl der Speicher der Eingabe wiederverwendet wird.