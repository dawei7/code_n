# Formale mathematische Spezifikation: K-th Smallest / Order Statistic (Binary Lifting)

## 1. Definitionen und Notation

Sei $\mathcal{U} = \{1, 2, \dots, M\}$ das Universum möglicher Werte, wobei $M \in \mathbb{N}$ der Maximalwert ist. Wir definieren den Zustand unserer Sammlung als Häufigkeitsfunktion $f: \mathcal{U} \to \mathbb{N}_0$, wobei $f(x)$ die Anzahl der Vorkommen des Wertes $x$ in der Sammlung angibt.

Der Fenwick Tree (Binary Indexed Tree) ist als Datenstruktur $\mathcal{B}$ definiert, die die Präfixsummen von $f$ repräsentiert. Speziell gilt für jeden Index $i \in \{1, \dots, M\}$, dass der in $\mathcal{B}[i]$ gespeicherte Wert wie folgt definiert ist:
$$\mathcal{B}[i] = \sum_{j=i - \text{lsb}(i) + 1}^{i} f(j)$$
wobei $\text{lsb}(i) = i \& (-i)$ der Wert des niedrigstwertigen Bits (least significant bit) von $i$ ist.

Die Präfixsummenfunktion $P(x)$ ist definiert als:
$$P(x) = \sum_{j=1}^{x} f(j) = \sum_{k \in \text{path}(x)} \mathcal{B}[k]$$
wobei $\text{path}(x)$ die Menge der Indizes ist, die bei einer Standard-Fenwick-Abfrage durchlaufen werden.

Das Ziel ist es, die Ordnungsstatistik $x^*$ zu finden, definiert als:
$$x^* = \min \{ x \in \mathcal{U} \mid P(x) \ge K \}$$
gegeben einen Zielrang $K \in \{1, \dots, \sum_{x \in \mathcal{U}} f(x)\}$.

## 2. Algebraische Charakterisierung

Der Algorithmus nutzt Binary Lifting, um eine Suche über die Bit-Repräsentation des Indexraums durchzuführen. Sei $L = \lfloor \log_2 M \rfloor$. Wir stellen den Zielindex $x^*$ als Summe von Zweierpotenzen dar: $x^* = \sum_{i=0}^{L} b_i 2^i$, wobei $b_i \in \{0, 1\}$.

Wir führen während der Iteration zwei Variablen mit:
1. `idx`: Der aktuelle Präfix-Index, initialisiert auf $0$.
2. `remaining`: Der verbleibende Rang, der erfüllt werden muss, initialisiert auf $K$.

**Schleifeninvariante:** Zu Beginn jeder Iteration $j$ (wobei $j$ von $L$ bis $0$ läuft), sei $S = 2^j$. Die Invariante besagt:
$$P(\text{idx}) < K \quad \text{und} \quad P(\text{idx} + S) \text{ wird ausgewertet, um zu bestimmen, ob } x^* \in (\text{idx}, \text{idx} + S]$$

Die Übergangslogik ist durch die Eigenschaft der Fenwick Tree-Struktur definiert: $\mathcal{B}[\text{idx} + 2^j]$ speichert die Summe der Häufigkeiten im Intervall $(\text{idx}, \text{idx} + 2^j]$. 
Die Aktualisierungsregel lautet:
$$\text{idx}_{new} = \begin{cases} \text{idx} + 2^j & \text{falls } \text{idx} + 2^j \le M \text{ und } \mathcal{B}[\text{idx} + 2^j] < \text{remaining} \\ \text{idx} & \text{sonst} \end{cases}$$
$$\text{remaining}_{new} = \begin{cases} \text{remaining} - \mathcal{B}[\text{idx} + 2^j] & \text{falls Bedingung erfüllt} \\ \text{remaining} & \text{sonst} \end{cases}$$

Nach Beendigung stellt die Invariante sicher, dass `idx` die größte Ganzzahl ist, für die $P(\text{idx}) < K$ gilt. Folglich ist das $K$-te kleinste Element $x^* = \text{idx} + 1$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus besteht aus einer einzelnen Schleife, die über die Bits von $M$ iteriert. Sei $L = \lfloor \log_2 M \rfloor$. 
- Die Schleife wird exakt $L+1$ Mal ausgeführt.
- Innerhalb jeder Iteration werden die Operationen (Addition, bitweiser Vergleich und Subtraktion) in konstanter Zeit, $O(1)$, durchgeführt.
- Die gesamte Zeitkomplexität ergibt sich aus der Summation:
$$T(M) = \sum_{j=0}^{\lfloor \log_2 M \rfloor} O(1) = O(\log M)$$
Dies ist strikt optimal, da es die $O(\log^2 M)$-Komplexität vermeidet, die mit einer binären Suche über die Präfixsummenfunktion $P(x)$ verbunden wäre.

### Platzkomplexität
- **Zusätzlicher Speicherplatz:** Der Algorithmus benötigt $O(1)$ zusätzlichen Speicherplatz für die Variablen `idx`, `bitmask` und `remaining`.
- **Gesamtspeicherplatz:** Der Fenwick Tree $\mathcal{B}$ benötigt ein Array der Größe $M+1$, um die Häufigkeitssummen zu speichern. Somit beträgt die gesamte Platzkomplexität $O(M)$. 
- Hinweis: Falls das Universum $\mathcal{U}$ dünn besetzt ist oder der Wertebereich groß ist, ist eine Koordinatenkompression erforderlich, die die unterschiedlichen Werte auf den Bereich $[1, N]$ abbildet, wobei $N \le \text{Anzahl der Elemente}$, was zu $O(N)$ Speicherplatz führt.