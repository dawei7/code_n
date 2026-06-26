# Formale mathematische Spezifikation: Palindrom-Partitionierung (Min Cuts)

## 1. Definitionen und Notation

Sei $\Sigma$ ein endliches Alphabet. Sei $s = s_0 s_1 \dots s_{n-1}$ ein String der Länge $n$, wobei $s_i \in \Sigma$. 
Ein Teilstring $s[i..j]$ ist definiert als die Sequenz der Zeichen $s_i s_{i+1} \dots s_j$ für $0 \le i \le j < n$.

**Definition 1 (Palindrom):** Ein String $P$ ist ein Palindrom, wenn $P = P^R$ gilt, wobei $P^R$ die Umkehrung von $P$ bezeichnet. Formal ist $s[i..j]$ genau dann ein Palindrom, wenn $s_{i+k} = s_{j-k}$ für alle $0 \le k \le j-i$ gilt.

**Definition 2 (Partition):** Eine Partition von $s$ ist eine Sequenz von Teilstrings $(p_1, p_2, \dots, p_k)$, sodass deren Konkatenation $s$ ergibt. Wir definieren die Menge aller gültigen Palindrom-Partitionen als:
$$\mathcal{P}(s) = \{ (p_1, \dots, p_k) \mid \forall m \in \{1, \dots, k\}, p_m \text{ ist ein Palindrom und } \bigoplus_{m=1}^k p_m = s \}$$

**Definition 3 (Zielsetzung):** Wir suchen die Minimierung der Anzahl der Schnitte, was äquivalent zur Minimierung von $(k-1)$ ist, wobei $k$ die Anzahl der Palindrom-Teilstrings in der Partition ist. Sei $f(i)$ die minimale Anzahl an Schnitten, die erforderlich sind, um das Suffix $s[i..n-1]$ zu partitionieren. Das Ziel ist die Berechnung von $f(0)$.

## 2. Algebraische Charakterisierung

Der Algorithmus basiert auf zwei verschiedenen Rekursionsgleichungen.

### Stufe 1: Palindrom-Vorberechnung
Sei $P(i, j)$ eine boolesche Indikatorfunktion, sodass $P(i, j) = 1$ gilt, wenn $s[i..j]$ ein Palindrom ist, und $P(i, j) = 0$ andernfalls. Die Rekursionsgleichung ist definiert als:
$$P(i, j) = \begin{cases} 1 & \text{if } i \ge j \\ (s_i = s_j) \land P(i+1, j-1) & \text{if } i < j \end{cases}$$
Dies definiert eine Dynamic Programming-Tabelle der Größe $n \times n$.

### Stufe 2: Min-Cut-Optimierung
Sei $dp[i]$ die minimale Anzahl an Schnitten, die für das Suffix $s[i..n-1]$ erforderlich sind. Der Induktionsanfang ist $dp[n] = -1$ (dies repräsentiert das leere Suffix, das keine weiteren Schnitte erfordert, angepasst für die finale Summierung). Die Rekursionsgleichung lautet:
$$dp[i] = \min \{ 1 + dp[j+1] \mid i \le j < n, P(i, j) = 1 \}$$
wobei das Endergebnis $dp[0]$ ist. Beachten Sie, dass die Kosten $0$ betragen, wenn $P(i, n-1) = 1$ (keine Schnitte für das gesamte Suffix erforderlich).

**Invarianten:**
1. Nach Abschluss von Stufe 1 identifiziert $P(i, j)$ für alle $0 \le i \le j < n$ korrekt die Palindrom-Teilstrings.
2. Nach Abschluss von Stufe 2 repräsentiert $dp[i]$ den Wert $\min_{k} \{ (\text{Anzahl der Schnitte für } s[i..n-1]) \}$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus besteht aus zwei Stufen:
1. **Stufe 1:** Die Berechnung von $P(i, j)$ beinhaltet das Füllen einer $n \times n$ Tabelle. Jeder Eintrag $(i, j)$ wird in $O(1)$ Zeit berechnet, gegeben die Ergebnisse von $(i+1, j-1)$. Die Gesamtlaufzeit beträgt:
   $$\sum_{i=0}^{n-1} \sum_{j=i}^{n-1} O(1) = \frac{n(n+1)}{2} = O(n^2)$$
2. **Stufe 2:** Die Berechnung von $dp[i]$ beinhaltet eine Iteration über $j$ von $i$ bis $n-1$. Die Gesamtlaufzeit beträgt:
   $$\sum_{i=0}^{n-1} \sum_{j=i}^{n-1} O(1) = O(n^2)$$
Somit ergibt sich eine gesamte Zeitkomplexität von $O(n^2) + O(n^2) = O(n^2)$.

### Platzkomplexität
1. **Hilfsspeicher:** Die Tabelle $P$ benötigt $O(n^2)$ Platz zur Speicherung der booleschen Werte. Das Array $dp$ benötigt $O(n)$ Platz.
2. **Gesamtspeicher:** Der dominante Term ist die $n \times n$ Matrix, was zu einer Platzkomplexität von $O(n^2)$ führt.

*Hinweis:* Obwohl der Speicherbedarf auf $O(n)$ reduziert werden kann, indem der Palindrom-Status mittels der "Expand-around-center"-Technik zur Laufzeit berechnet wird, behält der hier spezifizierte Standard-Dynamic-Programming-Ansatz eine Platzkomplexität von $O(n^2)$ bei.