# Formale mathematische Spezifikation: Rat in a Maze

## 1. Definitionen und Notation

Sei $N \in \mathbb{N}^+$ die Dimension eines quadratischen Gitters. Wir definieren die Koordinaten-Indexmenge als $I_N = \{0, 1, \dots, N-1\}$. Der räumliche Bereich des Labyrinths wird durch das kartesische Produkt dargestellt:

$$\mathcal{C} = I_N \times I_N$$

Das Labyrinth ist formal als binäre Matrix $M \in \{0, 1\}^{N \times N}$ definiert, wobei für jede Koordinate $u = (r, c) \in \mathcal{C}$ gilt:
* $M(u) = 1$ repräsentiert eine offene, begehbare Zelle.
* $M(u) = 0$ repräsentiert eine blockierte Zelle (eine Wand).

Wir definieren die Menge der begehbaren Knoten $V \subseteq \mathcal{C}$ als:

$$V = \{ u \in \mathcal{C} \mid M(u) = 1 \}$$

Sei $\|\cdot\|_1$ die $L_1$-Norm (Manhattan-Distanz) auf $\mathbb{Z}^2$. Für zwei beliebige Koordinaten $u = (r_1, c_1)$ und $v = (r_2, c_2)$ ist die Distanz gegeben durch:

$$\|u - v\|_1 = |r_1 - r_2| + |c_1 - c_2|$$

Wir definieren die Menge der gerichteten Kanten $E \subseteq V \times V$, die gültige 4-Richtungs-Bewegungen innerhalb der offenen Räume des Labyrinths repräsentieren:

$$E = \{ (u, v) \in V \times V \mid \|u - v\|_1 = 1 \}$$

Das Labyrinth wird somit als ungewichteter, ungerichteter Gittergraph $G = (V, E)$ modelliert.

### Pfade und Richtungen
Sei $s = (0, 0) \in \mathcal{C}$ der Startknoten und $t = (N-1, N-1) \in \mathcal{C}$ der Zielknoten. Wir nehmen an, dass $s, t \in V$; falls $M(s) = 0$ oder $M(t) = 0$, ist die Menge der gültigen Pfade trivialerweise leer.

Ein **einfacher Pfad** $P$ der Länge $k$ von $s$ nach $t$ in $G$ ist eine Folge von Knoten $P = (v_0, v_1, \dots, v_k)$, die folgende Bedingungen erfüllt:
1. $v_0 = s$ und $v_k = t$.
2. $(v_i, v_{i+1}) \in E$ für alle $0 \le i < k$.
3. $v_i \neq v_j$ für alle $0 \le i < j \le k$ (die Eigenschaft der Selbstvermeidung).

Sei $\mathcal{P}_{s, t}$ die Menge aller solcher einfachen Pfade von $s$ nach $t$.

Um Pfade als gerichtete Strings darzustellen, definieren wir die Menge der Bewegungsrichtungen $\mathcal{D} = \{\text{'U'}, \text{'D'}, \text{'L'}, \text{'R'}\}$ und eine bijektive Abbildung $\phi: E \to \mathcal{D}$, definiert durch:

$$\phi((r, c), (r', c')) = \begin{cases} 
\text{'U'} & \text{falls } r' = r - 1 \\
\text{'D'} & \text{falls } r' = r + 1 \\
\text{'L'} & \text{falls } c' = c - 1 \\
\text{'R'} & \text{falls } c' = c + 1 
\end{cases}$$

Für jeden einfachen Pfad $P = (v_0, v_1, \dots, v_k) \in \mathcal{P}_{s, t}$ ist seine entsprechende String-Repräsentation $S(P) \in \mathcal{D}^k$ die Folge:

$$S(P) = \left( \phi(v_0, v_1), \phi(v_1, v_2), \dots, \phi(v_{k-1}, v_k) \right)$$

Das Ziel des **Rat in a Maze**-Algorithmus ist die Konstruktion der Menge aller Pfad-Strings:

