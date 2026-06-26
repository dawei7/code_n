# Formale mathematische Spezifikation: M-Coloring-Problem

## 1. Definitionen und Notation

Sei $G = (V, E)$ ein ungerichteter Graph, wobei $V = \{0, 1, \dots, n-1\}$ die Menge der Knoten und $E \subseteq \{\{u, v\} : u, v \in V, u \neq v\}$ die Menge der Kanten ist. Sei $M \in \mathbb{Z}^+$ die Anzahl der verfügbaren Farben.

*   **Färbungsfunktion:** Eine Abbildung $f: V \to \{1, 2, \dots, M\}$.
*   **Gültige Färbung:** Eine Färbungsfunktion $f$ ist genau dann gültig, wenn für jede Kante $\{u, v\} \in E$ gilt: $f(u) \neq f(v)$.
*   **Zustandsraum:** Der Zustandsraum $\mathcal{S}$ ist die Menge aller partiellen Abbildungen $f_k: \{0, \dots, k-1\} \to \{1, \dots, M\}$ für $0 \leq k \leq n$.
*   **Ziel:** Bestimmen, ob eine totale Abbildung $f_n: V \to \{1, \dots, M\}$ existiert, sodass $f_n$ eine gültige Färbung ist.

## 2. Algebraische Charakterisierung

Das Problem ist definiert als die Suche nach einer gültigen Zuweisung im Konfigurationsraum $\mathcal{C} = \{1, \dots, M\}^n$. Die Gültigkeit einer partiellen Zuweisung $f_k$ wird durch das Bedingungsprädikat $P(f_k)$ bestimmt:

$$P(f_k) = \bigwedge_{\{u, v\} \in E, u, v < k} [f_k(u) \neq f_k(v)]$$

Der Algorithmus verwendet eine Backtracking-Suche, die durch die rekursive Funktion $H(k, f_k)$ definiert ist. Diese gibt wahr zurück, falls eine Erweiterung der partiellen Färbung $f_k$ zu einer gültigen totalen Färbung $f_n$ existiert. Der Übergang ist definiert als:

$$H(k, f_k) = \begin{cases} 
\text{True} & \text{falls } k = n \\
\bigvee_{c=1}^M \left( \text{is\_safe}(k, c, f_k) \land H(k+1, f_k \cup \{k \mapsto c\}) \right) & \text{falls } k < n 
\end{cases}$$

wobei das Prädikat $\text{is\_safe}(k, c, f_k)$ definiert ist als:
$$\text{is\_safe}(k, c, f_k) = \forall u \in \text{Adj}(k) \text{ s.t. } u < k : f_k(u) \neq c$$

Der Algorithmus terminiert erfolgreich, wenn $H(0, \emptyset) = \text{True}$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus durchsucht einen Zustandsraum-Baum der Tiefe $n$. Auf jeder Ebene $k$ der Rekursion iteriert der Algorithmus über $M$ mögliche Farbzuweisungen.

1.  **Verzweigungsfaktor:** Der Verzweigungsfaktor des Suchbaums beträgt höchstens $M$.
2.  **Baumtiefe:** Die Tiefe der Rekursion beträgt $n = |V|$.
3.  **Aufwand pro Knoten:** An jedem Knoten im Rekursionsbaum iteriert die Funktion `is_safe` über die Adjacency List des aktuellen Knotens. Im Schlechtesten Fall benötigt dies $O(\text{deg}(v)) = O(n)$ Zeit.

Die Gesamtzahl der Knoten im Suchbaum ist beschränkt durch $\sum_{i=0}^{n} M^i = \frac{M^{n+1}-1}{M-1} = O(M^n)$. 
Unter Einbeziehung der Kosten für die Sicherheitsprüfung an jedem Knoten ergibt sich die gesamte Zeitkomplexität $T(n)$ zu:
$$T(n) = O\left( \sum_{i=0}^{n-1} M^i \cdot n \right) = O(n \cdot M^n)$$
Somit ist die Zeitkomplexität $O(V \cdot M^V)$.

### Platzkomplexität
Die Platzkomplexität wird durch zwei Faktoren bestimmt:
1.  **Rekursions-Stack:** Die Tiefe der Rekursion beträgt $n$, was $O(n)$ Platz auf dem Call-Stack erfordert.
2.  **Color Array:** Das `color` Array speichert die aktuelle Zuweisung für jeden Knoten, was $O(n)$ Platz erfordert.
3.  **Adjacency List:** Die Repräsentation des Graphen erfordert $O(V + E)$ Platz.

Unter Ausschluss des Eingabespeichers beträgt die zusätzliche Platzkomplexität $O(V)$. Unter Einbeziehung der Eingabe beträgt die gesamte Platzkomplexität $O(V + E)$.