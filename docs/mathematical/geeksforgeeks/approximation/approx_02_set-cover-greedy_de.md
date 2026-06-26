# Formale mathematische Spezifikation: Set Cover (Greedy-Approximation)

## 1. Definitionen und Notation

Sei die Probleminstanz durch ein Tupel $(U, \mathcal{S})$ definiert, wobei:
*   $U = \{u_1, u_2, \dots, u_n\}$ eine endliche Menge von Elementen ist, genannt **Universum**, mit der Kardinalität $|U| = n \in \mathbb{N}^+$.
*   $\mathcal{S} = \{S_1, S_2, \dots, S_m\}$ eine Familie nicht-leerer Teilmengen von $U$ ist, wobei $m = |\mathcal{S}| \in \mathbb{N}^+$, sodass $\bigcup_{i=1}^m S_i = U$ gilt.
*   $I = \{1, 2, \dots, m\}$ die Indexmenge der Familie $\mathcal{S}$ ist.

### Definition 1.1: Set Cover
Eine Teilmenge von Indizes $J \subseteq I$ ist ein **Set Cover** von $U$ genau dann, wenn:
$$\bigcup_{j \in J} S_j = U$$

### Definition 1.2: Optimales Set Cover
Das Optimierungsziel ist es, ein Set Cover $J^*$ mit minimaler Kardinalität zu finden. Wir definieren die optimale Indexmenge $J^*$ als:
$$J^* \in \arg\min_{J \subseteq I} \left\{ |J| \;\middle|\; \bigcup_{j \in J} S_j = U \right\}$$
Wir bezeichnen die Größe des optimalen Covers als $OPT = |J^*|$.

### Definition 1.3: Zustandsraum
Der Zustand des Greedy-Algorithmus zu einem beliebigen Schritt $t \in \mathbb{N}$ wird durch das Tupel $(U_t, J_t) \in \mathcal{P}(U) \times \mathcal{P}(I)$ repräsentiert, wobei:
*   $U_t \subseteq U$ die Menge der Elemente ist, die zum Zeitpunkt $t$ noch **nicht abgedeckt** sind.
*   $J_t \subseteq I$ die Menge der Indizes der Teilmengen ist, die bis zum Schritt $t$ **ausgewählt** wurden.

Der Anfangszustand ist definiert als:
$$(U_0, J_0) = (U, \emptyset)$$

Der Algorithmus terminiert zum Schritt $T$, wenn der Endzustand $(U_T, J_T)$ die Bedingung $U_T = \emptyset$ erfüllt.

---

## 2. Algebraische Charakterisierung

### 2.1 Die Greedy-Wahlfunktion
In jedem Schritt $t \ge 0$ wählt der Algorithmus einen Index $j_{t+1} \in I \setminus J_t$, der die Anzahl der neu abgedeckten Elemente maximiert. Sei $f: I \times \mathcal{P}(U) \to \mathbb{N}$ die Abdeckungsfunktion, definiert durch:
$$f(j, U_t) = |S_j \cap U_t|$$

Die Greedy-Wahl im Schritt $t+1$ ist gegeben durch:
$$j_{t+1} = \arg\max_{j \in I \setminus J_t} f(j, U_t)$$

Um Determinismus zu gewährleisten, setzen wir eine totale Ordnung auf $I$ voraus, sodass Gleichstände durch die Wahl des lexikographisch kleinsten Index aufgelöst werden:
$$j_{t+1} = \min \left( \arg\max_{j \in I \setminus J_t} f(j, U_t) \right)$$

### 2.2 Zustandsübergangsrelationen
Die Zustandsübergänge vom Schritt $t$ zu $t+1$ werden durch die folgenden Rekursionsgleichungen bestimmt:
$$J_{t+1} = J_t \cup \{j_{t+1}\}$$
$$U_{t+1} = U_t \setminus S_{j_{t+1}}$$

### 2.3 Schleifeninvarianten
Für jeden Schritt $t \in \{0, 1, \dots, T\}$ gelten die folgenden Invarianten:
1.  **Fortschritt des Set Covers:** $U_t = U \setminus \left( \bigcup_{j \in J_t} S_j \right)$.
2.  **Monotonie der Kardinalität:** $|J_t| = t$.
3.  **Terminierungsgarantie:** $U_t = \emptyset \iff t = T$. Da $U$ endlich ist und $\bigcup_{i=1}^m S_i = U$ gilt, ist die Folge der nicht abgedeckten Mengen streng geschachtelt: $U_0 \supset U_1 \supset \dots \supset U_T = \emptyset$, was $T \le n$ sicherstellt.