$$\mathcal{S}_{s, t} = \{ S(P) \mid P \in \mathcal{P}_{s, t} \}$$

---

## 2. Algebraische Charakterisierung

Der Backtracking-Algorithmus exploriert systematisch den Zustandsraum der selbstvermeidenden Pfade auf $G$ mittels Tiefensuche (DFS) mit Pruning.

### Zustandsraum-Repräsentation
Ein Zustand $\sigma$ in der Backtracking-Suche wird durch ein Tripel repräsentiert:

$$\sigma = (u, \mathcal{V}, \pi)$$

wobei:
* $u \in V$ der aktuelle Knoten ist.
* $\mathcal{V} \subseteq V$ die Menge der Knoten ist, die entlang des aktuellen Pfades besucht wurden (um Zyklen zu vermeiden).
* $\pi \in V^*$ die Folge von Knoten ist, die den aktiven Pfad von $s$ nach $u$ repräsentiert.

Sei $\Sigma = V \times \mathcal{P}(V) \times V^*$ der Zustandsraum, wobei $\mathcal{P}(V)$ die Potenzmenge von $V$ bezeichnet.

### Rekursive Formulierung
Wir definieren die Suchfunktion $f: \Sigma \to \mathcal{P}(V^*)$, die für einen gegebenen Zustand $(u, \mathcal{V}, \pi)$ die Menge aller gültigen einfachen Pfade von $s$ nach $t$ zurückgibt, die den Präfix $\pi$ erweitern.

Die Funktion $f$ ist rekursiv definiert als:

$$f(u, \mathcal{V}, \pi) = \begin{cases}
\{\pi\} & \text{falls } u = t \\
\emptyset & \text{falls } u \neq t \text{ und } \text{Adj}(u) \setminus \mathcal{V} = \emptyset \\
\bigcup_{w \in \text{Adj}(u) \setminus \mathcal{V}} f(w, \mathcal{V} \cup \{w\}, \pi \cdot w) & \text{sonst}
\end{cases}$$

wobei:
* $\text{Adj}(u) = \{ v \in V \mid (u, v) \in E \}$ die Menge der offenen Nachbarn von $u$ ist.
* $\pi \cdot w$ die Konkatenation des Knotens $w$ an die Folge $\pi$ bezeichnet.

Der initiale Aufruf des Algorithmus lautet:

$$\mathcal{P}_{s, t} = f(s, \{s\}, (s))$$

### Backtracking und Zustands-Wiederherstellung
Die algebraische Formulierung von $f$ erfasst auf natürliche Weise den Backtracking-Mechanismus. Der Mengenvereinigungsoperator $\bigcup$ über die unbesuchten Nachbarn $\text{Adj}(u) \setminus \mathcal{V}$ impliziert, dass jeder Zweig unabhängig evaluiert wird.

Wenn die Rekursion von einem Zweig $w$ zurückkehrt, wird die besuchte Menge $\mathcal{V} \cup \{w\}$ verworfen, wodurch der besuchte Kontext für den nächsten Geschwisterzweig in $\text{Adj}(u) \setminus \mathcal{V}$ auf $\mathcal{V}$ zurückgesetzt wird. Dieses mathematische Scoping entspricht direkt dem imperativen Schritt der Zustands-Wiederherstellung:

$$\text{visited}[r][c] = \text{False}$$

---

## 3. Komplexitätsanalyse

### Zeitkomplexität

Um die Zeitkomplexität im Schlechtesten Fall zu bestimmen, analysieren wir die Größe des Zustandsraum-Baums, der durch die rekursive Funktion $f$ generiert wird.

#### Theorem 1
*Die Zeitkomplexität des Rat in a Maze-Algorithmus im Schlechtesten Fall auf einem $N \times N$-Gitter beträgt $O(4^{N^2})$.*

#### Beweis:
Sei $G = (V, E)$ ein vollständiger Gittergraph, bei dem $M(u) = 1$ für alle $u \in \mathcal{C}$ gilt. Somit ist $|V| = N^2$.

