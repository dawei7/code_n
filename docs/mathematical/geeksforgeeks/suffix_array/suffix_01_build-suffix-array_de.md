# Formale mathematische Spezifikation: Aufbau eines Suffix-Arrays

## 1. Definitionen und Notation

Sei $\Sigma$ ein endliches geordnetes Alphabet. Sei $S = s_0s_1\dots s_{n-1}$ ein String der Länge $n$ über $\Sigma$, wobei $s_i \in \Sigma$. Wir bezeichnen den leeren String als $\epsilon$.

*   **Suffix:** Für jedes $0 \le i < n$ ist der Suffix $S_i$ der Teilstring $S[i \dots n-1] = s_i s_{i+1} \dots s_{n-1}$.
*   **Suffix-Array:** Das Suffix-Array $SA$ ist eine Permutation der Menge der Indizes $\{0, 1, \dots, n-1\}$, so dass die entsprechenden Suffixe lexikographisch geordnet sind: $S_{SA[0]} < S_{SA[1]} < \dots < S_{SA[n-1]}$.
*   **Lexikographische Ordnung:** Für zwei Strings $A$ und $B$ gilt $A < B$, wenn es einen Index $j$ gibt, so dass $A[k] = B[k]$ für alle $k < j$ und entweder ($j = |A| < |B|$) oder ($j < |A|, j < |B|$ und $A[j] < B[j]$).
*   **Rang-Array:** Sei $R_k[i]$ der lexikographische Rang des Präfixes der Länge $k$, das bei Index $i$ beginnt. Speziell gilt $R_k[i] = \text{rank}(S[i \dots \min(i+k-1, n-1)])$.

## 2. Algebraische Charakterisierung

Die Konstruktion basiert auf dem Prinzip der Präfix-Verdopplung. Wir definieren den Rang eines Suffixes der Länge $2^m$ basierend auf den Rängen zweier überlappender Präfixe der Länge $2^{m-1}$.

**Basisfall ($m=0$):**
Für die Länge $k=1$ ist der Rang $R_1[i]$ einfach der ordinale Wert des Zeichens $s_i$ in $\Sigma$:
$$R_1[i] = \text{ord}(s_i)$$

**Rekursiver Schritt ($m > 0$):**
Um den Rang für die Länge $2^m$ zu berechnen, definieren wir ein Tupel $T_m[i]$ für jeden Index $i$:
$$T_m[i] = \left( R_{2^{m-1}}[i], \quad R_{2^{m-1}}[i + 2^{m-1}] \right)$$
wobei wir $R_{2^{m-1}}[j] = -1$ für alle $j \ge n$ definieren (Padding für Suffixe, die kürzer als $2^{m-1}$ sind).

Der Rang $R_{2^m}[i]$ ist der Index von $T_m[i]$ in der sortierten Sequenz aller Tupel $\{T_m[0], T_m[1], \dots, T_m[n-1]\}$. Formal gilt:
$$R_{2^m}[i] = \text{rank}(T_m[i] \mid \{T_m[0], \dots, T_m[n-1]\} \text{ lexikographisch sortiert})$$

**Invariante:**
Nach $m$ Iterationen liefert das Array $R_{2^m}$ eine totale Ordnung aller Präfixe der Länge $2^m$. Der Algorithmus terminiert bei $m = \lceil \log_2 n \rceil$, wobei $R_{2^m}[i]$ eine eindeutige totale Ordnung aller Suffixe $S_i$ induziert, so dass $R_{2^m}[SA[j]] = j$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus durchläuft $k = \lceil \log_2 n \rceil$ Iterationen.
In jeder Iteration $m \in \{1, \dots, k\}$:
1.  **Tupelkonstruktion:** Wir konstruieren $n$ Tupel, was jeweils $O(1)$ Zeit benötigt. Gesamt: $O(n)$.
2.  **Sortierung:** Wir sortieren $n$ Tupel. Mit einem vergleichsbasierten Sortierverfahren dauert dies $O(n \log n)$ Zeit.
3.  **Rangzuweisung:** Wir durchlaufen die sortierten Tupel, um Ränge zuzuweisen, was $O(n)$ Zeit benötigt.

Die gesamte Zeitkomplexität $T(n)$ ergibt sich aus der Summation:
$$T(n) = \sum_{m=1}^{\lceil \log_2 n \rceil} O(n \log n) = O(n \log n \cdot \log n) = O(n \log^2 n)$$
*Hinweis: Wenn Radix-Sort für die Tupelsortierung verwendet wird, reduziert sich der innere Schritt auf $O(n)$, was zu einer Gesamtkomplexität von $O(n \log n)$ führt.*

### Platzkomplexität
Der Algorithmus benötigt Speicher für:
1.  Den Eingabestring $S$ der Größe $O(n)$.
2.  Das Rang-Array $R$ der Größe $O(n)$.
3.  Das Tupel-Array $T$ der Größe $O(n)$.
4.  Das Suffix-Array $SA$ der Größe $O(n)$.

Da alle Hilfsstrukturen linear von der Eingabelänge $n$ abhängen, beträgt die gesamte Platzkomplexität:
$$S(n) = O(n)$$