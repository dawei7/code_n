# Formale mathematische Spezifikation: Fractional Knapsack (Greedy-Schranke)

## 1. Definitionen und Notation

Das Fractional Knapsack Problem ist ein kontinuierliches Optimierungsproblem. Wir modellieren die Probleminstanz, den zulässigen Bereich und die Zielfunktion mithilfe der folgenden mathematischen Formalismen.

### 1.1 Probleminstanz
Eine Probleminstanz ist definiert durch ein 4-Tupel $\mathcal{P} = (I, \mathbf{v}, \mathbf{w}, W)$, wobei:
*   $I = \{1, 2, \dots, n\}$ eine endliche Menge von $n \in \mathbb{N}^+$ Objekten ist.
*   $\mathbf{v} = (v_1, v_2, \dots, v_n) \in (\mathbb{R}^+)^n$ der Vektor der Objektwerte ist, wobei $v_i > 0$ den Nutzen oder Wert des Objekts $i$ darstellt.
*   $\mathbf{w} = (w_1, w_2, \dots, w_n) \in (\mathbb{R}^+)^n$ der Vektor der Objektgewichte ist, wobei $w_i > 0$ das physische Gewicht des Objekts $i$ darstellt.
*   $W \in \mathbb{R}_{\ge 0}$ die maximale Gewichtskapazität des Rucksacks ist.

### 1.2 Entscheidungsvariablen und Zustandsraum
Im Gegensatz zum 0-1 Knapsack Problem, bei dem die Auswahl binär ist, erlaubt die fraktionale Variante eine kontinuierliche Aufteilung der Objekte.
*   Sei $\mathbf{x} = (x_1, x_2, \dots, x_n) \in [0, 1]^n$ der Allokationsvektor, wobei $x_i$ den Anteil des Objekts $i$ bezeichnet, der in den Rucksack gelegt wird.
*   Der zulässige Bereich (oder Zustandsraum) $\mathcal{S}(W)$ ist als konvexes Polytop definiert:
    $$\mathcal{S}(W) = \left\{ \mathbf{x} \in [0, 1]^n \;\middle|\; \sum_{i=1}^n w_i x_i \le W \right\}$$

### 1.3 Zielfunktion
Das Ziel ist die Maximierung des Gesamtwerts der ausgewählten Anteile. Wir definieren die Zielfunktion $f: [0, 1]^n \to \mathbb{R}_{\ge 0}$ als:
$$f(\mathbf{x}) = \sum_{i=1}^n v_i x_i$$

Das Optimierungsproblem ist formuliert als:
$$\text{Maximiere } f(\mathbf{x}) \quad \text{unter der Bedingung } \mathbf{x} \in \mathcal{S}(W)$$

### 1.4 Wertdichte (Effizienz)
Für jedes Objekt $i \in I$ definieren wir dessen Wertdichte (oder Effizienzverhältnis) $r_i$ als:
$$r_i = \frac{v_i}{w_i}$$
Die Dichte $r_i \in \mathbb{R}^+$ repräsentiert den Nutzen pro Gewichtseinheit des Objekts $i$.

---

## 2. Algebraische Charakterisierung und Korrektheit

Der Greedy-Algorithmus löst dieses kontinuierliche Optimierungsproblem, indem er die Objekte in nicht-aufsteigender Reihenfolge ihrer Wertdichten sortiert.

### 2.1 Permutation und Sortierung
Sei $\pi: I \to I$ eine bijektive Abbildung (Permutation), die die Objekte nach Wertdichte in nicht-aufsteigender Reihenfolge sortiert:
$$r_{\pi(1)} \ge r_{\pi(2)} \ge \dots \ge r_{\pi(n)}$$

Zur Vereinfachung der Notation nehmen wir ohne Beschränkung der Allgemeinheit an, dass die Objekte bereits so sortiert sind, dass gilt:
$$\frac{v_1}{w_1} \ge \frac{v_2}{w_2} \ge \dots \ge \frac{v_n}{w_n}$$

### 2.2 Die Greedy-Allokationsregel
Sei $k \in I \cup \{n+1\}$ der kritische Index (oft als *Split-Objekt*-Index bezeichnet), definiert als:
$$k = \min \left\{ j \in I \;\middle|\; \sum_{i=1}^j w_i > W \right\}$$
Falls $\sum_{i=1}^n w_i \le W$, definieren wir $k = n + 1$.

