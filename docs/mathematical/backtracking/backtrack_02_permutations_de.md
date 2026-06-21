# Formale mathematische Spezifikation: Permutationen

## 1. Definitionen und Notation

Sei $\mathcal{U}$ ein total geordnetes Universum von Elementen. Wir definieren den Input für den Algorithmus als eine Sequenz (oder ein Array) $A$ der Länge $n \in \mathbb{N}_0$, dargestellt als $n$-Tupel:

$$A = (a_1, a_2, \dots, a_n) \in \mathcal{U}^n$$

wobei die Elemente paarweise verschieden sind, d. h.

$$\forall i, j \in \{1, \dots, n\}, \quad i \neq j \implies a_i \neq a_j$$

Sei $S_A = \{a_1, a_2, \dots, a_n\}$ die zugrunde liegende Menge der Elemente in $A$, wobei $|S_A| = n$ gilt.

### 1.1 Permutationen
Eine **Permutation** der Sequenz $A$ ist eine Bijektion $\sigma: \{1, \dots, n\} \to S_A$. Äquivalent dazu repräsentieren wir eine Permutation als ein $n$-Tupel $P = (p_1, p_2, \dots, p_n) \in S_A^n$, sodass gilt:

$$\forall i, j \in \{1, \dots, n\}, \quad i \neq j \implies p_i \neq p_j$$

Die Menge aller möglichen Permutationen von $A$ wird mit $\mathcal{P}(A)$ bezeichnet. Die Kardinalität dieser Menge ergibt sich aus der Fakultät der Sequenzlänge:

$$|\mathcal{P}(A)| = n!$$

### 1.2 Zustandsraum der Backtracking-Suche
Der Backtracking-Algorithmus exploriert systematisch den Raum der partiellen Permutationen. Wir definieren den **Zustandsraum** $\mathcal{X}$ als die Menge aller Präfixe von Permutationen von $A$:

$$\mathcal{X} = \bigcup_{k=0}^{n} \left\{ (p_1, \dots, p_k) \in S_A^k \;\middle|\; \forall i, j \in \{1, \dots, k\}, \, i \neq j \implies p_i \neq p_j \right\}$$

Für jeden Zustand $x = (p_1, \dots, p_k) \in \mathcal{X}$ definieren wir:
*   Die **Länge** des Zustands: $|x| = k$.
*   Den **leeren Zustand** (Wurzel des Suchraums): $\epsilon = ()$ wobei $|\epsilon| = 0$.
*   Die **terminalen Zustände** (Blätter des Suchraums): $\mathcal{T} = \{ x \in \mathcal{X} \mid |x| = n \}$. Beachten Sie, dass $\mathcal{T} = \mathcal{P}(A)$ gilt.

---

## 2. Algebraische Charakterisierung

Der Backtracking-Algorithmus kann formal als eine Tiefensuche (Depth-First Search, DFS) über einen gerichteten Zustandsübergangsbaum $T = (\mathcal{X}, E)$ modelliert werden.

### 2.1 Übergangsrelation und Suchbaum
Die Menge der gerichteten Kanten $E \subset \mathcal{X} \times \mathcal{X}$ definiert die gültigen Übergänge von einer partiellen Permutation der Länge $k$ zu einer partiellen Permutation der Länge $k+1$:

$$E = \left\{ (u, v) \;\middle|\; u = (p_1, \dots, p_k), \, v = (p_1, \dots, p_k, a_i) \text{ für ein } a_i \in S_A \setminus \{p_1, \dots, p_k\} \right\}$$

Für jeden Zustand $u \in \mathcal{X} \setminus \mathcal{T}$ ist die Menge seiner Kinder (unmittelbare Nachfolger) definiert durch:

$$\text{children}(u) = \left\{ u \cdot a_i \;\middle|\; a_i \in S_A \setminus \text{set}(u) \right\}$$

wobei $\cdot$ den Konkatenationsoperator bezeichnet und $\text{set}(u)$ die Menge der Elemente ist, die im Tupel $u$ vorkommen.

### 2.2 Zustandsrepräsentation und Invarianten
In jedem Schritt der Rekursion verwaltet der Algorithmus ein globales Zustandstupel $(P, U)$, wobei:
1.  $P \in \mathcal{X}$ die aktive Pfadsequenz ist, die die aktuelle partielle Permutation repräsentiert.
2.  $U \in \{0, 1\}^n$ ein boolescher Tracking-Vektor (das `used` Array) der Größe $n$ ist.

Der Algorithmus bewahrt die folgenden **Repräsentationsinvarianten** beim Eintritt in und beim Verlassen von jedem rekursiven Aufruf:

$$\forall i \in \{1, \dots, n\}, \quad U_i = 1 \iff a_i \in \text{set}(P)$$

$$\forall i, j \in \{1, \dots, |P|\}, \quad i \neq j \implies P_i \neq P_j$$

### 2.3 Rekursive Formulierung des Generators
Sei $f: \mathcal{X} \to \mathcal{P}(\mathcal{P}(A))$ eine mengenwertige Funktion, die einen partiellen Zustand $P$ auf die Menge aller vollständigen Permutationen abbildet, die von $P$ aus erreichbar sind. Wir definieren $f$ induktiv:

$$f(P) = \begin{cases} 
\{ P \} & \text{falls } |P| = n \\
\bigcup_{i \in \{1, \dots, n\}: U_i = 0} f(P \cdot a_i) & \text{falls } |P| < n
\end{cases}$$

