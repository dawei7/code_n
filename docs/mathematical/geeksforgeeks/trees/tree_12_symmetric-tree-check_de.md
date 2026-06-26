# Formale Mathematische Spezifikation: Symmetrische Baumprüfung

## 1. Definitionen und Notation
Ein Baum $T$ ist symmetrisch, wenn er strukturell und wertmäßig mit seinem Spiegelbild $\mathcal{M}(T)$ identisch ist.
$T = \mathcal{M}(T)$.

## 2. Algebraische Charakterisierung
Definieren Sie eine binäre Prädikatenfunktion $\mathcal{E}(T_A, T_B)$, die die Äquivalenz zwischen einem linken Ast und einem gespiegelten rechten Ast evaluiert:
$$ \mathcal{E}(T_A, T_B) = \begin{cases}
\text{True} & \text{falls } T_A = \emptyset \land T_B = \emptyset \\
\text{False} & \text{falls } (T_A = \emptyset \oplus T_B = \emptyset) \\
r_A = r_B \land \mathcal{E}(T_{A,L}, T_{B,R}) \land \mathcal{E}(T_{A,R}, T_{B,L}) & \text{andernfalls}
\end{cases} $$

Der Baum ist symmetrisch genau dann, wenn $\mathcal{E}(T_L, T_R)$ True ist.

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** Die Prädikatenfunktion prüft jedes Knotenpaar höchstens einmal. $O(|V|)$.
- **Platzkomplexität:** Die Rekursionstiefe ist begrenzt durch $O(\mathcal{H}(T))$.