# Formale mathematische Spezifikation: Push-Relabel (Max Flow)

## 1. Definitionen und Notation

Sei $G = (V, E)$ ein gerichteter Graph, wobei $V$ die Menge der Knoten und $E \subseteq V \times V$ die Menge der Kanten ist. Wir definieren eine Kapazitätsfunktion $c: V \times V \to \mathbb{R}_{\geq 0}$, wobei $c(u, v) = 0$ gilt, falls $(u, v) \notin E$. Wir bestimmen eine Quelle $s \in V$ und eine Senke $t \in V$.

Der Algorithmus verwaltet einen **Preflow** $f: V \times V \to \mathbb{R}$, der die folgenden Bedingungen erfüllt:
1. **Kapazitätsbedingung:** $\forall u, v \in V, f(u, v) \leq c(u, v)$.
2. **Antisymmetrie:** $\forall u, v \in V, f(u, v) = -f(v, u)$.
3. **Nicht-Negativität des Überschusses:** Für alle $v \in V \setminus \{s\}$ ist der Überschussfluss $e(v)$ definiert als:
   $$e(v) = \sum_{u \in V} f(u, v) \geq 0$$
   Ein Knoten $v$ ist **aktiv**, wenn $v \in V \setminus \{s, t\}$ und $e(v) > 0$ gilt.

Wir definieren eine **Höhenfunktion** $h: V \to \mathbb{N}$ und die **Restkapazität** $c_f(u, v) = c(u, v) - f(u, v)$. Eine Restkante $(u, v)$ existiert, wenn $c_f(u, v) > 0$ gilt.

## 2. Algebraische Charakterisierung

Der Algorithmus hält die **Höheninvariante** aufrecht:
1. $h(s) = |V|$ und $h(t) = 0$.
2. Für jede Restkante $(u, v) \in E_f$ gilt $h(u) \leq h(v) + 1$.

### Die Push-Operation
Für einen aktiven Knoten $u$ und einen Nachbarn $v$, sodass $c_f(u, v) > 0$ und $h(u) = h(v) + 1$ gilt, aktualisiert die Push-Operation den Fluss:
$$\delta = \min(e(u), c_f(u, v))$$
$$f(u, v) \leftarrow f(u, v) + \delta, \quad f(v, u) \leftarrow f(v, u) - \delta$$
$$e(u) \leftarrow e(u) - \delta, \quad e(v) \leftarrow e(v) + \delta$$

### Die Relabel-Operation
Für einen aktiven Knoten $u$, bei dem für alle $v \in V$ mit $c_f(u, v) > 0$ die Bedingung $h(u) \leq h(v)$ gilt, aktualisiert die Relabel-Operation die Höhe:
$$h(u) \leftarrow 1 + \min \{h(v) : (u, v) \in E_f\}$$

### Korrektheitsinvariante
Der Algorithmus terminiert, wenn keine aktiven Knoten mehr vorhanden sind. Bei Terminierung stellt die Höhenfunktion sicher, dass im Restgraphen $G_f$ kein Pfad von $s$ nach $t$ existiert. Nach dem Max-Flow Min-Cut Theorem ist der resultierende Fluss $f$ ein maximaler Fluss, dessen Wert durch $\sum_{v \in V} f(v, t)$ gegeben ist.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Komplexität ergibt sich aus der Gesamtzahl der Operationen:
1. **Relabel-Operationen:** Jeder Knoten $u$ kann höchstens $2|V|-1$ Mal neu markiert werden. Gesamtzahl der Relabels: $O(V^2)$.
2. **Sättigende Pushes:** Ein Push ist sättigend, wenn $c_f(u, v)$ zu 0 wird. Zwischen zwei sättigenden Pushes auf einer Kante $(u, v)$ müssen $u$ und $v$ neu markiert werden. Gesamtzahl der sättigenden Pushes: $O(VE)$.
3. **Nicht-sättigende Pushes:** Unter Verwendung der "Highest-Label"-Auswahlregel ist die Anzahl der nicht-sättigenden Pushes im Allgemeinen durch $O(V^2 E)$ beschränkt, für die Highest-Label-Variante jedoch spezifisch durch $O(V^3)$.

Addiert man diese Werte, ergibt sich eine Gesamtlaufzeit von $O(V^3)$. Der Arbeitsaufwand pro Iteration wird durch die Suche nach einer zulässigen Kante dominiert, welche über den Relabel-Prozess amortisiert wird.

### Platzkomplexität
Der Algorithmus benötigt:
1. **Restkapazitätsmatrix:** $O(V^2)$, um $c_f(u, v)$ für alle Paare zu speichern.
2. **Hilfs-Arrays:** $O(V)$, um $h(v)$ und $e(v)$ zu speichern.
3. **Aktive Menge:** $O(V)$, um die Menge der aktiven Knoten zu verwalten.

Die gesamte Platzkomplexität beträgt $O(V^2)$, was für dichte Graphen, die durch Adjazenzmatrizen dargestellt werden, optimal ist.