# Formale mathematische Spezifikation: Überprüfung auf Zweierpotenz

## 1. Definitionen und Notation

Um ein rigoroses Fundament für den Algorithmus zu etablieren, definieren wir die mathematischen Domänen, Repräsentationsschemata und Operatoren, die zur Charakterisierung von Eingabe, Ausgabe und Zustandsraum verwendet werden.

### 1.1 Mathematische Domänen und Mengen
* Sei $\mathbb{Z}$ die Menge aller ganzen Zahlen.
* Sei $\mathbb{Z}^+$ die Menge der streng positiven ganzen Zahlen, $\{n \in \mathbb{Z} \mid n > 0\}$.
* Sei $\mathbb{N}_0$ die Menge der nicht-negativen ganzen Zahlen, $\{0, 1, 2, \dots\}$.
* Sei $\mathbb{B} = \{\text{True}, \text{False}\}$ die boolesche Domäne.
* Sei $\mathcal{P}_2 \subset \mathbb{Z}^+$ die Menge aller Zweierpotenzen, formal definiert als:
  $$\mathcal{P}_2 = \{ 2^x \mid x \in \mathbb{N}_0 \}$$

### 1.2 Binäre Repräsentation
Für jede positive ganze Zahl $n \in \mathbb{Z}^+$ existiert eine eindeutige binäre Repräsentation der Form:
$$n = \sum_{i=0}^{k} b_i 2^i$$
wobei $k = \lfloor \log_2 n \rfloor$, $b_i \in \{0, 1\}$ für alle $0 \le i \le k$ und das höchstwertige Bit $b_k = 1$ ist.

Wir bezeichnen die Sequenz der binären Koeffizienten von $n$ als Bit-Vektor $\mathbf{b}(n) = (b_k, b_{k-1}, \dots, b_0)_2$.

### 1.3 Bitweise Operatoren
Sei $\&$ der bitweise AND-Operator. Für zwei beliebige nicht-negative ganze Zahlen $u, v \in \mathbb{N}_0$ mit binären Entwicklungen $u = \sum_{i=0}^{\infty} u_i 2^i$ und $v = \sum_{i=0}^{\infty} v_i 2^i$ (wobei $u_i, v_i \in \{0, 1\}$ und nur endlich viele Koeffizienten ungleich null sind), ist die bitweise AND-Operation algebraisch definiert als:
$$u \ \& \ v = \sum_{i=0}^{\infty} (u_i \cdot v_i) 2^i$$
wobei $u_i \cdot v_i$ die Standardmultiplikation in $\{0, 1\}$ darstellt, was äquivalent zur logischen Konjunktion $u_i \land v_i$ ist.

---

## 2. Algebraische Charakterisierung

Der Algorithmus evaluiert eine Entscheidungsfunktion $f: \mathbb{Z} \to \mathbb{B}$, definiert durch:
$$f(n) = (n > 0) \land \big( (n \ \& \ (n - 1)) == 0 \big)$$

### Theorem 1 (Korrektheit der Zweierpotenz-Überprüfung)
Für jede ganze Zahl $n \in \mathbb{Z}$ gilt:
$$f(n) = \text{True} \iff n \in \mathcal{P}_2$$

### Beweis
Wir beweisen diese Äquivalenz durch Partitionierung der Domäne $\mathbb{Z}$ in zwei Fälle: $n \le 0$ und $n > 0$.

#### Fall 1: $n \le 0$
* **Von links nach rechts ($\implies$):** Wenn $n \le 0$, evaluiert die Klausel $(n > 0)$ zu $\text{False}$. Aufgrund der Definition der logischen Konjunktion ist $f(n) = \text{False}$.
* **Von rechts nach links ($\impliedby$):** Per Definition ist $\mathcal{P}_2 = \{2^x \mid x \in \mathbb{N}_0\}$. Da $2^x > 0$ für alle $x \in \mathbb{R}$ gilt, folgt daraus $\mathcal{P}_2 \subset \mathbb{Z}^+$. Somit gilt für $n \le 0$, dass $n \notin \mathcal{P}_2$.
* Daher gilt das Theorem trivialerweise für alle $n \le 0$.

