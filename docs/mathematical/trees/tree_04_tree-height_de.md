# Formale Mathematische Spezifikation: Baumhöhe

## 1. Definitionen und Notation
Sei $T$ ein Binärbaum. Die Höhe $\mathcal{H}(T)$ ist definiert als die maximale Anzahl von Kanten auf dem längsten Pfad von der Wurzel zu einem beliebigen Blatt.

## 2. Algebraische Charakterisierung
$$ \mathcal{H}(T) = \begin{cases} 
0 & \text{falls } T = \emptyset \\
1 + \max(\mathcal{H}(T_L), \mathcal{H}(T_R)) & \text{falls } T = (r, T_L, T_R)
\end{cases} $$
*(Hinweis: Wenn die Höhe durch Knoten statt durch Kanten definiert wird, ist der Basisfall für einen leeren Baum 0 und ein einzelner Knoten 1).*

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** $O(|V|)$.
- **Platzkomplexität:** $O(\mathcal{H}(T))$.