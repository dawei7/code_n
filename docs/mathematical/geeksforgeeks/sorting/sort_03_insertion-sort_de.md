# Formale Mathematische Spezifikation: Insertion Sort

## 1. Definitionen und Notation

Sei $A = [a_0, a_1, \dots, a_{n-1}]$ eine Sequenz von $n$ Elementen, entnommen aus einer total geordneten Menge $(\mathcal{X}, \le)$. Das Ziel des Insertion Sort Algorithmus ist es, eine Permutation $A'$ von $A$ zu erzeugen, sodass $A'$ in nicht-absteigender Reihenfolge sortiert ist:
$$a'_0 \le a'_1 \le \dots \le a'_{n-1}$$

Wir definieren den Zustand des Algorithmus in jeder Iteration $i$ (wobei $1 \le i < n$) durch die Konfiguration des Arrays $A^{(i)}$. Der Algorithmus unterhält eine Partition des Arrays in zwei zusammenhängende Sub-Segmente:
1.  **Das sortierte Präfix:** $A[0 \dots i-1]$, welches eine Permutation der ursprünglichen Elemente $\{a_0, \dots, a_{i-1}\}$ ist, sodass $A[k] \le A[k+1]$ für alle $0 \le k < i-1$ gilt.
2.  **Das unsortierte Suffix:** $A[i \dots n-1]$, welches die noch zu verarbeitenden Elemente enthält.

## 2. Algebraische Charakterisierung

Die Korrektheit von Insertion Sort wird mittels einer **Schleifeninvariante** etabliert. Sei $P(i)$ das Prädikat, dass das Sub-Array $A[0 \dots i-1]$ aus den ursprünglich in $A[0 \dots i-1]$ enthaltenen Elementen in sortierter Reihenfolge besteht.

**Initialisierung:** Für $i=1$ ist das Sub-Array $A[0 \dots 0]$ trivialerweise sortiert. $P(1)$ gilt.

**Erhaltung:** Angenommen, $P(i)$ gilt. Wir definieren den "key" als $k = A[i]$. Wir suchen einen Index $j \in \{0, \dots, i\}$ sodass:
$$A[m] \le k \text{ for } m < j \quad \text{and} \quad A[m] > k \text{ for } j \le m < i$$
Der Algorithmus führt eine Rechts-Shift-Operation auf den Elementen $A[j \dots i-1]$ durch, um eine Leerstelle an Index $j$ zu schaffen, wodurch das sortierte Präfix $A[0 \dots i-1]$ effektiv in $A[0 \dots i]$ transformiert wird, sodass $P(i+1)$ gilt.

**Terminierung:** Die Schleife terminiert, wenn $i = n$. In diesem Zustand impliziert die Invariante $P(n)$, dass das gesamte Array $A[0 \dots n-1]$ sortiert ist.

Die Übergangsfunktion für die innere Schleife, welche Elemente verschiebt, kann ausgedrückt werden als:
$$A[m+1] \leftarrow A[m] \quad \forall m \in \{j, j+1, \dots, i-1\}$$
gefolgt von der Zuweisung $A[j] \leftarrow k$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität $T(n)$ wird durch die Anzahl der durchgeführten Vergleiche und Zuweisungen bestimmt. Sei $c_i$ die Anzahl der Shifts, die während der $i$-ten Iteration durchgeführt werden. Die Gesamtzeit ist:
$$T(n) = \sum_{i=1}^{n-1} (c_i + 1)$$

*   **Schlechtester Fall:** Tritt auf, wenn die Eingabe in umgekehrter Reihenfolge vorliegt. Für jedes $i$ ist $c_i = i$.
    $$T_{worst}(n) = \sum_{i=1}^{n-1} (i + 1) = \sum_{k=2}^{n} k = \frac{n(n+1)}{2} - 1 = \Theta(n^2)$$
*   **Bester Fall:** Tritt auf, wenn die Eingabe bereits sortiert ist. Für jedes $i$ ist $c_i = 0$ (die Bedingung der inneren Schleife schlägt sofort fehl).
    $$T_{best}(n) = \sum_{i=1}^{n-1} 1 = n - 1 = \Omega(n)$$
*   **Durchschnittlicher Fall:** Angenommen, alle Permutationen sind gleich wahrscheinlich, ist die erwartete Anzahl der Shifts $E[c_i] = i/2$.
    $$T_{avg}(n) = \sum_{i=1}^{n-1} \left(\frac{i}{2} + 1\right) = \frac{1}{2} \frac{(n-1)n}{2} + (n-1) = \Theta(n^2)$$

### Platzkomplexität
Der Algorithmus arbeitet **in-place**. Er benötigt einen konstanten Betrag an Hilfsplatz für die Variablen `key`, `i` und `j`, unabhängig von der Eingabegröße $n$.
$$S(n) = O(1)$$
Die gesamte Platzkomplexität beträgt $O(n)$ zur Speicherung des Eingabe-Arrays, aber die Hilfsplatzkomplexität ist streng $O(1)$.