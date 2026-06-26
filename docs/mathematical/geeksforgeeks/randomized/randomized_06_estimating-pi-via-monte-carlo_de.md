# Formale mathematische Spezifikation: Schätzung von Pi mittels Monte Carlo

## 1. Definitionen und Notation

Sei $N \in \mathbb{Z}^+$ die Gesamtzahl der unabhängigen Versuche (Iterationen).
Sei $\mathcal{S} = [0, 1] \times [0, 1] \subset \mathbb{R}^2$ das Einheitsquadrat in der kartesischen Ebene, welches den Stichprobenraum unserer Zufallsvariablen darstellt.
Sei $X_i = (x_i, y_i)$ eine Folge von $N$ unabhängigen und identisch verteilten (i.i.d.) Zufallsvektoren, wobei $x_i, y_i \sim \text{Uniform}(0, 1)$.

Wir definieren die Indikator-Zufallsvariable $I_i$ für jeden Versuch $i \in \{1, \dots, N\}$ wie folgt:
$$I_i = \begin{cases} 1 & \text{falls } x_i^2 + y_i^2 \le 1 \\ 0 & \text{sonst} \end{cases}$$

Das Ergebnis des Algorithmus ist der Schätzer $\hat{\pi}_N$, definiert als:
$$\hat{\pi}_N = 4 \cdot \frac{1}{N} \sum_{i=1}^N I_i$$

## 2. Algebraische Charakterisierung

Die Korrektheit des Algorithmus beruht auf dem Gesetz der großen Zahlen. Betrachten wir den Flächeninhalt der Region $\mathcal{C} \subset \mathcal{S}$, die durch den Quadranten des Einheitskreises definiert ist:
$$\text{Area}(\mathcal{C}) = \iint_{\mathcal{S}} \mathbb{I}(x^2 + y^2 \le 1) \, dA = \int_0^1 \int_0^{\sqrt{1-x^2}} dy \, dx = \frac{\pi}{4}$$

Da die Punkte aus einer Gleichverteilung über $\mathcal{S}$ gezogen werden, ist die Wahrscheinlichkeit $p$, dass ein Punkt innerhalb von $\mathcal{C}$ liegt:
$$p = P(X_i \in \mathcal{C}) = \frac{\text{Area}(\mathcal{C})}{\text{Area}(\mathcal{S})} = \frac{\pi/4}{1} = \frac{\pi}{4}$$

Die Summe $S_N = \sum_{i=1}^N I_i$ folgt einer Binomialverteilung $B(N, p)$. Nach dem starken Gesetz der großen Zahlen konvergiert der Stichprobenmittelwert fast sicher gegen den Erwartungswert:
$$\lim_{N \to \infty} \frac{S_N}{N} = E[I_i] = p = \frac{\pi}{4}$$

Somit ist der Schätzer $\hat{\pi}_N = 4 \frac{S_N}{N}$ ein konsistenter Schätzer für $\pi$, da:
$$\lim_{N \to \infty} \hat{\pi}_N = 4 \left( \frac{\pi}{4} \right) = \pi$$

Die Varianz unseres Schätzers, welche die Präzision für ein endliches $N$ bestimmt, ist gegeben durch:
$$\text{Var}(\hat{\pi}_N) = 16 \cdot \text{Var}\left(\frac{S_N}{N}\right) = \frac{16}{N^2} \cdot Np(1-p) = \frac{16}{N} \left(\frac{\pi}{4}\right)\left(1 - \frac{\pi}{4}\right) = \frac{\pi(4-\pi)}{N}$$

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus führt eine Folge von $N$ Iterationen aus. In jeder Iteration $i$ werden die folgenden Operationen durchgeführt:
1. Generierung von zwei gleichverteilten Zufallsvariablen $x_i, y_i$.
2. Zwei Multiplikationen und eine Addition zur Berechnung von $x_i^2 + y_i^2$.
3. Ein Vergleich mit der Konstante $1.0$.
4. Eine bedingte Inkrementierung des Zählers `inside`.

Jede dieser Operationen wird in konstanter Zeit, $O(1)$, ausgeführt. Die gesamte Zeitkomplexität $T(N)$ ist die Summe des Arbeitsaufwands pro Iteration:
$$T(N) = \sum_{i=1}^N O(1) = O(N)$$
Somit ist der Algorithmus linear in Bezug auf die Anzahl der Stichproben $N$.

### Platzkomplexität
Der Algorithmus verwaltet eine feste Anzahl an skalaren Variablen: den Schleifenzähler $i$, den Akkumulator `inside` sowie die temporären Variablen $x$ und $y$. Diese Variablen belegen unabhängig von der Eingabegröße $N$ eine konstante Menge an Speicher.
$$S(N) = O(1)$$
Die Platzkomplexität ist daher konstant, $O(1)$, unter der Annahme, dass der Zustand des Zufallszahlengenerators als Objekt konstanter Größe behandelt wird.