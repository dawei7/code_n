# Formale mathematische Spezifikation: Zyklenerkennung (gerichtet und ungerichtet)

## 1. Definitionen und Notation

Sei $G = (V, E)$ ein Graph, wobei $V = \{v_1, v_2, \dots, v_n\}$ die Menge der Knoten und $E \subseteq V \times V$ die Menge der Kanten ist. Sei $n = |V|$ und $m = |E|$.

*   **Ungerichteter Graph:** $E$ ist eine Menge ungeordneter Paare $\{u, v\}$. Die Adjazenzrelation ist symmetrisch: $(u, v) \in E \iff (v, u) \in E$.
*   **Gerichteter Graph (Digraph):** $E$ ist eine Menge geordneter Paare $(u, v)$.
*   **Zyklus:** Eine Folge von Knoten $(v_1, v_2, \dots, v_k)$, sodass $(v_i, v_{i+1}) \in E$ für $1 \le i < k$ und $(v_k, v_1) \in E$ gilt.
*   **Zustandsraum $\mathcal{S}$:**
    *   Für ungerichtete Graphen definieren wir eine Abbildung $\phi: V \to \{0, 1\}$, wobei $\phi(v) = 1$ ist, falls $v$ bereits besucht wurde, und $0$ andernfalls.
    *   Für gerichtete Graphen definieren wir eine Abbildung $\sigma: V \to \{0, 1, 2\}$, welche die Farben repräsentiert: Weiß ($0$), Grau ($1$) und Schwarz ($2$).

## 2. Algebraische Charakterisierung

### Ungerichtete Graphen
Ein Zyklus existiert in einem ungerichteten Graphen genau dann, wenn eine Kante $(u, v) \in E$ existiert, sodass $v$ bereits besucht wurde und $v \neq \text{parent}(u)$ gilt, wobei $\text{parent}(u)$ der Knoten ist, von dem aus $u$ im Depth-First Search (DFS)-Baum entdeckt wurde.
Formal sei $T$ der DFS-Wald. Ein Zyklus existiert, wenn eine Rückkante (back-edge) $(u, v) \in E \setminus T$ existiert. Da $T$ für jede Zusammenhangskomponente $n-1$ Kanten enthält, existiert ein Zyklus, wenn:
$$|E| > |V| - c$$
wobei $c$ die Anzahl der Zusammenhangskomponenten ist. Präziser ausgedrückt: Wenn wir während der Traversierung auf eine Kante $(u, v)$ stoßen, für die $\phi(v) = 1$ und $v \neq \text{parent}(u)$ gilt, enthält der Graph einen Zyklus.

### Gerichtete Graphen
Ein Zyklus existiert in einem gerichteten Graphen genau dann, wenn der DFS-Wald mindestens eine **Rückkante** enthält. Eine Rückkante ist eine Kante $(u, v)$, bei der $v$ ein Vorfahre von $u$ im DFS-Baum ist.
Unter Verwendung der 3-Farben-Zustandsabbildung $\sigma$:
1.  $\sigma(v) = 0$ (Weiß): $v$ ist unentdeckt.
2.  $\sigma(v) = 1$ (Grau): $v$ befindet sich aktuell im Rekursions-Stack (ein Vorfahre des aktuellen Knotens).
3.  $\sigma(v) = 2$ (Schwarz): $v$ und alle seine Nachfahren wurden vollständig exploriert.

Ein Zyklus existiert genau dann, wenn eine Kante $(u, v) \in E$ existiert, sodass $\sigma(u) = 1$ und $\sigma(v) = 1$ gilt. Diese Bedingung impliziert, dass $v$ ein Vorfahre von $u$ im aktuellen Rekursionspfad ist, wodurch ein Zyklus geschlossen wird.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus führt eine Traversierung (DFS) des Graphen durch.
*   **Initialisierung:** Die Initialisierung des `state`- bzw. `visited`-Arrays benötigt $O(V)$.
*   **Traversierung:** Jeder Knoten $v \in V$ wird genau einmal besucht. Für jeden Knoten iterieren wir über seine Adjazenzliste $Adj(v)$. Der Gesamtaufwand beträgt:
    $$\sum_{v \in V} \text{deg}(v)$$
    Nach dem Handschlag-Lemma gilt $\sum_{v \in V} \text{deg}(v) = 2|E|$ für ungerichtete Graphen und $\sum_{v \in V} \text{deg}_{out}(v) = |E|$ für gerichtete Graphen.
*   **Gesamtzeit:** $O(V + E)$. Da jede Kante und jeder Knoten eine konstante Anzahl an Malen verarbeitet wird, beträgt die Komplexität $\Theta(V + E)$.

### Platzkomplexität
*   **Zustandsspeicherung:** Das `visited`-Array oder `state`-Array benötigt $O(V)$ Platz, um den Status jedes Knotens zu speichern.
*   **Rekursions-Stack:** Im Schlechtesten Fall (z. B. ein Pfadgraph $v_1 \to v_2 \to \dots \to v_n$) erreicht die Tiefe des DFS-Rekursions-Stacks $O(V)$.
*   **Adjazenzliste:** Die Eingaberepräsentation benötigt $O(V + E)$ Platz.
*   **Hilfsspeicher:** Abgesehen von der Speicherung des Eingabegraphen beträgt die Platzkomplexität für den Hilfsspeicher $O(V)$.