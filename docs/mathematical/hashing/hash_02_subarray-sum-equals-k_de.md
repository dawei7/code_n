# Formale mathematische Spezifikation: Subarray Sum Equals K

## 1. Definitionen und Notation

Sei $A = [a_0, a_1, \dots, a_{n-1}]$ eine Folge von Ganzzahlen, wobei $a_i \in \mathbb{Z}$ für alle $i \in \{0, \dots, n-1\}$ gilt. Sei $k \in \mathbb{Z}$ die Zielsumme.

Wir definieren die **Präfixsummenfolge** $P = [p_0, p_1, \dots, p_n]$ wie folgt:
- $p_0 = 0$
- $p_j = \sum_{i=0}^{j-1} a_i$ für $1 \le j \le n$

Ein **zusammenhängendes Subarray** $A[i \dots j-1]$ (wobei $0 \le i < j \le n$) hat eine Summe $S(i, j)$, die definiert ist als:
$$S(i, j) = \sum_{m=i}^{j-1} a_m = p_j - p_i$$

Das Ziel ist es, die Kardinalität der Menge der Indexpaare $\mathcal{I} = \{ (i, j) \in \mathbb{Z}^2 \mid 0 \le i < j \le n \text{ und } S(i, j) = k \}$ zu berechnen.

Sei $f: \mathbb{Z} \to \mathbb{N}_0$ eine Häufigkeitsabbildung (Hash Map), wobei $f(v)$ die Anzahl angibt, wie oft ein Wert $v$ in der bisher verarbeiteten Präfixsummenfolge aufgetreten ist.

## 2. Algebraische Charakterisierung

Die Bedingung $S(i, j) = k$ ist äquivalent zur algebraischen Identität:
$$p_j - p_i = k \iff p_i = p_j - k$$

Für einen festen Index $j \in \{1, \dots, n\}$ entspricht die Anzahl der gültigen Startindizes $i < j$, für die die Subarray-Summe gleich $k$ ist, exakt der Häufigkeit, mit der der Wert $(p_j - k)$ in der Menge $\{p_0, p_1, \dots, p_{j-1}\}$ aufgetreten ist.

Sei $C_j$ die Anzahl der Subarrays, die am Index $j-1$ enden und die Summe $k$ aufweisen. Dann gilt:
$$C_j = \sum_{i=0}^{j-1} \mathbb{I}(p_i = p_j - k)$$
wobei $\mathbb{I}(\cdot)$ die Indikatorfunktion ist. Die Gesamtzahl $T$ ist:
$$T = \sum_{j=1}^{n} C_j = \sum_{j=1}^{n} f_{j-1}(p_j - k)$$
wobei $f_{j-1}(v) = |\{m \in \{0, \dots, j-1\} : p_m = v\}|$.

**Schleifeninvariante:** Zu Beginn der Iteration $j$ (wobei $j$ von $0$ bis $n-1$ läuft), erfüllt die Hash Map $f$:
$$f(v) = \sum_{m=0}^{j} \mathbb{I}(p_m = v)$$
Diese Invariante stellt sicher, dass beim Verarbeiten von $p_{j+1}$ die Hash Map $f$ die Häufigkeiten aller vorangegangenen Präfixsummen enthält, wodurch der Algorithmus die Anforderung $p_i = p_{j+1} - k$ in erwarteter $O(1)$ Zeit erfüllen kann.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus führt einen einzigen Durchlauf über das Array $A$ der Länge $n$ aus.
1. In jeder Iteration $j \in \{0, \dots, n-1\}$ führen wir aus:
   - Eine Addition zur Aktualisierung der laufenden Präfixsumme: $O(1)$.
   - Einen Hash Map-Zugriff für $p_j - k$: $O(1)$ erwartete Zeit.
   - Ein Hash Map-Update für $p_j$: $O(1)$ erwartete Zeit.

Die gesamte Zeitkomplexität ergibt sich aus der Summation:
$$T(n) = \sum_{j=0}^{n-1} (O(1) + O(1) + O(1)) = O(n)$$
Unter der Annahme einer gleichmäßigen Hash-Verteilung beträgt die Komplexität im Durchschnitt $\Theta(n)$. Im schlechtesten Fall (z. B. bei Hash-Kollisionen) beträgt die Komplexität $O(n^2)$, was jedoch durch robuste Implementierungen der Hash-Funktion abgemildert wird.

### Platzkomplexität
Die Platzkomplexität wird durch den Speicherbedarf der Häufigkeitsabbildung $f$ bestimmt.
- Im schlechtesten Fall sind alle Präfixsummen $\{p_0, p_1, \dots, p_n\}$ verschieden.
- Die Hash Map speichert maximal $n+1$ Einträge.
- Jeder Eintrag besteht aus einem Key (der Präfixsumme) und einem Value (der Häufigkeit).

Somit beträgt die zusätzliche Platzkomplexität $O(n)$. Die gesamte Platzkomplexität beträgt $O(n)$, um das Eingabearray und die Hash Map zu speichern.