# Formale Mathematische Spezifikation: Bereichsaktualisierung mit Lazy Propagation (Summe)

## 1. Definitionen und Notation

Sei $A = [a_0, a_1, \dots, a_{n-1}]$ ein Array von $n$ Elementen, wobei $a_i \in \mathbb{R}$. Wir definieren einen Segment Tree als einen gewurzelten Binärbaum $\mathcal{T}$, wobei jeder Knoten $v$ ein zusammenhängendes Intervall $[lo_v, hi_v] \subseteq [0, n-1]$ repräsentiert.

- **Zustandsraum:** Jeder Knoten $v$ verwaltet zwei Werte:
    - $S_v$: Die Summe der Elemente im Bereich $[lo_v, hi_v]$, definiert als $S_v = \sum_{i=lo_v}^{hi_v} a_i$.
    - $L_v$: Ein Lazy Propagation Wert, der eine ausstehende additive Aktualisierung repräsentiert, die auf alle Elemente im Bereich $[lo_v, hi_v]$ angewendet werden soll.
- **Definitionsbereich:** Die Menge aller möglichen Zustände ist $\mathcal{S} = \{ (S_v, L_v) \mid v \in \mathcal{T} \}$.
- **Update-Operation:** Eine Bereichsaktualisierung $U(l, r, \delta)$ modifiziert das Array so, dass $a_i \leftarrow a_i + \delta$ für alle $i \in [l, r] \cap [0, n-1]$.
- **Query-Operation:** Eine Bereichssummen-Query $Q(l, r)$ gibt $\sum_{i=l}^r a_i$ zurück.

## 2. Algebraische Charakterisierung

Die Korrektheit des Algorithmus beruht auf der Distributivität des Summenoperators über die additive Aktualisierung.

### Der Apply-Operator
Für einen Knoten $v$, der das Intervall $[lo_v, hi_v]$ abdeckt, aktualisiert das Anwenden eines Lazy-Wertes $\delta$ den Zustand wie folgt:
1. $S_v \leftarrow S_v + \delta \cdot (hi_v - lo_v + 1)$
2. $L_v \leftarrow L_v + \delta$

### Rekursionsgleichungen
Die Summe $S_v$ wird durch die Invariante aufrechterhalten:
$$S_v = \begin{cases} a_{lo_v} & \text{if } lo_v = hi_v \\ S_{left(v)} + S_{right(v)} & \text{if } lo_v < hi_v \end{cases}$$

Wenn eine Aktualisierung $U(l, r, \delta)$ auf Knoten $v$ angewendet wird:
1. **Vollständige Überlappung ($[lo_v, hi_v] \subseteq [l, r]$):** Wende die Aktualisierung auf $S_v$ und $L_v$ an und beende.
2. **Partielle Überlappung ($[lo_v, hi_v] \cap [l, r] \neq \emptyset$):**
   - Führe eine "Push"-Operation aus: Falls $L_v \neq 0$, wende $L_v$ auf die Kinder $left(v)$ und $right(v)$ an, setze dann $L_v = 0$.
   - Rekursion: $update(left(v), \dots) + update(right(v), \dots)$.
   - Neuberechnung: $S_v = S_{left(v)} + S_{right(v)}$.

### Invariante
Für jeden Knoten $v$ ist die wahre Summe $S_v$ stets konsistent mit der Summe seiner Kinder plus dem Effekt seines eigenen ausstehenden Lazy-Wertes $L_v$, angewendet auf seine Bereichslänge $len_v = hi_v - lo_v + 1$:
$$S_v = \left( \sum_{i \in \text{leaves}(v)} a_i \right) + L_v \cdot len_v$$

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität wird durch die Anzahl der besuchten Knoten während einer Aktualisierung oder Query bestimmt.
- **Rekurrenz:** Sei $T(n)$ die Zeit, um einen Bereich der Größe $n$ zu verarbeiten.
- Im schlechtesten Fall besucht der Algorithmus Knoten, die partiell mit $[l, r]$ überlappen. Auf jeder Ebene des Baumes gibt es höchstens 4 Knoten, die die Grenzen des Query-Bereichs partiell überlappen.
- Da die Höhe des Baumes $H = \lceil \log_2 n \rceil$ beträgt und wir an jedem besuchten Knoten einen konstanten Arbeitsaufwand leisten (die `push`- und `apply`-Operationen sind $O(1)$):
$$T(n) = O(H) = O(\log n)$$
Somit sind sowohl `update`- als auch `query`-Operationen strikt $O(\log n)$.

### Platzkomplexität
- **Baumspeicher:** Der Segment Tree ist ein vollständiger Binärbaum (oder ein Heap-indiziertes Array). Für $n$ Blätter beträgt die Anzahl der Knoten im Baum höchstens $4n$.
- **Hilfsspeicher:** Wir verwalten zwei Arrays, `tree` und `lazy`, jeweils der Größe $4n$.
- **Gesamtplatz:** Die Gesamtplatzkomplexität beträgt $O(n)$, was optimal für die Speicherung des Zustands des Segment Tree ist.