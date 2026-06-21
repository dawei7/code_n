# Formale mathematische Spezifikation: Überprüfung auf symmetrische Bäume

## 1. Definitionen und Notation
Ein Baum $T$ ist symmetrisch, wenn er strukturell und wertmäßig identisch mit seinem Spiegelbild $\mathcal{M}(T)$ ist.
$T = \mathcal{M}(T)$.

## 2. Algebraische Charakterisierung
Definieren wir ein binäres Prädikat $\mathcal{E}(T_A, T_B)$, das die Äquivalenz zwischen einem linken Zweig und einem gespiegelten rechten Zweig evaluiert:
$$ \mathcal{E}(T_A, T_B) = \begin{cases}
\text{True} & \text{if } T_A = \emptyset \land T_B = \emptyset \\
\text{False} & \text{if } (T_A = \emptyset \oplus T_B = \emptyset) \\
r_A = r_B \land \mathcal{E}(T_{A,L}, T_{B,R}) \land \mathcal{E}(T_{A,R}, T_{B,L}) & \text{otherwise}
\end{cases} $$

Der Baum ist genau dann symmetrisch, wenn $\mathcal{E}(T_L, T_R)$ den Wert True ergibt.

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** Das Prädikat überprüft jedes Knotenpaar höchstens einmal. $O(|V|)$.
- **Platzkomplexität:** Die Rekursionstiefe ist durch $O(\mathcal{H}(T))$ beschränkt.