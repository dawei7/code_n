# Formale mathematische Spezifikation: Bipartite Matching (Max Flow)

## 1. Definitionen und Notation

Sei $G = (V, E)$ ein bipartiter Graph, bei dem die Knotenmenge $V$ in zwei disjunkte Mengen $L$ (links, $|L| = n_L$) und $R$ (rechts, $|R| = n_R$) partitioniert ist, sodass $E \subseteq L \times R$ gilt. Ein Matching $M \subseteq E$ ist eine Menge von Kanten, bei der keine zwei Kanten in $M$ einen gemeinsamen Knoten teilen. Das Ziel ist es, die Kardinalität des maximalen Matchings zu bestimmen, $|M^*| = \max \{|M| : M \text{ ist ein Matching}\}$.

Um dies mittels Netzwerkfluss zu lösen, definieren wir ein Flussnetzwerk $\mathcal{N} = (V', E', c, s, t)$, wobei:
*   **Knotenmenge:** $V' = L \cup R \cup \{s, t\}$, wobei $s$ die Quelle (source) und $t$ die Senke (sink) ist.
*   **Kantenmenge:** $E' = \{(s, u) : u \in L\} \cup \{(u, v) : (u, v) \in E\} \cup \{(v, t) : v \in R\}$.
*   **Kapazitätsfunktion:** $c: E' \to \mathbb{Z}^+$ definiert als:
    *   $c(s, u) = 1, \forall u \in L$
    *   $c(u, v) = 1, \forall (u, v) \in E$
    *   $c(v, t) = 1, \forall v \in R$
*   **Fluss:** Eine Funktion $f: E' \to \mathbb{R}$, die die Kapazitätsbeschränkungen $0 \leq f(e) \leq c(e)$ und die Flusserhaltung $\sum_{u} f(u, v) = \sum_{w} f(v, w)$ für alle $v \in V' \setminus \{s, t\}$ erfüllt.

## 2. Algebraische Charakterisierung

Die Korrektheit dieser Reduktion beruht auf dem **Integralsatz** (Integrality Theorem) und der Konstruktion des Netzwerks. Da alle Kapazitäten $c(e)$ ganzzahlig sind, existiert ein ganzzahliger maximaler Fluss $f^*$.

**Theorem (Äquivalenz):** Der Wert des maximalen Flusses $|f^*| = \sum_{u \in L} f(s, u)$ ist gleich der Kardinalität des maximalen bipartiten Matchings $|M^*|$.

*Beweisskizze:*
1.  **Matching zu Fluss:** Gegeben ein Matching $M$, definieren wir einen Fluss $f$ durch $f(s, u) = 1, f(u, v) = 1, f(v, t) = 1$ für alle $(u, v) \in M$, und $0$ andernfalls. Der Flusswert ist $|M|$.
2.  **Fluss zu Matching:** Gegeben ein ganzzahliger Fluss $f$ in $\mathcal{N}$, bildet die Menge $M = \{(u, v) \in E : f(u, v) = 1\}$ ein gültiges Matching, da die Kapazitätsbeschränkungen $c(s, u) = 1$ und $c(v, t) = 1$ sicherstellen, dass jeder Knoten $u \in L$ und $v \in R$ zu höchstens einer Kante in $M$ inzident ist.

Der Algorithmus erhält die Invariante aufrecht, dass der Residualgraph $G_f$ in jeder Iteration einen augmentierenden Pfad $p$ von $s$ nach $t$ enthält. Der Fluss wird aktualisiert durch $f_{new} = f + \Delta f$, wobei $\Delta f$ der Fluss entlang $p$ ist. Nach dem **Max-Flow Min-Cut Theorem** terminiert der Algorithmus, wenn kein solcher Pfad mehr existiert; zu diesem Zeitpunkt ist der Fluss maximal.

## 3. Komplexitätsanalyse

### Zeitkomplexität: $O(V \cdot E)$
Der Edmonds-Karp-Algorithmus läuft im Allgemeinen in $O(V \cdot E^2)$. In einem bipartiten Matching-Netzwerk beobachten wir jedoch Folgendes:
1.  **Einheitskapazitäten:** Jede Kante hat die Kapazität 1.
2.  **Augmentierende Pfade:** Jede Augmentierung erhöht den Fluss um genau 1 Einheit. Da der maximal mögliche Fluss $\min(|L|, |R|) \leq |V|$ beträgt, gibt es höchstens $O(V)$ Augmentierungen.
3.  **BFS-Kosten:** Jeder BFS-Durchlauf des Residualgraphen benötigt $O(V + E)$.
4.  **Gesamtaufwand:** Die gesamte Zeitkomplexität beträgt $O(\text{max\_flow} \times (V + E))$. Da $\text{max\_flow} \leq V$ gilt, ist die Komplexität $O(V(V+E))$. Da in einem bipartiten Graphen $E \geq V-1$ (für einen zusammenhängenden Graphen) gilt, vereinfacht sich dies zu $O(V \cdot E)$.

### Platzkomplexität: $O(V^2)$
*   **Adjacency Matrix:** Die Kapazitätsmatrix $c$ benötigt $O(|V'|^2)$ Speicherplatz, wobei $|V'| = |L| + |R| + 2$. Da $|V'| \approx |V|$ gilt, beträgt die Platzkomplexität $O(V^2)$.
*   **Adjacency List:** Bei der Implementierung mittels Adjacency Lists zur Speicherung des Graphen und der Residualkapazitäten beträgt die Platzkomplexität $O(V + E)$, was für dünn besetzte (sparse) bipartite Graphen speichereffizienter ist.