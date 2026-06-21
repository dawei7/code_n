# Formale mathematische Spezifikation: Fibonacci Search

## 1. Definitionen und Notation

Sei $A = [a_0, a_1, \dots, a_{n-1}]$ eine Sequenz von Elementen aus einer total geordneten Menge $(\mathcal{X}, \le)$, sodass $a_i \le a_{i+1}$ für alle $0 \le i < n-1$ gilt. Sei $x \in \mathcal{X}$ der gesuchte Zielwert.

Wir definieren die Fibonacci-Folge $\{F_k\}_{k \in \mathbb{N}_0}$ durch die Rekursionsgleichung:
$F_0 = 0, F_1 = 1, F_k = F_{k-1} + F_{k-2}$ für $k \ge 2$.

Der Algorithmus operiert auf einem Zustandsraum $\mathcal{S} \subseteq \mathbb{N}_0^3 \times \mathbb{Z} \times \mathbb{Z}$, wobei ein Zustand durch das Tupel $(F_k, F_{k-1}, F_{k-2}, \text{offset}, n)$ definiert ist.
- $n \in \mathbb{N}$ ist die Länge des Array.
- $k$ ist der Index, sodass $F_k$ die kleinste Fibonacci-Zahl ist, die $F_k \ge n$ erfüllt.
- $\text{offset} \in \{-1, 0, \dots, n-2\}$ repräsentiert den Index unmittelbar vor dem aktuellen Such-Teilintervall.

Die Ausgabe ist eine Funktion $f: \mathcal{X}^n \times \mathcal{X} \to \{-1, 0, \dots, n-1\}$, definiert als:
$f(A, x) = \begin{cases} i & \text{falls } a_i = x \\ -1 & \text{falls } \forall i, a_i \neq x \end{cases}$

## 2. Algebraische Charakterisierung

Der Algorithmus erhält die Schleifeninvariante aufrecht, dass das Ziel $x$, falls vorhanden, innerhalb des Indexbereichs $(\text{offset}, \text{offset} + F_k]$ liegt. Die Suche partitioniert den aktuellen Bereich der Länge $F_k$ in zwei Teilintervalle der Längen $F_{k-1}$ und $F_{k-2}$, wobei $F_k = F_{k-1} + F_{k-2}$ gilt.

Sei $i = \min(\text{offset} + F_{k-2}, n-1)$. Die Übergangslogik wird durch die Trichotomie-Eigenschaft der geordneten Menge $\mathcal{X}$ bestimmt:

1. **Fall $a_i < x$:** Das Ziel muss im Intervall $(\text{offset} + F_{k-2}, \text{offset} + F_k]$ liegen. Wir aktualisieren:
   $\text{offset}' = i$
   $F_k' = F_{k-1}, \quad F_{k-1}' = F_{k-2}, \quad F_{k-2}' = F_{k-1} - F_{k-2} = F_{k-3}$
   
2. **Fall $a_i > x$:** Das Ziel muss im Intervall $(\text{offset}, \text{offset} + F_{k-2}]$ liegen. Wir aktualisieren:
   $\text{offset}' = \text{offset}$
   $F_k' = F_{k-2}, \quad F_{k-1}' = F_{k-3}, \quad F_{k-2}' = F_{k-2} - F_{k-3} = F_{k-4}$

3. **Fall $a_i = x$:** Die Suche terminiert mit dem Index $i$.

Die Schleife terminiert, wenn $F_k \le 1$. Die Korrektheit beruht auf der Eigenschaft, dass der Suchraum um einen Faktor reduziert wird, der mit dem goldenen Schnitt $\phi = \frac{1+\sqrt{5}}{2}$ zusammenhängt, spezifisch $F_{k-2} \approx \frac{F_k}{\phi^2}$, was sicherstellt, dass die Intervallgröße strikt abnimmt.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus führt pro Iteration eine konstante Anzahl an Additionen und Subtraktionen aus. Die Anzahl der Iterationen $T(n)$ wird durch die Anzahl der Schritte bestimmt, die erforderlich sind, um $F_k$ auf 1 zu reduzieren.

Gegeben sei die Binet-Formel $F_k = \frac{\phi^k - \psi^k}{\sqrt{5}}$, wobei $\phi = \frac{1+\sqrt{5}}{2}$ und $\psi = \frac{1-\sqrt{5}}{2}$. Da $|\psi| < 1$, gilt $F_k \approx \frac{\phi^k}{\sqrt{5}}$.
Setzen wir $F_k \ge n$, erhalten wir $k \approx \log_\phi(n\sqrt{5})$.
Da jede Iteration den Index $k$ um mindestens 1 reduziert, beträgt die Anzahl der Iterationen $O(\log_\phi n)$. Durch die Basiswechselformel gilt $\log_\phi n = \frac{\ln n}{\ln \phi}$, somit:
$T(n) = O(\log n)$.

### Platzkomplexität
Der Algorithmus verwaltet eine feste Menge an Variablen: $\{F_k, F_{k-1}, F_{k-2}, \text{offset}, i\}$. Keine dieser Variablen skaliert mit der Eingabegröße $n$ hinsichtlich der Speicherallokation (sie werden in Registern fester Breite gespeichert).
Daher ist die zusätzliche Platzkomplexität:
$S(n) = O(1)$.