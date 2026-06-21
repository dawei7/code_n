# Formale mathematische Spezifikation: Baumdurchmesser

## 1. Definitionen und Notation
Sei $d(u, v)$ die Distanz (Anzahl der Kanten) zwischen den Knoten $u, v \in V$.
Der Durchmesser $\mathcal{D}(T)$ ist definiert als $\max_{u, v \in V} d(u, v)$.

## 2. Algebraische Charakterisierung
Für jeden Knoten $x \in V$ sei $P(x)$ die Länge des längsten Pfades, der durch $x$ verläuft und bei dem $x$ der höchste Knoten (am nächsten zur Wurzel) auf dem Pfad ist.
$$ P(x) = \mathcal{H}(x_L) + \mathcal{H}(x_R) $$
wobei $\mathcal{H}$ die Höhe, definiert durch die Anzahl der Knoten, ist.
Der Durchmesser ist strukturell durch das globale Maximum begrenzt:
$$ \mathcal{D}(T) = \max_{x \in V} P(x) $$

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** Eine Post-Order-Traversal berechnet $\mathcal{H}(x_L)$ und $\mathcal{H}(x_R)$ für alle Knoten sequenziell. Die Auswertung des globalen Maximums ist bei jedem Schritt eine $O(1)$ Skalaroperation. Die Gesamtzeit beträgt $O(|V|)$.
- **Platzkomplexität:** Rekursionstiefe $O(\mathcal{H}(T))$.