# Formale mathematische Spezifikation: Reverse Linked List

## 1. Definitionen und Notation

Sei eine einfach verkettete Liste definiert als ein Tupel $L = (V, E, h)$, wobei:
*   $V = \{v_1, v_2, \dots, v_n\}$ eine endliche Menge von Knoten ist.
*   $E \subset V \times V$ eine Menge gerichteter Kanten ist, die die `next`-Pointer repräsentieren. Die Listenstruktur impliziert, dass $E$ einen einfachen Pfad bildet: $v_{i} \to v_{i+1}$ für $1 \le i < n$.
*   $h \in V$ der Kopf (Head) der Liste ist, wobei $h = v_1$.
*   Der Endknoten $v_n$ die Bedingung erfüllt, dass $\nexists u \in V$ existiert, sodass $(v_n, u) \in E$. Wir bezeichnen den terminalen Zustand als $\text{null}$.

Der Zustand des Algorithmus zu einer beliebigen Iteration $k$ ist definiert durch das Tripel $\mathcal{S}_k = (\text{prev}_k, \text{curr}_k, \text{next\_node}_k)$, wobei $\text{prev}_k, \text{curr}_k \in V \cup \{\text{null}\}$.

Das Ziel ist die Definition einer Transformationsfunktion $f: L \to L'$, sodass $L' = (V, E', h')$, wobei:
*   $E' = \{ (v_{i+1}, v_i) \mid 1 \le i < n \}$.
*   $h' = v_n$.

## 2. Algebraische Charakterisierung

Der Algorithmus arbeitet durch die Aufrechterhaltung einer Schleifeninvariante, die die teilweise Umkehrung der Liste sicherstellt. Sei $E_k$ die Menge der Kanten in der Iteration $k$.

**Schleifeninvariante:**
Zu Beginn jeder Iteration $k$ (wobei $k=0$ dem Anfangszustand entspricht) ist die Liste in zwei Segmente unterteilt:
1.  Ein umgekehrtes Segment: $v_k \to v_{k-1} \to \dots \to v_1 \to \text{null}$.
2.  Ein nicht umgekehrtes Segment: $v_{k+1} \to v_{k+2} \to \dots \to v_n \to \text{null}$.

Formal gilt für $0 \le k \le n$:
*   $\text{prev}_k = v_k$ (mit $v_0 = \text{null}$).
*   $\text{curr}_k = v_{k+1}$ (mit $v_{n+1} = \text{null}$).
*   Die Kanten $E_k$ sind definiert als:
    $$E_k = \{ (v_j, v_{j-1}) \mid 2 \le j \le k \} \cup \{ (v_j, v_{j+1}) \mid k+1 \le j < n \}$$

**Zustandsübergang:**
Der Übergang von $\mathcal{S}_k$ zu $\mathcal{S}_{k+1}$ wird durch die folgenden atomaren Aktualisierungen gesteuert:
1.  $\text{next\_node}_{k+1} = \text{curr}_k.\text{next}$
2.  $\text{curr}_k.\text{next} = \text{prev}_k$
3.  $\text{prev}_{k+1} = \text{curr}_k$
4.  $\text{curr}_{k+1} = \text{next\_node}_{k+1}$

Der Algorithmus terminiert, wenn $\text{curr}_k = \text{null}$ ist; zu diesem Zeitpunkt ist $\text{prev}_k = v_n$, was dem neuen Kopf $h'$ entspricht.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus führt einen einzigen Durchlauf der Linked List durch. Sei $T(n)$ die Anzahl der Operationen, die für eine Liste der Länge $n$ erforderlich sind.
Die Schleife wird genau $n$-mal ausgeführt, da $\text{curr}$ von $v_1$ nach $v_n$ und schließlich zu $\text{null}$ übergeht. Innerhalb jeder Iteration sind die Operationen (Pointer-Zuweisung, Variablenaktualisierungen) von konstanter Zeit, $O(1)$.
Die gesamte Zeitkomplexität ergibt sich aus der Summation:
$$T(n) = \sum_{k=1}^{n} c = c \cdot n = O(n)$$
Somit ist der Algorithmus linear in Bezug auf die Anzahl der Knoten $n$.

### Platzkomplexität
Die Platzkomplexität $S(n)$ ist die Summe des vom Algorithmus verwendeten zusätzlichen Speichers.
Der Algorithmus verwaltet eine feste Anzahl von Pointern: $\text{prev}$, $\text{curr}$ und $\text{next\_node}$. Unabhängig von der Eingabegröße $n$ ist der für diese Pointer reservierte Speicher konstant:
$$S(n) = S_{\text{aux}} + S_{\text{input}} = O(1) + O(n)$$
Da wir uns für die zusätzliche Platzkomplexität (den über die Eingabestruktur hinaus benötigten Speicher) interessieren, gilt:
$$S_{\text{aux}} = O(1)$$
Dies erfüllt die Anforderung für eine In-Place-Transformation.