Das primäre Ziel des Algorithmus ist die Berechnung von $f(\epsilon)$, was die vollständige Menge der Permutationen ergibt:

$$f(\epsilon) = \mathcal{P}(A)$$

Die Korrektheit des Backtracking-Algorithmus folgt direkt aus dieser induktiven Definition, da der Suchbaum endlich und azyklisch ist und jeder terminale Knoten genau einmal besucht wird.

---

## 3. Komplexitätsanalyse

### 3.1 Zeitkomplexität

Um die Zeitkomplexität abzuleiten, analysieren wir die Gesamtzahl der besuchten Knoten im Zustandsübergangsbaum $T$ und den Rechenaufwand an jedem Knoten.

#### 3.1.1 Knotenzahl des Suchbaums
Der Suchbaum $T$ ist in Ebenen $k \in \{0, 1, \dots, n\}$ strukturiert, wobei Ebene $k$ alle partiellen Permutationen der Länge $k$ enthält. Die Anzahl der Knoten auf Ebene $k$, bezeichnet als $N_k$, ist die Anzahl der $k$-Permutationen von $n$ Elementen:

$$N_k = P(n, k) = \frac{n!}{(n-k)!}$$

Die Gesamtzahl der Knoten im Baum, $N_{\text{total}}$, ist die Summe über alle Ebenen:

$$N_{\text{total}} = \sum_{k=0}^{n} N_k = \sum_{k=0}^{n} \frac{n!}{(n-k)!} = n! \sum_{j=0}^{n} \frac{1}{j!}$$

Unter Verwendung der Taylor-Reihenentwicklung der Exponentialfunktion $e^x = \sum_{j=0}^{\infty} \frac{x^j}{j!}$ schätzen wir die Summe ab:

$$e - 1 < \sum_{j=0}^{n} \frac{1}{j!} < e \quad (\text{für } n \ge 1)$$

Somit ist die Gesamtzahl der Knoten im Suchbaum strikt beschränkt:

$$n! \le N_{\text{total}} < e \cdot n!$$

Dies belegt, dass die Gesamtzahl der besuchten Zustände $\Theta(n!)$ beträgt.

#### 3.1.2 Aufwand pro Knoten
Wir unterteilen den vom Algorithmus geleisteten Aufwand in zwei Kategorien:
1.  **Innere Knoten ($|P| < n$):** An jedem inneren Knoten der Ebene $k$ führt der Algorithmus eine Schleife der Größe $n$ aus. Innerhalb jeder Iteration führt er $O(1)$ Operationen aus: Überprüfung des booleschen Arrays $U$, Aktualisierung von $U$, Anhängen an $P$, Rekursion und Backtracking (pop von $P$ und Zurücksetzen von $U$). Somit ist der lokale Aufwand an jedem inneren Knoten $\Theta(n)$.
2.  **Blattknoten ($|P| = n$):** An jedem Blattknoten wird der Basisfall ausgelöst. Der Algorithmus kopiert den aktuellen Pfad $P$ der Länge $n$ in die globale Ergebnisliste. Diese Kopieroperation erfordert $\Theta(n)$ Operationen.

#### 3.1.3 Ableitung der gesamten Zeitkomplexität
Sei $W(n)$ der gesamte Rechenaufwand:

$$W(n) = \sum_{k=0}^{n-1} \left( N_k \cdot \Theta(n) \right) + N_n \cdot \Theta(n)$$

$$W(n) = \Theta(n) \sum_{k=0}^{n} \frac{n!}{(n-k)!} = \Theta(n) \cdot \Theta(n!) = \Theta(n \cdot n!)$$

Somit ergibt sich die gesamte Zeitkomplexität zu:

$$T(n) = \Theta(n \cdot n!)$$

---

### 3.2 Platzkomplexität

Wir analysieren die Platzkomplexität, indem wir sie in Hilfsspeicher (Arbeitsspeicher) und Gesamtspeicher (einschließlich Ausgabespeicher) unterteilen.

#### 3.2.1 Hilfsspeicher
Der Hilfsspeicher besteht aus dem Speicher, der auf dem Call Stack belegt wird, sowie den Zustandsvariablen:
1.  **Rekursionstiefe:** Die maximale Tiefe des Rekursionsbaums beträgt $n + 1$ (entsprechend dem Pfad von der Wurzel $\epsilon$ zu einem Blatt der Länge $n$). Jeder Stack-Frame speichert eine konstante Anzahl an Referenzen und primitiven Variablen. Somit beträgt der Platzbedarf des Call Stacks $O(n)$.
2.  **Zustandsvariablen:** 
    *   Das Pfad-Array $P$ speichert höchstens $n$ Elemente: $O(n)$ Speicherplatz.
    *   Das boolesche Tracking-Array $U$ speichert genau $n$ Elemente: $O(n)$ Speicherplatz.

Zusammengefasst ergibt sich die Hilfsplatzkomplexität zu:

$$S_{\text{aux}}(n) = O(n)$$

#### 3.2.2 Gesamtspeicher
Wenn der Speicherplatz für die finale Ausgabe einbezogen wird, muss der Algorithmus $n!$ Permutationen speichern, wobei jede Permutation ein Array der Größe $n$ ist. Der Speicherbedarf für die Ausgabe beträgt:

$$S_{\text{out}}(n) = \Theta(n \cdot n!)$$

Daher ist die gesamte Platzkomplexität, einschließlich der Repräsentation der Ausgabe:

$$S_{\text{total}}(n) = \Theta(n \cdot n!)$$