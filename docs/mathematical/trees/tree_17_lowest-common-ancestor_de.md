# Formale mathematische Spezifikation: Lowest Common Ancestor (LCA)

## 1. Definitionen und Notation
Seien $u, v \in V$. Ein Knoten $a$ ist ein Vorfahre von $x$, wenn $a$ auf dem Pfad von der Wurzel zu $x$ liegt. 
Der Lowest Common Ancestor $\text{LCA}(u, v)$ ist derjenige Knoten $a$, der ein Vorfahre von sowohl $u$ als auch $v$ ist, sodass $d(\text{root}, a)$ maximiert wird.

## 2. Algebraische Charakterisierung
Für einen allgemeinen Binärbaum sei $f(T)$ eine Funktion, die $T$ zurückgibt, falls $T = u$ oder $T = v$, und andernfalls rekursiv berechnet wird:
$$ L = f(T_L), \quad R = f(T_R) $$
$$ \text{LCA}(T) = \begin{cases} 
T & \text{if } T \in \{u, v\} \\
T & \text{if } L \neq \emptyset \land R \neq \emptyset \\
L \text{ or } R & \text{if exactly one of } L, R \neq \emptyset \\
\emptyset & \text{otherwise}
\end{cases} $$

*(Für einen BST liefert die Strukturinvariante den $\text{LCA}$ direkt durch das Finden des ersten Knotens $a$, für den $\min(u, v) \leq a.val \leq \max(u, v)$ gilt).*

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** Ein allgemeiner Binärbaum erfordert eine vollständige Traversierung, $O(|V|)$. Ein BST ermöglicht eine binäre Suche, beschränkt durch $O(\mathcal{H}(T))$.
- **Platzkomplexität:** $O(\mathcal{H}(T))$.