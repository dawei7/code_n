# Formale mathematische Spezifikation: Mustererkennung mit Suffix-Array

## 1. Definitionen und Notation

Sei $\Sigma$ ein endliches geordnetes Alphabet. Sei $T$ ein Textstring der Länge $N$ über $\Sigma$, definiert als eine Sequenz $T = t_0 t_1 \dots t_{N-1}$, wobei $t_i \in \Sigma$. Wir bezeichnen den Substring von $T$, der am Index $i$ beginnt und am Index $j$ endet, als $T[i \dots j]$.

Ein **Suffix** von $T$, der am Index $i$ beginnt, ist definiert als $S_i = T[i \dots N-1]$ für $0 \le i < N$.
Das **Suffix-Array** $A$ ist eine Permutation der Menge der Indizes $\{0, 1, \dots, N-1\}$, so dass die Sequenz der Suffixe lexikographisch geordnet ist:
$$S_{A[0]} < S_{A[1]} < \dots < S_{A[N-1]}$$
wobei $<$ die Standard-Lexikographische Ordnung auf Strings bezeichnet.

Gegeben sei ein Muster $P$ der Länge $M$, wobei $P = p_0 p_1 \dots p_{M-1}$. Wir definieren das Suchproblem als das Finden der Menge von Indizes $\mathcal{I} = \{i \mid P \text{ ist ein Präfix von } S_i\}$. Da die Suffixe in $A$ sortiert sind, bilden alle Suffixe, die $P$ als Präfix haben, einen zusammenhängenden Bereich $[L, R]$ in $A$.

## 2. Algebraische Charakterisierung

Die Korrektheit des Algorithmus beruht auf der Monotonie der lexikographischen Ordnung. Wir definieren das Prädikat $\text{is\_prefix}(P, S)$ als:
$$\text{is\_prefix}(P, S) \iff S[0 \dots M-1] = P$$

Da $A$ sortiert ist, entspricht die Menge der Indizes $i$, für die $P$ ein Präfix von $S_{A[i]}$ ist, dem Intervall $[L, R]$, wobei:
1. $L = \min \{ k \in \{0, \dots, N-1\} \mid S_{A[k]} \ge P \}$
2. $R = \max \{ k \in \{0, \dots, N-1\} \mid S_{A[k]} \text{ beginnt mit } P \}$

Wir verwenden binäre Suche, um diese Grenzen zu identifizieren. Sei $f(k)$ die Vergleichsfunktion zwischen $P$ und $S_{A[k]}$:
$$f(k) = \begin{cases} -1 & \text{wenn } S_{A[k]} < P \\ 0 & \text{wenn } P \text{ ein Präfix von } S_{A[k]} \text{ ist} \\ 1 & \text{wenn } S_{A[k]} > P \text{ und } P \text{ kein Präfix ist} \end{cases}$$

Der Suchraum wird durch die Invariante der binären Suche partitioniert:
- **Invariante:** In jedem Schritt der binären Suche auf dem Intervall $[lo, hi]$ liegt die Zielgrenze innerhalb des aktuellen Bereichs.
- **Übergang:** Für einen Mittelpunkt $mid = \lfloor \frac{lo + hi}{2} \rfloor$:
  - Wenn $S_{A[mid]} < P$, dann ist $lo = mid + 1$.
  - Andernfalls ist $hi = mid$.

Dies konvergiert zum kleinsten Index $L$, so dass $S_{A[L]} \ge P$. Eine symmetrische binäre Suche wird durchgeführt, um die obere Grenze $R$ zu finden, bei der die Präfix-Bedingung fehlschlägt.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus führt zwei binäre Suchen über das Suffix-Array $A$ durch, das die Größe $N$ hat.
1. **Schritte der binären Suche:** Jede binäre Suche benötigt $\lceil \log_2 N \rceil$ Iterationen, um den Suchraum auf einen einzelnen Index einzugrenzen.
2. **Kosten des Vergleichs:** In jeder Iteration führen wir einen lexikographischen Vergleich zwischen $P$ und einem Suffix $S_{A[mid]}$ durch. Der Vergleich $P \stackrel{?}{=} S_{A[mid]}[0 \dots M-1]$ erfordert höchstens $M$ Zeichenvergleiche.
3. **Gesamtarbeit:** Die gesamte Zeitkomplexität $T(N, M)$ ist gegeben durch:
   $$T(N, M) = \Theta(\log N \cdot M)$$
   Dies ergibt sich aus der Summation der Arbeit über die Tiefe des binären Suchbaums, wobei jeder Knoten $O(M)$ Arbeit verrichtet.

### Platzkomplexität
- **Hilfsplatz:** Der Algorithmus benötigt nur eine konstante Anzahl von Zeigern ($lo, hi, mid, L, R$), was zu einer Hilfsplatzkomplexität von $O(1)$ führt.
- **Gesamtplatz:** Die Gesamtplatzkomplexität beträgt $O(N)$, dominiert durch die Speicherung des vorab berechneten Suffix-Arrays $A$ der Länge $N$. Der Eingabetext $T$ belegt ebenfalls $O(N)$ Platz.