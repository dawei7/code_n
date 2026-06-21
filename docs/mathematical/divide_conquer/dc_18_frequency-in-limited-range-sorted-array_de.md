# Formale mathematische Spezifikation: Häufigkeit von Elementen in einem sortierten Array

## 1. Definitionen und Notation

Sei $A = [a_0, a_1, \dots, a_{n-1}]$ eine Folge von Ganzzahlen der Länge $n \in \mathbb{N}_0$, wobei die Folge nicht-abnehmend ist, sodass $a_i \leq a_{i+1}$ für alle $0 \leq i < n-1$ gilt. Sei $x \in \mathbb{Z}$ der Zielwert.

Wir definieren die Menge der Indizes, an denen der Zielwert auftritt, als:
$$I_x = \{i \in \{0, \dots, n-1\} \mid a_i = x\}$$

Das Ziel ist es, die Kardinalität von $I_x$, bezeichnet als $|I_x|$, zu bestimmen oder das Grenzpaar $(\min(I_x), \max(I_x))$ zurückzugeben, falls $I_x \neq \emptyset$, andernfalls $(-1, -1)$.

- **Definitionsbereich der Indizes:** $\mathcal{I} = \{0, 1, \dots, n-1\}$.
- **Zustandsraum:** Der Algorithmus verwaltet einen Zustand $\mathcal{S} = (l, r, \text{ans})$, wobei $l, r \in \mathbb{Z}$ die Suchgrenzen repräsentieren und $\text{ans} \in \mathcal{I} \cup \{-1\}$ den aktuell besten Kandidatenindex darstellt.

## 2. Algebraische Charakterisierung

Der Algorithmus beruht auf der Monotonie des Prädikats $P(i) \equiv (a_i \geq x)$. Da $A$ sortiert ist, existiert ein eindeutiger Partitionspunkt $k$, sodass $a_i < x$ für alle $i < k$ und $a_i \geq x$ für alle $i \geq k$ gilt.

### Linkestes Vorkommen ($\mathcal{L}$)
Um $\min(I_x)$ zu finden, definieren wir die Suchfunktion $f_L(A, x)$, welche die folgende Invariante aufrechterhält:
1. Wenn $a_{mid} < x$, dann ist $\min(I_x) > mid$.
2. Wenn $a_{mid} \geq x$, dann ist $\min(I_x) \leq mid$.

Die Aktualisierungsregel für das Suchintervall $[l, r]$ lautet:
$$
\begin{cases} 
l_{t+1} = mid + 1, & \text{falls } a_{mid} < x \\
r_{t+1} = mid - 1, \text{ ans} = mid, & \text{falls } a_{mid} = x \\
r_{t+1} = mid - 1, & \text{falls } a_{mid} > x 
\end{cases}
$$
Die Suche terminiert, wenn $l > r$, was $\min(I_x) = \text{ans}$ ergibt, falls $a_{\text{ans}} = x$, andernfalls ist es $\text{undefined}$.

### Rechtestes Vorkommen ($\mathcal{R}$)
Um $\max(I_x)$ zu finden, definieren wir die Suchfunktion $f_R(A, x)$, welche die folgende Invariante aufrechterhält:
1. Wenn $a_{mid} \leq x$, dann ist $\max(I_x) \geq mid$.
2. Wenn $a_{mid} > x$, dann ist $\max(I_x) < mid$.

Die Aktualisierungsregel für das Suchintervall $[l, r]$ lautet:
$$
\begin{cases} 
l_{t+1} = mid + 1, \text{ ans} = mid, & \text{falls } a_{mid} = x \\
l_{t+1} = mid + 1, & \text{falls } a_{mid} < x \\
r_{t+1} = mid - 1, & \text{falls } a_{mid} > x 
\end{cases}
$$
Die Häufigkeit ist durch die Abbildung $\Phi: A \times \mathbb{Z} \to \mathbb{N}_0$ gegeben:
$$\Phi(A, x) = \begin{cases} \max(I_x) - \min(I_x) + 1 & \text{falls } I_x \neq \emptyset \\ 0 & \text{falls } I_x = \emptyset \end{cases}$$

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus führt zwei unabhängige binäre Suchen durch. Jede binäre Suche operiert auf einem Suchraum der Größe $N$, der bei jeder Iteration $t$ halbiert wird. Die Rekurrenz für die Anzahl der Operationen $T(N)$ lautet:
$$T(N) = T\left(\frac{N}{2}\right) + c$$
Nach dem Master-Theorem, wobei $a=1, b=2, f(n)=O(1)$, erhalten wir $T(N) = O(\log_2 N)$.
Da der Algorithmus zwei solcher Suchen sequenziell ausführt, beträgt die gesamte Zeitkomplexität:
$$T_{total}(N) = O(\log N) + O(\log N) = O(\log N)$$

### Platzkomplexität
Der Algorithmus verwendet eine konstante Anzahl an Hilfsvariablen ($l, r, mid, \text{first}, \text{last}$), unabhängig von der Eingabegröße $N$.
- **Zusätzlicher Speicherplatz:** $O(1)$.
- **Gesamter Speicherplatz:** $O(N)$ zur Speicherung des Eingabe-Arrays, aber $O(1)$ zusätzlicher Speicherplatz über die Eingabespeicherung hinaus. Somit ist der Algorithmus strikt in-place.