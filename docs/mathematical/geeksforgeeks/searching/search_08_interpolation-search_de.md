# Formale mathematische Spezifikation: Interpolationssuche

## 1. Definitionen und Notation

Sei $A = [a_0, a_1, \dots, a_{n-1}]$ eine Folge von Elementen aus einer total geordneten Menge $(\mathcal{X}, \leq)$, sodass $a_i \leq a_{i+1}$ für alle $0 \leq i < n-1$ gilt. Wir definieren den Suchraum als die Indexmenge $\mathcal{I} = \{0, 1, \dots, n-1\}$.

Gegeben ein Zielwert $t \in \mathcal{X}$, ist das Ziel, einen Index $k \in \mathcal{I}$ zu bestimmen, sodass $a_k = t$, oder einen Sentinel-Wert $\bot \notin \mathcal{I}$ zurückzugeben, falls kein solches $k$ existiert.

Der Algorithmus verwaltet ein dynamisches Teilintervall $[L, R] \subseteq \mathcal{I}$, das initial als $[0, n-1]$ gesetzt wird. In jeder Iteration definieren wir den Zustandsraum $\mathcal{S} = \{(L, R) \in \mathcal{I}^2 \mid L \leq R\}$.

## 2. Algebraische Charakterisierung

Der Algorithmus basiert auf der Annahme, dass die Werte $a_i$ linear bezüglich ihrer Indizes $i$ verteilt sind. Wir definieren die Sondenposition $P$ als eine lineare Interpolation zwischen den Werten an den Grenzen des aktuellen Intervalls $[L, R]$:

$$P = L + \left\lfloor \frac{(t - a_L)(R - L)}{a_R - a_L} \right\rfloor$$

### Schleifeninvariante
Damit der Algorithmus korrekt ist, muss zu Beginn jeder Iteration die folgende Invariante gelten:
Wenn $t \in \{a_i \mid L \leq i \leq R\}$, dann existiert ein $k \in [L, R]$, sodass $a_k = t$.

### Übergangslogik
Der Zustand $(L, R)$ wird basierend auf dem Vergleich zwischen $a_P$ und $t$ aktualisiert:
1. Wenn $a_P = t$, terminiert der Algorithmus und gibt $P$ zurück.
2. Wenn $a_P < t$, ist der neue Zustand $(P + 1, R)$.
3. Wenn $a_P > t$, ist der neue Zustand $(L, P - 1)$.

Der Algorithmus terminiert, wenn $L > R$ oder $t < a_L$ oder $t > a_R$ gilt; in diesem Fall wird $\bot$ zurückgegeben.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität hängt von der Verteilung der Elemente in $A$ ab.

**Durchschnittlicher Fall:**
Für eine Menge von $n$ Elementen, die aus einer Gleichverteilung stammen, beträgt die erwartete Anzahl der Sonden, die zum Auffinden des Ziels erforderlich sind, $O(\log(\log n))$. Dies leitet sich aus der Rekurrenz für die erwartete Anzahl der nach einer Sonde verbleibenden Elemente ab:
$$E[n_{k+1}] \approx \sqrt{E[n_k]}$$
Durch Lösen dieser Rekurrenz finden wir, dass die Anzahl der Iterationen $k$ die Bedingung $n^{(1/2)^k} \approx 2$ erfüllt, was $k \approx \log_2(\log_2 n)$ ergibt. Somit beträgt die durchschnittliche Zeitkomplexität $\Theta(\log(\log n))$.

**Schlechtester Fall:**
Bei stark nicht-uniformen Verteilungen (z. B. exponentielles Wachstum, bei dem $a_i = 2^i$) kann die Interpolationsformel konsistent $P = L$ oder $P = R$ ergeben. In solchen Fällen reduziert sich der Suchraum pro Iteration nur um ein Element:
$$T(n) = T(n-1) + O(1)$$
Dies führt zu einer Zeitkomplexität im schlechtesten Fall von $O(n)$, wodurch der Algorithmus effektiv auf eine lineare Suche reduziert wird.

### Platzkomplexität
Der Algorithmus arbeitet in-place und benötigt nur eine konstante Anzahl an Hilfsvariablen ($L, R, P, \text{value}$), um die aktuellen Grenzen und den Sondenindex zu speichern.

Sei $S(n)$ die zusätzliche Platzkomplexität:
$$S(n) = \text{space}(\text{pointers}) + \text{space}(\text{scalars}) = O(1) + O(1) = O(1)$$
Somit beträgt die Platzkomplexität $O(1)$.