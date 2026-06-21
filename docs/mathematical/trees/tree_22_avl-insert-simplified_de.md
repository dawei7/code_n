# Formale mathematische Spezifikation: AVL-Baum-Einfügung

## 1. Definitionen und Notation
Ein AVL-Baum ist ein Binary Search Tree, für den gilt: $\forall x \in V, |\mathcal{H}(x_L) - \mathcal{H}(x_R)| \leq 1$.
Definiere den Balance-Faktor $\delta(x) = \mathcal{H}(x_L) - \mathcal{H}(x_R)$.

## 2. Algebraische Charakterisierung (Rotationen)
Wenn eine Einfügung die AVL-Eigenschaft verletzt (d. h. $\exists x, |\delta(x)| = 2$), wenden wir $O(1)$ Pointer-Rotationen an:
- **Linksrotation $\text{Rot}_L(x)$:** Sei $y = x_R$. $x_R \leftarrow y_L$, $y_L \leftarrow x$.
- **Rechtsrotation $\text{Rot}_R(x)$:** Sei $y = x_L$. $x_L \leftarrow y_R$, $y_R \leftarrow x$.

Balance-Korrekturen werden deterministisch abgebildet:
1. $\delta(x) = 2 \land \delta(x_L) = 1 \implies \text{Rot}_R(x)$
2. $\delta(x) = 2 \land \delta(x_L) = -1 \implies \text{Rot}_L(x_L) \circ \text{Rot}_R(x)$
3. $\delta(x) = -2 \land \delta(x_R) = -1 \implies \text{Rot}_L(x)$
4. $\delta(x) = -2 \land \delta(x_R) = 1 \implies \text{Rot}_R(x_R) \circ \text{Rot}_L(x)$

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** Der Abstieg erfolgt in $O(\mathcal{H}(T))$. Höhenaktualisierungen und Rotationen beim Aufstieg benötigen $O(1)$ pro Ebene. Die gesamte Zeitkomplexität beträgt $O(\mathcal{H}(T)) = O(\log |V|)$.
- **Platzkomplexität:** $O(\log |V|)$ Rekursionstiefe.