Der Greedy-Allokationsvektor $\mathbf{x}^g = (x_1^g, x_2^g, \dots, x_n^g)$ ist algebraisch definiert als:
$$x_i^g = \begin{cases} 
1 & \text{falls } i < k \\
\frac{W - \sum_{j=1}^{k-1} w_j}{w_k} & \text{falls } i = k \\
0 & \text{falls } i > k 
\end{cases}$$
Falls $k = n+1$, dann gilt $x_i^g = 1$ für alle $i \in I$.

### 2.3 Beweis der Optimalität (Variations-/Austauschargument)
Wir beweisen, dass die Greedy-Allokation $\mathbf{x}^g$ global optimal ist: $f(\mathbf{x}^g) \ge f(\mathbf{y})$ für jede zulässige Lösung $\mathbf{y} \in \mathcal{S}(W)$.

**Beweis:**
Sei $\mathbf{y} = (y_1, y_2, \dots, y_n) \in \mathcal{S}(W)$ eine beliebige zulässige Lösung. Betrachten wir die Differenz der Zielfunktionswerte:
$$f(\mathbf{x}^g) - f(\mathbf{y}) = \sum_{i=1}^n v_i (x_i^g - y_i) = \sum_{i=1}^n r_i w_i (x_i^g - y_i)$$

Wir analysieren die Terme dieser Summe in Bezug auf den kritischen Index $k$:
1.  Für $i < k$ gilt $x_i^g = 1$. Da $y_i \in [0, 1]$, folgt $x_i^g - y_i \ge 0$. Aufgrund der Sortierung gilt $r_i \ge r_k$. Somit:
    $$(r_i - r_k)(x_i^g - y_i) \ge 0$$
2.  Für $i > k$ gilt $x_i^g = 0$. Da $y_i \in [0, 1]$, folgt $x_i^g - y_i \le 0$. Aufgrund der Sortierung gilt $r_i \le r_k$. Somit:
    $$(r_i - r_k)(x_i^g - y_i) \ge 0$$
3.  Für $i = k$ ist der Term $r_i - r_k = 0$, also trivialerweise:
    $$(r_i - r_k)(x_i^g - y_i) = 0$$

Daher gilt für alle $i \in I$ die Ungleichung:
$$(r_i - r_k) w_i (x_i^g - y_i) \ge 0$$

Nun schreiben wir die Differenz der Zielfunktion um, indem wir $r_k \sum_{i=1}^n w_i (x_i^g - y_i)$ addieren und subtrahieren:
$$\sum_{i=1}^n r_i w_i (x_i^g - y_i) = \sum_{i=1}^n (r_i - r_k) w_i (x_i^g - y_i) + r_k \sum_{i=1}^n w_i (x_i^g - y_i)$$

*   Die erste Summe ist nicht-negativ, da jeder Term nicht-negativ ist:
    $$\sum_{i=1}^n (r_i - r_k) w_i (x_i^g - y_i) \ge 0$$
*   Für den zweiten Term gilt: Falls $k \le n$, füllt die Greedy-Lösung den Rucksack vollständig aus, was bedeutet $\sum_{i=1}^n w_i x_i^g = W$. Da $\mathbf{y}$ zulässig ist, gilt $\sum_{i=1}^n w_i y_i \le W$. Somit:
    $$\sum_{i=1}^n w_i (x_i^g - y_i) = W - \sum_{i=1}^n w_i y_i \ge 0$$
    Da $r_k > 0$, ist auch der zweite Term nicht-negativ. (Falls $k = n+1$, dann ist $x_i^g = 1 \ge y_i$ für alle $i$, wodurch die Ungleichung trivialerweise erfüllt ist).

Zusammenfassend ergibt sich:
$$f(\mathbf{x}^g) - f(\mathbf{y}) \ge 0 \implies f(\mathbf{x}^g) \ge f(\mathbf{y})$$
Somit ist die Greedy-Allokation $\mathbf{x}^g$ optimal. $\blacksquare$

### 2.4 Zustandsübergang und Schleifeninvarianten
Sei $j \in \{0, 1, \dots, n\}$ der Index der Schleifeniteration. Wir definieren die Zustandsvariablen zum Schritt $j$:
*   $R^{(j)}$: Verbleibende Kapazität des Rucksacks.
*   $T^{(j)}$: Akkumulierter Wert.

Die Rekursionsgleichungen für die Zustandsübergänge lauten:
$$R^{(0)} = W, \quad T^{(0)} = 0$$

