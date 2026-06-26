# Formale mathematische Spezifikation: Aufbau eines Fenwick Tree (Binary Indexed Tree)

## 1. Definitionen und Notation

Sei $A = (a_1, a_2, \dots, a_N)$ eine Sequenz von $N$ Elementen über einer kommutativen Gruppe $(G, +)$. Im Kontext dieses Algorithmus gilt $G = \mathbb{Z}$ oder $\mathbb{R}$.

Wir definieren den **Fenwick Tree** (oder Binary Indexed Tree) als eine Sequenz $B = (b_0, b_1, \dots, b_N)$, wobei $b_0$ ein Dummy-Element (üblicherweise $0$) ist und $b_i$ für $i \in \{1, \dots, N\}$ als die Summe eines spezifischen Bereichs von $A$ definiert ist:
$$b_i = \sum_{j=i - \text{lsb}(i) + 1}^{i} a_j$$
wobei $\text{lsb}(i)$ den Wert des niedrigstwertigen Bits (least significant bit) von $i$ bezeichnet, definiert als:
$$\text{lsb}(i) = i \& (-i) = 2^k$$
wobei $k$ die größte ganze Zahl ist, sodass $2^k$ ein Teiler von $i$ ist.

Der Zustandsraum $\mathcal{S}$ des Algorithmus ist die Menge aller möglichen Arrays $B \in G^{N+1}$. Die Transformation $f: G^N \to \mathcal{S}$ bildet das Eingabe-Array $A$ auf die Fenwick-Repräsentation $B$ ab.

## 2. Algebraische Charakterisierung

Die Konstruktion des Fenwick Tree beruht auf der Eigenschaft, dass jeder Index $i$ für einen Bereich der Länge $\text{lsb}(i)$ verantwortlich ist. Um eine Konstruktion in $O(N)$ zu erreichen, nutzen wir die im BIT inhärente Baumstruktur.

Sei $parent(i) = i + \text{lsb}(i)$. Die Indizes bilden einen Wald (oder einen Baum, wenn wir eine virtuelle Wurzel bei $N+1$ betrachten), wobei $i$ ein Kind von $parent(i)$ ist, sofern $parent(i) \leq N$.

**Initialisierung:**
Wir initialisieren $b_i = a_i$ für alle $i \in \{1, \dots, N\}$. Dies stellt den Induktionsanfang dar, bei dem jeder Knoten seinen eigenen Wert enthält.

**Propagationsinvariante:**
Nach der Initialisierung führen wir einen einzelnen Durchlauf $i = 1, \dots, N$ aus. Die Korrektheit der Konstruktion wird durch die folgende Rekursionsgleichung bestimmt:
$$b_{parent(i)} \leftarrow b_{parent(i)} + b_i, \quad \forall i \in \{1, \dots, N\} \text{ s.t. } parent(i) \leq N$$

Diese Operation stellt sicher, dass der Wert an $b_j$ die Summen aller seiner direkten Kinder in der BIT-Struktur akkumuliert. Da die BIT-Struktur ein gerichteter azyklischer Graph ist (speziell ein Baum, bei dem Kanten durch $i \to i + \text{lsb}(i)$ definiert sind), garantiert die Verarbeitung der Indizes in aufsteigender Reihenfolge, dass beim Erreichen des Index $j$ alle seine Kinder $i$ (für die $parent(i) = j$ gilt) bereits vollständig verarbeitet wurden und ihre Werte an $b_j$ propagiert wurden.

Somit ist der finale Wert von $b_j$:
$$b_j = a_j + \sum_{i \in \text{children}(j)} b_i$$
Durch vollständige Induktion erfüllt dies die Definition $b_j = \sum_{k=j-\text{lsb}(j)+1}^{j} a_k$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus besteht aus zwei unterschiedlichen Phasen:
1. **Initialisierung:** Ein linearer Scan, um $N$ Elemente in das Array $B$ zu kopieren. Dies erfordert $\Theta(N)$ Operationen.
2. **Propagation:** Eine Schleife von $i = 1$ bis $N$. Innerhalb der Schleife werden die bitweise Operation $\text{lsb}(i)$ und die Addition $b_{parent(i)} += b_i$ in $O(1)$ Zeit ausgeführt.

Die gesamte Zeitkomplexität $T(N)$ ergibt sich zu:
$$T(N) = \sum_{i=1}^{N} \Theta(1) = \Theta(N)$$
Da jeder Index $i$ genau einmal besucht wird und zu höchstens einem Elternknoten beiträgt, ist der Aufwand strikt linear. Somit gilt $T(N) \in O(N)$.

### Platzkomplexität
Der Algorithmus benötigt ein zusätzliches Array $B$ der Größe $N+1$, um den Fenwick Tree zu speichern.
- **Zusätzlicher Speicherplatz:** $O(1)$ (exklusive des Ausgabe-Arrays).
- **Gesamter Speicherplatz:** $O(N)$, um die BIT-Struktur zu speichern.

Da die Ausgabe die Größe $N+1$ haben muss, ist die Platzkomplexität mit $\Theta(N)$ optimal.