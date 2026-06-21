# Formale mathematische Spezifikation: Longest Palindromic Substring

## 1. Definitionen und Notation
Sei $S \in \Sigma^*$ ein String der Länge $n$.
Ein String $P$ ist ein Palindrom, wenn $P = P^R$, wobei $P^R$ die Umkehrung von $P$ bezeichnet.
Wir definieren $S[i \dots j]$ als den Substring, der bei Index $i$ beginnt und bei $j$ endet (1-basiert).

## 2. Zielsetzung
Finde $i^*, j^*$, sodass $1 \leq i^* \leq j^* \leq n$, $S[i^* \dots j^*]$ ein Palindrom ist und die Länge $(j^* - i^* + 1)$ über alle palindromischen Substrings maximiert wird.

## 3. Algebraische Charakterisierung
Ein Substring $S[i \dots j]$ ist genau dann ein Palindrom, wenn:
1. Basisfälle: $j - i \leq 0 \implies$ True.
2. Induktionsschritt: $S[i] = S[j]$ und $S[i+1 \dots j-1]$ ein Palindrom ist.

## 4. Algorithmen-Formalisierung (Dynamische Programmierung)
Sei $P(i, j)$ ein boolesches Prädikat, das angibt, ob $S[i \dots j]$ ein Palindrom ist.
Rekursionsgleichung:
$$ P(i, j) = \begin{cases} 
\text{True} & \text{if } i \geq j \\
S[i] = S[j] \land P(i+1, j-1) & \text{if } i < j
\end{cases} $$

Der optimale Substring ist $\arg\max_{i, j \mid P(i, j)} (j - i + 1)$.

## 5. Algorithmen-Formalisierung (Expand Around Center)
Für jedes potenzielle Zentrum $c \in \{1, 1.5, 2, \dots, n-0.5, n\}$ definiere den maximalen Radius $r(c) \geq 0$, sodass $S[\lfloor c - r(c) \rfloor \dots \lceil c + r(c) \rceil]$ ein Palindrom ist.
Der Algorithmus inkrementiert $r(c)$ iterativ, bis die Bedingung nicht mehr erfüllt ist.
Die maximale Palindromlänge ist $\max_c (2 r(c) + 1)$ für ganzzahlige Zentren und $\max_c (2 r(c))$ für halbzahlige Zentren.

## 6. Komplexitätsanalyse
- **Zeitkomplexität:** Die Anzahl der Zentren beträgt $2n - 1$. Die Expansion erfordert höchstens $n/2$ Schritte. Somit ist die Zeitkomplexität durch $O(n^2)$ beschränkt.
- **Platzkomplexität:** Der „Expand Around Center“-Algorithmus verwaltet einen Zustand von $O(1)$ (Zentrumsindizes und aktuelle maximale Länge). Die Platzkomplexität ist strikt $O(1)$.