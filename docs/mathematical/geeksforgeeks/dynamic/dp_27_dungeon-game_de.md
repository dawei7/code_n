# Formale mathematische Spezifikation: Dungeon Game

## 1. Definitionen und Notation
Gitter $M$. Bestimme die minimale initiale Gesundheit bei $(1, 1)$, um $(m, n)$ zu erreichen, während die Gesundheit stets $>0$ bleibt.

## 2. Algebraische Charakterisierung (Rekursionsgleichung)
Iteriere rückwärts von $(m, n)$. Sei $H(i, j)$ die minimale Gesundheit, die bei $(i, j)$ erforderlich ist. $$ H(i, j) = \max(1, \min(H(i+1, j), H(i, j+1)) - M[i, j]) $$

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** $O(nm)$.
- **Platzkomplexität:** $O(n)$ durch Zeilenreduktion.