# Formale mathematische Spezifikation: Springerproblem (Knight's Tour)

## 1. Definitionen und Notation

Um das Springerproblem zu formalisieren, modellieren wir das Schachbrett und die erlaubten Züge eines Springers mithilfe der Graphentheorie und mengentheoretischer Formulierungen.

### 1.1 Das Brett und der Koordinatenraum
Sei $N \in \mathbb{N}$ die Dimension des quadratischen Schachbretts. Wir definieren den Koordinatenraum (oder die Knotenmenge) $V_N$ als das kartesische Produkt der Koordinatenintervalle:
$$V_N = \{0, 1, \dots, N-1\} \times \{0, 1, \dots, N-1\}$$
Die Kardinalität der Knotenmenge beträgt $|V_N| = N^2$. Ein einzelnes Feld auf dem Brett wird als Tupel $u = (r, c) \in V_N$ dargestellt, wobei $r$ den Zeilenindex und $c$ den Spaltenindex bezeichnet.

### 1.2 Die Springerzug-Relation
Die Menge der erlaubten Züge für einen Springer ist durch eine algebraische Relation $R \subset V_N \times V_N$ definiert. Zwei Felder $u = (r_1, c_1)$ und $v = (r_2, c_2)$ stehen in der Relation $R$ genau dann, wenn ihre Koordinatendifferenzen einem „L-förmigen“ Sprung entsprechen:
$$(u, v) \in R \iff \left( |r_1 - r_2| = 1 \land |c_1 - c_2| = 2 \right) \lor \left( |r_1 - r_2| = 2 \land |c_1 - c_2| = 1 \right)$$
Da $R$ symmetrisch ist, können wir den Springer-Graphen als ungerichteten, ungewichteten Graphen $\mathcal{G}_N = (V_N, E_N)$ definieren, wobei die Kantenmenge $E_N$ gegeben ist durch:
$$E_N = \left\{ \{u, v\} \subseteq V_N \mid (u, v) \in R \right\}$$

### 1.3 Die Nachbarschafts- und Gradfunktionen
Für jeden Knoten $v \in V_N$ ist die offene Nachbarschaft $N(v)$ die Menge der Knoten, die in $\mathcal{G}_N$ zu $v$ benachbart sind:
$$N(v) = \{ u \in V_N \mid \{v, u\} \in E_N \}$$
Der Grad eines Knotens $v$ ist definiert als $d(v) = |N(v)|$. Für jede Teilmenge von Knoten $U \subseteq V_N$ definieren wir die eingeschränkte Nachbarschaft von $v$ bezüglich $U$ als:
$$N_U(v) = N(v) \cap U$$
Der eingeschränkte Grad ist dann $d_U(v) = |N_U(v)|$.

