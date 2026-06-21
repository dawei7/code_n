# Formale mathematische Spezifikation: Optimal Binary Search Tree

## 1. Definitionen und Notation

Sei $K = \{k_1, k_2, \dots, k_n\}$ eine Menge von $n$ Keys, die so sortiert sind, dass $k_1 < k_2 < \dots < k_n$ gilt.
Sei $F = \{f_1, f_2, \dots, f_n\}$ eine Menge zugehöriger Frequenzen, wobei $f_i \in \mathbb{R}^+$ die Suchhäufigkeit des Keys $k_i$ repräsentiert.

Ein Binary Search Tree (BST) $T$ ist definiert als ein Wurzelbaum, bei dem für jeden Knoten $u$ mit Key $k_i$ alle Knoten im linken Teilbaum Keys $k_j < k_i$ und alle Knoten im rechten Teilbaum Keys $k_m > k_i$ besitzen.

Die **Suchkosten** eines Knotens $u$ auf der Tiefe $d(u)$ (wobei die Wurzel auf Tiefe 1 liegt) sind definiert als $f_u \cdot d(u)$. Die Gesamtkosten eines Baums $T$ betragen:
$$C(T) = \sum_{i=1}^n f_i \cdot d(k_i)$$

Wir definieren das Gewicht eines Teilbaums, der die Keys $k_i$ bis $k_j$ enthält, als die Summe ihrer Frequenzen:
$$w(i, j) = \sum_{m=i}^j f_m$$

Das Ziel ist es, einen Baum $T^*$ zu finden, sodass $C(T^*) = \min_{T \in \mathcal{T}} C(T)$ gilt, wobei $\mathcal{T}$ die Menge aller gültigen BSTs für die gegebenen Keys ist.

## 2. Algebraische Charakterisierung

Wir definieren den Zustand $dp[i][j]$ als die minimalen Suchkosten eines BST, der aus den Keys $\{k_i, \dots, k_j\}$ konstruiert wurde, wobei $1 \le i \le j \le n$ gilt.

Für ein Teilproblem, das durch das Intervall $[i, j]$ definiert ist, wählen wir eine Wurzel $k_r$, wobei $i \le r \le j$ gilt. Aufgrund der Eigenschaften eines BST muss der linke Teilbaum die Keys $\{k_i, \dots, k_{r-1}\}$ und der rechte Teilbaum die Keys $\{k_{r+1}, \dots, k_j\}$ enthalten.

Wenn diese Teilbäume an die Wurzel $k_r$ angehängt werden, erhöht sich die Tiefe jedes Knotens in den Teilbäumen um 1. Folglich erhöhen sich die Gesamtkosten um die Summe der Frequenzen aller Knoten in den Teilbäumen zuzüglich der Frequenz der Wurzel selbst, was exakt $w(i, j)$ entspricht.

Die Rekursionsgleichung ist gegeben durch:
$$dp[i][j] = \min_{i \le r \le j} \left( dp[i][r-1] + dp[r+1][j] \right) + w(i, j)$$

**Basisfälle:**
1. Wenn $i > j$, ist der Baum leer: $dp[i][j] = 0$.
2. Wenn $i = j$, besteht der Baum aus einem einzelnen Knoten: $dp[i][i] = f_i$.

Die finale Lösung ist $dp[1][n]$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus verwendet einen Ansatz der dynamischen Programmierung mit drei verschachtelten Schleifen.
1. Die äußere Schleife iteriert über die Länge des Intervalls $L = j - i + 1$, wobei $1 \le L \le n$ gilt.
2. Die mittlere Schleife iteriert über den Startindex $i$, wobei $1 \le i \le n - L + 1$ gilt.
3. Die innere Schleife iteriert über die möglichen Wurzeln $r$, wobei $i \le r \le j$ gilt.

Die Gesamtzahl der Operationen ist proportional zu:
$$T(n) = \sum_{L=1}^n \sum_{i=1}^{n-L+1} L = \sum_{L=1}^n (n - L + 1) \cdot L$$
Unter Verwendung der Identität für die Summe von Quadraten und arithmetischen Reihen ergibt sich:
$$T(n) = (n+1)\sum L - \sum L^2 = (n+1)\frac{n(n+1)}{2} - \frac{n(n+1)(2n+1)}{6} = \frac{n(n+1)(n+2)}{6}$$
Somit gilt $T(n) = \Theta(n^3)$.

### Platzkomplexität
Der Algorithmus verwaltet eine DP-Tabelle der Größe $n \times n$, um die Ergebnisse der Teilprobleme $dp[i][j]$ zu speichern. Zusätzlich wird ein Präfixsummen-Array der Größe $n+1$ verwendet, um $w(i, j)$ in $O(1)$ Zeit zu berechnen.
Die gesamte Platzkomplexität beträgt:
$$S(n) = O(n^2) + O(n) = O(n^2)$$
Dies ist optimal für die Standard-DP-Formulierung, da wir die Ergebnisse der $O(n^2)$ möglichen Teilintervalle speichern müssen.