# Formale mathematische Spezifikation: Kruskal-Algorithmus (Minimaler Spannbaum)

## 1. Definitionen und Notation

Sei $G = (V, E, w)$ ein zusammenhängender, ungerichteter, gewichteter Graph, wobei:
*   $V = \{v_1, v_2, \dots, v_n\}$ die Menge der Knoten ist, mit $|V| = n$.
*   $E \subseteq \{\{u, v\} : u, v \in V, u \neq v\}$ die Menge der Kanten ist, mit $|E| = m$.
*   $w: E \to \mathbb{R}^+$ eine Gewichtsfunktion ist, die jeder Kante einen positiven reellen Wert zuweist.

Ein **Spannbaum** $T = (V, E_T)$ ist ein Teilgraph von $G$, sodass $E_T \subseteq E$, $|E_T| = n - 1$ und $T$ azyklisch ist. Das Gewicht des Spannbaums ist definiert als $W(T) = \sum_{e \in E_T} w(e)$. Ein **Minimaler Spannbaum (MST)** ist ein Spannbaum $T^*$, für den $W(T^*) \leq W(T)$ für alle Spannbäume $T$ von $G$ gilt.

Der Algorithmus verwendet eine **Disjoint Set Union (DSU)** Datenstruktur, definiert als eine Partition $\mathcal{P} = \{S_1, S_2, \dots, S_k\}$ von $V$. Die DSU unterstützt zwei Operationen:
*   $\text{find}(v)$: Gibt das Repräsentantenelement der Menge $S_i$ zurück, die $v$ enthält.
*   $\text{union}(u, v)$: Vereinigt die Mengen, die $u$ und $v$ enthalten, falls sie verschieden sind, und erhält dabei die Partitionseigenschaft.

## 2. Algebraische Charakterisierung

Der Kruskal-Algorithmus ist eine Greedy-Strategie, die auf der **Schnitt-Eigenschaft** (Cut Property) von MSTs basiert. Für jeden Schnitt $(S, V \setminus S)$ von $G$ gilt: Wenn eine Kante $e$ die Kante mit dem minimalen Gewicht ist, die den Schnitt kreuzt, dann gehört $e$ zu einem MST von $G$.

Sei $E' = \{e_1, e_2, \dots, e_m\}$ die Menge der Kanten, sortiert nach $w(e_1) \leq w(e_2) \leq \dots \leq w(e_m)$. Der Algorithmus konstruiert eine Folge von Wäldern $F_i = (V, E_i)$, wobei $E_0 = \emptyset$ und $E_i$ durch die folgende Rekurrenz definiert ist:

$$E_i = \begin{cases} E_{i-1} \cup \{e_i\} & \text{if } e_i = \{u, v\} \text{ and } \text{find}(u) \neq \text{find}(v) \\ E_{i-1} & \text{otherwise} \end{cases}$$

**Schleifeninvariante:** In jedem Schritt $i$ ist der Wald $F_i$ eine Teilmenge eines MST von $G$.
*   **Induktionsanfang:** $F_0$ ist ein Wald aus $n$ isolierten Knoten, was trivialerweise eine Teilmenge jedes MST ist.
*   **Induktionsschritt:** Aufgrund der Schnitt-Eigenschaft gilt: Wenn $e_i$ zwei Zusammenhangskomponenten $C_u$ und $C_v$ verbindet und das minimale Gewicht unter allen Kanten besitzt, die $C_u$ mit $V \setminus C_u$ verbinden, dann ist es sicher, $e_i$ hinzuzufügen. Da wir die Kanten in nicht-absteigender Reihenfolge verarbeiten, ist garantiert, dass $e_i$ die Kante mit dem minimalen Gewicht ist, die den durch die Partition von $V$ in die aktuellen Zusammenhangskomponenten definierten Schnitt kreuzt.
*   **Terminierung:** Der Algorithmus terminiert, wenn $|E_i| = n - 1$, was zu einem Spannbaum $T^* = (V, E_{n-1})$ führt.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die gesamte Zeitkomplexität $T(n, m)$ ist die Summe aus der Sortierphase und den DSU-Operationen:

1.  **Sortierung:** Das Sortieren von $m$ Kanten benötigt $O(m \log m)$. Da $m \leq n^2$, gilt $\log m \leq \log n^2 = 2 \log n$, somit $O(m \log m) = O(m \log n)$.
2.  **DSU-Operationen:** Wir führen $m$ `find`-Operationen und höchstens $n-1$ `union`-Operationen aus. Unter Verwendung von Pfadkompression und Union-by-Rank beträgt die amortisierte Zeitkomplexität pro Operation $O(\alpha(n))$, wobei $\alpha$ die inverse Ackermann-Funktion ist.

Die gesamte Zeit beträgt:
$$T(n, m) = O(m \log m + m \cdot \alpha(n))$$
Da $\alpha(n)$ extrem langsam wächst und für alle praktischen $n$ effektiv konstant ist, dominiert der Sortierterm:
$$T(n, m) = O(m \log m) \equiv O(m \log n)$$

### Platzkomplexität
Die Platzkomplexität $S(n, m)$ wird durch die Speicheranforderungen bestimmt:
1.  **Graph-Speicherung:** $O(m)$ zur Speicherung der Edge List.
2.  **DSU-Struktur:** $O(n)$ zur Speicherung der `parent`- und `rank`-Arrays.
3.  **Ausgabe:** $O(n)$ zur Speicherung der Kanten des MST.

Somit ergibt sich die gesamte Platzkomplexität zu:
$$S(n, m) = O(n + m)$$
In einem dünn besetzten Graphen (sparse graph), in dem $m = O(n)$, vereinfacht sich dies zu $O(n)$.