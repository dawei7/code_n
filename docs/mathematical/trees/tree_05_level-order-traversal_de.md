# Formale Mathematische Spezifikation: Level-order Traversal

## 1. Definitionen und Notation
Sei $d(v)$ die Tiefe des Knotens $v \in V$, definiert als die Anzahl der Kanten von der Wurzel zu $v$.
Wir partitionieren $V$ in disjunkte Teilmengen $L_k = \{ v \in V \mid d(v) = k \}$ für $0 \leq k \leq \mathcal{H}(T)$.

## 2. Zielsetzung
Ausgabe der Sequenz von Mengen $(L_0, L_1, \dots, L_{\mathcal{H}(T)})$, wobei innerhalb jeder Menge $L_k$ die Elemente nach ihrer relativen Links-nach-Rechts-Position in der geometrischen Einbettung von $T$ geordnet sind.

## 3. Algorithmus-Formalisierung (BFS)
Sei $Q$ eine FIFO Queue.
1. Initialisiere $Q \leftarrow [r]$.
2. Für $k = 0, 1, \dots$:
   - Sei $S_k$ die Sequenz der Elemente, die sich aktuell in $Q$ befinden.
   - Leere $Q$ und enqueuen Sie alle Kinder der Elemente in $S_k$ sequenziell von links nach rechts.
   - Wenn $Q$ leer ist, beenden Sie.

## 4. Komplexitätsanalyse
- **Zeitkomplexität:** Jeder Knoten wird genau einmal enqueued und dequeued. $O(|V|)$.
- **Platzkomplexität:** Die maximale Größe von $Q$ ist begrenzt durch $\max_k |L_k|$. Im schlechtesten Fall (ein perfekt balancierter Baum) enthält die letzte Ebene genau $(|V|+1)/2$ Knoten, was zu einer Platzkomplexität von $O(|V|)$ führt.