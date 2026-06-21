# Formale mathematische Spezifikation: Reverse String (Rekursiv)

## 1. Definitionen und Notation

Sei $\Sigma$ ein endliches Alphabet. Wir definieren die Eingabe als eine Sequenz (oder ein Array) $S$ der Länge $n \in \mathbb{N}_0$, wobei $S = (s_0, s_1, \dots, s_{n-1})$ und jedes $s_i \in \Sigma$ gilt.

Der Zustandsraum $\mathcal{S}$ des Algorithmus ist durch das Tupel $(S, \ell, r)$ definiert, wobei:
*   $S \in \Sigma^n$ die veränderbare Sequenz von Zeichen ist.
*   $\ell \in \{0, 1, \dots, n\}$ der linke Pointer-Index ist.
*   $r \in \{-1, 0, \dots, n-1\}$ der rechte Pointer-Index ist.

Das Ziel ist die Definition einer Transformation $f: \Sigma^n \to \Sigma^n$, sodass $f(S) = S'$, wobei $s'_i = s_{n-1-i}$ für alle $0 \le i < n$ gilt. Die rekursive Funktion $H(\ell, r)$ fungiert als Zustandstransformator für die Sequenz $S$.

## 2. Algebraische Charakterisierung

Der Algorithmus wird durch eine rekursive Übergangsfunktion $H: \mathbb{N} \times \mathbb{N} \to \text{void}$ gesteuert. Sei $\tau(a, b)$ der Transpositionsoperator, sodass $\tau(S, i, j)$ die Elemente an den Indizes $i$ und $j$ vertauscht.

Das Verhalten des Algorithmus ist durch die folgende Rekursionsgleichung definiert:

$$
H(\ell, r) = 
\begin{cases} 
\text{id} & \text{if } \ell \ge r \\
H(\ell + 1, r - 1) \circ \tau(S, \ell, r) & \text{if } \ell < r 
\end{cases}
$$

**Schleifeninvariante:**
Auf jeder Rekursionstiefe $k$ (wobei $k=0$ der initiale Aufruf ist), erfüllt der Zustand der Sequenz $S^{(k)}$:
1. Für alle $i < \ell_k$ und $i > r_k$ befinden sich die Elemente bereits an ihren Zielpositionen: $s_i = s_{n-1-i}$.
2. Das Teilsegment $S[\ell_k \dots r_k]$ ist das ursprüngliche Teilsegment $S[\ell_k \dots r_k]$, dessen Elemente so permutiert wurden, dass die verbleibenden Umkehrungen noch durchgeführt werden müssen.

Der Induktionsanfang $\ell \ge r$ beendet die Rekursion und stellt sicher, dass die Sequenz $S$ in $S'$ transformiert wurde, wobei $s'_i = s_{n-1-i}$ für alle $i \in \{0, \dots, n-1\}$ gilt.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität $T(n)$ wird durch die Anzahl der rekursiven Aufrufe bestimmt. Jeder Aufruf führt eine Transposition $\tau$ in konstanter Zeit sowie einen Vergleich in konstanter Zeit durch.

Die Rekursionsgleichung für die Anzahl der Operationen lautet:
$$T(n) = T(n-2) + \Theta(1)$$
Mit den Induktionsanfängen $T(0) = \Theta(1)$ und $T(1) = \Theta(1)$.

Durch Auflösen der Rekursion ergibt sich:
$$T(n) = \sum_{i=0}^{\lfloor n/2 \rfloor} \Theta(1) = \Theta\left(\frac{n}{2}\right) = O(n)$$
Somit ist die Zeitkomplexität linear in Bezug auf die Eingabegröße $n$.

### Platzkomplexität
Die Platzkomplexität $S(n)$ wird durch die maximale Tiefe des Rekursions-Stacks bestimmt. Jeder rekursive Aufruf fügt einen neuen Frame zum Call-Stack hinzu, der die lokalen Variablen $(\ell, r)$ und die Rücksprungadresse speichert.

Die Tiefe der Rekursion $D(n)$ ist durch die Anzahl der Schritte definiert, bis der Induktionsanfang $\ell \ge r$ erreicht ist:
$$D(n) = \left\lceil \frac{n}{2} \right\rceil$$

Da jeder Stack-Frame $\Theta(1)$ zusätzlichen Platz verbraucht, beträgt die gesamte zusätzliche Platzkomplexität:
$$S(n) = D(n) \cdot \Theta(1) = \Theta(n)$$

Ohne Tail-Call Optimization (TCO) ist die Platzkomplexität strikt $O(n)$. Falls TCO implementiert wäre, würde der Compiler die Rekursion in einen iterativen Prozess umwandeln, was die zusätzliche Platzkomplexität auf $O(1)$ reduzieren würde. Gemäß den Problemvorgaben und Standard-Ausführungsumgebungen (z. B. CPython) bleibt die Platzkomplexität jedoch $O(n)$.