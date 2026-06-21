# Formale mathematische Spezifikation: Wechselgeld-Problem (Anzahl der Möglichkeiten)

## 1. Definitionen und Notation

Sei $C = \{c_1, c_2, \dots, c_n\}$ eine endliche Menge positiver Ganzzahlen, die die verfügbaren Münzwerte repräsentieren, wobei $c_i \in \mathbb{Z}^+$. Sei $A \in \mathbb{N}_0$ der Zielbetrag.

Wir definieren das Ziel als die Bestimmung der Anzahl nicht-negativer ganzzahliger Lösungen $(x_1, x_2, \dots, x_n)$ für die lineare diophantische Gleichung:
$$\sum_{i=1}^{n} x_i \cdot c_i = A, \quad \text{wobei } x_i \in \{0, 1, 2, \dots\}$$

Sei $\mathcal{S}$ der Zustandsraum der Dynamic Programming-Tabelle, definiert als eine Sequenz $dp = (dp_0, dp_1, \dots, dp_A)$, wobei $dp_j$ die Anzahl der eindeutigen Münzkombinationen repräsentiert, die exakt die Summe $j$ ergeben.

## 2. Algebraische Charakterisierung

Das Problem ist äquivalent zur Bestimmung des Koeffizienten von $z^A$ in der erzeugenden Funktion $P(z)$:
$$P(z) = \prod_{i=1}^{n} \left( \sum_{k=0}^{\infty} z^{k \cdot c_i} \right) = \prod_{i=1}^{n} \frac{1}{1 - z^{c_i}}$$

Um dies mittels Dynamic Programming zu berechnen, definieren wir $dp[i][j]$ als die Anzahl der Möglichkeiten, den Betrag $j$ unter Verwendung nur der ersten $i$ Münzwerte zu bilden. Die Rekursionsgleichung lautet:
$$dp[i][j] = dp[i-1][j] + dp[i][j - c_i]$$
unter Berücksichtigung der Basisfälle:
1. $dp[i][0] = 1$ für alle $0 \le i \le n$ (es gibt eine Möglichkeit, den Betrag Null zu bilden: keine Münzen verwenden).
2. $dp[0][j] = 0$ für alle $j > 0$ (es gibt null Möglichkeiten, einen positiven Betrag ohne Münzen zu bilden).

Durch die Beobachtung, dass $dp[i][j]$ nur von der aktuellen Zeile $i$ und der vorherigen Zeile $i-1$ abhängt, optimieren wir den Speicherbedarf, indem wir den Zustand in ein 1D-Array $dp[j]$ reduzieren. Der Übergang wird zu:
$$dp[j] \leftarrow dp[j] + dp[j - c_i]$$
wobei die Aktualisierung für $j \in \{c_i, c_i+1, \dots, A\}$ durchgeführt wird. Die Reihenfolge der Iteration (äußere Schleife über $C$, innere Schleife über $A$) stellt sicher, dass jede Münze $c_i$ als "Addition" zu bestehenden Kombinationen betrachtet wird, was effektiv eine kanonische Reihenfolge der Münzen erzwingt und das Zählen von Permutationen verhindert.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus besteht aus einer verschachtelten Schleifenstruktur. Die äußere Schleife iteriert über die Menge der Münzwerte $C$, welche die Kardinalität $n$ besitzt. Die innere Schleife iteriert über den Bereich der Beträge von $c_i$ bis $A$.

Die Gesamtzahl der Operationen $T(n, A)$ ergibt sich aus der Summe:
$$T(n, A) = \sum_{i=1}^{n} (A - c_i + 1)$$
Da $c_i \ge 1$, gilt $A - c_i + 1 \le A$. Somit folgt:
$$T(n, A) \le \sum_{i=1}^{n} A = n \cdot A$$
Daher beträgt die Zeitkomplexität $O(n \cdot A)$. Da jede innere Operation eine Addition in konstanter Zeit ist, ist die Komplexität exakt $\Theta(n \cdot A)$.

### Platzkomplexität
Der Algorithmus verwendet ein 1D-Array $dp$ der Größe $A+1$, um die Anzahl der Möglichkeiten zur Bildung jedes Teilbetrags zu speichern.
- **Zusätzlicher Speicher:** Der für die DP-Tabelle benötigte Speicher beträgt $A+1$ Ganzzahlen.
- **Gesamtspeicher:** $O(A)$.

Da der Algorithmus nicht die Speicherung der vollständigen $n \times A$-Matrix erfordert, ist die Platzkomplexität mit $O(A)$ optimal, wobei $A$ der Zielbetrag ist.