# Formale mathematische Spezifikation: Karatsuba-Multiplikation

## 1. Definitionen und Notation

Seien $X, Y \in \mathbb{Z}^+$ zwei positive ganze Zahlen, die zur Basis $B$ (typischerweise $B=10$) dargestellt werden. Sei $n$ die Anzahl der Ziffern der größeren Zahl, definiert als $n = \max(\lfloor \log_B X \rfloor + 1, \lfloor \log_B Y \rfloor + 1)$.

Wir definieren die Zerlegung von $X$ und $Y$ relativ zu einem Teilungspunkt $m = \lceil n/2 \rceil$:
- $X = A \cdot B^m + B_{low}$
- $Y = C \cdot B^m + D_{low}$

Wobei:
- $A = \lfloor X / B^m \rfloor$ und $B_{low} = X \pmod{B^m}$
- $C = \lfloor Y / B^m \rfloor$ und $D_{low} = Y \pmod{B^m}$

Die Definitionsmenge des Algorithmus ist die Menge der natürlichen Zahlen $\mathbb{N}$, und die Zielmenge ist das Produkt $P = X \cdot Y$. Der Zustandsraum $\mathcal{S}$ wird durch den Rekursionsbaum definiert, der durch die rekursive Zerlegung der Operanden erzeugt wird, bis der Basisfall $n < 2$ erreicht ist.

## 2. Algebraische Charakterisierung

Das Produkt $P = X \cdot Y$ wird über das Distributivgesetz expandiert:
$$P = (A \cdot B^m + B_{low})(C \cdot B^m + D_{low})$$
$$P = (A \cdot C) \cdot B^{2m} + (A \cdot D_{low} + B_{low} \cdot C) \cdot B^m + (B_{low} \cdot D_{low})$$

Seien die drei fundamentalen Produkte wie folgt definiert:
1. $Z_2 = A \cdot C$
2. $Z_0 = B_{low} \cdot D_{low}$
3. $Z_1 = (A + B_{low}) \cdot (C + D_{low})$

Durch Ausmultiplizieren von $Z_1$ beobachten wir:
$$Z_1 = AC + AD_{low} + B_{low}C + B_{low}D_{low}$$
$$Z_1 = Z_2 + (AD_{low} + B_{low}C) + Z_0$$

Somit kann der mittlere Term $(AD_{low} + B_{low}C)$ isoliert werden, ohne die einzelnen Kreuzprodukte explizit berechnen zu müssen:
$$(AD_{low} + B_{low}C) = Z_1 - Z_2 - Z_0$$

Durch Einsetzen in die Expansion von $P$ erhalten wir die Karatsuba-Identität:
$$P = Z_2 \cdot B^{2m} + (Z_1 - Z_2 - Z_0) \cdot B^m + Z_0$$

Diese Identität reduziert die Anzahl der rekursiven Multiplikationen von vier auf drei, was den fundamentalen algebraischen Übergang darstellt, der die Effizienz des Algorithmus bestimmt.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus folgt einem Divide-and-Conquer-Paradigma. Die Arbeit, die auf jeder Ebene der Rekursion verrichtet wird, besteht aus Additionen, Subtraktionen und Verschiebungen (Multiplikationen mit Potenzen von $B$), was $O(n)$ Operationen entspricht. Die Rekursionsgleichung für die Zeitkomplexität $T(n)$ lautet:
$$T(n) = 3T(n/2) + O(n)$$

Unter Anwendung des Master-Theorems für Divide-and-Conquer-Rekursionen der Form $T(n) = aT(n/b) + f(n)$:
- $a = 3$
- $b = 2$
- $f(n) = O(n^1)$

Da $\log_b a = \log_2 3 \approx 1.585$ und $f(n) = O(n^c)$ mit $c < \log_b a$, wird die Komplexität von den rekursiven Aufrufen dominiert:
$$T(n) = \Theta(n^{\log_2 3}) \approx O(n^{1.585})$$

### Platzkomplexität
Die Platzkomplexität $S(n)$ wird durch die maximale Tiefe des Rekursions-Stacks und den für die Zwischenprodukte $Z_0, Z_1, Z_2$ benötigten zusätzlichen Speicher bestimmt.

1. **Rekursionstiefe:** Die Problemgröße halbiert sich bei jedem Schritt, was zu einer Tiefe des Rekursionsbaums von $d = \lceil \log_2 n \rceil$ führt.
2. **Stack-Frame:** Jeder Frame speichert eine konstante Anzahl an Variablen ($A, B_{low}, C, D_{low}, Z_0, Z_1, Z_2$).
3. **Zusätzlicher Speicher:** Während die Gesamtzahl der über alle Ebenen des Stacks gespeicherten Bits $O(n)$ beträgt, ist der *aktive* Speicher an jedem Punkt der Tiefensuche $O(n)$ aufgrund der Speicherung der Zwischensummen. Wenn wir jedoch die Stack-Tiefe spezifisch als primäre Einschränkung für den zusätzlichen Speicher betrachten, liegt diese bei $O(\log n)$.

Somit beträgt die zusätzliche Platzkomplexität $O(n)$ für die Speicherung der Zahlen auf jeder Ebene, aber die Tiefe des Rekursions-Stacks ist $O(\log n)$. In Standardimplementierungen beträgt die gesamte Platzkomplexität $O(n)$.