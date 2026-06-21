# Formale mathematische Spezifikation: Minimale Bit-Flips zur Konvertierung einer Zahl

## 1. Definitionen und Notation

Sei $\mathbb{Z}_{2^W} = \{0, 1, \dots, 2^W - 1\}$ die Menge der nicht-negativen Ganzzahlen, die innerhalb eines $W$-Bit-Computerworts darstellbar sind, wobei $W \in \mathbb{N}$ die Wortbreite ist (typischerweise $W = 32$ oder $W = 64$).

### Binäre Darstellung
Für jede Ganzzahl $x \in \mathbb{Z}_{2^W}$ ist ihre eindeutige $W$-Bit-Binärdarstellung durch den Vektor $\mathbf{x} = (x_{W-1}, x_{W-2}, \dots, x_0) \in \{0, 1\}^W$ gegeben, sodass:
$$x = \sum_{i=0}^{W-1} x_i 2^i$$
wobei $x_i \in \{0, 1\}$ das $i$-te Bit von $x$ repräsentiert.

### Bitweise Operatoren
Wir definieren die folgenden binären Operatoren über $\mathbb{Z}_{2^W}$:
1. **Bitweises XOR ($\oplus$):** 
   $$(x \oplus y)_i = x_i \oplus y_i \equiv (x_i + y_i) \pmod 2 \quad \forall i \in \{0, \dots, W-1\}$$
2. **Bitweises AND ($\wedge$):**
   $$(x \wedge y)_i = x_i \cdot y_i \quad \forall i \in \{0, \dots, W-1\}$$

### Hamming-Distanz und Hamming-Gewicht
* **Hamming-Distanz:** Die Hamming-Distanz $d_H: \mathbb{Z}_{2^W} \times \mathbb{Z}_{2^W} \to \{0, \dots, W\}$ misst die Anzahl der Positionen, an denen sich die entsprechenden Bits zweier Ganzzahlen unterscheiden:
  $$d_H(a, b) = \sum_{i=0}^{W-1} (a_i \oplus b_i)$$
* **Hamming-Gewicht:** Das Hamming-Gewicht (oder die Population Count) $\operatorname{wt}: \mathbb{Z}_{2^W} \to \{0, \dots, W\}$ ist die Anzahl der von Null verschiedenen Bits in einer Ganzzahl:
  $$\operatorname{wt}(z) = \sum_{i=0}^{W-1} z_i$$

### Problemformulierung
Gegeben seien zwei Ganzzahlen $a, b \in \mathbb{Z}_{2^W}$. Das Ziel ist es, die minimale Anzahl an Bit-Flips zu berechnen, die erforderlich sind, um $a$ in $b$ zu konvertieren. Dies ist mathematisch äquivalent zur Berechnung der Hamming-Distanz zwischen $a$ und $b$:
$$f(a, b) = d_H(a, b) = \operatorname{wt}(a \oplus b)$$

---

## 2. Algebraische Charakterisierung und Korrektheit

Der Algorithmus berechnet $f(a, b)$ in zwei unterschiedlichen Phasen:
1. **Isolierung der Diskrepanzen:** Berechnung der bitweisen XOR-Differenz $z = a \oplus b$.
2. **Population Count:** Berechnung von $\operatorname{wt}(z)$ unter Verwendung des Algorithmus von Brian Kernighan.

### Algebraische Eigenschaften der Transition nach Brian Kernighan
Sei $\operatorname{lsb}(x)$ der Index des niederwertigsten gesetzten Bits einer von Null verschiedenen Ganzzahl $x \in \mathbb{Z}_{2^W} \setminus \{0\}$:
$$\operatorname{lsb}(x) = \min \{ i \in \{0, \dots, W-1\} \mid x_i = 1 \}$$

Wir können $x$ algebraisch ausdrücken als:
$$x = y \cdot 2^{\operatorname{lsb}(x) + 1} + 2^{\operatorname{lsb}(x)}$$
wobei $y \in \mathbb{Z}_{2^{W - \operatorname{lsb}(x) - 1}}$.

Die Subtraktion von $1$ von $x$ ergibt:
$$x - 1 = y \cdot 2^{\operatorname{lsb}(x) + 1} + 2^{\operatorname{lsb}(x)} - 1 = y \cdot 2^{\operatorname{lsb}(x) + 1} + \sum_{i=0}^{\operatorname{lsb}(x)-1} 2^i$$

Anwendung des bitweisen AND-Operators auf $x$ und $x-1$:
$$x \wedge (x - 1) = \left( y \cdot 2^{\operatorname{lsb}(x) + 1} + 2^{\operatorname{lsb}(x)} \right) \wedge \left( y \cdot 2^{\operatorname{lsb}(x) + 1} + \sum_{i=0}^{\operatorname{lsb}(x)-1} 2^i \right)$$

Da das bitweise AND von $2^{\operatorname{lsb}(x)}$ und $\sum_{i=0}^{\operatorname{lsb}(x)-1} 2^i$ gleich $0$ ist, vereinfacht sich der Ausdruck zu:
$$x \wedge (x - 1) = y \cdot 2^{\operatorname{lsb}(x) + 1}$$

Dies beweist, dass die Transition $x \leftarrow x \wedge (x - 1)$ exakt das niederwertigste gesetzte Bit von $x$ auf $0$ setzt, während alle anderen höherwertigen Bits unverändert bleiben. Folglich gilt:
$$\operatorname{wt}(x \wedge (x - 1)) = \operatorname{wt}(x) - 1$$

