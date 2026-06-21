# Formale mathematische Spezifikation: Punkt-im-Polygon (Ray-Casting)

## 1. Definitionen und Notation

Sei $\mathcal{P}$ ein einfaches Polygon, das durch eine geordnete Folge von $V$ Knoten in der euklidischen Ebene $\mathbb{R}^2$ definiert ist, notiert als $\mathcal{P} = \{v_0, v_1, \dots, v_{V-1}\}$, wobei $v_i = (x_i, y_i)$. Die Kanten des Polygons sind die Liniensegmente $e_i = \overline{v_i v_{i+1}}$ für $0 \le i < V$, wobei die Indizes modulo $V$ genommen werden.

Sei $P = (x_p, y_p) \in \mathbb{R}^2$ der zu testende Punkt. Wir definieren den Strahl $\mathcal{R}$, der in $P$ beginnt, als die Menge der Punkte:
$$\mathcal{R} = \{ (x, y) \in \mathbb{R}^2 \mid x \ge x_p, y = y_p \}$$

Wir definieren die Schnittmenge $\mathcal{I}$ als die Ansammlung von Punkten, an denen der Strahl $\mathcal{R}$ den Rand $\partial\mathcal{P} = \bigcup_{i=0}^{V-1} e_i$ schneidet:
$$\mathcal{I} = \mathcal{R} \cap \partial\mathcal{P}$$

Das Ziel ist es, die Zugehörigkeit von $P$ relativ zum Inneren $\text{int}(\mathcal{P})$ und zum Rand $\partial\mathcal{P}$ zu bestimmen.

## 2. Algebraische Charakterisierung

Der Algorithmus basiert auf dem Jordanschen Kurvensatz, der besagt, dass eine einfache geschlossene Kurve die Ebene in genau zwei Regionen unterteilt: ein Inneres und ein Äußeres. Der Ray-Casting-Algorithmus nutzt die Parität der Schnittanzahl, um die Region zu bestimmen.

### 2.1. Schnittbedingung
Für eine Kante $e_i$, die durch die Endpunkte $v_i = (x_i, y_i)$ und $v_{i+1} = (x_{i+1}, y_{i+1})$ definiert ist, schneidet der Strahl $\mathcal{R}$ die Kante $e_i$ genau dann, wenn:
1. Die $y$-Koordinate von $P$ strikt zwischen den $y$-Koordinaten der Kantenendpunkte liegt: $(y_i > y_p) \neq (y_{i+1} > y_p)$.
2. Die $x$-Koordinate des Schnittpunkts $x_{int}$ die Bedingung $x_{int} > x_p$ erfüllt.

Unter Verwendung linearer Interpolation ergibt sich die $x$-Koordinate des Schnittpunkts auf dem Liniensegment $e_i$ bei der Höhe $y_p$ zu:
$$x_{int} = x_i + (x_{i+1} - x_i) \frac{y_p - y_i}{y_{i+1} - y_i}$$

### 2.2. Die Even-Odd-Regel
Sei $\chi(e_i)$ eine Indikatorfunktion, sodass $\chi(e_i) = 1$, falls der Strahl $\mathcal{R}$ die Kante $e_i$ schneidet, und $\chi(e_i) = 0$ andernfalls. Der Punkt $P$ liegt genau dann im Inneren $\text{int}(\mathcal{P})$, wenn:
$$\left( \sum_{i=0}^{V-1} \chi(e_i) \right) \equiv 1 \pmod 2$$

### 2.3. Randbedingung
Der Punkt $P$ liegt auf dem Rand $\partial\mathcal{P}$, wenn ein $i \in \{0, \dots, V-1\}$ existiert, sodass $P \in e_i$. Dies ist erfüllt, wenn $P$ kollinear zu $v_i$ und $v_{i+1}$ ist und innerhalb der Bounding Box des Segments liegt:
$$\min(x_i, x_{i+1}) \le x_p \le \max(x_i, x_{i+1}) \land \min(y_i, y_{i+1}) \le y_p \le \max(y_i, y_{i+1})$$
$$\text{und } (x_{i+1} - x_i)(y_p - y_i) = (y_{i+1} - y_i)(x_p - x_i)$$

## 3. Komplexitätsanalyse

### 3.1. Zeitkomplexität
Der Algorithmus iteriert durch die Menge der Kanten $E = \{e_0, e_1, \dots, e_{V-1}\}$. Für jede Kante $e_i$ führt der Algorithmus eine konstante Anzahl an arithmetischen Operationen (Vergleiche, Additionen und Multiplikationen) aus, um die Schnittbedingung und die Randbedingung auszuwerten.

Sei $T(V)$ die gesamte Zeitkomplexität. Da jede Kante genau einmal verarbeitet wird, gilt:
$$T(V) = \sum_{i=0}^{V-1} O(1) = O(V)$$
Somit ist der Algorithmus linear in Bezug auf die Anzahl der Knoten $V$.

### 3.2. Platzkomplexität
Der Algorithmus verwaltet eine konstante Anzahl an skalaren Variablen: die aktuellen Knotenindizes $i$ und $j$, die Koordinaten des Testpunkts $P$ und ein boolesches Flag `inside`. Es werden keine zusätzlichen Datenstrukturen allokiert, deren Größe proportional zur Eingabegröße ist.

Die gesamte Platzkomplexität beträgt:
$$S(V) = O(1)$$
Dies stellt eine optimale Nutzung des zusätzlichen Speichers dar, da der Algorithmus in-place in Bezug auf die Repräsentation des Eingabepolygons arbeitet.