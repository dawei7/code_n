# Formale mathematische Spezifikation: Prim-Algorithmus (Minimaler Spannbaum)

## 1. Definitionen und Notation

Sei $G = (V, E, w)$ ein zusammenhängender, ungerichteter, gewichteter Graph, wobei:
*   $V = \{v_1, v_2, \dots, v_n\}$ die Menge der Knoten ist, mit $|V| = n$.
*   $E \subseteq \{\{u, v\} : u, v \in V, u \neq v\}$ die Menge der Kanten ist, mit $|E| = m$.
*   $w: E \to \mathbb{R}^+$ eine Gewichtsfunktion ist, die jeder Kante einen positiven reellen Wert zuweist.

Ein **Spannbaum** $T = (V, E_T)$ ist ein Teilgraph von $G$, sodass $E_T \subseteq E$, $|E_T| = n - 1$ und $T$ azyklisch ist. Das Ziel ist es, einen Baum $T^*$ zu finden, der das Gesamtgewicht minimiert:
$$W(T^*) = \sum_{e \in E_T^*} w(e) = \min_{T \in \mathcal{T}} \sum_{e \in E_T} w(e)$$
wobei $\mathcal{T}$ die Menge aller Spannbäume von $G$ ist.

Der Algorithmus verwaltet den folgenden Zustand:
*   $S \subset V$: Die Menge der Knoten, die bereits im wachsenden Baum enthalten sind.
*   $Q$: Eine Priority Queue, die Kanten $e = \{u, v\}$ enthält, sodass $u \in S$ und $v \in V \setminus S$, geordnet nach $w(e)$.
*   $E_T$: Die Menge der für den MST ausgewählten Kanten.

## 2. Algebraische Charakterisierung

Der Prim-Algorithmus basiert auf der **Schnitt-Eigenschaft** (Cut Property) von MSTs. Für jeden Schnitt $(S, V \setminus S)$ eines Graphen $G$ gilt: Wenn eine Kante $e = \{u, v\}$ mit $u \in S$ und $v \in V \setminus S$ das minimale Gewicht unter allen Kanten hat, die den Schnitt kreuzen, dann gehört diese Kante zu einem MST von $G$.

### Schleifeninvariante
Zu Beginn jeder Iteration der Hauptschleife gelten die folgenden Bedingungen:
1.  $S$ ist die Menge der Knoten, die durch die Kanten in $E_T$ verbunden sind.
2.  $E_T$ bildet einen Spannbaum für den durch $S$ induzierten Teilgraphen.
3.  $Q$ enthält alle Kanten $\{u, v\}$, sodass $u \in S$ und $v \in V \setminus S$.
4.  Für jeden Knoten $v \in V \setminus S$ speichert die Priority Queue $Q$ die Kante mit dem minimalen Gewicht, die $v$ mit einem beliebigen Knoten in $S$ verbindet.

### Übergang
Sei $e_{min} = \{u, v\} = \arg \min \{w(e) : e = \{x, y\}, x \in S, y \in V \setminus S\}$.
Der Zustand ändert sich wie folgt:
$$S_{i+1} = S_i \cup \{v\}$$
$$E_{T, i+1} = E_{T, i} \cup \{e_{min}\}$$
Der Algorithmus terminiert, wenn $S = V$, wobei zu diesem Zeitpunkt $|E_T| = n - 1$ gilt.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus führt die folgenden Operationen aus:
1.  **Initialisierung:** Der Aufbau der Adjacency List benötigt $O(m)$.
2.  **Priority Queue Operationen:**
    *   Jeder Knoten $v \in V$ wird genau einmal zu $S$ hinzugefügt. Wenn $v$ hinzugefügt wird, iterieren wir über seine Adjacency List $\text{adj}(v)$.
    *   Jede Kante $\{u, v\} \in E$ wird höchstens zweimal in die Priority Queue eingefügt (einmal für jeden Endpunkt). Somit gibt es höchstens $2m$ `push`-Operationen.
    *   Jede `pop`-Operation entfernt eine Kante aus der Priority Queue. Es gibt höchstens $2m$ `pop`-Operationen.
    *   Da die Priority Queue höchstens $m$ Elemente enthält, benötigt jede `push`- und `pop`-Operation $O(\log m)$ Zeit.

Da $m \leq n^2$ gilt, haben wir $\log m \leq \log n^2 = 2 \log n$, folglich $O(\log m) = O(\log n)$. Die gesamte Zeitkomplexität beträgt:
$$T(n, m) = O(m \log m) = O(m \log n)$$

### Platzkomplexität
1.  **Adjacency List:** Das Speichern des Graphen erfordert $O(n + m)$ Platz.
2.  **Visited Set:** Das Speichern der Zugehörigkeit zu $S$ erfordert $O(n)$ Platz.
3.  **Priority Queue:** Im Schlechtesten Fall speichert die Priority Queue alle Kanten, was $O(m)$ Platz erfordert.

Die gesamte zusätzliche Platzkomplexität beträgt $O(n + m)$. In einer Standardimplementierung, bei der der Graph bereitgestellt wird, wird die Platzkomplexität durch die Speicherung des Graphen und der Priority Queue dominiert, was $O(V + E)$ ergibt.