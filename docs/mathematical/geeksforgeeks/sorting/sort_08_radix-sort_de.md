# Formale Mathematische Spezifikation: Radix Sort

## 1. Definitionen und Notation

Sei $A = [a_0, a_1, \dots, a_{n-1}]$ eine Eingabesequenz von $n$ nicht-negativen ganzen Zahlen, wobei jedes $a_i \in \mathbb{N}_0$ ist. Sei $b \in \mathbb{N}, b \ge 2$ die Basis (Radix) des Zahlensystems.

Jede ganze Zahl $a_i$ kann in Basis $b$ als eine Sequenz von Ziffern dargestellt werden:
$$a_i = \sum_{j=0}^{D-1} d_{i,j} \cdot b^j$$
wobei $d_{i,j} = \lfloor \frac{a_i}{b^j} \rfloor \pmod b$ die Ziffer an Position $j$ ist, und $D = \lfloor \log_b(\max(A)) \rfloor + 1$ die maximale Anzahl von Ziffern ist, die zur Darstellung des größten Elements in $A$ erforderlich ist.

Wir definieren eine stabile Sortierfunktion $f(A, j)$, die eine Permutation von $A$ zurückgibt, sodass für beliebige zwei Elemente $a_x, a_y$, bei denen $a_x$ im Input vor $a_y$ erscheint, gilt: wenn $d_{x,j} < d_{y,j}$, dann geht $a_x$ im Output $a_y$ voraus. Wenn $d_{x,j} = d_{y,j}$, bleibt die relative Reihenfolge von $a_x$ und $a_y$ erhalten.

## 2. Algebraische Charakterisierung

Die Korrektheit von Radix Sort beruht auf dem Induktionsprinzip über die Ziffernpositionen $j \in \{0, 1, \dots, D-1\}$.

**Schleifeninvariante:**
Sei $A^{(k)}$ der Zustand des Arrays nach $k$ Durchläufen des Algorithmus (Sortierung nach den Ziffern $0$ bis $k-1$). Nach dem $k$-ten Durchlauf ist die Sequenz $A^{(k)}$ gemäß den Werten der $k$-stelligen Suffixe der Basis-$b$-Darstellung der ganzen Zahlen sortiert. Insbesondere gilt für beliebige $a_x, a_y \in A^{(k)}$, wenn:
$$\sum_{j=0}^{k-1} d_{x,j} \cdot b^j < \sum_{j=0}^{k-1} d_{y,j} \cdot b^j$$
dann geht $a_x$ in $A^{(k)}$ dem Element $a_y$ voraus.

**Stabilitätsanforderung:**
Der Algorithmus verwendet einen stabilen Counting Sort als Unterprogramm $f(A, j)$. Stabilität ist definiert als:
$$\forall x, y \in \{0, \dots, n-1\}, x < y \land d_{x,j} = d_{y,j} \implies \text{pos}(a_x) < \text{pos}(a_y)$$
wobei $\text{pos}(\cdot)$ den Index im Output Array bezeichnet. Dies stellt sicher, dass die durch die Ziffern $0$ bis $j-1$ etablierte Sortierreihenfolge beim Sortieren nach Ziffer $j$ nicht gestört wird.

**Terminierung:**
Der Algorithmus terminiert, wenn $k = D$. In diesem Zustand wird die Bedingung zu:
$$\sum_{j=0}^{D-1} d_{x,j} \cdot b^j < \sum_{j=0}^{D-1} d_{y,j} \cdot b^j \iff a_x < a_y$$
Somit ist $A^{(D)}$ in nicht-absteigender Reihenfolge sortiert.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus führt $D$ Durchläufe durch. In jedem Durchlauf führen wir einen Counting Sort durch. Das Counting Sort Unterprogramm besteht aus:
1. Häufigkeitszählung: $\sum_{i=0}^{n-1} 1 = O(n)$.
2. Präfixsummenberechnung: $\sum_{i=0}^{b-1} 1 = O(b)$.
3. Konstruktion des Output Arrays: $\sum_{i=0}^{n-1} 1 = O(n)$.

Die gesamte Zeitkomplexität $T(n, D, b)$ ist die Summe der Arbeit über alle $D$ Durchläufe:
$$T(n, D, b) = \sum_{j=0}^{D-1} O(n + b) = O(D \cdot (n + b))$$
Mit $K = b$ erhalten wir die Standardform $O(D(n + K))$. In dem Fall, dass $b$ so gewählt wird, dass $b \approx n$, beträgt die Komplexität $O(D \cdot n)$.

### Platzkomplexität
Der Algorithmus benötigt zusätzlichen Platz für:
1. Das `counts` Array der Größe $b$ (oder $K$).
2. Das `output` Array der Größe $n$.

Die gesamte zusätzliche Platzkomplexität $S(n, K)$ beträgt:
$$S(n, K) = O(n + K)$$
Dieser Platz wird in jeder der $D$ Iterationen wiederverwendet, daher bleibt die gesamte Platzkomplexität $O(n + K)$.