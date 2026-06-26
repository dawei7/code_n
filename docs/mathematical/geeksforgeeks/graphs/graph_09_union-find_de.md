# Formale mathematische Spezifikation: Union-Find (Disjoint Set Union, DSU)

## 1. Definitionen und Notation

Sei $S = \{0, 1, \dots, n-1\}$ eine endliche Menge von $n$ Elementen. Eine **Partition** $\mathcal{P}$ von $S$ ist eine Ansammlung disjunkter, nicht-leerer Teilmengen $\{S_1, S_2, \dots, S_k\}$, sodass $\bigcup_{i=1}^k S_i = S$ und $S_i \cap S_j = \emptyset$ für $i \neq j$ gilt.

Die Disjoint Set Union (DSU) Datenstruktur verwaltet eine Repräsentation von $\mathcal{P}$ durch einen Wald aus bewurzelten Bäumen $\mathcal{F} = \{T_1, T_2, \dots, T_k\}$. Jeder Baum $T_i$ entspricht einer Menge $S_i \in \mathcal{P}$.

- **Zustandsraum:** Der Zustand wird durch ein Paar von Abbildungen $(\pi, \rho)$ definiert, wobei:
    - $\pi: S \to S$ die Eltern-Pointer-Funktion ist. Für jeden Knoten $x$ bezeichnet $\pi(x)$ den Elternknoten von $x$. Wenn $\pi(x) = x$ gilt, dann ist $x$ der **Repräsentant** (Wurzel) seiner Menge.
    - $\rho: S \to \mathbb{N}_0$ die Rangfunktion ist, wobei $\rho(x)$ eine obere Schranke für die Höhe des Teilbaums mit Wurzel $x$ angibt.
- **Operationen:**
    - $\text{find}(x)$: Gibt die eindeutige Wurzel $r \in S$ zurück, sodass $r$ der Vorfahre von $x$ in $\mathcal{F}$ ist.
    - $\text{union}(x, y)$: Transformiert $\mathcal{P}$ in $\mathcal{P}'$ durch Verschmelzen der Mengen, die $x$ und $y$ enthalten.

## 2. Algebraische Charakterisierung

Die Korrektheit der DSU-Struktur wird durch die folgenden Invarianten und Übergangsregeln bestimmt:

### Invarianten
1. **Repräsentanten-Invariante:** Für jedes $x \in S$ ist der Repräsentant der Menge, die $x$ enthält, das eindeutige Element $r$, für das $\pi^{(k)}(x) = r$ für ein $k \ge 0$ gilt, wobei $\pi^{(k)}$ die $k$-te Iteration von $\pi$ bezeichnet und $\pi(r) = r$ gilt.
2. **Rang-Invariante:** Für jeden Knoten $x$ ist $\rho(x)$ strikt kleiner als $\rho(\pi(x))$, sofern $x$ keine Wurzel ist. Des Weiteren erfüllt die Wurzel $r$ für jeden Baum der Höhe $h$ die Bedingung $\rho(r) \ge h$.

### Übergangsregeln (Union by Rank)
Gegeben seien $r_x = \text{find}(x)$ und $r_y = \text{find}(y)$. Die union-Operation aktualisiert $\pi$ und $\rho$ wie folgt:
- Wenn $r_x = r_y$, bleibt die Partition unverändert.
- Wenn $r_x \neq r_y$:
    - Wenn $\rho(r_x) < \rho(r_y)$, setze $\pi(r_x) \leftarrow r_y$.
    - Wenn $\rho(r_x) > \rho(r_y)$, setze $\pi(r_y) \leftarrow r_x$.
    - Wenn $\rho(r_x) = \rho(r_y)$, setze $\pi(r_y) \leftarrow r_x$ und inkrementiere $\rho(r_x) \leftarrow \rho(r_x) + 1$.

### Pfadkompression (Path Compression)
Während $\text{find}(x)$ wird die Abbildung $\pi$ für alle Knoten $v$ auf dem Pfad von $x$ zur Wurzel $r$ aktualisiert:
$$\forall v \in \text{path}(x, r), \pi(v) \leftarrow r$$
Diese Transformation bewahrt die Mengenpartition $\mathcal{P}$ und reduziert gleichzeitig die Pfadlänge für zukünftige Operationen.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die amortisierte Zeitkomplexität einer Sequenz von $m$ Operationen auf $n$ Elementen beträgt $O(m \cdot \alpha(n))$, wobei $\alpha$ die inverse Ackermann-Funktion ist.

**Herleitung:**
Die Ackermann-Funktion $A_k(j)$ wächst extrem schnell. Ihre Inverse, $\alpha(n) = \min \{k : A_k(1) \ge n\}$, wächst extrem langsam. Der Beweis, ursprünglich von Tarjan (1975) erbracht, verwendet eine Potenzialfunktion $\Phi$, die auf dem Zustand des Waldes definiert ist.
Sei $rank(x)$ der Rang des Knotens $x$. Wir definieren ein Potenzial $\phi(x)$ basierend auf der Distanz von $rank(x)$ zum Rang seines Elternknotens. Es lässt sich zeigen, dass das Gesamtpotenzial $\Phi = \sum \phi(x)$ während der Pfadkompression abnimmt oder stabil bleibt, was die $O(\log n)$ Schlechtester-Fall-Baumhöhe kompensiert. Die Summierung der amortisierten Kosten über $m$ Operationen ergibt:
$$T(m, n) = \sum_{i=1}^m \text{cost}(op_i) \le O(m \cdot \alpha(n))$$
Für alle praktischen Werte von $n$ ($n < 2^{2^{65536}}$) gilt $\alpha(n) \le 5$, wodurch die Operationen effektiv in konstanter Zeit ablaufen.

### Platzkomplexität
Die Platzkomplexität beträgt $O(n)$.
- Das Eltern-Array $\pi$ benötigt $n$ Speichereinheiten.
- Das Rang-Array $\rho$ benötigt $n$ Speichereinheiten.
- Der gesamte zusätzliche Speicherbedarf beträgt $2n$, was $\Theta(n)$ entspricht. Der Eingabespeicher ist $O(n+m)$, aber die Datenstruktur selbst ist strikt linear in Bezug auf die Anzahl der Elemente.