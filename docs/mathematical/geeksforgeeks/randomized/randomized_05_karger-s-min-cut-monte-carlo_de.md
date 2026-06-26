# Formale mathematische Spezifikation: Kargers Min-Cut (Monte Carlo)

## 1. Definitionen und Notation

Sei $G = (V, E)$ ein zusammenhängender, ungerichteter Multigraph, wobei $V$ die Menge der Knoten, $|V| = n$, und $E$ die Menge der Kanten, $|E| = m$, ist.

*   **Schnitt (Cut):** Ein Schnitt ist eine Partition von $V$ in zwei nicht-leere, disjunkte Mengen $(S, V \setminus S)$.
*   **Schnittmenge (Cut-set):** Die Menge der Kanten $C(S, V \setminus S) = \{ \{u, v\} \in E \mid u \in S, v \in V \setminus S \}$.
*   **Min-Cut:** Der minimale Schnitt ist definiert als $\min_{S \subset V, S \neq \emptyset} |C(S, V \setminus S)|$. Sei $k$ die Größe des minimalen Schnitts.
*   **Kontraktion:** Für eine Kante $e = \{u, v\}$ ist die Kontraktion $G/e$ ein Graph, in dem $u$ und $v$ zu einem einzigen Knoten $w$ verschmolzen werden. Alle Kanten, die zu $u$ oder $v$ inzident waren, sind nun zu $w$ inzident. Durch die Kontraktion entstandene Selbstschleifen werden entfernt.
*   **Zustandsraum:** Der Algorithmus operiert auf einer Sequenz von Graphen $G_n, G_{n-1}, \dots, G_2$, wobei $G_i$ der Graph nach $n-i$ Kantenkontraktionen ist, was zu $i$ Super-Knoten führt.

## 2. Algebraische Charakterisierung

Die Korrektheit von Kargers Algorithmus beruht auf der Wahrscheinlichkeit, dass während des Kontraktionsprozesses keine Kante aus einem spezifischen minimalen Schnitt $C^*$ ausgewählt wird.

Sei $C^*$ ein fester minimaler Schnitt der Größe $k$. Zu jedem Schritt $i$ (wobei der Graph $i$ Knoten besitzt) gilt für die Anzahl der Kanten $|E_i| \ge \frac{ik}{2}$, da jeder Knoten einen Grad von mindestens $k$ haben muss (andernfalls würde ein kleinerer Schnitt existieren).

Die Wahrscheinlichkeit $P_i$, im Schritt $i$ eine Kante aus $C^*$ zu wählen, ist:
$$P(\text{pick } e \in C^* \mid |V|=i) = \frac{|C^*|}{|E_i|} \le \frac{k}{ik/2} = \frac{2}{i}$$

Die Wahrscheinlichkeit, im Schritt $i$ *keine* Kante aus $C^*$ zu wählen, beträgt $1 - \frac{2}{i} = \frac{i-2}{i}$. Die Wahrscheinlichkeit, dass der Algorithmus erfolgreich ist (d. h. keine Kante in $C^*$ wird während des gesamten Prozesses von $n$ auf 2 Knoten kontrahiert), ist das Produkt dieser Wahrscheinlichkeiten:
$$P(\text{success}) = \prod_{i=3}^{n} \left( \frac{i-2}{i} \right) = \left( \frac{1}{3} \cdot \frac{2}{4} \cdot \frac{3}{5} \dots \frac{n-2}{n} \right) = \frac{2}{n(n-1)}$$

Um die Erfolgswahrscheinlichkeit zu erhöhen, führen wir $T$ unabhängige Durchläufe (Trials) durch. Die Wahrscheinlichkeit des Scheiterns nach $T$ Durchläufen ist:
$$P(\text{fail}) \le \left( 1 - \frac{2}{n(n-1)} \right)^T$$
Unter Verwendung der Ungleichung $1-x \le e^{-x}$ erhalten wir für $T = \frac{n(n-1)}{2} \ln n$:
$$P(\text{fail}) \le e^{-\ln n} = \frac{1}{n}$$

## 3. Komplexitätsanalyse

### Zeitkomplexität
Ein einzelner Durchlauf umfasst $n-2$ Kontraktionen. Unter Verwendung einer Union-Find-Datenstruktur mit Pfadkompression und Union-by-Rank benötigt jede Kontraktionsoperation (find und union) amortisiert nahezu konstante Zeit, $\alpha(n)$. Die bereitgestellte initiale Implementierung iteriert jedoch über die Edge List, um Kanten zu identifizieren, die den Schnitt kreuzen, was zu einer Komplexität von $O(m)$ pro Durchlauf führt.

1.  **Einzelner Durchlauf:** Der Kontraktionsprozess benötigt $O(m \alpha(n))$ oder $O(m)$, abhängig von der Implementierung.
2.  **Verstärkung:** Um eine Erfolgswahrscheinlichkeit von $1 - 1/n$ zu erreichen, benötigen wir $T = \Theta(n^2 \log n)$ Durchläufe.
3.  **Gesamte erwartete Zeit:** 
    $$T_{total} = \sum_{trials} O(m) = O(n^2 \log n \cdot m)$$
    In einem dichten Graphen, in dem $m = O(n^2)$, ergibt dies $O(n^4 \log n)$. Die angegebene $O(V^2 E)$-Komplexität setzt eine spezifische Implementierung des Kontraktionsprozesses voraus, bei der die Anzahl der Kanten abnimmt.

### Platzkomplexität
Der Algorithmus verwaltet die Graphstruktur und die Union-Find-Metadaten:
1.  **Graphspeicherung:** $O(n + m)$ zur Speicherung der Adjacency List oder Edge List.
2.  **Union-Find-Struktur:** $O(n)$ zur Speicherung der `parent`- und `rank`-Arrays.
3.  **Gesamter Platzbedarf:** $O(n + m)$, was linear zur Eingabegröße ist.