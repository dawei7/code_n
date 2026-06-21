# Formale mathematische Spezifikation: Stark zusammenhängende Komponenten (Tarjan-Algorithmus)

## 1. Definitionen und Notation

Sei $G = (V, E)$ ein gerichteter Graph, wobei $V = \{v_1, v_2, \dots, v_n\}$ die Menge der Knoten und $E \subseteq V \times V$ die Menge der gerichteten Kanten ist. Sei $n = |V|$ und $m = |E|$.

*   **Stark zusammenhängende Komponente (SCC):** Eine Teilmenge $S \subseteq V$ ist eine SCC, wenn für jedes Paar $u, v \in S$ ein gerichteter Pfad von $u$ nach $v$ und ein gerichteter Pfad von $v$ nach $u$ existiert, und $S$ bezüglich dieser Eigenschaft maximal ist.
*   **Entdeckungszeit ($\text{tin}: V \to \mathbb{N}$):** Eine Abbildung, die jedem Knoten $v$ den Zeitpunkt zuweist, zu dem er während einer Tiefensuche (DFS) zum ersten Mal besucht wurde.
*   **Low-link-Wert ($\text{low}: V \to \mathbb{N}$):** Eine Abbildung, die wie folgt definiert ist:
    $$\text{low}(u) = \min \left( \{\text{tin}(u)\} \cup \{\text{low}(v) \mid (u, v) \in E, v \text{ ist im aktuellen DFS-Teilbaum}\} \cup \{\text{tin}(v) \mid (u, v) \in E, v \in \text{Stack}\} \right)$$
*   **Zustandsraum ($\mathcal{S}$):** Der Algorithmus verwaltet ein Zustandstupel $(\text{tin}, \text{low}, \text{Stack}, \text{on\_stack}, \text{SCCs})$, wobei $\text{Stack}$ eine geordnete Sequenz von Knoten ist und $\text{on\_stack}: V \to \{0, 1\}$ eine Indikatorfunktion darstellt.

## 2. Algebraische Charakterisierung

Die Korrektheit des Tarjan-Algorithmus beruht auf den Eigenschaften des DFS-Baums und der Verwaltung des Stacks.

### Die Wurzelbedingung
Ein Knoten $u$ ist die Wurzel einer SCC genau dann, wenn:
$$\text{low}(u) = \text{tin}(u)$$
Diese Bedingung impliziert, dass kein Knoten im Teilbaum, dessen Wurzel $u$ ist, eine Rückkante zu einem Vorfahren von $u$ im DFS-Baum besitzt. Folglich bilden die Knoten im Teilbaum von $u$, die noch keiner SCC zugewiesen wurden, eine vollständige SCC.

### Stack-Invariante
Sei $\mathcal{S}_t$ die Menge der Knoten, die sich zum Zeitpunkt $t$ auf dem Stack befinden. Wenn für einen Knoten $u$ gilt, dass $v \in \mathcal{S}_t$ und ein Pfad von $u$ nach $v$ existiert, dann muss $v$ ein Vorfahre von $u$ im DFS-Baum sein oder $v$ muss sich in derselben SCC wie $u$ befinden. Der Stack erhält die Eigenschaft aufrecht, dass Knoten genau dann mittels pop entfernt werden, wenn sie einen maximalen stark zusammenhängenden Teilgraphen bilden.

### Übergangslogik
Für eine Kante $(u, v) \in E$:
1.  **Baumkante:** Wenn $v$ unbesucht ist, $\text{low}(u) \leftarrow \min(\text{low}(u), \text{low}(v))$.
2.  **Rückkante:** Wenn $v$ besucht ist und $\text{on\_stack}(v) = 1$, $\text{low}(u) \leftarrow \min(\text{low}(u), \text{tin}(v))$.
3.  **Querkante:** Wenn $v$ besucht ist und $\text{on\_stack}(v) = 0$, wird die Kante ignoriert, da $v$ zu einer bereits identifizierten SCC gehört.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus führt einen einzigen DFS-Durchlauf durch.
*   Jeder Knoten $v \in V$ wird genau einmal besucht, was zu $O(V)$ Operationen für die Initialisierung und die Stack-Verwaltung führt.
*   Jede Kante $(u, v) \in E$ wird während des Durchlaufs der Adjazenzliste genau einmal untersucht.
*   Die Stack-Operationen (push und pop) finden höchstens einmal pro Knoten statt.
*   Die gesamte Zeitkomplexität ergibt sich aus der Summe der Knotenbesuche und Kantenrelaxationen:
    $$T(V, E) = \sum_{v \in V} O(1) + \sum_{u \in V} \text{deg}_{out}(u) = O(V + E)$$
Somit ist der Algorithmus linear in Bezug auf die Größe des Graphen.

### Platzkomplexität
Die Platzkomplexität wird durch die zusätzlichen Datenstrukturen bestimmt:
*   $\text{tin}$- und $\text{low}$-Arrays: $O(V)$.
*   $\text{on\_stack}$-Boolean-Array: $O(V)$.
*   $\text{Stack}$ und Rekursionstiefe (DFS-Stack): $O(V)$.
*   Speicherung der Adjazenzliste: $O(V + E)$.
Da die Ausgabe (die SCCs) $V$ partitioniert, erfordert die Speicherung des Ergebnisses $O(V)$ Platz.
Die gesamte zusätzliche Platzkomplexität beträgt $O(V)$, während der gesamte Platzbedarf inklusive des Eingabegraphen $O(V + E)$ beträgt.