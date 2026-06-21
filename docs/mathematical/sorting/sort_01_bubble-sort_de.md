# Formale mathematische Spezifikation: Bubble Sort

## 1. Definitionen und Notation

Sei $A = [a_0, a_1, \dots, a_{n-1}]$ eine Sequenz von $n$ Elementen aus einer total geordneten Menge $(\mathcal{X}, \le)$. Das Ziel des Sortieralgorithmus ist es, eine Permutation $A' = [a'_0, a'_1, \dots, a'_{n-1}]$ zu erzeugen, sodass $a'_i \le a'_{i+1}$ für alle $0 \le i < n-1$ gilt.

- **Zustandsraum:** Der Zustand des Algorithmus bei jeder Iteration ist durch das Tupel $(A, k)$ definiert, wobei $A \in \mathcal{X}^n$ die aktuelle Konfiguration der Sequenz ist und $k \in \{1, \dots, n-1\}$ die Grenze des unsortierten Suffixes darstellt.
- **Swap-Operator:** Wir definieren einen Swap-Operator $\sigma_i: \mathcal{X}^n \to \mathcal{X}^n$, sodass für eine Sequenz $A$ die Operation $\sigma_i(A)$ zu einer Sequenz $A^*$ führt, bei der $A^*_i = A_{i+1}$, $A^*_{i+1} = A_i$ und $A^*_j = A_j$ für $j \notin \{i, i+1\}$ gilt.
- **Vergleich:** Der Algorithmus basiert auf dem Prädikat $P(i, A) \equiv (A_i > A_{i+1})$.

## 2. Algebraische Charakterisierung

Die Korrektheit von Bubble Sort wird durch die Aufrechterhaltung einer Schleifeninvariante begründet. Sei $k$ der Index, sodass alle Elemente im Suffix $A[k \dots n-1]$ an ihren endgültigen sortierten Positionen stehen.

**Schleifeninvariante:** Zu Beginn jeder Iteration der äußeren Schleife (indiziert durch $k$ von $n-1$ abwärts bis $1$) gelten die folgenden Bedingungen:
1. Für alle $j \ge k$ gilt $A_j = \max(\{A_0, \dots, A_j\})$.
2. Für alle $p, q$ mit $k \le p < q < n$ gilt $A_p \le A_q$.

**Übergangsfunktion:**
Die innere Schleife führt eine Sequenz von benachbarten Vergleichen und Swaps durch. Für ein festes $k$ führt die innere Schleife die folgende Transformation aus:
$$A^{(i+1)} = \begin{cases} \sigma_i(A^{(i)}) & \text{if } A^{(i)}_i > A^{(i)}_{i+1} \\ A^{(i)} & \text{otherwise} \end{cases}$$
für $i = 0, 1, \dots, k-1$. 

Nach $k$ Iterationen der inneren Schleife ist garantiert, dass für das Element $A_k$ gilt:
$$A_k = \max_{0 \le j \le k} \{A_j\}$$
Dies bestätigt, dass der "Bubbling"-Prozess das maximale Element des unsortierten Präfixes korrekt an die $k$-te Position befördert. Durch vollständige Induktion über $k$ terminiert der Algorithmus bei $k=0$, was zu einer sortierten Sequenz führt.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität wird durch die Anzahl der Vergleiche $C(n)$ bestimmt. Die äußere Schleife läuft für $k = n-1, n-2, \dots, 1$. Für jedes $k$ führt die innere Schleife $k$ Vergleiche durch.

Die Gesamtzahl der Vergleiche ergibt sich aus der arithmetischen Reihe:
$$T(n) = \sum_{k=1}^{n-1} k = \frac{(n-1)n}{2} = \frac{1}{2}n^2 - \frac{1}{2}n$$

- **Schlechtester Fall:** Wenn die Eingabe in umgekehrter Reihenfolge vorliegt, führt jeder Vergleich zu einem Swap. Die Anzahl der Operationen ist $\Theta(n^2)$.
- **Bestfall:** Mit der Optimierung durch vorzeitigen Abbruch (Prüfung, ob ein Swap stattgefunden hat), führt der Algorithmus bei einem bereits sortierten Array nur einen Durchlauf von $n-1$ Vergleichen durch. Somit gilt $T_{best}(n) = \Omega(n)$.
- **Durchschnittlicher Fall:** Da die Anzahl der Inversionen in einer zufälligen Permutation im Durchschnitt $\frac{n(n-1)}{4}$ beträgt, ist die erwartete Anzahl der Swaps $\Theta(n^2)$, was zu $T_{avg}(n) = \Theta(n^2)$ führt.

### Platzkomplexität
Der Algorithmus arbeitet in-place. Der einzige zusätzliche Speicherbedarf besteht für die Schleifenindizes ($k, i$) und ein boolesches Flag für die Optimierung, welche alle $O(1)$ Platz beanspruchen.

- **Zusätzlicher Speicher:** $S_{aux} = O(1)$.
- **Gesamtspeicher:** $S_{total} = O(n)$ zur Speicherung des Eingabe-Arrays $A$, zuzüglich $O(1)$ zusätzlichem Speicher.