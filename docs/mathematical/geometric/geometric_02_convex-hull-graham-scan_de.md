# Formale mathematische Spezifikation: Konvexe Hülle (Graham Scan)

## 1. Definitionen und Notation

Sei $P = \{p_1, p_2, \dots, p_N\}$ eine Menge von $N$ Punkten in der euklidischen Ebene $\mathbb{R}^2$, wobei jeder Punkt $p_i = (x_i, y_i)$ ist.

*   **Konvexe Hülle:** Die konvexe Hülle von $P$, bezeichnet als $\text{CH}(P)$, ist die eindeutige minimale konvexe Menge $C \subseteq \mathbb{R}^2$, sodass $P \subseteq C$ gilt. Die Eckpunkte von $\text{CH}(P)$ sind eine Teilmenge von $P$.
*   **Ankerpunkt:** Sei $p_0 \in P$ der Punkt, für den $y_0 = \min_{i} \{y_i\}$ gilt, wobei bei Gleichheit $x_0 = \min \{x_i\}$ zur Entscheidung herangezogen wird.
*   **Polarwinkel:** Für jeden Punkt $p_i \in P \setminus \{p_0\}$ sei $\theta_i = \operatorname{atan2}(y_i - y_0, x_i - x_0)$ der Polarwinkel relativ zu $p_0$.
*   **Kreuzprodukt:** Für ein geordnetes Tripel von Punkten $(A, B, C)$ wird die Orientierung durch das Vorzeichen des Kreuzprodukts der Vektoren $\vec{AB}$ und $\vec{BC}$ bestimmt:
    $$\text{CCW}(A, B, C) = (x_B - x_A)(y_C - y_A) - (y_B - y_A)(x_C - x_A)$$
    *   $\text{CCW} > 0$: Linkskurve (gegen den Uhrzeigersinn).
    *   $\text{CCW} < 0$: Rechtskurve (im Uhrzeigersinn).
    *   $\text{CCW} = 0$: Kollinear.
*   **Zustandsraum:** Der Algorithmus verwaltet einen Stack $S = (s_0, s_1, \dots, s_k)$, wobei $s_i \in P$ und $k$ der aktuelle Index des obersten Stack-Elements ist.

## 2. Algebraische Charakterisierung

Der Graham Scan konstruiert den Rand von $\text{CH}(P)$, indem er eine Sequenz von Punkten beibehält, die die Konvexitätsbedingung erfüllen.

**Sortierung:**
Die Menge $P \setminus \{p_0\}$ wird in eine Sequenz $Q = (q_1, q_2, \dots, q_{N-1})$ sortiert, sodass für jedes $i < j$ entweder $\theta_i < \theta_j$ gilt, oder bei $\theta_i = \theta_j$ die Bedingung $\|\vec{p_0 q_i}\| < \|\vec{p_0 q_j}\|$ erfüllt ist.

**Schleifeninvariante:**
Bei jeder Iteration $m \in \{1, \dots, N-1\}$ enthält der Stack $S$ die Eckpunkte der konvexen Hülle der Menge $\{p_0, q_1, \dots, q_m\}$ in einer Reihenfolge gegen den Uhrzeigersinn.

**Übergangsregel:**
Für einen neuen Punkt $q_m$ stellt der Algorithmus die Invariante sicher, indem er für die obersten zwei Elemente des Stacks $s_{k-1}, s_k$ und den neuen Punkt $q_m$ prüft:
$$\text{CCW}(s_{k-1}, s_k, q_m) > 0$$
Falls $\text{CCW}(s_{k-1}, s_k, q_m) \leq 0$, wird der Punkt $s_k$ vom Stack $S$ entfernt (pop). Dieser Vorgang wird wiederholt, bis die Bedingung erfüllt ist oder $|S| < 2$ gilt. Anschließend wird der Punkt $q_m$ auf den Stack $S$ gelegt (push).

**Korrektheit:**
Der Algorithmus terminiert, wenn $m = N-1$. Da $p_0$ der unterste Punkt ist, ist garantiert, dass er ein Eckpunkt von $\text{CH}(P)$ ist. Die Sortierung nach dem Polarwinkel stellt sicher, dass die Punkte in einem monotonen Winkel-Sweep besucht werden, und die CCW-Bedingung garantiert, dass der Rand strikt konvex bleibt.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die gesamte Zeitkomplexität $T(N)$ ist die Summe aus der Vorverarbeitungsphase und der Scan-Phase:

1.  **Finden des Ankerpunkts:** $T_{anchor} = O(N)$, um einen linearen Scan für die minimale Koordinate durchzuführen.
2.  **Sortierung:** $T_{sort} = O(N \log N)$, um die verbleibenden $N-1$ Punkte basierend auf dem Polarwinkel $\theta$ zu sortieren.
3.  **Scan-Phase:** Die Scan-Phase umfasst eine einzelne Schleife über $N-1$ Punkte. Jeder Punkt $q_i$ wird genau einmal auf den Stack gelegt. Ein Punkt wird höchstens einmal vom Stack entfernt. Somit beträgt die Gesamtzahl der Stack-Operationen $O(N)$.

$$T(N) = O(N) + O(N \log N) + O(N) = O(N \log N)$$

### Platzkomplexität
1.  **Zusätzlicher Speicher:** Der Algorithmus benötigt $O(N)$ Speicherplatz, um die sortierte Liste der Punkte $Q$ zu speichern.
2.  **Stack-Speicher:** Der Stack $S$ speichert im Schlechtesten Fall höchstens $N$ Eckpunkte (z. B. wenn alle Punkte auf der konvexen Hülle liegen).

$$S(N) = O(N) + O(N) = O(N)$$

Der Algorithmus ist im Modell des algebraischen Entscheidungsbaums optimal, da das Problem der Bestimmung der konvexen Hülle eine untere Schranke von $\Omega(N \log N)$ besitzt, was durch die Reduktion vom Sortierproblem begründet ist.