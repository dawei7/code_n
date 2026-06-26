# Formale mathematische Spezifikation: Karatsuba-Multiplikation

## 1. Definitionen und Notation

Sei $\mathbb{N}_0$ die Menge der nicht-negativen ganzen Zahlen. Wir definieren den Input als ein Paar von ganzen Zahlen $(x, y) \in \mathbb{N}_0 \times \mathbb{N}_0$. Sei $n$ die Anzahl der Ziffern der größeren ganzen Zahl in einer gewählten Basis $B$ (typischerweise $B=10$ oder $B=2^k$).

Wir stellen $x$ und $y$ zur Basis $B$ so dar, dass $x, y < B^n$ gilt. Für einen gewählten Teilungspunkt $m = \lfloor n/2 \rfloor$ definieren wir die Zerlegung von $x$ und $y$ wie folgt:
$$x = a \cdot B^m + b$$
$$y = c \cdot B^m + d$$
wobei $a, b, c, d \in \mathbb{N}_0$ so gewählt sind, dass $0 \le b, d < B^m$ gilt.

Das Ziel ist die Berechnung des Produkts $P = x \cdot y$. Der Zustandsraum $\mathcal{S}$ besteht aus den rekursiven Teilproblemen, die durch das Tupel $(a, b, c, d)$ auf jeder Ebene des Rekursionsbaums definiert sind.

## 2. Algebraische Charakterisierung

Das Produkt $P$ kann über das Distributivgesetz erweitert werden:
$$P = (a \cdot B^m + b)(c \cdot B^m + d) = ac \cdot B^{2m} + (ad + bc) \cdot B^m + bd$$

Der naive Divide-and-Conquer-Ansatz erfordert vier Multiplikationen: $ac, ad, bc, bd$. Karatsubas Erkenntnis besteht darin, die Anzahl der Multiplikationen durch Ausnutzung der folgenden Identität zu reduzieren:
$$(a + b)(c + d) = ac + ad + bc + bd$$

Seien die drei rekursiven Produkte wie folgt definiert:
1. $Z_0 = ac$
2. $Z_1 = bd$
3. $Z_2 = (a + b)(c + d)$

Der mittlere Term $(ad + bc)$ lässt sich durch die Linearkombination zurückgewinnen:
$$ad + bc = Z_2 - Z_0 - Z_1$$

Durch Einsetzen in die Erweiterung von $P$ erhalten wir die Karatsuba-Identität:
$$P = Z_0 \cdot B^{2m} + (Z_2 - Z_0 - Z_1) \cdot B^m + Z_1$$

Diese Formulierung ist für alle $x, y \in \mathbb{N}_0$ korrekt, da der Ring der ganzen Zahlen $\mathbb{Z}$ kommutativ und assoziativ ist, was sicherstellt, dass die algebraische Identität unabhängig von der Größe von $n$ gilt.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Ausführungszeit $T(n)$ des Algorithmus wird durch die Anzahl der rekursiven Aufrufe und den Overhead für Addition/Subtraktion bestimmt. Da der Algorithmus drei rekursive Multiplikationen auf Inputs der Größe $n/2$ durchführt und eine konstante Anzahl an Additionen und Subtraktionen (die $O(n)$ Zeit benötigen) ausführt, stellen wir die folgende Rekursionsgleichung auf:
$$T(n) = 3T(n/2) + O(n)$$

Unter Anwendung des **Master-Theorems** für Divide-and-Conquer-Rekursionen der Form $T(n) = aT(n/b) + f(n)$:
- Hier ist $a = 3$, $b = 2$ und $f(n) = O(n^1)$.
- Wir vergleichen $f(n)$ mit $n^{\log_b a} = n^{\log_2 3}$.
- Da $\log_2 3 \approx 1,585 > 1$ gilt, wird die Komplexität von den Blättern des Rekursionsbaums dominiert.
- Somit gilt $T(n) = \Theta(n^{\log_2 3}) \approx O(n^{1,585})$.

### Platzkomplexität
Die Platzkomplexität $S(n)$ wird durch die maximale Tiefe des Rekursions-Stacks und den für Zwischenergebnisse auf jeder Ebene benötigten zusätzlichen Speicher bestimmt.
1. **Rekursionstiefe:** Die Tiefe des Rekursionsbaums beträgt $\log_2 n$.
2. **Zusätzlicher Speicher:** Auf jeder Ebene der Rekursion speichern wir die Zwischenwerte $Z_0, Z_1, Z_2$ sowie die zerlegten Teile $a, b, c, d$. Diese benötigen $O(n)$ Speicher auf der obersten Ebene, $O(n/2)$ auf der nächsten und so weiter.
3. **Gesamtspeicher:** Die Summe des Speichers über alle Ebenen hinweg ist eine geometrische Reihe:
   $$S(n) = O(n) + O(n/2) + O(n/4) + \dots + O(1) = O(n) \sum_{i=0}^{\log n} \left(\frac{1}{2}\right)^i = O(n)$$
Somit beträgt die gesamte zusätzliche Platzkomplexität $O(n)$.