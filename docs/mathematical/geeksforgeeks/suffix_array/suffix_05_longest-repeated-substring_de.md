# Formale mathematische Spezifikation: Längster wiederholter Substring

## 1. Definitionen und Notation

Sei $\Sigma$ ein endliches Alphabet. Sei $S$ ein String der Länge $n$ über $\Sigma$, dargestellt als eine Sequenz von Zeichen $S = s_0s_1\dots s_{n-1}$, wobei $s_i \in \Sigma$. Wir bezeichnen die Menge aller Substrings von $S$ als $\mathcal{Sub}(S) = \{S[i..j] \mid 0 \le i \le j < n\}$.

*   **Suffixe:** Sei $Suffix_i$ der Suffix von $S$, der bei Index $i$ beginnt, definiert als $S[i..n-1]$. Die Menge aller Suffixe ist $\mathcal{S} = \{Suffix_0, Suffix_1, \dots, S_{n-1}\}$.
*   **Suffix Array ($SA$):** Das Suffix Array $SA$ ist eine Permutation der Indizes $\{0, 1, \dots, n-1\}$, so dass die entsprechenden Suffixe in lexikographischer Reihenfolge sortiert sind: $Suffix_{SA[0]} < Suffix_{SA[1]} < \dots < Suffix_{SA[n-1]}$.
*   **Longest Common Prefix ($LCP$):** Für zwei beliebige Strings $A$ und $B$ ist $LCP(A, B)$ die Länge des längsten Strings $P$, so dass $P$ ein Präfix von sowohl $A$ als auch $B$ ist.
*   **LCP Array:** Das Array $LCP$ der Länge $n$ ist so definiert, dass $LCP[i] = LCP(Suffix_{SA[i-1]}, Suffix_{SA[i]})$ für $1 \le i < n$, mit $LCP[0] = 0$.
*   **Ziel:** Wir suchen einen Substring $T \in \mathcal{Sub}(S)$, so dass es Indizes $i \neq j$ gibt, für die $S[i..i+|T|-1] = S[j..j+|T|-1] = T$, und $|T|$ maximiert wird.

## 2. Algebraische Charakterisierung

Die Korrektheit des Algorithmus beruht auf dem folgenden Theorem:

**Theorem:** Die Länge des längsten wiederholten Substrings in $S$ ist gegeben durch:
$$\max_{1 \le i < n} LCP[i]$$

**Beweisskizze:**
1.  **Suffizienz:** Wenn $LCP[i] = k > 0$, dann ist das Präfix der Länge $k$ gemeinsam für $Suffix_{SA[i-1]}$ und $Suffix_{SA[i]}$. Da dies unterschiedliche Suffixe sind, die an verschiedenen Positionen in $S$ beginnen, ist das Präfix der Länge $k$ ein wiederholter Substring.
2.  **Notwendigkeit:** Angenommen, der längste wiederholte Substring $T$ hat die Länge $L$. Dann ist $T$ ein Präfix von zwei verschiedenen Suffixen $Suffix_u$ und $Suffix_v$ (wobei $u \neq v$). Im sortierten Suffix Array seien $rank[u]$ und $rank[v]$ die Positionen dieser Suffixe. Ohne Beschränkung der Allgemeinheit nehmen wir an, dass $rank[u] < rank[v]$. Aufgrund der Eigenschaften der lexikographischen Sortierung muss $T$ ein Präfix aller Suffixe $Suffix_{SA[k]}$ für $rank[u] \le k \le rank[v]$ sein. Insbesondere ist $T$ ein Präfix von $Suffix_{SA[k-1]}$ und $Suffix_{SA[k]}$ für alle $k$ in diesem Bereich. Somit gilt $LCP[k] \ge |T|$ für ein gewisses $k$, was impliziert, dass $\max(LCP) \ge L$.

**Kasai's Algorithmus-Invariante:**
Um das $LCP$-Array in $O(n)$ zu berechnen, nutzen wir die Höhen-Eigenschaft. Sei $h_i$ der $LCP$-Wert des Suffixs, das bei $i$ beginnt, und seines Vorgängers im Suffix Array. Der Algorithmus hält die Invariante aufrecht:
$$h_{SA[rank[i]]} \ge h_{SA[rank[i-1]]} - 1$$
Dies ermöglicht es dem Zeiger $h$, höchstens $n$ Mal dekrementiert und höchstens $2n$ Mal inkrementiert zu werden, was eine lineare Zeitkomplexität sicherstellt.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die gesamte Zeitkomplexität ist $T(n) = T_{SA}(n) + T_{LCP}(n)$.
1.  **Konstruktion des Suffix Arrays:** Unter Verwendung von Standard-Sortieralgorithmen (z. B. Quicksort oder Mergesort) auf Suffixen dauert der Vergleich zweier Suffixe $O(n)$. Das Sortieren von $n$ Elementen erfordert $O(n \log n)$ Vergleiche. Somit ist $T_{SA}(n)$ naiv $O(n^2 \log n)$, aber durch Verwendung von Prefix Doubling oder Induced Sorting erreichen wir $T_{SA}(n) = O(n \log n)$.
2.  **Konstruktion des LCP Arrays (Kasai's):** Die Variable $h$ wird über die gesamte Ausführung der Schleife höchstens $n$ Mal inkrementiert und höchstens $n$ Mal dekrementiert. Jeder Zeichenvergleich ist $O(1)$. Somit ist $T_{LCP}(n) = O(n)$.
3.  **Gesamt:** $T(n) = O(n \log n) + O(n) = O(n \log n)$.

### Platzkomplexität
Der Algorithmus benötigt:
*   Den String $S$: $O(n)$
*   Das Suffix Array $SA$: $O(n)$
*   Das Rank Array: $O(n)$
*   Das LCP Array: $O(n)$
Der gesamte zusätzliche Speicherplatz ist $S(n) = O(n)$, was für dieses Problem optimal ist.