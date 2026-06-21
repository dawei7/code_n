# Formale Mathematische Spezifikation: Bereichsminimumabfrage mit Verzögerten Aktualisierungen

## 1. Definitionen und Notation

Sei $A = [a_0, a_1, \dots, a_{n-1}]$ ein Array von Elementen, wobei $a_i \in \mathbb{R}$. Wir definieren einen Segment Tree $\mathcal{T}$ als einen gewurzelten Binärbaum, bei dem jeder Knoten $u$ einem geschlossenen Intervall $[L_u, R_u] \subseteq [0, n-1]$ entspricht.

- **Zustandsraum:** Jeder Knoten $u$ verwaltet zwei Werte:
    - $T_u$: Der Minimalwert im Bereich $[L_u, R_u]$, definiert als $T_u = \min_{i \in [L_u, R_u]} a_i$.
    - $\Lambda_u$: Ein Lazy-Propagation-Wert, der eine ausstehende additive Aktualisierung darstellt. $\Lambda_u \in \mathbb{R} \cup \{0\}$ (wobei $0$ das neutrale Element für die Addition bezeichnet).
- **Operationen:**
    - $\text{Update}(l, r, \delta)$: Für alle $i \in [l, r]$ gilt $a_i \leftarrow a_i + \delta$.
    - $\text{Query}(l, r)$: Gibt $\min_{i \in [l, r]} a_i$ zurück.
- **Definitionsbereich:** Die Menge der Indizes ist $\mathcal{I} = \{0, 1, \dots, n-1\}$. Die Baumstruktur ist so definiert, dass für jeden internen Knoten $u$ mit Kindern $v_{left}$ und $v_{right}$ gilt: $[L_u, R_u] = [L_{v_{left}}, R_{v_{left}}] \cup [L_{v_{right}}, R_{v_{right}}]$.

## 2. Algebraische Charakterisierung

Die Korrektheit des Algorithmus beruht auf der Distributivität des Minimum-Operators über die Addition.

### Die Aktualisierungs-Invariante
Für jeden Bereich $[L_u, R_u]$ gilt: Wenn wir eine additive Aktualisierung $\delta$ anwenden, ist das neue Minimum $T_u'$:
$$T_u' = \min_{i \in [L_u, R_u]} (a_i + \delta) = \left( \min_{i \in [L_u, R_u]} a_i \right) + \delta = T_u + \delta$$
Dies bestätigt, dass der Minimalwert um genau die Größe der Aktualisierung verschoben wird, unabhängig von der Segmentlänge.

### Lazy-Propagation-Rekurrenz
Sei $\text{push}(u)$ die Operation, die $\Lambda_u$ an ihre Kinder $v \in \{v_{left}, v_{right}\}$ propagiert. Die Zustandsübergänge sind:
1. $T_v \leftarrow T_v + \Lambda_u$
2. $\Lambda_v \leftarrow \Lambda_v + \Lambda_u$
3. $\Lambda_u \leftarrow 0$

Dies erfüllt die Invariante, dass der im Knoten gespeicherte Wert $T_u$ jederzeit alle Aktualisierungen, die auf den Bereich $[L_u, R_u]$ angewendet wurden und an $u$ "gepusht" wurden, korrekt widerspiegelt, aber möglicherweise noch nicht an seine Nachkommen.

### Abfrage-Rekurrenz
Die Abfragefunktion $Q(u, l, r)$ ist rekursiv definiert:
$$Q(u, l, r) =
\begin{cases}
\infty & \text{if } [L_u, R_u] \cap [l, r] = \emptyset \\
T_u & \text{if } [L_u, R_u] \subseteq [l, r] \\
\min(Q(v_{left}, l, r), Q(v_{right}, l, r)) & \text{otherwise}
\end{cases}$$
Vor der Auswertung des rekursiven Schritts wird $\text{push}(u)$ aufgerufen, um sicherzustellen, dass die Kindknoten $v_{left}, v_{right}$ die aktuellsten Werte enthalten.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus führt Operationen auf einem balancierten Binärbaum der Höhe $H = \lceil \log_2 n \rceil$ aus.

- **Aktualisierung/Abfrage:** Bei beiden Operationen besuchen wir Knoten im Baum. Ein Bereich $[l, r]$ wird in höchstens $O(\log n)$ kanonische Knoten zerlegt. Da jeder Knoten pro Operation höchstens eine konstante Anzahl von Malen besucht wird (aufgrund des Lazy-Propagation-Mechanismus), ist der geleistete Aufwand proportional zur Höhe des Baumes.
- **Rekurrenz:** Sei $W(n)$ der Aufwand für eine Operation auf einem Bereich der Größe $n$.
$$W(n) = 2W(n/2) + O(1) \implies W(n) = O(\log n)$$
Somit arbeiten sowohl `update_range` als auch `query_min` in $O(\log n)$ Zeit.

### Platzkomplexität
- **Baumspeicher:** Der Segment Tree ist ein vollständiger Binärbaum. Für ein Array der Größe $n$ ist die Anzahl der Knoten im Baum durch $4n$ begrenzt.
- **Hilfsspeicher:** Wir verwalten zwei Arrays, `tree` und `lazy`, jeweils der Größe $4n$.
- **Gesamtplatz:** Die Gesamtplatzkomplexität beträgt $O(n)$, was optimal für die Speicherung des Zustands des Segment Trees ist.