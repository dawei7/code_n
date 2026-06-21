# Formale mathematische Spezifikation: 0-1 BFS (Kürzester Pfad)

## 1. Definitionen und Notation

Sei $G = (V, E)$ ein gewichteter, ungerichteter Graph, wobei $V = \{v_1, v_2, \dots, v_n\}$ die Menge der Knoten und $E \subseteq V \times V$ die Menge der Kanten ist. Wir definieren eine Gewichtsfunktion $w: E \to \{0, 1\}$, die jeder Kante einen binären Wert zuweist.

*   **Eingabe:** Ein Graph $G = (V, E)$, eine Gewichtsfunktion $w$ und ein Startknoten $s \in V$.
*   **Ausgabe:** Eine Distanzabbildung $\delta: V \to \mathbb{N} \cup \{\infty\}$, wobei $\delta(v)$ die Distanz des kürzesten Pfades von $s$ nach $v$ bezeichnet.
*   **Zustandsraum:** Der Algorithmus verwaltet einen Zustand, der durch das Tupel $(dist, Q)$ repräsentiert wird, wobei $dist: V \to \mathbb{N} \cup \{\infty\}$ die aktuelle Schätzung der Distanz des kürzesten Pfades ist und $Q$ eine Deque (Double-Ended Queue) ist, die eine Teilmenge von $V$ enthält.
*   **Distanzmetrik:** Die Distanz des kürzesten Pfades $d(s, v)$ ist definiert als:
    $$d(s, v) = \min_{P \in \mathcal{P}_{s,v}} \sum_{e \in P} w(e)$$
    wobei $\mathcal{P}_{s,v}$ die Menge aller Pfade von $s$ nach $v$ ist.

## 2. Algebraische Charakterisierung

Die Korrektheit des 0-1 BFS Algorithmus beruht auf der Aufrechterhaltung einer monotonen Eigenschaft innerhalb der Deque $Q$. Sei $Q = (q_1, q_2, \dots, q_k)$ die Sequenz der Knoten in der Deque.

**Invariante:** Zu jedem Iterationsschritt ist die Sequenz der Distanzen in der Deque nicht-fallend und nimmt höchstens zwei Werte an:
$$\exists d \in \mathbb{N} \text{ s.t. } \forall q_i \in Q, dist(q_i) \in \{d, d+1\}$$
Des Weiteren gilt: Wenn $dist(q_i) = d+1$, dann gilt für alle $j > i$, dass $dist(q_j) = d+1$.

**Relaxationsbedingung:** Für eine Kante $(u, v) \in E$ mit Gewicht $w(u, v)$ wird die Distanzschätzung mittels der Relaxationsoperation aktualisiert:
$$dist(v) = \min(dist(v), dist(u) + w(u, v))$$

**Übergangsregeln:**
Bei der Verarbeitung eines Knotens $u$ mit aktueller Distanz $dist(u) = d$:
1.  Wenn $w(u, v) = 0$ und $dist(u) + 0 < dist(v)$, aktualisieren wir $dist(v) \leftarrow d$ und führen $Q.\text{push\_front}(v)$ aus.
2.  Wenn $w(u, v) = 1$ und $dist(u) + 1 < dist(v)$, aktualisieren wir $dist(v) \leftarrow d + 1$ und führen $Q.\text{push\_back}(v)$ aus.

Dies stellt sicher, dass die Deque nach Distanz sortiert bleibt und die Eigenschaft $dist(q_i) \leq dist(q_{i+1})$ für alle $i$ erfüllt ist. Dies ist ein spezieller Fall der **Monotonic Queue Property**, die garantiert, dass beim Entfernen eines Knotens $u$ von der Vorderseite der Deque $dist(u)$ der optimale Wert für den kürzesten Pfad $d(s, u)$ ist.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität beträgt $O(|V| + |E|)$.

*   **Initialisierung:** Die Initialisierung des Distanz-Array benötigt $O(|V|)$.
*   **Knotenverarbeitung:** Jeder Knoten $v \in V$ wird höchstens einmal zur Deque hinzugefügt und wieder entfernt. Dies liegt daran, dass ein Knoten nur dann zur Deque hinzugefügt wird, wenn seine Distanzschätzung strikt verbessert wird. Da die maximal mögliche Distanz $|V|-1$ beträgt und jede Aktualisierung die Distanz verringert, ist die Gesamtzahl der Deque-Operationen durch $O(|V|)$ beschränkt.
*   **Kantenrelaxation:** Für jeden Knoten $u$ iterieren wir über seine Adjacency List. Über die gesamte Ausführung hinweg wird jede Kante $(u, v) \in E$ genau zweimal untersucht (einmal von $u$ aus und einmal von $v$ aus). Jede Relaxationsprüfung und Deque-Operation (push/pop) ist $O(1)$.
*   **Summierung:** Die Gesamtarbeit $T$ ergibt sich zu:
    $$T = \sum_{v \in V} O(1) + \sum_{u \in V} \text{deg}(u) \cdot O(1) = O(|V| + 2|E|) = O(|V| + |E|)$$

### Platzkomplexität
Die Platzkomplexität beträgt $O(|V|)$.

*   **Distanz-Array:** Das Speichern von $dist(v)$ für alle $v \in V$ erfordert $O(|V|)$ Platz.
*   **Adjacency List:** Das Speichern des Graphen erfordert $O(|V| + |E|)$ Platz. Im Kontext des zusätzlichen Speicherbedarfs für den Algorithmus (exklusive des Eingabegraphen) benötigen wir jedoch nur die Deque $Q$ und das Distanz-Array.
*   **Deque:** Im schlechtesten Fall enthält die Deque alle Knoten, was $O(|V|)$ Platz erfordert.
*   **Gesamter zusätzlicher Speicherbedarf:** $O(|V|)$.