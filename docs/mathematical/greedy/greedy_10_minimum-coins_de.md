# Formale mathematische Spezifikation: Minimum Coins (Greedy-Variante)

## 1. Definitionen und Notation

Sei $\mathcal{D} = \{d_1, d_2, \dots, d_n\}$ eine Menge von Münzwerten, sodass $d_i \in \mathbb{Z}^+$ und $d_1 > d_2 > \dots > d_n$. Ohne Beschränkung der Allgemeinheit nehmen wir an, dass $d_n = 1$, um die Existenz einer Lösung für jeden Zielwert $V \in \mathbb{Z}_{\ge 0}$ zu gewährleisten.

*   **Zielwert:** $V \in \mathbb{Z}_{\ge 0}$, der darzustellende Gesamtbetrag.
*   **Münzwertmenge:** $\mathcal{D} \subset \mathbb{Z}^+$, geordnet nach $d_1 > d_2 > \dots > d_n$.
*   **Lösungsvektor:** Sei $\mathbf{x} = (x_1, x_2, \dots, x_n)$ ein Vektor, wobei $x_i \in \mathbb{Z}_{\ge 0}$ die Anzahl der verwendeten Münzen des Wertes $d_i$ darstellt.
*   **Zielfunktion:** Wir streben die Minimierung der Gesamtzahl der Münzen $f(\mathbf{x}) = \sum_{i=1}^n x_i$ an, unter der Nebenbedingung:
    $$\sum_{i=1}^n x_i \cdot d_i = V$$

## 2. Algebraische Charakterisierung

Der Greedy-Ansatz konstruiert den Lösungsvektor $\mathbf{x}$ durch iterative Anwendung des Divisionsalgorithmus. Für jeden Münzwert $d_i$ bestimmen wir die maximale Anzahl an Münzen $x_i$, sodass der verbleibende Wert nicht-negativ bleibt.

### Der Greedy-Übergang
Sei für jedes $i \in \{1, \dots, n\}$ $R_i$ der verbleibende Wert vor der Betrachtung des Münzwertes $d_i$, wobei $R_1 = V$. Die Greedy-Entscheidung ist durch die folgende Rekurrenz definiert:
$$x_i = \left\lfloor \frac{R_i}{d_i} \right\rfloor$$
$$R_{i+1} = R_i \pmod{d_i} = R_i - x_i \cdot d_i$$

Der Algorithmus terminiert, wenn $R_{n+1} = 0$. Die Gesamtzahl der Münzen ergibt sich zu:
$$N = \sum_{i=1}^n \left\lfloor \frac{R_i}{d_i} \right\rfloor$$

### Die kanonische Bedingung
Die Greedy-Strategie ist genau dann optimal, wenn die Menge $\mathcal{D}$ **kanonisch** ist. Eine Menge $\mathcal{D}$ ist kanonisch, wenn der Greedy-Algorithmus für alle $V \in \mathbb{Z}^+$ die optimale Lösung liefert. Mathematisch erfordert dies, dass für jedes $V$ die Greedy-Lösung $\mathbf{x}^G$ erfüllt:
$$f(\mathbf{x}^G) = \min \left\{ \sum x_i \mid \sum x_i d_i = V, x_i \in \mathbb{Z}_{\ge 0} \right\}$$
Falls $\mathcal{D}$ nicht kanonisch ist, existiert mindestens ein $V$, für das die Greedy-Entscheidung in einem Schritt $i$ das globale Optimum verhindert. Dies erfordert einen Ansatz mittels Dynamischer Programmierung, bei dem der Zustandsraum durch die Bellman-Gleichung definiert ist:
$$OPT(v) = 1 + \min_{d \in \mathcal{D}, d \le v} \{ OPT(v - d) \}$$

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus durchläuft die Menge der Münzwerte $\mathcal{D}$ genau einmal. Für jeden Münzwert $d_i$ werden folgende Operationen ausgeführt:
1.  **Ganzzahlige Division:** $\lfloor R_i / d_i \rfloor$
2.  **Modulo-Operation:** $R_i \pmod{d_i}$

Unter der Annahme, dass Standard-Arithmetikoperationen auf Ganzzahlen fester Breite $O(1)$ Zeit benötigen, ergibt sich die gesamte Zeitkomplexität zu:
$$T(n) = \sum_{i=1}^n \Theta(1) = \Theta(n)$$
Wobei $n = |\mathcal{D}|$. Da die Münzwerte in einem einzigen Durchlauf verarbeitet werden, ist die Komplexität linear in Bezug auf die Anzahl der verfügbaren Münzwerte, $O(n)$. In praktischen Währungssystemen, in denen $n$ eine kleine Konstante ist, entspricht dies effektiv $O(1)$.

### Platzkomplexität
*   **Zusätzlicher Speicherplatz:** Der Algorithmus verwaltet nur wenige skalare Variablen ($count$, $amount$, $R_i$), die $O(1)$ Speicherplatz belegen.
*   **Gesamtspeicherplatz:** Wenn der Algorithmus nur die ganzzahlige Anzahl der Münzen zurückgibt, beträgt die Platzkomplexität $O(1)$. Wenn der Algorithmus den Lösungsvektor $\mathbf{x}$ (die Liste der verwendeten Münzen) zurückgeben muss, beträgt die Platzkomplexität $O(k)$, wobei $k = \sum x_i$ die Gesamtzahl der ausgegebenen Münzen ist. Unter der Greedy-Nebenbedingung ist $k$ durch $V/d_n = V$ beschränkt, daher beträgt die Platzkomplexität im schlechtesten Fall $O(V)$ für die Speicherung der Ausgabe.