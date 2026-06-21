# Formale Mathematische Spezifikation: Selection Sort

## 1. Definitionen und Notation

Sei $A = [a_0, a_1, \dots, a_{n-1}]$ eine Sequenz von $n$ Elementen, entnommen aus einer total geordneten Menge $(\mathcal{X}, \le)$. Das Ziel des Selection Sort Algorithmus ist es, eine Permutation $A'$ von $A$ zu erzeugen, sodass $A' = [a'_0, a'_1, \dots, a'_{n-1}]$ die Bedingung $a'_0 \le a'_1 \le \dots \le a'_{n-1}$ erfüllt.

Wir definieren den Zustand des Algorithmus in jeder Iteration $i \in \{0, 1, \dots, n-2\}$ durch die Partition des Arrays in zwei zusammenhängende Segmente:
*   **Sortiertes Präfix:** $A[0 \dots i-1]$, wobei für alle $j < k < i$ gilt: $a_j \le a_k$.
*   **Unsortiertes Suffix:** $A[i \dots n-1]$, wobei für alle $x \in A[0 \dots i-1]$ und $y \in A[i \dots n-1]$ gilt: $x \le y$.

Der Algorithmus operiert im Zustandsraum $\mathcal{S} = \mathcal{X}^n$ und transformiert die initiale Konfiguration $A^{(0)} = A$ in die finale Konfiguration $A^{(n-1)}$ durch eine Sequenz von $n-1$ diskreten Vertauschungsoperationen (Swaps).

## 2. Algebraische Charakterisierung

Die Korrektheit von Selection Sort wird durch die folgende Schleifeninvariante gewährleistet: Zu Beginn jeder Iteration $i$ ist das Sub-Array $A[0 \dots i-1]$ sortiert und enthält die $i$ kleinsten Elemente des ursprünglichen Arrays.

### Die Selektionsfunktion
In jeder Iteration $i$ definieren wir die Selektion des Index $m_i$ wie folgt:
$$m_i = \text{argmin}_{j \in \{i, \dots, n-1\}} \{A[j]\}$$
Falls mehrere Indizes die Bedingung erfüllen, wird $m_i$ als der kleinste dieser Indizes definiert.

### Die Zustandsübergangsfunktion
Der Übergang von Zustand $i$ zu $i+1$ wird durch die Transposition $\tau_i = (i, m_i)$ definiert, welche die Elemente an den Indizes $i$ und $m_i$ vertauscht:
$$A^{(i+1)} = A^{(i)} \circ \tau_i$$
wobei die Komposition die Anwendung der Vertauschung (Swap) bezeichnet. Der Algorithmus terminiert, wenn $i = n-1$, woraufhin die Invariante impliziert:
$$\forall j, k \in \{0, \dots, n-1\}, j < k \implies A[j] \le A[k]$$

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität wird durch die Anzahl der durchgeführten Vergleiche bestimmt. In jeder Iteration $i$ führt der Algorithmus einen linearen Scan des unsortierten Suffixes $A[i \dots n-1]$ durch. Die Anzahl der Vergleiche $C(n)$ ergibt sich aus der Summation:
$$T(n) = \sum_{i=0}^{n-2} \sum_{j=i+1}^{n-1} 1$$
Auswertung der inneren Summe:
$$\sum_{j=i+1}^{n-1} 1 = (n-1) - (i+1) + 1 = n - i - 1$$
Einsetzen in die äußere Summe:
$$T(n) = \sum_{i=0}^{n-2} (n - i - 1)$$
Sei $k = n - i - 1$. Während $i$ von $0$ bis $n-2$ läuft, läuft $k$ von $n-1$ abwärts bis $1$:
$$T(n) = \sum_{k=1}^{n-1} k = \frac{(n-1)n}{2} = \frac{1}{2}n^2 - \frac{1}{2}n$$
Somit ist $T(n) = \Theta(n^2)$. Da die Anzahl der Vergleiche unabhängig von der initialen Permutation von $A$ ist, sind die Zeitkomplexitäten im Bestfall, durchschnittlichen Fall und schlechtesten Fall identisch: $O(n^2)$.

### Platzkomplexität
Der Algorithmus arbeitet in-place. Er benötigt einen konstanten Betrag an Hilfsspeicher für die Schleifenindizes $i, j$ und den Pointer $m_i$, unabhängig von der Eingabegröße $n$.
*   **Hilfsspeicher:** $O(1)$.
*   **Gesamtplatzbedarf:** $O(n)$ zum Speichern des Eingabe-Arrays $A$.

Die Anzahl der Schreiboperationen (Swaps) ist durch $n-1$ begrenzt, da jede Iteration höchstens eine Vertauschung (Swap) durchführt, was die Anforderung an minimale Schreiboperationen in speicherbeschränkten Umgebungen erfüllt.