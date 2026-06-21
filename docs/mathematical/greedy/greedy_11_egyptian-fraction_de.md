# Formale mathematische Spezifikation: Ägyptischer Bruch

## 1. Definitionen und Notation

Sei die Eingabe eine rationale Zahl $r \in \mathbb{Q}$ mit $0 < r < 1$. Wir repräsentieren $r$ als ein Paar teilerfremder positiver ganzer Zahlen $(n, d) \in \mathbb{Z}^+ \times \mathbb{Z}^+$, wobei $r = \frac{n}{d}$ und $\gcd(n, d) = 1$ gilt.

*   **Zustandsraum ($\mathcal{S}$):** Der Zustand zu einer beliebigen Iteration $k$ ist definiert durch das Tupel $(n_k, d_k) \in \mathbb{Z}^+ \times \mathbb{Z}^+$.
*   **Stammbruch:** Ein Bruch der Form $\frac{1}{x}$, wobei $x \in \mathbb{Z}^+$.
*   **Ausgabemenge ($\mathcal{D}$):** Eine endliche Folge von Nennern $X = \{x_1, x_2, \dots, x_m\}$, sodass:
    $$\frac{n}{d} = \sum_{i=1}^{m} \frac{1}{x_i}$$
    wobei $x_i \in \mathbb{Z}^+$ und $x_i < x_{i+1}$ für alle $1 \le i < m$ gilt.

## 2. Algebraische Charakterisierung

Der Algorithmus verwendet eine Greedy-Strategie, die auf der Fibonacci-Sylvester-Entwicklung basiert. Gegeben den aktuellen Zustand $(n_k, d_k)$, definieren wir den nächsten Nenner $x_k$ als die kleinste ganze Zahl, für die $\frac{1}{x_k} \le \frac{n_k}{d_k}$ gilt.

**Die Greedy-Wahl:**
$$x_k = \left\lceil \frac{d_k}{n_k} \right\rceil$$

**Rekurrenz:**
Der Übergang vom Zustand $(n_k, d_k)$ zu $(n_{k+1}, d_{k+1})$ ist definiert durch:
$$\frac{n_{k+1}}{d_{k+1}} = \frac{n_k}{d_k} - \frac{1}{x_k} = \frac{n_k x_k - d_k}{d_k x_k}$$

Um die kanonische Darstellung beizubehalten, definieren wir den nächsten Zustand durch Kürzen des Bruchs:
$$g_k = \gcd(n_k x_k - d_k, d_k x_k)$$
$$n_{k+1} = \frac{n_k x_k - d_k}{g_k}, \quad d_{k+1} = \frac{d_k x_k}{g_k}$$

**Schleifeninvariante:**
In jedem Schritt $k$ erfüllt der Rest $r_k = \frac{n_k}{d_k}$ die Bedingung $0 \le r_k < 1$. Der Algorithmus terminiert im Schritt $m$, wenn $n_m = 0$ ist. Die strikte Abnahme des Zählers $n_{k+1} < n_k$ (für $n_k > 1$) stellt die Terminierung sicher. Da $x_k \ge \frac{d_k}{n_k}$ gilt, folgt insbesondere $n_k x_k - d_k < n_k x_k - (n_k x_k - n_k) = n_k$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität wird durch die Anzahl der Iterationen $m$ und die Kosten der arithmetischen Operationen pro Iteration bestimmt.

1.  **Anzahl der Iterationen ($m$):** Für einen gegebenen Bruch $\frac{n}{d}$ ist die Anzahl der Terme $m$ beschränkt. Während der Schlechteste Fall für allgemeine Eingaben groß sein kann, ist für den Greedy-Algorithmus bekannt, dass $m = O(n)$ im Schlechtesten Fall gilt. Für die meisten Eingaben nimmt die Folge der Zähler jedoch schnell ab, was zu einem Durchschnittlichen Fall von $O(\log d)$ führt.
2.  **Kosten pro Iteration:** Jede Iteration erfordert:
    *   Berechnung von $x_k = \lceil d/n \rceil$: $O(1)$ arithmetische Operationen.
    *   GCD-Berechnung: Unter Verwendung des euklidischen Algorithmus benötigt $\gcd(n_k x_k - d_k, d_k x_k)$ eine Zeit von $O(\log(\min(n_k, d_k)))$.
    *   Multiplikation und Division: $O(\log^2(\max(n_k, d_k)))$ bei Verwendung von Standardalgorithmen oder $O(\log(\max(n_k, d_k)))$ unter Annahme von Operationen auf Wortgröße.

Somit ergibt sich eine gesamte Zeitkomplexität von $O(m \cdot \log(\text{bits}))$, was sich im Schlechtesten Fall zu $O(n \log d)$ vereinfacht, beziehungsweise $O(\log d)$ unter günstigen Bedingungen.

### Platzkomplexität
*   **Hilfsplatzbedarf:** Der Algorithmus verwaltet eine konstante Anzahl an Variablen $(n, d, x, g)$, um den aktuellen Zustand zu verfolgen. Daher ist die Platzkomplexität für den Hilfsplatz $O(1)$.
*   **Gesamtplatzbedarf:** Unter Einbeziehung der Ausgabefolge der Länge $m$ beträgt die Platzkomplexität $O(m)$, wobei $m$ die Anzahl der generierten Stammbrüche ist. Aufgrund der Greedy-Wahl ist $m$ typischerweise klein, im Schlechtesten Fall jedoch $O(n)$.