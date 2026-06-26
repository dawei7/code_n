# Formale mathematische Spezifikation: Evaluate Reverse Polish Notation

## 1. Definitionen und Notation

Sei $\Sigma$ die Menge der gültigen Tokens, definiert als $\Sigma = \mathbb{Z} \cup \mathcal{O}$, wobei $\mathbb{Z}$ die Menge der ganzen Zahlen und $\mathcal{O} = \{+, -, *, /\}$ die Menge der binären arithmetischen Operatoren ist.

Ein RPN-Ausdruck wird als eine Sequenz $T = (t_1, t_2, \dots, t_N)$ dargestellt, wobei $t_i \in \Sigma$. Die Auswertung von $T$ ist eine Abbildung $f: \Sigma^N \to \mathbb{Z}$.

Wir definieren den Zustand des Algorithmus in Schritt $k$ (wobei $0 \le k \le N$) as ein Tupel $(\sigma_k, \tau_k)$, wobei:
*   $\sigma_k \in \mathbb{Z}^*$ ein Stack ist, dargestellt als eine endliche Sequenz von ganzen Zahlen. Wir bezeichnen den leeren Stack als $\epsilon$.
*   $\tau_k = (t_{k+1}, \dots, t_N)$ das verbleibende Suffix der Eingabesequenz ist.

Der Divisionsoperator $/$ ist als die in Richtung Null abschneidende Funktion definiert:
$$a / b = \text{sgn}(a/b) \cdot \lfloor |a/b| \rfloor$$
wobei $a, b \in \mathbb{Z}, b \neq 0$.

## 2. Algebraische Charakterisierung

Der Algorithmus definiert eine Zustandsübergangsfunktion $\delta: (\mathbb{Z}^*, \Sigma) \to \mathbb{Z}^*$. Gegeben ein Stack $\sigma$ und ein Token $t$, ist der Übergang wie folgt definiert:

1.  **Wenn $t \in \mathbb{Z}$:**
    $$\delta(\sigma, t) = \sigma \cdot [t]$$
    wobei $\cdot$ die Konkatenation der Sequenz $\sigma$ mit der einelementigen Sequenz $[t]$ bezeichnet.

2.  **Wenn $t \in \mathcal{O}$:**
    Sei $\sigma = (\dots, a, b)$. Dann gilt:
    $$\delta(\sigma, t) = (\dots, a \circ_t b)$$
    wobei $\circ_t$ die binäre Operation ist, die $t \in \{+, -, *, /\}$ entspricht.

**Korrektheitsinvariante:**
Sei $S_k$ der Stack nach der Verarbeitung von $k$ Tokens. Für jeden gültigen RPN-Ausdruck $T$ wahrt der Algorithmus die Invariante, dass der Stack die Teilergebnisse der Traversierung des Ausdrucksbaums enthält. Speziell gilt: Wenn $T$ einen Baum $E$ repräsentiert, dann enthält der Stack $\sigma_N$ nach $N$ Schritten genau ein Element $v \in \mathbb{Z}$, sodass $v = \text{eval}(E)$.

Die Auswertung wird durch die rekursive Struktur des Postfix-Ausdrucks bestimmt:
$$ \text{eval}(T) = \begin{cases} t_1 & \text{if } N=1 \\ \text{eval}(T_{left}) \circ \text{eval}(T_{right}) & \text{if } t_N \in \mathcal{O} \end{cases} $$

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus führt einen einzelnen linearen Scan der Eingabesequenz $T$ durch. Sei $N$ die Anzahl der Tokens.
Für jedes Token $t_i$:
*   Wenn $t_i \in \mathbb{Z}$, ist die Operation ein Stack-`push`, was $O(1)$ ist.
*   Wenn $t_i \in \mathcal{O}$, umfasst die Operation zwei `pop`-Operationen und eine `push`-Operation, jeweils in $O(1)$.

Die gesamte Zeitkomplexität $T(N)$ ist durch die Summation gegeben:
$$T(N) = \sum_{i=1}^{N} c_i$$
wobei $c_i$ der konstante Zeitaufwand der $i$-ten Operation ist. Da $c_i = \Theta(1)$ für alle $i$ gilt, erhalten wir:
$$T(N) = \Theta(N)$$

### Platzkomplexität
Die Platzkomplexität wird durch die maximale Tiefe des Stacks $\sigma$ bestimmt. 
Sei $n_i$ die Anzahl der Operanden und $o_i$ die Anzahl der Operatoren, die bis zu Schritt $i$ angetroffen wurden. Die Stack-Größe $|\sigma_i|$ ist gegeben durch:
$$|\sigma_i| = n_i - o_i$$
Im schlechtesten Fall, in dem alle Operanden vor allen Operatoren erscheinen (z. B. $T = (z_1, z_2, \dots, z_{N/2}, o_1, o_2, \dots, o_{N/2})$), wächst der Stack auf die Größe $N/2$ an. 

Da der für den Stack benötigte Hilfsspeicher proportional zur Anzahl der gepushten Elemente ist, beträgt die Platzkomplexität:
$$S(N) = O(N)$$
Dies ist optimal, da der Stack Zwischenoperanden speichern muss, um die Postfix-Auswertungsreihenfolge einzuhalten.