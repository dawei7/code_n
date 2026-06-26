# Formale mathematische Spezifikation: Majority Element (Divide and Conquer)

## 1. Definitionen und Notation

Sei $A = [a_0, a_1, \dots, a_{n-1}]$ ein Array aus $n$ Elementen, wobei jedes $a_i \in \mathcal{X}$ und $\mathcal{X}$ eine total geordnete Menge ist.

Definiere die Häufigkeitsfunktion $f: \mathcal{X} \times \mathcal{P}(A) \to \mathbb{N}_0$ so, dass für jeden Wert $x \in \mathcal{X}$ und jedes Subarray $S \subseteq A$ gilt: $f(x, S) = \sum_{a \in S} \mathbb{I}(a = x)$, wobei $\mathbb{I}(\cdot)$ die Indikatorfunktion ist.

Das **Majority Element** $m \in \mathcal{X}$ ist definiert als das eindeutige Element, das die folgende Bedingung erfüllt:
$$f(m, A) > \left\lfloor \frac{|A|}{2} \right\rfloor$$

Wir definieren die rekursive Funktion $\mathcal{M}(S)$, die den Majority-Kandidaten für ein Subarray $S$ der Länge $k = |S|$ zurückgibt. Der Definitionsbereich des Algorithmus ist die Menge aller endlichen Sequenzen über $\mathcal{X}$, die ein Majority Element enthalten.

## 2. Algebraische Charakterisierung

Die Korrektheit des Divide-and-Conquer-Ansatzes beruht auf dem **Majority Lemma**: Wenn $m$ das Majority Element von $A$ ist und $A$ in zwei disjunkte Subarrays $A_L$ und $A_R$ partitioniert wird, sodass $A = A_L \cup A_R$, dann muss $m$ das Majority Element von mindestens einem der Subarrays $A_L$ oder $A_R$ sein.

### Rekursionsgleichung
Sei $T(n)$ die Zeitkomplexität für eine Eingabe der Größe $n$. Der Algorithmus ist durch die folgende Rekursionsgleichung definiert:
$$T(n) = 2T\left(\frac{n}{2}\right) + g(n)$$
wobei $g(n)$ die Kosten des Merge-Schritts repräsentiert. Der Merge-Schritt beinhaltet zwei lineare Durchläufe des aktuellen Subarrays, um das Vorkommen der von den rekursiven Aufrufen zurückgegebenen Kandidaten zu zählen:
$$g(n) = \Theta(n)$$

### Korrektheitsinvariante
Seien für ein Subarray $S$ die Werte $c_L = \mathcal{M}(S_L)$ und $c_R = \mathcal{M}(S_R)$. Der Merge-Schritt definiert die Ausgabe $\mathcal{M}(S)$ als:
$$\mathcal{M}(S) = \begin{cases} c_L & \text{if } f(c_L, S) > \frac{|S|}{2} \\ c_R & \text{if } f(c_R, S) > \frac{|S|}{2} \\ \text{undefined} & \text{otherwise} \end{cases}$$
Unter der Problemvorgabe, dass garantiert ein Majority Element existiert, liefert der Merge-Schritt garantiert ein gültiges $m$ zurück.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität wird durch das Master-Theorem für Divide-and-Conquer-Rekursionen der Form $T(n) = aT(n/b) + f(n)$ bestimmt.
Hierbei ist $a=2$, $b=2$ und $f(n) = O(n)$.
Vergleicht man $f(n) = n^1$ mit $n^{\log_b a} = n^{\log_2 2} = n^1$, so fällt dies unter Fall 2 des Master-Theorems.
Daraus folgt:
$$T(n) = \Theta(n^{\log_b a} \log n) = \Theta(n \log n)$$
Der Gesamtaufwand auf jeder Tiefe $d$ des Rekursionsbaums beträgt $\sum_{i=1}^{2^d} O(n/2^d) = O(n)$. Da die Baumtiefe $\log_2 n$ beträgt, ist die gesamte Zeitkomplexität $O(n \log n)$.

### Platzkomplexität
Die Platzkomplexität $S(n)$ wird durch die maximale Tiefe des Rekursions-Stacks bestimmt. Jeder rekursive Aufruf fügt einen Frame zum Call-Stack hinzu.
$$S(n) = S\left(\frac{n}{2}\right) + O(1)$$
Löst man diese Rekursionsgleichung, ergibt sich:
$$S(n) = O(\log n)$$
Der zusätzliche Speicherbedarf wird vom Rekursions-Stack dominiert, da der Zählprozess im Merge-Schritt in-place unter Verwendung von $O(1)$ zusätzlichen Variablen durchgeführt werden kann. Daher beträgt die gesamte Platzkomplexität $O(\log n)$.