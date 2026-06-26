# Formale Mathematische Spezifikation: Merge Sort

## 1. Definitionen und Notation

Sei $A = [a_0, a_1, \dots, a_{n-1}]$ eine Sequenz von Elementen, die aus einer total geordneten Menge $(\mathcal{X}, \le)$ stammen. Das Ziel des Merge Sort Algorithmus ist es, eine Permutation $A' = [a'_0, a'_1, \dots, a'_{n-1}]$ von $A$ zu erzeugen, sodass $a'_i \le a'_{i+1}$ für alle $0 \le i < n-1$ gilt.

Wir definieren die folgenden Domänen und Operatoren:
*   **Sequenzraum:** Sei $\mathcal{S}$ die Menge aller endlichen Sequenzen über $\mathcal{X}$.
*   **Konkatenation:** Für $S_1, S_2 \in \mathcal{S}$ bezeichnet $S_1 \oplus S_2$ die Konkatenation von Sequenzen.
*   **Teilsequenz:** Für $0 \le i \le j < |S|$ bezeichnet $S[i:j]$ die Teilsequenz von $S$ vom Index $i$ bis $j-1$.
*   **Merge-Operator:** Definiere eine Funktion $\text{merge}: \mathcal{S} \times \mathcal{S} \to \mathcal{S}$, sodass für zwei sortierte Sequenzen $L$ und $R$, $\text{merge}(L, R)$ eine sortierte Sequenz $M$ zurückgibt, die alle Elemente von $L \cup R$ (Multimengenvereinigung) enthält.

## 2. Algebraische Charakterisierung

Der Algorithmus ist durch die rekursive Funktion $f: \mathcal{S} \to \mathcal{S}$ definiert:

$$
f(A) =
\begin{cases}
A & \text{if } |A| \le 1 \\
\text{merge}(f(A[0 : \lfloor n/2 \rfloor]), f(A[\lfloor n/2 \rfloor : n])) & \text{if } |A| > 1
\end{cases}
$$

### Die Merge-Invariante
Die Korrektheit der $\text{merge}(L, R)$-Operation beruht auf der folgenden Invariante. Seien $L = [l_1, \dots, l_p]$ und $R = [r_1, \dots, r_q]$ sortiert. In jedem Schritt $k$ des Merge-Prozesses sei $M_k$ die bisher konstruierte Sequenz und $L_i, R_j$ die verbleibenden Suffixe von $L$ und $R$. Die Invariante besagt:
1. $M_k$ ist sortiert.
2. $\forall x \in M_k, \forall y \in (L_i \cup R_j), x \le y$.
3. $M_k \cup L_i \cup R_j = L \cup R$.

Bei Terminierung sind $L_i = \emptyset$ und $R_j = \emptyset$, was impliziert, dass $M_k$ eine sortierte Permutation der ursprünglichen Eingabe ist.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität $T(n)$ wird durch das Master-Theorem für Divide-and-Conquer-Rekurrenzen bestimmt. Gegeben sei ein Array der Größe $n$:
1. Der Divisionsschritt benötigt $O(1)$ Zeit.
2. Die rekursiven Aufrufe bestehen aus zwei Teilproblemen der Größe $n/2$.
3. Die Merge-Operation führt höchstens $n-1$ Vergleiche durch, was einen Aufwand von $O(n)$ ergibt.

Die Rekursionsgleichung lautet:
$$T(n) = 2T\left(\frac{n}{2}\right) + \Theta(n)$$

Anwendung des Master-Theorems, wobei $a=2, b=2, f(n)=n$:
Da $n^{\log_b a} = n^{\log_2 2} = n^1$ und $f(n) = \Theta(n^1)$, fallen wir in Fall 2 des Master-Theorems. Daher gilt:
$$T(n) = \Theta(n \log n)$$

### Platzkomplexität
Die Platzkomplexität wird durch den Hilfsspeicher bestimmt, der während der Merge-Phase und dem Rekursions-Stack benötigt wird.

1. **Hilfs-Array:** Auf jeder Ebene der Rekursion allozieren wir temporären Speicher, um die zusammengeführten Ergebnisse zu speichern. Während der gesamte Speicher über alle rekursiven Aufrufe hinweg $O(n \log n)$ betragen könnte, wenn er nicht sorgfältig verwaltet wird, verwendet die Standardimplementierung Speicher wieder oder gibt ihn frei, sodass der maximal benötigte Hilfsspeicher zu jedem Zeitpunkt $O(n)$ beträgt.
2. **Rekursions-Stack:** Die Tiefe des Rekursionsbaums beträgt $\lceil \log_2 n \rceil$. Jeder Stack-Frame verbraucht $O(1)$ Platz, was zu $O(\log n)$ Stack-Platz führt.

Die gesamte Platzkomplexität wird durch das Hilfs-Array dominiert:
$$S(n) = O(n) + O(\log n) = O(n)$$