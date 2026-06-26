# Formale mathematische Spezifikation: Minimale Anzahl an Seiten zuweisen

## 1. Definitionen und Notation

Sei $A = \{a_1, a_2, \dots, a_N\}$ eine geordnete Sequenz von $N$ positiven Ganzzahlen, wobei $a_i \in \mathbb{Z}^+$ die Anzahl der Seiten im $i$-ten Buch repräsentiert. Sei $M \in \mathbb{Z}^+$ die Anzahl der Studenten.

Wir definieren eine Partition von $A$ in $M$ zusammenhängende, nicht leere Teilsequenzen (Subarrays) $S_1, S_2, \dots, S_M$, sodass gilt:
1. $\bigcup_{j=1}^M S_j = A$ und $S_j \cap S_k = \emptyset$ für $j \neq k$.
2. Jedes $S_j$ besteht aus einem zusammenhängenden Bereich von Indizes $[l_j, r_j]$, sodass $l_1 = 1, r_M = N$ und $l_{j+1} = r_j + 1$.

Sei $\sigma(S_j) = \sum_{i \in S_j} a_i$ die Gesamtzahl der Seiten, die dem $j$-ten Studenten zugewiesen wurden. Das Ziel ist es, den Wert $X^*$ zu finden, der durch das folgende Minimax-Optimierungsproblem definiert ist:
$$X^* = \min_{\mathcal{P} \in \Omega} \left( \max_{1 \le j \le M} \sigma(S_j) \right)$$
wobei $\Omega$ die Menge aller gültigen Partitionen von $A$ in $M$ zusammenhängende Teilsequenzen ist.

Der Definitionsbereich des Antwortraums ist das Intervall $\mathcal{I} = [\max(A), \sum_{i=1}^N a_i]$.

## 2. Algebraische Charakterisierung

Der Algorithmus verwendet eine monotone Prädikatfunktion $f: \mathbb{Z} \to \{0, 1\}$, um die Durchführbarkeit zu bestimmen. Für eine gegebene Kapazität $C \in \mathcal{I}$ gilt $f(C) = 1$, falls eine Partition $\mathcal{P}$ existiert, sodass $\forall j: \sigma(S_j) \le C$, und $f(C) = 0$ andernfalls.

**Greedy-Kriterium für Durchführbarkeit:**
Um $f(C)$ zu evaluieren, definieren wir eine Greedy-Funktion $g(C)$, die die minimale Anzahl an Studenten $m_{req}$ berechnet, die erforderlich ist, um sicherzustellen, dass kein Student die Kapazität $C$ überschreitet:
$$m_{req}(C) = 1 + \sum_{i=1}^{N-1} \mathbb{I}\left( \text{prefix\_sum}(i, \text{last\_reset}) + a_{i+1} > C \right)$$
wobei $\mathbb{I}(\cdot)$ die Indikatorfunktion ist. Das Prädikat ist definiert als:
$$f(C) = \begin{cases} 1 & \text{falls } m_{req}(C) \le M \\ 0 & \text{falls } m_{req}(C) > M \end{cases}$$

**Monotonie:**
Die Funktion $f(C)$ ist in Bezug auf $C$ monoton nicht fallend. Insbesondere gilt: Wenn $C_1 < C_2$, dann ist $m_{req}(C_1) \ge m_{req}(C_2)$, was $f(C_1) \le f(C_2)$ impliziert. Diese Eigenschaft garantiert, dass die binäre Suche gegen das eindeutige Minimum $X^*$ konvergiert, für das $f(X^*) = 1$ gilt.

**Schleifeninvariante:**
Zu Beginn jeder Iteration der binären Suche mit den Grenzen $[L, R]$ gilt die folgende Invariante:
$$f(L-1) = 0 \quad \land \quad f(R) = 1$$
Die Suche terminiert, wenn $L = R$, was das optimale $X^* = L$ ergibt.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus führt eine binäre Suche über den Bereich $\mathcal{I} = [\max(A), \sum_{i=1}^N a_i]$ durch. Sei $S = \sum_{i=1}^N a_i$ und $K = \max(A)$. Die Anzahl der Iterationen $T$, die zur Konvergenz erforderlich sind, beträgt:
$$T = \lceil \log_2(S - K + 1) \rceil$$
In jeder Iteration führt die Funktion $f(C)$ einen linearen Durchlauf durch das Array $A$ aus, um $m_{req}(C)$ zu berechnen, was $\Theta(N)$ Operationen erfordert. Somit ergibt sich die gesamte Zeitkomplexität zu:
$$T_{total} = \Theta(N \cdot \log(S - K))$$

### Platzkomplexität
Der Algorithmus verwaltet eine konstante Anzahl an skalaren Variablen ($lo, hi, mid, needed, pages$), unabhängig von der Eingabegröße $N$.
- **Hilfsplatzkomplexität:** $\Theta(1)$.
- **Gesamtplatzkomplexität:** $\Theta(N)$ zur Speicherung des Eingabearrays $A$.
Da die Eingabe bereits bereitgestellt ist, beträgt die zusätzliche Platzkomplexität strikt $O(1)$.