# Formale mathematische Spezifikation: Reverse Bits

## 1. Definitionen und Notation

Sei $\mathbb{Z}_{2^k}$ der Ring der ganzen Zahlen modulo $2^k$. In dieser Spezifikation definieren wir die Bitbreite $W = 32$. Der Eingaberaum ist die Menge der vorzeichenlosen 32-Bit-Ganzzahlen, dargestellt als die Menge $\mathcal{N} = \{n \in \mathbb{Z} \mid 0 \le n < 2^W\}$.

Jedes $n \in \mathcal{N}$ kann eindeutig in seiner binären Stellenwertschreibweise als Vektor von Bits $b = (b_{W-1}, b_{W-2}, \dots, b_1, b_0)$ dargestellt werden, wobei $b_i \in \{0, 1\}$ gilt, sodass:
$$n = \sum_{i=0}^{W-1} b_i 2^i$$

Das Ziel ist die Definition einer Funktion $f: \mathcal{N} \to \mathcal{N}$, sodass die Ausgabe $n' = f(n)$ die folgende Bedingung erfüllt:
$$n' = \sum_{i=0}^{W-1} b_i 2^{W-1-i}$$

## 2. Algebraische Charakterisierung

### 2.1 Iterative Formulierung
Der Algorithmus konstruiert $n'$, indem er über die Bitpositionen von $n$ iteriert. Sei $n^{(k)}$ der Wert der Eingabe nach $k$ Rechtsschiebeoperationen (Right-Shifts) und $r^{(k)}$ der Wert des Ergebnisses nach $k$ Iterationen.

Die Zustandsübergänge für $k \in \{0, 1, \dots, W-1\}$ sind durch die folgende Rekurrenz definiert:
1. **Extraktion:** $b_k = \lfloor n^{(k)} / 2^0 \rfloor \pmod 2$
2. **Verschieben und Akkumulieren:** $r^{(k+1)} = (r^{(k)} \cdot 2) + b_k$
3. **Eingabereduktion:** $n^{(k+1)} = \lfloor n^{(k)} / 2 \rfloor$

Induktionsanfang: $n^{(0)} = n$ und $r^{(0)} = 0$. Das Endergebnis ist $r^{(W)}$.

### 2.2 Invariante
Zu Beginn jeder Iteration $k$ (wobei $0 \le k \le W$) gilt die folgende Schleifeninvariante:
$$r^{(k)} = \sum_{j=0}^{k-1} b_j 2^{k-1-j}$$
Dies bestätigt, dass nach $W$ Iterationen $r^{(W)} = \sum_{j=0}^{W-1} b_j 2^{W-1-j}$ gilt, was der bitweise umgekehrten Darstellung von $n$ entspricht.

### 2.3 Divide-and-Conquer-Formulierung (Bit-Masking)
Alternativ kann die Transformation als Komposition von bitweisen Permutationen ausgedrückt werden. Sei $M_s$ eine Maske der Länge $W$, die aus abwechselnden Blöcken von $s$ Einsen und $s$ Nullen besteht. Die Umkehrung ist die Komposition von $m = \log_2 W$ Operationen:
$$n_{i+1} = \left( (n_i \& M_{2^{m-1-i}}) \gg 2^{m-1-i} \right) \lor \left( (n_i \& \overline{M_{2^{m-1-i}}}) \ll 2^{m-1-i} \right)$$
wobei $n_0 = n$ und $n_m = f(n)$ gilt.

## 3. Komplexitätsanalyse

### 3.1 Zeitkomplexität
Der iterative Ansatz führt eine feste Anzahl von Operationen $W = 32$ aus. Jede Iteration $k$ beinhaltet eine konstante Anzahl bitweiser Operationen (AND, OR, LSHIFT, RSHIFT), von denen jede auf einer standardmäßigen wortadressierbaren Maschine $O(1)$ benötigt.

Die Gesamtlaufzeit $T(W)$ ergibt sich zu:
$$T(W) = \sum_{k=0}^{W-1} c = c \cdot W$$
Da $W$ eine Konstante ist ($W=32$), gilt $T(W) = O(1)$.

In der Divide-and-Conquer-Variante beträgt die Anzahl der Operationen $T(W) = \sum_{i=0}^{\log_2 W - 1} c = c \log_2 W$. Mit $W=32$ ergibt sich $\log_2 32 = 5$, was ebenfalls $O(1)$ entspricht.

### 3.2 Platzkomplexität
Der Algorithmus verwaltet eine konstante Anzahl an Hilfsvariablen ($n, r, i$), unabhängig vom Eingabewert. Der Speicherbedarf ist unabhängig von der Eingabegröße $n$ und der Bitbreite $W$ (unter der Annahme, dass $W$ fest ist).

Sei $S(W)$ der zusätzliche Speicherplatz:
$$S(W) = \Theta(1)$$
Somit arbeitet der Algorithmus mit einer Platzkomplexität von $O(1)$.