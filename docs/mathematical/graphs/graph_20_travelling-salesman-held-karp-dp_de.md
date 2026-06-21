# Formale mathematische Spezifikation: Travelling Salesperson (Held-Karp DP)

## 1. Definitionen und Notation

Sei $G = (V, E)$ ein vollständiger ungerichteter Graph, wobei $V = \{0, 1, \dots, n-1\}$ die Menge der Knoten ist und $n = |V|$. Sei $w: V \times V \to \mathbb{R}^+$ eine Gewichtsfunktion, die durch eine Adjacency Matrix $W$ dargestellt wird, wobei $w_{ij}$ die Kosten der Kante $(i, j)$ bezeichnet.

Ein Hamilton-Zyklus ist eine Permutation $\sigma$ von $V$, sodass die Gesamtkosten $\sum_{i=0}^{n-1} w_{\sigma(i), \sigma(i+1 \pmod n)}$ betragen. Das Ziel ist es, Folgendes zu finden:
$$\min_{\sigma \in S_n} \sum_{i=0}^{n-1} w_{\sigma(i), \sigma(i+1 \pmod n)}$$

Wir definieren den Zustandsraum $\mathcal{S}$ unter Verwendung einer Potenzmengenrepräsentation. Sei $S \subseteq V$ eine Teilmenge von Knoten, dargestellt durch eine Bitmaske $m \in \{0, 1, \dots, 2^n - 1\}$, wobei das $i$-te Bit gesetzt ist, wenn $i \in S$.
Der DP-Zustand ist definiert als:
$C(S, i)$: Die minimalen Kosten eines Pfades, der genau die Menge der Knoten $S \subseteq V$ besucht, bei Knoten $0$ beginnt und bei Knoten $i \in S$ endet, wobei $0 \in S$.

## 2. Algebraische Charakterisierung

Der Held-Karp-Algorithmus beruht auf dem Optimalitätsprinzip und zerlegt das Problem in Teilprobleme mit zunehmender Teilmengengröße.

### Induktionsanfang
Für einen Pfad, der bei Knoten $0$ beginnt und bei $0$ endet, wobei nur Knoten $0$ besucht wurde:
$$C(\{0\}, 0) = 0$$
Für alle $i \in V \setminus \{0\}$:
$$C(\{0, i\}, i) = w_{0, i}$$

### Rekursionsgleichung
Für jede Teilmenge $S \subseteq V$, sodass $|S| > 2$ und $0 \in S$, und für jeden Knoten $i \in S \setminus \{0\}$:
$$C(S, i) = \min_{j \in S \setminus \{i\}, j \neq 0} \{ C(S \setminus \{i\}, j) + w_{j, i} \}$$

### Optimale Lösung
Die optimalen Kosten der Travelling Salesperson Tour sind die minimalen Kosten, um alle Knoten zu besuchen und zum Ursprung zurückzukehren:
$$\text{TSP}_{opt} = \min_{i \in V \setminus \{0\}} \{ C(V, i) + w_{i, 0} \}$$

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus iteriert über alle möglichen Teilmengen $S \subseteq V$ und alle möglichen Endknoten $i \in S$.
1. **Größe des Zustandsraums:** Es gibt $2^n$ mögliche Teilmengen $S$. Für jede Teilmenge gibt es $n$ mögliche Endknoten $i$. Somit beträgt die Anzahl der Zustände $O(n \cdot 2^n)$.
2. **Übergangskosten:** Für jeden Zustand $(S, i)$ erfordert die Rekursionsgleichung eine Iteration über alle möglichen vorherigen Knoten $j \in S \setminus \{i\}$. Dies benötigt $O(n)$ Zeit.

Die gesamte Zeitkomplexität $T(n)$ ergibt sich aus der Summation über die Anzahl der Zustände multipliziert mit dem Arbeitsaufwand pro Übergang:
$$T(n) = \sum_{k=2}^{n} \binom{n}{k} \cdot k \cdot (k-1) \approx O(n^2 \cdot 2^n)$$
Formal gilt: Da es $2^n$ Teilmengen gibt und wir für jede Teilmenge $O(n^2)$ Operationen (oder $O(n)$ pro Zustand) durchführen, beträgt die Komplexität $O(n^2 2^n)$.

### Platzkomplexität
Der Algorithmus benötigt eine Memoization-Tabelle (oder DP-Tabelle), um die Ergebnisse von $C(S, i)$ zu speichern.
1. **Tabellendimensionen:** Die Tabelle benötigt $2^n$ Zeilen (für jede Maske) und $n$ Spalten (für jeden Endknoten).
2. **Speicherbedarf:** Jeder Eintrag speichert einen skalaren Kostenwert.
$$S(n) = \Theta(n \cdot 2^n)$$
Diese Platzkomplexität ist notwendig, um die Ergebnisse der optimalen Teilstrukturen zu speichern. Dies stellt sicher, dass jedes Teilproblem exakt einmal berechnet wird, wodurch die $O(n!)$-Komplexität einer erschöpfenden Suche (Brute-Force) vermieden wird.