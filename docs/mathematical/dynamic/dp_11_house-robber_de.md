# Formale mathematische Spezifikation: House Robber

## 1. Definitionen und Notation
Vermögens-Array $W = (w_1 \dots w_n)$. Maximierung der Summe ohne Auswahl benachbarter Elemente.

## 2. Algebraische Charakterisierung (Rekursionsgleichung)
Sei $H(i)$ das maximale Vermögen aus den ersten $i$ Häusern. $$ H(i) = \begin{cases} 0 & \text{if } i = 0 \\ w_1 & \text{if } i = 1 \\ \max(H(i-1), H(i-2) + w_i) & \text{if } i > 1 \end{cases} $$

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** $O(n)$.
- **Platzkomplexität:** $O(1)$, wobei nur die letzten zwei Zustände gespeichert werden.