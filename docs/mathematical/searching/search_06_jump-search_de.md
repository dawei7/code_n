# Formale mathematische Spezifikation: Jump Search (Block Search)

## 1. Definitionen und Notation

Sei $A = (a_0, a_1, \dots, a_{n-1})$ eine Folge von Elementen aus einer total geordneten Menge $(\mathcal{X}, \le)$, sodass für alle $i, j \in \{0, \dots, n-1\}$ gilt: Wenn $i < j$, dann $a_i \le a_j$.
Sei $x \in \mathcal{X}$ der gesuchte Zielwert.
Wir definieren den Suchraum als die Indexmenge $\mathcal{I} = \{0, 1, \dots, n-1\}$.

Der Algorithmus verwendet einen Sprungparameter $m \in \mathbb{Z}^+$, wobei $m = \lfloor \sqrt{n} \rfloor$.
Wir definieren die Menge der Sprungindizes als $\mathcal{J} = \{k \cdot m \mid k \in \mathbb{N}_0, k \cdot m < n\} \cup \{n-1\}$.

Die Ausgabe ist eine Funktion $f: \mathcal{X} \times \mathcal{I}^n \to \mathcal{I} \cup \{-1\}$, definiert als:
$$f(x, A) = \begin{cases} i & \text{falls } a_i = x \\ -1 & \text{falls } \forall i \in \mathcal{I}, a_i \neq x \end{cases}$$

## 2. Algebraische Charakterisierung

Der Algorithmus unterteilt $\mathcal{I}$ in eine Folge von Blöcken $B_k = \{i \in \mathbb{Z} \mid (k-1)m \le i < \min(km, n)\}$ für $k = 1, 2, \dots, \lceil n/m \rceil$.

### Schleifeninvariante
Sei $p_k$ der Wert der Variable `prev` zu Beginn der $k$-ten Iteration der Sprungphase. Die aufrechterhaltene Invariante lautet:
1. Wenn $x \in A$, dann existiert ein $k$, sodass $x \in \{a_i \mid p_k \le i < \min(p_k + m, n)\}$.
2. Für alle $j < p_k$ gilt $a_j < x$.

### Abbruchbedingung
Die Sprungphase terminiert beim kleinsten Index $k^*$, für den $a_{\min(k^*m, n)-1} \ge x$ oder $k^*m \ge n$ gilt.
Der Suchraum wird anschließend auf das Intervall $[p_{k^*}, \min(p_{k^*} + m, n))$ eingeschränkt. Die Korrektheit der nachfolgenden linearen Suche wird durch die Monotonie von $A$ garantiert: Da $a_{p_{k^*-1}} < x$ und $a_{\min(k^*m, n)-1} \ge x$ gilt, impliziert der Zwischenwertsatz für diskrete geordnete Mengen, dass $x$, sofern es existiert, innerhalb des identifizierten Blocks liegen muss.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus besteht aus zwei unterschiedlichen Phasen: der Sprungphase und der linearen Suchphase.

1. **Sprungphase:** Die Anzahl der Sprünge beträgt $N_J = \lceil n/m \rceil$. Bei jedem Sprung führen wir eine konstante Anzahl an Vergleichen durch. Somit beträgt die Zeitkomplexität $O(n/m)$.
2. **Lineare Suchphase:** Im Schlechtesten Fall befindet sich das Ziel am Ende des Blocks, was $N_L = m - 1$ Vergleiche erfordert.

Die gesamte Zeitkomplexität $T(n)$ ergibt sich zu:
$$T(n) = O\left(\frac{n}{m} + m\right)$$
Um $T(n)$ zu minimieren, leiten wir nach $m$ ab:
$$\frac{d}{dm} \left( \frac{n}{m} + m \right) = -\frac{n}{m^2} + 1$$
Das Nullsetzen der Ableitung ergibt $m^2 = n$ bzw. $m = \sqrt{n}$. Durch Einsetzen von $m = \sqrt{n}$ in den Komplexitätsausdruck erhalten wir:
$$T(n) = O\left(\frac{n}{\sqrt{n}} + \sqrt{n}\right) = O(\sqrt{n} + \sqrt{n}) = O(\sqrt{n})$$
Somit ist die Zeitkomplexität im Schlechtesten Fall $\Theta(\sqrt{n})$.

### Platzkomplexität
Der Algorithmus verwaltet eine feste Anzahl an skalaren Variablen: `step`, `prev` und `index`. Diese Variablen belegen $O(1)$ Platz. Da keine zusätzlichen Datenstrukturen proportional zur Eingabegröße $n$ allokiert werden, beträgt die gesamte zusätzliche Platzkomplexität:
$$S(n) = O(1)$$