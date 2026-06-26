# Formale mathematische Spezifikation: Stock-Span-Problem

## 1. Definitionen und Notation

Sei $P = \langle p_0, p_1, \dots, p_{n-1} \rangle$ eine Sequenz von $n$ täglichen Aktienkursen, wobei $p_i \in \mathbb{R}_{\geq 0}$ für alle $i \in \{0, 1, \dots, n-1\}$ gilt. 

Die **Spanne** (engl. *span*) des Aktienkurses am Tag $i$, bezeichnet mit $s_i$, ist definiert als die Kardinalität des maximalen zusammenhängenden Teilsegments von Indizes, das bei $i$ endet, sodass alle Kurse in diesem Segment kleiner oder gleich $p_i$ sind. Formal:
$$s_i = \max \{ k \in \mathbb{Z}^+ : \forall j \in \{i-k+1, \dots, i\}, p_j \leq p_i \}$$

Wir definieren die Ausgabe als eine Sequenz $S = \langle s_0, s_1, \dots, s_{n-1} \rangle$.

Sei $\mathcal{S}$ der Zustand des Stacks, dargestellt als ein geordnetes Tupel von Indizes $\langle idx_1, idx_2, \dots, idx_m \rangle$, sodass $idx_1 < idx_2 < \dots < idx_m$ gilt. Der Stack erhält die **Monotonieeigenschaft** aufrecht:
$$\forall j \in \{1, \dots, m-1\}, p_{idx_j} > p_{idx_{j+1}}$$

## 2. Algebraische Charakterisierung

Um $s_i$ zu bestimmen, suchen wir den Index des **vorherigen größeren Elements** (engl. *Previous Greater Element*, PGE). Sei $PGE(i)$ definiert als:
$$PGE(i) = \max \{ j < i : p_j > p_i \} \cup \{-1\}$$

Die Spanne $s_i$ kann ausgedrückt werden als:
$$s_i = i - PGE(i)$$

### Schleifeninvariante
Zu Beginn jeder Iteration $i \in \{0, \dots, n-1\}$ enthält der Stack $\mathcal{S}$ Indizes $j < i$, sodass $p_j$ die Kurse der „sichtbaren“ Elemente links von $i$ sind. Spezifisch existiert für jedes $j \in \mathcal{S}$ kein $k$, sodass $j < k < i$ und $p_k \geq p_j$ gilt. 

Der Übergang für den Stack-Zustand $\mathcal{S}_{i+1}$ gegeben $\mathcal{S}_i$ ist:
1. **Pop-Phase:** $\mathcal{S}' = \mathcal{S}_i \setminus \{idx \in \mathcal{S}_i : p_{idx} \leq p_i\}$
2. **Push-Phase:** $\mathcal{S}_{i+1} = \mathcal{S}' \cup \{i\}$

Die Korrektheit des Algorithmus beruht auf der Tatsache, dass, falls $p_j \leq p_i$ für ein $j < i$ gilt, der Kurs $p_j$ für jeden zukünftigen Tag $t > i$ niemals das PGE sein wird, da $p_i$ zuerst angetroffen wird und $p_i \geq p_j$ gilt. Somit ist $j$ redundant.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität wird durch die Gesamtzahl der Stack-Operationen bestimmt. Sei $T(n)$ die Gesamtzahl der Operationen. Jeder Index $i \in \{0, \dots, n-1\}$ wird genau einmal auf den Stack gepusht. Ein Index wird nur dann vom Stack gepoppt, wenn er kleiner oder gleich dem aktuellen Kurs $p_i$ ist. Da jeder Index genau einmal gepusht wird, kann er höchstens einmal gepoppt werden.

Der Gesamtaufwand $W$ ist:
$$W = \sum_{i=0}^{n-1} (1 + \text{pop}_i)$$
wobei $\text{pop}_i$ die Anzahl der während der Iteration $i$ gepoppten Elemente ist. Da $\sum_{i=0}^{n-1} \text{pop}_i \leq n$ gilt, erhalten wir:
$$W \leq n + n = 2n$$
Somit gilt $T(n) = O(n)$. Die amortisierten Kosten pro Element betragen $O(1)$.

### Platzkomplexität
Die Platzkomplexität wird durch den zusätzlichen Speicherplatz bestimmt, der für den Stack $\mathcal{S}$ und das Ausgabe-Array $S$ benötigt wird.
1. **Ausgabe-Array:** $S$ benötigt $O(n)$ Platz, um $n$ Ganzzahlen zu speichern.
2. **Stack:** Im schlechtesten Fall (einer streng monoton fallenden Sequenz von Kursen, $p_0 > p_1 > \dots > p_{n-1}$) werden niemals Elemente gepoppt. Die Stack-Größe wächst auf $n$ an. Somit benötigt der Stack $O(n)$ Platz.

Die Gesamtplatzkomplexität beträgt $O(n) + O(n) = O(n)$.