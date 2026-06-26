# Formale mathematische Spezifikation: Fisher-Yates-Shuffle

## 1. Definitionen und Notation

Sei $A = (a_0, a_1, \dots, a_{n-1})$ eine Sequenz von $n$ verschiedenen Elementen, die zu einer Menge $\mathcal{X}$ gehören. Die Menge aller möglichen Permutationen von $A$ wird als $\mathcal{S}_n$ bezeichnet, wobei $|\mathcal{S}_n| = n!$ gilt.

*   **Eingabe:** Eine Sequenz $A^{(0)} \in \mathcal{S}_n$.
*   **Zustandsraum:** Der Algorithmus durchläuft eine Sequenz von Zuständen $A^{(k)}$ für $k = 0, 1, \dots, n-1$, wobei $A^{(k)}$ die Konfiguration des Array nach $k$ Iterationen darstellt.
*   **Zufallsvariable:** Sei $J_i$ eine diskrete gleichverteilte Zufallsvariable, die den in Iteration $i$ gewählten Index repräsentiert, sodass $J_i \sim \text{Uniform}\{0, 1, \dots, i\}$ gilt.
*   **Ausgabe:** Eine Permutation $A^{(n-1)}$, sodass für jedes $\sigma \in \mathcal{S}_n$ die Wahrscheinlichkeit $P(A^{(n-1)} = \sigma) = \frac{1}{n!}$ beträgt.

## 2. Algebraische Charakterisierung

Der Fisher-Yates-Shuffle (die Variante von Durstenfeld) definiert eine Sequenz von Transpositionen. Sei $\tau_{i, j}$ der Transpositionsoperator, der die Elemente an den Indizes $i$ und $j$ vertauscht. Der Algorithmus erzeugt eine Sequenz von Permutationen:

$$A^{(n-k)} = A^{(n-k+1)} \circ \tau_{n-k, J_{n-k}}$$

wobei $k$ von $1$ bis $n-1$ läuft. 

### Korrektheit durch vollständige Induktion
Um zu beweisen, dass der Algorithmus eine Gleichverteilung erzeugt, definieren wir die Schleifeninvariante: Zu Beginn der Iteration $i$ (wobei $i$ von $n-1$ abwärts bis $1$ läuft) ist der Suffix $A[i+1 \dots n-1]$ eine gleichverteilte zufällige Permutation der $n-1-i$ Elemente, die ursprünglich an diesen Positionen standen, und der Präfix $A[0 \dots i]$ enthält die verbleibenden Elemente.

**Induktionsanfang:** Für $i = n-1$ ist der Suffix leer und der Präfix ist das ursprüngliche Array. Die Wahrscheinlichkeit, dass ein beliebiges Element am Index $n-1$ steht, ist $P(J_{n-1} = j) = \frac{1}{n}$ für alle $j \in \{0, \dots, n-1\}$.

**Induktionsschritt:** Wir nehmen an, dass nach $k$ Schritten jede Sequenz von $k$ Elementen mit einer Wahrscheinlichkeit von $\frac{(n-k)!}{n!}$ im Suffix platziert wurde. Im nächsten Schritt wählen wir einen Index $j \in \{0, \dots, n-k-1\}$ mit einer Wahrscheinlichkeit von $\frac{1}{n-k}$. Die Wahrscheinlichkeit, dass ein spezifisches Element $x$ an die Position $n-k-1$ bewegt wird, ist:
$$P(\text{element } x \text{ is chosen}) = P(\text{chosen at step } k) \times P(\text{not chosen in steps } 0 \dots k-1)$$
$$= \frac{1}{n-k} \times \prod_{m=0}^{k-1} \left(1 - \frac{1}{n-m}\right) = \frac{1}{n-k} \times \frac{n-k}{n} = \frac{1}{n}$$
Somit hat durch vollständige Induktion jedes Element eine Wahrscheinlichkeit von $1/n$, jede Position zu besetzen, was die Bedingung für eine Gleichverteilung über $\mathcal{S}_n$ erfüllt.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus besteht aus einer einzelnen Schleife, die von $i = n-1$ abwärts bis $1$ iteriert.
Sei $T(n)$ die gesamte Zeitkomplexität. Der in jeder Iteration $i$ durchgeführte Aufwand besteht aus:
1. Generierung einer Zufallszahl $J_i$: $O(1)$ unter der Annahme eines PRNG mit konstanter Laufzeit.
2. Vertauschen zweier Elemente im Speicher: $O(1)$.

Die gesamte Zeitkomplexität ergibt sich aus der Summation:
$$T(n) = \sum_{i=1}^{n-1} (O(1) + O(1)) = O(n)$$
Da die Anzahl der Operationen linear mit der Eingabegröße $n$ skaliert, ist der Algorithmus $\Theta(n)$.

### Platzkomplexität
Der Algorithmus arbeitet in-place. Wir definieren den zusätzlichen Speicherbedarf $S(n)$ als den Speicher, der über das Eingabe-Array hinaus benötigt wird.
*   Der Algorithmus verwendet eine konstante Anzahl an skalaren Variablen (den Schleifenindex $i$, den Zufallsindex $j$ und eine temporäre Variable für die Vertauschungsoperation).
*   Es werden keine zusätzlichen Datenstrukturen allokiert, deren Größe proportional zu $n$ ist.

Somit ist die zusätzliche Platzkomplexität:
$$S(n) = O(1)$$
Die gesamte Platzkomplexität, einschließlich des Eingabe-Arrays, beträgt $O(n)$.