# Formale mathematische Spezifikation: Longest Common Subsequence

## 1. Definitionen und Notation
Seien $A, B \in \Sigma^*$ Sequenzen der Längen $n, m$. Wir suchen die maximale Länge einer gemeinsamen, nicht notwendigerweise zusammenhängenden Teilsequenz.

## 2. Algebraische Charakterisierung (Rekursionsgleichung)
Sei $L(i, j)$ die LCS von $A[1 \dots i]$ und $B[1 \dots j]$. $$ L(i, j) = \begin{cases} 0 & \text{if } i=0 \lor j=0 \\ L(i-1, j-1) + 1 & \text{if } A[i] = B[j] \\ \max(L(i-1, j), L(i, j-1)) & \text{if } A[i] \neq B[j] \end{cases} $$

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** Die Auswertung von $nm$ Zuständen benötigt $O(nm)$ Zeit.
- **Platzkomplexität:** $O(nm)$, optimierbar auf $O(\min(n, m))$ durch Zeilenreduktion.