# Formale mathematische Spezifikation: BST-Suche

## 1. Definitionen und Notation
Sei $T = (r, T_L, T_R)$ ein Binary Search Tree (BST). Per Definition gilt $\forall x \in T_L, x.val < r.val$ und $\forall y \in T_R, y.val > r.val$.

## 2. Algebraische Charakterisierung
Definiere die Suchfunktion $\mathcal{S}(T, k) \to \{ \text{True}, \text{False} \}$:
$$ \mathcal{S}(T, k) = \begin{cases} 
\text{False} & \text{if } T = \emptyset \\
\text{True} & \text{if } r.val = k \\
\mathcal{S}(T_L, k) & \text{if } k < r.val \\
\mathcal{S}(T_R, k) & \text{if } k > r.val
\end{cases} $$

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** Die Anzahl der rekursiven Aufrufe ist durch die Höhe des Baumes $\mathcal{H}(T)$ begrenzt. Somit ist die Zeit $O(\mathcal{H}(T))$, was in einem balancierten Baum $O(\log |V|)$ und im schlechtesten Fall $O(|V|)$ ist.
- **Platzkomplexität:** Die iterative Auswertung benötigt strikt $O(1)$ Platz. Die rekursive Auswertung benötigt $O(\mathcal{H}(T))$ Platz für den Call Stack.