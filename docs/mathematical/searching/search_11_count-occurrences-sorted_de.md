# Formale mathematische Spezifikation: Zählen von Vorkommen in einem sortierten Array

## 1. Definitionen und Notation

Sei $A = [a_0, a_1, \dots, a_{n-1}]$ eine Folge von Ganzzahlen der Länge $n \in \mathbb{N}_0$, wobei die Folge nicht abnehmend ist, sodass $a_i \leq a_{i+1}$ für alle $0 \leq i < n-1$ gilt. Sei $x \in \mathbb{Z}$ der Zielwert.

Wir definieren die folgenden Mengen und Funktionen:
*   **Indexmenge:** $\mathcal{I} = \{0, 1, \dots, n\}$.
*   **Lower-Bound-Funktion:** $L(A, x) = \min \{ i \in \{0, \dots, n\} \mid i = n \lor a_i \geq x \}$.
*   **Upper-Bound-Funktion:** $U(A, x) = \min \{ i \in \{0, \dots, n\} \mid i = n \lor a_i > x \}$.
*   **Anzahl der Vorkommen:** Das Ziel ist die Berechnung der Kardinalität der Menge der Indizes, an denen der Zielwert auftritt:
    $$\mathcal{C}(A, x) = |\{ i \in \{0, \dots, n-1\} \mid a_i = x \}|$$

## 2. Algebraische Charakterisierung

Die Korrektheit des Algorithmus beruht auf den Eigenschaften der Binary-Search-Funktionen $L$ und $U$. Aufgrund der Sortierung von $A$ gelten die folgenden Beziehungen:

**Theorem 1 (Identität der Anzahl):** Die Anzahl der Vorkommen von $x$ in $A$ ergibt sich aus der Differenz der Upper- und Lower-Bounds:
$$\mathcal{C}(A, x) = U(A, x) - L(A, x)$$

**Beweisskizze:**
1. Per Definition ist $L(A, x)$ der kleinste Index $i$, für den $a_i \geq x$ gilt. Falls kein solches $i$ existiert, ist $L(A, x) = n$.
2. Per Definition ist $U(A, x)$ der kleinste Index $j$, für den $a_j > x$ gilt. Falls kein solches $j$ existiert, ist $U(A, x) = n$.
3. Für alle $k$ mit $L(A, x) \leq k < U(A, x)$ muss $a_k = x$ gelten.
4. Somit bilden die Indizes von $x$ ein zusammenhängendes Intervall $[L(A, x), U(A, x) - 1]$. Die Anzahl der Elemente in diesem Intervall beträgt $(U(A, x) - 1) - L(A, x) + 1 = U(A, x) - L(A, x)$.

**Schleifeninvariante:**
Für eine Binary Search über den Bereich $[lo, hi]$ sei $P$ das Prädikat, das die Grenze definiert. Die zu Beginn jeder Iteration aufrechterhaltene Invariante lautet:
*   $0 \leq lo \leq hi \leq n$
*   Für alle $k < lo$ ist $\neg P(a_k)$ wahr.
*   Für alle $k \geq hi$ ist $P(a_k)$ wahr.
Nach Beendigung gilt $lo = hi$, und $lo$ ist der eindeutige Index, der die Grenzbedingung erfüllt.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus führt zwei unabhängige Binary Searches durch. Sei $T(n)$ die Zeitkomplexität.
Jede Binary Search halbiert den Suchraum $\mathcal{S}$ in jedem Schritt $k$. Die Größe des Suchraums im Schritt $k$ ist gegeben durch:
$$|\mathcal{S}_k| = \frac{n}{2^k}$$
Die Suche endet, wenn $|\mathcal{S}_k| = 1$ ist, was $k = \log_2 n$ impliziert.
Da jeder Schritt eine konstante Anzahl an Vergleichen und arithmetischen Operationen umfasst, beträgt der Aufwand pro Suche $W = O(1) \cdot \log_2 n$.
Die gesamte Zeitkomplexität ist:
$$T(n) = T_{lower}(n) + T_{upper}(n) = O(\log n) + O(\log n) = O(\log n)$$

### Platzkomplexität
Der Algorithmus verwendet eine feste Anzahl an Hilfsvariablen (Pointer `lo`, `hi`, `mid` sowie die Rückgabewerte `first`, `last`).
Sei $S(n)$ die zusätzliche Platzkomplexität. Da die Anzahl der Variablen unabhängig von der Eingabegröße $n$ ist, gilt:
$$S(n) = \Theta(1)$$
Der Algorithmus arbeitet in-place auf dem Eingabe-Array $A$, daher beträgt die gesamte Platzkomplexität $O(1)$ zuzüglich des Speichers für die Eingabe.