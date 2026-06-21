# Formale mathematische Spezifikation: Sqrt(x) (Abgerundete Quadratwurzel)

## 1. Definitionen und Notation

Sei $x \in \mathbb{N}_0$ die nicht-negative Ganzzahl als Eingabe. Wir definieren die Zielfunktion $f: \mathbb{N}_0 \to \mathbb{N}_0$ wie folgt:
$$f(x) = \lfloor \sqrt{x} \rfloor$$
wobei $\lfloor \cdot \rfloor$ die Floor-Funktion (Abrundungsfunktion) bezeichnet, die eine reelle Zahl auf die größte ganze Zahl abbildet, die kleiner oder gleich dieser ist.

Der Algorithmus operiert über einem diskreten Suchraum $\mathcal{S} = \{0, 1, 2, \dots, x\}$. Wir definieren den Zustand des Algorithmus in der Iteration $k$ durch das Tupel $(L_k, R_k, \text{res}_k)$, wobei:
*   $L_k \in \mathbb{N}_0$ die untere Schranke des Suchintervalls ist.
*   $R_k \in \mathbb{N}_0$ die obere Schranke des Suchintervalls ist.
*   $\text{res}_k \in \mathbb{N}_0$ die aktuell beste Approximation (der „Kandidat“ für den Floor-Wert) ist, sodass $\text{res}_k^2 \le x$ gilt.

## 2. Algebraische Charakterisierung

Der Algorithmus ist eine Suche nach der eindeutigen Ganzzahl $y \in \mathcal{S}$, die die folgende Bedingung erfüllt:
$$y^2 \le x < (y+1)^2$$

### Schleifeninvariante
Zu Beginn jeder Iteration $k$ gilt die folgende Invariante:
1.  Der wahre Wert $f(x)$ ist im Intervall $[L_k, R_k]$ enthalten, wenn wir den Kandidaten $\text{res}_k$ betrachten. Formeller ausgedrückt: Für alle $z \in \mathbb{N}_0$ mit $z^2 \le x$ ist $z \le R_k$ nicht notwendigerweise wahr, aber es gilt $\text{res}_k = \max \{ z \in \{0, \dots, L_k-1\} \mid z^2 \le x \}$.
2.  Der Suchraum nimmt monoton ab: $|R_{k+1} - L_{k+1}| \approx \frac{1}{2} |R_k - L_k|$.

### Zustandsübergänge
Gegeben sei $m_k = \lfloor L_k + \frac{R_k - L_k}{2} \rfloor$. Die Übergangsfunktion $\delta: (L_k, R_k, \text{res}_k) \to (L_{k+1}, R_{k+1}, \text{res}_{k+1})$ ist definiert als:
$$
(L_{k+1}, R_{k+1}, \text{res}_{k+1}) = 
\begin{cases} 
(m_k + 1, R_k, m_k) & \text{falls } m_k^2 \le x \\
(L_k, m_k - 1, \text{res}_k) & \text{falls } m_k^2 > x 
\end{cases}
$$
Der Algorithmus terminiert in der Iteration $K$, wenn $L_K > R_K$, und gibt $\text{res}_K$ zurück.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus führt eine binäre Suche über der Domäne $\mathcal{D} = [0, x]$ durch. Sei $N = x$. In jeder Iteration wird die Größe des Suchintervalls $I_k = R_k - L_k + 1$ um etwa die Hälfte reduziert:
$$I_{k+1} \le \frac{I_k}{2}$$
Die Rekurrenz für die Anzahl der Operationen $T(N)$ lautet:
$$T(N) = T\left(\frac{N}{2}\right) + c$$
wobei $c$ die konstante Zeit für arithmetische Operationen (Multiplikation, Vergleich und Addition) darstellt. Nach dem Master-Theorem (Fall 2), wobei $a=1, b=2, d=0$:
$$T(N) = \Theta(\log_2 N)$$
Somit beträgt die Zeitkomplexität $O(\log x)$.

### Platzkomplexität
Der Algorithmus verwaltet eine feste Anzahl an skalaren Variablen: $L, R, \text{res}, \text{mid}, \text{sq}$. 
Sei $S(N)$ der benötigte zusätzliche Speicherplatz. Da der Speicherverbrauch unabhängig von der Eingabegröße $x$ ist (unter der Annahme einer Ganzzahldarstellung mit fester Breite für $x$), gilt:
$$S(N) = O(1)$$
Der Algorithmus arbeitet in-place und benötigt keine zusätzlichen Datenstrukturen, die mit der Eingabe skalieren.