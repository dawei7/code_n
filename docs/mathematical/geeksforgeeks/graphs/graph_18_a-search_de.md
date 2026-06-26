# Formale mathematische Spezifikation: A*-Suchalgorithmus

## 1. Definitionen und Notation

Sei $G = (V, E)$ ein gewichteter, gerichteter Graph, wobei $V$ eine endliche Menge von Knoten und $E \subseteq V \times V$ eine Menge von Kanten ist. Sei $w: E \to \mathbb{R}^+$ eine Kostenfunktion, die jeder Kante ein positives Gewicht zuweist.

*   **Start und Ziel:** Wir definieren einen Startknoten $s \in V$ und einen Zielknoten $t \in V$.
*   **Pfad:** Ein Pfad $P$ von $s$ nach $t$ ist eine Folge von Knoten $(v_0, v_1, \dots, v_k)$, sodass $v_0 = s$, $v_k = t$ und $(v_i, v_{i+1}) \in E$ für alle $0 \le i < k$ gilt.
*   **Kostenfunktion:** Die Kosten eines Pfades $P$ sind definiert als $c(P) = \sum_{i=0}^{k-1} w(v_i, v_{i+1})$.
*   **Optimaler Pfad:** Die kürzeste Pfaddistanz $d^*(s, t)$ ist definiert als $\min \{c(P) \mid P \text{ ist ein Pfad von } s \text{ nach } t\}$.
*   **Heuristische Funktion:** Sei $h: V \to \mathbb{R}_{\ge 0}$ eine heuristische Funktion, für die $h(t) = 0$ gilt.
*   **Zustandsvariablen:**
    *   $g(n)$: Die vom Algorithmus gefundene Kosten des Pfades von $s$ nach $n$.
    *   $f(n) = g(n) + h(n)$: Die geschätzten Gesamtkosten eines Pfades von $s$ nach $t$, der durch $n$ verläuft.
    *   $\mathcal{O}$: Das "Open Set" (Priority Queue), das entdeckte, aber noch nicht expandierte Knoten enthält, sortiert nach $f(n)$.
    *   $\mathcal{C}$: Das "Closed Set", das bereits expandierte Knoten enthält.

## 2. Algebraische Charakterisierung

Die Korrektheit von A* beruht auf den Eigenschaften der Heuristik $h(n)$.

### Zulässigkeit
Eine Heuristik $h$ ist **zulässig** (admissible), wenn für alle $n \in V$ gilt:
$$h(n) \le d^*(n, t)$$
wobei $d^*(n, t)$ die tatsächliche kürzeste Pfaddistanz von $n$ nach $t$ ist. Wenn $h$ zulässig ist, garantiert A* das Finden eines optimalen Pfades.

### Konsistenz (Monotonie)
Eine Heuristik $h$ ist **konsistent**, wenn für jeden Knoten $n$ und jeden Nachfolger $n'$ von $n$, der durch eine Kante $(n, n')$ mit Kosten $w(n, n')$ erzeugt wurde, gilt:
$$h(n) \le w(n, n') + h(n')$$
Konsistenz impliziert Zulässigkeit. Unter Konsistenz sind die $f$-Werte der von A* expandierten Knoten nicht abnehmend, was sicherstellt, dass bei der Expansion eines Knotens $n$ gilt: $g(n) = d^*(s, n)$.

### Die Expansionsinvariante
Sei $g(n)$ zu jedem Zeitpunkt der Iteration die aktuell beste bekannte Distanz von $s$ nach $n$. Der Algorithmus erhält die folgende Invariante aufrecht:
Für jeden Knoten $n \in \mathcal{O}$ ist $g(n)$ die bisher gefundene kürzeste Pfaddistanz von $s$ nach $n$. Der Algorithmus wählt $n \in \mathcal{O}$ so, dass:
$$n = \arg\min_{u \in \mathcal{O}} \{g(u) + h(u)\}$$
Nach der Expansion von $n$ führt der Algorithmus für jeden Nachbarn $v$ von $n$ einen Relaxationsschritt durch:
$$g(v) = \min(g(v), g(n) + w(n, v))$$
Falls $g(v)$ aktualisiert wird, wird $v$ mit der Priorität $f(v) = g(v) + h(v)$ in $\mathcal{O}$ eingefügt.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität wird durch die Anzahl der Priority-Queue-Operationen bestimmt. Jede Kante $(u, v) \in E$ wird bei einer konsistenten Heuristik höchstens einmal relaxiert.
*   **Gesamtaufwand:** Der Algorithmus führt höchstens $|V|$ `extract-min`-Operationen und höchstens $|E|$ `decrease-key`- (oder `insert`-) Operationen durch.
*   **Asymptotische Schranke:** Bei Verwendung eines Fibonacci-Heaps beträgt die Komplexität $O(E + V \log V)$. Bei Verwendung eines Standard-Binary-Heaps beträgt sie $O(E \log V)$.
*   **Einfluss der Heuristik:** Der effektive Verzweigungsfaktor $b^*$ bestimmt die Anzahl der expandierten Knoten. Wenn $h(n) = 0$ (Dijkstra), beträgt die Komplexität $O(E \log V)$. Wenn $h(n) = d^*(n, t)$ (perfekte Heuristik), beträgt die Komplexität $O(V)$, da der Algorithmus nur die Knoten auf dem optimalen Pfad untersucht.

### Platzkomplexität
Die Platzkomplexität wird primär durch die Speicherung des Graphen und der Hilfsdatenstrukturen bestimmt:
*   **Graphspeicherung:** $O(V + E)$ für die Adjacency List.
*   **Zusätzlicher Speicher:** Die Priority Queue $\mathcal{O}$ und die Distanz-Map $g$ speichern höchstens $O(V)$ Knoten.
*   **Gesamtspeicher:** $O(V + E)$, was sich in dünn besetzten Graphen, in denen $E \approx V$ gilt, zu $O(V)$ vereinfacht.