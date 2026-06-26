# Formale mathematische Spezifikation: K-kleinstes Element in einem BST

## 1. Definitionen und Notation
Sei $T$ ein BST mit $n$ Knoten. Wir suchen den Knoten $v$, dessen Wert den Rang $k$ in der sortierten Sequenz von $V$ besitzt.

## 2. Algebraische Charakterisierung
Aufgrund der BST-Eigenschaft ist die durch die In-order-Traversierung $\mathcal{I}(T)$ erzeugte Sequenz monoton.
Der gesuchte Knoten ist genau das $k$-te Element von $\mathcal{I}(T)$.

Wenn Knoten um ein `size`-Attribut $S(v) = 1 + S(v_L) + S(v_R)$ erweitert werden, kann die Suche ohne vollständige Traversierung rekursiv gesteuert werden:
$$ \text{Find}(T, k) = \begin{cases} 
T & \text{if } k = S(T_L) + 1 \\
\text{Find}(T_L, k) & \text{if } k \leq S(T_L) \\
\text{Find}(T_R, k - S(T_L) - 1) & \text{if } k > S(T_L) + 1
\end{cases} $$

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** Eine explizite In-order-Traversierung benötigt $O(\mathcal{H}(T) + k)$ Zeit. Die Suche mittels des erweiterten `size`-Attributs operiert in strikter $O(\mathcal{H}(T))$ Zeit.
- **Platzkomplexität:** $O(\mathcal{H}(T))$.