# Formale mathematische Spezifikation: Unique Paths

## 1. Definitionen und Notation
Gitter $m \times n$. Ein Pfad verläuft nur nach unten oder nach rechts. Bestimme die Gesamtzahl der Pfade von $(1, 1)$ nach $(m, n)$.

## 2. Algebraische Charakterisierung (Rekursionsgleichung)
Sei $U(i, j)$ die Anzahl der Pfade, um $(i, j)$ zu erreichen. $$ U(i, j) = \begin{cases} 1 & \text{if } i = 1 \lor j = 1 \\ U(i-1, j) + U(i, j-1) & \text{otherwise} \end{cases} $$

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** $O(nm)$. (Alternativ berechnet die Kombinatorik $\binom{m+n-2}{m-1}$ in $O(m)$ Zeit).
- **Platzkomplexität:** $O(n)$ Speicherplatz durch Zeilenoptimierung.