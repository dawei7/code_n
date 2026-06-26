# Formale mathematische Spezifikation: Die Potenzsumme

## 1. Definitionen und Notation

Sei $X \in \mathbb{Z}^+$ die Zielzahl und $N \in \mathbb{Z}^+$ der Exponent. Wir definieren die Menge der infrage kommenden natürlichen Zahlen als $\mathcal{C} = \{i \in \mathbb{Z}^+ \mid i^N \leq X\}$. Die Kardinalität dieser Menge ist $M = \lfloor X^{1/N} \rfloor$.

Das Problem besteht darin, die Anzahl der Teilmengen $S \subseteq \mathcal{C}$ zu finden, für die die Summe der $N$-ten Potenzen der Elemente in $S$ gleich $X$ ist. Formal definieren wir den Lösungsraum als:
$$\mathcal{F} = \left\{ S \subseteq \mathcal{C} : \sum_{s \in S} s^N = X \right\}$$
Das Ziel ist die Berechnung der Kardinalität $|\mathcal{F}|$.

Wir definieren den Zustand unseres rekursiven Prozesses als Tupel $(t, i)$, wobei:
*   $t \in \mathbb{Z}_{\geq 0}$ die verbleibende Zielsumme ist.
*   $i \in \mathbb{Z}^+$ die aktuelle Kandidatenbasis ist, die für die Aufnahme in die Teilmenge in Betracht gezogen wird.

## 2. Algebraische Charakterisierung

Der Algorithmus wird durch die Funktion $f(t, i)$ definiert, welche die Anzahl der Möglichkeiten zurückgibt, $t$ als Summe eindeutiger $N$-ter Potenzen unter Verwendung einer Teilmenge von $\{i, i+1, \dots, M\}$ auszudrücken. Die Rekursionsgleichung ist definiert als:

$$f(t, i) = 
\begin{cases} 
1 & \text{falls } t = 0 \\
0 & \text{falls } t < 0 \lor i^N > t \\
f(t - i^N, i + 1) + f(t, i + 1) & \text{sonst}
\end{cases}$$

**Korrektheitsinvarianten:**
1.  **Vollständigkeit:** Der Verzweigungsfaktor $f(t - i^N, i + 1) + f(t, i + 1)$ repräsentiert die Partition der Potenzmenge von $\mathcal{C}$ in zwei disjunkte Mengen: diejenigen, die $i$ enthalten, und diejenigen, die $i$ nicht enthalten.
2.  **Terminierung:** Da $i$ in jedem rekursiven Aufruf streng monoton wächst ($i \to i+1$) und der Definitionsbereich durch $M = \lfloor X^{1/N} \rfloor$ beschränkt ist, ist die Rekursionstiefe endlich, was die Terminierung des Algorithmus sicherstellt.
3.  **Eindeutigkeit:** Die Einschränkung $i+1$ im Rekursionsschritt stellt sicher, dass jedes Element $i \in \mathcal{C}$ höchstens einmal berücksichtigt wird, was die Anforderung an eindeutige natürliche Zahlen erfüllt.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus durchläuft einen binären Rekursionsbaum. Sei $T(i)$ die Anzahl der Knoten im Rekursionsbaum, beginnend beim Index $i$. Die Rekurrenz für die Anzahl der Operationen lautet:
$$T(i) = 1 + T(i+1) + T(i+1) = 2T(i+1) + 1$$
Unter Berücksichtigung des Induktionsanfangs $T(M+1) = 1$ handelt es sich um eine lineare inhomogene Rekursionsgleichung. Durch Auflösung erhalten wir:
$$T(1) = \sum_{k=0}^{M} 2^k = 2^{M+1} - 1$$
Durch Einsetzen von $M = \lfloor X^{1/N} \rfloor$ ergibt sich die Zeitkomplexität zu $O(2^{X^{1/N}})$. Dies entspricht der Gesamtzahl der Teilmengen von $\mathcal{C}$, die im Schlechtesten Fall ausgewertet werden.

### Platzkomplexität
Die Platzkomplexität wird durch die maximale Tiefe des Rekursions-Stacks bestimmt. Im Schlechtesten Fall durchläuft der Algorithmus den Baum bis zu einer Tiefe von $M$.
*   **Zusätzlicher Speicherplatz:** Der Stack-Frame speichert die aktuellen Parameter $(t, i)$ sowie die Rücksprungadresse. Da jeder Frame $O(1)$ Platz beansprucht, ist der gesamte zusätzliche Speicherplatz proportional zur maximalen Tiefe des Rekursionsbaums.
*   **Gesamtspeicherplatz:** 
$$\text{Platz} = O(\text{Tiefe}) = O(M) = O(X^{1/N})$$
Somit beträgt die Platzkomplexität $O(X^{1/N})$, was der Höhe des Rekursionsbaums entspricht.