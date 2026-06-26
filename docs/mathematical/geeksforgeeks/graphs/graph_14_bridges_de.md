# Formale mathematische Spezifikation: Brücken in einem Graphen (Cut Edges)

## 1. Definitionen und Notation

Sei $G = (V, E)$ ein ungerichteter, zusammenhängender Graph, wobei $V = \{v_1, v_2, \dots, v_n\}$ die Menge der Knoten und $E \subseteq \{\{u, v\} : u, v \in V, u \neq v\}$ die Menge der Kanten ist. Sei $|V| = n$ und $|E| = m$.

*   **Brücke:** Eine Kante $e \in E$ ist genau dann eine Brücke, wenn der Graph $G' = (V, E \setminus \{e\})$ mehr Zusammenhangskomponenten besitzt als $G$.
*   **DFS-Baum:** Sei $T = (V, E_T)$ ein Spannbaum von $G$, der in einem beliebigen Knoten $r \in V$ verwurzelt ist und durch eine Tiefensuche (DFS) erzeugt wurde. $E_T$ enthält die Baumkanten und $E_B = E \setminus E_T$ enthält die Rückwärtskanten (Back-Edges).
*   **Entdeckungszeit ($\text{disc}$):** Eine Funktion $\text{disc}: V \to \{1, 2, \dots, n\}$, die die Reihenfolge repräsentiert, in der Knoten während der DFS-Traversierung zum ersten Mal besucht werden.
*   **Niedrigste erreichbare Zeit ($\text{low}$):** Eine Funktion $\text{low}: V \to \{1, 2, \dots, n\}$, definiert als:
    $$\text{low}(u) = \min \left( \{\text{disc}(u)\} \cup \{\text{low}(v) : (u, v) \in E_T, v \text{ ist ein Kind von } u\} \cup \{\text{disc}(v) : (u, v) \in E_B\} \right)$$
    wobei $E_B$ die Rückwärtskanten bezeichnet, die mit $u$ verbunden sind und nicht auf den unmittelbaren Elternknoten von $u$ in $T$ zeigen.

## 2. Algebraische Charakterisierung

Die Korrektheit des Algorithmus beruht auf den Eigenschaften des DFS-Baums. Für jede Kante $(u, v) \in E_T$, bei der $v$ ein Kind von $u$ ist, ist die Kante $(u, v)$ genau dann eine Brücke, wenn es keinen Pfad von dem in $v$ verwurzelten Teilbaum (bezeichnet als $T_v$) zu $u$ oder einem Vorfahren von $u$ in $T$ gibt, außer der Kante $(u, v)$ selbst.

**Theorem:** Eine Kante $(u, v) \in E_T$ ist genau dann eine Brücke, wenn $\text{low}(v) > \text{disc}(u)$.

*Beweisskizze:*
1.  **Notwendigkeit:** Wenn $\text{low}(v) \leq \text{disc}(u)$, existiert eine Rückwärtskante von einem Nachfahren $w \in T_v$ zu $u$ oder einem Vorfahren von $u$. Diese Rückwärtskante bietet einen alternativen Pfad zwischen $T_v$ und dem Rest des Graphen, wodurch sichergestellt wird, dass der Graph nach dem Entfernen von $(u, v)$ zusammenhängend bleibt.
2.  **Hinlänglichkeit:** Wenn $\text{low}(v) > \text{disc}(u)$, dann müssen alle Pfade von $T_v$ nach $V \setminus T_v$ durch die Kante $(u, v)$ verlaufen. Da keine Rückwärtskante existiert, die $T_v$ mit $u$ oder einem Knoten, der vor $u$ besucht wurde, verbindet, trennt das Entfernen von $(u, v)$ den Teilbaum $T_v$ von der Wurzel $r$, wodurch die Anzahl der Zusammenhangskomponenten erhöht wird.

Der Zustandsübergang für $\text{low}(u)$ während der DFS wird durch die folgende Rekurrenz bestimmt:
$$\text{low}(u) = \min \left( \text{disc}(u), \min_{(u, v) \in E_T} \text{low}(v), \min_{(u, v) \in E_B, v \neq \text{parent}(u)} \text{disc}(v) \right)$$

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus führt eine einzelne Traversierung des Graphen mittels DFS durch.
*   Jeder Knoten $v \in V$ wird genau einmal besucht, was $O(1)$ Aufwand für die Initialisierung und Zustandsaktualisierungen erfordert.
*   Jede Kante $e \in E$ wird genau zweimal traversiert (einmal von jedem Endpunkt aus). Für jede Kante führt der Algorithmus eine konstante Anzahl von Vergleichen und Aktualisierungen durch.
*   Die gesamte Zeitkomplexität ergibt sich aus der Summe der Arbeit über alle Knoten und Kanten:
    $$T(n, m) = \sum_{v \in V} O(\text{deg}(v)) + \sum_{v \in V} O(1) = O(V + E)$$
Somit ist der Algorithmus linear in Bezug auf die Größe des Graphen.

### Platzkomplexität
*   **Zusätzlicher Speicherplatz:** Wir verwalten die Arrays $\text{disc}$ und $\text{low}$, die jeweils eine Größe von $O(V)$ haben. Der Rekursions-Stack für die DFS hat im Schlechtesten Fall eine maximale Tiefe von $O(V)$ (bei einem Pfad-Graphen).
*   **Ausgabespeicher:** Im Schlechtesten Fall kann ein Graph $O(V)$ Brücken haben (z. B. ein Linien-Graph).
*   **Gesamtspeicher:** Die gesamte Platzkomplexität beträgt $O(V + E)$, um die Adjazenzlisten-Repräsentation des Graphen zu speichern, sowie $O(V)$ für die zusätzlichen Arrays und den Rekursions-Stack.
    $$S(n, m) = O(V + E)$$