# Formale mathematische Spezifikation: Pow(x, n) (Schnelle Exponentiation)

## 1. Definitionen und Notation

Sei $x \in \mathbb{R}$ die Basis und $n \in \mathbb{Z}$ der Exponent. Wir definieren die Funktion $f: \mathbb{R} \times \mathbb{Z} \to \mathbb{R}$ als $f(x, n) = x^n$.

Der Definitionsbereich des Algorithmus ist durch die Menge der Paare $(x, n) \in \mathbb{R} \times \mathbb{Z}$ gegeben. Wir definieren die folgenden Teilmengen und Operationen:
*   **Basisfall:** $x^0 = 1$ für alle $x \neq 0$.
*   **Reziproke Eigenschaft:** Für $n < 0$ gilt $x^n = (x^{-1})^{-n} = \frac{1}{x^{-n}}$.
*   **Binärdarstellung:** Sei $n$ in Binärform dargestellt als $n = \sum_{i=0}^{k} b_i 2^i$, wobei $b_i \in \{0, 1\}$ und $k = \lfloor \log_2 |n| \rfloor$.

## 2. Algebraische Charakterisierung

Der Algorithmus basiert auf dem Prinzip der **Exponentiation durch Quadrieren** (Exponentiation by Squaring), welches aus der folgenden Rekursionsgleichung abgeleitet ist:

$$
f(x, n) = 
\begin{cases} 
1 & \text{if } n = 0 \\
(f(x, n/2))^2 & \text{if } n > 0, n \equiv 0 \pmod 2 \\
x \cdot (f(x, (n-1)/2))^2 & \text{if } n > 0, n \equiv 1 \pmod 2 \\
\frac{1}{f(x, |n|)} & \text{if } n < 0 
\end{cases}
$$

### Schleifeninvariante
Für die iterative Implementierung seien $r_i$ das Ergebnis, $b_i$ die Basis und $e_i$ der Exponent in Iteration $i$. Der Algorithmus erhält die folgende Invariante aufrecht:
$$x^n = r_i \cdot b_i^{e_i}$$
Zu Beginn gilt $r_0 = 1, b_0 = x, e_0 = n$. In jedem Schritt $i$ wird der Exponent $e_i$ halbiert ($e_{i+1} = \lfloor e_i / 2 \rfloor$). Wenn $e_i$ ungerade ist, wird das Ergebnis aktualisiert zu $r_{i+1} = r_i \cdot b_i$ und die Basis quadriert zu $b_{i+1} = b_i^2$. Die Invariante bleibt erhalten, da:
$$r_i \cdot b_i^{e_i} = (r_i \cdot b_i) \cdot (b_i^2)^{(e_i-1)/2} = r_i \cdot b_i^{e_i}$$

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität wird durch die Anzahl der Iterationen bestimmt, die erforderlich sind, um den Exponenten $n$ auf 0 zu reduzieren. Da der Algorithmus in jeder Iteration eine Rechts-Shift-Operation auf $n$ durchführt (äquivalent zu $n \leftarrow \lfloor n/2 \rfloor$), wird die Anzahl der Iterationen $T(n)$ durch die folgende Rekurrenz bestimmt:
$$T(n) = T(\lfloor n/2 \rfloor) + O(1)$$
Nach dem Master-Theorem (Fall 2), wobei $a=1, b=2, f(n)=O(1)$, erhalten wir:
$$T(n) = \Theta(\log_2 n)$$
Somit beträgt die Zeitkomplexität $O(\log n)$.

### Platzkomplexität
*   **Rekursive Implementierung:** Die Platzkomplexität wird durch die Tiefe des Call Stacks bestimmt. Da die Problemgröße in jedem rekursiven Schritt halbiert wird, beträgt die Tiefe des Rekursionsbaums $\lceil \log_2 n \rceil$. Daher liegt die zusätzliche Platzkomplexität bei $O(\log n)$.
*   **Iterative Implementierung:** Der iterative Ansatz verwendet eine konstante Anzahl an Variablen ($r, b, e$), unabhängig von der Größe von $n$. Folglich beträgt die zusätzliche Platzkomplexität $O(1)$.

*Hinweis: Im Kontext des vorgestellten Algorithmus wird der iterative Ansatz aufgrund seiner Platzoptimalität bevorzugt, obwohl die rekursive Definition der Standard für die theoretische Analyse nach dem Divide-and-Conquer-Prinzip bleibt.*