#### Fall 2: $n > 0$
Für $n \in \mathbb{Z}^+$ evaluiert die Klausel $(n > 0)$ zu $\text{True}$. Die Entscheidungsfunktion vereinfacht sich zu:
$$f(n) = \text{True} \iff (n \ \& \ (n - 1)) = 0$$
Wir müssen zeigen, dass für jedes $n \in \mathbb{Z}^+$ gilt: $(n \ \& \ (n - 1)) = 0 \iff n \in \mathcal{P}_2$.

Sei die eindeutige binäre Repräsentation von $n$:
$$n = \sum_{i=0}^{k} b_i 2^i \quad \text{mit } b_k = 1$$
Sei $j$ der Index des niedrigstwertigen gesetzten Bits (das rechteste $1$-Bit) von $n$:
$$j = \min \{ i \in \mathbb{N}_0 \mid b_i = 1 \}$$
Per Definition von $j$ haben wir $b_j = 1$ und $b_i = 0$ für alle $0 \le i < j$. Wir können $n$ zerlegen als:
$$n = \sum_{i=j+1}^{k} b_i 2^i + 2^j$$

Betrachten wir nun die algebraische Repräsentation von $n - 1$:
$$n - 1 = \sum_{i=j+1}^{k} b_i 2^i + 2^j - 1$$
Unter Verwendung der Identität für die geometrische Reihe $2^j - 1 = \sum_{i=0}^{j-1} 2^i$ substituieren wir und erhalten:
$$n - 1 = \sum_{i=j+1}^{k} b_i 2^i + \sum_{i=0}^{j-1} 1 \cdot 2^i$$

Sei $c_i(x)$ der $i$-te binäre Koeffizient einer ganzen Zahl $x$. Aus unseren Ausdrücken für $n$ und $n-1$ extrahieren wir die jeweiligen Koeffizienten:
$$c_i(n) = \begin{cases} 
b_i & \text{falls } i > j \\ 
1 & \text{falls } i = j \\ 
0 & \text{falls } i < j 
\end{cases}$$

$$c_i(n - 1) = \begin{cases} 
b_i & \text{falls } i > j \\ 
0 & \text{falls } i = j \\ 
1 & \text{falls } i < j 
\end{cases}$$

Unter Anwendung der Definition des bitweisen AND-Operators sind die Koeffizienten von $n \ \& \ (n - 1)$ gegeben durch:
$$c_i(n \ \& \ (n - 1)) = c_i(n) \cdot c_i(n - 1)$$

Die Auswertung dieses Produkts für jedes Intervall von $i$:
1. Für $i > j$: $c_i(n \ \& \ (n - 1)) = b_i \cdot b_i = b_i$ (da $b_i \in \{0, 1\}$).
2. Für $i = j$: $c_i(n \ \& \ (n - 1)) = 1 \cdot 0 = 0$.
3. Für $i < j$: $c_i(n \ \& \ (n - 1)) = 0 \cdot 1 = 0$.

Die Rekonstruktion des ganzzahligen Wertes der bitweisen AND-Operation ergibt:
$$n \ \& \ (n - 1) = \sum_{i=j+1}^{k} b_i 2^i$$

Wir evaluieren nun die Bedingung, unter der dieser Wert gleich $0$ ist:
$$n \ \& \ (n - 1) = 0 \iff \sum_{i=j+1}^{k} b_i 2^i = 0$$
Da $2^i > 0$ und $b_i \ge 0$ für alle $i$ gilt, ist die Summe genau dann null, wenn:
$$b_i = 0 \quad \forall i \in \{j+1, \dots, k\}$$

Diese Bedingung impliziert, dass $j$ der einzige Index ist, für den $b_i = 1$ gilt. Somit ist $k = j$ und die binäre Entwicklung von $n$ reduziert sich auf:
$$n = 2^j$$
Da $j \in \mathbb{N}_0$, ist dies äquivalent zur Aussage, dass $n \in \mathcal{P}_2$.

