# Formale mathematische Spezifikation: Shortest Common Supersequence

## 1. Definitionen und Notation

Sei $\Sigma$ ein endliches Alphabet. Seien $X = \langle x_1, x_2, \dots, x_M \rangle$ und $Y = \langle y_1, y_2, \dots, y_N \rangle$ zwei Strings (Sequenzen) über $\Sigma$, wobei $M, N \in \mathbb{N}_0$.

*   **Subsequence:** Ein String $Z$ ist eine Subsequence von $X$, wenn eine streng monoton steigende Folge von Indizes $\langle i_1, i_2, \dots, i_k \rangle$ existiert, sodass $1 \le i_1 < i_2 < \dots < i_k \le M$ und $Z = \langle x_{i_1}, x_{i_2}, \dots, x_{i_k} \rangle$ gilt.
*   **Supersequence:** Ein String $S$ ist eine Supersequence von $X$, wenn $X$ eine Subsequence von $S$ ist.
*   **Shortest Common Supersequence (SCS):** Ein String $S^*$ ist eine SCS von $X$ und $Y$, wenn $S^*$ eine Supersequence von sowohl $X$ als auch $Y$ ist und für jede andere gemeinsame Supersequence $S'$ die Bedingung $|S^*| \le |S'|$ gilt.
*   **Zustandsraum:** Wir definieren eine DP-Tabelle $D \in \mathbb{N}_0^{(M+1) \times (N+1)}$, wobei $D_{i,j}$ die Länge der SCS der Präfixe $X_{1..i}$ und $Y_{1..j}$ repräsentiert.

## 2. Algebraische Charakterisierung

Das Problem wird durch die Beziehung zwischen der SCS und der Longest Common Subsequence (LCS) bestimmt. Sei $L_{i,j}$ die Länge der LCS der Präfixe $X_{1..i}$ und $Y_{1..j}$. Die Rekurrenz für $L_{i,j}$ ist definiert als:

$$
L_{i,j} = 
\begin{cases} 
0 & \text{falls } i=0 \text{ oder } j=0 \\
1 + L_{i-1, j-1} & \text{falls } x_i = y_j \\
\max(L_{i-1, j}, L_{i, j-1}) & \text{falls } x_i \neq y_j 
\end{cases}
$$

Die Länge der SCS, $|S^*|$, ergibt sich aus der Identität:
$$|S^*| = M + N - L_{M,N}$$

Um $S^*$ zu konstruieren, definieren wir einen Pfad $\mathcal{P}$ im Gitter von $(M, N)$ nach $(0, 0)$. Sei $S^{(k)}$ die Sequenz der Zeichen, die während des Tracebacks angehängt werden. Die Übergangsfunktion $\delta(i, j)$ für das Traceback lautet:

$$
\text{Step}(i, j) = 
\begin{cases} 
(i-1, j-1), \text{ hänge } x_i \text{ an} & \text{falls } x_i = y_j \\
(i-1, j), \text{ hänge } x_i \text{ an} & \text{falls } x_i \neq y_j \text{ und } L_{i-1, j} \ge L_{i, j-1} \\
(i, j-1), \text{ hänge } y_j \text{ an} & \text{falls } x_i \neq y_j \text{ und } L_{i-1, j} < L_{i, j-1}
\end{cases}
$$

Die Induktionsanfänge (Basisfälle) für das Traceback treten ein, wenn $i=0$ oder $j=0$ gilt; in diesem Fall hängen wir das verbleibende Suffix des nicht-leeren Strings an.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus besteht aus zwei unterschiedlichen Phasen:
1.  **Tabellenkonstruktion:** Die DP-Tabelle $D$ (oder $L$) wird mittels einer verschachtelten Schleifenstruktur gefüllt. Die äußere Schleife läuft $M$-mal und die innere Schleife $N$-mal. Die Berechnung jeder Zelle erfolgt in $O(1)$. Die Gesamtlaufzeit beträgt:
    $$\sum_{i=1}^{M} \sum_{j=1}^{N} \Theta(1) = \Theta(MN)$$
2.  **Traceback:** Das Traceback durchläuft das Gitter von $(M, N)$ nach $(0, 0)$. In jedem Schritt wird entweder $i$ oder $j$ (oder beide) dekrementiert. Die maximale Anzahl an Schritten beträgt $M+N$. Somit ist das Traceback in $O(M+N)$ möglich.

Die gesamte Zeitkomplexität beträgt $O(MN) + O(M+N) = O(MN)$.

### Platzkomplexität
Der Algorithmus erfordert die Speicherung der DP-Tabelle $L$ der Dimensionen $(M+1) \times (N+1)$, um die Rekonstruktion des Strings $S^*$ zu ermöglichen. 
*   **Hilfsspeicher:** Die Matrix $L$ belegt $(M+1)(N+1)$ Speicherzellen.
*   **Gesamtspeicher:** Da das Traceback einen wahlfreien Zugriff auf die Werte von $L_{i,j}$ benötigt, um den optimalen Pfad zu bestimmen, ist die Platzkomplexität strikt $\Theta(MN)$. Im Gegensatz zur reinen Längenberechnung, die mittels zweier Zeilen auf $O(\min(M, N))$ optimiert werden kann, erfordert die Rekonstruktionsphase die vollständige Matrix, um die Entscheidungshistorie beizubehalten.