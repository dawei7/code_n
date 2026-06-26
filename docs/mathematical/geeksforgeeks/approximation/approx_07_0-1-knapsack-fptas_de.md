# Formale mathematische Spezifikation: 0-1 Knapsack (FPTAS-Approximation)

## 1. Definitionen und Notation

Sei $I = \{1, 2, \dots, n\}$ eine Menge von $n \in \mathbb{N}_{>0}$ Objekten. Jedes Objekt $i \in I$ ist durch ein Tupel $(w_i, v_i)$ charakterisiert, wobei:
*   $w_i \in \mathbb{R}_{>0}$ das **Gewicht** des Objekts $i$ repräsentiert.
*   $v_i \in \mathbb{R}_{>0}$ den **Wert** des Objekts $i$ repräsentiert.

Sei $W \in \mathbb{R}_{>0}$ die maximale Gewichtskapazität des Rucksacks. Ohne Beschränkung der Allgemeinheit nehmen wir an, dass $w_i \le W$ für alle $i \in I$ gilt, da jedes Objekt, das die Kapazität überschreitet, in einem Vorverarbeitungsschritt verworfen werden kann.

Sei $x = (x_1, x_2, \dots, x_n) \in \{0, 1\}^n$ ein Entscheidungsvektor, wobei $x_i = 1$, falls Objekt $i$ ausgewählt wird, und $x_i = 0$ andernfalls. Der zulässige Bereich $\mathcal{X}$ ist definiert als:
$$\mathcal{X} = \left\{ x \in \{0, 1\}^n \;\middle|\; \sum_{i=1}^n w_i x_i \le W \right\}$$

Das Ziel ist die Maximierung des Gesamtwerts der ausgewählten Objekte. Der optimale Lösungswert $OPT$ ist definiert als:
$$OPT = \max_{x \in \mathcal{X}} \sum_{i=1}^n v_i x_i$$

Sei $\epsilon \in (0, 1)$ der benutzerdefinierte Approximations-Toleranzparameter. Ein **Fully Polynomial-Time Approximation Scheme (FPTAS)** ist ein Algorithmus, der eine zulässige Lösung $x^{approx} \in \mathcal{X}$ ausgibt, die folgende Bedingung erfüllt:
$$\sum_{i=1}^n v_i x^{approx}_i \ge (1 - \epsilon) OPT$$
mit einer Laufzeit, die durch ein Polynom in $n$ und $1/\epsilon$ beschränkt ist.

---

## 2. Algebraische Charakterisierung

Um die Rechenkomplexität von der Größenordnung der Werte $v_i$ und der Kapazität $W$ zu entkoppeln, skaliert und rundet das FPTAS die Objektwerte.

### 2.1 Wertskalierung und Quantisierung
Sei $v_{\max} = \max_{i \in I} v_i$. Da $w_i \le W$ für alle $i$ gilt, muss die optimale Lösung mindestens ein Objekt enthalten, woraus folgt:
$$v_{\max} \le OPT \le n \cdot v_{\max}$$

Wir definieren den Skalierungsfaktor $K \in \mathbb{R}_{>0}$ als:
$$K = \frac{\epsilon \cdot v_{\max}}{n}$$

Für jedes Objekt $i \in I$ definieren wir seinen skalierten ganzzahligen Wert $v'_i \in \mathbb{Z}_{\ge 0}$ mittels der Floor-Funktion:
$$v'_i = \left\lfloor \frac{v_i}{K} \right\rfloor$$

### 2.2 Duale dynamische Programmierung (wertbasierte DP)
Da die skalierten Werte $v'_i$ Ganzzahlen sind, können wir das minimale Gewicht berechnen, das erforderlich ist, um einen bestimmten skalierten Wert zu erreichen. Sei $V'_{max}$ die obere Schranke für die Summe der skalierten Werte:
$$V'_{max} = \sum_{i=1}^n v'_i \le \sum_{i=1}^n \frac{v_i}{K} \le \frac{n \cdot v_{\max}}{K} = \frac{n^2}{\epsilon}$$

