# Formale mathematische Spezifikation: Levenshtein-Editierdistanz

## 1. Definitionen und Notation
Strings $A, B$ der Länge $n, m$. Operationen: Einfügen (insert), Löschen (delete), Ersetzen (substitute) (Kosten 1).

## 2. Algebraische Charakterisierung (Rekursionsgleichung)
Sei $E(i, j)$ die Distanz zwischen $A[1 \dots i]$ und $B[1 \dots j]$. $$ E(i, j) = \begin{cases} i & \text{if } j = 0 \\ j & \text{if } i = 0 \\ E(i-1, j-1) & \text{if } A[i] = B[j] \\ 1 + \min(E(i-1, j), E(i, j-1), E(i-1, j-1)) & \text{if } A[i] \neq B[j] \end{cases} $$

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** $O(nm)$.
- **Platzkomplexität:** $O(\min(n, m))$ unter Verwendung von Zeilenreduktion.