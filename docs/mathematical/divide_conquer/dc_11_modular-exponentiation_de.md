# Formale mathematische Spezifikation: Modulare Exponentiation

## 1. Definitionen und Notation

Sei die Domäne des Algorithmus definiert durch das Tripel $(x, y, p) \in \mathbb{Z}_{\ge 0} \times \mathbb{Z}_{\ge 0} \times \mathbb{Z}_{> 1}$. 
Das Ziel ist die Berechnung der Funktion $f: \mathbb{Z}_{\ge 0}^2 \times \mathbb{Z}_{> 1} \to \mathbb{Z}_p$, wobei $\mathbb{Z}_p = \{0, 1, \dots, p-1\}$, definiert als:
$$f(x, y, p) \equiv x^y \pmod{p}$$

Wir definieren den Zustand des Algorithmus in der Iteration $i$ (wobei $i=0$ die Initialisierung darstellt) als Tupel $\mathcal{S}_i = (r_i, b_i, e_i)$, wobei:
*   $r_i \in \mathbb{Z}_p$ das akkumulierte Ergebnis ist.
*   $b_i \in \mathbb{Z}_p$ die aktuelle Basis ist, welche $x^{2^i} \pmod{p}$ repräsentiert.
*   $e_i \in \mathbb{Z}_{\ge 0}$ der verbleibende Exponent ist, wobei $e_i = \lfloor y / 2^i \rfloor$.

## 2. Algebraische Charakterisierung

Die Korrektheit des Algorithmus beruht auf der Eigenschaft der modularen Multiplikation: Für beliebige $a, b, m \in \mathbb{Z}$ gilt $(a \cdot b) \pmod{m} = [(a \pmod{m}) \cdot (b \pmod{m})] \pmod{m}$. 

Wir stellen den Exponenten $y$ in seiner Binärdarstellung dar: $y = \sum_{j=0}^{\lfloor \log_2 y \rfloor} d_j 2^j$, wobei $d_j \in \{0, 1\}$. Nach den Potenzgesetzen gilt:
$$x^y = x^{\sum d_j 2^j} = \prod_{j=0}^{\lfloor \log_2 y \rfloor} (x^{2^j})^{d_j}$$

Wendet man den Modulo-Operator auf das Produkt an, erhält man:
$$x^y \pmod{p} = \left( \prod_{j=0}^{\lfloor \log_2 y \rfloor} (x^{2^j})^{d_j} \right) \pmod{p}$$

**Schleifeninvariante:**
Zu Beginn jeder Iteration $i$ gilt die folgende Invariante:
$$x^y \equiv r_i \cdot b_i^{e_i} \pmod{p}$$

**Übergangsregeln:**
Gegeben sei $\mathcal{S}_i = (r_i, b_i, e_i)$, der Zustand $\mathcal{S}_{i+1}$ wird wie folgt hergeleitet:
1.  **Ergebnis aktualisieren:** Wenn $e_i \equiv 1 \pmod{2}$, dann $r_{i+1} = (r_i \cdot b_i) \pmod{p}$; andernfalls $r_{i+1} = r_i$.
2.  **Basis aktualisieren:** $b_{i+1} = (b_i^2) \pmod{p}$.
3.  **Exponent aktualisieren:** $e_{i+1} = \lfloor e_i / 2 \rfloor$.

Der Algorithmus terminiert in der Iteration $k = \lfloor \log_2 y \rfloor + 1$, wenn $e_k = 0$, was $r_k \equiv x^y \pmod{p}$ ergibt.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus führt eine Sequenz von Operationen aus, die durch die Binärdarstellung von $y$ bestimmt wird. Sei $L = \lfloor \log_2 y \rfloor + 1$ die Anzahl der Bits, die zur Darstellung von $y$ erforderlich sind. 
In jeder Iteration $i \in \{0, 1, \dots, L-1\}$ führt der Algorithmus eine konstante Anzahl an arithmetischen Operationen aus (Multiplikation, Modulo, bitweises Verschieben und Vergleich). 

Die gesamte Zeitkomplexität $T(y)$ ergibt sich aus der Summe:
$$T(y) = \sum_{i=0}^{L-1} \Theta(1) = \Theta(L) = \Theta(\log y)$$
Da jede Multiplikation Zahlen involviert, die durch $p$ begrenzt sind, und unter der Annahme, dass $p$ in ein Maschinenwort passt, ist jede Multiplikation $O(1)$. Somit beträgt die Zeitkomplexität $O(\log y)$.

### Platzkomplexität
Der Algorithmus verwaltet eine feste Menge an Variablen $(r, b, e)$. Unabhängig von der Größe von $y$ oder $p$ ist der Speicherbedarf auf die Speicherung dieser drei Variablen beschränkt.
*   $r, b \in [0, p-1]$
*   $e \in [0, y]$

Der benötigte zusätzliche Speicherplatz beträgt $S = \Theta(1)$, da der Speicherverbrauch nicht mit der Eingabegröße $y$ oder $p$ skaliert (unter der Annahme einer Ganzzahldarstellung mit fester Breite). Somit beträgt die Platzkomplexität $O(1)$.