### 1.4 Mathematische Formulierung der Tour
Eine **Springer-Tour** (Knight's Tour) ist ein Hamiltonpfad im Springer-Graphen $\mathcal{G}_N$. Formal ist dies eine Folge von Knoten $P = (v_0, v_1, \dots, v_{N^2-1})$, die folgende Bedingungen erfüllt:
1. **Vollständigkeit und Eindeutigkeit (Bijektivität):** Die Abbildung $i \mapsto v_i$ ist eine Bijektion von $\{0, 1, \dots, N^2-1\}$ auf $V_N$.
2. **Adjazenz:** Für alle $i \in \{0, 1, \dots, N^2-2\}$ gilt $\{v_i, v_{i+1}\} \in E_N$.
3. **Anfangsbedingung:** $v_0 = (0, 0)$.

Die Ausgabe des Algorithmus wird als Matrix $M \in (\{-1\} \cup \{0, 1, \dots, N^2-1\})^{N \times N}$ dargestellt, definiert durch:
$$M[r][c] = \begin{cases} 
i & \text{falls } v_i = (r, c) \text{ für ein } i \in \{0, \dots, N^2-1\} \\
-1 & \text{falls keine solche Folge } P \text{ existiert}
\end{cases}$$

---

## 2. Algebraische Charakterisierung und Zustandsraumsuche

Der Backtracking-Algorithmus durchsucht systematisch den Zustandsraum einfacher Pfade in $\mathcal{G}_N$ beginnend bei $v_0$.

### 2.1 Zustandsraumrepräsentation
Sei $\mathcal{S}$ die Menge der gültigen Teilzustände. Ein Zustand $s \in \mathcal{S}$ bei Schritt $k$ (wobei $1 \le k \le N^2$) wird durch das Tupel dargestellt:
$$s = (P_k, U_k)$$
wobei:
* $P_k = (v_0, v_1, \dots, v_{k-1})$ eine Folge von $k$ verschiedenen Knoten ist, die den bisher durchlaufenen Pfad repräsentiert, mit $v_0 = (0, 0)$.
* $U_k = V_N \setminus \{v_0, \dots, v_{k-1}\}$ die Menge der noch nicht besuchten Knoten ist, mit $|U_k| = N^2 - k$.

### 2.2 Zustandsübergang und Backtracking
Sei $\tau: \mathcal{S} \to \mathcal{P}(\mathcal{S})$ die Übergangsrelation, die einen Zustand auf seine potenziellen Nachfolgezustände abbildet. Für einen Zustand $s = (P_k, U_k)$ mit $P_k = (v_0, \dots, v_{k-1})$ gilt:
$$\tau((P_k, U_k)) = \left\{ (P_{k+1}, U_{k+1}) \;\middle|\; v_{k} \in N(v_{k-1}) \cap U_k \right\}$$
wobei:
* $P_{k+1} = P_k \mathbin{\Vert} (v_k)$ (wobei $\mathbin{\Vert}$ die Konkatenation von Folgen bezeichnet).
* $U_{k+1} = U_k \setminus \{v_k\}$.

Die Suche endet erfolgreich, wenn ein Zustand erreicht wird, in dem $k = N^2$, was bedeutet, dass $U_k = \emptyset$ ist. Wenn $\tau((P_k, U_k)) = \emptyset$ und $k < N^2$, führt der Algorithmus ein Backtracking durch, indem er den Zustand auf $s' = (P_{k-1}, U_{k-1})$ zurücksetzt und alternative Übergänge versucht.

### 2.3 Warnsdorff-Heuristik
Um die Suche zu optimieren, erzwingt die Warnsdorff-Heuristik eine totale Vorordnung auf den infrage kommenden Nachfolgeknoten. Für einen Zustand $s = (P_k, U_k)$ mit aktuellem Knoten $v_{k-1}$ ist die Menge der möglichen nächsten Schritte:
$$C(s) = N_{U_k}(v_{k-1})$$
Für jeden Kandidaten $w \in C(s)$ berechnen wir seinen weiterführenden Grad innerhalb des Teilgraphen der unbesuchten Knoten:
$$\text{deg}_{U_k \setminus \{w\}}(w) = \left| N(w) \cap \left( U_k \setminus \{w\} \right) \right|$$
Die Warnsdorff-Heuristik besagt, dass Kandidaten in nicht-absteigender Reihenfolge ihrer weiterführenden Grade priorisiert werden sollten. Wir definieren die Ordnungsrelation $\le_W$ auf $C(s)$ als:
$$w_1 \le_W w_2 \iff \text{deg}_{U_k \setminus \{w_1\}}(w_1) \le \text{deg}_{U_k \setminus \{w_2\}}(w_2)$$
Der Backtracking-Algorithmus evaluiert Übergänge zu Nachfolgezuständen $(P_k \mathbin{\Vert} (w), U_k \setminus \{w\})$ sequenziell gemäß dieser sortierten Reihenfolge.

### 2.4 Korrektheit und Invarianten
Die Korrektheit der Backtracking-Suche wird durch die folgenden Schleifen- und Rekursionsinvarianten begründet:

#### Invariante 1 (Pfadgültigkeit)
Bei jeder Rekursionstiefe $k$ ist die Folge $P_k = (v_0, \dots, v_{k-1})$ ein einfacher Pfad in $\mathcal{G}_N$.
$$\forall i, j \in \{0, \dots, k-1\}, \; i \neq j \implies v_i \neq v_j \quad \land \quad \forall i \in \{0, \dots, k-2\}, \; \{v_i, v_{i+1}\} \in E_N$$

#### Invariante 2 (Zustandspartitionierung)
Bei jedem Schritt $k$ bilden die Menge der besuchten Knoten und die Menge der unbesuchten Knoten eine Partition der Knotenmenge $V_N$:
$$\{v_0, \dots, v_{k-1}\} \cup U_k = V_N \quad \text{und} \quad \{v_0, \dots, v_{k-1}\} \cap U_k = \emptyset$$

#### Theorem (Terminierung und Korrektheit)
Der Algorithmus terminiert, da der Zustandsraum $\mathcal{S}$ endlich ist (beschränkt durch $|V_N|!$). Nach der Terminierung liefert er genau dann einen nicht-leeren Pfad $P$ zurück, wenn es eine Folge gibt, die die Kriterien für einen Hamiltonpfad auf $\mathcal{G}_N$ beginnend bei $(0,0)$ erfüllt.

---

## 3. Komplexitätsanalyse

### 3.1 Zeitkomplexität

#### Analyse des schlechtesten Falls (Worst-Case)
Im schlechtesten Fall kann die Heuristik versagen, Sackgassen frühzeitig zu beschneiden, was den Algorithmus dazu zwingt, den gesamten Zustandsraum-Baum zu durchlaufen.

Sei $T(k)$ die maximale Anzahl der besuchten Zustände von Tiefe $k$ bis zum Blatt-Level $N^2$. Bei jedem Schritt hat der Springer höchstens 8 legale Züge. Die Rekursionsgleichung, die die Größe des Suchbaums im schlechtesten Fall bestimmt, lautet:
$$T(k) \le 8 \cdot T(k+1) + \mathcal{O}(1)$$
Mit dem Induktionsanfang $T(N^2) = \mathcal{O}(1)$ ergibt die Lösung dieser Rekursion:
$$T(0) \le \sum_{k=0}^{N^2-1} 8^k = \frac{8^{N^2} - 1}{7} = \mathcal{O}\left(8^{N^2}\right)$$
Somit beträgt die Zeitkomplexität im schlechtesten Fall $\mathcal{O}\left(8^{N^2}\right)$.

#### Analyse des besten Falls (Best-Case)
Im besten Fall identifiziert die Warnsdorff-Heuristik erfolgreich einen gültigen Hamiltonpfad ohne einen einzigen Backtracking-Schritt.

Bei jedem Schritt $k \in \{1, \dots, N^2\}$ führt der Algorithmus folgende Operationen aus:
1. Identifikation benachbarter unbesuchter Knoten: $\mathcal{O}(1)$ (da $|N(v)| \le 8$).
2. Berechnung des weiterführenden Grades für jeden Nachbarn: $\mathcal{O}(1)$ (Evaluierung von höchstens 8 Nachbarn, wobei jeder höchstens 8 Nachbarn hat, was maximal 64 Prüfungen erfordert).
3. Sortieren der Kandidaten: $\mathcal{O}(d \log d)$ wobei $d \le 8$, was $\mathcal{O}(1)$ entspricht.

Da der Algorithmus bei jeder Ebene des Rekursionsbaums der Tiefe $N^2$ direkt in den korrekten Zustand übergeht, ergibt sich der Gesamtaufwand zu:
$$T_{\text{best}}(N) = \sum_{k=1}^{N^2} \mathcal{O}(1) = \mathcal{O}(N^2)$$
Somit beträgt die Zeitkomplexität im besten Fall $\mathcal{O}(N^2)$.

### 3.2 Platzkomplexität

Die Platzkomplexität wird durch die Speicherung des Brettzustands und den Ausführungs-Stack der rekursiven Hilfsfunktion bestimmt.

#### Hilfsspeicher (Auxiliary Space)
1. **Rekursions-Stack:** Die maximale Tiefe des Rekursionsbaums beträgt exakt $N^2$ Frames. Jeder Stack-Frame speichert eine konstante Menge an Informationen: die aktuellen Koordinaten $(r, c)$, die aktuelle Schrittnummer und eine Liste von Kandidaten der Größe maximal 8. Somit beträgt der Stack-Platz:
   $$S_{\text{stack}}(N) = \mathcal{O}(N^2)$$
2. **Zustandsverfolgung:** 
   * Die `visited`-Matrix der Größe $N \times N$ benötigt $\mathcal{O}(N^2)$ Bits.
   * Die `path`-Liste speichert höchstens $N^2$ Koordinatenpaare, was $\mathcal{O}(N^2)$ Platz erfordert.

Kombiniert man diese Komponenten, ergibt sich die Platzkomplexität für den Hilfsspeicher zu:
$$\text{Space}_{\text{aux}}(N) = S_{\text{stack}}(N) + S_{\text{state}}(N) = \mathcal{O}(N^2) + \mathcal{O}(N^2) = \mathcal{O}(N^2)$$

#### Gesamte Platzkomplexität
Da die Ausgabematrix $M$ die Größe $N \times N$ hat, beträgt die gesamte Platzkomplexität (einschließlich des Ausgabespeichers):
$$\text{Space}_{\text{total}}(N) = \mathcal{O}(N^2)$$