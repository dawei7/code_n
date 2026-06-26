# Formale mathematische Spezifikation: Activity Selection Problem

## 1. Definitionen und Notation

Sei $A = \{a_1, a_2, \dots, a_n\}$ eine Menge von $n$ Aktivitäten. Jede Aktivität $a_i$ ist definiert als ein geordnetes Paar reeller Zahlen $(s_i, f_i)$, wobei $s_i \in \mathbb{R}_{\ge 0}$ die Startzeit und $f_i \in \mathbb{R}_{> s_i}$ die Endzeit bezeichnet.

Wir definieren eine binäre Relation $\mathcal{C}$ auf der Menge $A$, welche die Bedingung der "Nicht-Konfliktfreiheit" repräsentiert. Zwei Aktivitäten $a_i, a_j$ sind kompatibel genau dann, wenn:
$$a_i \mathcal{C} a_j \iff f_i \le s_j \lor f_j \le s_i$$

Eine Teilmenge $S \subseteq A$ wird als **gegenseitig kompatible Menge** bezeichnet, wenn für jedes Paar $a_i, a_j \in S$ mit $i \neq j$ die Bedingung $a_i \mathcal{C} a_j$ gilt. Das Ziel ist es, eine Teilmenge $S^* \subseteq A$ zu finden, sodass $|S^*|$ maximiert wird, unter der Nebenbedingung, dass $S^*$ gegenseitig kompatibel ist.

## 2. Algebraische Charakterisierung

Seien die Aktivitäten so indiziert, dass sie nach ihren Endzeiten sortiert sind: $f_1 \le f_2 \le \dots \le f_n$.

### Die Greedy-Choice-Eigenschaft
Die Optimalität der Greedy-Strategie beruht auf der Existenz einer optimalen Lösung, die die Aktivität mit der frühesten Endzeit enthält. Sei $S_{opt}$ eine optimale Lösung. Sei $a_k$ die Aktivität in $A$ mit der minimalen Endzeit. Wenn $a_k \in S_{opt}$, ist die Greedy-Wahl konsistent mit einer optimalen Lösung. Wenn $a_k \notin S_{opt}$, sei $a_j$ die Aktivität in $S_{opt}$ mit der minimalen Endzeit. Da $f_k \le f_j$, führt das Ersetzen von $a_j$ durch $a_k$ in $S_{opt}$ zu einer Menge $S' = (S_{opt} \setminus \{a_j\}) \cup \{a_k\}$. Da $f_k \le f_j$, bleibt $S'$ gegenseitig kompatibel und $|S'| = |S_{opt}|$. Somit ist $S'$ ebenfalls eine optimale Lösung.

### Rekurrenz
Sei $OPT(i)$ die maximale Anzahl kompatibler Aktivitäten, die aus der Teilmenge der Aktivitäten $\{a_i, a_{i+1}, \dots, a_n\}$ ausgewählt werden können, unter der Voraussetzung, dass die zuletzt ausgewählte Aktivität zum Zeitpunkt $t_{last}$ endete. Der Zustandsübergang ist definiert als:

$$OPT(i, t_{last}) = 
\begin{cases} 
0 & \text{falls } i > n \\
1 + OPT(i+1, f_i) & \text{falls } s_i \ge t_{last} \\
OPT(i+1, t_{last}) & \text{falls } s_i < t_{last}
\end{cases}$$

Der Algorithmus berechnet diese Rekurrenz effektiv nach dem Greedy-Prinzip, indem er immer den Zweig wählt, der den Zähler inkrementiert, wenn $s_i \ge t_{last}$ gilt.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus besteht aus zwei primären Phasen:
1. **Sortierung:** Die Menge $A$ wird basierend auf den Endzeiten $f_i$ sortiert. Unter Verwendung eines vergleichsbasierten Sortierverfahrens (z. B. Timsort oder Heapsort) beträgt die Zeitkomplexität $T_{sort}(n) = \Theta(n \log n)$.
2. **Selektion:** Der Algorithmus führt einen einzelnen linearen Durchlauf über die sortierte Menge $A$ durch. Für jedes Element führt er einen Vergleich $s_i \ge t_{last}$ in konstanter Zeit aus. Diese Phase ist $T_{scan}(n) = \Theta(n)$.

Die gesamte Zeitkomplexität beträgt:
$$T(n) = T_{sort}(n) + T_{scan}(n) = \Theta(n \log n) + \Theta(n) = O(n \log n)$$

### Platzkomplexität
Die Platzkomplexität wird durch die Speicherung der Aktivitäts-Tupel bestimmt.
1. **Zusätzlicher Speicherplatz:** Der Algorithmus benötigt $O(1)$ zusätzlichen Speicherplatz für die Variablen `count` und `last_finish`.
2. **Gesamtspeicherplatz:** Wenn die Eingabe-Arrays als separate Strukturen bereitgestellt werden, erfordert die Erstellung der Liste von Tupeln $O(n)$ Speicherplatz. Wenn die Eingabe als vorab allokiertes Array von Objekten bereitgestellt wird, kann das Sortieren in-place erfolgen (z. B. mittels Heapsort), was zu $O(1)$ zusätzlichem Speicherplatz führt. In der bereitgestellten Standardimplementierung beträgt die Platzkomplexität aufgrund der Erstellung der `pairs`-Liste $O(n)$.