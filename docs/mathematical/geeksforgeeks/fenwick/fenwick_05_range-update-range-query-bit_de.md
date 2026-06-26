# Formale mathematische Spezifikation: Bereichs-Update, Bereichs-Abfrage (Dual BIT)

## 1. Definitionen und Notation

Sei $A = \{a_1, a_2, \dots, a_n\}$ ein Array aus $n$ Elementen, wobei initial $a_i = 0$ für alle $i \in \{1, \dots, n\}$ gilt. Wir definieren den Zustand des Systems durch die Sequenz der auf $A$ angewendeten Updates.

*   **Update-Operation:** Ein Bereichs-Update ist definiert durch das Tupel $(l, r, \delta)$, wobei $1 \le l \le r \le n$ und $\delta \in \mathbb{R}$. Die Operation transformiert $A$ so, dass $a_i \leftarrow a_i + \delta$ für alle $i \in [l, r]$ gilt.
*   **Abfrage-Operation (Query):** Eine Bereichs-Abfrage ist definiert durch das Tupel $(l, r)$ und gibt die Summe $S(l, r) = \sum_{i=l}^r a_i$ zurück.
*   **Differenz-Array:** Sei $D = \{d_1, d_2, \dots, d_n, d_{n+1}\}$ das Differenz-Array, sodass $d_i = a_i - a_{i-1}$ (mit $a_0 = 0$). Folglich gilt $a_i = \sum_{j=1}^i d_j$.
*   **Fenwick Tree (BIT):** Ein BIT ist eine Datenstruktur, die ein Array $B$ repräsentiert und Punkt-Updates sowie Präfixsummen-Abfragen in $O(\log n)$ Zeit unterstützt. Wir bezeichnen $BIT(B, x) = \sum_{j=1}^x B_j$.

## 2. Algebraische Charakterisierung

Um Bereichs-Updates und Bereichs-Abfragen zu unterstützen, drücken wir die Präfixsumme $P(x) = \sum_{i=1}^x a_i$ mithilfe des Differenz-Arrays $D$ aus.

Durch Expansion der Definition von $a_i$:
$$P(x) = \sum_{i=1}^x \sum_{j=1}^i d_j$$

Durch Vertauschen der Summationsreihenfolge (Zählen, wie oft jedes $d_j$ zur Gesamtsumme beiträgt):
$$P(x) = \sum_{j=1}^x d_j \cdot (x - j + 1)$$
$$P(x) = (x + 1) \sum_{j=1}^x d_j - \sum_{j=1}^x (d_j \cdot j)$$

Wir definieren zwei Fenwick Trees, $T_1$ und $T_2$, um die Komponenten dieser Identität zu verwalten:
1. $T_1$ speichert das Differenz-Array $D$, sodass $T_1.query(x) = \sum_{j=1}^x d_j$.
2. $T_2$ speichert das Produkt-Array $D'$, wobei $d'_j = d_j \cdot j$, sodass $T_2.query(x) = \sum_{j=1}^x (d_j \cdot j)$.

**Update-Übergang:**
Für ein Bereichs-Update $(l, r, \delta)$ wird das Differenz-Array $D$ an den Indizes $l$ und $r+1$ modifiziert:
*   $d_l \leftarrow d_l + \delta$
*   $d_{r+1} \leftarrow d_{r+1} - \delta$

Dementsprechend lauten die Updates für $T_1$ und $T_2$:
*   $T_1$: Update Index $l$ um $\delta$ und Index $r+1$ um $-\delta$.
*   $T_2$: Update Index $l$ um $\delta \cdot l$ und Index $r+1$ um $-\delta \cdot (r+1)$.

**Abfrage-Formulierung:**
Die Präfixsumme $P(x)$ wird berechnet als:
$$P(x) = (x + 1) \cdot T_1.query(x) - T_2.query(x)$$
Die Bereichssumme $S(l, r)$ ergibt sich dann aus dem Fundamentalsatz der Summation:
$$S(l, r) = P(r) - P(l-1)$$

## 3. Komplexitätsanalyse

### Zeitkomplexität
Sei $N$ die Anzahl der Elemente und $M$ die Anzahl der Operationen.
*   **Update:** Die `range_update`-Operation führt vier Punkt-Updates über zwei BITs aus. Jedes Punkt-Update in einem BIT der Größe $N$ durchläuft die Höhe des Baumes, welche $\lceil \log_2 N \rceil$ beträgt. Somit liegt die Komplexität bei $O(\log N)$.
*   **Abfrage:** Die `range_query`-Operation führt zwei Präfixsummen-Berechnungen durch, von denen jede zwei BIT-Abfragen beinhaltet. Jede BIT-Abfrage benötigt $O(\log N)$ Zeit. Somit liegt die Komplexität bei $O(\log N)$.
*   **Gesamtzeit:** $O(M \log N)$.

### Platzkomplexität
Der Algorithmus verwaltet zwei Arrays der Größe $N+2$, um die Fenwick Trees $T_1$ und $T_2$ zu repräsentieren.
*   **Gesamtspeicher:** $O(N)$.
Der zusätzliche Speicherbedarf ist minimal, da die Struktur in-place auf den zwei BIT-Arrays operiert. Dies erfüllt die Anforderungen an die Speichereffizienz im Vergleich zu einem Segment Tree, der typischerweise $O(4N)$ Speicher benötigt.