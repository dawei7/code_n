# Formale mathematische Spezifikation: Matrix-Kettenmultiplikation (Top-Down-Memoization)

## 1. Definitionen und Notation

Sei $\mathcal{A} = \{A_1, A_2, \dots, A_n\}$ eine Sequenz von $n$ Matrizen. Jede Matrix $A_i$ hat die Dimensionen $d_{i-1} \times d_i$, wobei die Sequenz der Dimensionen durch einen Vektor $p \in \mathbb{Z}_{>0}^{n+1}$ gegeben ist, sodass $A_i \in \mathbb{R}^{p_{i-1} \times p_i}$ gilt.

Das Ziel ist es, die minimale Anzahl an skalaren Multiplikationen zu finden, die erforderlich sind, um das Produkt $A_1 A_2 \dots A_n$ zu berechnen. Da die Matrixmultiplikation assoziativ ist, ist das Produkt wohldefiniert, aber die Rechenkosten hängen von der Klammerung ab.

- **Zustandsraum:** Sei $\mathcal{S} = \{ (i, j) \in \mathbb{Z}^2 \mid 1 \le i \le j \le n \}$ die Menge aller möglichen Teilketten von Matrizen.
- **Kostenfunktion:** Sei $m(i, j)$ die minimale Anzahl an skalaren Multiplikationen, die erforderlich sind, um das Produkt $A_{i \dots j} = A_i A_{i+1} \dots A_j$ zu berechnen.
- **Memoization-Tabelle:** Wir definieren eine Tabelle $M \in \mathbb{Z}^{n \times n}$, in der $M_{i,j}$ den berechneten Wert von $m(i, j)$ speichert.

## 2. Algebraische Charakterisierung

Die optimalen Kosten $m(i, j)$ sind durch die folgende Rekursionsgleichung definiert:

$$
m(i, j) = 
\begin{cases} 
0 & \text{falls } i = j \\
\min_{i \le k < j} \{ m(i, k) + m(k+1, j) + p_{i-1} \cdot p_k \cdot p_j \} & \text{falls } i < j
\end{cases}
$$

**Korrektheitsinvariante:**
Für jede Teilkette $A_{i \dots j}$ sind die optimalen Kosten das Minimum über alle möglichen Teilungspunkte $k \in \{i, i+1, \dots, j-1\}$ der Summe der Kosten der beiden resultierenden Teilketten zuzüglich der Kosten der finalen Multiplikation der beiden resultierenden Matrizen, welche die Dimensionen $(p_{i-1} \times p_k)$ bzw. $(p_k \times p_j)$ haben.

Der Memoization-Mechanismus stellt sicher, dass für jedes Paar $(i, j) \in \mathcal{S}$ der Wert $m(i, j)$ genau einmal berechnet und gespeichert wird, wodurch die rekursive Struktur in eine Auswertung mittels dynamischer Programmierung über den Zustandsraum $\mathcal{S}$ transformiert wird.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität wird durch die Anzahl der Zustände in der Memoization-Tabelle und den Arbeitsaufwand pro Zustand bestimmt.

1. **Größe des Zustandsraums:** Die Anzahl der eindeutigen Paare $(i, j)$ mit $1 \le i \le j \le n$ ist durch die Dreieckszahl gegeben:
   $$|\mathcal{S}| = \sum_{i=1}^n \sum_{j=i}^n 1 = \frac{n(n+1)}{2} = O(n^2)$$
2. **Arbeitsaufwand pro Zustand:** Für jeden Zustand $(i, j)$ iterieren wir durch $k$ von $i$ bis $j-1$. Die Anzahl der Iterationen beträgt $j - i$. Im schlechtesten Fall ist dies $O(n)$.
3. **Gesamtkomplexität:** Die gesamte Zeitkomplexität $T(n)$ ist die Summe des Arbeitsaufwands über alle Zustände:
   $$T(n) = \sum_{1 \le i \le j \le n} (j - i) \approx \int_1^n \int_i^n (j-i) \, dj \, di = O(n^3)$$
Somit arbeitet der Algorithmus in $\Theta(n^3)$ Zeit.

### Platzkomplexität
1. **Zusätzlicher Speicher:** Die Memoization-Tabelle $M$ benötigt $O(n^2)$ Speicherplatz, um die Ergebnisse der Teilprobleme zu speichern.
2. **Rekursions-Stack:** Beim Top-Down-Ansatz beträgt die maximale Tiefe des Rekursionsbaums $n$. Daher beträgt der Stack-Speicher $O(n)$.
3. **Gesamtspeicher:** Die gesamte Platzkomplexität wird durch die Memoization-Tabelle dominiert, was zu $O(n^2)$ führt.