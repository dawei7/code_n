# Formale mathematische Spezifikation: In-order-Traversal

## 1. Definitionen und Notation
Sei $T = (r, T_L, T_R)$ ein Binärbaum.

## 2. Algebraische Charakterisierung
Wir definieren die In-order-Traversal-Funktion $\mathcal{I}: \mathcal{T} \to V^*$.
$$ \mathcal{I}(T) = \begin{cases} 
\epsilon & \text{falls } T = \emptyset \\
\mathcal{I}(T_L) \cdot r \cdot \mathcal{I}(T_R) & \text{falls } T = (r, T_L, T_R)
\end{cases} $$

**Satz (BST-Eigenschaft):** Wenn $T$ ein Binärer Suchbaum (Binary Search Tree) ist, ist die Sequenz $\mathcal{I}(T)$ monoton nicht abnehmend.

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** $O(|V|)$, da jeder Knoten einmal besucht wird.
- **Platzkomplexität:** $O(H)$, wobei $H$ die Baumhöhe ist.