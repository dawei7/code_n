# Formale mathematische Spezifikation: Wechselgeldproblem (Minimale Anzahl an Münzen)

## 1. Definitionen und Notation
Sei $C = \{c_1 \dots c_k\}$ die Menge der Münzwerte. Die Zielsumme sei $S$. Wir suchen $\min \sum x_i$ unter der Bedingung, dass $\sum x_i c_i = S, x_i \in \mathbb{N}$ gilt.

## 2. Algebraische Charakterisierung (Rekursionsgleichung)
Sei $M(s)$ die minimale Anzahl an Münzen für die Summe $s$. $$ M(s) = \begin{cases} 0 & \text{if } s = 0 \\ \min_{c \in C, c \leq s} M(s - c) + 1 & \text{if } s > 0 \end{cases} $$

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** $O(S \cdot k)$ wobei $k = |C|$.
- **Platzkomplexität:** $O(S)$.