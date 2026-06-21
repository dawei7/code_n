# Formale mathematische Spezifikation: BFS Grid

## 1. Definitionen und Notation

Sei das Gitter als eine endliche Menge von Zellen $G = \{ (r, c) \in \mathbb{Z}^2 \mid 0 \le r < H, 0 \le c < W \}$ definiert. 
Wir definieren eine charakteristische Funktion $\chi: G \to \{0, 1\}$, wobei $\chi(r, c) = 0$ eine **passierbare** Zelle und $\chi(r, c) = 1$ eine **blockierte** Zelle bezeichnet.

Das Gitter induziert einen ungerichteten Graphen $\mathcal{G} = (V, E)$, wobei:
*   **Knoten:** $V = \{ v \in G \mid \chi(v) = 0 \}$.
*   **Kanten:** $E = \{ \{u, v\} \subseteq V \mid \|u - v\|_1 = 1 \}$, wobei $\|\cdot\|_1$ die Manhattan-Distanz ist. Dies definiert die 4-Konnektivität des Gitters.

**Eingabe:** Ein Tupel $(G, \chi, s, t)$ mit $s, t \in V$.
**Ausgabe:** Ein Wert $d \in \mathbb{N}_0 \cup \{-1\}$, der die kürzeste Pfadlänge $\delta(s, t)$ in $\mathcal{G}$ repräsentiert, oder $-1$, falls $t$ von $s$ aus nicht erreichbar ist.

## 2. Algebraische Charakterisierung

Der Algorithmus berechnet die kürzeste Pfaddistanz $\delta(s, t)$ unter Verwendung der Eigenschaft, dass BFS den Graphen in Schichten durchsucht. Sei $L_k$ die Menge der Knoten mit Distanz $k$ vom Startknoten $s$:
*   $L_0 = \{s\}$
*   $L_{k+1} = \{ v \in V \setminus \bigcup_{i=0}^k L_i \mid \exists u \in L_k, \{u, v\} \in E \}$

Die Distanzfunktion $\delta(s, v)$ ist als das kleinste $k$ definiert, für das $v \in L_k$ gilt. Der Algorithmus verwaltet eine Queue $Q$ und eine Menge besuchter Knoten $M \subseteq V$. 

**Schleifeninvariante:** Zu Beginn jeder Iteration der `while`-Schleife gilt für jeden Knoten $v$, der aus der Queue entfernt (`pop`) wurde:
1.  Falls $v$ erreicht wurde, ist $\delta(s, v)$ korrekt aufgezeichnet.
2.  Die Menge $M$ enthält exakt die Knoten $v$, für die $\delta(s, v) \le k$ gilt, wobei $k$ die aktuell verarbeitete Distanzschicht ist.

Die Übergangsfunktion für den Zustand $(u, d)$ ist durch den Nachbarschaftsoperator $N(u) = \{ v \in V \mid \{u, v\} \in E \}$ definiert. Der Algorithmus durchsucht den Zustandsraum durch Anwendung des Operators:
$$ \text{Next}(u, d) = \{ (v, d+1) \mid v \in N(u) \land v \notin M \} $$
Der Algorithmus terminiert beim kleinsten $d$, für das $t \in L_d$ gilt, was die Optimalitätsbedingung erfüllt:
$$ \delta(s, t) = \min \{ k \mid t \in L_k \} $$

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität beträgt $O(|V| + |E|)$. 
*   Jeder Knoten $v \in V$ wird höchstens einmal zur Queue hinzugefügt (`push`) und höchstens einmal entfernt (`pop`).
*   Für jeden Knoten $v$ untersuchen wir seine Nachbarn $N(v)$. Da das Gitter 4-konnektiv ist, gilt $|N(v)| \le 4$.
*   Der Gesamtaufwand ist proportional zu $\sum_{v \in V} \text{deg}(v) = 2|E|$.
*   Da $|V| = W \times H$ und $|E| \le 4|V|$ gilt, beträgt die Komplexität $O(W \cdot H)$. Im Kontext eines $n \times n$ Gitters entspricht dies $O(n^2)$.

### Platzkomplexität
Die Platzkomplexität beträgt $O(|V|)$.
*   **Besuchte Knoten (Visited Set):** Die Menge $M$ speichert höchstens $|V|$ Knoten, was $O(W \cdot H)$ Speicherplatz erfordert.
*   **Queue:** Im schlechtesten Fall (z. B. ein Gitter ohne Hindernisse) kann die Queue $Q$ eine Front enthalten, die proportional zum Umfang der Suche ist; dies ist $O(\sqrt{|V|})$ für ein Gitter, aber in der ungünstigsten Graphentopologie ist sie durch $O(|V|)$ beschränkt.
*   **Gesamt:** Der zusätzliche Speicherbedarf beträgt $O(W \cdot H)$, was für ein $n \times n$ Gitter $O(n^2)$ entspricht.