# Formale mathematische Spezifikation: TSP mittels reduzierter Matrix (Branch and Bound)

## 1. Definitionen und Notation

Sei $G = (V, E)$ ein vollständiger gerichteter Graph, wobei $V = \{0, 1, \dots, n-1\}$ die Menge der $n$ Städte ist. Sei $C \in (\mathbb{R}_{\ge 0} \cup \{\infty\})^{n \times n}$ die Adjacency Matrix, wobei $c_{ij}$ die Kosten der Kante $(i, j) \in E$ bezeichnet. Existiert keine Kante, so ist $c_{ij} = \infty$.

Eine **Tour** ist ein Hamilton-Zyklus in $G$, dargestellt als Permutation $\sigma$ von $V$, sodass die Gesamtkosten $L(\sigma) = \sum_{i=0}^{n-1} c_{\sigma(i), \sigma(i+1)}$ betragen, mit $\sigma(n) = \sigma(0)$. Das Ziel ist es, $\sigma^* = \arg \min_{\sigma \in S_n} L(\sigma)$ zu finden.

- **Zustandsraum $\mathcal{S}$**: Ein Knoten im Suchbaum ist definiert durch ein Tupel $(P, M, \text{cost\_so\_far})$, wobei $P = (v_0, v_1, \dots, v_k)$ der aktuelle Pfad ist, $M$ die reduzierte Kostenmatrix für das verbleibende Teilproblem darstellt und $\text{cost\_so\_far}$ die Summe der Kantengewichte in $P$ ist.
- **Reduktionsoperator $\mathcal{R}(M)$**: Eine Funktion, die $M$ in $M'$ transformiert, sodass $\min_{j} m'_{ij} = 0$ für alle $i$ und $\min_{i} m'_{ij} = 0$ für alle $j$ gilt. Die Reduktionskosten $\rho(M)$ sind der Gesamtwert, der von $M$ subtrahiert wurde, um diesen Zustand zu erreichen.

## 2. Algebraische Charakterisierung

Der Algorithmus basiert auf der **Lower Bound Property**. Für jede Matrix $M$ sind die Kosten eines jeden Hamilton-Zyklus, der in $M$ enthalten ist, nach unten durch die Summe der aktuellen Pfadkosten und der Reduktionskosten der Matrix beschränkt.

### Matrixreduktion
Gegeben eine Matrix $M$, sind die Reduktionskosten $\rho(M)$ definiert als:
$$\rho(M) = \sum_{i=0}^{n-1} \min_{j} m_{ij} + \sum_{j=0}^{n-1} \min_{i} m_{ij}$$
wobei das Minimum über endliche Elemente gebildet wird. Die reduzierte Matrix $M'$ ergibt sich durch:
$$m'_{ij} = m_{ij} - \min_{k} m_{ik} - \min_{k} m_{kj}$$

### Branching and Bound
Beim Übergang von einem Zustand mit Matrix $M$ zu einem Kindzustand durch Auswahl der Kante $(i, j)$ definieren wir die neue Matrix $M_{ij}$ wie folgt:
1. Setzen der Zeile $i$ und Spalte $j$ auf $\infty$.
2. Setzen von $M_{ji} = \infty$, um Sub-Zyklen zu verhindern.
3. Anwendung von $\mathcal{R}(M_{ij})$, um $M'_{ij}$ und die zugehörigen Reduktionskosten $\rho(M_{ij})$ zu erhalten.

Die **Lower Bound** $LB$ für einen Knoten ist rekursiv definiert:
$$LB(\text{child}) = LB(\text{parent}) + c_{ij} + (\rho(M_{ij}) - \rho(M_{\text{parent}}))$$
wobei $c_{ij}$ die Kosten in der reduzierten Matrix des Elternknotens sind. Der Algorithmus erhält die Invariante aufrecht, dass für jeden Knoten in der Priority Queue $LB$ eine nicht-abnehmende Schätzung der optimalen Tourkosten ist, die durch den Teilpfad $P$ verlaufen.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität im schlechtesten Fall beträgt $O(n! \cdot n^2)$.
- **Verzweigungsfaktor:** Auf jeder Ebene $k$ des Suchbaums gibt es höchstens $(n-k)$ Auswahlmöglichkeiten. Die Gesamtzahl der Knoten im Zustandsraum-Baum beträgt $\sum_{k=0}^{n} \frac{n!}{k!} = O(n!)$.
- **Aufwand pro Knoten:** An jedem Knoten iteriert die `reduce`-Funktion über die $n \times n$ Matrix und führt Zeilen- sowie Spaltenscans durch, was zu $O(n^2)$ Operationen führt.
- **Gesamt:** Das Produkt aus der Anzahl der Knoten und dem Aufwand pro Knoten ergibt $O(n! \cdot n^2)$. In der Praxis reduziert die Pruning-Bedingung $LB \ge \text{best}$ den effektiven Suchraum signifikant, was für bestimmte Instanzen oft zu einer nahezu polynomiellen Laufzeit führt.

### Platzkomplexität
Die Platzkomplexität beträgt im absoluten schlechtesten Fall $O(n! \cdot n^2)$, da die Priority Queue einen signifikanten Teil der Knoten des Zustandsraum-Baums speichern kann.
- **Zusätzlicher Speicher:** Jeder Knoten speichert eine $n \times n$ Matrix, was $O(n^2)$ Speicherplatz erfordert.
- **Gesamtspeicher:** Da die Priority Queue $O(n!)$ Knoten enthalten kann, beträgt der Gesamtspeicher $O(n! \cdot n^2)$. Da der Algorithmus jedoch eine Best-First Search Strategie verwendet, wird der Speicherbedarf durch die Breite des Suchbaums in der aktuellen Tiefe dominiert, welche für wohlgeformte Kostenmatrizen typischerweise deutlich kleiner als $n!$ ist.