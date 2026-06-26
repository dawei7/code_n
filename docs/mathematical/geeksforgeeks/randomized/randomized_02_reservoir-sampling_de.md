# Formale mathematische Spezifikation: Reservoir Sampling

## 1. Definitionen und Notation

Sei $\mathcal{S} = \{x_1, x_2, \dots, x_N\}$ eine Sequenz von Elementen (ein Stream) unbekannter Länge $N \in \mathbb{N}$. Wir definieren das Sampling-Ziel als die Auswahl einer Teilmenge $\mathcal{R} \subset \mathcal{S}$, sodass $|\mathcal{R}| = K$, wobei $K \le N$.

*   **Input:** Ein Stream $\mathcal{S}$ und eine Kapazität $K \in \mathbb{Z}^+$.
*   **Zustandsraum:** Sei $\mathcal{R}_i$ der Zustand des Reservoirs nach der Verarbeitung des $i$-ten Elements des Streams, wobei $\mathcal{R}_i = \{r_1, r_2, \dots, r_K\}$.
*   **Zufallsvariable:** Sei $J_i$ eine diskrete gleichverteilte Zufallsvariable, sodass $J_i \sim \text{Uniform}\{1, 2, \dots, i\}$.
*   **Output:** Der finale Zustand $\mathcal{R}_N$, sodass für jedes $x \in \mathcal{S}$ die Inklusionswahrscheinlichkeit $P(x \in \mathcal{R}_N) = \frac{K}{N}$ beträgt.

## 2. Algebraische Charakterisierung

Der Algorithmus ist durch den folgenden Zustandsübergang für das Reservoir $\mathcal{R}_i$ bei Ankunft des Elements $x_{i+1}$ definiert:

1.  **Initialisierung:** Für $i \le K$ gilt $\mathcal{R}_i = \{x_1, \dots, x_i\}$.
2.  **Übergang:** Für $i > K$ wird das Reservoir $\mathcal{R}_i$ wie folgt zu $\mathcal{R}_{i+1}$ aktualisiert:
    $$
    \mathcal{R}_{i+1} = 
    \begin{cases} 
    (\mathcal{R}_i \setminus \{r_{J_{i+1}}\}) \cup \{x_{i+1}\} & \text{falls } J_{i+1} \le K \\
    \mathcal{R}_i & \text{falls } J_{i+1} > K 
    \end{cases}
    $$
    wobei $J_{i+1} \sim \text{Uniform}\{1, \dots, i+1\}$.

**Theorem (Korrektheit):** Für jedes $x_m \in \mathcal{S}$ ist die Wahrscheinlichkeit, dass $x_m \in \mathcal{R}_N$ gilt, gleich $\frac{K}{N}$.

*Beweis durch vollständige Induktion:*
Induktionsanfang: Für $i=K$ gilt $P(x_m \in \mathcal{R}_K) = 1 = \frac{K}{K}$.
Induktionsschritt: Angenommen, es gilt $P(x_m \in \mathcal{R}_i) = \frac{K}{i}$. Bei Ankunft von $x_{i+1}$ verbleibt $x_m$ im Reservoir, wenn es bereits vorhanden war und nicht ersetzt wurde. Die Wahrscheinlichkeit für eine Ersetzung ist $P(\text{replace}) = P(J_{i+1} \le K) \cdot P(\text{select } x_m | J_{i+1} \le K) = \frac{K}{i+1} \cdot \frac{1}{K} = \frac{1}{i+1}$.
Somit ergibt sich die Überlebenswahrscheinlichkeit zu:
$$P(x_m \in \mathcal{R}_{i+1}) = P(x_m \in \mathcal{R}_i) \cdot \left(1 - \frac{1}{i+1}\right) = \frac{K}{i} \cdot \frac{i}{i+1} = \frac{K}{i+1}$$
Durch Induktion folgt $P(x_m \in \mathcal{R}_N) = \frac{K}{N}$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus verarbeitet jedes Element $x_i$ im Stream genau einmal. Für jedes $i \in \{1, \dots, N\}$ werden folgende Operationen durchgeführt:
1.  Generierung einer Zufallszahl $J_i$: $O(1)$.
2.  Bedingter Vergleich und potenzielle Array-Aktualisierung: $O(1)$.

Die gesamte Zeitkomplexität $T(N)$ ergibt sich aus der Summe:
$$T(N) = \sum_{i=1}^{N} O(1) = O(N)$$
Da der Algorithmus einen einzigen Durchlauf (Single Pass) mit konstanten Operationen pro Element durchführt, ist die Komplexität streng linear in Bezug auf die Stream-Länge $N$.

### Platzkomplexität
Der Algorithmus verwaltet ein Reservoir $\mathcal{R}$ mit fester Kapazität $K$.
*   **Zusätzlicher Speicherbedarf:** Das Reservoir benötigt $O(K)$ Speicherplatz, um die ausgewählten Elemente zu halten.
*   **Gesamtspeicherbedarf:** Abgesehen vom Eingabestream (der elementweise verarbeitet und nicht vollständig gespeichert wird), wird der Speicherbedarf maßgeblich durch das Reservoir bestimmt.
Somit ist die Platzkomplexität $O(K)$, unabhängig von $N$.