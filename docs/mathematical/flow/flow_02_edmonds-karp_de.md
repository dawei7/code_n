# Formale mathematische Spezifikation: Edmonds-Karp (Max Flow)

## 1. Definitionen und Notation

Sei $G = (V, E)$ ein endlicher gerichteter Graph, wobei $V$ die Menge der Knoten ist, sodass $|V| = n$, und $E \subseteq V \times V$ die Menge der gerichteten Kanten ist, sodass $|E| = m$. Wir definieren eine Kapazitätsfunktion $c: V \times V \to \mathbb{R}_{\ge 0}$, wobei $c(u, v) > 0$ gilt, falls $(u, v) \in E$, und $c(u, v) = 0$ andernfalls.

Ein **Flow Network** ist ein Tupel $(G, c, s, t)$, wobei $s \in V$ die Quelle (Source) und $t \in V$ die Senke (Sink) ist. Ein Flow ist eine Funktion $f: V \times V \to \mathbb{R}$, die folgende Bedingungen erfüllt:
1. **Kapazitätsbeschränkung:** $\forall u, v \in V, f(u, v) \le c(u, v)$.
2. **Antisymmetrie:** $\forall u, v \in V, f(u, v) = -f(v, u)$.
3. **Flusserhaltung:** $\forall u \in V \setminus \{s, t\}, \sum_{v \in V} f(u, v) = 0$.

Die **Restkapazität** $c_f(u, v)$ ist definiert als $c_f(u, v) = c(u, v) - f(u, v)$. Der Residualgraph $G_f = (V, E_f)$ besteht aus Kanten mit $c_f(u, v) > 0$.

## 2. Algebraische Charakterisierung

Der Edmonds-Karp-Algorithmus ist eine Implementierung der Ford-Fulkerson-Methode, die den augmentierenden Pfad $p$ in $G_f$ auswählt, welcher die Anzahl der Kanten minimiert (der kürzeste Pfad bezüglich der Anzahl der Hops).

**Augmentierungsschritt:**
Sei $p$ ein einfacher Pfad von $s$ nach $t$ in $G_f$. Die Engpasskapazität (Bottleneck Capacity) ist definiert als:
$$c_f(p) = \min \{c_f(u, v) : (u, v) \in p\}$$
Die Regel zur Aktualisierung des Flows lautet:
$$f_{new}(u, v) = f(u, v) + c_f(p) \cdot \mathbb{I}((u, v) \in p) - c_f(p) \cdot \mathbb{I}((v, u) \in p)$$
wobei $\mathbb{I}(\cdot)$ die Indikatorfunktion ist.

**Monotonie-Invariante:**
Sei $\delta_f(s, v)$ die Distanz des kürzesten Pfades (Anzahl der Kanten) von $s$ nach $v$ in $G_f$. Für jeden Knoten $v \in V \setminus \{s, t\}$ nimmt die Distanz $\delta_f(s, v)$ mit jeder Augmentierung monoton zu. Insbesondere gilt: Wenn $f$ zu $f'$ aktualisiert wird, dann ist $\delta_{f'}(s, v) \ge \delta_f(s, v)$.

**Lemma der kritischen Kante:**
Eine Kante $(u, v)$ ist *kritisch* auf einem augmentierenden Pfad $p$, wenn $c_f(u, v) = c_f(p)$. Wenn $(u, v)$ kritisch ist, verschwindet sie aus dem Residualgraphen $G_f$. Damit sie wieder erscheint, muss Flow entlang $(v, u)$ geschoben werden, was $\delta_f(s, v) = \delta_f(s, u) + 1$ erfordert. Nach dem Push erfüllt die neue Distanz $\delta_{f'}(s, u) = \delta_{f'}(s, v) + 1 \ge \delta_f(s, v) + 1 = \delta_f(s, u) + 2$. Somit erhöht sich die Distanz zu $u$ um mindestens 2, jedes Mal wenn $(u, v)$ kritisch wird.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die gesamte Zeitkomplexität beträgt $O(V E^2)$.

1. **Anzahl der Augmentierungen:** Jede Kante $(u, v)$ kann höchstens $O(V)$ Mal kritisch werden, da ihre Distanz von der Quelle jedes Mal, wenn sie kritisch wird, um mindestens 2 zunimmt und die maximale Distanz $|V|-1$ beträgt. Da es $O(E)$ Kanten gibt, beträgt die Gesamtzahl der Augmentierungen $O(V E)$.
2. **Aufwand pro Augmentierung:** Jede Augmentierung erfordert eine Breadth-First Search (BFS), um den kürzesten Pfad zu finden. Eine BFS auf einem Graphen mit $V$ Knoten und $E$ Kanten benötigt $O(E)$ Zeit.
3. **Gesamtaufwand:** Die Multiplikation der Anzahl der Augmentierungen mit den Kosten pro Augmentierung ergibt:
$$T(V, E) = O(V E) \cdot O(E) = O(V E^2)$$

### Platzkomplexität
Die Platzkomplexität beträgt $O(V^2)$ bei Verwendung einer Adjazenzmatrix zur Darstellung der Kapazitäten oder $O(V + E)$ bei Verwendung einer Adjazenzliste.

1. **Hilfsspeicher:** Der Algorithmus verwaltet ein `parent`-Array der Größe $O(V)$, ein `visited`-Array der Größe $O(V)$ und eine Queue für die BFS der Größe $O(V)$.
2. **Gesamtspeicher:** Der primäre Speicherbedarf liegt in der Struktur der Restkapazitäten. Bei Verwendung einer Adjazenzmatrix speichern wir $n^2$ Werte, was zu $O(V^2)$ Platz führt. Bei Verwendung einer Adjazenzliste speichern wir $O(V + E)$ Einträge. Da $E \le V^2$ gilt, wird die Matrixdarstellung oft für dichte Graphen bevorzugt, während die Listendarstellung für dünn besetzte Graphen optimal ist.