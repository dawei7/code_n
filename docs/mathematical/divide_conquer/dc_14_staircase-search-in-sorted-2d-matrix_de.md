# Formale mathematische Spezifikation: Suche in einer 2D-Matrix (Treppensuche)

## 1. Definitionen und Notation

Sei $M$ eine $m \times n$ Matrix von Ganzzahlen, wobei $m, n \in \mathbb{Z}^+$. Wir bezeichnen das Element in Zeile $i$ und Spalte $j$ als $A_{i,j}$, wobei $0 \le i < m$ und $0 \le j < n$ gilt.

Die Matrix $A$ ist durch die folgenden Monotonieeigenschaften definiert:
1. **Zeilenweise Monotonie:** $\forall i \in \{0, \dots, m-1\}, \forall j \in \{0, \dots, n-2\}: A_{i,j} \le A_{i,j+1}$
2. **Spaltenweise Monotonie:** $\forall j \in \{0, \dots, n-1\}, \forall i \in \{0, \dots, m-2\}: A_{i,j} \le A_{i+1,j}$

Das Suchziel ist die Bestimmung der Existenz eines Zielwerts $\tau \in \mathbb{Z}$, sodass:
$$f(A, \tau) = \begin{cases} 1 & \text{falls } \exists (i, j) \in \{0, \dots, m-1\} \times \{0, \dots, n-1\} \text{ mit } A_{i,j} = \tau \\ 0 & \text{sonst} \end{cases}$$

Der Zustandsraum $\mathcal{S}$ des Algorithmus ist durch das Tupel $(i, j)$ definiert, welches die aktuell untersuchten Indizes repräsentiert, wobei $(i, j) \in \{0, \dots, m-1\} \times \{0, \dots, n-1\}$ gilt.

## 2. Algebraische Charakterisierung

Der Algorithmus operiert durch die Aufrechterhaltung einer Schleifeninvariante, die den Suchraum einschränkt. Sei $S_k$ die Menge der Kandidaten-Indizes $(i, j)$ in Iteration $k$, die potenziell $\tau$ enthalten könnten. Zu Beginn gilt $S_0 = \{0, \dots, m-1\} \times \{0, \dots, n-1\}$.

Wir initialisieren den Pointer in der oberen rechten Ecke: $(i_0, j_0) = (0, n-1)$. In jedem Schritt $k$ vergleichen wir $A_{i_k, j_k}$ mit $\tau$:

1. **Fall 1 (Treffer):** Wenn $A_{i_k, j_k} = \tau$, terminiert die Suche erfolgreich.
2. **Fall 2 (Eliminierung der Spalte):** Wenn $A_{i_k, j_k} > \tau$, dann gilt aufgrund der zeilenweisen Monotonie $\forall j' \ge j_k, A_{i_k, j'} \ge A_{i_k, j_k} > \tau$. Des Weiteren gilt aufgrund der spaltenweisen Monotonie $\forall i' > i_k, A_{i', j_k} \ge A_{i_k, j_k} > \tau$. Somit sind alle Elemente in Spalte $j_k$ in oder unterhalb von Zeile $i_k$ strikt größer als $\tau$. Wir aktualisieren $j_{k+1} = j_k - 1$.
3. **Fall 3 (Eliminierung der Zeile):** Wenn $A_{i_k, j_k} < \tau$, dann gilt aufgrund der spaltenweisen Monotonie $\forall i' \le i_k, A_{i', j_k} \le A_{i_k, j_k} < \tau$. Des Weiteren gilt aufgrund der zeilenweisen Monotonie $\forall j' < j_k, A_{i_k, j'} \le A_{i_k, j_k} < \tau$. Somit sind alle Elemente in Zeile $i_k$ in oder links von Spalte $j_k$ strikt kleiner als $\tau$. Wir aktualisieren $i_{k+1} = i_k + 1$.

Die Invariante besagt, dass in jedem Schritt $k$, falls $\tau \in A$ gilt, $\tau$ in der durch die verbleibenden gültigen Indizes definierten Teilmatrix existieren muss. Der Algorithmus terminiert, wenn $i_k \ge m$ oder $j_k < 0$, was bedeutet, dass der Suchraum leer ist und somit $\tau \notin A$ gilt.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus führt eine Traversierung beginnend bei $(0, n-1)$ durch und terminiert, sobald der Pointer die Grenzen der Matrix verlässt. In jeder Iteration wird entweder $i$ inkrementiert oder $j$ dekrementiert.
Sei $T(m, n)$ die Anzahl der Schritte. Da $i$ höchstens $m$-mal erhöht und $j$ höchstens $n$-mal verringert werden kann, ist die Gesamtzahl der Iterationen $K$ beschränkt durch:
$$K \le m + n$$
Jede Iteration führt eine konstante Anzahl an Operationen $O(1)$ aus. Daher beträgt die gesamte Zeitkomplexität:
$$T(m, n) = O(m + n)$$
Dies ist optimal, da jeder Algorithmus im Schlechtesten Fall $O(m+n)$ Elemente untersuchen muss, um die Abwesenheit eines Zielwerts in einer sortierten Matrix zu verifizieren.

### Platzkomplexität
Der Algorithmus verwendet eine konstante Anzahl an Hilfsvariablen $(i, j, v)$, um die aktuelle Position und den Wert des Matrixelements zu verfolgen. Es werden keine zusätzlichen Datenstrukturen benötigt, die proportional zur Eingabegröße sind.
$$S(m, n) = O(1)$$
Die Platzkomplexität ist konstant und erfüllt somit die Anforderung für $O(1)$ zusätzlichen Speicherplatz.