# Formale mathematische Spezifikation: Find Middle of Linked List

## 1. Definitionen und Notation

Sei $L$ eine einfach verkettete Linked List, definiert als Tupel $(V, E, h)$, wobei:
*   $V = \{v_0, v_1, \dots, v_{n-1}\}$ die Menge der $n$ Knoten in der Liste ist.
*   $E \subset V \times V$ die Menge der gerichteten Kanten ist, sodass $(v_i, v_{i+1}) \in E$ für alle $0 \le i < n-1$ gilt, was den `next` Pointer repräsentiert.
*   $h \in V$ der Head-Knoten $v_0$ ist.
*   Die Länge der Liste $|V| = n$ beträgt.

Wir definieren eine Nachfolgerfunktion $f: V \to V \cup \{\text{null}\}$, sodass $f(v_i) = v_{i+1}$ für $i < n-1$ und $f(v_{n-1}) = \text{null}$ gilt. Wir definieren die $k$-te Iteration der Nachfolgerfunktion als $f^k(v)$, wobei $f^0(v) = v$ und $f^k(v) = f(f^{k-1}(v))$ ist.

Das Ziel ist es, den Knoten $v_m$ zu finden, für den gilt:
$$m = \left\lfloor \frac{n}{2} \right\rfloor$$
wobei der Index $m$ bei Listen mit gerader Länge dem zweiten mittleren Knoten entspricht.

## 2. Algebraische Charakterisierung

Der Algorithmus verwendet zwei Pointer, $s$ (slow) und $f$ (fast), die Elemente in $V$ repräsentieren. Seien $s_k$ und $f_k$ die Positionen der Pointer nach $k$ Iterationen.

**Initialisierung:**
$s_0 = h$
$f_0 = h$

**Zustandsübergänge:**
Für jede Iteration $k \ge 0$:
$$s_{k+1} = f(s_k)$$
$$f_{k+1} = f(f(f_k))$$

**Abbruchbedingung:**
Der Algorithmus terminiert bei der kleinsten ganzen Zahl $k$, für die $f_k = \text{null}$ oder $f(f_k) = \text{null}$ gilt.

**Korrektheitsinvariante:**
In jeder Iteration $k$ ist die Position des slow Pointers $s_k = f^k(h)$ und die des fast Pointers $f_k = f^{2k}(h)$. 
Die Schleife terminiert, wenn $2k \ge n-1$. Speziell gilt:
1. Wenn $n$ ungerade ist, $n = 2m + 1$. Die Schleife terminiert, wenn $2k = 2m$, d. h. $k = m$. Somit ist $s_m = f^m(h)$, was dem Knoten am Index $m = \lfloor n/2 \rfloor$ entspricht.
2. Wenn $n$ gerade ist, $n = 2m$. Die Schleife terminiert, wenn $2k = n-2$ (falls $f(f_k) = \text{null}$), was $k = m-1$ bedeutet. Die Bedingung $f(f_k) = \text{null}$ impliziert jedoch, dass $f_k$ der vorletzte Knoten ist. Der nächste Schritt $s_{k+1}$ bewegt den slow Pointer auf $f^m(h)$, was dem Knoten am Index $m = n/2$ entspricht.

Somit identifiziert der Algorithmus korrekt $v_{\lfloor n/2 \rfloor}$ für alle $n \in \mathbb{N}$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität wird durch die Anzahl der Iterationen $k$ bestimmt, die erforderlich sind, um die Abbruchbedingung zu erreichen. 
Wie festgestellt, terminiert die Schleife, wenn $f_k$ das Ende der Liste erreicht. Da $f_k = f^{2k}(h)$, terminiert die Schleife, wenn $2k \approx n$. 
Die Gesamtzahl der Operationen $T(n)$ ist proportional zur Anzahl der Schritte, die der fast Pointer ausführt:
$$T(n) = \sum_{k=0}^{\lfloor n/2 \rfloor} c = c \cdot \left( \frac{n}{2} + 1 \right)$$
wobei $c$ die konstante Zeit für Pointer-Aktualisierungen ist.
Daher gilt $T(n) \in \Theta(n)$.

### Platzkomplexität
Der Algorithmus verwaltet unabhängig von der Eingabegröße $n$ genau zwei Pointer, $s$ und $f$. 
Sei $S(n)$ die zusätzliche Platzkomplexität:
$$S(n) = \text{size}(s) + \text{size}(f) = O(1) + O(1) = O(1)$$
Da keine zusätzlichen Datenstrukturen (wie Arrays oder Rekursions-Stacks) verwendet werden, die mit $n$ skalieren, ist die Platzkomplexität strikt $O(1)$.