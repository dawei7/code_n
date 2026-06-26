# Formale mathematische Spezifikation: K-tes kleinstes Element in einer sortierten Matrix

## 1. Definitionen und Notation

Sei $M$ eine $N \times N$ Matrix, wobei $M_{i,j} \in \mathbb{R}$ für $0 \le i, j < N$ gilt. Die Matrix erfüllt die Monotonieeigenschaft:
1. $\forall i, j_1 < j_2: M_{i, j_1} \le M_{i, j_2}$ (zeilenweise sortiert)
2. $\forall j, i_1 < i_2: M_{i_1, j} \le M_{i_2, j}$ (spaltenweise sortiert)

Wir definieren die Menge aller Elemente in der Matrix als $\mathcal{M} = \{M_{i,j} \mid 0 \le i, j < N\}$. Sei $f: \{1, \dots, N^2\} \to \mathcal{M}$ eine Bijektion, sodass $f(1) \le f(2) \le \dots \le f(N^2)$ gilt. Unser Ziel ist es, den Wert $f(K)$ für ein gegebenes $K \in \{1, \dots, N^2\}$ zu bestimmen.

Wir definieren einen Zustandsraum $\mathcal{S} \subseteq \{0, \dots, N-1\}^2$, der die Indizes der Elemente repräsentiert, die aktuell für die Priority Queue in Betracht gezogen werden. Eine Priority Queue $\mathcal{H}$ speichert Tupel $(M_{i,j}, i, j)$, geordnet nach dem Wert $M_{i,j}$.

## 2. Algebraische Charakterisierung

Der Algorithmus basiert auf der Eigenschaft, dass das $K$-te kleinste Element das Ergebnis einer $K$-stufigen Extraktion aus einer Menge von $N$ sortierten Sequenzen (den Zeilen) ist.

### Heap-Invariante
Sei $\mathcal{P}_k$ die Menge der Elemente, die nach $k$ Iterationen aus der Priority Queue entfernt (pop) wurden. Sei $\mathcal{C}_k$ die Menge der "Kandidaten"-Elemente, die sich aktuell in der Priority Queue befinden. Die folgende Invariante gilt:
1. $\forall (v, i, j) \in \mathcal{C}_k$, falls $j > 0$, dann ist $M_{i, j-1} \in \mathcal{P}_k$.
2. $\forall (v, i, j) \in \mathcal{C}_k$, falls $i > 0$, dann ist $M_{i-1, j} \in \mathcal{P}_k$.

Dies stellt sicher, dass für jedes Element $M_{i,j}$, das zur Priority Queue hinzugefügt wird, alle seine Vorgänger in der durch die Matrixindizes definierten Halbordnung bereits verarbeitet wurden.

### Übergangsfunktion
Sei $H_k$ die Priority Queue zum Zeitpunkt $k$. Der Übergang von $H_k$ zu $H_{k+1}$ ist definiert durch:
1. Extraktion des Minimums: $(v^*, r, c) = \text{argmin}_{(v, i, j) \in H_k} \{v\}$.
2. Nachfolgegenerierung: Definiere die Menge der potenziellen Nachfolger $\mathcal{N}(r, c) = \{(r+1, c), (r, c+1)\}$.
3. Aktualisierung: $H_{k+1} = (H_k \setminus \{(v^*, r, c)\}) \cup \{(M_{r', c'}, r', c') \mid (r', c') \in \mathcal{N}(r, c) \land r', c' < N \land (r', c') \notin \mathcal{P}_{k+1}\}$.

Der Algorithmus terminiert bei $k=K$, wobei das Ergebnis $v^*$ ist.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus führt $K$ Iterationen durch. In jeder Iteration:
1. **Extraktion:** $\text{heappop}$ benötigt $O(\log |\mathcal{H}|)$. Da $|\mathcal{H}| \le N$, entspricht dies $O(\log N)$.
2. **Einfügung:** Es werden höchstens zwei $\text{heappush}$-Operationen durchgeführt, die jeweils $O(\log N)$ benötigen.

Die gesamte Zeitkomplexität ergibt sich aus der Summation:
$$T(K, N) = \sum_{k=1}^{K} O(\log (\min(k, N))) = O(K \log (\min(K, N)))$$
Da $K \le N^2$ gilt, ist dies durch $O(K \log N)$ beschränkt.

### Platzkomplexität
Die Platzkomplexität wird primär durch die Speicherung der Priority Queue $\mathcal{H}$ und der Menge der besuchten Indizes $\mathcal{V}$ bestimmt.
1. **Priority Queue:** Die Priority Queue enthält zu jedem Zeitpunkt höchstens $\min(K, N)$ Elemente, da wir anfangs nur Elemente aus der ersten Spalte hinzufügen und zeilenweise expandieren.
2. **Besuchte Indizes:** Um redundante Einfügungen zu vermeiden, führen wir eine Menge besuchter Indizes $(i, j)$, was im Schlechtesten Fall $O(K)$ Platz benötigt.

Somit beträgt die gesamte zusätzliche Platzkomplexität $O(\min(K, N^2))$, was sich für $K < N^2$ zu $O(K)$ und im Grenzwert zu $O(N^2)$ vereinfacht. Wenn wir die Eigenschaft nutzen, dass wir nur den aktuellen Spaltenindex für jede Zeile verfolgen müssen, kann dies auf $O(N)$ optimiert werden.