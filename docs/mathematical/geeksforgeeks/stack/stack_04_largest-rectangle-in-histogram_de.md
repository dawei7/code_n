# Formale mathematische Spezifikation: Largest Rectangle in Histogram

## 1. Definitionen und Notation

Sei $H = [h_0, h_1, \dots, h_{n-1}]$ eine Folge nicht-negativer ganzer Zahlen, welche die Höhen von $n$ Balken darstellen, wobei jeder Balken eine Einheitsbreite besitzt. Wir definieren die Definitionsmenge der Indizes als $\mathcal{I} = \{0, 1, \dots, n-1\}$.

Ein durch das Intervall $[L, R] \subseteq \mathcal{I}$ definiertes Rechteck hat eine Höhe, die durch den minimalen Balken innerhalb dieses Intervalls beschränkt ist:
$$h_{\min}(L, R) = \min_{k \in [L, R]} h_k$$
Die Fläche eines Rechtecks, das sich vom Index $L$ bis $R$ erstreckt, ist gegeben durch:
$$A(L, R) = h_{\min}(L, R) \times (R - L + 1)$$
Das Ziel ist es, die maximale Fläche $A^*$ über alle möglichen Intervalle zu finden:
$$A^* = \max_{0 \le L \le R < n} A(L, R)$$

Um den Algorithmus zu unterstützen, erweitern wir $H$ um einen Sentinel-Wert $h_n = 0$, um sicherzustellen, dass bei Terminierung alle Elemente vom Stack ge-`pop`t werden. Sei $S$ ein Stack, der eine streng monoton steigende Folge von Indizes $i_1, i_2, \dots, i_m$ enthält, sodass $h_{i_1} < h_{i_2} < \dots < h_{i_m}$.

## 2. Algebraische Charakterisierung

Für jeden Balken $i \in \mathcal{I}$ sei $L_i$ der Index des **Previous Smaller Element (PSE)** und $R_i$ der Index des **Next Smaller Element (NSE)**. Formal:
$$L_i = \max \{j < i \mid h_j < h_i\} \cup \{-1\}$$
$$R_i = \min \{j > i \mid h_j < h_i\} \cup \{n\}$$

Das größte Rechteck mit der Höhe $h_i$ als Minimum ist durch die maximale Breite $w_i = R_i - L_i - 1$ definiert. Die globale maximale Fläche ist:
$$A^* = \max_{i \in \mathcal{I}} (h_i \times (R_i - L_i - 1))$$

**Schleifeninvariante:**
Zu Beginn jeder Iteration $i \in \{0, \dots, n\}$ enthält der Stack $S$ Indizes $s_1, s_2, \dots, s_k$, sodass:
1. $h_{s_1} < h_{s_2} < \dots < h_{s_k}$.
2. Für jeden verarbeiteten Index $j$ mit $j < i$ und $j \notin S$ wurde die maximale Fläche $A^*$ so aktualisiert, dass sie das maximale Rechteck enthält, bei dem $j$ die minimale Höhe ist.
3. Für jedes $s_j \in S$ gilt $L_{s_j} = s_{j-1}$ (mit $s_0 = -1$).

Wenn $h_i < h_{s_k}$, wird das Element $s_k$ ge-`pop`t. Da $h_i$ das erste Element rechts ist, das kleiner als $h_{s_k}$ ist, gilt $R_{s_k} = i$. Das PSE ist das neue oberste Element des Stacks, $s_{k-1}$, folglich gilt $L_{s_k} = s_{k-1}$. Die Fläche wird als $h_{s_k} \times (i - s_{k-1} - 1)$ berechnet.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus führt einen einzigen Durchlauf über das Eingabe-Array $H$ der Größe $n$ aus. 
- Jeder Index $i \in \{0, \dots, n-1\}$ wird genau einmal auf den Stack ge-`push`t.
- Jeder Index $i$ wird höchstens einmal vom Stack ge-`pop`t.
- Die Operationen innerhalb der `while`-Schleife (`pop`, Vergleich, Flächenberechnung) sind in $O(1)$.

Sei $T(n)$ die gesamte Zeitkomplexität. Die Gesamtzahl der `push`-Operationen beträgt $n+1$ (einschließlich des Sentinels), und die Gesamtzahl der `pop`-Operationen beträgt höchstens $n+1$. Der Gesamtaufwand ist:
$$T(n) = \sum_{i=0}^{n} (\text{push}_i + \text{pop}_i) = O(n)$$
Somit ist der Algorithmus im durchschnittlichen Fall und im schlechtesten Fall in $\Theta(n)$.

### Platzkomplexität
Die Platzkomplexität wird durch den Hilfs-Stack $S$ dominiert.
- Im schlechtesten Fall (eine streng monoton steigende Folge von Höhen) enthält der Stack alle $n$ Indizes.
- Der benötigte Platz beträgt $S(n) = O(n)$.
- Es sind keine zusätzlichen Datenstrukturen proportional zu $n$ erforderlich, wodurch die zusätzliche Platzkomplexität bei $O(n)$ bleibt.