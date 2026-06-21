# Formale Mathematische Spezifikation: Segment Tree Aufbau

## 1. Definitionen und Notation

Sei $A = [a_0, a_1, \dots, a_{n-1}]$ eine Eingabesequenz von Elementen aus einer Menge $\mathcal{X}$, ausgestattet mit einer assoziativen binären Operation $\oplus: \mathcal{X} \times \mathcal{X} \to \mathcal{X}$.

Ein **Segment Tree** ist ein gewurzelter binärer Baum $\mathcal{T} = (V, E)$, der eine hierarchische Zerlegung der Indexmenge $I = \{0, 1, \dots, n-1\}$ darstellt.
- Jeder Knoten $v \in V$ ist einem Unterintervall $[l_v, r_v] \subseteq I$ zugeordnet.
- Der Wurzelknoten $v_{root}$ ist $[0, n-1]$ zugeordnet.
- Für jeden internen Knoten $v$ mit Intervall $[l_v, r_v]$, sei $m = \lfloor \frac{l_v + r_v}{2} \rfloor$. Das linke Kind $v_L$ ist $[l_v, m]$ zugeordnet und das rechte Kind $v_R$ ist $[m+1, r_v]$ zugeordnet.
- Blattknoten sind Knoten, bei denen $l_v = r_v$ gilt.

Wir bilden $\mathcal{T}$ auf einen Array $T$ der Größe $M = 4n$ ab, unter Verwendung der Indexierungsfunktion $idx: V \to \{1, \dots, M\}$:
- $idx(v_{root}) = 1$.
- $idx(v_L) = 2 \cdot idx(v)$ und $idx(v_R) = 2 \cdot idx(v) + 1$.

Der Zustandsraum $\mathcal{S}$ des Baumes ist durch die Abbildung $f: V \to \mathcal{X}$ definiert, wobei $f(v)$ das Ergebnis der Bereichsabfrage über $[l_v, r_v]$ speichert.

## 2. Algebraische Charakterisierung

Der Aufbau des Baumes wird durch die folgende Rekursionsgleichung für die in den Knoten gespeicherten Werte bestimmt:

$$
f(v) = 
\begin{cases} 
a_{l_v} & \text{if } l_v = r_v \text{ (Basisfall)} \\
f(v_L) \oplus f(v_R) & \text{if } l_v < r_v \text{ (Rekursiver Schritt)}
\end{cases}
$$

**Korrektheitsinvariante:**
Für jeden Knoten $v$, der das Intervall $[l_v, r_v]$ abdeckt, erfüllt der Wert $f(v)$:
$$f(v) = \bigoplus_{i=l_v}^{r_v} a_i$$
Da $\oplus$ assoziativ ist, ist die Reihenfolge der Auswertung im Post-Order-Traversal garantiert, das korrekte Ergebnis für jeden Bereich $[l, r] \subseteq [0, n-1]$ zu liefern.

**Strukturinvariante:**
Der Baum ist eine vollständige binäre Baumstruktur, die in einem Array eingebettet ist. Für eine Eingabegröße von $n$ ist die Anzahl der Blattknoten $n$, und die Gesamtzahl der Knoten $|V| = 2n - 1$. Die Array-Größe $4n$ wird so gewählt, dass für jedes $n \ge 1$ gilt: $4n \ge 2^{\lceil \log_2 n \rceil + 1} - 1$, wodurch sichergestellt wird, dass während der Abbildung $idx(v)$ kein Index-Out-of-Bounds-Fehler auftritt.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus verwendet eine Post-Order-Traversal des Baumes. Sei $T(n)$ die Zeitkomplexität für den Aufbau eines Segment Tree für einen Array der Größe $n$. Die Rekursionsgleichung ist:
$$T(n) = T\left(\left\lfloor \frac{n}{2} \right\rfloor\right) + T\left(\left\lceil \frac{n}{2} \right\rceil\right) + O(1)$$
Nach dem Master-Theorem (oder der Rekursionsbaum-Methode), da die an jedem Knoten geleistete Arbeit konstant $O(1)$ ist und die Anzahl der Knoten $2n-1$ beträgt, ist die gesamte Zeitkomplexität:
$$T(n) = \sum_{v \in V} O(1) = O(2n - 1) = O(n)$$
Somit ist der Aufbauprozess linear bezüglich der Eingabegröße $n$.

### Platzkomplexität
Die Platzkomplexität wird durch den Speicherbedarf für den Array $T$ bestimmt.
- **Hilfsspeicher:** Die Rekursionsstacktiefe beträgt $O(\log n)$, was der Höhe des balancierten binären Baumes entspricht.
- **Gesamtspeicher:** Der Algorithmus allokiert einen Array der Größe $4n$. Da $4n$ ein konstantes Vielfaches von $n$ ist, beträgt die gesamte Platzkomplexität:
$$S(n) = O(n) + O(\log n) = O(n)$$
Der $O(n)$ Platzbedarf ist optimal für eine statische Repräsentation der Segment Tree Struktur.