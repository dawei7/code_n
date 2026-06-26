# Formale Mathematische Spezifikation: Maximaler Pfadsummenwert

## 1. Definitionen und Notation
Sei $w: V \to \mathbb{R}$ eine Funktion, die jedem Knoten ein Skalar zuordnet. Wir suchen nach dem Maximum von $\sum_{v \in P} w(v)$ über alle einfachen Pfade $P \subseteq V$.

## 2. Algebraische Charakterisierung
Für einen Knoten $x \in V$ definieren wir $M(x)$ als den maximalen Pfadsummenwert, der bei $x$ beginnt und in höchstens einen seiner Teilbäume absteigt:
$$ M(x) = w(x) + \max(0, M(x_L), M(x_R)) $$
(mit $M(\emptyset) = -\infty$).

Definieren wir $C(x)$ als den maximalen Pfadsummenwert, bei dem $x$ der höchste Knoten auf dem Pfad ist (als verbindendes Vertex fungierend):
$$ C(x) = w(x) + \max(0, M(x_L)) + \max(0, M(x_R)) $$

Der global optimale Pfadsummenwert ist $\max_{x \in V} C(x)$.

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** $M(x)$ und $C(x)$ werden in einer einzigen Post-Order-Traversal berechnet. $O(|V|)$.
- **Platzkomplexität:** $O(\mathcal{H}(T))$.