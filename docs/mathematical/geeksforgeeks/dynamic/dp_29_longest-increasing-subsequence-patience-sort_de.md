# Formale mathematische Spezifikation: Longest Increasing Subsequence ($O(n \log n)$ Patience Sort)

## 1. Definitionen und Notation

Sei $A = \langle a_1, a_2, \dots, a_n \rangle$ eine Sequenz von $n$ Elementen aus einer total geordneten Menge $(\mathcal{X}, \le)$.

Eine Teilsequenz von $A$ ist eine Sequenz $\langle a_{i_1}, a_{i_2}, \dots, a_{i_k} \rangle$, sodass $1 \le i_1 < i_2 < \dots < i_k \le n$ gilt. Die Teilsequenz ist streng monoton steigend, wenn $a_{i_1} < a_{i_2} < \dots < a_{i_k}$ gilt. Wir bezeichnen die Menge aller streng monoton steigenden Teilsequenzen von $A$ als $\mathcal{S}$. Das Ziel ist es, die Länge der längsten solchen Teilsequenz zu finden:
$$L = \max \{ k \mid \exists \langle a_{i_1}, \dots, a_{i_k} \rangle \in \mathcal{S} \}$$

Wir definieren den Zustandsraum $\mathcal{T}$ als eine Sequenz von "Tails" $T = \langle t_1, t_2, \dots, t_m \rangle$, wobei $t_j$ das kleinste Abschlusselement aller streng monoton steigenden Teilsequenzen der Länge $j$ repräsentiert, die im Präfix $A[1 \dots i]$ gefunden wurden.

## 2. Algebraische Charakterisierung

Der Algorithmus erhält die Invariante aufrecht, dass die Sequenz $T$ bei jedem Schritt $i \in \{1, \dots, n\}$ streng monoton steigend ist: $t_1 < t_2 < \dots < t_m$.

### Der Zustandsübergang
Sei $T^{(i)}$ der Zustand des Tails-Array nach der Verarbeitung von $a_i$. Gegeben $T^{(i-1)} = \langle t_1, \dots, t_m \rangle$:
1. Wenn $a_i > t_m$, dann ist $T^{(i)} = \langle t_1, \dots, t_m, a_i \rangle$.
2. Wenn $a_i \le t_m$, sei $j$ der eindeutige Index, für den $t_{j-1} < a_i \le t_j$ gilt (mit $t_0 = -\infty$). Dann ist $T^{(i)} = \langle t_1, \dots, t_{j-1}, a_i, t_{j+1}, \dots, t_m \rangle$.

### Korrektheitsinvariante
Die Länge der längsten monoton steigenden Teilsequenz, die am oder vor dem Index $i$ endet, entspricht exakt der Länge der Sequenz $T^{(i)}$.
**Beweisskizze:**
- **Monotonie:** Durch vollständige Induktion lässt sich zeigen: Wenn $T^{(i-1)}$ sortiert ist, bewahrt die binäre Suche die Sortiereigenschaft. Wenn $a_i$ angehängt wird, bleibt die Eigenschaft aufgrund der Bedingung $a_i > t_m$ erhalten. Wenn $a_i$ das Element $t_j$ ersetzt, gilt die Eigenschaft $t_{j-1} < a_i < t_{j+1}$, da $t_{j-1} < a_i \le t_j < t_{j+1}$ gilt.
- **Optimalität:** Für jede Länge $j$ ist $t_j$ der minimal mögliche Wert für das Ende einer monoton steigenden Teilsequenz der Länge $j$. Indem wir $t_j$ durch einen kleineren Wert $a_i$ ersetzen, erhöhen wir das Potenzial, die Teilsequenz in zukünftigen Schritten zu erweitern, ohne die aktuelle maximale Länge $m$ zu verringern.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus verarbeitet jedes Element $a_i \in A$ genau einmal. Für jedes $a_i$ führen wir eine binäre Suche auf der Sequenz $T$ durch.
- Sei $m_i$ die Länge von $T$ im Schritt $i$. Die binäre Suche benötigt $O(\log m_i)$ Zeit.
- Da $m_i \le n$ für alle $i$ gilt, ist der Aufwand pro Iteration durch $O(\log n)$ beschränkt.
- Die gesamte Zeitkomplexität $T(n)$ ergibt sich aus der Summation:
$$T(n) = \sum_{i=1}^{n} O(\log i) = O\left(\sum_{i=1}^{n} \log i\right) = O(\log(n!))$$
Unter Anwendung der Stirling-Formel gilt $\log(n!) \approx n \log n - n$, somit:
$$T(n) = O(n \log n)$$

### Platzkomplexität
Der Algorithmus verwaltet die Sequenz $T$. Im Schlechtesten Fall (wenn das Eingabe-Array $A$ bereits streng monoton steigend ist), wächst die Länge von $T$ auf $n$ an.
- Der benötigte zusätzliche Speicherplatz ist der Speicher für $T$, welcher $O(n)$ beträgt.
- Es werden keine weiteren Datenstrukturen benötigt, die mit $n$ skalieren, daher ist die gesamte Platzkomplexität:
$$S(n) = O(n)$$