# Formale Mathematische Spezifikation: Zähle Distinkte Substrings

## 1. Definitionen und Notation

Sei $\Sigma$ ein endliches Alphabet. Sei $S$ ein String der Länge $N$ über $\Sigma$, dargestellt als eine Sequenz von Zeichen $S = s_0s_1\dots s_{N-1}$, wobei $s_i \in \Sigma$.

*   **Substring:** Ein Substring $S[i..j]$ ist eine zusammenhängende Sequenz von Zeichen $s_i s_{i+1} \dots s_j$, wobei $0 \le i \le j < N$. Die Menge aller Substrings von $S$ wird mit $\mathcal{Sub}(S)$ bezeichnet.
*   **Suffix:** Ein Suffix $S_i$ ist der Substring $S[i..N-1]$ für $0 \le i < N$. Die Menge aller Suffixe ist $\mathcal{Suf}(S) = \{S_0, S_1, \dots, S_{N-1}\}$.
*   **Suffix Array ($SA$):** Eine Permutation der Indizes $\{0, 1, \dots, N-1\}$, so dass die Suffixe lexikographisch sortiert sind: $S_{SA[0]} < S_{SA[1]} < \dots < S_{SA[N-1]}$.
*   **LCP Array:** Eine Sequenz $LCP$ der Länge $N$, wobei $LCP[i]$ die Länge des längsten gemeinsamen Präfixes zwischen dem Suffix $S_{SA[i]}$ und seinem Vorgänger $S_{SA[i-1]}$ im sortierten Suffix Array ist, für $i > 0$, und $LCP[0] = 0$. Formal:
    $$LCP[i] = \max \{ k : S[SA[i]..SA[i]+k-1] = S[SA[i-1]..SA[i-1]+k-1] \}$$

## 2. Algebraische Charakterisierung

Die Gesamtzahl der Substrings in $S$ ergibt sich aus der Summe der Längen aller Suffixe, da jedes Suffix $S_i$ $N-i$ Substrings (seine Präfixe) beiträgt. Somit:
$$|\mathcal{Sub}(S)|_{total} = \sum_{i=0}^{N-1} (N - i) = \frac{N(N+1)}{2}$$

Um die Anzahl der *distinkten* Substrings zu ermitteln, beobachten wir, dass das sortierte Suffix Array $SA$ identische Präfixe gruppiert. Für jedes Suffix $S_{SA[i]}$ wurden die Präfixe der Längen $1, 2, \dots, LCP[i]$ bereits als Präfixe des lexikographisch vorhergehenden Suffixes $S_{SA[i-1]}$ gezählt.

Die Anzahl der eindeutigen Substrings, die vom Suffix $S_{SA[i]}$ beigesteuert werden, ist die Länge des Suffixes abzüglich der Länge des längsten Präfixes, das es mit seinem Vorgänger teilt:
$$\text{Unique}(S_{SA[i]}) = |S_{SA[i]}| - LCP[i] = (N - SA[i]) - LCP[i]$$

Durch Summieren über alle Suffixe ergibt sich die Gesamtzahl der distinkten Substrings $\mathcal{D}(S)$ zu:
$$\mathcal{D}(S) = \sum_{i=0}^{N-1} (N - SA[i] - LCP[i])$$

Durch Einsetzen der gesamten Substring-Anzahl leiten wir die Identität ab:
$$\mathcal{D}(S) = \frac{N(N+1)}{2} - \sum_{i=0}^{N-1} LCP[i]$$

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus besteht aus drei Hauptphasen:
1.  **Suffix Array Konstruktion:** Unter Verwendung eines optimalen Konstruktionsalgorithmus (z. B. SA-IS oder Prefix Doubling mit Radix Sort) wird das Suffix Array $SA$ in $T_{SA} = O(N \log N)$ oder $O(N)$ konstruiert.
2.  **LCP Array Konstruktion:** Unter Verwendung von Kasais Algorithmus berechnen wir $LCP$ in $T_{LCP} = O(N)$. Kasais Algorithmus basiert auf der Beobachtung, dass der LCP-Wert beim Übergang von Suffix $S_i$ zu $S_{i+1}$ um höchstens 1 abnimmt, was sicherstellt, dass der Zeiger $h$ höchstens $2N$ Mal inkrementiert wird.
3.  **Summation:** Die abschließende Summation ist ein linearer Durchlauf des $LCP$-Arrays und benötigt $T_{sum} = O(N)$.

Die gesamte Zeitkomplexität wird von der Suffix Array Konstruktion dominiert:
$$T(N) = T_{SA} + T_{LCP} + T_{sum} = O(N \log N) + O(N) + O(N) = O(N \log N)$$

### Platzkomplexität
Der Algorithmus benötigt Speicher für:
*   Den Eingabestring $S$: $O(N)$.
*   Das Suffix Array $SA$: $O(N)$.
*   Das Rank-Array (Inverse von $SA$): $O(N)$.
*   Das LCP-Array: $O(N)$.

Die gesamte zusätzliche Platzkomplexität beträgt:
$$S(N) = O(N) + O(N) + O(N) + O(N) = O(N)$$