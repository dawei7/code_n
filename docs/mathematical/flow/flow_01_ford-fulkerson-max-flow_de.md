# Formale mathematische Spezifikation: Ford-Fulkerson (Max Flow)

## 1. Definitionen und Notation

Sei $G = (V, E)$ ein gerichteter Graph, wobei $V$ eine endliche Menge von Knoten und $E \subseteq V \times V$ eine Menge gerichteter Kanten ist. Wir definieren eine Kapazitätsfunktion $c: V \times V \to \mathbb{R}_{\geq 0}$, wobei $c(u, v) > 0$ gilt, falls $(u, v) \in E$, und $c(u, v) = 0$ andernfalls. Wir bestimmen einen Quellknoten $s \in V$ und einen Senkenknoten $t \in V$.

Ein **Flow** ist eine Funktion $f: V \times V \to \mathbb{R}$, die die folgenden drei Bedingungen erfüllt:
1. **Kapazitätsbedingung:** $\forall u, v \in V, f(u, v) \leq c(u, v)$.
2. **Antisymmetrie:** $\forall u, v \in V, f(u, v) = -f(v, u)$.
3. **Flusserhaltung:** $\forall u \in V \setminus \{s, t\}, \sum_{v \in V} f(u, v) = 0$.

Der **Wert des Flows** ist definiert als $|f| = \sum_{v \in V} f(s, v)$. Das Ziel ist es, einen Flow $f$ zu finden, der $|f|$ maximiert.

Die **Restkapazität** $c_f: V \times V \to \mathbb{R}$ ist definiert als $c_f(u, v) = c(u, v) - f(u, v)$. Der **Residualgraph** $G_f = (V, E_f)$ besteht aus Kanten mit $c_f(u, v) > 0$.

## 2. Algebraische Charakterisierung

Die Ford-Fulkerson-Methode basiert auf dem **Max-Flow Min-Cut-Theorem**, welches besagt, dass der Wert eines maximalen Flows gleich der Kapazität eines minimalen Schnitts ist. Der Algorithmus verbessert den Flow iterativ, indem er einen **augmentierenden Pfad** $p$ im Residualgraphen $G_f$ findet.

### Augmentierung
Sei $p$ ein einfacher Pfad von $s$ nach $t$ in $G_f$. Die Restkapazität des Pfades ist:
$$c_f(p) = \min \{c_f(u, v) : (u, v) \in p\}$$

Der Flow $f$ wird wie folgt zu $f'$ aktualisiert:
$$f'(u, v) = \begin{cases} f(u, v) + c_f(p) & \text{falls } (u, v) \in p \\ f(u, v) - c_f(p) & \text{falls } (v, u) \in p \\ f(u, v) & \text{sonst} \end{cases}$$

### Schleifeninvariante
Zu Beginn jeder Iteration ist der Flow $f$ ein gültiger Flow. Der Algorithmus terminiert, wenn kein Pfad $p$ von $s$ nach $t$ in $G_f$ existiert. Gemäß dem Max-Flow Min-Cut-Theorem ist der aktuelle Flow $f$ ein maximaler Flow, wenn kein solcher Pfad existiert.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität beträgt $O(E \cdot |f^*|)$, wobei $|f^*|$ der Wert des maximalen Flows ist.

**Herleitung:**
1. Jede Iteration des Algorithmus identifiziert einen augmentierenden Pfad mittels Depth-First Search (DFS), was $O(V + E)$ Zeit in Anspruch nimmt. Da der Graph für Flusszwecke zusammenhängend ist, entspricht dies $O(E)$.
2. In jeder Iteration erhöht sich der Flow-Wert $|f|$ um mindestens 1 (unter der Annahme ganzzahliger Kapazitäten).
3. Die Gesamtzahl der Augmentierungen ist durch den Wert des maximalen Flows $|f^*|$ beschränkt.
4. Somit ergibt sich eine Gesamtlaufzeit von $O(E \cdot |f^*|)$. 

*Hinweis:* Bei irrationalen Kapazitäten ist die Terminierung des Algorithmus nicht garantiert. Bei ganzzahligen Kapazitäten terminiert der Algorithmus garantiert in einer endlichen Anzahl von Schritten.

### Platzkomplexität
Die Platzkomplexität beträgt $O(V^2)$ oder $O(V + E)$, abhängig von der Implementierung des Residualgraphen.

**Herleitung:**
1. **Adjacency Matrix:** Das Speichern der Kapazität $c(u, v)$ für alle Paare $(u, v) \in V \times V$ erfordert $O(V^2)$ Speicherplatz.
2. **Adjacency List:** Das Speichern des Graphen als Adjacency List erfordert $O(V + E)$ Speicherplatz für die Knoten und Kanten.
3. **Zusätzlicher Speicher:** Der DFS-Stack und das `parent`-Array, die zur Rekonstruktion des Pfades verwendet werden, benötigen $O(V)$ Speicherplatz.
4. Daher wird die gesamte Platzkomplexität durch die Repräsentation des Graphen dominiert: $O(V^2)$ für dichte Matrizen oder $O(V + E)$ für dünnbesetzte Adjacency Lists.