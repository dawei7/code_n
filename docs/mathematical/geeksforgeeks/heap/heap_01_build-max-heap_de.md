# Formale mathematische Spezifikation: Build Max Heap (Heapify)

## 1. Definitionen und Notation

Sei $A = [a_0, a_1, \dots, a_{n-1}]$ ein Array von $n$ Elementen aus einer total geordneten Menge $(\mathcal{X}, \leq)$. Wir definieren die Struktur als einen vollständigen Binärbaum $T$, der auf die Array-Indizes $I = \{0, 1, \dots, n-1\}$ abgebildet ist.

*   **Eltern-Kind-Abbildung:** Für jeden Index $i \in I$ sind das linke Kind $L(i)$ und das rechte Kind $R(i)$ definiert als:
    $L(i) = 2i + 1$
    $R(i) = 2i + 2$
    vorausgesetzt, $L(i), R(i) < n$.
*   **Max-Heap-Eigenschaft:** Eine Sequenz $A$ erfüllt die Max-Heap-Eigenschaft genau dann, wenn für alle $i$ mit $0 \leq i < \lfloor n/2 \rfloor$ gilt:
    $a_i \geq a_{L(i)}$ (falls $L(i) < n$)
    $a_i \geq a_{R(i)}$ (falls $R(i) < n$)
*   **Zustandsraum:** Der Algorithmus operiert auf dem Raum aller Permutationen des Eingabe-Arrays, $\mathcal{S} = \text{Perm}(A)$. Das Ziel ist es, einen Zustand $A^* \in \mathcal{S}$ zu erreichen, sodass $A^*$ die Max-Heap-Eigenschaft erfüllt.

## 2. Algebraische Charakterisierung

Der Algorithmus verwendet die `sift_down`-Prozedur, bezeichnet als $\text{SD}(i, n)$, welche die Heap-Eigenschaft für einen Teilbaum mit Wurzel $i$ wiederherstellt, unter der Annahme, dass die Teilbäume mit den Wurzeln $L(i)$ und $R(i)$ bereits gültige Max-Heaps sind.

**Schleifeninvariante:**
Für die Hauptschleife, die $k$ von $\lfloor n/2 \rfloor - 1$ abwärts bis $0$ iteriert:
Zu Beginn jeder Iteration $k$ bildet das Subarray $A[k+1 \dots n-1]$ einen Wald aus gültigen Max-Heaps. Speziell gilt für alle $j > k$, dass der Teilbaum mit Wurzel $j$ die Max-Heap-Eigenschaft erfüllt.

**Rekursive Definition von `sift_down`:**
Sei $m$ der Index des größten Elements in der Menge $\{i, L(i), R(i)\} \cap I$.
Falls $m \neq i$:
1. Vertausche $a_i$ und $a_m$.
2. $\text{SD}(m, n)$ wird rekursiv aufgerufen.
Falls $m = i$, ist die Eigenschaft für den Index $i$ erfüllt und die Rekursion terminiert.

**Korrektheit:**
Durch Induktionsbeweis über $k$: Da der Induktionsanfang $k = \lfloor n/2 \rfloor - 1$ damit beginnt, dass alle Knoten $j > k$ Blätter sind (die die Eigenschaft trivialerweise erfüllen), und jeder Aufruf von $\text{SD}(k, n)$ die Eigenschaft für den Teilbaum mit Wurzel $k$ bewahrt, stellt der Endzustand bei $k=0$ sicher, dass der gesamte Baum ein Max-Heap ist.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität wird durch die Summe der Kosten von $\text{SD}(i, n)$ für alle $i$ von $\lfloor n/2 \rfloor - 1$ abwärts bis $0$ bestimmt.
Sei $h$ die Höhe des Baums, $h = \lfloor \log_2 n \rfloor$. Ein Knoten auf der Höhe $d$ (wobei Blätter auf $d=0$ liegen) kann höchstens $d$ Vertauschungen durchführen.

Die Anzahl der Knoten auf der Höhe $d$ beträgt höchstens $\lceil n / 2^{d+1} \rceil$. Der Gesamtaufwand $W(n)$ ist:
$$W(n) = \sum_{d=0}^{\lfloor \log_2 n \rfloor} \lceil \frac{n}{2^{d+1}} \rceil \cdot O(d)$$
$$W(n) = O\left( n \sum_{d=0}^{\infty} \frac{d}{2^d} \right)$$

Unter Verwendung der Identität für arithmetisch-geometrische Reihen $\sum_{d=0}^{\infty} d x^d = \frac{x}{(1-x)^2}$ für $|x| < 1$, mit $x = 1/2$:
$$\sum_{d=0}^{\infty} \frac{d}{2^d} = \frac{1/2}{(1 - 1/2)^2} = \frac{1/2}{1/4} = 2$$
Daraus folgt $W(n) = O(2n) = O(n)$.

### Platzkomplexität
*   **Zusätzlicher Speicherplatz:** Die iterative Implementierung von `sift_down` benötigt nur eine konstante Anzahl an Pointern und temporären Variablen für den Tauschvorgang, was zu einer Platzkomplexität von $O(1)$ für den zusätzlichen Speicher führt.
*   **Gesamtspeicherplatz:** Der Algorithmus arbeitet in-place auf dem Eingabe-Array $A$ und benötigt $O(n)$ Gesamtspeicherplatz zur Speicherung der Daten. Falls die rekursive Implementierung verwendet wird, fügt der Call Stack $O(\log n)$ Speicherplatz hinzu, was jedoch für die optimale $O(1)$-Schranke für zusätzlichen Speicher nicht erforderlich ist.