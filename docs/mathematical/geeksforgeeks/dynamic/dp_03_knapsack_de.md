# Formale mathematische Spezifikation: 0/1-Knapsack-Problem

## 1. Definitionen und Notation
Sei $\mathcal{I} = \{1, \dots, n\}$ eine Menge von Objekten, wobei Objekt $i$ das Gewicht $w_i > 0$ und den Wert $v_i > 0$ besitzt. Sei $W$ die Kapazitätsbeschränkung.

## 2. Algebraische Charakterisierung (Rekursionsgleichung)
Sei $K(i, w)$ der maximale Wert, der unter Verwendung einer Teilmenge von $\{1 \dots i\}$ mit einem Gesamtgewicht $\leq w$ erreichbar ist. $$ K(i, w) = \begin{cases} 0 & \text{if } i = 0 \lor w = 0 \\ K(i-1, w) & \text{if } w_i > w \\ \max(K(i-1, w), K(i-1, w - w_i) + v_i) & \text{if } w_i \leq w \end{cases} $$

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** Die Matrix besitzt $n \times W$ Zustände. Jeder Übergang ist $O(1)$. Die Gesamtlaufzeit beträgt $O(nW)$.
- **Platzkomplexität:** $O(nW)$, was auf $O(W)$ reduziert werden kann, da die Berechnung von Zeile $i$ lediglich die Zeile $i-1$ erfordert.