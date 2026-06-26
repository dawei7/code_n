# Formale mathematische Spezifikation: Binary Search

## 1. Definitionen und Notation

Sei $A = (a_0, a_1, \dots, a_{n-1})$ eine Sequenz von Elementen aus einer total geordneten Menge $(\mathcal{X}, \le)$. Die Sequenz ist so sortiert, dass $a_i \le a_{i+1}$ für alle $0 \le i < n-1$ gilt. Gegeben ein Zielwert $t \in \mathcal{X}$, ist das Ziel, einen Index $k \in \{0, 1, \dots, n-1\}$ zu bestimmen, sodass $a_k = t$, oder einen Sentinel-Wert $\bot \notin \{0, \dots, n-1\}$ zurückzugeben, falls kein solches $k$ existiert.

Wir definieren den Zustand des Algorithmus in der Iteration $m$ durch das Tupel $(L_m, R_m)$, wobei $L_m, R_m \in \mathbb{Z}$ die inklusiven Grenzen des Suchintervalls $[L_m, R_m]$ repräsentieren. Der Anfangszustand ist $(L_0, R_0) = (0, n-1)$.

## 2. Algebraische Charakterisierung

Der Algorithmus wird durch eine Schleifeninvariante $\mathcal{I}(L, R)$ gesteuert, die besagt, dass, falls $t$ in $A$ existiert, dessen Index innerhalb des abgeschlossenen Intervalls $[L, R]$ liegen muss.

**Invariante:**
$$\mathcal{I}(L, R) \equiv \forall k \in \{0, \dots, n-1\} : (a_k = t) \implies (L \le k \le R)$$

**Übergangsfunktion:**
Sei $M_m = \lfloor \frac{L_m + R_m}{2} \rfloor$. Der Zustandsübergang $(L_m, R_m) \to (L_{m+1}, R_{m+1})$ ist durch die Trichotomie der geordneten Menge $\mathcal{X}$ definiert:

1. Wenn $a_{M_m} = t$, terminiert der Algorithmus und gibt $M_m$ zurück.
2. Wenn $a_{M_m} < t$, dann gilt für alle $k \le M_m$, dass $a_k \le a_{M_m} < t$. Somit ist $a_k \neq t$. Der neue Zustand ist $(L_{m+1}, R_{m+1}) = (M_m + 1, R_m)$.
3. Wenn $a_{M_m} > t$, dann gilt für alle $k \ge M_m$, dass $a_k \ge a_{M_m} > t$. Somit ist $a_k \neq t$. Der neue Zustand ist $(L_{m+1}, R_{m+1}) = (L_m, M_m - 1)$.

**Terminierung:**
Der Algorithmus terminiert, wenn $L_m > R_m$. An diesem Punkt impliziert die Invariante $\mathcal{I}(L_m, R_m)$, dass die Menge der Indizes $\{k \mid L_m \le k \le R_m\}$ leer ist. Folglich existiert kein $k$, sodass $a_k = t$, und der Algorithmus gibt $\bot$ zurück.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Sei $N_m = R_m - L_m + 1$ die Größe des Suchraums in der Iteration $m$. In jeder Iteration führt der Algorithmus eine konstante Anzahl von Operationen $c$ aus, um $M_m$ zu berechnen und $a_{M_m}$ mit $t$ zu vergleichen. Die Größe des Suchraums entwickelt sich wie folgt:
$$N_{m+1} \le \left\lfloor \frac{N_m}{2} \right\rfloor$$
Diese Rekurrenz $T(n) = T(n/2) + O(1)$ beschreibt die Halbierung des Suchraums. Nach dem Master-Theorem (Fall 2), wobei $a=1, b=2, f(n)=O(1)$, erhalten wir:
$$T(n) = \Theta(n^{\log_b a}) = \Theta(n^0 \log n) = O(\log n)$$
Die Anzahl der Iterationen $m$ im Schlechtesten Fall ist die kleinste Ganzzahl, für die $N_m < 1$ gilt, was $n/2^m < 1$ erfüllt und zu $m = \lceil \log_2(n+1) \rceil$ führt.

### Platzkomplexität
Der Algorithmus verwaltet eine feste Anzahl von skalaren Variablen $(L, R, M, \text{value})$ unabhängig von der Eingabegröße $n$.
- **Zusätzlicher Speicherplatz:** Die iterative Implementierung benötigt $O(1)$ zusätzlichen Speicherplatz, um die Pointer und den Index des Mittelpunkts zu speichern.
- **Gesamtspeicherplatz:** Die Platzkomplexität beträgt $O(n)$, um das Eingabe-Array $A$ zu speichern, aber der Speicherbedarf des Algorithmus selbst ist $O(1)$ relativ zur Eingabe.