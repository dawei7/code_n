# Formale mathematische Spezifikation: Sliding Window Maximum

## 1. Definitionen und Notation

Sei $A = [a_0, a_1, \dots, a_{n-1}]$ eine Folge von Integern der Länge $n$, wobei $a_i \in \mathbb{Z}$. Sei $k \in \mathbb{Z}^+$ die Fenstergröße, sodass $1 \le k \le n$.

Wir definieren ein Sliding Window der Größe $k$, das am Index $i$ beginnt, als die Teilfolge $W_i = [a_i, a_{i+1}, \dots, a_{i+k-1}]$ für $0 \le i \le n-k$.

Das Ziel ist die Berechnung der Folge $M = [m_0, m_1, \dots, m_{n-k}]$, wobei jedes Element $m_i$ als das Supremum des Fensters $W_i$ definiert ist:
$$m_i = \max \{a_j \mid i \le j \le i+k-1\}$$

Wir definieren den Zustandsraum $\mathcal{S}$ der monotonen Deque als eine Folge von Indizes $Q = [q_1, q_2, \dots, q_m]$, sodass gilt:
1. **Index-Ordnung:** $i-k < q_1 < q_2 < \dots < q_m \le i$.
2. **Monotonie:** $a_{q_1} > a_{q_2} > \dots > a_{q_m}$.

## 2. Algebraische Charakterisierung

Die Korrektheit des Ansatzes mit der monotonen Deque beruht auf der Aufrechterhaltung der Invariante $\mathcal{I}$ bei jedem Schritt $i \in \{0, \dots, n-1\}$:

**Schleifeninvariante $\mathcal{I}$:** Für jeden Index $j \in \{i-k+1, \dots, i\}$ gilt: Wenn $j$ nicht in $Q$ enthalten ist, dann existiert ein $q \in Q$, sodass $q > j$ und $a_q \ge a_j$.

**Übergangsregeln:**
Sei $Q^{(i)}$ der Zustand der Deque nach der Verarbeitung des Index $i$.
1. **Entfernung veralteter Indizes:** $Q' = \{q \in Q^{(i-1)} \mid q > i-k\}$.
2. **Aufrechterhaltung der Monotonie:** Sei $Q''$ die Folge, die durch das Entfernen aller $q \in Q'$ entsteht, für die $a_q \le a_i$ gilt.
3. **Update:** $Q^{(i)} = Q'' \cup \{i\}$.

Das Maximum des aktuellen Fensters $W_i$ ist durch das erste Element (head) der Deque gegeben:
$$m_i = a_{q_1} \quad \text{wobei } q_1 = \text{head}(Q^{(i)})$$

Dies gilt, da andernfalls, wenn $a_{q_1}$ nicht das Maximum wäre, ein Index $j \in \{i-k+1, \dots, i\}$ existieren müsste, für den $a_j > a_{q_1}$ gilt. Aufgrund der Konstruktion von $Q$ hätte jedoch jeder Index $j$, der zur Deque hinzugefügt wird und $a_j > a_{q_1}$ erfüllt, dazu geführt, dass $q_1$ während des Schritts "Aufrechterhaltung der Monotonie" entfernt worden wäre, was der Existenz von $q_1$ an der Spitze widerspricht.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus verarbeitet jeden Index $i \in \{0, \dots, n-1\}$ genau einmal.
Sei $T(n)$ die gesamte Zeitkomplexität. Die in jedem Schritt $i$ ausgeführten Operationen sind:
1. `popleft()`: $O(1)$
2. `pop()`: $O(1)$ pro entferntem Element.
3. `append()`: $O(1)$

Sei $c_i$ die Anzahl der Elemente, die im Schritt $i$ aus der Deque entfernt werden. Die Gesamtlaufzeit beträgt:
$$T(n) = \sum_{i=0}^{n-1} (1 + c_i)$$
Da jeder Index $j \in \{0, \dots, n-1\}$ genau einmal zur Deque hinzugefügt wird, kann er höchstens einmal entfernt werden. Somit gilt $\sum_{i=0}^{n-1} c_i \le n$.
Daraus folgt $T(n) = O(n) + O(n) = O(n)$. Die amortisierte Zeitkomplexität pro Schritt beträgt $O(1)$.

### Platzkomplexität
Die Platzkomplexität wird durch die maximale Größe der Deque $Q$ bestimmt.
Im Schlechtesten Fall (eine streng monoton fallende Eingabefolge) speichert die Deque alle $k$ Elemente des aktuellen Fensters.
$$|Q| \le k$$
Somit beträgt die zusätzliche Platzkomplexität $O(k)$. Die gesamte Platzkomplexität, einschließlich der Eingabe- und Ausgabe-Arrays, beträgt $O(n + k) = O(n)$.