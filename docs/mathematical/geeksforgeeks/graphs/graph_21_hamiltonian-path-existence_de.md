# Formale mathematische Spezifikation: Existenz eines Hamiltonpfades

## 1. Definitionen und Notation

Sei $G = (V, E)$ ein ungewichteter Graph, wobei $V = \{v_1, v_2, \dots, v_n\}$ die Menge der Knoten ist, sodass $|V| = n$, und $E \subseteq V \times V$ die Menge der Kanten ist. Für einen ungerichteten Graphen gilt $(u, v) \in E \iff (v, u) \in E$.

Ein **Hamiltonpfad** ist definiert als eine Sequenz von Knoten $P = (p_1, p_2, \dots, p_n)$, sodass:
1. $\{p_1, p_2, \dots, p_n\} = V$ (Der Pfad besucht jeden Knoten).
2. $p_i \neq p_j$ für alle $i \neq j$ (Der Pfad besucht jeden Knoten genau einmal).
3. $(p_i, p_{i+1}) \in E$ für alle $1 \le i < n$ (Aufeinanderfolgende Knoten sind benachbart).

Der Algorithmus versucht, die Existenz einer Abbildung $f: \{1, \dots, n\} \to V$ zu bestimmen, sodass $f$ eine Bijektion ist und $(f(i), f(i+1)) \in E$ für alle $i \in \{1, \dots, n-1\}$ gilt.

## 2. Algebraische Charakterisierung

Der Algorithmus verwendet eine Backtracking-Suche über den Zustandsraum $\mathcal{S} \subseteq V \times \mathcal{P}(V) \times \mathbb{Z}^+$, wobei ein Zustand durch das Tupel $(u, S, k)$ definiert ist:
- $u \in V$: Der aktuelle Knoten.
- $S \subseteq V$: Die Menge der besuchten Knoten.
- $k = |S|$: Die Anzahl der besuchten Knoten.

Die Existenz eines Hamiltonpfades ist äquivalent zur Existenz einer Sequenz von Übergängen $(u_i, S_i, i) \to (u_{i+1}, S_{i+1}, i+1)$, ausgehend von einem Anfangszustand $(v_{start}, \{v_{start}\}, 1)$ für ein beliebiges $v_{start} \in V$, welche die folgende Rekursionsgleichung erfüllt:

$$\text{Exists}(u, S, k) = 
\begin{cases} 
\text{True} & \text{if } k = n \\
\bigvee_{v \in \text{Adj}(u), v \notin S} \text{Exists}(v, S \cup \{v\}, k+1) & \text{if } k < n 
\end{cases}$$

Wobei $\text{Adj}(u) = \{v \in V \mid (u, v) \in E\}$. Die globale Entscheidung ist gegeben durch:
$$\Phi(G) = \bigvee_{v \in V} \text{Exists}(v, \{v\}, 1)$$

**Schleifeninvariante:** Auf jeder Rekursionstiefe $k$ erfüllt die Menge $S$ die Bedingung $|S| = k$, und der konstruierte Pfad $P = (p_1, \dots, p_k)$ erfüllt $p_i \in S$ sowie $(p_i, p_{i+1}) \in E$ für alle $1 \le i < k$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus führt eine Tiefensuche auf dem Zustandsraum-Baum durch. Im Schlechtesten Fall ist der Graph ein vollständiger Graph $K_n$. Die Anzahl der möglichen Pfade der Länge $n$ ist durch die Anzahl der Permutationen von $V$ gegeben.

Der Verzweigungsfaktor auf der Tiefe $k$ beträgt höchstens $n-k$. Die Gesamtzahl der Knoten im Suchbaum ist beschränkt durch:
$$T(n) = \sum_{k=0}^{n-1} \frac{n!}{(n-k)!} = O(n!)$$
Konkret untersuchen wir für jeden Knoten alle Permutationen der verbleibenden Knoten. Da wir die Existenz von mindestens einer gültigen Permutation verifizieren müssen, liegt die obere Schranke bei $O(n \cdot n!)$, was in der asymptotischen Notation zu $O(n!)$ vereinfacht wird.

### Platzkomplexität
Die Platzkomplexität wird durch die für die Rekursion erforderlichen Hilfsstrukturen bestimmt:
1. **Rekursions-Stack:** Die Tiefe der Rekursion beträgt $n$, was $O(n)$ Platz erfordert.
2. **Besucht-Menge:** Das boolesche Array (oder Bitmask) erfordert $O(n)$ Platz.
3. **Adjacency List:** Das Speichern des Graphen erfordert $O(V + E)$ Platz.

Da der Algorithmus auf der Graphenstruktur operiert, beträgt die zusätzliche Platzkomplexität (exklusive des Eingabegraphen) $O(n)$. Die gesamte Platzkomplexität beträgt $O(V + E)$.