# Formale mathematische Spezifikation: Miller-Rabin-Primzahltest

## 1. Definitionen und Notation

Sei $n \in \mathbb{Z}^+$ eine ungerade Ganzzahl mit $n > 3$. Wir definieren das Problem des Primzahltests als die Bestimmung des Prädikats $\text{is\_prime}(n) : \mathbb{Z}^+ \to \{0, 1\}$.

*   **Zerlegung von $n-1$:** Da $n$ ungerade ist, ist $n-1$ gerade. Wir definieren die eindeutige Faktorisierung $n-1 = 2^s \cdot d$, wobei $s \in \mathbb{Z}^+$, $d \in \mathbb{Z}^+$ und $d \equiv 1 \pmod 2$.
*   **Zeugenmenge (Witness Set):** Sei $a \in \mathbb{Z}$ eine Basis, sodass $2 \le a \le n-2$. Wir definieren $a$ als einen *Miller-Rabin-Zeugen* für die Zusammengesetztheit von $n$, wenn die folgenden Bedingungen erfüllt sind:
    1. $a^d \not\equiv 1 \pmod n$
    2. $a^{2^r \cdot d} \not\equiv -1 \pmod n$ für alle $0 \le r < s$.
*   **Zustandsraum:** Der Algorithmus operiert innerhalb der multiplikativen Gruppe $(\mathbb{Z}/n\mathbb{Z})^\times$. Der Zustand bei jeder Iteration $i \in \{1, \dots, k\}$ ist durch das Tupel $(a_i, x_{i,r})$ definiert, wobei $x_{i,r} = a_i^{2^r \cdot d} \pmod n$.

## 2. Algebraische Charakterisierung

Die Korrektheit des Miller-Rabin-Tests beruht auf der Kontraposition des folgenden Theorems:

**Theorem:** Wenn $n$ eine ungerade Primzahl ist, dann erfüllt für jedes $a$ mit $\gcd(a, n) = 1$ die Folge $x_r = a^{2^r \cdot d} \pmod n$ für $0 \le r < s$:
1. $x_0 \equiv 1 \pmod n$, ODER
2. Es existiert ein $r \in \{0, 1, \dots, s-1\}$, sodass $x_r \equiv -1 \pmod n$.

**Beweisskizze:** Nach dem kleinen fermatschen Satz gilt $a^{n-1} \equiv 1 \pmod n$. Da $n$ prim ist, besitzt der Körper $\mathbb{Z}/n\mathbb{Z}$ nur zwei Quadratwurzeln von $1$, nämlich $1$ und $-1$. Die Folge $x_r$ wird durch wiederholtes Quadrieren gebildet. Wenn $x_0 \not\equiv 1$, dann muss dem ersten $r$, für das $x_r \equiv 1$ gilt, ein $x_{r-1}$ vorausgegangen sein, sodass $x_{r-1}^2 \equiv 1$. Aufgrund der Eigenschaft von Körpern muss $x_{r-1}$ gleich $-1 \equiv n-1$ sein.

**Entscheidungsregel:**
Für eine gewählte Basis $a$ wird $n$ als zusammengesetzt erklärt, wenn:
$$a^d \not\equiv 1 \pmod n \land \forall r \in \{0, \dots, s-1\} : a^{2^r \cdot d} \not\equiv -1 \pmod n$$
Andernfalls wird $n$ als *starke wahrscheinliche Primzahl* zur Basis $a$ deklariert. Die Wahrscheinlichkeit, dass ein zusammengesetztes $n$ eine einzelne Runde besteht, ist durch $\frac{1}{4}$ beschränkt (Monier-Rabin-Theorem). Für $k$ unabhängige Durchläufe ist die Fehlerwahrscheinlichkeit beschränkt durch:
$$P(\text{falsch positiv}) \le 4^{-k}$$

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus führt $k$ unabhängige Runden durch. Jede Runde besteht aus:
1. **Modulare Exponentiation:** Berechnung von $a^d \pmod n$ unter Verwendung des Algorithmus zur binären Exponentiation (Square-and-Multiply). Dies erfordert $O(\log d)$ modulare Multiplikationen. Da $d < n$, entspricht dies $O(\log n)$ Multiplikationen.
2. **Quadrierungsfolge:** Höchstens $s-1$ Quadrierungen, wobei $s < \log_2 n$. Dies entspricht $O(\log n)$ modularen Multiplikationen.

Da jede modulare Multiplikation zweier $m$-Bit-Ganzzahlen (wobei $m = \log_2 n$) bei Verwendung der Standardmultiplikation $O(m^2)$ Zeit benötigt (oder $O(m \log m \log \log m)$ bei Verwendung von Schönhage-Strassen), beträgt die Komplexität pro Runde $O(\log^3 n)$.
Summiert über $k$ Runden ergibt sich die gesamte Zeitkomplexität zu:
$$T(n, k) = O(k \cdot \log^3 n)$$

### Platzkomplexität
Der Algorithmus verwaltet eine konstante Anzahl an Variablen ($s, d, a, x, r$) unabhängig von der Größe von $n$. Jede Variable benötigt $O(\log n)$ Bits Speicherplatz. Somit ist die zusätzliche Platzkomplexität:
$$S(n) = O(\log n)$$
Im Kontext der Wort-RAM-Modell-Komplexität, bei der ein Wort $\log n$ Bits hält, ist die Platzkomplexität:
$$S(n) = O(1)$$