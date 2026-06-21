# Formale mathematische Spezifikation: 0-1 Knapsack (Branch and Bound)

## 1. Definitionen und Notation

Sei $I = \{1, 2, \dots, n\}$ eine Menge von $n$ Objekten. Jedes Objekt $i \in I$ ist durch ein Paar $(v_i, w_i) \in \mathbb{R}^+ \times \mathbb{R}^+$ charakterisiert, welches seinen Wert beziehungsweise sein Gewicht repräsentiert. Sei $W \in \mathbb{R}^+$ die Gesamtkapazität des Rucksacks.

Wir definieren den Entscheidungsvektor $\mathbf{x} = (x_1, x_2, \dots, x_n) \in \{0, 1\}^n$, wobei $x_i = 1$, falls Objekt $i$ in den Rucksack aufgenommen wird, und $x_i = 0$ andernfalls. Das 0-1 Knapsack-Problem ist als folgendes Ganzzahliges Lineares Programm (ILP) definiert:

$$\text{Maximiere } Z = \sum_{i=1}^n v_i x_i$$
$$\text{unter den Nebenbedingungen } \sum_{i=1}^n w_i x_i \leq W, \quad x_i \in \{0, 1\}$$

Der Zustandsraum $\mathcal{S}$ wird als ein Binärbaum der Tiefe $n$ dargestellt. Ein Knoten $u \in \mathcal{S}$ auf der Ebene $k$ ist durch das Tupel $(k, \text{profit}_u, \text{weight}_u)$ definiert, wobei:
- $\text{profit}_u = \sum_{i=1}^k v_i x_i$
- $\text{weight}_u = \sum_{i=1}^k w_i x_i$

## 2. Algebraische Charakterisierung

Um den Suchraum zu beschneiden (Pruning), definieren wir eine obere Schrankenfunktion $U(u)$ für jeden Knoten $u$. Wir relaxieren die Ganzzahligkeitsbedingung $x_i \in \{0, 1\}$ zu $x_i \in [0, 1]$ für die verbleibenden Objekte $i > k$.

### Die fraktionale Relaxation
Seien die Objekte so sortiert, dass $\frac{v_1}{w_1} \geq \frac{v_2}{w_2} \geq \dots \geq \frac{v_n}{w_n}$ gilt. Für einen Knoten $u$ auf der Ebene $k$ wird die obere Schranke $U(u)$ berechnet, indem die verbleibende Kapazität $W - \text{weight}_u$ gierig (greedy) aufgefüllt wird:

1. Sei $j$ der erste Index, für den $j > k$ und $\sum_{i=k+1}^j w_i > W - \text{weight}_u$ gilt.
2. Die Schranke ist:
   $$U(u) = \text{profit}_u + \sum_{i=k+1}^{j-1} v_i + \left( \frac{W - \text{weight}_u - \sum_{i=k+1}^{j-1} w_i}{w_j} \right) v_j$$

### Pruning-Bedingung
Sei $Z^*$ der bisher gefundene globale Maximalwert (der aktuelle Bestwert). Ein Knoten $u$ wird genau dann beschnitten, wenn:
$$U(u) \leq Z^*$$
Dies ist zulässig, da $U(u)$ die optimale Lösung der Linearen Programmierung (LP)-Relaxation des Teilproblems am Knoten $u$ darstellt. Da der zulässige Bereich des ILP eine Teilmenge des zulässigen Bereichs der LP-Relaxation ist, liefert $U(u)$ eine rigorose obere Schranke für den Zielfunktionswert, der von jedem Nachfahren von $u$ erreicht werden kann.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität im Schlechtesten Fall beträgt $O(2^n)$.
- **Herleitung:** Im Schlechtesten Fall wird die Pruning-Bedingung $U(u) \leq Z^*$ erst erreicht, wenn die Blattknoten erreicht sind. Der Algorithmus führt dann eine erschöpfende Suche im Binärbaum der Höhe $n$ durch. Die Anzahl der Knoten in einem vollständigen Binärbaum der Höhe $n$ beträgt $\sum_{i=0}^n 2^i = 2^{n+1} - 1$.
- **Durchschnittlicher Fall:** Durch das Sortieren der Objekte nach Dichte $\rho_i = v_i/w_i$ findet der Algorithmus frühzeitig einen hochwertigen aktuellen Bestwert $Z^*$. Die Anzahl der besuchten Knoten reduziert sich auf $O(2^n \cdot \alpha)$, wobei $\alpha \ll 1$ der Pruning-Faktor ist, der durch die Güte der fraktionalen Schranke bestimmt wird.

### Platzkomplexität
Die Platzkomplexität beträgt $O(2^n)$ im Schlechtesten Fall.
- **Herleitung:** Der Algorithmus verwendet eine Queue (oder einen Stack), um die Grenze (Frontier) des Suchbaums zu speichern. Bei einer Breitensuche (BFS) tritt die maximale Anzahl der in der Queue gespeicherten Knoten zu jedem Zeitpunkt auf der tiefsten Ebene des Baums auf, was $O(2^n)$ entspricht.
- **Zusätzlicher Speicher:** Der Sortierschritt erfordert $O(n)$ Speicherplatz, und der Rekursions-Stack (falls mittels Tiefensuche implementiert) erfordert $O(n)$ Speicherplatz. Der gesamte Speicherbedarf wird jedoch durch die Speicherung der Grenzknoten im Zustandsraum-Baum dominiert.