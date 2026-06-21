# Formale mathematische Spezifikation: Strassen-Matrixmultiplikation

## 1. Definitionen und Notation

Sei $\mathcal{R}$ ein Ring (üblicherweise der Körper der reellen Zahlen $\mathbb{R}$ oder der komplexen Zahlen $\mathbb{C}$). Wir definieren die Menge der quadratischen Matrizen der Ordnung $n$ über $\mathcal{R}$ als $\mathcal{M}_n(\mathcal{R})$.

Gegeben seien zwei Matrizen $A, B \in \mathcal{M}_n(\mathcal{R})$, wobei $n = 2^k$ für ein $k \in \mathbb{N}$ gilt. Wir definieren die Blockzerlegung von $A$ und $B$ als:
$$A = \begin{pmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{pmatrix}, \quad B = \begin{pmatrix} B_{11} & B_{12} \\ B_{21} & B_{22} \end{pmatrix}$$
wobei $A_{ij}, B_{ij} \in \mathcal{M}_{n/2}(\mathcal{R})$. Das Ziel ist die Berechnung des Produkts $C = A \cdot B \in \mathcal{M}_n(\mathcal{R})$, wobei $C$ in Quadranten $C_{ij} \in \mathcal{M}_{n/2}(\mathcal{R})$ unterteilt ist.

## 2. Algebraische Charakterisierung

Die Standarddefinition der Matrixmultiplikation erfordert $C_{ij} = \sum_{k=1}^2 A_{ik} B_{kj}$. Der Strassen-Algorithmus ersetzt die acht Standardmultiplikationen durch sieben Zwischenprodukte $M_1, \dots, M_7 \in \mathcal{M}_{n/2}(\mathcal{R})$, die wie folgt definiert sind:

$$
\begin{aligned}
M_1 &= (A_{11} + A_{22})(B_{11} + B_{22}) \\
M_2 &= (A_{21} + A_{22})B_{11} \\
M_3 &= A_{11}(B_{12} - B_{22}) \\
M_4 &= A_{22}(B_{21} - B_{11}) \\
M_5 &= (A_{11} + A_{12})B_{22} \\
M_6 &= (A_{21} - A_{11})(B_{11} + B_{12}) \\
M_7 &= (A_{12} - A_{22})(B_{21} + B_{22})
\end{aligned}
$$

Die Quadranten der resultierenden Matrix $C$ werden anschließend durch Linearkombinationen dieser Produkte rekonstruiert:

$$
\begin{aligned}
C_{11} &= M_1 + M_4 - M_5 + M_7 \\
C_{12} &= M_3 + M_5 \\
C_{21} &= M_2 + M_4 \\
C_{22} &= M_1 - M_2 + M_3 + M_6
\end{aligned}
$$

**Korrektheit:** Die Gültigkeit dieser Konstruktion beruht auf dem Distributivgesetz des Rings $\mathcal{R}$. Zum Beispiel ergibt die Expansion von $C_{12}$:
$$C_{12} = A_{11}(B_{12} - B_{22}) + (A_{11} + A_{12})B_{22} = A_{11}B_{12} - A_{11}B_{22} + A_{11}B_{22} + A_{12}B_{22} = A_{11}B_{12} + A_{12}B_{22}$$
Dies entspricht der Standarddefinition des Blockmatrixprodukts.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus folgt einem Divide-and-Conquer-Paradigma. Sei $T(n)$ die Anzahl der arithmetischen Operationen, die zur Multiplikation zweier $n \times n$-Matrizen erforderlich sind.

1. **Divide:** Die Partitionierung der Matrizen benötigt $O(1)$ Zeit (oder $O(n^2)$, falls Kopieren erforderlich ist).
2. **Conquer:** Der Algorithmus führt 7 rekursive Multiplikationen der Größe $n/2$ durch.
3. **Combine:** Die Additionen und Subtraktionen der $n/2 \times n/2$-Matrizen erfordern $O(n^2)$ Operationen.

Dies ergibt die Rekursionsgleichung:
$$T(n) = 7T(n/2) + \Theta(n^2)$$

Unter Anwendung des **Master-Theorems** für Rekursionen der Form $T(n) = aT(n/b) + f(n)$, wobei $a=7, b=2, f(n)=n^2$:
Da $\log_b(a) = \log_2(7) \approx 2.807$ und $f(n) = O(n^{\log_2(7) - \epsilon})$ für $\epsilon \approx 0.807$ gilt, wird die Komplexität von den rekursiven Aufrufen dominiert:
$$T(n) = \Theta(n^{\log_2 7}) \approx O(n^{2.807})$$

### Platzkomplexität
Sei $S(n)$ der benötigte zusätzliche Speicherplatz. Auf jeder Rekursionsebene müssen die Zwischenmatrizen $M_1, \dots, M_7$ sowie die Summen/Differenzen der Teilmatrizen gespeichert werden.

Die Rekursion für den Speicherplatz lautet $S(n) = S(n/2) + O(n^2)$. Durch Summierung der geometrischen Reihe ergibt sich:
$$S(n) = \sum_{i=0}^{\log_2 n} O\left(\left(\frac{n}{2^i}\right)^2\right) = O(n^2) \sum_{i=0}^{\log_2 n} \left(\frac{1}{4}\right)^i = O(n^2)$$
Somit beträgt die gesamte zusätzliche Platzkomplexität $O(n^2)$, da der Speicherbedarf auf der obersten Rekursionsebene die Summe des Speicherbedarfs aller nachfolgenden Ebenen dominiert.