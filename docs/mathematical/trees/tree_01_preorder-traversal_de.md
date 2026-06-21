# Formale mathematische Spezifikation: Pre-order-Traversal

## 1. Definitionen und Notation
Sei $T$ ein binärer Baum, der rekursiv definiert ist als entweder leer ($\emptyset$) oder ein Tupel $T = (r, T_L, T_R)$, wobei $r \in V$ der Wurzelknoten ist und $T_L, T_R$ binäre Bäume sind, die die linken und rechten Teilbäume repräsentieren.
Sei $V$ die Menge aller Knoten in $T$.

## 2. Algebraische Charakterisierung
Wir definieren die Pre-order-Traversal-Funktion $\mathcal{P}: \mathcal{T} \to V^*$ (die einen Baum auf eine Sequenz von Knoten abbildet).
$$ \mathcal{P}(T) = \begin{cases} 
\epsilon & \text{wenn } T = \emptyset \\
r \cdot \mathcal{P}(T_L) \cdot \mathcal{P}(T_R) & \text{wenn } T = (r, T_L, T_R)
\end{cases} $$
wobei $\cdot$ die Sequenzkonkatenation bezeichnet und $\epsilon$ die leere Sequenz ist.

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** Die Funktion $\mathcal{P}$ wird genau einmal pro Knoten $v \in V$ angewendet. Somit ist die Zeit $O(|V|)$.
- **Platzkomplexität:** Die Rekursionstiefe ist durch die Höhe des Baumes $H$ begrenzt. Der Platzbedarf ist $O(H)$.