# Formale mathematische Spezifikation: Längste wiederholte Teilsequenz

## 1. Definitionen und Notation
Sei $S$ ein String der Länge $n$.
Wir suchen zwei aufsteigende Indexsequenzen $I = (i_1, \dots, i_k)$ und $J = (j_1, \dots, j_k)$, so dass $S_{i_x} = S_{j_x}$ für alle $1 \leq x \leq k$, und streng $i_x \neq j_x$. Wir maximieren $k$.

## 2. Algebraische Charakterisierung (Dynamische Programmierung)
Dies ist äquivalent zum Finden der Längsten Gemeinsamen Teilsequenz von $S$ mit sich selbst, unter Berücksichtigung des Index-Ausschlusses.
Definiere $L(i, j)$ als die Länge der LRS bis zu den Präfixen $i$ und $j$.
$$ L(i, j) = \begin{cases} 
0 & \text{wenn } i = 0 \text{ oder } j = 0 \\
L(i-1, j-1) + 1 & \text{wenn } S[i] = S[j] \land i \neq j \\
\max(L(i-1, j), L(i, j-1)) & \text{wenn } S[i] \neq S[j] \lor i = j
\end{cases} $$

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** $n^2$ Zustände, jeder $O(1)$ zur Auswertung. Die Zeit ist $O(n^2)$.
- **Platzkomplexität:** Die DP-Matrix benötigt $O(n^2)$ Platz, optimierbar auf $O(n)$ durch Beibehaltung nur der vorherigen Zeile.