# Formale mathematische Spezifikation: Zählen distinkter Elemente in jedem Fenster

## 1. Definitionen und Notation

Sei $A = [a_0, a_1, \dots, a_{N-1}]$ eine Sequenz von Elementen, wobei $a_i \in \mathcal{U}$ für ein Universum $\mathcal{U}$ gilt. Sei $K \in \mathbb{Z}^+$ die feste Fenstergröße, sodass $1 \le K \le N$ gilt.

Ein gleitendes Fenster (Sliding Window) der Größe $K$, das am Index $i$ beginnt, ist definiert als die Teilsequenz $W_i = [a_i, a_{i+1}, \dots, a_{i+K-1}]$ für $0 \le i \le N-K$.

Wir definieren Folgendes:
*   **Frequenz-Map:** Eine Funktion $f_i: \mathcal{U} \to \mathbb{N}_0$, die die Anzahl jedes Elements im Fenster $W_i$ repräsentiert und wie folgt definiert ist:
    $$f_i(x) = \sum_{j=i}^{i+K-1} \mathbb{I}(a_j = x)$$
    wobei $\mathbb{I}(\cdot)$ die Indikatorfunktion ist.
*   **Support-Menge:** Die Menge der distinkten Elemente im Fenster $W_i$ ist der Support von $f_i$:
    $$\text{supp}(f_i) = \{x \in \mathcal{U} \mid f_i(x) > 0\}$$
*   **Zielausgabe:** Die Sequenz $D = [d_0, d_1, \dots, d_{N-K}]$, wobei $d_i = |\text{supp}(f_i)|$ gilt.

## 2. Algebraische Charakterisierung

Der Algorithmus basiert auf der inkrementellen Aktualisierung der Frequenz-Map $f_i$ zu $f_{i+1}$. Gegeben $f_i$, beinhaltet der Übergang zu $f_{i+1}$ das Entfernen von $a_i$ und das Hinzufügen von $a_{i+K}$:

$$f_{i+1}(x) = f_i(x) - \mathbb{I}(x = a_i) + \mathbb{I}(x = a_{i+K})$$

Die Anzahl der distinkten Elemente $d_{i+1}$ wird basierend auf dem Zustand der Frequenz-Map aus $d_i$ abgeleitet:

1.  **Aktualisierung für $a_{i+K}$:** Wenn $f_i(a_{i+K}) = 0$, dann ist $d_{i+1} = d_i + 1$. Andernfalls ist $d_{i+1} = d_i$.
2.  **Aktualisierung für $a_i$:** Wenn $f_{i+1}(a_i) = 0$, dann ist $d_{i+1} = d_{i+1} - 1$. Andernfalls bleibt $d_{i+1}$ unverändert.

**Schleifeninvariante:**
Zu Beginn jeder Iteration $i \in \{0, \dots, N-K\}$ erfüllt die Map $M$:
$$\forall x \in \mathcal{U}, M(x) = f_i(x) \quad \text{und} \quad |M| = d_i$$
wobei $|M|$ die Anzahl der Schlüssel in der Map mit einem Wert ungleich Null bezeichnet. Die Löschoperation `del map[old]` stellt sicher, dass die Invariante $|M| = \sum_{x \in \mathcal{U}} \mathbb{I}(M(x) > 0)$ aufrechterhalten wird.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus besteht aus zwei Phasen:
1.  **Initialisierung:** Das Konstruieren von $f_0$ erfordert $K$ Einfügungen in die Hash Map. Unter der Annahme einer gleichmäßigen Hash-Verteilung ist jede Einfügung im Durchschnitt $O(1)$. Gesamt: $O(K)$.
2.  **Gleitende Phase:** Die Schleife läuft für $N-K$ Iterationen. In jeder Iteration $i$:
    *   Erfolgt eine Einfügung und eine Löschung/Aktualisierung in der Map.
    *   Die Größe der Map wird abgefragt.
    *   Jede Operation ist amortisiert $O(1)$.

Die gesamte Zeitkomplexität $T(N)$ ist:
$$T(N) = O(K) + \sum_{i=0}^{N-K-1} O(1) = O(K + (N-K)) = O(N)$$
Somit ist der Algorithmus linear in Bezug auf die Eingabegröße $N$.

### Platzkomplexität
Die Platzkomplexität $S(N)$ wird durch die Speicherung der Frequenz-Map $M$ dominiert.
*   Die Map speichert zu jedem Zeitpunkt höchstens $K$ distinkte Elemente, da die Fenstergröße auf $K$ festgelegt ist.
*   Der benötigte zusätzliche Speicherplatz beträgt $O(K)$.
*   Das Ausgabe-Array erfordert $O(N-K+1)$ Speicherplatz.

Unter Ausschluss der Ausgabe beträgt die zusätzliche Platzkomplexität $O(K)$. Wenn das Universum $\mathcal{U}$ groß ist, bildet die Hash Map die aktiven Elemente effektiv auf einen Raum ab, der proportional zur Fenstergröße ist, was die $O(K)$-Anforderung erfüllt.