Wir definieren den Zustandsraum $\mathcal{S} = \{0, \dots, n\} \times \{0, \dots, V'_{max}\}$. Sei $DP(i, v)$ das minimale Gewicht, das erforderlich ist, um einen skalierten Gesamtwert von exakt $v$ unter Verwendung einer Teilmenge der ersten $i$ Objekte zu erreichen.

#### Induktionsanfang
$$\forall v \in \{1, \dots, V'_{max}\}, \quad DP(0, v) = \infty$$
$$DP(0, 0) = 0$$

#### Rekursionsgleichung
Für $i \in \{1, \dots, n\}$ und $v \in \{0, \dots, V'_{max}\}$:
$$DP(i, v) = \begin{cases} 
DP(i-1, v) & \text{falls } v < v'_i \\
\min\left( DP(i-1, v), \, DP(i-1, v - v'_i) + w_i \right) & \text{falls } v \ge v'_i 
\end{cases}$$

### 2.3 Optimierung und Rekonstruktion
Der maximale skalierte Wert, der innerhalb der Kapazität $W$ erreichbar ist, beträgt:
$$V'_{approx} = \max \left\{ v \in \{0, \dots, V'_{max}\} \;\middle|\; DP(n, v) \le W \right\}$$

Der approximative Entscheidungsvektor $x^{approx} \in \mathcal{X}$ wird durch Backtracking vom Zustand $(n, V'_{approx})$ rekonstruiert. Der endgültige Rückgabewert ist:
$$ALG = \sum_{i=1}^n v_i x^{approx}_i$$

### 2.4 Mathematischer Beweis der Approximationsgarantie
Wir beweisen, dass $ALG \ge (1 - \epsilon) OPT$ gilt.

Aufgrund der Definition der Floor-Funktion gilt für jedes Objekt $i \in I$:
$$\frac{v_i}{K} - 1 < \left\lfloor \frac{v_i}{K} \right\rfloor \le \frac{v_i}{K} \implies v_i - K < K v'_i \le v_i$$

Sei $x^* \in \mathcal{X}$ der optimale Entscheidungsvektor für die ursprüngliche Instanz und $x^{approx} \in \mathcal{X}$ der optimale Entscheidungsvektor für die skalierte Instanz. Aufgrund der Optimalität unter den skalierten Werten gilt:
$$\sum_{i=1}^n v'_i x^{approx}_i \ge \sum_{i=1}^n v'_i x^*_i$$

Multiplikation beider Seiten mit $K$:
$$\sum_{i=1}^n K v'_i x^{approx}_i \ge \sum_{i=1}^n K v'_i x^*_i$$

Unter Anwendung der unteren und oberen Schranken von $K v'_i$:
$$ALG = \sum_{i=1}^n v_i x^{approx}_i \ge \sum_{i=1}^n K v'_i x^{approx}_i \ge \sum_{i=1}^n K v'_i x^*_i \ge \sum_{i=1}^n (v_i - K) x^*_i$$

Ausmultiplizieren des rechten Terms:
$$ALG \ge \sum_{i=1}^n v_i x^*_i - K \sum_{i=1}^n x^*_i = OPT - K \sum_{i=1}^n x^*_i$$

Da $x^*_i \in \{0, 1\}$, gilt $\sum_{i=1}^n x^*_i \le n$. Durch Einsetzen dieses Wertes und der Definition von $K$:
$$ALG \ge OPT - n K = OPT - n \left( \frac{\epsilon \cdot v_{\max}}{n} \right) = OPT - \epsilon \cdot v_{\max}$$

Da $v_{\max} \le OPT$:
$$ALG \ge OPT - \epsilon \cdot OPT = (1 - \epsilon) OPT$$

Damit ist der Beweis erbracht.

---

## 3. Komplexitätsanalyse

### 3.1 Zeitkomplexität
Die Zeitkomplexität des Algorithmus wird durch die Konstruktion der Tabelle für die dynamische Programmierung dominiert.

1.  **Skalierungsschritt:** Die Berechnung von $v_{\max}$ und die Skalierung aller $n$ Werte auf $v'_i$ benötigt $\Theta(n)$ Operationen.
2.  **Größe der DP-Tabelle:** Die Tabelle hat die Dimensionen $n \times (V'_{max} + 1)$. Die obere Schranke für $V'_{max}$ ist:
    $$V'_{max} \le \frac{n^2}{\epsilon}$$
    Somit ist die Gesamtzahl der Zustände beschränkt durch:
    $$| \mathcal{S} | \le n \cdot \left( \frac{n^2}{\epsilon} + 1 \right) = O\left( \frac{n^3}{\epsilon} \right)$$
3.  **Zustandsübergänge:** Jeder Zustandsübergang $DP(i, v)$ erfordert $O(1)$ Operationen (ein einzelner Zugriff und eine Minimierung).
4.  **Rekonstruktion:** Das Finden von $V'_{approx}$ erfordert das Durchsuchen der letzten Zeile der DP-Tabelle, was $O(V'_{max}) = O(n^2/\epsilon)$ Schritte benötigt. Das Backtracking zur Ermittlung der ausgewählten Objekte benötigt $O(n)$ Schritte.

Summiert man diese Komponenten, ergibt sich die gesamte Zeitkomplexität zu:
$$\mathcal{T}(n, \epsilon) = \Theta\left( \frac{n^3}{\epsilon} \right)$$

### 3.2 Platzkomplexität

#### Naive Implementierung
Das Speichern der gesamten 2D-DP-Tabelle, um ein direktes Backtracking zu ermöglichen, erfordert:
$$\mathcal{S}_{naive}(n, \epsilon) = \Theta\left( n \cdot V'_{max} \right) = \Theta\left( \frac{n^3}{\epsilon} \right) \text{ Hilfsspeicher.}$$

#### Speicheroptimierte Implementierung
Da die Rekursionsgleichung für Zeile $i$ nur von Zeile $i-1$ abhängt, können wir den optimalen Wert unter Verwendung von nur zwei Zeilen (oder einer einzelnen Zeile, die in umgekehrter Reihenfolge von $V'_{max}$ bis $v'_i$ aktualisiert wird) berechnen. Dies reduziert die Platzkomplexität des Hilfsspeichers auf:
$$\mathcal{S}_{optimized}(n, \epsilon) = \Theta\left( V'_{max} \right) = \Theta\left( \frac{n^2}{\epsilon} \right)$$

Falls eine Rekonstruktion der Objekte innerhalb dieser reduzierten Speicherschranke erforderlich ist, können Divide-and-Conquer-Techniken zur Speicherreduktion (wie der Hirschberg-Algorithmus) angewendet werden, um den Speicherbedarf bei $O(n^2/\epsilon)$ zu halten, während die Zeitkomplexität bei $O(n^3/\epsilon)$ bleibt.