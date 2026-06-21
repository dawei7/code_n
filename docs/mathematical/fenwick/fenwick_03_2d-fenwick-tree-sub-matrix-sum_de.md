# Formale mathematische Spezifikation: 2D Fenwick Tree (Sub-Matrix-Summe)

## 1. Definitionen und Notation

Sei $A$ eine Matrix der Dimensionen $N \times M$ über einem Körper $\mathbb{F}$ (üblicherweise $\mathbb{R}$ oder $\mathbb{Z}$), wobei $A_{i,j}$ das Element in Zeile $i$ und Spalte $j$ für $1 \le i \le N$ und $1 \le j \le M$ bezeichnet.

Wir definieren den **2D Fenwick Tree** (oder Binary Indexed Tree) als eine Datenstruktur, die durch eine Matrix $T$ der Dimensionen $(N+1) \times (M+1)$ repräsentiert wird, wobei $T_{i,j} \in \mathbb{F}$. Die Struktur wird durch die Funktion $L(k) = k \& -k$ gesteuert, welche den Wert des niederwertigsten Bits (Least Significant Bit) von $k$ zurückgibt.

- **Point Update:** Eine Operation $\text{update}(r, c, \delta)$ modifiziert $A_{r,c} \leftarrow A_{r,c} + \delta$ und propagiert die Änderung in $T$.
- **Prefix Sum:** Eine Funktion $S(r, c) = \sum_{i=1}^r \sum_{j=1}^c A_{i,j}$, die die Summe des rechteckigen Bereichs $[1, r] \times [1, c]$ darstellt.
- **Range Query:** Eine Funktion $Q(r_1, c_1, r_2, c_2)$, die die Summe der Sub-Matrix zurückgibt, welche durch die obere linke Ecke $(r_1, c_1)$ und die untere rechte Ecke $(r_2, c_2)$ definiert ist.

## 2. Algebraische Charakterisierung

Der 2D Fenwick Tree $T$ speichert partielle Summen, sodass jeder Eintrag $T_{i,j}$ die Summe eines Sub-Rechtecks von $A$ mit den Dimensionen $L(i) \times L(j)$ enthält. Spezifisch gilt:
$$T_{i,j} = \sum_{x=i-L(i)+1}^{i} \sum_{y=j-L(j)+1}^{j} A_{x,y}$$

### Prefix-Sum-Invariante
Die Prefix-Summe $S(r, c)$ wird durch Aggregation nicht überlappender Sub-Rechtecke berechnet, die in $T$ gespeichert sind:
$$S(r, c) = \sum_{i \in \text{path}(r)} \sum_{j \in \text{path}(c)} T_{i,j}$$
wobei der Pfad durch die Sequenz $p_0 = k, p_{m+1} = p_m - L(p_m)$ bis $p_m = 0$ definiert ist.

### Range Query mittels Inklusions-Exklusions-Prinzip
Die Summe der Sub-Matrix $A[r_1 \dots r_2][c_1 \dots c_2]$ wird aus dem Inklusions-Exklusions-Prinzip abgeleitet:
$$Q(r_1, c_1, r_2, c_2) = S(r_2, c_2) - S(r_1-1, c_2) - S(r_2, c_1-1) + S(r_1-1, c_1-1)$$

### Update-Übergang
Für ein Update $\delta$ an der Position $(r, c)$ erhält die Struktur die Invariante aufrecht, indem alle $T_{i,j}$ aktualisiert werden, deren abgedeckter Bereich $(r, c)$ enthält:
$$T_{i,j} \leftarrow T_{i,j} + \delta, \quad \text{für } i \in \{r, r+L(r), \dots \le N\}, j \in \{c, c+L(c), \dots \le M\}$$

## 3. Komplexitätsanalyse

### Zeitkomplexität
- **Update-Operation:** Das Update durchläuft die Indizes $i$ und $j$ durch Addition des niederwertigsten Bits. Die Anzahl der Iterationen für eine einzelne Dimension $N$ ist durch die Anzahl der gesetzten Bits begrenzt, was $\lfloor \log_2 N \rfloor + 1$ entspricht. Aufgrund der verschachtelten Struktur ergibt sich die Gesamtzahl der Operationen zu:
  $$T_{\text{update}} = O(\log N \cdot \log M)$$
- **Query-Operation:** Analog dazu durchläuft die Prefix-Summe $S(r, c)$ die Indizes durch Subtraktion des niederwertigsten Bits. Die Anzahl der Schritte ist durch die Bit-Länge der Indizes begrenzt:
  $$T_{\text{query}} = O(\log N \cdot \log M)$$
- **Range Query:** Da eine Range Query aus vier Aufrufen der Prefix-Summen-Funktion mit konstanter Zeit besteht, bleibt die Komplexität bei $O(\log N \cdot \log M)$.

### Platzkomplexität
Die Struktur erfordert ein 2D-Array $T$ der Größe $(N+1) \times (M+1)$ zur Speicherung der partiellen Summen.
- **Gesamter Speicherplatz:** $S(N, M) = (N+1)(M+1) \in \Theta(NM)$.
- **Zusätzlicher Speicherplatz:** Der Algorithmus arbeitet in-place auf der Struktur $T$ und benötigt $O(1)$ zusätzlichen Speicherplatz über die Speicherung des Baums selbst hinaus.