# Formale mathematische Spezifikation: Convex Hull (Jarvis March / Gift Wrapping)

## 1. Definitionen und Notation

Sei $P = \{p_1, p_2, \dots, p_n\}$ eine Menge von $n$ Punkten in der euklidischen Ebene $\mathbb{R}^2$, wobei jeder Punkt $p_i = (x_i, y_i)$ ist.

*   **Convex Hull:** Die Convex Hull von $P$, bezeichnet als $\text{CH}(P)$, ist das eindeutige minimale konvexe Polygon, sodass $P \subseteq \text{CH}(P)$ gilt. Die Vertices von $\text{CH}(P)$ sind eine Teilmenge von $P$.
*   **Orientierungsfunktion:** Für jedes geordnete Tripel von Punkten $(a, b, c)$ wird die Orientierung durch das Vorzeichen des Kreuzprodukts der Vektoren $\vec{ab}$ und $\vec{ac}$ bestimmt:
    $$\Omega(a, b, c) = (x_b - x_a)(y_c - y_a) - (y_b - y_a)(x_c - x_a)$$
    *   Wenn $\Omega(a, b, c) > 0$, vollzieht die Sequenz $(a, b, c)$ eine Drehung gegen den Uhrzeigersinn (nach links).
    *   Wenn $\Omega(a, b, c) < 0$, vollzieht die Sequenz $(a, b, c)$ eine Drehung im Uhrzeigersinn (nach rechts).
    *   Wenn $\Omega(a, b, c) = 0$, sind die Punkte kollinear.
*   **Zustandsraum:** Der Algorithmus verwaltet eine Sequenz von Vertices $H = (h_0, h_1, \dots, h_{m-1})$, wobei $m = |H|$ die Anzahl der Vertices auf der Hull ist. Der Zustand in Iteration $k$ ist durch den aktuellen Vertex $h_k \in P$ definiert.

## 2. Algebraische Charakterisierung

Der Jarvis-March-Algorithmus konstruiert die Sequenz $H$ durch iteratives Auswählen des "am weitesten gegen den Uhrzeigersinn liegenden" Punktes relativ zum aktuellen Vertex.

**Initialisierung:**
Der Start-Vertex $h_0$ ist definiert als der Punkt mit der minimalen $x$-Koordinate (und bei Gleichstand mit der minimalen $y$-Koordinate):
$$h_0 = \text{argmin}_{p \in P} \{x_p \mid \forall q \in P, x_p < x_q \lor (x_p = x_q \land y_p \le y_q)\}$$

**Induktionsschritt:**
Gegeben der aktuelle Vertex $h_k$, wird der nächste Vertex $h_{k+1}$ so gewählt, dass für alle $p \in P \setminus \{h_k\}$ die Orientierung $\Omega(h_k, h_{k+1}, p) \ge 0$ gilt. Formal:
$$h_{k+1} = \{q \in P \mid \forall p \in P, \Omega(h_k, q, p) \ge 0\}$$
Im Falle kollinearer Punkte, bei denen $\Omega(h_k, q, p) = 0$ gilt, wird der Punkt $p$ gewählt, der den euklidischen Abstand $\|p - h_k\|_2$ maximiert, um sicherzustellen, dass die Grenze der Hull strikt durch die Extrempunkte definiert ist.

**Terminierung:**
Der Algorithmus terminiert in Schritt $m$, wenn $h_m = h_0$. Die Sequenz $H = (h_0, h_1, \dots, h_{m-1})$ bildet die Vertices der Convex Hull in der Reihenfolge gegen den Uhrzeigersinn.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus verläuft in $m$ Iterationen, wobei $m$ die Anzahl der Vertices auf der Convex Hull ist (in der Problemstellung als $H$ bezeichnet).

In jeder Iteration $k \in \{0, \dots, m-1\}$ führt der Algorithmus einen linearen Scan über alle $n$ Punkte durch, um den nächsten Vertex $h_{k+1}$ zu identifizieren. Der Arbeitsaufwand pro Iteration beträgt $\Theta(n)$. Summiert über alle Iterationen ergibt sich die gesamte Zeitkomplexität $T(n)$ zu:
$$T(n) = \sum_{k=0}^{m-1} \Theta(n) = \Theta(n \cdot m)$$
Da $m \le n$ gilt, ist die Komplexität im Schlechtesten Fall $O(n^2)$, was eintritt, wenn alle Punkte auf der Convex Hull liegen (z. B. Punkte, die auf einem Kreis verteilt sind). Die Komplexität im Bestfall ist $\Omega(n)$, was eintritt, wenn $m$ konstant ist. Somit ist der Algorithmus ausgabesensitiv mit einer Komplexität von $O(n \cdot H)$.

### Platzkomplexität
*   **Zusätzlicher Speicherplatz:** Der Algorithmus verwaltet eine konstante Anzahl an Pointern und Variablen (`leftmost`, `cur`, `candidate`, `cross`), um den aktuellen Zustand zu verfolgen. Daher beträgt die zusätzliche Platzkomplexität $O(1)$.
*   **Gesamtspeicherplatz:** Der Algorithmus speichert die resultierenden Hull-Vertices. Wenn die Ausgabe als Teil des Speicherbedarfs betrachtet wird, beträgt die Platzkomplexität $O(H)$. Ohne die Ausgabe bleibt die Platzkomplexität $O(1)$.