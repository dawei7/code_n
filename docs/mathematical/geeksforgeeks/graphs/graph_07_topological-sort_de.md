# Formale mathematische Spezifikation: Topologische Sortierung

## 1. Definitionen und Notation

Sei $G = (V, E)$ ein gerichteter Graph, wobei $V = \{v_1, v_2, \dots, v_n\}$ eine endliche Menge von Knoten und $E \subseteq V \times V$ eine Menge von gerichteten Kanten ist. Wir definieren den Graphen als einen gerichteten azyklischen Graphen (DAG), wenn keine Folge von Knoten $(v_1, v_2, \dots, v_k)$ existiert, sodass $(v_i, v_{i+1}) \in E$ für $1 \le i < k$ und $v_1 = v_k$ gilt.

*   **Eingangsgrad-Funktion:** Wir definieren den Eingangsgrad eines Knotens $v \in V$ als $\text{deg}^-(v) = |\{u \in V : (u, v) \in E\}|$.
*   **Topologische Sortierung:** Eine topologische Sortierung von $G$ ist eine Bijektion $\sigma: V \to \{1, 2, \dots, n\}$, sodass für jede gerichtete Kante $(u, v) \in E$ die Bedingung $\sigma(u) < \sigma(v)$ erfüllt ist.
*   **Zustandsraum:** Der Algorithmus verwaltet einen Zustand $\mathcal{S} = (\text{deg}^-, Q, \mathcal{L})$, wobei:
    *   $\text{deg}^-: V \to \mathbb{N}_0$ die aktuelle Abbildung der Eingangsgrade ist.
    *   $Q \subseteq \{v \in V : \text{deg}^-(v) = 0\}$ die Menge der Knoten mit Eingangsgrad Null ist (die „bereite“ Menge).
    *   $\mathcal{L} = (l_1, l_2, \dots, l_k)$ die geordnete Sequenz der bisher verarbeiteten Knoten ist.

## 2. Algebraische Charakterisierung

Die Korrektheit des Algorithmus von Kahn beruht auf der Eigenschaft, dass jeder nicht-leere DAG mindestens einen Knoten mit einem Eingangsgrad von Null enthält.

**Schleifeninvariante:** Sei zu Beginn jeder Iteration der `while`-Schleife $V_{processed} = \{l_1, \dots, l_k\}$ die Menge der Knoten, die bereits an $\mathcal{L}$ angehängt wurden. Die folgenden Bedingungen gelten:
1.  Für alle $v \in V \setminus V_{processed}$ ist $\text{deg}^-(v)$ gleich der Anzahl der Kanten $(u, v) \in E$, für die $u \notin V_{processed}$ gilt.
2.  $Q = \{v \in V \setminus V_{processed} : \text{deg}^-(v) = 0\}$.
3.  Für alle $(u, v) \in E$ gilt: Wenn $u \in V_{processed}$, dann ist auch $v \in V_{processed}$.

**Terminierung und Korrektheit:**
Der Algorithmus terminiert, wenn $Q = \emptyset$. Sei $n = |V|$.
*   Wenn $|V_{processed}| = n$, dann definiert $\sigma(v_i) = i$ eine gültige topologische Sortierung, da die Invariante sicherstellt, dass keine Kante $(u, v)$ existiert, bei der $u$ nach $v$ verarbeitet wird.
*   Wenn $|V_{processed}| < n$, dann ist die Menge $V \setminus V_{processed}$ nicht leer und enthält keine Knoten mit Eingangsgrad Null. Durch die Kontraposition der DAG-Eigenschaft muss $G$ mindestens einen gerichteten Zyklus enthalten.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus führt die folgenden Operationen aus:
1.  **Initialisierung:** Die Berechnung von $\text{deg}^-(v)$ für alle $v \in V$ erfordert das Iterieren über alle Kanten. Dies benötigt $\Theta(|V| + |E|)$.
2.  **Queue-Operationen:** Jeder Knoten $v \in V$ wird genau einmal zur Queue $Q$ hinzugefügt und daraus entfernt. Dies trägt $\Theta(|V|)$ bei.
3.  **Kantenrelaxation:** Für jeden Knoten $u$, der aus $Q$ entfernt wird, iterieren wir über dessen Adjacency List $Adj(u)$. Die Gesamtarbeit über alle Iterationen hinweg beträgt $\sum_{u \in V} \text{deg}^+(u) = |E|$.

Somit ergibt sich die gesamte Zeitkomplexität zu:
$$T(V, E) = \Theta(|V| + |E|)$$
Bei einer Darstellung als Adjazenzmatrix iteriert die innere Schleife für jeden Knoten $u$ über alle $V$ Knoten, was zu folgendem führt:
$$T(V) = \Theta(V^2)$$

### Platzkomplexität
Die Platzkomplexität wird durch die Speicherung des Graphen und der zusätzlichen Datenstrukturen bestimmt:
1.  **Adjacency List:** $\Theta(|V| + |E|)$.
2.  **Eingangsgrad-Array:** $\Theta(|V|)$.
3.  **Queue und Sortierungsliste:** $\Theta(|V|)$.

Die gesamte zusätzliche Platzkomplexität beträgt $\Theta(|V|)$, während die gesamte Platzkomplexität (einschließlich der Graphdarstellung) $\Theta(|V| + |E|)$ beträgt.