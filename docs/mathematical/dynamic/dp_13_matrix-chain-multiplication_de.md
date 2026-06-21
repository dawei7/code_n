# Formale mathematische Spezifikation: Matrix Chain Multiplication

## 1. Definitionen und Notation
Matrizen $A_1 \dots A_n$ mit den Dimensionen $p_0 \dots p_n$. Minimierung der skalaren Multiplikationen.

## 2. Algebraische Charakterisierung (Rekursionsgleichung)
Sei $M(i, j)$ die minimale Anzahl an Operationen, um $A_i \dots A_j$ zu multiplizieren. $$ M(i, j) = \begin{cases} 0 & \text{if } i = j \\ \min_{i \leq k < j} (M(i, k) + M(k+1, j) + p_{i-1}p_k p_j) & \text{if } i < j \end{cases} $$

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** $O(n^3)$ aufgrund der Iteration über die Intervalllänge und der Auswahl des Pivot-Elements.
- **Platzkomplexität:** $O(n^2)$.