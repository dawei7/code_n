# Formale mathematische Spezifikation: Inversionen zählen

## 1. Definitionen und Notation

Sei $A = \langle a_1, a_2, \dots, a_n \rangle$ eine Sequenz von $n$ Elementen aus einer total geordneten Menge $(\mathcal{X}, \leq)$.

*   **Inversion:** Eine Inversion in $A$ ist definiert als ein geordnetes Paar von Indizes $(i, j)$, sodass $1 \leq i < j \leq n$ und $a_i > a_j$ gilt.
*   **Inversionsmenge:** Sei $\mathcal{I}(A) = \{ (i, j) \in \mathbb{Z}^2 \mid 1 \leq i < j \leq n \land a_i > a_j \}$.
*   **Inversionsanzahl:** Das Ziel ist die Berechnung der Kardinalität der Inversionsmenge, bezeichnet als $I(A) = |\mathcal{I}(A)|$.
*   **Zustandsraum:** Der Algorithmus operiert auf dem Raum der Permutationen der Eingabesequenz und transformiert $A$ in sein sortiertes Gegenstück $A'$, während er die Anzahl der während der Transformation auftretenden Inversionen akkumuliert.

## 2. Algebraische Charakterisierung

Der Algorithmus nutzt das Divide-and-Conquer-Paradigma und stützt sich auf die Eigenschaft, dass die Gesamtzahl der Inversionen in einer Sequenz $A$ basierend auf einer Partition von $A$ in zwei Teilsequenzen $L = \langle a_1, \dots, a_m \rangle$ und $R = \langle a_{m+1}, \dots, a_n \rangle$ zerlegt werden kann, wobei $m = \lfloor n/2 \rfloor$ ist.

Die gesamte Inversionsanzahl $I(A)$ erfüllt die folgende Rekursionsgleichung:
$$I(A) = I(L) + I(R) + I_{split}(L, R)$$

Hierbei repräsentiert $I_{split}(L, R)$ die Anzahl der Paare $(i, j)$, sodass $a_i \in L$ und $a_j \in R$ mit $a_i > a_j$ gilt. Da $L$ und $R$ sortiert sind (als Postkondition der rekursiven Aufrufe), definieren wir die Zählfunktion während des Merge-Schritts. Sei $L$ indiziert mit $1 \dots |L|$ und $R$ indiziert mit $1 \dots |R|$. Wenn $L[i] > R[j]$ gilt, dann erfüllen aufgrund der Sortierung von $L$ alle Elemente $L[k]$ für $k \geq i$ die Bedingung $L[k] \geq L[i] > R[j]$.

Somit ergibt sich die Anzahl der Split-Inversionen zu:
$$I_{split}(L, R) = \sum_{j=1}^{|R|} |\{ i \in \{1, \dots, |L|\} : L[i] > R[j] \}|$$

**Schleifeninvariante:** Zu Beginn jeder Iteration des Merge-Prozesses enthält das Hilfs-Array die sortierten Elemente von $L[1 \dots i-1]$ und $R[1 \dots j-1]$, und die Variable `count` enthält die Anzahl der Inversionen, die innerhalb der bisher verarbeiteten Subarrays gefunden wurden.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus folgt dem Master-Theorem für Divide-and-Conquer-Rekursionen. Die Arbeit, die auf jeder Ebene des Rekursionsbaums verrichtet wird, besteht aus einem linearen Durchlauf (dem Merge-Schritt), um Inversionen zu zählen und Elemente neu anzuordnen.

Die Rekursionsgleichung für die Zeitkomplexität $T(n)$ lautet:
$$T(n) = 2T\left(\frac{n}{2}\right) + \Theta(n)$$

Unter Anwendung des Master-Theorems, wobei $a=2, b=2, f(n) = n^1$:
Da $n^{\log_b a} = n^{\log_2 2} = n^1$ gilt, fallen wir in Fall 2 des Master-Theorems.
Daher ist $T(n) = \Theta(n \log n)$.

### Platzkomplexität
Der Algorithmus benötigt zusätzlichen Speicherplatz für den Merge-Prozess. Auf jeder Tiefe $d$ des Rekursionsbaums allokiert der Algorithmus temporäre Arrays, um die Elemente der aktuellen Subarrays zu speichern.

*   **Hilfsspeicher:** Der Merge-Schritt benötigt $O(n)$ Speicherplatz, um die zusammengeführten Elemente zu speichern, bevor sie zurück in das ursprüngliche Array kopiert werden.
*   **Stack-Speicher:** Die Rekursionstiefe beträgt $\lceil \log_2 n \rceil$.
*   **Gesamtspeicher:** Da die Merge-Arrays nach der Rückkehr des rekursiven Aufrufs wieder freigegeben werden, beträgt die maximale Platzkomplexität für den Hilfsspeicher $O(n)$, dominiert durch den Speicherbedarf für die größte Merge-Operation auf der obersten Ebene der Rekursion. Somit ist die gesamte Platzkomplexität $O(n)$.