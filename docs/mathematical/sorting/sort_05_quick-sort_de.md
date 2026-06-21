# Formale Mathematische Spezifikation: Quick Sort

## 1. Definitionen und Notation

Sei $A = [a_0, a_1, \dots, a_{n-1}]$ eine Sequenz von $n$ Elementen, die aus einer total geordneten Menge $(\mathcal{X}, \le)$ stammen. Ziel ist es, eine Permutation $P$ der Indizes $\{0, 1, \dots, n-1\}$ zu berechnen, sodass die resultierende Sequenz $A' = [a_{P(0)}, a_{P(1)}, \dots, a_{P(n-1)}]$ die nicht-absteigende Bedingung erfüllt:
$$a_{P(i)} \le a_{P(j)} \quad \forall i, j \in \{0, \dots, n-1\} \text{ where } i < j$$

Der Algorithmus arbeitet auf einem Sub-Array, das durch das Indexintervall $[L, R] \subseteq \{0, \dots, n-1\}$ definiert ist. Wir definieren die Partitionierungsfunktion $\mathcal{P}: \mathcal{X}^{R-L+1} \to \mathcal{X}^{R-L+1} \times \mathbb{Z}^2$, die ein Sub-Array auf ein neu geordnetes Sub-Array und ein Paar von Indizes $(lt, gt)$ abbildet, sodass gilt:
1. $\forall k \in [L, lt-1]: A[k] < \text{pivot}$
2. $\forall k \in [lt, gt]: A[k] = \text{pivot}$
3. $\forall k \in [gt+1, R]: A[k] > \text{pivot}$

## 2. Algebraische Charakterisierung

Die Korrektheit des 3-Wege Quick Sort wird durch die **Schleifeninvariante** bestimmt, die während der Partitionierungsphase aufrechterhalten wird. Sei $i$ der aktuelle Scan-Index, und $lt, gt$ seien die Grenzen des Bereichs "gleich dem pivot". Bei jeder Iteration $k$ der `while i <= gt` Schleife gilt die folgende Partitionierung:
- $A[L \dots lt-1] < \text{pivot}$
- $A[lt \dots i-1] = \text{pivot}$
- $A[i \dots gt]$ sind noch zu klassifizierende Elemente
- $A[gt+1 \dots R] > \text{pivot}$

Der Algorithmus terminiert, wenn $i > gt$, wodurch die Nachbedingung erfüllt ist, dass der Array in drei zusammenhängende Segmente partitioniert ist. Die Rekursion wird durch die Rekursionsgleichung für die Anzahl der Vergleiche $T(n)$ definiert:
$$T(n) = T(n_{<}) + T(n_{>}) + \Theta(n)$$
wobei $n_{<} + n_{=} + n_{>} = n$, und $n_{=}$ die Anzahl der Elemente ist, die gleich dem pivot sind. In der 3-Wege-Variante werden $n_{=}$ Elemente von nachfolgenden rekursiven Aufrufen ausgeschlossen, wodurch die Problemgröße effektiver reduziert wird als bei der Standard-2-Wege-Partitionierung.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität wird durch die Tiefe des Rekursionsbaums und die auf jeder Ebene geleistete Arbeit bestimmt.

- **Durchschnittlicher Fall:** Angenommen, die pivot-Auswahl partitioniert den Array in zwei annähernd gleiche Hälften, so lautet die Rekurrenz $T(n) = 2T(n/2) + \Theta(n)$. Nach dem **Master-Theorem** (Fall 2), wobei $a=2, b=2, f(n)=n$, erhalten wir $T(n) = \Theta(n \log n)$.
- **Schlechtester Fall:** Wenn die pivot-Auswahl konsistent zu einer stark unausgewogenen Partitionierung führt (z.B. $n_{<} = 0$ oder $n_{>} = 0$), wird die Rekurrenz zu $T(n) = T(n-1) + \Theta(n)$. Durch Expansion dieser Summation:
  $$T(n) = \sum_{k=1}^{n} k = \frac{n(n+1)}{2} = \Theta(n^2)$$
  Die 3-Wege-Partitionierung stellt jedoch sicher, dass, wenn alle Elemente gleich sind ($n_{<} = 0$ und $n_{>} = 0$), der Algorithmus in $O(n)$ Zeit terminiert, wodurch die $O(n^2)$-Degradation für Arrays mit hoher Duplikatdichte verhindert wird.

### Platzkomplexität
Die Platzkomplexität wird durch den für die Rekursion benötigten Hilfs-Stack dominiert.

- **Hilfsplatz:** Der Algorithmus verwendet einen expliziten Stack, um Sub-Array-Grenzen $(L, R)$ zu speichern. Im schlechtesten Fall einer unausgewogenen Partitionierung kann die Stack-Tiefe $O(n)$ erreichen.
- **Optimierter Platz:** Indem stets das größere Sub-Array zuletzt auf den Stack gelegt und zuerst in das kleinere Sub-Array rekursiv aufgerufen wird, ist die maximale Stack-Tiefe durch $O(\log n)$ begrenzt.
- **Gesamtplatz:** Da der Algorithmus Swaps in-place durchführt, beträgt die gesamte Hilfsplatzkomplexität $O(\log n)$ unter der Annahme von Tail-Call-Optimierung oder Stack-Größenverwaltung.