### Formale Schleifeninvariante
Sei $z^{(0)} = a \oplus b$ der Anfangszustand und $c^{(0)} = 0$ der Anfangszähler. Die Zustandsfolge $(z^{(j)}, c^{(j)})$ am Ende der $j$-ten Iteration der Schleife ist rekursiv definiert durch:
$$z^{(j+1)} = z^{(j)} \wedge (z^{(j)} - 1)$$
$$c^{(j+1)} = c^{(j)} + 1$$

**Invariante:** Für jeden Iterationsschritt $j \ge 0$, in dem $z^{(j)}$ definiert ist, gilt:
$$\operatorname{wt}(z^{(j)}) = \operatorname{wt}(z^{(0)}) - j \quad \text{und} \quad c^{(j)} = j$$

#### Beweis durch vollständige Induktion:
* **Induktionsanfang ($j=0$):** 
  $$\operatorname{wt}(z^{(0)}) = \operatorname{wt}(z^{(0)}) - 0 \quad \text{und} \quad c^{(0)} = 0$$
  Die Invariante gilt trivialerweise.
* **Induktionsschritt:** Angenommen, die Invariante gilt für $j = k$, das heißt $\operatorname{wt}(z^{(k)}) = \operatorname{wt}(z^{(0)}) - k$ und $c^{(k)} = k$. Falls $z^{(k)} \neq 0$, wird die Schleife für den Schritt $k+1$ ausgeführt:
  $$\operatorname{wt}(z^{(k+1)}) = \operatorname{wt}(z^{(k)} \wedge (z^{(k)} - 1)) = \operatorname{wt}(z^{(k)}) - 1$$
  Einsetzen der Induktionsvoraussetzung:
  $$\operatorname{wt}(z^{(k+1)}) = \left( \operatorname{wt}(z^{(0)}) - k \right) - 1 = \operatorname{wt}(z^{(0)}) - (k+1)$$
  Analog für den Zähler:
  $$c^{(k+1)} = c^{(k)} + 1 = k + 1$$
  Die Invariante gilt für $j = k+1$. $\square$

### Terminierung und Korrektheit
Da $\operatorname{wt}(z^{(j)}) \in \{0, \dots, W\}$ eine streng monoton fallende Folge nicht-negativer Ganzzahlen ist, existiert eine eindeutige endliche Ganzzahl $K = \operatorname{wt}(z^{(0)})$, sodass $z^{(K)} = 0$.

Im Schritt $j = K$ ist die Schleifenabbruchbedingung $z^{(j)} = 0$ erfüllt. Der finale Wert des Zählers ist:
$$c^{(K)} = K = \operatorname{wt}(z^{(0)}) = \operatorname{wt}(a \oplus b) = d_H(a, b)$$

Dies garantiert sowohl die Terminierung des Algorithmus als auch die Korrektheit des Ergebnisses.

---

## 3. Komplexitätsanalyse

### Zeitkomplexität
Sei $K = d_H(a, b)$ die Hamming-Distanz zwischen $a$ und $b$.

1. **XOR-Operation:** Die initiale Berechnung $z = a \oplus b$ ist eine primitive bitweise Operation, die im Word-RAM-Modell $\Theta(1)$ Zeit benötigt.
2. **Schleifeniterationen:** Die Schleife wird exakt $K$-mal ausgeführt. In jeder Iteration $j \in \{0, \dots, K-1\}$ führt der Algorithmus Folgendes aus:
   * Eine Subtraktion: $z^{(j)} - 1$
   * Ein bitweises AND: $z^{(j)} \wedge (z^{(j)} - 1)$
   * Eine Inkrementierung: $c^{(j)} + 1$
   * Ein Vergleich: $z^{(j+1)} \neq 0$
   
   Jede dieser Operationen benötigt auf Standard-Hardwarearchitekturen $\Theta(1)$ Zeit.

Somit ergibt sich die gesamte Zeitkomplexität zu:
$$T(W, K) = \Theta(1) + \sum_{j=0}^{K-1} \Theta(1) = \Theta(K)$$

#### Asymptotische Schranken:
* **Bestfall:** $\Theta(1)$, wenn $a = b$ (somit $K = 0$). Die Schleifenbedingung ist initial falsch und der Algorithmus terminiert sofort.
* **Schlechtester Fall:** $\Theta(W)$, wenn $a = \sim b$ (bitweises Komplement, somit $K = W$).
* **Durchschnittlicher Fall:** Unter der Annahme, dass $a$ und $b$ gleichverteilt zufällig aus $\mathbb{Z}_{2^W}$ gewählt werden, ist jedes Bit von $z = a \oplus b$ ein unabhängiger Bernoulli-Versuch mit Parameter $p = 0.5$. Die erwartete Hamming-Distanz ist:
  $$\mathbb{E}[K] = \sum_{i=0}^{W-1} \mathbb{E}[z_i] = \frac{W}{2}$$
  Daher ist die durchschnittliche Zeitkomplexität $\Theta(W)$.

*Hinweis zur Hardware-Optimierung:* Falls die Zielarchitektur einen dedizierten Hardware-Befehl für die Population Count unterstützt (z. B. `POPCNT` bei x86 oder `VCNT` bei ARM), kann das Hamming-Gewicht parallel mittels Bit-Permutationsnetzwerken berechnet werden, was die Zeitkomplexität unabhängig von $K$ auf $\Theta(1)$ reduziert.

### Platzkomplexität
Der Algorithmus arbeitet in-place und benötigt Speicherplatz nur für eine feste Anzahl an Variablen: die Eingabewerte $a, b$, die Zwischendifferenz $z$ und den Zähler $c$.

* **Zusätzliche Platzkomplexität:** $\Theta(1)$ Wörter Speicher, was $\Theta(W)$ Bits entspricht.
* **Gesamte Platzkomplexität:** $\Theta(1)$ Wörter Speicher zur Speicherung der Eingaben und des Ausführungszustands.