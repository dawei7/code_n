# Formale Mathematische Spezifikation: Heap Sort

## 1. Definitionen und Notation

Sei $A = [a_0, a_1, \dots, a_{n-1}]$ ein Array von $n$ Elementen, entnommen aus einer total geordneten Menge $(\mathcal{X}, \le)$. Das Ziel des Algorithmus ist es, eine Permutation $A'$ von $A$ zu erzeugen, sodass $a'_0 \le a'_1 \le \dots \le a'_{n-1}$ gilt.

Wir definieren einen **Binären Max-Heap** als einen vollständigen Binärbaum, der auf ein Array $A$ der Länge $n$ abgebildet wird, wobei für jeden Knoten am Index $i$ (wobei $0 \le i < n$) die folgende **Heap Property** gilt:
- Falls $2i + 1 < n$, dann $a_i \ge a_{2i+1}$ (Linke Kind-Bedingung).
- Falls $2i + 2 < n$, dann $a_i \ge a_{2i+2}$ (Rechte Kind-Bedingung).

Sei $\text{sift\_down}(A, i, k)$ eine Funktion, die die Heap Property für einen Teilbaum, der an $i$ verwurzelt ist, innerhalb eines Array-Segments der Länge $k$ wiederherstellt, unter der Annahme, dass die Teilbäume, die an $2i+1$ und $2i+2$ verwurzelt sind, die Heap Property bereits erfüllen.

## 2. Algebraische Charakterisierung

Der Algorithmus läuft in zwei unterschiedlichen Phasen ab, die durch die folgenden Invarianten gekennzeichnet sind:

### Phase 1: Max-Heap Aufbau
Wir transformieren das beliebige Array $A$ in einen Max-Heap. Wir definieren den Zustand nach der $j$-ten Iteration des Aufbauprozesses (für $j$ von $\lfloor n/2 \rfloor - 1$ absteigend bis $0$) wie folgt:
- **Invariante:** Für alle $k > j$ erfüllt der an $k$ verwurzelte Teilbaum die Max-Heap Property.
- **Übergang:** $\text{sift\_down}(A, j, n)$ stellt sicher, dass der an $j$ verwurzelte Teilbaum die Property erfüllt, wodurch die Invariante auf $k \ge j$ erweitert wird.

### Phase 2: Extrahieren und Sortieren
Sei $A^{(m)}$ der Zustand des Arrays nach $m$ Extraktionen, wobei $0 \le m < n$. Das Array ist in zwei Segmente unterteilt: einen Heap $H_m = A[0 \dots n-m-1]$ und ein sortiertes Suffix $S_m = A[n-m \dots n-1]$.
- **Invariante:**
  1. $H_m$ ist ein gültiger Max-Heap.
  2. $\forall x \in H_m, \forall y \in S_m : x \le y$.
  3. $S_m$ ist in nicht-absteigender Reihenfolge sortiert.
- **Übergang:**
  1. Tausch: $A[0] \leftrightarrow A[n-m-1]$.
  2. Wiederherstellung: $\text{sift\_down}(A, 0, n-m-1)$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die gesamte Zeitkomplexität $T(n)$ ist die Summe der Zeit für die Aufbauphase $T_B(n)$ und die Extraktionsphase $T_E(n)$.

**1. Aufbauphase:**
Die Kosten von $\text{sift\_down}$ auf Höhe $h$ betragen $O(h)$. In einem vollständigen Binärbaum mit $n$ Knoten gibt es höchstens $\lceil n/2^{h+1} \rceil$ Knoten auf Höhe $h$. Die gesamte Arbeit beträgt:
$$T_B(n) = \sum_{h=0}^{\lfloor \log n \rfloor} \left\lceil \frac{n}{2^{h+1}} \right\rceil O(h) = O\left( n \sum_{h=0}^{\infty} \frac{h}{2^h} \right)$$
Da die geometrische Reihe $\sum_{h=0}^{\infty} h x^h$ für $|x|<1$ gegen $\frac{x}{(1-x)^2}$ konvergiert, konvergiert die Summation gegen eine Konstante. Daher ist $T_B(n) = O(n)$.

**2. Extraktionsphase:**
Wir führen $n-1$ Extraktionen durch. Jede Extraktion beinhaltet einen Tausch ($O(1)$) und eine $\text{sift\_down}$-Operation auf einem Heap der Größe höchstens $n$. Die Höhe des Heaps ist $\lfloor \log k \rfloor$ für einen Heap der Größe $k$.
$$T_E(n) = \sum_{k=1}^{n-1} O(\log k) = O(\log((n-1)!)) = O(n \log n)$$
Durch Kombination dieser Ergebnisse ergibt sich $T(n) = O(n) + O(n \log n) = O(n \log n)$.

### Platzkomplexität
Der Algorithmus arbeitet strikt in-place. Er benötigt eine konstante Anzahl von Hilfsvariablen (Pointern/Indizes wie `root`, `child`, `start`, `end`), unabhängig von der Eingabegröße $n$.
$$S(n) = O(1)$$
Daher ist Heap Sort ein Sortieralgorithmus mit optimaler Platzkomplexität.