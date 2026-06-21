# Formale mathematische Spezifikation: Job Assignment (Branch and Bound)

## 1. Definitionen und Notation

Sei $N \in \mathbb{Z}^+$ die Anzahl der Arbeiter und Jobs. Wir definieren die Menge der Arbeiter als $\mathcal{W} = \{0, 1, \dots, N-1\}$ und die Menge der Jobs als $\mathcal{J} = \{0, 1, \dots, N-1\}$. Der Input ist eine Kostenmatrix $C \in \mathbb{R}^{N \times N}$, wobei $c_{i,j}$ die Kosten für die Zuweisung von Arbeiter $i$ zu Job $j$ bezeichnet.

Eine Zuweisung ist eine Bijektion $\sigma: \mathcal{W} \to \mathcal{J}$. Die Menge aller möglichen Zuweisungen ist die symmetrische Gruppe $S_N$, welche $N!$ Permutationen enthält. Das Ziel ist es, eine optimale Zuweisung $\sigma^*$ zu finden, sodass:
$$\sigma^* = \arg \min_{\sigma \in S_N} \sum_{i=0}^{N-1} c_{i, \sigma(i)}$$

Der Zustandsraum $\mathcal{S}$ besteht aus partiellen Zuweisungen. Ein Zustand $s$ auf der Tiefe $k$ (wobei $0 \le k \le N$) ist durch das Tupel $(A_k, U_k)$ definiert, wobei:
- $A_k = \{(i, \sigma(i)) \mid 0 \le i < k\}$ die Menge der Zuweisungen für die ersten $k$ Arbeiter ist.
- $U_k = \mathcal{J} \setminus \{\sigma(0), \dots, \sigma(k-1)\}$ die Menge der noch nicht zugewiesenen Jobs ist.

## 2. Algebraische Charakterisierung

Der Branch and Bound-Algorithmus durchsucht den Zustandsraum-Baum, wobei jeder Knoten auf der Tiefe $k$ in $|U_k| = N-k$ Kinder verzweigt. Um die Suche zu beschneiden (Pruning), definieren wir eine untere Schrankenfunktion $L(s)$ für einen Zustand $s = (A_k, U_k)$.

Sei $C_{curr}(s) = \sum_{(i,j) \in A_k} c_{i,j}$ die akkumulierten Kosten der partiellen Zuweisung. Die untere Schranke $L(s)$ ist definiert als:
$$L(s) = C_{curr}(s) + \sum_{i=k}^{N-1} \min_{j \in U_k} c_{i,j}$$

**Theorem (Gültigkeit der unteren Schranke):** Für jeden Zustand $s$ auf der Tiefe $k$ gilt $L(s) \le \text{cost}(\sigma)$ für jede vollständige Zuweisung $\sigma$, die die partielle Zuweisung $A_k$ erweitert.
*Beweis:* Da $\min_{j \in U_k} c_{i,j}$ die minimal möglichen Kosten für Arbeiter $i$ bei der Zuweisung zu einem verbleibenden Job $j \in U_k$ darstellt, liefert die Summe $\sum_{i=k}^{N-1} \min_{j \in U_k} c_{i,j}$ eine untere Schranke für die Kosten jeder gültigen Vervollständigung der Zuweisung. Da die Kosten der partiellen Zuweisung fixiert sind, ist die Summe $L(s)$ eine gültige untere Schranke.

**Pruning-Kriterium:** Sei $C_{best}$ die Kosten der bisher besten gefundenen vollständigen Zuweisung. Ein Zweig, der vom Zustand $s$ ausgeht, wird beschnitten, wenn:
$$L(s) \ge C_{best}$$

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität im Schlechtesten Fall beträgt $O(N!)$. 
In Abwesenheit von effektivem Pruning (z. B. wenn die Kostenmatrix so strukturiert ist, dass $L(s)$ konsistent klein ist), führt der Algorithmus eine Tiefensuche oder eine Best-First-Suche des gesamten Permutationsbaums durch. Die Anzahl der Knoten im Zustandsraum-Baum ergibt sich aus der Summe der partiellen Permutationen:
$$\sum_{k=0}^{N} \frac{N!}{(N-k)!} = \lfloor N! \cdot e \rfloor$$
Jeder Knoten erfordert die Berechnung der unteren Schranke, was $O((N-k)^2)$ Zeit in Anspruch nimmt, um die Minima für die verbleibenden Arbeiter zu finden. Somit ist der Gesamtaufwand durch $O(N \cdot N!)$ beschränkt. In der Praxis reduziert der Pruning-Faktor $\alpha$ den effektiven Suchraum auf $O(\alpha^N)$, wobei $\alpha < N$.

### Platzkomplexität
Die Platzkomplexität wird durch die maximale Tiefe des Rekursions-Stacks und die Speicherung der Priority Queue (bei Best-First-Suche) oder des Rekursions-Stacks (bei Tiefensuche) bestimmt.
- **Rekursions-Stack:** Die Tiefe des Baums beträgt $N$, was zu $O(N)$ Platz für den Aufruf-Stack führt.
- **Priority Queue:** Im Schlechtesten Fall kann die Anzahl der in der Frontier gespeicherten Knoten proportional zur Anzahl der Blätter sein, $O(N!)$.
- **Gesamtplatz:** $O(N!)$ im Schlechtesten Fall, obwohl typischerweise $O(N)$ für Tiefensuche-Implementierungen oder $O(2^N)$ für Best-First-Implementierungen, abhängig von der Effizienz des Prunings.