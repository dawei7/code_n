# Formale mathematische Spezifikation: Alle Teilfolgen ausgeben

## 1. Definitionen und Notation

Sei $S = \{s_0, s_1, \dots, s_{n-1}\}$ eine Menge von $n$ eindeutigen Elementen, die als geordnete Sequenz (Array) der Länge $n$ dargestellt wird.

*   **Potenzmenge:** Das Ziel ist die Konstruktion der Potenzmenge $\mathcal{P}(S)$, definiert als die Menge aller Teilmengen von $S$, wobei $|\mathcal{P}(S)| = 2^n$ gilt.
*   **Zustandsraum:** Ein Zustand ist definiert durch das Tupel $(i, \sigma)$, wobei $i \in \{0, 1, \dots, n\}$ den aktuellen Index in $S$ bezeichnet, der betrachtet wird, und $\sigma \in \mathcal{P}(S_i)$ die partielle Teilfolge ist, die aus dem Präfix $S_i = \{s_0, \dots, s_{i-1}\}$ konstruiert wurde.
*   **Entscheidungsraum:** An jedem Index $i$ definieren wir eine Entscheidungsvariable $d_i \in \{0, 1\}$, wobei $d_i = 1$ die Aufnahme von $s_i$ in die Teilfolge und $d_i = 0$ den Ausschluss bezeichnet.
*   **Ausgabe:** Der Algorithmus erzeugt eine Kollektion $\mathcal{R} = \{ \sigma_1, \sigma_2, \dots, \sigma_{2^n} \}$, wobei jedes $\sigma_j$ einem eindeutigen Vektor $(d_0, d_1, \dots, d_{n-1}) \in \{0, 1\}^n$ entspricht.

## 2. Algebraische Charakterisierung

Der Algorithmus wird durch eine rekursive Funktion $f(i, \sigma)$ gesteuert, welche den Binärbaum der Entscheidungen durchläuft. Die Korrektheit wird durch die folgende Rekursionsgleichung begründet:

Sei $f(i, \sigma)$ die Menge aller Teilfolgen, die ausgehend vom Index $i$ bei gegebenem aktuellen Präfix $\sigma$ erreichbar sind:

$$
f(i, \sigma) = 
\begin{cases} 
\{\sigma\} & \text{falls } i = n \\
f(i+1, \sigma) \cup f(i+1, \sigma \cup \{s_i\}) & \text{falls } 0 \le i < n 
\end{cases}
$$

**Invarianten:**
1. **Vollständigkeit:** Für jede Teilmenge $A \subseteq S$ existiert ein eindeutiger Pfad im Rekursionsbaum, sodass die Sequenz der Entscheidungen $(d_0, \dots, d_{n-1})$ die Bedingung $d_j = 1 \iff s_j \in A$ erfüllt.
2. **Terminierung:** Da der Index $i$ bei jedem rekursiven Schritt strikt um 1 zunimmt, beträgt die Tiefe des Rekursionsbaums exakt $n$. Der Basisfall $i=n$ wird garantiert in endlicher Zeit erreicht.

Die Gesamtmenge der Teilfolgen ergibt sich aus der Vereinigung aller Blattknoten im Rekursionsbaum:
$$\mathcal{R} = \bigcup_{\text{Pfade } \pi} \text{leaf}(\pi) = \mathcal{P}(S)$$

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Rekursionsbaum ist ein vollständiger Binärbaum der Tiefe $n$. Die Anzahl der Knoten in einem vollständigen Binärbaum der Tiefe $n$ beträgt $2^{n+1} - 1$.

An jedem Blattknoten (wo $i=n$) führt der Algorithmus eine Kopieroperation des aktuellen Pfades $\sigma$ durch. Im Schlechtesten Fall gilt $|\sigma| = n$. Die Anzahl der Blattknoten beträgt exakt $2^n$.

Die gesamte Zeitkomplexität $T(n)$ ist die Summe des Arbeitsaufwands an jedem Knoten:
$$T(n) = \sum_{k=0}^{n-1} 2^k \cdot O(1) + 2^n \cdot O(n)$$
Der erste Term repräsentiert die inneren Knoten (konstanter Aufwand), und der zweite Term repräsentiert die Blattknoten (Kopieren der Teilfolge).
$$T(n) = O(2^n) + O(n \cdot 2^n) = O(n \cdot 2^n)$$
Somit beträgt die Zeitkomplexität $O(n \cdot 2^n)$.

### Platzkomplexität
Die Platzkomplexität wird durch zwei Komponenten bestimmt:
1. **Rekursions-Stack:** Die maximale Tiefe der Rekursion ist $n$. Daher benötigt der Call-Stack $O(n)$ Platz.
2. **Hilfsspeicher:** Das `current_path` Array speichert maximal $n$ Elemente, was $O(n)$ Platz erfordert.

Die gesamte Platzkomplexität für Hilfsspeicher beträgt $O(n)$.

*Hinweis: Wenn die Ausgabe $\mathcal{R}$ als Teil des Speicherbedarfs betrachtet wird, beträgt die gesamte Platzkomplexität $O(n \cdot 2^n)$, da es $2^n$ Teilmengen mit einer durchschnittlichen Länge von $n/2$ gibt.*