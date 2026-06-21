# Formale mathematische Spezifikation: Tiefensuche (DFS)

## 1. Definitionen und Notation

Sei $G = (V, E)$ ein Graph, wobei $V = \{v_1, v_2, \dots, v_n\}$ eine endliche Menge von Knoten und $E \subseteq V \times V$ eine Menge von Kanten ist. Für einen gerichteten Graphen bezeichnen wir die Adjazenzmenge eines Knotens $u \in V$ als $Adj(u) = \{v \in V \mid (u, v) \in E\}$.

Wir definieren die folgenden Zustandsvariablen während der Ausführung des Algorithmus:
*   **Entdeckungszeit:** Eine Abbildung $d: V \to \mathbb{N}_0$, wobei $d(u)$ den Zeitpunkt angibt, zu dem der Knoten $u$ zum ersten Mal besucht wird.
*   **Abschlusszeit:** Eine Abbildung $f: V \to \mathbb{N}_0$, wobei $f(u)$ den Zeitpunkt angibt, zu dem die Exploration des Teilbaums mit der Wurzel $u$ abgeschlossen ist.
*   **Vorgänger-Abbildung:** Eine partielle Funktion $\pi: V \to V \cup \{\text{null}\}$, wobei $\pi(v) = u$ gilt, falls $v$ während der Exploration von $u$ entdeckt wurde.
*   **Färbung:** Eine Funktion $c: V \to \{\text{white, gray, black}\}$, die den Status als unbesucht, aktiv bzw. abgeschlossen repräsentiert.
*   **Globaler Timer:** Eine Variable $t \in \mathbb{N}_0$, die bei jedem Entdeckungs- und Abschlussereignis monoton inkrementiert wird.

Das Ergebnis des Algorithmus ist das Tupel $(d, f, \pi)$, welches die Entdeckungszeiten, Abschlusszeiten und den Vorgänger-Teilgraphen $G_\pi = (V, E_\pi)$ darstellt, wobei $E_\pi = \{(\pi(v), v) \in E \mid \pi(v) \neq \text{null}\}$.

## 2. Algebraische Charakterisierung

Der DFS-Algorithmus kann durch den rekursiven Übergang des Zustands $c(u)$ charakterisiert werden. Für einen Startknoten $s$ definiert der Algorithmus eine Traversierung, die das **Klammertheorem** erfüllt.

### Das Klammertheorem
Für zwei beliebige Knoten $u, v \in V$ gilt genau eine der folgenden Bedingungen:
1. Die Intervalle $[d(u), f(u)]$ und $[d(v), f(v)]$ sind disjunkt, und weder $u$ noch $v$ ist ein Nachfahre des jeweils anderen im DFS-Wald.
2. Das Intervall $[d(u), f(u)]$ ist vollständig in $[d(v), f(v)]$ enthalten, und $u$ ist ein Nachfahre von $v$ im DFS-Wald.
3. Das Intervall $[d(v), f(v)]$ ist vollständig in $[d(u), f(u)]$ enthalten, und $v$ ist ein Nachfahre von $u$ im DFS-Wald.

### Rekurrenz
Die Entdeckungs- und Abschlusszeiten werden durch die folgende rekursive Struktur bestimmt:
$$d(u) = \min \{t \mid \text{state of } u \text{ transitions from white to gray}\}$$
$$f(u) = \max \{t \mid \text{state of } u \text{ transitions from gray to black}\}$$

Der Algorithmus erhält die Invariante aufrecht, dass zu jedem Zeitpunkt $t$ die Menge der grauen Knoten einen Pfad im DFS-Wald von der Wurzel bis zum aktuell explorierten Knoten bildet. Die Exploration von $u$ ist genau dann abgeschlossen, wenn für alle $v \in Adj(u)$ gilt, dass $v$ besucht wurde und $f(v)$ definiert ist.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität ergibt sich aus der Summe des Aufwands für jeden Knoten und jede Kante.
1. **Initialisierung:** Das Setzen von $c(v) = \text{white}$ für alle $v \in V$ benötigt $\Theta(|V|)$.
2. **Knotenverarbeitung:** Jeder Knoten $u$ wird genau einmal besucht, wenn seine Farbe von white zu gray wechselt. Der Aufwand pro Knoten (exklusive der Schleife über die Nachbarn) beträgt $O(1)$.
3. **Kantenverarbeitung:** Die Schleife `for v in G[u]` iteriert über alle $v \in Adj(u)$. Über die gesamte Ausführung hinweg wird jede Kante $(u, v) \in E$ genau einmal (in gerichteten Graphen) oder zweimal (in ungerichteten Graphen) untersucht.

Die gesamte Zeitkomplexität $T(V, E)$ ist:
$$T(V, E) = \sum_{u \in V} (1 + \text{deg}(u)) = |V| + \sum_{u \in V} \text{deg}(u)$$
Nach dem Handschlag-Lemma gilt $\sum_{u \in V} \text{deg}(u) = |E|$ (bzw. $2|E|$ bei ungerichteten Graphen). Somit gilt $T(V, E) = \Theta(|V| + |E|)$.
Bei einer Repräsentation mittels Adjazenzmatrix iteriert die innere Schleife für jeden Knoten $u$ über alle $n$ Knoten, was zu $T(V) = \sum_{u \in V} O(|V|) = O(|V|^2)$ führt.

### Platzkomplexität
Die Platzkomplexität $S(V, E)$ wird durch die zusätzlichen Datenstrukturen bestimmt:
1. **Speicher:** Die Arrays für $d, f, \pi$ sowie die Menge/das Array für $c$ benötigen $\Theta(|V|)$ Speicherplatz.
2. **Rekursions-Stack:** Im Schlechtesten Fall (z. B. bei einem Pfad-Graphen) beträgt die Tiefe des Rekursions-Stacks $|V|$. Daher ist der Stack-Platzbedarf $O(|V|)$.

Die gesamte Platzkomplexität beträgt $S(V) = \Theta(|V|)$.