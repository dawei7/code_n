# Formale mathematische Spezifikation: BST-Einfügung

## 1. Definitionen und Notation
Sei $T$ ein Binärer Suchbaum (Binary Search Tree, BST) und $k$ ein Skalarwert, der eingefügt werden soll.

## 2. Algebraische Charakterisierung
Die Einfügefunktion $\mathcal{I}(T, k) \to T'$ erzeugt einen neuen strukturell gültigen BST:
$$ \mathcal{I}(T, k) = \begin{cases} 
(k, \emptyset, \emptyset) & \text{falls } T = \emptyset \\
(r, \mathcal{I}(T_L, k), T_R) & \text{falls } k < r.val \\
(r, T_L, \mathcal{I}(T_R, k)) & \text{falls } k > r.val \\
T & \text{falls } k = r.val \text{ (Annahme: keine Duplikate)}
\end{cases} $$

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** Die Pfadverfolgung benötigt $O(\mathcal{H}(T))$ Zeit.
- **Platzkomplexität:** Iterative Manipulation benötigt $O(1)$ zusätzlichen Platz.