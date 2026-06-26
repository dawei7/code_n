# Formale mathematische Spezifikation: Range Sum Query (Punkt-Update)

## 1. Definitionen und Notation

Sei $A = [a_0, a_1, \dots, a_{n-1}]$ ein Array aus $n$ Elementen, wobei $a_i \in \mathbb{R}$. Wir definieren einen Fenwick Tree (Binary Indexed Tree) als ein Array $T$ der Größe $n+1$, wobei $T[i]$ die Summe einer spezifischen Teilmenge von Elementen aus $A$ speichert.

*   **Index-Abbildung:** Wir definieren eine Bijektion zwischen dem 0-indizierten Array $A$ und dem 1-indizierten Baum $T$. Der Index $i \in \{1, \dots, n\}$ in $T$ entspricht dem Bereich $(i - 2^{k} + 1, i]$, wobei $k$ die Anzahl der nachgestellten Nullen in der Binärdarstellung von $i$ ist.
*   **Lowest Set Bit (LSB):** Wir definieren die Funktion $\text{lsb}(i) = i \& (-i)$, welche den Wert des niedrigstwertigen Bits von $i$ extrahiert. Mathematisch gilt $\text{lsb}(i) = 2^{\nu_2(i)}$, wobei $\nu_2(i)$ die 2-adische Bewertung von $i$ ist.
*   **Zustandsraum:** Der Zustand des Systems ist durch das Tupel $(A, T)$ definiert. Eine Update-Operation $U(i, \Delta)$ transformiert $A \to A'$ und $T \to T'$, wobei $a'_i = a_i + \Delta$.
*   **Abfragebereich:** Eine Bereichsabfrage (Range Query) ist definiert als eine Funktion $Q(l, r) = \sum_{k=l}^{r} a_k$, wobei $0 \le l \le r < n$.

## 2. Algebraische Charakterisierung

Der Fenwick Tree beruht auf der Eigenschaft, dass jede ganze Zahl $i \in [1, n]$ eindeutig in eine Summe von Zweierpotenzen zerlegt werden kann, was den disjunkten Intervallen entspricht, die in $T$ gespeichert sind.

### Konstruktion der Präfixsumme
Die Präfixsummenfunktion $P(i) = \sum_{j=0}^{i-1} a_j$ wird wie folgt berechnet:
$$P(i) = \sum_{k=0}^{\text{popcount}(i)-1} T[idx_k]$$
wobei $idx_0 = i$ und $idx_{k+1} = idx_k - \text{lsb}(idx_k)$, mit Abbruch bei $idx_k = 0$.

### Übergang bei Punkt-Update
Wenn ein Element $a_i$ um $\Delta = a_{new} - a_{old}$ modifiziert wird, propagiert das Update durch den Baum zu allen Knoten $j$, die den Index $i+1$ abdecken. Die Update-Regel lautet:
$$T[j] \leftarrow T[j] + \Delta, \quad \text{für } j = (i+1), (i+1) + \text{lsb}(i+1), \dots, \le n$$
Dies stellt sicher, dass die Invariante $T[j] = \sum_{k=j-\text{lsb}(j)+1}^{j} a_{k-1}$ für alle $j \in \{1, \dots, n\}$ erhalten bleibt.

### Formulierung der Bereichsabfrage
Aufgrund der Additivität der Präfixsumme ergibt sich die Bereichssumme zu:
$$Q(l, r) = P(r+1) - P(l)$$
wobei $P(i)$ die Präfixsumme der ersten $i$ Elemente ist.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität wird durch die Anzahl der Bits im Index $n$ bestimmt.

*   **Abfrage:** Die `prefix(i)`-Operation durchläuft den Baum, indem sie bei jedem Schritt das LSB entfernt. Die Anzahl der Iterationen entspricht der Anzahl der gesetzten Bits in der Binärdarstellung von $i+1$, bezeichnet als $\text{popcount}(i+1)$. Da $\text{popcount}(i+1) \le \lfloor \log_2(n) \rfloor + 1$ gilt, beträgt die Komplexität der Abfrage $O(\log n)$.
*   **Update:** Die `update(i, delta)`-Operation durchläuft den Baum, indem sie bei jedem Schritt das LSB addiert. Die Anzahl der besuchten Knoten ist durch die Anzahl der Male begrenzt, die wir das LSB addieren können, bevor wir $n$ überschreiten. Dies entspricht der Anzahl der Bits, die in der Binärdarstellung von $i+1$ von 0 auf 1 gekippt werden können, was ebenfalls durch $O(\log n)$ begrenzt ist.

Somit sind beide Operationen strikt $O(\log n)$.

### Platzkomplexität
Der Fenwick Tree $T$ benötigt ein Array der Größe $n+1$, um die partiellen Summen zu speichern.
*   **Zusätzlicher Speicher:** $O(1)$ über den Eingabespeicher hinaus.
*   **Gesamtspeicher:** $O(n)$, da wir eine lineare Abbildung zwischen den ursprünglichen Array-Elementen und den Baumknoten beibehalten.