# Formale Mathematische Spezifikation: Cycle Sort

## 1. Definitionen und Notation

Sei $A = [a_0, a_1, \dots, a_{n-1}]$ ein Array von $n$ Elementen, die aus einer total geordneten Menge $(\mathcal{X}, \leq)$ stammen. Wir definieren das Sortierproblem als das Finden einer Permutation $\sigma$ der Indizes $\{0, 1, \dots, n-1\}$, sodass das resultierende Array $A' = [a_{\sigma(0)}, a_{\sigma(1)}, \dots, a_{\sigma(n-1)}]$ die Bedingung $a_{\sigma(i)} \leq a_{\sigma(j)}$ für alle $0 \leq i < j \leq n-1$ erfüllt.

*   **Zielfunktion für die Position:** Für jedes Element $x \in A$ sei $\text{pos}(x)$ der Rang von $x$ in $A$, definiert als:
    $$\text{pos}(x) = \sum_{j=0}^{n-1} \mathbb{I}(a_j < x) + \sum_{j=0}^{k-1} \mathbb{I}(a_j = x)$$
    wobei $\mathbb{I}(\cdot)$ die Indikatorfunktion ist und $k$ der aktuelle Index des zu platzierenden Elements ist.
*   **Zyklenzerlegung:** Die zur Sortierung von $A$ erforderliche Permutation kann in disjunkte Zyklen zerlegt werden. Sei $\pi: \{0, \dots, n-1\} \to \{0, \dots, n-1\}$ die Abbildung, bei der $\pi(i)$ der Index ist, an dem das Element, das sich derzeit bei $i$ befindet, liegen muss.
*   **Zustandsraum:** Der Algorithmus arbeitet im Zustandsraum $\mathcal{S} = \mathcal{X}^n \times \{0, \dots, n-1\} \times \mathcal{X}$, der die aktuelle Array-Konfiguration, den aktuellen Startindex des Zyklus und das "gehaltene" Element, das verschoben wird, repräsentiert.

## 2. Algebraische Charakterisierung

Der Algorithmus basiert auf der Zerlegung der Permutation $\pi$ in disjunkte Zyklen. Ein Zyklus ist eine Sequenz von Indizes $(i_0, i_1, \dots, i_m)$, sodass $\pi(i_j) = i_{j+1 \pmod{m+1}}$.

**Schleifeninvariante:**
Zu Beginn jeder Iteration der äußeren Schleife `cycle_start` $= s$ ist das Subarray $A[0 \dots s-1]$ sortiert und enthält die $s$ kleinsten Elemente des ursprünglichen Arrays an ihren korrekten Positionen.

**Übergangsregel:**
Gegeben ein Element $v$ am Index $i$, identifiziert der Algorithmus den Zielindex $j = \text{pos}(v)$. Die Swap-Operation ist definiert als:
$$(A[j], v) \leftarrow (v, A[j])$$
Diese Operation ist eine Transposition, die $v$ an seine korrekte sortierte Position bringt. Da die Gesamtzahl der Elemente endlich ist, muss die Sequenz der Verschiebungen $i \to j \to \dots \to i$ terminieren und einen Zyklus bilden.

**Korrektheit:**
Der Algorithmus ist korrekt, wenn für jeden Zyklus $C = \{i_0, i_1, \dots, i_m\}$ die Sequenz von $m$ Swaps dazu führt, dass $A[i_k]$ das Element $x$ enthält, sodass $\text{rank}(x) = i_k$. Da der Algorithmus alle $i \in \{0, \dots, n-1\}$ durchläuft und jedes Element höchstens einmal an seine korrekte Position verschoben wird, erfüllt der Endzustand $A'$ die Bedingung $A'[i] \leq A'[i+1]$ für alle $i$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität wird durch die Anzahl der durchgeführten Vergleiche bestimmt.

1.  **Allgemeiner Fall:** Für jedes `cycle_start` von $0$ bis $n-2$ führt der Algorithmus einen linearen Scan des verbleibenden Arrays durch, um die korrekte Position des aktuellen Elements zu bestimmen.
    Die Gesamtzahl der Vergleiche $T(n)$ ist gegeben durch:
    $$T(n) = \sum_{i=0}^{n-2} (n - 1 - i) = \sum_{k=1}^{n-1} k = \frac{(n-1)n}{2}$$
    Somit ist $T(n) = \Theta(n^2)$.

2.  **1-zu-N Optimierter Fall:** Wenn die Eingabe eine Permutation von $\{1, \dots, n\}$ ist, ist die Zielposition $\text{pos}(a_i) = a_i - 1$. Der Scan wird durch einen $O(1)$ Lookup ersetzt. Jeder Swap platziert mindestens ein Element an seiner endgültigen Position. Da es $n$ Elemente gibt, gibt es höchstens $n$ Swaps. Die gesamte Zeitkomplexität ist $T(n) = O(n)$.

### Platzkomplexität
Der Algorithmus führt alle Operationen in-place aus.
*   **Hilfsspeicher:** Der Algorithmus benötigt eine konstante Anzahl von Variablen (`item`, `pos`, `cycle_start`, `i`), um den aktuellen Zustand zu verfolgen.
*   **Gesamtplatz:** Die Platzkomplexität ist $O(1)$, da der Speicherverbrauch nicht mit der Eingabegröße $n$ skaliert, was die Anforderung an In-place-Sortierung erfüllt.