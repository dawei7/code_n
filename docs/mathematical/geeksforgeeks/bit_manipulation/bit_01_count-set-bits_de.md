# Formale mathematische Spezifikation: Count Set Bits (Brian Kernighans Algorithmus)

## 1. Definitionen und Notation

Sei $\mathbb{N}_0 = \mathbb{N} \cup \{0\}$ die Menge der nicht-negativen ganzen Zahlen. Für eine feste Wortbreite $W \in \mathbb{N}$ (typischerweise $W = 32$ oder $W = 64$) definieren wir den Definitionsbereich unserer Eingabe als den Ring der ganzen Zahlen modulo $2^W$, bezeichnet als:

$$\mathbb{Z}_{2^W} = \{0, 1, \dots, 2^W - 1\}$$

### 1.1 Binäre Darstellung
Für jede ganze Zahl $n \in \mathbb{Z}_{2^W}$ existiert eine eindeutige Bitfolge $\mathbf{b} = (b_{W-1}, b_{W-2}, \dots, b_0) \in \{0, 1\}^W$, sodass:

$$n = \sum_{i=0}^{W-1} b_i 2^i$$

Wir definieren die Projektionsfunktion $[\cdot]_i : \mathbb{Z}_{2^W} \to \{0, 1\}$, um das $i$-te Bit von $n$ zu extrahieren:

$$[n]_i = b_i$$

### 1.2 Hamming-Gewicht
Die Funktion für das Hamming-Gewicht (oder die Anzahl der gesetzten Bits) $w : \mathbb{Z}_{2^W} \to \{0, 1, \dots, W\}$ bildet eine ganze Zahl auf die Anzahl der gesetzten Bits ('1'en) in ihrer binären Darstellung ab:

$$w(n) = \sum_{i=0}^{W-1} [n]_i$$

### 1.3 Zustandsraum
Wir modellieren die Ausführung des Algorithmus als diskretes dynamisches System über einem Zustandsraum $\mathcal{S}$, der wie folgt definiert ist:

$$\mathcal{S} = \mathbb{Z}_{2^W} \times \{0, 1, \dots, W\}$$

Ein Zustand $s \in \mathcal{S}$ wird als Tupel $(x, c)$ dargestellt, wobei:
* $x \in \mathbb{Z}_{2^W}$ der aktuell veränderte Wert der Eingabe ist.
* $c \in \{0, 1, \dots, W\}$ der Akkumulator ist, der die gesetzten Bits zählt.

---

## 2. Algebraische Charakterisierung

### 2.1 Bitweise Operationen
Für beliebige $x, y \in \mathbb{Z}_{2^W}$ ist die bitweise AND-Operation, bezeichnet als $x \land y$, bitweise definiert als:

$$[x \land y]_i = [x]_i \cdot [y]_i \quad \forall i \in \{0, 1, \dots, W-1\}$$

### 2.2 Lemma: Die Identität zum Löschen des am weitesten rechts stehenden gesetzten Bits
Für jede von Null verschiedene ganze Zahl $x \in \mathbb{Z}_{2^W} \setminus \{0\}$ sei $j \in \{0, 1, \dots, W-1\}$ der Index des am wenigsten signifikanten gesetzten Bits (LSB) von $x$. Das heißt:

$$j = \min \{ i \in \{0, 1, \dots, W-1\} \mid [x]_i = 1 \}$$

Dann löscht der algebraische Übergang $x \leftarrow x \land (x - 1)$ genau das $j$-te Bit von $x$ und lässt alle anderen Bits unverändert.

#### Beweis:
Durch die Definition von $j$ können wir die binäre Darstellung von $x$ schreiben als:

$$x = \sum_{i=j+1}^{W-1} [x]_i 2^i + 2^j + \sum_{i=0}^{j-1} 0 \cdot 2^i = \sum_{i=j+1}^{W-1} [x]_i 2^i + 2^j$$

Die Subtraktion von $1$ von $x$ ergibt:

$$x - 1 = \sum_{i=j+1}^{W-1} [x]_i 2^i + 2^j - 1$$

Unter Verwendung der Identität für die geometrische Reihe $2^j - 1 = \sum_{i=0}^{j-1} 2^i$ schreiben wir $x - 1$ um als:

$$x - 1 = \sum_{i=j+1}^{W-1} [x]_i 2^i + \sum_{i=0}^{j-1} 2^i$$

Nun werten wir die bitweise AND-Operation $y = x \land (x - 1)$ aus, indem wir die Bits $[y]_i$ für drei verschiedene Intervalle von $i$ analysieren:

1. **Für $i > j$:**
   $$[y]_i = [x]_i \land [x - 1]_i = [x]_i \land [x]_i = [x]_i$$

2. **Für $i = j$:**
   $$[y]_j = [x]_j \land [x - 1]_j = 1 \land 0 = 0$$

3. **Für $i < j$:**
   $$[y]_i = [x]_i \land [x - 1]_i = 0 \land 1 = 0$$

Durch Kombination dieser Fälle ergibt sich die binäre Darstellung von $y$ zu:

$$y = \sum_{i=j+1}^{W-1} [x]_i 2^i$$

Vergleichen wir dies mit der Darstellung von $x$, stellen wir fest:

$$w(y) = w(x) - 1$$

Damit ist der Beweis vollständig. $\blacksquare$

### 2.3 Zustandsübergangssystem
Wir definieren die Zustandsübergangsfunktion $T : \mathcal{S} \to \mathcal{S}$ für jeden Zustand $(x, c) \in \mathcal{S}$, wobei $x \neq 0$:

