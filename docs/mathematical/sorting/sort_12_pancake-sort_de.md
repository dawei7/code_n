# Formale mathematische Spezifikation: Pancake Sort

## 1. Definitionen und Notation

Sei $A = [a_0, a_1, \dots, a_{n-1}]$ eine Sequenz von $n$ verschiedenen Ganzzahlen. Wir definieren den Zustandsraum $\mathcal{S}$ als die Menge aller Permutationen von $A$. Das Ziel ist es, den sortierten Zustand $A^* = [s_0, s_1, \dots, s_{n-1}]$ zu erreichen, sodass $s_0 < s_1 < \dots < s_{n-1}$, wobei ausschließlich der Präfix-Umkehroperator verwendet werden darf.

*   **Präfix-Umkehroperator:** Definiere $\rho_k: \mathcal{S} \to \mathcal{S}$ als die Funktion, die das Präfix der Länge $k+1$ (Indizes $0$ bis $k$) umkehrt. Formal ist für eine Sequenz $A$ die transformierte Sequenz $A' = \rho_k(A)$ definiert als:
    $$a'_i = \begin{cases} a_{k-i} & \text{if } 0 \le i \le k \\ a_i & \text{if } k < i < n \end{cases}$$
*   **Eingabe:** Eine Permutation $A \in \mathcal{S}$.
*   **Ausgabe:** Eine Sequenz von Indizes $\mathcal{K} = [k_1, k_2, \dots, k_m]$, sodass $\rho_{k_m}(\dots \rho_{k_1}(A) \dots) = A^*$.
*   **Aktive Grenze:** Sei $j$ die aktuelle Größe des unsortierten Präfixes, wobei $j \in \{n, n-1, \dots, 2\}$.

## 2. Algebraische Charakterisierung

Der Algorithmus arbeitet durch die Aufrechterhaltung einer Schleifeninvariante bezüglich des Suffixes des Array.

**Schleifeninvariante:** Zu Beginn jeder Iteration $j$ (wobei $j$ die Anzahl der Elemente im aktuellen unsortierten Präfix ist), ist das Suffix $A[j \dots n-1]$ sortiert und enthält die $n-j$ größten Elemente der ursprünglichen Menge $A$, sodass $\forall x \in \{0, \dots, j-1\}, \forall y \in \{j, \dots, n-1\}: a_x < a_y$.

**Übergangslogik:**
Sei $m_j$ der Index des maximalen Elements im Präfix $A[0 \dots j-1]$, sodass $a_{m_j} = \max \{a_0, \dots, a_{j-1}\}$. Der Algorithmus führt die folgenden Zustandsübergänge durch:
1. Wenn $m_j \neq 0$, wende $\rho_{m_j}$ an, um das Maximum an den Anfang zu bewegen: $A \leftarrow \rho_{m_j}(A)$.
2. Wende $\rho_{j-1}$ an, um das Maximum an das Ende des aktuellen aktiven Präfixes zu bewegen: $A \leftarrow \rho_{j-1}(A)$.

Die Korrektheit wird durch die Tatsache garantiert, dass nach diesen zwei Operationen das Element $a_{j-1}$ das globale Maximum der Menge $\{a_0, \dots, a_{j-1}\}$ ist, was die Invariante für $j-1$ erfüllt. Der Prozess terminiert, wenn $j=1$, da ein Präfix mit einem einzelnen Element trivialerweise sortiert ist.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus besteht aus einer äußeren Schleife, die $n-1$ Mal iteriert. Innerhalb jeder Iteration $j$:
1. **Finden des Maximums:** Ein linearer Scan über $j$ Elemente erfordert $j-1$ Vergleiche.
2. **Umkehroperationen:** Die `flip`-Operation (Präfix-Umkehr) beinhaltet $\lfloor \frac{k+1}{2} \rfloor$ Vertauschungen. Im Schlechtesten Fall ist $k = j-1$, was $O(j)$ Operationen erfordert.

Die gesamte Zeitkomplexität $T(n)$ ist die Summe der Arbeit, die über alle Iterationen hinweg geleistet wird:
$$T(n) = \sum_{j=2}^{n} (O(j) + O(j)) = \sum_{j=2}^{n} O(j)$$
Unter Verwendung der Summenformel für arithmetische Reihen $\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$ erhalten wir:
$$T(n) = O\left(\frac{n(n+1)}{2}\right) = O(n^2)$$
Somit ist der Algorithmus im Schlechtesten Fall und im Durchschnittlichen Fall durch $O(n^2)$ beschränkt.

### Platzkomplexität
Der Algorithmus führt alle Operationen in-place durch.
*   **Zusätzlicher Speicher:** Die Variablen `max_idx`, `size`, `start` und `end` benötigen $O(1)$ Speicherplatz.
*   **Gesamtspeicher:** Da das Eingabe-Array direkt modifiziert wird und für die Sortierlogik selbst keine zusätzlichen Datenstrukturen proportional zu $n$ erforderlich sind (ausgenommen die Ausgabesequenz $\mathcal{K}$), beträgt die zusätzliche Platzkomplexität $O(1)$. Falls die Sequenz der Flips $\mathcal{K}$ gespeichert werden muss, beträgt die Platzkomplexität $O(n)$, da die Anzahl der Flips durch $2n - 3$ beschränkt ist.