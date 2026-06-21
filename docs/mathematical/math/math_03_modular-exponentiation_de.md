# Formale mathematische Spezifikation: Modulare Exponentiation (Binäre Exponentiation)

## 1. Definitionen und Notation

Sei die Basis $b \in \mathbb{Z}$, der Exponent $e \in \mathbb{N}_0$ (wobei $\mathbb{N}_0 = \{0, 1, 2, \dots\}$) und der Modul $m \in \mathbb{Z}^+$. Wir definieren die Funktion der modularen Exponentiation $f: \mathbb{Z} \times \mathbb{N}_0 \times \mathbb{Z}^+ \to \mathbb{Z}_{m}$ als:
$$f(b, e, m) \equiv b^e \pmod m$$

Der Zustandsraum $\mathcal{S}$ des Algorithmus ist durch das Tripel $(r_i, b_i, e_i)$ definiert, wobei:
- $r_i \in \mathbb{Z}_m$ das akkumulierte Ergebnis in Iteration $i$ ist.
- $b_i \in \mathbb{Z}_m$ die aktuelle Basis potenziert mit $2^i$ ist.
- $e_i \in \mathbb{N}_0$ der verbleibende Exponent ist, der verarbeitet werden muss.

Die Binärdarstellung des Exponenten $e$ ist durch die Bitfolge $(a_k, a_{k-1}, \dots, a_0)$ gegeben, sodass:
$$e = \sum_{i=0}^{k} a_i 2^i, \quad a_i \in \{0, 1\}$$
wobei $k = \lfloor \log_2 e \rfloor$.

## 2. Algebraische Charakterisierung

Der Algorithmus basiert auf der Eigenschaft der Exponentiation durch Quadrieren, die aus der Binärdarstellung von $e$ abgeleitet wird. Wir definieren den Zustandsübergang $(r_{i+1}, b_{i+1}, e_{i+1})$ von $(r_i, b_i, e_i)$ wie folgt:

1. **Basis-Update:** $b_{i+1} \equiv b_i^2 \pmod m$
2. **Exponent-Update:** $e_{i+1} = \lfloor e_i / 2 \rfloor$
3. **Ergebnis-Update:** 
   $$r_{i+1} \equiv \begin{cases} r_i \cdot b_i \pmod m & \text{falls } e_i \equiv 1 \pmod 2 \\ r_i \pmod m & \text{falls } e_i \equiv 0 \pmod 2 \end{cases}$$

**Schleifeninvariante:**
Zu Beginn jeder Iteration $i$ (wobei $i$ die Anzahl der verarbeiteten Bits bezeichnet) gilt die folgende Invariante:
$$r_i \cdot b_i^{e_i} \equiv b^e \pmod m$$
Induktionsanfang: Für $i=0$ gilt $r_0 = 1$, $b_0 = b \pmod m$ und $e_0 = e$. Somit gilt $1 \cdot b^e \equiv b^e \pmod m$.
Terminierung: Wenn $e_k = 0$ erreicht ist, liefert die Invariante $r_k \cdot b_k^0 \equiv r_k \equiv b^e \pmod m$, was die Korrektheit des Ergebnisses bestätigt.

Die verwendete modulare Eigenschaft ist der Homomorphismus der Multiplikationsoperation über dem Ring $\mathbb{Z}_m$:
$$(x \cdot y) \pmod m = ((x \pmod m) \cdot (y \pmod m)) \pmod m$$
Dies stellt sicher, dass alle Zwischenprodukte $r_i \cdot b_i$ und $b_i^2$ innerhalb des Bereichs $[0, m-1]$ bleiben, wodurch ein arithmetischer Überlauf verhindert wird.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus terminiert, wenn der Exponent $e$ den Wert 0 erreicht. In jeder Iteration wird der Exponent mittels der Rechts-Shift-Operation $e \leftarrow \lfloor e/2 \rfloor$ transformiert. 

Sei $T(e)$ die Anzahl der für einen Exponenten $e$ benötigten Iterationen. Die Rekurrenz lautet:
$$T(e) = 1 + T(\lfloor e/2 \rfloor), \quad T(0) = 0$$
Nach dem Master-Theorem (oder durch einfache Expansion) beträgt die Anzahl der Iterationen exakt $\lfloor \log_2 e \rfloor + 1$. Da jede Iteration eine konstante Anzahl an arithmetischen Operationen (Multiplikation, Modulo, bitweiser Shift und Vergleich) umfasst, ergibt sich die gesamte Zeitkomplexität zu:
$$T(e) = O(\log e)$$

### Platzkomplexität
Der Algorithmus verwaltet eine feste Anzahl an Variablen $(r, b, e, m)$, unabhängig von der Größe der Eingabe. Es werden keine zusätzlichen Datenstrukturen (wie Arrays oder Rekursions-Stacks) verwendet. 

Sei $S(m)$ der Speicherplatz, der zum Speichern der Variablen benötigt wird. Unter der Annahme, dass die Wortbreite der Maschine ausreicht, um die Zwischenprodukte zu speichern (typischerweise $O(\log m)$ Bits), beträgt die zusätzliche Platzkomplexität:
$$S = O(1)$$
Dies ist ein strikt konstanter Platzbedarf, da der Speicherbedarf nicht mit der Größe von $e$ oder $b$ skaliert.