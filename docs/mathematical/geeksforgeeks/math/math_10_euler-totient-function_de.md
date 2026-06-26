# Formale mathematische Spezifikation: Eulersche Phi-Funktion

## 1. Definitionen und Notation

Sei $\mathbb{Z}^+$ die Menge der positiven ganzen Zahlen. Wir definieren die Eulersche Phi-Funktion $\phi: \mathbb{Z}^+ \to \mathbb{Z}^+$ als die Kardinalität der Menge der ganzen Zahlen $k$, für die $1 \le k \le n$ und $\gcd(k, n) = 1$ gilt:
$$\phi(n) = |\{k \in \mathbb{Z} : 1 \le k \le n, \gcd(k, n) = 1\}|$$

**Eingabe:** Eine ganze Zahl $n \in \mathbb{Z}^+$.
**Ausgabe:** Eine ganze Zahl $m \in \mathbb{Z}^+$, sodass $m = \phi(n)$.
**Zustandsraum:** Der Algorithmus verwaltet ein Zustandstupel $(n_{curr}, \phi_{curr}, p)$, wobei:
- $n_{curr} \in \mathbb{Z}^+$ den verbleibenden Faktor des ursprünglichen $n$ darstellt, der noch verarbeitet werden muss.
- $\phi_{curr} \in \mathbb{Z}^+$ die Teilproduktberechnung der Phi-Funktion darstellt.
- $p \in \mathbb{Z}^+$ den aktuellen Kandidaten für einen Primfaktor darstellt.

## 2. Algebraische Charakterisierung

Der Algorithmus beruht auf der Eigenschaft, dass $\phi(n)$ eine multiplikative Funktion ist. Nach dem Fundamentalsatz der Arithmetik besitzt jede Zahl $n > 1$ eine eindeutige Primfaktorzerlegung $n = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}$. Die Phi-Funktion ist gegeben durch:
$$\phi(n) = n \prod_{i=1}^{k} \left(1 - \frac{1}{p_i}\right) = \prod_{i=1}^{k} (p_i^{a_i} - p_i^{a_i-1})$$

**Schleifeninvariante:**
Zu Beginn jeder Iteration der Schleife mit dem Kandidaten $p$ sei $n_{orig}$ die ursprüngliche Eingabe. Der Zustand erfüllt:
$$\phi_{curr} = n_{orig} \cdot \prod_{p_j < p, p_j | n_{orig}} \left(1 - \frac{1}{p_j}\right)$$
wobei $n_{curr} = n_{orig} / \prod_{p_j < p, p_j | n_{orig}} p_j^{a_j}$.

**Übergang:**
Wenn ein Primfaktor $p$ identifiziert wird ($n_{curr} \equiv 0 \pmod p$), lautet die Aktualisierungsregel:
$$\phi_{new} = \phi_{curr} \left(1 - \frac{1}{p}\right) = \phi_{curr} - \frac{\phi_{curr}}{p}$$
Diese Transformation bewahrt die Invariante, indem der Beitrag des Primfaktors $p$ in das Produkt einbezogen wird. Die Division $n_{curr} \leftarrow n_{curr} / p^a$ stellt sicher, dass $p$ aus der verbleibenden Faktorisierung entfernt wird, was die Bedingung erfüllt, dass nachfolgende Iterationen nur Primfaktoren $q > p$ berücksichtigen.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus iteriert über die Kandidaten für Teiler $p$ beginnend bei $2$ bis zu $\lfloor \sqrt{n} \rfloor$.

1. **Fall 1: $n$ ist prim.** Die Schleife läuft für $p = 2, \dots, \lfloor \sqrt{n} \rfloor$. Kein $p$ teilt $n$, daher wird die innere `while`-Schleife nie ausgeführt. Die Komplexität beträgt $O(\sqrt{n})$.
2. **Fall 2: $n$ ist zusammengesetzt.** Die Anzahl der Iterationen ist durch $\sqrt{n}$ begrenzt. Jedes Mal, wenn jedoch ein Primfaktor gefunden wird, wird $n_{curr}$ um einen Faktor von mindestens $p$ reduziert. Die Gesamtzahl der Divisionen, die über alle inneren `while`-Schleifen hinweg durchgeführt werden, ist durch $\Omega(\log n)$ begrenzt.

Die Zeitkomplexität im schlechtesten Fall wird durch die Schleifenobergrenze bestimmt:
$$T(n) = \sum_{p=2}^{\sqrt{n}} 1 = O(\sqrt{n})$$
Im durchschnittlichen Fall ist die Dichte der Primfaktoren für eine zufällige ganze Zahl gering, und die Reduktion von $n_{curr}$ beschleunigt den Abbruch der Schleife erheblich, aber die obere Schranke bleibt $O(\sqrt{n})$.

### Platzkomplexität
Der Algorithmus verwendet eine feste Anzahl an Integer-Variablen ($n_{curr}, \phi_{curr}, p$). Es werden keine zusätzlichen Datenstrukturen (wie Arrays oder Rekursions-Stacks) allokiert, die mit $n$ skalieren. Daher beträgt die Platzkomplexität:
$$S(n) = O(1)$$
Dies ist optimal, da der Algorithmus in-place auf dem Eingabewert operiert.