$$T(x, c) = (x \land (x - 1), c + 1)$$

Der Algorithmus erzeugt eine Folge von Zuständen $(s_0, s_1, s_2, \dots)$ ausgehend vom Anfangszustand:

$$s_0 = (n, 0)$$

Die Folge ist rekursiv definiert durch:

$$s_{k} = T(s_{k-1}) \quad \text{für } x_{k-1} \neq 0$$

### 2.4 Schleifeninvariante
Für jeden vom Algorithmus erzeugten Zustand $s_k = (x_k, c_k)$ gilt die folgende Invariante:

$$\mathcal{I}(s_k) \iff w(n) = w(x_k) + c_k$$

#### Beweis durch vollständige Induktion:
* **Induktionsanfang ($k = 0$):**
  $$w(x_0) + c_0 = w(n) + 0 = w(n)$$
  Die Invariante gilt.

* **Induktionsschritt:**
  Angenommen, $\mathcal{I}(s_k)$ gilt für ein $k \ge 0$ und $x_k \neq 0$. Der nächste Zustand ist $s_{k+1} = (x_{k+1}, c_{k+1}) = (x_k \land (x_k - 1), c_k + 1)$.
  Unter Verwendung des in Abschnitt 2.2 bewiesenen Lemmas erhalten wir $w(x_{k+1}) = w(x_k) - 1$.
  Daher:
  $$w(x_{k+1}) + c_{k+1} = (w(x_k) - 1) + (c_k + 1) = w(x_k) + c_k$$
  Nach der Induktionsvoraussetzung gilt $w(x_k) + c_k = w(n)$, folglich:
  $$w(x_{k+1}) + c_{k+1} = w(n)$$
  Die Invariante $\mathcal{I}(s_{k+1})$ gilt. $\blacksquare$

### 2.5 Terminierung und Korrektheit
Da $w(x_k) \in \mathbb{N}_0$ und $w(x_{k+1}) = w(x_k) - 1$ gilt, ist die Folge der Hamming-Gewichte $\{w(x_k)\}_{k=0}^{\infty}$ streng monoton fallend:

$$w(x_k) = w(n) - k$$

Da $w(x_k) \ge 0$ für alle $k$ gilt, muss die Folge nach einer endlichen Anzahl von Schritten $K$ terminieren, bei denen $x_K = 0$ ist.
Die Terminierungsbedingung $x_K = 0$ impliziert $w(x_K) = 0$.
Setzt man dies in die Schleifeninvariante $\mathcal{I}(s_K)$ ein:

$$w(n) = w(x_K) + c_K = 0 + c_K = c_K$$

Somit enthält der Akkumulator $c_K$ bei Terminierung exakt das Hamming-Gewicht der Eingabe $n$.

---

## 3. Komplexitätsanalyse

### 3.1 Zeitkomplexität
Sei $K = w(n)$ die Anzahl der gesetzten Bits in der Eingabe $n \in \mathbb{Z}_{2^W}$.

* **Anzahl der Iterationen:** Die Schleife terminiert, wenn $x_k = 0$. Da $w(x_k) = w(n) - k$, ist die Terminierungsbedingung $w(x_K) = 0$ genau dann erfüllt, wenn $K = w(n)$ Iterationen ausgeführt wurden.
* **Aufwand pro Iteration:** Jede Iteration führt eine konstante Anzahl primitiver Operationen aus:
  1. Eine Subtraktion: $x_k - 1$
  2. Ein bitweises AND: $x_k \land (x_k - 1)$
  3. Eine Addition: $c_k + 1$
  4. Eine Zuweisung und ein Vergleich: $x_{k+1} \leftarrow x_k \land (x_k - 1)$ und Prüfung, ob $x_{k+1} \neq 0$.

Im Word-RAM-Modell benötigt jede dieser Operationen $O(1)$ Zeit. Somit ergibt sich die gesamte Zeitkomplexität $T(n)$ zu:

$$T(n) = \sum_{k=1}^{K} O(1) = \Theta(K)$$

* **Bestfall:** Tritt ein, wenn $n = 0$, was $K = 0$ ergibt.
  $$T_{\text{best}}(n) = \Theta(1)$$
* **Schlechtester Fall:** Tritt ein, wenn alle Bits gesetzt sind ($n = 2^W - 1$), was $K = W$ ergibt.
  $$T_{\text{worst}}(n) = \Theta(W)$$

Für eine feste Wortbreite $W$ (z. B. $W = 32$ oder $W = 64$) ist die Zeitkomplexität in Bezug auf die Größe von $n$ durch $O(1)$ beschränkt, asymptotisch in Bezug auf das Hamming-Gewicht jedoch exakt $\Theta(K)$.

### 3.2 Platzkomplexität
Der Algorithmus wird in-place ausgeführt und benötigt nur Speicherplatz für die Zustandsvariablen $(x, c) \in \mathcal{S}$.

* **Zusätzlicher Speicherplatz:** Die Variablen $x$ und $c$ benötigen:
  $$\text{Bits}(x) = W$$
  $$\text{Bits}(c) = \lceil \log_2(W + 1) \rceil$$
  Da $W$ ein fester Hardware-Parameter ist, beträgt die zusätzliche Platzkomplexität:
  $$S_{\text{aux}}(n) = O(1) \text{ Wörter}$$

* **Gesamter Speicherplatz:** Unter Einbeziehung der Eingabe $n$ beträgt die gesamte Platzkomplexität:
  $$S_{\text{total}}(n) = O(1) \text{ Wörter}$$