Umgekehrt, falls $n \notin \mathcal{P}_2$, muss mindestens ein Index $m > j$ existieren, sodass $b_m = 1$. Dies garantiert:
$$\sum_{i=j+1}^{k} b_i 2^i \ge 2^m > 0$$
was impliziert, dass $n \ \& \ (n - 1) \neq 0$.

Damit ist der Beweis vollständig. $\blacksquare$

---

## 3. Komplexitätsanalyse

### 3.1 Zeitkomplexität
Um die Zeitkomplexität formal zu analysieren, definieren wir unser Ausführungsmodell unter dem **Word RAM Model of Computation**. In diesem Modell operiert die CPU auf Wörtern der Größe $w$ Bits, wobei $w \ge \log_2 n$. Grundlegende arithmetische Operationen (Addition, Subtraktion) und bitweise Operationen (AND, Vergleiche) auf $w$-Bit-Wörtern werden in $O(1)$ Zeit ausgeführt.

Sei $T(n)$ die Anzahl der primitiven Operationen für die Eingabe $n$:
1. **Relationaler Vergleich ($n > 0$):** Erfordert 1 Vergleichsoperation.
2. **Arithmetische Subtraktion ($n - 1$):** Erfordert 1 Subtraktionsoperation.
3. **Bitweise Konjunktion ($n \ \& \ (n - 1)$):** Erfordert 1 bitweise AND-Operation.
4. **Gleichheitsvergleich ($== 0$):** Erfordert 1 Vergleichsoperation.
5. **Logische Konjunktion ($\land$):** Erfordert höchstens 1 logische Operation (bei Kurzschlussauswertung).

Somit ist die Gesamtzahl der Operationen durch eine Konstante $C \le 5$ beschränkt.
$$T(n) \le C \cdot \tau = \Theta(1)$$
wobei $\tau$ die Taktzykluskosten einer Instruktion auf Wortebene sind.

#### Verallgemeinerung auf beliebige Präzision
Wenn $n$ eine Ganzzahl mit beliebiger Präzision ist, die unter Verwendung von $L = \Theta(\log n)$ Bits dargestellt wird:
* Die Subtraktion $n - 1$ erfordert im Schlechtesten Fall $\Theta(L)$ Bit-Operationen.
* Das bitweise AND $n \ \& \ (n - 1)$ erfordert $\Theta(L)$ Bit-Operationen.
* Unter diesem Bit-Komplexitätsmodell ist die Zeitkomplexität $\Theta(L) = \Theta(\log n)$. Für standardmäßige, hardwareseitig unterstützte Ganzzahlen fester Breite (z. B. 32-Bit oder 64-Bit) bleibt die Komplexität jedoch strikt $\Theta(1)$.

### 3.2 Platzkomplexität
Sei $S(n)$ die gesamte Platzkomplexität des Algorithmus, unterteilt in Eingabespeicher, Hilfsspeicher und Stack-Speicher.

* **Eingabespeicher:** Der Algorithmus nimmt eine einzelne Ganzzahl $n$ entgegen, die in einem einzelnen Maschinenwort der Größe $w$ Bits dargestellt ist. Somit beträgt der Eingabespeicher $O(1)$ Wörter.
* **Hilfsspeicher ($A(n)$):** Der Algorithmus allokiert keinen dynamischen Speicher, noch skaliert er seine Variablen mit der Eingabegröße. Er benötigt nur eine konstante Anzahl an Registern, um Zwischenzustände zu speichern:
  $$\mathcal{S}_{\text{intermediate}} = \{ n - 1, \ n \ \& \ (n-1), \ \text{boolesche Flags} \}$$
  Dies erfordert $O(1)$ Hilfsspeicher.
* **Call Stack Speicher:** Die Ausführung ist nicht-rekursiv, was zu einer Call-Stack-Tiefe von $O(1)$ führt.

Daher ist die Platzkomplexität für den Hilfsspeicher:
$$A(n) = \Theta(1)$$