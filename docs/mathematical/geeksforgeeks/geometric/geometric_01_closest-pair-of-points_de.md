# Formale mathematische Spezifikation: Closest Pair of Points

## 1. Definitionen und Notation

Sei $P = \{p_1, p_2, \dots, p_n\}$ eine Menge von $n$ Punkten in der euklidischen Ebene $\mathbb{R}^2$, wobei jeder Punkt $p_i$ durch ein Koordinatenpaar $(x_i, y_i) \in \mathbb{R}^2$ repräsentiert wird.

Wir definieren die Abstandsfunktion $\delta: \mathbb{R}^2 \times \mathbb{R}^2 \to \mathbb{R}_{\ge 0}$ als die euklidische Standardmetrik:
$$\delta(p_i, p_j) = \sqrt{(x_i - x_j)^2 + (y_i - y_j)^2}$$

Das Ziel ist es, den minimalen Abstand $\Delta$ zu finden, der wie folgt definiert ist:
$$\Delta = \min_{1 \le i < j \le n} \delta(p_i, p_j)$$

Sei $S \subset P$ eine Teilmenge von Punkten. Wir definieren die Projektion von $S$ auf die $x$-Achse als $X(S) = \{x \mid (x, y) \in S\}$. Gegeben eine vertikale Linie $L$, definiert durch $x = x_{mid}$, partitionieren wir $P$ in zwei Teilmengen:
$P_L = \{p \in P \mid x \le x_{mid}\}$ und $P_R = \{p \in P \mid x > x_{mid}\}$.

## 2. Algebraische Charakterisierung

Der Algorithmus basiert auf dem Divide-and-Conquer-Paradigma. Sei $T(n)$ der minimale Abstand für eine Menge von $n$ Punkten. Die Rekursionsgleichung wird durch die Kombination der Teilprobleme bestimmt:

1. **Divide:** Seien $\Delta_L$ und $\Delta_R$ die minimalen Abstände in $P_L$ bzw. $P_R$. Sei $\delta = \min(\Delta_L, \Delta_R)$.
2. **Conquer (Der Streifen):** Wir definieren den Streifen $S_\delta$ als:
   $$S_\delta = \{p \in P \mid |x_p - x_{mid}| < \delta\}$$
   Für jeden Punkt $p \in S_\delta$ betrachten wir nur Punkte $q \in S_\delta$, für die $|y_p - y_q| < \delta$ gilt.

**Geometrisches Lemma:** Für jeden Punkt $p \in S_\delta$ ist die Anzahl der Punkte $q \in S_\delta$, für die $y_q \in [y_p, y_p + \delta]$ gilt, höchstens 7.
*Beweisskizze:* Die Region $[x_{mid}-\delta, x_{mid}+\delta] \times [y_p, y_p+\delta]$ kann in zwei Quadrate der Seitenlänge $\delta/2$ unterteilt werden. Nach dem Schubfachprinzip (Pigeonhole Principle) gilt, da je zwei Punkte in der linken (oder rechten) Hälfte mindestens den Abstand $\delta$ zueinander haben, dass jedes Quadrat höchstens 4 Punkte enthalten kann. Somit ist die Gesamtzahl der Punkte im $2\delta \times \delta$ Rechteck durch eine Konstante $k=8$ begrenzt (einschließlich $p$ selbst).

Die Rekursionsgleichung für die Zeitkomplexität lautet:
$$T(n) = 2T(n/2) + O(n)$$
Wobei $O(n)$ die lineare Zeit darstellt, die benötigt wird, um die Ergebnisse durch das Scannen des nach $y$-Koordinate sortierten Streifens $S_\delta$ zusammenzuführen.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität des Algorithmus wird aus dem Master-Theorem für Divide-and-Conquer-Rekursionen abgeleitet. Gegeben die Rekursion:
$$T(n) = 2T\left(\frac{n}{2}\right) + f(n)$$
wobei $f(n) = O(n)$ der Aufwand ist, der für das Zusammenführen der Teilprobleme (Sortieren des Streifens oder Filtern vorsortierter Listen) anfällt.

Gemäß dem Master-Theorem, für $a=2, b=2, d=1$:
Da $a = b^d$ ($2 = 2^1$) gilt, ist die Komplexität:
$$T(n) = \Theta(n^{\log_b a} \log n) = \Theta(n \log n)$$
Falls der Streifen in jedem Rekursionsschritt ohne Vorsortierung sortiert wird, wird der Merge-Schritt zu $O(n \log n)$, was zu $T(n) = O(n \log^2 n)$ führt. Indem wir die Punkte während der gesamten Rekursion nach $y$-Koordinate sortiert halten, stellen wir sicher, dass der Merge-Schritt strikt $O(n)$ ist, wodurch die optimale $\Theta(n \log n)$ erreicht wird.

### Platzkomplexität
Die Platzkomplexität $S(n)$ wird durch die Tiefe des Rekursions-Stacks und die Speicherung der Punkte bestimmt:
1. **Rekursions-Stack:** Die Tiefe des Rekursionsbaums beträgt $\lceil \log_2 n \rceil$, was $O(\log n)$ zum zusätzlichen Speicherplatz beiträgt.
2. **Datenspeicherung:** Das Speichern der Punkte erfordert $O(n)$ Speicherplatz.
3. **Hilfs-Arrays:** In der optimalen Implementierung erfordert das Erstellen des Streifens $S_\delta$ auf jeder Ebene $O(n)$ Speicherplatz.

Somit ist die gesamte Platzkomplexität:
$$S(n) = O(n)$$