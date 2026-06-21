# Formale mathematische Spezifikation: Fractional Knapsack Problem

## 1. Definitionen und Notation

Sei $n \in \mathbb{N}$ die Anzahl der verfügbaren Items. Jedes Item $i \in \{1, 2, \dots, n\}$ ist durch ein Paar $(v_i, w_i)$ charakterisiert, wobei $v_i \in \mathbb{R}^+$ der Wert und $w_i \in \mathbb{R}^+$ das Gewicht des Items ist. Sei $W \in \mathbb{R}^+$ die gesamte Gewichtskapazität des Knapsack.

Wir definieren die **Dichte** (oder das Wert-zu-Gewicht-Verhältnis) von Item $i$ als:
$$\rho_i = \frac{v_i}{w_i}$$

Das Ziel ist es, einen Vektor von Anteilen $x = (x_1, x_2, \dots, x_n)$ zu bestimmen, wobei $x_i \in [0, 1]$ den Anteil des Items $i$ repräsentiert, der in den Knapsack aufgenommen wird. Der Zustandsraum $\mathcal{S}$ ist die Menge aller zulässigen Vektoren $x$, die die Kapazitätsbeschränkung erfüllen:
$$\mathcal{S} = \left\{ x \in \mathbb{R}^n : 0 \le x_i \le 1, \forall i \in \{1, \dots, n\} \text{ und } \sum_{i=1}^n x_i w_i \le W \right\}$$

Das Ziel ist die Maximierung der Zielfunktion $f(x)$:
$$f(x) = \sum_{i=1}^n x_i v_i$$

## 2. Algebraische Charakterisierung

Das Fractional Knapsack Problem ist ein Problem der linearen Optimierung. Aufgrund der **Greedy Choice Property** kann eine optimale Lösung konstruiert werden, indem Items mit der höchsten Dichte priorisiert werden.

Sei $\pi$ eine Permutation der Menge $\{1, \dots, n\}$, sodass die Dichten nicht-aufsteigend geordnet sind:
$$\rho_{\pi(1)} \ge \rho_{\pi(2)} \ge \dots \ge \rho_{\pi(n)}$$

Sei $k$ der kritische Index, für den gilt:
$$\sum_{i=1}^{k-1} w_{\pi(i)} \le W < \sum_{i=1}^{k} w_{\pi(i)}$$

Die optimale Lösung $x^*$ ist definiert als:
$$x^*_{\pi(i)} = \begin{cases} 1 & \text{if } i < k \\ \frac{W - \sum_{j=1}^{k-1} w_{\pi(j)}}{w_{\pi(k)}} & \text{if } i = k \\ 0 & \text{if } i > k \end{cases}$$

**Korrektheit (Austauschargument):**
Angenommen, es existiert eine optimale Lösung $x$, die nicht der Greedy-Reihenfolge folgt. Wenn $i, j$ existieren, sodass $\rho_i > \rho_j$, aber $x_i < 1$ und $x_j > 0$, können wir eine neue Lösung $x'$ konstruieren, indem wir $x_i$ um $\epsilon$ erhöhen und $x_j$ um $\epsilon \frac{w_i}{w_j}$ verringern, sodass das Gesamtgewicht konstant bleibt. Die Änderung des Gesamtwerts beträgt $\Delta V = \epsilon v_i - (\epsilon \frac{w_i}{w_j}) v_j = \epsilon w_i (\rho_i - \rho_j)$. Da $\rho_i > \rho_j$, ist $\Delta V > 0$, was der Optimalität von $x$ widerspricht.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus besteht aus zwei primären Phasen:
1. **Sortieren:** Wir berechnen $\rho_i$ für alle $n$ Items und sortieren diese. Unter Verwendung eines effizienten vergleichsbasierten Sortieralgorithmus (z. B. Timsort oder Quicksort) beträgt die Zeitkomplexität $T_{sort}(n) = \Theta(n \log n)$.
2. **Linearer Scan:** Wir iterieren höchstens einmal durch die sortierten Items. Diese Phase führt $n$ Operationen mit konstanter Zeit aus, was $T_{scan}(n) = \Theta(n)$ ergibt.

Die gesamte Zeitkomplexität beträgt:
$$T(n) = T_{sort}(n) + T_{scan}(n) = \Theta(n \log n) + \Theta(n) = O(n \log n)$$

### Platzkomplexität
Die Platzkomplexität hängt von der Implementierung des Sortieralgorithmus und der Speicherung der Indizes ab:
1. **Zusätzlicher Speicher:** Wir benötigen ein Array von Indizes oder Pointern der Größe $n$, um die sortierte Reihenfolge beizubehalten, ohne den ursprünglichen Input zu verändern, was zu $S(n) = O(n)$ führt.
2. **In-place Sortierung:** Wenn das Eingabe-Array veränderbar ist und in-place sortiert werden kann, beträgt die zusätzliche Platzkomplexität $S(n) = O(1)$ (unter der Annahme, dass der Sortieralgorithmus $O(1)$ oder $O(\log n)$ Stack-Speicher verwendet).

Somit ist die gesamte Platzkomplexität $O(n)$ im allgemeinen Fall oder $O(1)$ unter strikten In-place-Bedingungen.