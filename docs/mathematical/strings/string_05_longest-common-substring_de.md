# Formale mathematische Spezifikation: Longest Common Substring

## 1. Definitionen und Notation
Seien $S_1, S_2 \in \Sigma^*$ zwei Strings der Länge $n$ bzw. $m$.
Wir suchen $i, j, k \in \mathbb{N}$, sodass $S_1[i \dots i+k-1] = S_2[j \dots j+k-1]$ und $k$ maximiert wird.

## 2. Algebraische Charakterisierung (Dynamische Programmierung)
Definiere $L(i, j)$ als die Länge des längsten gemeinsamen Suffixes der Präfixe $S_1[1 \dots i]$ und $S_2[1 \dots j]$.
Rekursionsgleichung:
$$ L(i, j) = \begin{cases} 
0 & \text{if } i = 0 \text{ or } j = 0 \\
L(i-1, j-1) + 1 & \text{if } S_1[i] = S_2[j] \\
0 & \text{if } S_1[i] \neq S_2[j]
\end{cases} $$

Die Länge des längsten gemeinsamen Teilstrings ist $\max_{i, j} L(i, j)$.

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** Die Rekurrenz $L(i, j)$ wird für alle $1 \leq i \leq n$ und $1 \leq j \leq m$ ausgewertet. Jede Auswertung erfordert $O(1)$ Zeit. Die Zeitkomplexität beträgt $O(nm)$.
- **Platzkomplexität:** Bei einer strikten Auswertung unter Verwendung eines 2D-Arrays beträgt der Platzbedarf $O(nm)$. Da $L(i, j)$ nur von $L(i-1, j-1)$ abhängt, kann der Speicherplatzbedarf auf $O(\min(n, m))$ optimiert werden, indem nur die vorherige Zeile gespeichert wird.