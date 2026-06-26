# Formale mathematische Spezifikation: Dijkstra-Algorithmus

## 1. Definitionen und Notation

Sei $G = (V, E, w)$ ein gewichteter gerichteter Graph, wobei:
*   $V = \{v_1, v_2, \dots, v_n\}$ die Menge der $n$ Knoten ist.
*   $E \subseteq V \times V$ die Menge der Kanten ist.
*   $w: E \to \mathbb{R}_{\ge 0}$ eine Gewichtsfunktion ist, die jeder Kante einen nicht-negativen reellen Wert zuweist.

Wir definieren die folgenden Zustandsvariablen:
*   $s \in V$: Der Startknoten.
*   $d: V \to \mathbb{R}_{\ge 0} \cup \{\infty\}$: Eine Distanzfunktion, wobei $d(v)$ die aktuelle Schätzung des kürzesten Pfades von $s$ nach $v$ bezeichnet.
*   $S \subseteq V$: Die Menge der "finalisierten" Knoten, für die die Distanz des kürzesten Pfades von $s$ bekannt ist.
*   $Q = V \setminus S$: Die Menge der "unbesuchten" Knoten.

Das Ziel ist die Berechnung der Funktion $\delta(s, v)$, definiert als das Gewicht des kürzesten Pfades von $s$ nach $v$ in $G$.

## 2. Algebraische Charakterisierung

Der Dijkstra-Algorithmus ist ein iteratives Greedy-Verfahren, das die folgende **Schleifeninvariante** aufrechterhält:
Für jeden Knoten $u \in S$ gilt $d(u) = \delta(s, u)$. Des Weiteren ist $d(v)$ für alle $v \in V$ das Gewicht des kürzesten Pfades von $s$ nach $v$, wobei nur Knoten aus $S$ als Zwischenknoten verwendet werden.

### Relaxation
Der zentrale Übergang ist die Relaxation einer Kante $(u, v) \in E$. Falls $d(u) + w(u, v) < d(v)$, aktualisieren wir:
$$d(v) \leftarrow d(u) + w(u, v)$$

### Greedy-Eigenschaft
In jeder Iteration wählen wir $u \in Q$ so, dass:
$$u = \text{argmin}_{v \in Q} \{d(v)\}$$
Die Korrektheit des Algorithmus beruht auf der Tatsache, dass aufgrund von $w(e) \ge 0$ für alle $e \in E$ kein später entdeckter Pfad eine Distanz liefern kann, die kleiner als $d(u)$ ist, sobald $u$ zu $S$ hinzugefügt wurde. Formal gilt: Wenn $u$ der Knoten mit dem minimalen $d$-Wert in $Q$ ist, dann ist $d(u) = \delta(s, u)$.

### Terminierung
Der Algorithmus terminiert, wenn $Q = \emptyset$ ist oder wenn der Zielknoten $t$ zu $S$ verschoben wurde. Der Endzustand erfüllt:
$$\forall v \in V, d(v) = \min_{p \in \mathcal{P}_{s,v}} \sum_{e \in p} w(e)$$
wobei $\mathcal{P}_{s,v}$ die Menge aller Pfade von $s$ nach $v$ ist.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus besteht aus einer Initialisierungsphase und einer Hauptschleife, die $n$-mal ausgeführt wird.

1.  **Initialisierung:** Das Setzen von $d(s) = 0$ und $d(v) = \infty$ für $v \neq s$ benötigt $O(n)$ Zeit.
2.  **Hauptschleife:**
    *   **Auswahl:** Das Finden von $u = \text{argmin}_{v \in Q} d(v)$ erfordert einen linearen Suchlauf über die Menge $Q$. In der $k$-ten Iteration gilt $|Q| = n - k + 1$. Die Gesamtzahl der Operationen für die Auswahl beträgt $\sum_{k=1}^{n} (n - k + 1) = \sum_{i=1}^{n} i = \frac{n(n+1)}{2} = O(n^2)$.
    *   **Relaxation:** Jede Kante $(u, v)$ wird genau einmal relaxiert, wenn ihr Startknoten $u$ aus $Q$ extrahiert wird. Über die gesamte Ausführung hinweg führen wir höchstens $|E| = m$ Relaxationen durch.
    *   **Gesamtzeit:** Die Komplexität wird durch den Auswahlprozess dominiert:
        $$T(n, m) = O(n^2 + m) = O(n^2)$$
    Da in einem einfachen Graphen $m \le n^2$ gilt, begrenzt der Term $O(n^2)$ den Gesamtaufwand.

### Platzkomplexität
Der Algorithmus benötigt Speicherplatz für:
*   Das Distanz-Array $d$: $O(n)$.
*   Die Menge der besuchten Knoten $S$ (oder ein boolesches Array): $O(n)$.
*   Die Repräsentation des Graphen $G$ (Adjacency List): $O(n + m)$.

Somit beträgt die zusätzliche Platzkomplexität $O(n)$, und die gesamte Platzkomplexität, einschließlich der Speicherung des Graphen, beträgt $O(n + m)$.