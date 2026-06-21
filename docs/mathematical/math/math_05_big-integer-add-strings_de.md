# Formale mathematische Spezifikation: Add Strings (Big Integer Addition)

## 1. Definitionen und Notation

Sei $\Sigma = \{'0', '1', \dots, '9'\}$ das Alphabet der Dezimalziffern. Eine nicht-negative ganze Zahl $X$ wird als String $S_X \in \Sigma^n$ dargestellt, wobei $n$ die Länge des Strings ist. Wir definieren eine Abbildungsfunktion $\phi: \Sigma \to \{0, 1, \dots, 9\}$, sodass $\phi(d)$ den ganzzahligen Wert des Zeichens $d$ zurückgibt.

Der Wert des Strings $S_X = d_{n-1}d_{n-2}\dots d_0$ ist durch die Stellenwertschreibweise gegeben:
$$V(S_X) = \sum_{i=0}^{n-1} \phi(d_i) \cdot 10^i$$

**Eingaben:** Zwei Strings $A \in \Sigma^N$ und $B \in \Sigma^M$.
**Ausgabe:** Ein String $R \in \Sigma^L$, sodass $V(R) = V(A) + V(B)$.
**Zustandsraum:** Der Algorithmus verwaltet ein Zustandstupel $(i, c) \in \mathbb{N}_0 \times \{0, 1\}$, wobei $i$ die aktuell verarbeitete Ziffernposition (Index) repräsentiert und $c$ den Übertragswert aus der vorherigen Position darstellt.

## 2. Algebraische Charakterisierung

Der Additionsvorgang ist durch die Propagation eines Übertrags $c_i$ durch jede Dezimalstelle $i$ definiert. Seien $a_i$ und $b_i$ die Ziffern an der Position $i$ für die Strings $A$ bzw. $B$, wobei $a_i = 0$ gilt, falls $i \ge N$, und $b_i = 0$, falls $i \ge M$.

Für jede Position $i \in \{0, 1, \dots, \max(N, M)-1\}$ sind die Summe $s_i$ und der Übertrag $c_{i+1}$ durch die folgenden Rekursionsgleichungen definiert:

1. **Summation:** $s_i = \phi(a_i) + \phi(b_i) + c_i$
2. **Ziffernextraktion:** $r_i = s_i \pmod{10}$
3. **Übertragspropagation:** $c_{i+1} = \lfloor s_i / 10 \rfloor$

**Induktionsanfang:** $c_0 = 0$.
**Terminierung:** Der Prozess terminiert am Index $k = \max(N, M)$, sodass $c_k = 0$. Falls $c_k > 0$, wird der Ergebnis-String $R$ um die Ziffer $\phi^{-1}(c_k)$ erweitert.

**Schleifeninvariante:** Zu Beginn jeder Iteration $i$ ist die partielle Summe der verarbeiteten Suffixe von $A$ und $B$ zuzüglich des Übertrags $c_i$ kongruent zur Gesamtsumme modulo $10^i$. Formal gilt, wenn $A^{(i)}$ und $B^{(i)}$ die durch die letzten $i$ Ziffern von $A$ und $B$ repräsentierten ganzen Zahlen sind:
$$V(A^{(i)}) + V(B^{(i)}) + c_i \cdot 10^i = \sum_{j=0}^{i-1} r_j \cdot 10^j + c_i \cdot 10^i$$

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus iteriert genau einmal durch die Ziffern der Eingabe-Strings. Seien $N = |A|$ und $M = |B|$. Die Anzahl der Iterationen $T$ wird durch die Länge des längeren Strings bestimmt:
$$T = \max(N, M)$$
In jeder Iteration $i$ sind die ausgeführten Operationen (Integer-Konvertierung, Addition, Modulo und Division) konstante Zeitoperationen, $O(1)$. Die abschließenden Umkehr- und Zusammenfügungsoperationen benötigen $O(L)$ Zeit, wobei $L$ die Länge des Ergebnis-Strings ist. Da $L \le \max(N, M) + 1$ gilt, ergibt sich die gesamte Zeitkomplexität zu:
$$T(N, M) = \sum_{i=1}^{\max(N, M)} O(1) + O(\max(N, M)) = O(\max(N, M))$$

### Platzkomplexität
Der zusätzliche Speicherbedarf wird primär durch die Speicherung der Ergebnisziffern vor der finalen String-Konstruktion dominiert.
1. **Result Array:** Wir speichern maximal $\max(N, M) + 1$ Ziffern.
2. **Pointer und Übertrag:** Wir speichern eine konstante Anzahl an Integer-Variablen ($i, c, s, da, db$), die $O(1)$ Platz beanspruchen.

Somit ergibt sich die gesamte Platzkomplexität zu:
$$S(N, M) = O(\max(N, M) + 1) = O(\max(N, M))$$
Dies ist optimal, da wir den Ausgabe-String speichern müssen, dessen Länge proportional zur Eingabegröße ist.