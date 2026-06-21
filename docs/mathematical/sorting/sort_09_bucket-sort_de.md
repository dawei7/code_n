# Formale Mathematische Spezifikation: Bucket Sort

## 1. Definitionen und Notation

Sei $A = \{a_1, a_2, \dots, a_n\}$ ein Multiset von $n$ reellen Zahlen, sodass jedes $a_i \in [x_{\min}, x_{\max}] \subset \mathbb{R}$. Wir definieren den Bereich der Eingabe als $R = x_{\max} - x_{\min}$.

Wir definieren eine Partition des Intervalls $[x_{\min}, x_{\max}]$ in $k$ disjunkte Unterintervalle (Buckets), bezeichnet als $B_0, B_1, \dots, B_{k-1}$. Für ein gegebenes $k \in \mathbb{N}$ ist die Breite jedes Buckets definiert als:
$$w = \frac{R}{k}$$
Der $j$-te Bucket $B_j$ ist definiert als die Menge der Elemente $a_i$, sodass gilt:
$$B_j = \{a_i \in A \mid \lfloor \frac{a_i - x_{\min}}{w} \rfloor = j\}$$
Für den Randfall, in dem $a_i = x_{\max}$ ist, definieren wir die Abbildung auf den Index $k-1$, um die Aufnahme in den letzten Bucket sicherzustellen.

Die Ausgabe ist eine Sequenz $S = (s_1, s_2, \dots, s_n)$, die eine Permutation von $A$ ist, sodass $s_1 \leq s_2 \leq \dots \leq s_n$.

## 2. Algebraische Charakterisierung

Die Korrektheit von Bucket Sort beruht auf der Eigenschaft, dass die Verkettung sortierter Buckets eine sortierte Sequenz ergibt. Sei $f: A \to \{0, 1, \dots, k-1\}$ die Bucket-Zuweisungsfunktion:
$$f(a_i) = \min\left( \left\lfloor \frac{a_i - x_{\min}}{w} \right\rfloor, k-1 \right)$$

**Korrektheitsinvariante:**
Für beliebige zwei Buckets $B_u$ und $B_v$, wobei $u < v$, und für beliebige Elemente $x \in B_u$ und $y \in B_v$ gilt, dass $x \leq y$.

Beweisskizze:
Nach der Definition von $f(a_i)$, wenn $f(x) = u$ und $f(y) = v$ mit $u < v$, dann gilt:
$$\frac{x - x_{\min}}{w} < u+1 \leq v \leq \frac{y - x_{\min}}{w}$$
Multiplikation mit $w$ und Addition von $x_{\min}$ ergibt $x < y$. Wenn also jeder Bucket $B_j$ intern sortiert wird, um eine Sequenz $S_j$ zu erzeugen, ist die Verkettung $S = S_0 \oplus S_1 \oplus \dots \oplus S_{k-1}$ monoton nicht-fallend.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die gesamte Zeitkomplexität $T(n)$ ist die Summe der Verteilungszeit, der Sortierzeit für jeden Bucket und der Verkettungszeit.

1.  **Verteilung:** Das Abbilden von $n$ Elementen auf Buckets benötigt $\Theta(n)$ Zeit.
2.  **Sortierung:** Sei $n_j = |B_j|$ die Anzahl der Elemente in Bucket $j$. Die Zeit zum Sortieren der Buckets beträgt $\sum_{j=0}^{k-1} O(n_j^2)$, wenn Insertion Sort verwendet wird.
3.  **Verkettung:** Das Zusammenführen von $k$ Buckets benötigt $\Theta(n + k)$ Zeit.

**Durchschnittlicher Fall:** Unter der Annahme, dass die Eingabe $A$ aus einer Gleichverteilung gezogen wird, ist die erwartete Anzahl von Elementen in jedem Bucket $E[n_j] = \frac{n}{k}$. Setzt man $k = \Theta(n)$, so ist $E[n_j] = 1$. Die erwartete Zeitkomplexität ist:
$$E[T(n)] = \Theta(n) + \sum_{j=0}^{n-1} O(E[n_j^2]) = \Theta(n) + n \cdot O(1^2) = \Theta(n)$$

**Schlechtester Fall:** Wenn die Verteilung nicht-uniform ist, sodass alle Elemente einem einzigen Bucket zugeordnet werden ($n_j = n$ für ein bestimmtes $j$), wird die Komplexität:
$$T(n) = \Theta(n) + O(n^2) = O(n^2)$$

### Platzkomplexität
Der Algorithmus benötigt Hilfsplatz, um die $k$ Buckets und die darin verteilten $n$ Elemente zu speichern.

1.  **Bucket-Speicher:** Wir verwalten ein Array von $k$ Pointern/Listen, was $\Theta(k)$ Platz benötigt.
2.  **Element-Speicher:** Jedes Element $a_i$ wird genau einmal über alle Buckets hinweg gespeichert, was $\Theta(n)$ Platz benötigt.

Die gesamte Platzkomplexität beträgt $\Theta(n + k)$. Angesichts der Standardimplementierung, bei der $k \approx n$ ist, beträgt die Platzkomplexität $\Theta(n)$.