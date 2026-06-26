# Formale mathematische Spezifikation: Bereichsaktualisierung, Punktabfrage (BIT)

## 1. Definitionen und Notation

Sei $A = [a_0, a_1, \dots, a_{n-1}]$ ein Array aus $n$ Elementen, wobei initial $a_i = 0$ für alle $i \in \{0, \dots, n-1\}$ gilt. Wir definieren das **Differenzen-Array** $D = [d_0, d_1, \dots, d_{n-1}]$ wie folgt:
$$d_i = a_i - a_{i-1} \quad \text{für } i > 0, \quad \text{und } d_0 = a_0$$
Durch den Fundamentalsatz der Analysis für diskrete Folgen (die Eigenschaft der Teleskopsumme) kann jedes Element $a_k$ aus der Präfixsumme von $D$ rekonstruiert werden:
$$a_k = \sum_{i=0}^{k} d_i$$

Der Fenwick Tree (Binary Indexed Tree) ist eine Datenstruktur $\mathcal{B}$, die ein Array $B$ der Größe $n+1$ verwaltet, um Teilsummen von $D$ zu speichern. Die Abbildung zwischen dem Index $i$ (0-basiert) und dem BIT-Index $j$ (1-basiert) ist gegeben durch $j = i + 1$. Der BIT unterstützt zwei primäre Operationen:
1. $\text{update}(i, \delta)$: Modifiziert $d_i$ durch Addition von $\delta$, was sich auf alle $B_j$ auswirkt, die den Index $i$ abdecken.
2. $\text{query}(k)$: Berechnet die Präfixsumme $\sum_{i=0}^{k} d_i$.

## 2. Algebraische Charakterisierung

### Bereichsaktualisierung (Range Update)
Eine Bereichsaktualisierungsoperation $\text{range\_update}(L, R, \Delta)$ modifiziert das logische Array $A$ so, dass $a_i \leftarrow a_i + \Delta$ für alle $i \in [L, R]$ gilt. In Bezug auf das Differenzen-Array $D$ lautet diese Transformation:
$$d_L' = d_L + \Delta$$
$$d_{R+1}' = d_{R+1} - \Delta$$
Für alle $k \notin \{L, R+1\}$ gilt $d_k' = d_k$. 

Die Korrektheit folgt aus der Eigenschaft der Präfixsumme:
- Für $k < L$: $\sum_{i=0}^k d_i' = \sum_{i=0}^k d_i = a_k$ (Unverändert).
- Für $L \le k \le R$: $\sum_{i=0}^k d_i' = (\sum_{i=0}^k d_i) + \Delta = a_k + \Delta$.
- Für $k > R$: $\sum_{i=0}^k d_i' = (\sum_{i=0}^k d_i) + \Delta - \Delta = a_k$ (Unverändert).

### Punktabfrage (Point Query)
Die Punktabfrage $\text{point\_query}(k)$ ist definiert als die Auswertung der Präfixsumme des Differenzen-Arrays:
$$\text{point\_query}(k) = \sum_{j=1}^{k+1} B_j$$
wobei $B_j$ die Summe eines spezifischen Bereichs von $D$ speichert, der durch das am wenigsten signifikante Bit (LSB) von $j$ bestimmt wird, bezeichnet als $\text{lsb}(j) = j \& -j$. Spezifisch gilt $B_j = \sum_{i=j-\text{lsb}(j)+1}^{j} d_{i-1}$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Sei $N$ die Anzahl der Elemente.
- **Update:** Die `update`-Operation durchläuft den BIT, indem $\text{lsb}(j)$ zum Index $j$ addiert wird. Da $j \le N+1$, ist die Anzahl der Iterationen durch die Anzahl der Bits in $N$ begrenzt, was $\lfloor \log_2 N \rfloor + 1$ entspricht. Somit ist jedes `update` in $O(\log N)$. Eine `range_update` führt exakt zwei `update`-Aufrufe aus, was $O(2 \log N) = O(\log N)$ beibehält.
- **Query:** Die `query`-Operation durchläuft den BIT, indem $\text{lsb}(j)$ von $j$ subtrahiert wird. Analog besucht dies höchstens $\lfloor \log_2 N \rfloor + 1$ Knoten. Somit ist `point_query` in $O(\log N)$.

Die gesamte Zeitkomplexität für $M$ Operationen beträgt $O(M \log N)$.

### Platzkomplexität
Der Algorithmus benötigt ein zusätzliches Array $B$ der Größe $N+1$, um die BIT-Struktur zu speichern.
- **Zusätzlicher Speicher:** $O(N)$ zur Speicherung der BIT-Knoten.
- **Gesamtspeicher:** $O(N)$, da das Eingabe-Array $A$ implizit durch das im BIT gespeicherte Differenzen-Array repräsentiert wird. Es sind keine zusätzlichen Datenstrukturen erforderlich, die proportional zur Anzahl der Operationen wachsen.