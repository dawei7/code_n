# Formale mathematische Spezifikation: Quickhull (Konvexe Hülle)

## 1. Definitionen und Notation

Sei $S = \{p_1, p_2, \dots, p_n\}$ eine Menge von $n$ Punkten in der euklidischen Ebene $\mathbb{R}^2$, wobei jeder Punkt $p_i = (x_i, y_i)$ ist.

*   **Konvexe Hülle:** Die konvexe Hülle von $S$, bezeichnet als $\text{CH}(S)$, ist die eindeutige minimale konvexe Menge $K \subseteq \mathbb{R}^2$, sodass $S \subseteq K$ gilt. Äquivalent dazu ist $\text{CH}(S)$ der Schnitt aller konvexen Mengen, die $S$ enthalten.
*   **Orientierungsfunktion:** Für ein geordnetes Tripel von Punkten $(A, B, P)$ definieren wir die Orientierungsfunktion $\Omega: (\mathbb{R}^2)^3 \to \mathbb{R}$ als die Determinante:
    $$\Omega(A, B, P) = \det \begin{pmatrix} x_A & y_A & 1 \\ x_B & y_B & 1 \\ x_P & y_P & 1 \end{pmatrix} = (x_B - x_A)(y_P - y_A) - (y_B - y_A)(x_P - x_A)$$
    Das Vorzeichen von $\Omega$ bestimmt die Seite der gerichteten Geraden $\vec{AB}$, auf der $P$ liegt:
    *   $\Omega > 0$: $P$ liegt links von $\vec{AB}$.
    *   $\Omega < 0$: $P$ liegt rechts von $\vec{AB}$.
    *   $\Omega = 0$: $P$ ist kollinear zu $AB$.
*   **Abstandsfunktion:** Der senkrechte Abstand $d(P, \vec{AB})$ vom Punkt $P$ zur Geraden durch $A$ und $B$ ist proportional zu $|\Omega(A, B, P)|$:
    $$d(P, \vec{AB}) = \frac{|\Omega(A, B, P)|}{\|B - A\|_2}$$

## 2. Algebraische Charakterisierung

Der Quickhull-Algorithmus basiert auf der Eigenschaft, dass Extrempunkte in einer gegebenen Richtung zur konvexen Hülle gehören müssen.

**Initialpartitionierung:**
Sei $p_{min} = \arg \min_{p \in S} x_p$ und $p_{max} = \arg \max_{p \in S} x_p$. Die Menge $S$ wird basierend auf der Orientierung relativ zur gerichteten Geraden $\vec{p_{min}p_{max}}$ in zwei Teilmengen partitioniert:
$$S_1 = \{p \in S \mid \Omega(p_{min}, p_{max}, p) > 0\}, \quad S_2 = \{p \in S \mid \Omega(p_{min}, p_{max}, p) < 0\}$$

**Rekursiver Schritt:**
Für ein gerichtetes Liniensegment $\vec{AB}$ und eine Menge von Punkten $S_{sub}$, die auf einer Seite liegen, definieren wir den am weitesten entfernten Punkt $P_{far}$ als:
$$P_{far} = \arg \max_{p \in S_{sub}} \Omega(A, B, p)$$
Der Algorithmus verarbeitet anschließend rekursiv die zwei neuen Mengen, die durch das Dreieck $\triangle ABP_{far}$ definiert sind:
1. $S_{left} = \{p \in S_{sub} \mid \Omega(A, P_{far}, p) > 0\}$
2. $S_{right} = \{p \in S_{sub} \mid \Omega(P_{far}, B, p) > 0\}$

**Invariante:**
In jedem rekursiven Schritt sind die Punkte $A$ und $B$ Eckpunkte von $\text{CH}(S)$. Jeder Punkt $P$, für den $\Omega(A, B, P) \leq 0$ gilt (relativ zur nach außen gerichteten Normalen der aktuellen Hüllkante), liegt strikt innerhalb des konvexen Polygons, das durch die aktuelle Hülle gebildet wird, und ist somit von der weiteren Betrachtung ausgeschlossen.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität wird durch die folgende Rekursionsgleichung bestimmt:
$$T(n) = T(k) + T(n - k - 2) + O(n)$$
wobei $n$ die Anzahl der Punkte und $k$ die Anzahl der in den rekursiven Teilproblemen verbleibenden Punkte ist.

*   **Durchschnittlicher Fall:** Wenn der Punkt $P_{far}$ so gewählt wird, dass die Punkte in etwa gleich große Teilmengen partitioniert werden ($k \approx n/2$), ergibt sich die Rekursion $T(n) = 2T(n/2) + O(n)$. Nach dem Master-Theorem gilt $T(n) = O(n \log n)$.
*   **Schlechtester Fall:** Wenn die Punkte so verteilt sind, dass die Partitionierung sehr unausgewogen ist (z. B. $k=0$ oder $k=n-1$ in jedem Schritt), ergibt sich die Rekursion $T(n) = T(n-1) + O(n)$, was zu $T(n) = O(n^2)$ führt. Dies tritt auf, wenn Punkte auf einem Kreis oder einer konvexen Kurve verteilt sind.

### Platzkomplexität
*   **Zusätzlicher Speicherplatz:** Der Algorithmus benötigt $O(n)$ Speicherplatz, um die Eingabepunkte zu speichern. Die Tiefe des Rekursions-Stacks $D$ hängt von der Partitionierung ab. Im durchschnittlichen Fall gilt $D = O(\log n)$. Im schlechtesten Fall gilt $D = O(n)$.
*   **Gesamtspeicherplatz:** Der Algorithmus arbeitet mit einem Gesamtspeicherplatz von $O(n)$, da die Punkte per Referenz übergeben werden und die Hülle inkrementell konstruiert wird. Der zusätzliche Stack-Speicherplatz beträgt im Durchschnitt $O(\log n)$ und im schlechtesten Fall $O(n)$.