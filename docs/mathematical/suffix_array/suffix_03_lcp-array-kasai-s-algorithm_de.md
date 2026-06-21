# Formale mathematische Spezifikation: LCP-Array (Kasai's Algorithmus)

## 1. Definitionen und Notation

Sei $\Sigma$ ein endliches Alphabet. Sei $S$ ein String der Länge $N$ über $\Sigma$, dargestellt als eine Sequenz von Zeichen $S = s_0 s_1 \dots s_{N-1}$.
Wir definieren das $i$-te Suffix von $S$, bezeichnet als $S_i$, als den Teilstring $S[i \dots N-1]$. Die Menge aller Suffixe ist $\mathcal{S} = \{S_0, S_1, \dots, S_{N-1}\}$.

- **Suffix Array ($SA$):** Eine Permutation der Indizes $\{0, 1, \dots, N-1\}$, so dass die entsprechenden Suffixe in lexikographischer Reihenfolge sortiert sind: $S_{SA[0]} < S_{SA[1]} < \dots < S_{SA[N-1]}$.
- **Rank Array ($Rank$):** Die inverse Permutation von $SA$, definiert als $Rank[SA[i]] = i$. Somit bezeichnet $Rank[i]$ den lexikographischen Rang des Suffixes, das bei Index $i$ beginnt.
- **LCP Array ($LCP$):** Ein Array der Länge $N$, wobei $LCP[i]$ definiert ist als die Länge des längsten gemeinsamen Präfixes zwischen dem Suffix bei $SA[i]$ und dem Suffix bei $SA[i-1]$ für $i > 0$, und $LCP[0] = 0$. Formal:
  $$LCP[i] = \text{lcp}(S_{SA[i]}, S_{SA[i-1]}) = \max \{ k : S[SA[i] \dots SA[i]+k-1] = S[SA[i-1] \dots SA[i-1]+k-1] \}$$

## 2. Algebraische Charakterisierung

Die Korrektheit von Kasai's Algorithmus beruht auf der Beziehung zwischen den LCP-Werten von aufeinanderfolgenden Suffixen im ursprünglichen String $S$. Sei $h_i$ der LCP-Wert des Suffixes, das bei Index $i$ beginnt, mit seinem lexikographischen Vorgänger in $SA$. Das heißt, $h_i = LCP[Rank[i]]$.

**Satz (Kasai's Lemma):** Für jedes $i \in \{0, \dots, N-2\}$, wenn $Rank[i] > 0$, dann gilt:
$$h_{i+1} \geq h_i - 1$$

*Skizze des Beweises:* Sei $j = SA[Rank[i]-1]$. Per Definition ist $h_i = \text{lcp}(S_i, S_j)$. Wenn $h_i > 0$, dann ist $S[i] = S[j]$ und $S[i+1 \dots i+h_i-1] = S[j+1 \dots j+h_i-1]$. Das Suffix $S_{i+1}$ ist $S_i$ mit dem ersten Zeichen entfernt. Sein Vorgänger im Suffix-Array, $S_{j'}$, muss $S_{j'} \leq S_{i+1} < S_i$ erfüllen. Da $S_j$ der unmittelbare Vorgänger von $S_i$ ist, folgt, dass $S_j$ (oder ein Suffix zwischen $S_j$ und $S_i$) mindestens $h_i - 1$ Zeichen mit $S_{i+1}$ gemeinsam hat.

**Rekursionsgleichung:**
Der Algorithmus berechnet $h_i$ iterativ für $i = 0, \dots, N-1$. Sei $k_i$ die aktuelle Länge des verglichenen LCP.
1. Wenn $Rank[i] = 0$, dann ist $h_i = 0$.
2. Wenn $Rank[i] > 0$, sei $j = SA[Rank[i]-1]$. Der Algorithmus initialisiert $k = \max(0, h_{i-1} - 1)$ und inkrementiert $k$, solange $S[i+k] = S[j+k]$.
3. $LCP[Rank[i]] = k$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität beträgt $\Theta(N)$.
Wir analysieren die Gesamtzahl der Zeichenvergleiche, die von der Variablen $k$ durchgeführt werden.
- In jeder Iteration $i$ wird die Variable $k$ mit $\max(0, h_{i-1} - 1)$ initialisiert.
- Die `while`-Schleife inkrementiert $k$ nur, wenn ein Zeichenübereinstimmung gefunden wird.
- Da $k$ durch $N$ begrenzt ist und in jedem Schritt $i$ der Wert von $k$ um höchstens 1 abnimmt (aufgrund des "Kasai Shrink"), ist die Gesamtzahl der Dekremente höchstens $N$.
- Folglich kann die Gesamtzahl der Inkremente von $k$ über die gesamte Ausführung $2N$ nicht überschreiten.
- Da jede Iteration konstante Zeitoperationen plus die Inkremente von $k$ durchführt, ist die Gesamtarbeit:
  $$T(N) = \sum_{i=0}^{N-1} (O(1) + \text{increments}_i) = O(N) + O(N) = O(N)$$

### Platzkomplexität
- **Hilfsplatz:** Der Algorithmus benötigt Speicher für das $Rank$-Array ($N$ Integer) und das $LCP$-Array ($N$ Integer).
- **Gesamtplatz:** Angesichts der Eingabe $SA$ (Größe $N$) und des Strings $S$ (Größe $N$) beträgt die Gesamtplatzkomplexität $\Theta(N)$. Der Algorithmus arbeitet in-place relativ zu den erforderlichen Ausgabestrukturen und erfüllt damit die $O(N)$-Anforderung.