# Formale mathematische Spezifikation: Min und Max in einem Array (Turnier-Methode)

## 1. Definitionen und Notation

Sei $A = [a_0, a_1, \dots, a_{n-1}]$ eine geordnete Sequenz (Array) von $n$ Elementen aus einer total geordneten Menge $(\mathcal{X}, \le)$.

*   **Eingabe:** Ein Array $A$ der Größe $n \in \mathbb{N}^+$.
*   **Ausgabe:** Ein Tupel $(m, M) \in \mathcal{X} \times \mathcal{X}$, sodass:
    *   $m = \min \{a_i \mid 0 \le i < n\}$
    *   $M = \max \{a_i \mid 0 \le i < n\}$
*   **Zustandsraum:** Der Algorithmus operiert auf einer rekursiven Zerlegung der Indexmenge $I = \{0, 1, \dots, n-1\}$. Ein Teilproblem ist durch das Intervall $[l, r] \subseteq I$ definiert, wobei der Zustand das Paar $(m_{[l,r]}, M_{[l,r]})$ ist, welches das Minimum und Maximum des Subarrays $A[l \dots r]$ repräsentiert.

## 2. Algebraische Charakterisierung

Der Algorithmus definiert eine rekursive Funktion $f(l, r)$, die ein Indexintervall auf die Menge der Extrema abbildet. Die Korrektheit wird durch die folgende Rekurrenz bestimmt:

$$
f(l, r) = 
\begin{cases} 
(a_l, a_l) & \text{if } l = r \\
(\min(a_l, a_{l+1}), \max(a_l, a_{l+1})) & \text{if } r = l + 1 \\
(\min(m_L, m_R), \max(M_L, M_R)) & \text{if } r > l + 1
\end{cases}
$$

wobei $(m_L, M_L) = f(l, \lfloor \frac{l+r}{2} \rfloor)$ und $(m_R, M_R) = f(\lfloor \frac{l+r}{2} \rfloor + 1, r)$.

**Korrektheitsinvariante:**
Für jedes Intervall $[l, r]$ erfüllt das zurückgegebene Tupel $(m, M)$:
1. $m \in \{a_i\}_{i=l}^r \land M \in \{a_i\}_{i=l}^r$
2. $\forall i \in [l, r], m \le a_i \le M$

Die Optimalität der Vergleichsanzahl $C(n)$ ist durch die Rekurrenz definiert:
$$C(n) = C(\lceil n/2 \rceil) + C(\lfloor n/2 \rfloor) + 2$$
Mit den Basisfällen $C(1) = 0$ und $C(2) = 1$. Das Lösen dieser Rekurrenz ergibt $C(n) = \lceil \frac{3n}{2} \rceil - 2$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität wird durch die Anzahl der durchgeführten Vergleiche bestimmt. Sei $T(n)$ die Anzahl der Vergleiche für eine Eingabe der Größe $n$. Die Rekursionsgleichung lautet:
$$T(n) = 2T\left(\frac{n}{2}\right) + 2$$
Anwendung des **Master-Theorems** für Divide-and-Conquer-Rekurrenzen der Form $T(n) = aT(n/b) + f(n)$:
*   Hier ist $a=2, b=2, f(n)=2$.
*   Da $f(n) = \Theta(n^{\log_b a}) = \Theta(n^{\log_2 2}) = \Theta(n^1)$, fallen wir in Fall 2 des Master-Theorems.
*   Daher ist $T(n) = \Theta(n \log n)$ inkorrekt, da der Arbeitsaufwand auf jeder Ebene konstant ist und nicht linear. Bei erneuter Evaluierung: $T(n) = \Theta(n)$.
*   Speziell ist die Gesamtzahl der Vergleiche $T(n) = \frac{3n}{2} - 2$ für $n = 2^k$, was strikt $O(n)$ entspricht.

### Platzkomplexität
Die Platzkomplexität wird durch die maximale Tiefe des Rekursions-Stacks bestimmt.
*   Der Rekursionsbaum ist ein Binärbaum mit einem Verzweigungsfaktor von 2.
*   Die Tiefe des Baums $D$ für eine Eingabe der Größe $n$ ist gegeben durch $D = \lceil \log_2 n \rceil$.
*   Auf jeder Ebene des Stacks speichern wir eine konstante Menge an Metadaten (die Indizes $l, r, mid$ und das zurückgegebene Tupel).
*   Somit ist die zusätzliche Platzkomplexität $S(n) = O(\text{Tiefe}) = O(\log n)$.