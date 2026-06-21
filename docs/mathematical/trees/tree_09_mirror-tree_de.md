# Formale Mathematische Spezifikation: Spiegelbaum

## 1. Definitionen und Notation
Sei $T = (r, T_L, T_R)$ ein binärer Baum.

## 2. Algebraische Charakterisierung
Die Spiegelungsfunktion $\mathcal{M}: \mathcal{T} \to \mathcal{T}$ ist eine Involution ($\mathcal{M}(\mathcal{M}(T)) = T$) definiert durch:
$$ \mathcal{M}(T) = \begin{cases}
\emptyset & \text{falls } T = \emptyset \\
(r, \mathcal{M}(T_R), \mathcal{M}(T_L)) & \text{falls } T = (r, T_L, T_R)
\end{cases} $$

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** Jeder Knoten wird genau einmal besucht und seine Kinder werden vertauscht. $O(|V|)$.
- **Platzkomplexität:** $O(\mathcal{H}(T))$.