### 2.4 Mathematischer Beweis des Approximationsverhältnisses
Sei $H_d = \sum_{i=1}^d \frac{1}{i}$ die $d$-te harmonische Zahl. Wir beweisen, dass der Greedy-Algorithmus ein Approximationsverhältnis von $H_g$ erreicht, wobei $g = \max_{j \in I} |S_j|$.

**Theorem:** Sei $J_T$ das vom Greedy-Algorithmus zurückgegebene Cover und $J^*$ ein optimales Cover. Dann gilt:
$$|J_T| \le H_g \cdot |J^*| \le H_n \cdot |J^*|$$

*Beweis:*
Wir verwenden die Formulierung der Preis-Methode (Dual Fitting). Wir weisen dem Algorithmus für jede ausgewählte Menge Gesamtkosten von $1$ zu. Wenn die Menge $S_{j_{t+1}}$ im Schritt $t+1$ ausgewählt wird, verteilen wir ihre Einheitskosten gleichmäßig auf die neu abgedeckten Elemente. Für jedes Element $x \in U$ bezeichne $c_x$ die Kosten, die $x$ zugewiesen wurden. Wenn $x \in S_{j_{t+1}} \cap U_t$, dann gilt:
$$c_x = \frac{1}{|S_{j_{t+1}} \cap U_t|}$$

Da die Elemente die Kosten jeder ausgewählten Menge partitionieren, sind die Gesamtkosten des Greedy-Covers:
$$\sum_{x \in U} c_x = \sum_{t=0}^{T-1} \sum_{x \in S_{j_{t+1}} \cap U_t} c_x = \sum_{t=0}^{T-1} 1 = T = |J_T|$$

Betrachten wir nun eine beliebige Menge $S \in \mathcal{S}$ (einschließlich derer im optimalen Cover $J^*$). Seien die Elemente von $S$ in der Reihenfolge geordnet, in der sie vom Greedy-Algorithmus abgedeckt werden: $x_1, x_2, \dots, x_k$, wobei $k = |S| \le g$.

Wenn das Element $x_i$ abgedeckt wird (etwa im Schritt $t+1$), müssen die Elemente $\{x_i, x_{i+1}, \dots, x_k\}$ noch nicht abgedeckt sein. Somit gilt $|S \cap U_t| \ge k - i + 1$. Aufgrund der Definition der Greedy-Wahl muss die ausgewählte Menge $S_{j_{t+1}}$ erfüllen:
$$|S_{j_{t+1}} \cap U_t| \ge |S \cap U_t| \ge k - i + 1$$

Folglich sind die Kosten, die $x_i$ zugewiesen werden, beschränkt durch:
$$c_{x_i} = \frac{1}{|S_{j_{t+1}} \cap U_t|} \le \frac{1}{k - i + 1}$$

Summieren wir die Kosten über alle Elemente in $S$:
$$\sum_{x \in S} c_x = \sum_{i=1}^k c_{x_i} \le \sum_{i=1}^k \frac{1}{k - i + 1} = \sum_{p=1}^k \frac{1}{p} = H_k \le H_g$$

Da $J^*$ ein gültiges Cover von $U$ ist, können wir schreiben:
$$|J_T| = \sum_{x \in U} c_x \le \sum_{S \in \mathcal{S}_{J^*}} \sum_{x \in S} c_x \le \sum_{S \in \mathcal{S}_{J^*}} H_{|S|} \le |J^*| \cdot H_g$$
wobei $\mathcal{S}_{J^*} = \{S_j \mid j \in J^*\}$. Dies schließt den Beweis ab. $\blacksquare$

---

## 3. Komplexitätsanalyse

Sei $N = |U|$ die Größe des Universums und $S = |\mathcal{S}|$ die Anzahl der Teilmengen. Sei $L = \sum_{i=1}^S |S_i|$ die Gesamtgröße der Eingaberepräsentation.

### 3.1 Zeitkomplexität

