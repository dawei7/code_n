# Formale mathematische Spezifikation: Bellman-Ford-Algorithmus

## 1. Definitionen und Notation

Sei $G = (V, E)$ ein gerichteter, gewichteter Graph, wobei $V = \{v_1, v_2, \dots, v_n\}$ die Menge der Knoten ist, sodass $|V| = n$, und $E \subseteq V \times V$ die Menge der gerichteten Kanten ist. Jede Kante $e = (u, v) \in E$ ist mit einer Gewichtsfunktion $w: E \to \mathbb{R}$ verknüpft.

Wir definieren Folgendes:
*   **Quellknoten:** Ein designierter Knoten $s \in V$.
*   **Distanzfunktion:** Eine Abbildung $d: V \to \mathbb{R} \cup \{\infty\}$, wobei $d(v)$ die aktuelle Schätzung der kürzesten Pfaddistanz von $s$ nach $v$ darstellt.
*   **Pfadgewicht:** Für einen Pfad $P = (v_0, v_1, \dots, v_k)$ ist das Gewicht definiert als $W(P) = \sum_{i=1}^{k} w(v_{i-1}, v_i)$.
*   **Kürzester Pfad:** Die Distanz $\delta(s, v) = \inf \{ W(P) : P \text{ ist ein Pfad von } s \text{ nach } v \}$. Wenn kein Pfad existiert, ist $\delta(s, v) = \infty$. Wenn $v$ von einem Zyklus mit negativem Gewicht aus erreichbar ist, ist $\delta(s, v) = -\infty$.

## 2. Algebraische Charakterisierung

Der Bellman-Ford-Algorithmus ist eine Anwendung der dynamischen Programmierung, die auf dem Prinzip der Relaxation basiert. Wir definieren $d^{(k)}(v)$ als das Gewicht des kürzesten Pfades von $s$ nach $v$ unter Verwendung von höchstens $k$ Kanten.

### Rekursionsgleichung
Die optimale Substruktur wird durch die folgende Rekursionsgleichung definiert:
1.  **Induktionsanfang:** 
    $d^{(0)}(s) = 0$ und $d^{(0)}(v) = \infty$ für alle $v \in V \setminus \{s\}$.
2.  **Induktionsschritt:** Für $k = 1, 2, \dots, n-1$:
    $d^{(k)}(v) = \min \left( d^{(k-1)}(v), \min_{(u, v) \in E} \{ d^{(k-1)}(u) + w(u, v) \} \right)$

### Schleifeninvariante
Zu Beginn jeder Iteration $k$ der äußeren Schleife (wobei $k$ von $1$ bis $n-1$ läuft), gilt die folgende Invariante:
Für jeden Knoten $v \in V$ ist $d(v)$ das Gewicht des kürzesten Pfades von $s$ nach $v$ unter Verwendung von höchstens $k-1$ Kanten.

### Erkennung von Zyklen mit negativem Gewicht
Ein Graph enthält genau dann einen Zyklus mit negativem Gewicht, der von $s$ aus erreichbar ist, wenn eine Kante $(u, v) \in E$ existiert, sodass:
$$\delta(s, v) > \delta(s, u) + w(u, v)$$
Nach $n-1$ Iterationen führt der Algorithmus eine abschließende Überprüfung durch. Wenn für eine beliebige Kante $(u, v) \in E$ gilt: $d(u) + w(u, v) < d(v)$, dann enthält der Graph einen negativen Zyklus, da der kürzeste Pfad mindestens $n$ Kanten erfordern würde, was nach dem Schubfachprinzip (Pigeonhole Principle) die Existenz eines Zyklus impliziert.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus besteht aus einer äußeren Schleife, die $n-1$ Mal ausgeführt wird. Innerhalb dieser Schleife iteriert der Algorithmus über die Menge der Kanten $E$. 

Die Gesamtzahl der Operationen $T(n, m)$ (wobei $m = |E|$) ergibt sich zu:
$$T(n, m) = \sum_{k=1}^{n-1} \sum_{(u, v) \in E} \Theta(1) = \Theta((n-1) \cdot m) = \Theta(n \cdot m)$$
Im Schlechtesten Fall, wenn der Graph dicht ist ($m = \Theta(n^2)$), beträgt die Komplexität $O(n^3)$. In einem dünnen Graphen ($m = \Theta(n)$) beträgt die Komplexität $O(n^2)$. Die Optimierung durch "vorzeitigen Abbruch" (Beendigung, falls in einer Iteration keine Relaxation stattfindet) ermöglicht eine Zeitkomplexität im Bestfall von $\Omega(m)$, was eintritt, wenn der Kürzeste-Pfad-Baum bereits in der ersten Iteration gefunden wird.

### Platzkomplexität
Der Algorithmus verwaltet ein Distanz-Array $d$ der Größe $|V|$, um die aktuellen Schätzungen der kürzesten Pfade zu speichern. 
*   **Zusätzlicher Speicherplatz:** $O(n)$ zur Speicherung der Distanzschätzungen.
*   **Gesamtspeicherplatz:** $O(n + m)$ zur Speicherung der Graphrepräsentation (die Adjacency List oder Edge List) und des Distanz-Arrays.
Da der Algorithmus direkt auf der Edge List operiert, ist die zusätzliche Platzkomplexität strikt $O(n)$, was die Anforderung für $O(V)$ Speicherplatz erfüllt.