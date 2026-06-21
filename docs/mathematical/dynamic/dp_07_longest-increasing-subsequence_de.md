# Formale mathematische Spezifikation: Longest Increasing Subsequence

## 1. Definitionen und Notation
Sequenz $A = (a_1 \dots a_n)$. Finde die längste Teilsequenz $A_{i_1} < A_{i_2} \dots < A_{i_k}$.

## 2. Algebraische Charakterisierung (Rekursionsgleichung)
Sei $L(i)$ die LIS, die exakt am Index $i$ endet. $$ L(i) = 1 + \max_{1 \leq j < i, A[j] < A[i]} L(j) $$ Das Ergebnis ist $\max_{i} L(i)$.

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** $O(n^2)$ unter Verwendung der Standard-DP-Rekursion. (Optimierbar auf $O(n \log n)$ mittels Patience Sorting).
- **Platzkomplexität:** $O(n)$.