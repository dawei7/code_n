# Formale mathematische Spezifikation: Min Cost Climbing Stairs

## 1. Definitionen und Notation

Sei $C = \{c_0, c_1, \dots, c_{n-1}\}$ eine Folge von nicht-negativen Ganzzahlen, die die Kosten für jeden Schritt $i \in \{0, 1, \dots, n-1\}$ repräsentieren, wobei $n = |C|$.

Wir definieren den Zustandsraum $\mathcal{S} = \{0, 1, \dots, n\}$, der die Indizes der Treppe darstellt, wobei $n$ die „oberste Etage“ (das Ziel) bezeichnet.

Sei $f(i)$ die minimalen Kosten, um Schritt $i$ zu erreichen. Das Ziel ist es, $f(n)$ zu bestimmen, die minimalen Kosten, um den Zielindex $n$ zu erreichen.

## 2. Algebraische Charakterisierung

Das Problem wird durch eine Rekursionsgleichung der dynamischen Programmierung bestimmt. Um Schritt $i$ zu erreichen, muss man entweder von Schritt $i-1$ oder von Schritt $i-2$ gekommen sein. Da die Kosten $c_j$ beim Verlassen von Schritt $j$ anfallen, sind die Gesamtkosten zum Erreichen von Schritt $i$ das Minimum der Kosten, die zum Erreichen der vorherigen Schritte anfielen, zuzüglich der Kosten für das Verlassen dieser Schritte.

### Rekursionsgleichung
Für $i \geq 2$ ist die optimale Substruktur definiert als:
$$f(i) = \min(f(i-1) + c_{i-1}, f(i-2) + c_{i-2})$$

### Induktionsanfang
Da die Startposition entweder Index $0$ oder Index $1$ mit anfänglichen Kosten von Null sein kann:
$$f(0) = 0$$
$$f(1) = 0$$

### Zielfunktion
Das Ziel ist es, Index $n$ zu erreichen. Da man Index $n$ entweder von Index $n-1$ oder von Index $n-2$ aus erreichen kann, lauten die Endkosten:
$$f(n) = \min(f(n-1) + c_{n-1}, f(n-2) + c_{n-2})$$

### Schleifeninvariante
Seien $p_1^{(k)}$ und $p_2^{(k)}$ die Werte von $f(k)$ beziehungsweise $f(k-1)$ zu Beginn der Iteration $k$. Der Übergang erhält die Invariante:
$$\forall i \in \{2, \dots, n\}: \text{cur}_i = \min(p_1 + c_{i-1}, p_2 + c_{i-2})$$
wobei $p_1$ und $p_2$ so aktualisiert werden, dass $p_2 \leftarrow p_1$ und $p_1 \leftarrow \text{cur}_i$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus führt einen einzelnen linearen Durchlauf über das Eingabe-Array $C$ aus. Sei $T(n)$ die Anzahl der Operationen, die für eine Eingabe der Größe $n$ erforderlich sind.
Die Initialisierung benötigt $O(1)$ Zeit. Die Schleife führt $n-2$ Iterationen aus. Innerhalb jeder Iteration führt der Algorithmus eine konstante Anzahl an arithmetischen Operationen (Addition und Vergleich) aus, bezeichnet als $k \in \mathbb{R}^+$.
$$T(n) = T_{init} + \sum_{i=2}^{n-1} k = O(1) + (n-2) \cdot O(1) = O(n)$$
Somit ist die Zeitkomplexität strikt linear, $O(n)$.

### Platzkomplexität
Der Algorithmus verwendet eine feste Anzahl an Hilfsvariablen ($prev1, prev2, cur$), um den Zustand der Rekursion zu speichern. Sei $S(n)$ die zusätzliche Platzkomplexität.
Da der Speicherverbrauch nicht mit der Eingabegröße $n$ skaliert:
$$S(n) = O(1)$$
Der Algorithmus erreicht eine optimale Platzeffizienz, indem er historische Zustände $f(i-k)$ für $k > 2$ verwirft, da die Rekursionsgleichung die Markow-Eigenschaft aufweist – der zukünftige Zustand hängt nur von den zwei unmittelbar vorangegangenen Zuständen ab.