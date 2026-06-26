# Formale Mathematische Spezifikation: Post-Order-Traversal

## 1. Definitionen und Notation
Sei $T = (r, T_L, T_R)$ ein binärer Baum.

## 2. Algebraische Charakterisierung
Wir definieren die Post-Order-Traversal-Funktion $\mathcal{O}: \mathcal{T} \to V^*$.
$$ \mathcal{O}(T) = \begin{cases} 
\epsilon & \text{falls } T = \emptyset \\
\mathcal{O}(T_L) \cdot \mathcal{O}(T_R) \cdot r & \text{falls } T = (r, T_L, T_R)
\end{cases} $$

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** $O(|V|)$.
- **Platzkomplexität:** $O(H)$.