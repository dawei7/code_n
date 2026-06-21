# Formale mathematische Spezifikation: Bin Packing (First Fit Decreasing)

## 1. Definitionen und Notation

Sei das Bin Packing Problem (BPP) über einer endlichen Menge von Objekten und einem unbegrenzten Vorrat an homogenen Bins definiert. Wir formalisieren die Eingaben, Ausgaben und Zustandsräume wie folgt:

### 1.1 Eingaberaum
*   **Objektmenge:** Sei $I = \{1, 2, \dots, n\}$ die Menge der Objektindizes, wobei $n \in \mathbb{N}$ die Gesamtzahl der Objekte darstellt.
*   **Kapazität:** Sei $C \in \mathbb{R}^+$ die maximale Kapazität jedes Bins. Ohne Beschränkung der Allgemeinheit kann das Problem so normalisiert werden, dass $C = 1$ gilt.
*   **Gewichte:** Sei $W = (w_1, w_2, \dots, w_n)$ eine Sequenz von Objektgewichten, wobei jedes $w_i \in (0, C]$ für alle $i \in I$ gilt.

### 1.2 Ausgaberaum
Die Ausgabe ist eine Partition von $I$ in $m$ disjunkte Teilmengen, die die Bins repräsentieren, zusammen mit der Kardinalität $m$.
*   **Bin-Partition:** Sei $\mathcal{B} = \{B_1, B_2, \dots, B_m\}$ eine Familie von Teilmengen von $I$, die folgende Bedingungen erfüllt:
    1.  **Disjunktheit:** $B_k \cap B_l = \emptyset \quad \forall k \neq l$.
    2.  **Vollständigkeit:** $\bigcup_{k=1}^m B_k = I$.
    3.  **Kapazitätsbeschränkung:** $\sum_{i \in B_k} w_i \le C \quad \forall k \in \{1, \dots, m\}$.
*   **Zielsetzung:** Minimierung der Anzahl aktiver Bins $m = |\mathcal{B}|$.

### 1.3 Zustandsraum des FFD-Dynamiksystems
Sei $\mathcal{S}$ der Zustandsraum des Algorithmus während der Ausführung. Zum Schritt $j \in \{0, 1, \dots, n\}$ wird der Zustand durch das Tupel $S_j = (m_j, R_j)$ repräsentiert, wobei:
*   $m_j \in \{0, \dots, j\}$ die Anzahl der aktuell geöffneten Bins ist.
*   $R_j = (R_{j, 1}, R_{j, 2}, \dots, R_{j, m_j})$ eine geordnete Sequenz der verbleibenden Kapazitäten für jedes offene Bin ist, wobei $R_{j, k} \in [0, C]$ für alle $k \in \{1, \dots, m_j\}$ gilt.
*   Der Anfangszustand ist definiert als $S_0 = (0, \emptyset)$.

---

## 2. Algebraische Charakterisierung

Der First Fit Decreasing (FFD) Algorithmus arbeitet in zwei unterschiedlichen Phasen: einer Sortierphase und einer iterativen Greedy-Platzierungsphase, die durch eine deterministische Übergangsfunktion gesteuert wird.

### 2.1 Sortierphase
Sei $\pi: I \to I$ eine Permutation der Objektindizes, welche die Gewichte in nicht-aufsteigender Reihenfolge sortiert. Wir definieren die sortierte Gewichtssequenz $X = (x_1, x_2, \dots, x_n)$ so, dass:
$$x_j = w_{\pi(j)} \quad \forall j \in \{1, \dots, n\}$$
wobei
$$x_1 \ge x_2 \ge \dots \ge x_n$$

### 2.2 Übergangsfunktion (First Fit Entscheidungsregel)
Für jedes sortierte Objekt $j \in \{1, \dots, n\}$ mit Gewicht $x_j$ definieren wir den Ziel-Bin-Index $k^*(j)$ unter Verwendung der Auswahlfunktion:
$$k^*(j) = \min \left( \{ k \in \{1, \dots, m_{j-1}\} \mid R_{j-1, k} \ge x_j \} \cup \{ m_{j-1} + 1 \} \right)$$

Diese Auswahlregel garantiert, dass das Objekt in das Bin mit dem niedrigsten Index platziert wird, das über ausreichend Restkapazität verfügt. Falls kein solches Bin existiert, wird ein neues Bin initialisiert.

### 2.3 Zustandsaktualisierungsgleichungen
Gegeben der Zustand $S_{j-1} = (m_{j-1}, R_{j-1})$ und die Entscheidung $k^* = k^*(j)$, geht der Zustand gemäß der folgenden Rekursionsgleichungen in $S_j = (m_j, R_j)$ über:

#### Fall 1: Platzierung in einem existierenden Bin ($k^* \le m_{j-1}$)
$$m_j = m_{j-1}$$
$$R_{j, k} = \begin{cases} 
R_{j-1, k} - x_j & \text{falls } k = k^* \\ 
R_{j-1, k} & \text{falls } k \neq k^* 
\end{cases} \quad \forall k \in \{1, \dots, m_j\}$$

#### Fall 2: Initialisierung eines neuen Bins ($k^* = m_{j-1} + 1$)
$$m_j = m_{j-1} + 1$$
$$R_{j, k} = \begin{cases} 
R_{j-1, k} & \text{falls } k \le m_{j-1} \\ 
C - x_j & \text{falls } k = m_j 
\end{cases}$$

### 2.4 Schleifeninvarianten
Die Korrektheit und die strukturellen Eigenschaften des FFD-Algorithmus werden durch die folgenden Invarianten gewahrt, die für alle Schritte $j \in \{1, \dots, n\}$ gelten:

1.  **Durchführbarkeitsinvariante:**
    $$\forall k \in \{1, \dots, m_j\}, \quad R_{j, k} \ge 0$$
2.  **Massenerhaltung:**
    $$\sum_{k=1}^{m_j} (C - R_{j, k}) = \sum_{i=1}^j x_i$$
3.  **First-Fit-Minimalität:**
    $$\forall k < k^*(j), \quad R_{j-1, k} < x_j$$
    *(Kein Bin vor dem gewählten Bin hat genügend Platz, um das aktuelle Objekt aufzunehmen).*

### 2.5 Approximationsschranken
Sei $\text{FFD}(I)$ die Anzahl der Bins, die vom FFD-Algorithmus für eine Instanz $I$ erzeugt werden, und sei $\text{OPT}(I)$ die optimale Anzahl an Bins.

#### Theorem (Dósa, 2007)
Für jede Instanz $I$ des Bin Packing Problems gilt:
$$\text{FFD}(I) \le \frac{11}{9} \text{OPT}(I) + \frac{6}{9}$$

Darüber hinaus ist diese Schranke scharf. Es existieren Instanzen, für die gilt:
$$\text{FFD}(I) = \left\lfloor \frac{11}{9} \text{OPT}(I) \right\rfloor$$

---

## 3. Komplexitätsanalyse

### 3.1 Zeitkomplexität

Die gesamte Zeitkomplexität des FFD-Algorithmus ergibt sich aus der Summe des Aufwands in der Sortierphase und der Platzierungsphase:
$$T(n) = T_{\text{sort}}(n) + T_{\text{place}}(n)$$

#### 1. Sortierphase
Das Sortieren von $n$ skalaren Gewichten mittels eines vergleichsbasierten Sortieralgorithmus (z. B. Mergesort oder Heapsort) erfordert:
$$T_{\text{sort}}(n) = \Theta(n \log n)$$

#### 2. Platzierungsphase (Naiver linearer Scan)
In der Standardimplementierung erfordert das Finden von $k^*(j)$ einen sequentiellen Scan über die existierenden $m_{j-1}$ Bins.
*   **Schlechtester Fall:** Im schlechtesten Fall erfordert jedes Objekt das Öffnen eines neuen Bins (z. B. wenn $w_i > \frac{C}{2}$ für alle $i$). Die Anzahl der aktiven Bins zum Schritt $j$ ist $j-1$. Die Gesamtzahl der Vergleiche beträgt:
    $$T_{\text{place}}(n) = \sum_{j=1}^n O(m_{j-1}) = \sum_{j=1}^n O(j) = O(n^2)$$
*   **Durchschnittlicher Fall:** Bei einer Gleichverteilung der Gewichte bleibt die erwartete Anzahl der pro Objekt gescannten Bins $O(n)$, was zu einer durchschnittlichen Komplexität von $O(n^2)$ führt.

#### 3. Platzierungsphase (Optimierter Segment Tree)
Um die erforderliche $O(n \log n)$ Komplexität zu erreichen, können wir die Bin-Kapazitäten mittels eines balancierten Segment Tree (oder Range Maximum Query Tree) der Größe $n$ repräsentieren.
*   **Struktur:** Die Blätter des Segment Tree repräsentieren die Restkapazitäten der Bins $B_1, B_2, \dots, B_n$, initialisiert auf $C$. Jeder innere Knoten $u$ speichert die maximale Restkapazität seiner Kinder:
    $$\text{val}(u) = \max(\text{val}(\text{left}(u)), \text{val}(\text{right}(u)))$$
*   **Abfrage und Aktualisierung:** Um das Objekt $x_j$ zu platzieren, durchlaufen wir den Baum, um das am weitesten links stehende Blatt $k$ zu finden, für das $\text{val}(k) \ge x_j$ gilt.
    *   Falls $\text{val}(\text{left}(u)) \ge x_j$, durchlaufen wir rekursiv das linke Kind.
    *   Andernfalls durchlaufen wir das rechte Kind.
    *   Sobald das Blatt $k$ identifiziert ist, aktualisieren wir dessen Wert: $R_k \leftarrow R_k - x_j$ und propagieren die Änderungen zurück zur Wurzel.
*   **Komplexität:** Da die Höhe des Segment Tree $\lceil \log_2 n \rceil$ beträgt, benötigen sowohl die Such- als auch die Aktualisierungsoperationen $O(\log n)$ Zeit.
    $$T_{\text{place}}(n) = \sum_{j=1}^n O(\log n) = O(n \log n)$$

#### Gesamte Zeitkomplexität
Unter Verwendung der Segment-Tree-Optimierung ergibt sich:
$$T(n) = \Theta(n \log n) + O(n \log n) = \Theta(n \log n)$$

### 3.2 Platzkomplexität

#### 1. Hilfsspeicher
*   **Sortierung:** In-place Sortieralgorithmen benötigen $O(\log n)$ zusätzlichen Stack-Speicher, während stabiler Mergesort $O(n)$ Speicher benötigt.
*   **Bin-Repräsentation:** 
    *   Die naive Array-Repräsentation der Bin-Kapazitäten erfordert $O(m) \le O(n)$ Speicher.
    *   Die Segment-Tree-Repräsentation erfordert einen Baum der Größe $2^{\lceil \log_2 n \rceil + 1} - 1 \approx 4n$ Knoten, was $O(n)$ Speicher entspricht.
*   Daher ist die Komplexität des Hilfsspeichers:
    $$S_{\text{aux}}(n) = \Theta(n)$$

#### 2. Gesamtspeicher
Unter Einbeziehung des Eingabespeichers für die Gewichte $W$ beträgt die gesamte Platzkomplexität:
$$S_{\text{total}}(n) = \Theta(n)$$