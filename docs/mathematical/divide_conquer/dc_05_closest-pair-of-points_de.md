# Formale mathematische Spezifikation: Closest Pair of Points

## 1. Definitionen und Notation

Sei $P = \{p_1, p_2, \dots, p_n\}$ eine Menge von $n$ Punkten in der euklidischen Ebene $\mathbb{R}^2$, wobei jeder Punkt $p_i$ durch das Koordinatenpaar $(x_i, y_i) \in \mathbb{R}^2$ definiert ist.

Wir definieren die euklidische Abstandsfunktion $d: \mathbb{R}^2 \times \mathbb{R}^2 \to \mathbb{R}_{\ge 0}$ als:
$$d(p_i, p_j) = \sqrt{(x_i - x_j)^2 + (y_i - y_j)^2}$$

Das Ziel ist es, den minimalen Abstand $\delta^*$ zu finden, der definiert ist durch:
$$\delta^* = \min_{1 \le i < j \le n} d(p_i, p_j)$$

Sei $S \subset P$ eine Teilmenge von Punkten. Wir definieren die Projektion von $S$ auf die $x$-Achse als $X(S) = \{x_i \mid p_i \in S\}$. Gegeben eine vertikale Linie $L$, definiert durch $x = x_{mid}$, partitionieren wir $P$ in zwei Teilmengen:
$P_L = \{p \in P \mid x \le x_{mid}\}$ und $P_R = \{p \in P \mid x > x_{mid}\}$.

## 2. Algebraische Charakterisierung

Der Algorithmus basiert auf dem Prinzip von Divide and Conquer. Seien $\delta_L$ und $\delta_R$ die minimalen Abstände innerhalb von $P_L$ beziehungsweise $P_R$. Sei $\delta = \min(\delta_L, \delta_R)$.

Um Paare $(p_i, p_j)$ zu berücksichtigen, bei denen $p_i \in P_L$ und $p_j \in P_R$ gilt, definieren wir den "Streifen" $S_\delta$ als:
$$S_\delta = \{p \in P \mid |x_p - x_{mid}| < \delta\}$$

**Lemma (Die Dünnheitseigenschaft):** Für jeden Punkt $p \in S_\delta$ gibt es höchstens 7 Punkte $q \in S_\delta$, sodass $y_q \in [y_p, y_p + \delta]$.
*Beweisskizze:* Betrachten wir ein Rechteck der Größe $2\delta \times \delta$, das an der Trennlinie zentriert ist. Dieses Rechteck kann in zwei $\delta \times \delta$ Quadrate unterteilt werden. Innerhalb jedes Quadrats können keine zwei Punkte einen geringeren Abstand als $\delta$ zueinander haben. Nach dem Schubfachprinzip kann jedes $\delta \times \delta$ Quadrat höchstens 4 Punkte enthalten (einen an jeder Ecke). Somit beträgt die Gesamtzahl der Punkte in der $2\delta \times \delta$ Region höchstens 8. Wenn wir den Punkt $p$ selbst ausschließen, müssen wir nur die nächsten 7 Punkte in der nach $y$ sortierten Reihenfolge überprüfen.

Die Rekursionsgleichung, die den Algorithmus bestimmt, lautet:
$$T(n) = 2T\left(\frac{n}{2}\right) + f(n)$$
wobei $f(n)$ die Kosten des Merge-Schritts repräsentiert. Wenn der Streifen auf jeder Ebene nach $y$ sortiert wird, gilt $f(n) = O(n \log n)$, was zu $T(n) = O(n \log^2 n)$ führt. Wenn die Punkte vorab nach $y$ sortiert sind, gilt $f(n) = O(n)$, was zu $T(n) = O(n \log n)$ führt.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus folgt dem Master-Theorem für Divide-and-Conquer-Rekursionen.

1. **Induktionsanfang:** Für $n \le 3$ benötigt die Brute-Force-Berechnung $O(1)$ Zeit.
2. **Divide:** Das Finden des Medians $x_{mid}$ benötigt $O(1)$ Zeit, sofern ein sortiertes Array vorliegt.
3. **Conquer:** Zwei rekursive Aufrufe für Mengen der Größe $n/2$.
4. **Merge:**
   - Die Konstruktion des Streifens $S_\delta$ benötigt $O(n)$.
   - Das Sortieren von $S_\delta$ nach $y$ benötigt $O(n \log n)$.
   - Der lineare Scan des Streifens benötigt $O(n \cdot k)$, wobei $k=7$ eine Konstante ist.

Die Rekursion $T(n) = 2T(n/2) + O(n \log n)$ ergibt $T(n) = O(n \log^2 n)$ gemäß Fall 2 des Master-Theorems. Durch das Beibehalten einer global nach $y$ sortierten Liste von Punkten und deren Weitergabe durch die Rekursion (Filtern in $O(n)$), wird der Merge-Schritt zu $O(n)$, was ergibt:
$$T(n) = 2T(n/2) + O(n) \implies T(n) = O(n \log n)$$

### Platzkomplexität
Die Platzkomplexität wird durch den Rekursions-Stack und die Speicherung der Hilfs-Arrays (die sortierten Punkte und der Streifen) dominiert.
- **Rekursions-Stack:** Die Tiefe des Rekursionsbaums beträgt $\lceil \log_2 n \rceil$.
- **Hilfsspeicher:** Auf jeder Ebene der Rekursion speichern wir eine Teilmenge von Punkten der Größe höchstens $n$.
- **Gesamtspeicher:** Da die Arrays als Referenz übergeben oder innerhalb des Gültigkeitsbereichs des rekursiven Aufrufs erstellt werden, beträgt der gesamte Hilfsspeicher $O(n)$, um die sortierte Reihenfolge und den Streifen beizubehalten. Somit ist die Platzkomplexität $O(n)$.