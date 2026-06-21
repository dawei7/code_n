# Formale mathematische Spezifikation: Das Skyline-Problem

## 1. Definitionen und Notation

Sei $\mathcal{B} = \{b_1, b_2, \dots, b_n\}$ eine Menge von $n$ Gebäuden, wobei jedes Gebäude $b_i$ als Tripel $(L_i, R_i, H_i) \in \mathbb{Z}^3$ definiert ist, sodass $L_i < R_i$ und $H_i > 0$ gilt.

Die **Skyline** von $\mathcal{B}$ ist definiert als eine Sequenz von Schlüsselpunkten $S = \{(x_1, y_1), (x_2, y_2), \dots, (x_m, y_m)\}$, sodass:
1. Die Punkte sind strikt nach ihren x-Koordinaten geordnet: $x_1 < x_2 < \dots < x_m$.
2. Die Sequenz repräsentiert die obere Einhüllende der Gebäude: $f(x) = \max(\{H_i \mid L_i \le x < R_i\} \cup \{0\})$.
3. Für jedes $x \in [x_j, x_{j+1})$ gilt $f(x) = y_j$.
4. Die Sequenz ist minimal, was bedeutet, dass $y_j \neq y_{j+1}$ für alle $1 \le j < m$ gilt.

Der Definitionsbereich der Eingabe ist $\mathcal{B} \subset \mathbb{Z}^3$, und die Ausgabe ist eine Sequenz $S \subset \mathbb{Z}^2$.

## 2. Algebraische Charakterisierung

Der Algorithmus verwendet eine Divide-and-Conquer-Strategie, die auf dem Prinzip der Superposition von Funktionen basiert. Seien $f_L(x)$ und $f_R(x)$ die Skyline-Funktionen für zwei disjunkte Teilmengen von Gebäuden $\mathcal{B}_L$ und $\mathcal{B}_R$. Die Skyline der Vereinigung $\mathcal{B}_L \cup \mathcal{B}_R$ ist gegeben durch:
$$f_{merged}(x) = \max(f_L(x), f_R(x))$$

### Rekursionsgleichung
Der Algorithmus zerlegt das Problem in Teilprobleme der Größe $n/2$. Sei $T(n)$ die Zeitkomplexität für eine Menge von $n$ Gebäuden. Die Rekursionsgleichung lautet:
$$T(n) = 2T\left(\frac{n}{2}\right) + M(n)$$
wobei $M(n)$ die Kosten der Merge-Operation sind. Gegeben zwei Skylines $S_L$ und $S_R$ mit den Längen $|S_L| = k_1$ und $|S_R| = k_2$, führt die Merge-Operation einen linearen Scan beider Sequenzen durch. Da die Anzahl der Schlüsselpunkte höchstens $2n$ beträgt, gilt $M(n) = O(k_1 + k_2) = O(n)$.

### Schleifeninvariante
Während der Ausführung der `_merge` Funktion seien $i$ und $j$ die Indizes der aktuellen Schlüsselpunkte, die in $S_L$ und $S_R$ verarbeitet werden. Seien $h_1$ und $h_2$ die Höhen der zuletzt verarbeiteten Schlüsselpunkte aus $S_L$ bzw. $S_R$. In jeder Iteration gilt die Invariante, dass die Höhe der zusammengeführten Skyline am aktuellen $x$ wie folgt definiert ist:
$$H_{curr} = \max(h_1, h_2)$$
Der Algorithmus fügt $(x, H_{curr})$ genau dann zum Ergebnis hinzu, wenn $H_{curr} \neq y_{last}$ gilt, wobei $y_{last}$ die Höhe des zuletzt hinzugefügten Schlüsselpunkts ist. Dies stellt die Minimalität der Skyline-Repräsentation sicher.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Rekursionsgleichung $T(n) = 2T(n/2) + O(n)$ fällt unter das **Master-Theorem** (Fall 2).
- Hierbei sind $a = 2$, $b = 2$ und $f(n) = O(n^1)$.
- Da $n^{\log_b a} = n^{\log_2 2} = n^1$ gilt, ist die Komplexität:
$$T(n) = \Theta(n^{\log_b a} \log n) = \Theta(n \log n)$$
Der Arbeitsaufwand auf jeder Ebene des Rekursionsbaums beträgt $O(n)$, und es gibt $\log_2 n$ Ebenen, was die obere Schranke von $O(n \log n)$ bestätigt.

### Platzkomplexität
- **Rekursions-Stack:** Die Tiefe des Rekursionsbaums beträgt $\lceil \log_2 n \rceil$, was $O(\log n)$ zum zusätzlichen Speicherbedarf beiträgt.
- **Ausgabespeicherung:** Jeder Merge-Schritt erzeugt eine neue Liste von Schlüsselpunkten. Im Schlechtesten Fall beträgt die Anzahl der Schlüsselpunkte in einer Skyline $2n$. Da der Algorithmus die Ergebnisse der Teilprobleme speichert, wird die gesamte Platzkomplexität durch die Speicherung der Schlüsselpunkte dominiert:
$$S(n) = 2S(n/2) + O(n) \implies S(n) = O(n)$$
Somit ist die gesamte Platzkomplexität $O(n)$, was für die Speicherung der resultierenden Skyline optimal ist.