#### Naive Implementierung (wie im Python-Code angegeben)
In der angegebenen Implementierung führt der Algorithmus folgende Operationen aus:
1.  **Initialisierung:** Das Erstellen der `uncovered`-Menge benötigt $\Theta(N)$ Zeit.
2.  **Äußere Schleife:** Läuft höchstens $T \le N$ Mal.
3.  **Innere Schleife:** In jeder Iteration der äußeren Schleife iteriert der Algorithmus über alle $S$ Teilmengen. Für jede Teilmenge $S_i$ berechnet er die Schnittmengengröße mit der `uncovered`-Menge:
    $$\text{Arbeit pro Teilmenge } S_i = \sum_{x \in S_i} O(1) = O(|S_i|)$$
    Summiert über alle Teilmengen ist die Arbeit in einer Iteration der äußeren Schleife:
    $$\sum_{i=1}^S O(|S_i|) = O(L)$$
4.  **Zustandsaktualisierung:** Das Entfernen der Elemente der gewählten Menge $S_{j^*}$ aus `uncovered` benötigt $O(|S_{j^*}|) = O(N)$ Zeit.

Daher ist die gesamte Zeitkomplexität im Schlechtesten Fall der naiven Implementierung:
$$\mathcal{T}_{\text{naive}}(N, S) = O(N) + \sum_{t=1}^T \left( O(L) + O(|S_{j_t}|) \right) = O(T \cdot L) = O(N \cdot L)$$

Da $L \le S \cdot N$, ist die Zeitkomplexität im Schlechtesten Fall:
$$\mathcal{T}_{\text{naive}}(N, S) = O(S \cdot N^2)$$

#### Optimale $O(S \cdot N)$-Implementierung
Die Zeitkomplexität kann auf $O(L)$ (was im Schlechtesten Fall $O(S \cdot N)$ entspricht) optimiert werden, indem redundante Schnittmengenberechnungen vermieden werden:
1.  **Konstruktion eines invertierten Index:** Erstellen einer Abbildung von jedem Element $x \in U$ auf die Liste der Teilmengenindizes, die $x$ enthalten. Dies benötigt $O(L)$ Zeit.
2.  **Aktive Nachverfolgung:** Ein Array `count` der Größe $S$ führen, wobei `count[i]` den Wert $|S_i \cap U_t|$ speichert.
3.  **Bucket Queue:** Die Teilmengen in einem Array von Buckets speichern, indiziert durch ihre aktuelle Abdeckungsanzahl (da die Anzahlen Ganzzahlen in $[0, N]$ sind). Dies ermöglicht den Zugriff auf die Teilmenge mit der maximalen Anzahl in $O(1)$.
4.  **Aktualisierungen:** Wenn eine Teilmenge $S_{j^*}$ ausgewählt wird, finden wir für jedes Element $x \in S_{j^*} \cap U_t$ alle Teilmengen $S_i$, die $x$ enthalten, unter Verwendung des invertierten Index, dekrementieren deren Zähler und aktualisieren ihre Positionen in der Bucket Queue. Jedes Element wird auf diese Weise höchstens einmal verarbeitet, wenn es von "nicht abgedeckt" zu "abgedeckt" wechselt.

Die Gesamtarbeit für Aktualisierungen über die gesamte Ausführung ist beschränkt durch:
$$\sum_{x \in U} \sum_{i : x \in S_i} O(1) = O(L)$$

Daher ist die optimierte Zeitkomplexität:
$$\mathcal{T}_{\text{optimal}}(N, S) = \Theta(S + N + L) = O(S \cdot N)$$

### 3.2 Platzkomplexität

#### Zusätzlicher Speicherplatz
Der zusätzliche Speicherplatz ist der für die Zustandsverfolgung reservierte Speicher, exklusive der Eingaberepräsentation:
*   `uncovered`-Menge: Speichert höchstens $N$ Elemente, was $O(N)$ Speicherplatz erfordert.
*   `chosen`-Liste: Speichert höchstens $S$ Indizes, was $O(S)$ Speicherplatz erfordert.
*   Temporäre Variablen für die Schleifenausführung: $O(1)$ Speicherplatz.

Daher ist die zusätzliche Platzkomplexität:
$$\mathcal{S}_{\text{aux}}(N, S) = O(N + S)$$

#### Gesamtspeicherplatz
Die gesamte Platzkomplexität beinhaltet die Eingaberepräsentation $\mathcal{S}$ und das Universum $U$:
$$\mathcal{S}_{\text{total}}(N, S) = O\left( N + \sum_{i=1}^S |S_i| \right) = O(N + L)$$

Im Schlechtesten Fall, in dem jede Teilmenge einen konstanten Anteil des Universums enthält, gilt $L = \Theta(S \cdot N)$, was ergibt:
$$\mathcal{S}_{\text{total}}(N, S) = O(S \cdot N)$$