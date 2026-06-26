# Formale mathematische Spezifikation: Randomized Quicksort

## 1. Definitionen und Notation

Sei $A = [a_0, a_1, \dots, a_{n-1}]$ ein Array von $n$ Elementen aus einer total geordneten Menge $(\mathcal{X}, \le)$. Das Ziel ist es, eine Permutation $\sigma$ der Indizes $\{0, 1, \dots, n-1\}$ zu finden, sodass das resultierende Array $A' = [a_{\sigma(0)}, a_{\sigma(1)}, \dots, a_{\sigma(n-1)}]$ die Bedingung $a_{\sigma(i)} \le a_{\sigma(j)}$ für alle $0 \le i < j < n$ erfüllt.

Wir definieren den Zustandsraum $\mathcal{S}$ als die Menge aller Permutationen von $A$. Der Algorithmus arbeitet mittels einer rekursiven Funktion $Q(A, \text{lo}, \text{hi})$, welche das Subarray $A[\text{lo} \dots \text{hi}]$ sortiert.

Sei $\mathcal{R}$ eine Zufallsvariable, die die Wahl des Pivot-Index repräsentiert, wobei $\mathcal{R} \sim \text{Uniform}(\text{lo}, \text{hi})$. Die Partitionierungsfunktion $P(A, \text{lo}, \text{hi}, \mathcal{R})$ bildet das Subarray auf einen Pivot-Index $p \in [\text{lo}, \text{hi}]$ ab, sodass gilt:
1. $\forall k \in [\text{lo}, p-1] : A[k] \le A[p]$
2. $\forall k \in [p+1, \text{hi}] : A[k] > A[p]$

## 2. Algebraische Charakterisierung

Die Korrektheit des Algorithmus wird durch die rekursive Zerlegung des Problems bestimmt. Gegeben ein zufällig gewählter Pivot-Index $p$, unterteilt der Algorithmus das Problem in zwei Teilprobleme der Größe $k$ und $n-k-1$.

Die Rekurrenz für die erwartete Anzahl an Vergleichen $T(n)$ ist gegeben durch:
$$T(n) = (n-1) + \frac{1}{n} \sum_{k=0}^{n-1} (T(k) + T(n-k-1))$$
wobei:
- $(n-1)$ die Kosten des Partitionierungsschritts (Lomuto-Partitionierung) repräsentiert.
- $\frac{1}{n} \sum_{k=0}^{n-1} (\dots)$ den Erwartungswert über die gleichverteilte Wahl des Pivot-Index $k$ repräsentiert, welcher die Größen der resultierenden Subarrays bestimmt.

**Schleifeninvariante:**
Für den Partitionierungsschritt sei $i$ der Index, für den $A[\text{lo} \dots i-1] \le \text{pivot}$ und $A[i \dots j-1] > \text{pivot}$ gilt. Bei jeder Iteration $j \in [\text{lo}, \text{hi}-1]$ bleibt die Invariante erhalten, dass das Subarray in Elemente, die kleiner oder gleich dem Pivot sind, und Elemente, die strikt größer als der Pivot sind, partitioniert ist.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Um die erwartete Zeitkomplexität $E[T(n)]$ abzuleiten, vereinfachen wir die Rekurrenz:
$$T(n) = (n-1) + \frac{2}{n} \sum_{k=0}^{n-1} T(k)$$
Multiplikation mit $n$:
$$n T(n) = n(n-1) + 2 \sum_{k=0}^{n-1} T(k)$$
Subtraktion der Gleichung für $n-1$:
$$n T(n) - (n-1) T(n-1) = 2(n-1) + 2 T(n-1)$$
$$n T(n) = (n+1) T(n-1) + 2(n-1)$$
Division durch $n(n+1)$:
$$\frac{T(n)}{n+1} = \frac{T(n-1)}{n} + \frac{2(n-1)}{n(n+1)}$$
Unter Verwendung der Methode der Teleskopsummen beobachten wir, dass $\frac{T(n)}{n+1} \approx 2 \sum \frac{1}{n} \approx 2 \ln n$. Somit gilt $T(n) = O(n \log n)$.

Die Komplexität im schlechtesten Fall bleibt $T(n) = \sum_{i=1}^n i = O(n^2)$, was eintritt, wenn die Pivot-Wahl konsistent das kleinste oder größte Element liefert, obwohl die Wahrscheinlichkeit für diese Sequenz $P = \prod_{i=1}^n \frac{2}{i} = \frac{2^n}{n!}$ beträgt, welche für $n \to \infty$ gegen $0$ konvergiert.

### Platzkomplexität
Die Platzkomplexität wird durch die maximale Tiefe des Rekursions-Stack bestimmt.
- **Durchschnittlicher Fall:** Die erwartete Tiefe des Rekursionsbaums beträgt $O(\log n)$, was zu einer erwarteten zusätzlichen Platzkomplexität von $O(\log n)$ führt.
- **Schlechtester Fall:** Im Falle von stark unausgeglichenen Partitionen kann die Rekursionstiefe $O(n)$ erreichen, was zu einer Platzkomplexität von $O(n)$ führt.
- **Gesamtplatzbedarf:** Da der Algorithmus in-place arbeitet, beträgt die gesamte Platzkomplexität $O(n)$ für die Speicherung der Eingabe, mit $O(\log n)$ erwartetem zusätzlichem Platzbedarf für den Call-Stack.