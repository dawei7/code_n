# Formale mathematische Spezifikation: Bellman-Ford (Dynamische Programmierung)

## 1. Definitionen und Notation

Sei $G = (V, E)$ ein gerichteter Graph, wobei $V = \{v_1, v_2, \dots, v_n\}$ die Menge der Knoten ist, sodass $|V| = n$, und $E \subseteq V \times V$ die Menge der gerichteten Kanten ist. Wir definieren eine Gewichtsfunktion $w: E \to \mathbb{R}$, die jeder Kante $(u, v) \in E$ ein reellwertiges Gewicht zuweist.

Wir definieren einen Startknoten $s \in V$. Das Ziel ist die Berechnung der kürzesten Pfaddistanz $\delta(s, u)$ für alle $u \in V$.

Wir definieren den DP-Zustandsraum wie folgt:
Sei $dp(k, u)$ das Gewicht des kürzesten Pfades von $s$ nach $u$ unter Verwendung von maximal $k$ Kanten, wobei $k \in \{0, 1, \dots, n-1\}$ und $u \in V$.

Der Definitionsbereich der Distanzfunktion ist definiert als:
$$dp: \{0, \dots, n-1\} \times V \to \mathbb{R} \cup \{\infty\}$$

## 2. Algebraische Charakterisierung

Der Bellman-Ford-Algorithmus basiert auf dem Optimalitätsprinzip. Der kürzeste Pfad zu $u$ unter Verwendung von maximal $k$ Kanten ist entweder der kürzeste Pfad zu $u$ unter Verwendung von maximal $k-1$ Kanten oder er entsteht durch die Erweiterung eines kürzesten Pfades zu einem Vorgänger $v$ unter Verwendung von $k-1$ Kanten um die Kante $(v, u)$.

### Rekursionsgleichung
Der Induktionsanfang für $k=0$ lautet:
$$dp(0, u) = \begin{cases} 0 & \text{if } u = s \\ \infty & \text{if } u \neq s \end{cases}$$

Für $k \in \{1, \dots, n-1\}$ lautet die Rekursionsgleichung:
$$dp(k, u) = \min \left( dp(k-1, u), \min_{(v, u) \in E} \{ dp(k-1, v) + w(v, u) \} \right)$$

### Korrektheit und Konvergenz
Ein einfacher Pfad in einem Graphen mit $n$ Knoten enthält maximal $n-1$ Kanten. Durch vollständige Induktion über $k$ konvergiert $dp(k, u)$ gegen die tatsächliche kürzeste Pfaddistanz $\delta(s, u)$ für alle $u$, die von $s$ aus innerhalb von $n-1$ Kanten erreichbar sind. Wenn der Graph keine Zyklen mit negativem Gewicht enthält, gilt $\delta(s, u) = dp(n-1, u)$.

### Platzoptimierter Zustand
Durch die Beobachtung, dass der Zustand $dp(k, \cdot)$ nur von $dp(k-1, \cdot)$ abhängt, können wir einen 1D-Zustand $dist[u]$ definieren, der die aktuell beste bekannte Distanz repräsentiert. Der Übergang wird zu einer iterativen Relaxation:
$$dist[u] \leftarrow \min(dist[u], dist[v] + w(v, u)) \quad \forall (v, u) \in E$$
Diese Aktualisierung wird $n-1$ Mal durchgeführt.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus besteht aus zwei verschachtelten Schleifen:
1. Eine äußere Schleife, die $k$ von $1$ bis $n-1$ iteriert.
2. Eine innere Schleife, die über alle Kanten $(u, v) \in E$ iteriert.

Die Gesamtzahl der Operationen $T(n, |E|)$ ergibt sich aus der Summe:
$$T(n, |E|) = \sum_{k=1}^{n-1} \sum_{(u, v) \in E} \Theta(1)$$
Da die innere Summation für jede der $n-1$ Iterationen $|E|$ Mal durchgeführt wird:
$$T(n, |E|) = (n-1) \cdot |E| = \Theta(n \cdot |E|)$$
Somit beträgt die Zeitkomplexität $O(V \cdot E)$.

### Platzkomplexität
Der Algorithmus verwaltet ein Distanz-Array $dist$ der Größe $|V|$.
- **Zusätzlicher Speicherplatz:** Der für das Distanz-Array benötigte Speicherplatz beträgt $O(V)$.
- **Gesamtspeicherplatz:** Da der Graph als Edge List der Größe $|E|$ gespeichert wird und das Distanz-Array $O(V)$ groß ist, beträgt die gesamte Platzkomplexität $O(V + E)$.
- Im Kontext der spezifischen DP-Formulierung benötigt die platzoptimierte Version $O(V)$ zusätzlichen Speicherplatz, um die aktuellen Schätzungen der kürzesten Pfade zu speichern.