1. **Obere Schranke durch einfache Pfade:**
   Der Backtracking-Algorithmus generiert alle selbstvermeidenden Pfade (SAWs), die bei $s$ beginnen. Jeder selbstvermeidende Pfad auf $G$ kann eine maximale Länge von $|V| = N^2$ Knoten haben.
   Am Startknoten $s$ gibt es höchstens 4 mögliche Richtungen für eine Bewegung. Für jeden nachfolgenden Knoten $u$ im Pfad belegt die eingehende Kante eine der 4 Richtungen, was höchstens 3 potenzielle Richtungen für die Exploration lässt:
   
   $$\text{Verzweigungsfaktor } b \le 3$$

   Sei $T(d)$ die Anzahl der Pfade der Länge $d$, die bei $s$ beginnen. Wir können $T(d)$ wie folgt begrenzen:
   
   $$T(d) \le 4 \cdot 3^{d-1} \quad \text{für } d \ge 1$$

   Die Gesamtzahl der besuchten Zustände im Suchbaum mit maximaler Tiefe $D = N^2$ ist durch die Summe der Knoten auf jeder Tiefe begrenzt:
   
   $$\sum_{d=0}^{N^2} T(d) \le 1 + \sum_{d=1}^{N^2} 4 \cdot 3^{d-1} = 1 + 4 \left( \frac{3^{N^2} - 1}{3 - 1} \right) = 2 \cdot 3^{N^2} - 1$$

2. **Asymptotische Komplexität:**
   Da $2 \cdot 3^{N^2} - 1 \in O(3^{N^2})$ und $O(3^{N^2}) \subset O(4^{N^2})$, ist die Zeitkomplexität im Schlechtesten Fall durch $O(4^{N^2})$ begrenzt. Diese lose obere Schranke von $O(4^{N^2})$ wird in der Literatur konventionell zitiert, um den uneingeschränkten 4-Wege-Verzweigungsfaktor an jeder Zelle darzustellen.
   
   Somit ist die Zeitkomplexität im Schlechtesten Fall $\Theta(3^{N^2})$ oder $O(4^{N^2})$. $\blacksquare$

### Platzkomplexität

#### Theorem 2
*Die zusätzliche Platzkomplexität des Algorithmus beträgt $O(N^2)$.*

#### Beweis:
Der vom Algorithmus verbrauchte zusätzliche Speicher besteht aus zwei Hauptkomponenten:
1. **Der Rekursions-Stack:**
   Die maximale Tiefe des Rekursionsbaums ist durch die maximale Länge eines einfachen Pfades in $G$ begrenzt. Da der Graph $|V| = N^2$ Knoten besitzt, kann jeder einfache Pfad höchstens $N^2$ Knoten enthalten. Daher beträgt die maximale Tiefe des Aufruf-Stacks $N^2$, was $O(N^2)$ Speicherplatz erfordert.

2. **Die Zustandsspeicherung:**
   * Die `visited`-Lookup-Tabelle ist eine boolesche Matrix der Größe $N \times N$, die $\Theta(N^2)$ Speicherplatz erfordert.
   * Die aktuelle Pfadfolge $\pi$ speichert höchstens $N^2$ Knoten, was $O(N^2)$ Speicherplatz erfordert.

Summiert man diese Komponenten:

$$\text{Space}_{\text{aux}}(N) = \underbrace{O(N^2)}_{\text{Stack-Tiefe}} + \underbrace{\Theta(N^2)}_{\text{Visited-Matrix}} + \underbrace{O(N^2)}_{\text{Pfadspeicher}} = O(N^2)$$

Wenn wir den Ausgabespeicher einbeziehen, der zum Speichern aller gültigen Pfade erforderlich ist, beträgt die gesamte Platzkomplexität im Schlechtesten Fall $O(N^2 \cdot 3^{N^2})$, da es bis zu $O(3^{N^2})$ Pfade geben kann, von denen jeder eine Länge von $O(N^2)$ hat. $\blacksquare$