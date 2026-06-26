# Formale mathematische Spezifikation: Target Sum

## 1. Definitionen und Notation

Sei $A = \{a_1, a_2, \dots, a_n\}$ ein Multiset von $n$ nicht-negativen ganzen Zahlen, wobei $a_i \in \mathbb{N}_0$. Sei $T \in \mathbb{Z}$ die Zielzahl (Target Integer). Wir definieren die Gesamtsumme des Multisets als $\Sigma = \sum_{i=1}^n a_i$.

Wir suchen die Anzahl der Vorzeichensequenzen $\sigma = (\sigma_1, \sigma_2, \dots, \sigma_n)$ mit $\sigma_i \in \{+1, -1\}$, sodass gilt:
$$\sum_{i=1}^n \sigma_i a_i = T$$

Sei $P \subseteq \{1, \dots, n\}$ die Menge der Indizes, für die $\sigma_i = +1$ gilt, und $N \subseteq \{1, \dots, n\}$ die Menge der Indizes, für die $\sigma_i = -1$ gilt. Per Definition gilt $P \cup N = \{1, \dots, n\}$ und $P \cap N = \emptyset$. Der Ausdruck wird zu:
$$\sum_{i \in P} a_i - \sum_{j \in N} a_j = T$$

Da $\sum_{i \in P} a_i + \sum_{j \in N} a_j = \Sigma$ gilt, addieren wir die beiden Gleichungen und erhalten:
$$2 \sum_{i \in P} a_i = T + \Sigma \implies \sum_{i \in P} a_i = \frac{T + \Sigma}{2}$$

Sei $S = \frac{T + \Sigma}{2}$. Das Problem ist äquivalent dazu, die Anzahl der Teilmengen $P \subseteq \{1, \dots, n\}$ zu finden, deren Summe der Elemente gleich $S$ ist.

## 2. Algebraische Charakterisierung

Wir definieren den Zustandsraum $\mathcal{S} = \{0, 1, \dots, S\}$. Sei $dp[k][s]$ die Anzahl der Teilmengen der ersten $k$ Elemente $\{a_1, \dots, a_k\}$, die exakt zu $s$ summieren.

**Induktionsanfang:**
Für $k=0$ ist die einzige Teilmenge die leere Menge $\emptyset$, deren Summe 0 ergibt.
$$dp[0][0] = 1, \quad dp[0][s] = 0 \text{ für } s > 0$$

**Rekursionsgleichung:**
Für jedes Element $a_k$ haben wir zwei Möglichkeiten: Entweder wir schließen $a_k$ von der Teilmenge aus oder wir schließen es ein (vorausgesetzt $s \geq a_k$). Der Übergang ist definiert als:
$$dp[k][s] = dp[k-1][s] + dp[k-1][s - a_k]$$
wobei $dp[k-1][s - a_k] = 0$ gilt, falls $s < a_k$.

**Platzoptimierte Invariante:**
Da $dp[k]$ nur von $dp[k-1]$ abhängt, können wir den Zustand auf ein 1D-Array $dp[s]$ reduzieren. Um sicherzustellen, dass wir bei der Berechnung der Iteration $k$ die Werte der vorherigen Iteration $k-1$ verwenden, iterieren wir $s$ in absteigender Reihenfolge:
$$dp_{new}[s] = dp_{old}[s] + dp_{old}[s - a_k]$$
Die zu Beginn jeder Iteration $k$ aufrechterhaltene Schleifeninvariante besagt, dass $dp[s]$ die Anzahl der Teilmengen von $\{a_1, \dots, a_{k-1}\}$ repräsentiert, die zu $s$ summieren.

**Existenzbedingungen:**
Eine Lösung existiert genau dann, wenn:
1. $(T + \Sigma) \equiv 0 \pmod 2$
2. $|T| \leq \Sigma$
Wenn diese Bedingungen nicht erfüllt sind, ist die Anzahl der Möglichkeiten 0.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus besteht aus einer äußeren Schleife, die über jedes der $n$ Elemente des Eingabe-Arrays iteriert. Die innere Schleife iteriert über die möglichen Summen von $S$ abwärts bis $a_k$.
Die Gesamtzahl der Operationen ergibt sich aus der Summe:
$$T(n, S) = \sum_{k=1}^n (S - a_k + 1) \approx O(n \cdot S)$$
Da $S = \frac{T + \Sigma}{2}$ ist, beträgt die Zeitkomplexität $O(n \cdot \Sigma)$, wobei $\Sigma$ die Summe der Elemente im Eingabe-Array ist.

### Platzkomplexität
Der Algorithmus verwendet ein 1D-Array der Größe $S+1$, um die Anzahl der Möglichkeiten zum Erreichen jeder Teilsumme zu speichern.
$$Space = \Theta(S) = \Theta\left(\frac{T + \Sigma}{2}\right) = O(\Sigma)$$
Der zusätzliche Speicherbedarf beträgt $O(S)$, da wir lediglich den Zustand der aktuellen Teilsummen-Anzahlen beibehalten und effektiv ein rollierendes Update auf der DP-Tabelle durchführen.