Für $j \ge 1$:
$$R^{(j)} = \max\left(0, R^{(j-1)} - w_{\pi(j)}\right)$$
$$T^{(j)} = T^{(j-1)} + v_{\pi(j)} \cdot \min\left(1, \frac{R^{(j-1)}}{w_{\pi(j)}}\right)$$

#### Schleifeninvariante
Zu Beginn der Iteration $j$ (wobei $1 \le j \le n+1$):
1.  Die verbleibende Kapazität ist $R^{(j-1)} = W - \sum_{i=1}^{j-1} w_{\pi(i)} x_{\pi(i)}^g$.
2.  Der akkumulierte Wert ist $T^{(j-1)} = \sum_{i=1}^{j-1} v_{\pi(i)} x_{\pi(i)}^g$.
3.  Die partielle Allokation $(x_{\pi(1)}^g, \dots, x_{\pi(j-1)}^g)$ ist optimal für das Teilproblem, das nur die ersten $j-1$ sortierten Objekte mit der Kapazität $W - R^{(j-1)}$ enthält.

---

## 3. Komplexitätsanalyse

### 3.1 Zeitkomplexität
Die Ausführung des Algorithmus besteht aus zwei unterschiedlichen Phasen: Sortierung und Greedy-Auswahl.

#### Phase 1: Sortierung
Die Berechnung der Dichteverhältnisse $r_i = \frac{v_i}{w_i}$ für alle $i \in I$ erfordert $n$ Divisionen:
$$T_{\text{ratio}}(n) = \Theta(n)$$

Das Sortieren der Objekte basierend auf diesen Verhältnissen unter Verwendung eines vergleichsbasierten Sortieralgorithmus (z. B. Mergesort oder Heapsort) erfordert:
$$T_{\text{sort}}(n) = \Theta(n \log n)$$

#### Phase 2: Greedy-Auswahl
Der Algorithmus iteriert durch die sortierten Objekte. In jeder Iteration $j$ führt er $O(1)$ Operationen aus:
*   Einen Vergleich: $w_{\pi(j)} \le R^{(j-1)}$
*   Arithmetische Aktualisierungen für $R^{(j)}$ und $T^{(j)}$.

Im Schlechtesten Fall (wobei $\sum_{i=1}^n w_i \le W$) läuft die Schleife $n$-mal durch. Daher ist die Komplexität der Auswahlphase:
$$T_{\text{select}}(n) = O(n)$$

#### Gesamte Zeitkomplexität
Zusammenfassend wird die gesamte Zeitkomplexität $T(n)$ durch den Sortierschritt dominiert:
$$T(n) = T_{\text{ratio}}(n) + T_{\text{sort}}(n) + T_{\text{select}}(n) = \Theta(n) + \Theta(n \log n) + O(n) = \Theta(n \log n)$$

#### Hinweis zur $O(n)$-Optimierung
Durch die Verwendung eines Auswahlalgorithmus (wie QuickSelect / Median-of-Medians), um das Split-Objekt $k$ zu finden, ohne das Array vollständig zu sortieren, kann das Problem gelöst werden in:
$$T_{\text{opt}}(n) = \Theta(n) \text{ Zeit im Schlechtesten Fall.}$$

---

### 3.2 Platzkomplexität

#### Hilfsspeicher
*   **Sortierung:** Wenn ein In-Place-Sortieralgorithmus (z. B. Heapsort) verwendet wird, um die Indizes der Objekte zu sortieren, beträgt der Hilfsspeicher $O(1)$. Wenn Mergesort verwendet wird, beträgt der Hilfsspeicher $O(n)$.
*   **Zustandsvariablen:** Die Variablen zur Verfolgung der verbleibenden Kapazität $R^{(j)}$, des akkumulierten Werts $T^{(j)}$ und des Schleifenindex $j$ erfordern $O(1)$ Hilfsspeicher.
*   **Speicherung der Verhältnisse:** Das Speichern der berechneten Verhältnisse oder der sortierten Index-Mappings erfordert $O(n)$ Hilfsspeicher.

Daher ist die Komplexität des Hilfsspeichers:
$$S_{\text{aux}}(n) = O(n)$$
(oder $O(1)$, wenn wir die Eingabe-Arrays in-place modifizieren und einen In-Place-Sortieralgorithmus verwenden dürfen).

#### Gesamte Platzkomplexität
Die Eingaberepräsentation erfordert das Speichern der Vektoren $\mathbf{v}$ und $\mathbf{w}$ der Größe $n$. Daher ist die gesamte Platzkomplexität:
$$S_{\text{total}}(n) = \Theta(n)$$