# Formale mathematische Spezifikation: Dinic-Algorithmus (Max Flow)

## 1. Definitionen und Notation

Sei $G = (V, E)$ ein gerichteter Graph, wobei $V$ die Menge der Knoten und $E \subseteq V \times V$ die Menge der Kanten ist. Wir definieren eine Kapazitätsfunktion $c: E \to \mathbb{R}^+$. Ein Flow Network ist ein Tupel $(G, c, s, t)$, wobei $s \in V$ die Quelle und $t \in V$ die Senke ist.

*   **Flow:** Eine Funktion $f: V \times V \to \mathbb{R}$, die folgende Bedingungen erfüllt:
    1.  **Kapazitätsbeschränkung:** $\forall u, v \in V, f(u, v) \leq c(u, v)$.
    2.  **Schiefsymmetrie:** $\forall u, v \in V, f(u, v) = -f(v, u)$.
    3.  **Flusserhaltung:** $\forall u \in V \setminus \{s, t\}, \sum_{v \in V} f(u, v) = 0$.
*   **Residualgraph:** Gegeben einen Flow $f$, besitzt der Residualgraph $G_f = (V, E_f)$ die Kanten $E_f = \{ (u, v) \in V \times V : c_f(u, v) > 0 \}$, wobei die Residualkapazität $c_f(u, v) = c(u, v) - f(u, v)$ ist.
*   **Level Graph:** Ein Teilgraph $L_G = (V, E_L)$, wobei $E_L = \{ (u, v) \in E_f : \text{dist}(s, v) = \text{dist}(s, u) + 1 \}$ und $\text{dist}(s, v)$ die kürzeste Pfaddistanz von $s$ nach $v$ in $G_f$ mittels BFS ist.
*   **Blocking Flow:** Ein Flow $f'$ im $L_G$, sodass jeder Pfad von $s$ nach $t$ in $L_G$ mindestens eine Kante $(u, v)$ enthält, für die $f'(u, v) = c_f(u, v)$ gilt.

## 2. Algebraische Charakterisierung

Der Dinic-Algorithmus konstruiert iterativ eine Folge von Flows $f_0, f_1, \dots, f_k$, bis $t$ von $s$ aus in $G_{f_k}$ nicht mehr erreichbar ist.

**Die Level-Graph-Invariante:**
Sei $d_i(v)$ die kürzeste Pfaddistanz von $s$ nach $v$ im Residualgraphen $G_{f_i}$. Der Algorithmus erhält die Eigenschaft $d_{i+1}(v) \geq d_i(v)$ für alle $v \in V$ aufrecht. Insbesondere gilt: Wenn $t$ in $G_{f_{i+1}}$ erreichbar ist, dann ist $d_{i+1}(t) > d_i(t)$.

**Konstruktion des Blocking Flow:**
In jeder Phase $i$ finden wir einen Blocking Flow $f'_i$ im Level Graph $L_{G_i}$. Die Update-Regel für den globalen Flow lautet:
$$f_{i+1}(u, v) = f_i(u, v) + f'_i(u, v)$$
Der Algorithmus terminiert, wenn $t \notin \{v \in V : \exists \text{ Pfad } s \to v \text{ in } G_{f_k}\}$. Nach dem Max-Flow Min-Cut Theorem ist der resultierende Flow $f_k$ genau dann maximal, wenn es keinen augmentierenden Pfad in $G_{f_k}$ mehr gibt.

**Next-Edge Pointer Optimierung:**
Sei $\text{adj}(u)$ die Menge der Nachbarn von $u$. Wir definieren einen Pointer $\text{ptr}(u)$, der den Index der ersten Kante in $\text{adj}(u)$ verfolgt, die noch nicht gesättigt ist. Der Suchraum der DFS wird wie folgt beschnitten:
$$\forall u \in V, \text{search}(u) \subseteq \{v \in \text{adj}(u) : \text{index}(v) \geq \text{ptr}(u)\}$$
Dies stellt sicher, dass jede Kante pro Phase nur eine konstante Anzahl von Malen untersucht wird.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Komplexität ergibt sich aus zwei Komponenten: der Anzahl der Phasen und dem Arbeitsaufwand pro Phase.

1.  **Anzahl der Phasen:** Da jede Phase (außer der letzten) die kürzeste Pfaddistanz $d(s, t)$ im Residualgraphen strikt erhöht und $d(s, t) < |V|$ gilt, gibt es höchstens $|V| - 1$ Phasen.
2.  **Arbeitsaufwand pro Phase:**
    *   **BFS:** Die Konstruktion des Level Graphs benötigt $O(E)$.
    *   **DFS:** Mit der `ptr`-Optimierung wird jede Kante pro Phase höchstens einmal durchlaufen, um Flow zu pushen, und jeder Knoten wird höchstens $O(V)$ Mal besucht, um von Sackgassen zurückzukehren (Backtracking). Somit benötigt das Finden eines Blocking Flow $O(V \cdot E)$.
3.  **Gesamtkomplexität:**
    $$\sum_{\text{Phasen}} O(V \cdot E) = O(V) \cdot O(V \cdot E) = O(V^2 E)$$

### Platzkomplexität
*   **Adjazenz-Repräsentation:** Wir speichern den Graphen und die Residualkapazitäten, was $O(V + E)$ Platz erfordert.
*   **Hilfsstrukturen:** Das `level`-Array, das `ptr`-Array und der Rekursions-Stack für die DFS benötigen jeweils $O(V)$ Platz.
*   **Gesamtplatz:** $O(V + E)$, was für einen graphenbasierten Flow-Algorithmus optimal ist.