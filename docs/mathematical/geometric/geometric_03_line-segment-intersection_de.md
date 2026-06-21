# Formale mathematische Spezifikation: Schnittpunkt von Liniensegmenten

## 1. Definitionen und Notation

Sei die euklidische Ebene definiert als $\mathbb{R}^2$. Ein Liniensegment $S$ ist definiert durch ein geordnetes Paar distinkter Punkte $(P_i, P_j) \in (\mathbb{Z}^2)^2$. Wir betrachten zwei Segmente:
$S_1 = (\mathbf{p}_1, \mathbf{p}_2)$ und $S_2 = (\mathbf{p}_3, \mathbf{p}_4)$, wobei $\mathbf{p}_k = (x_k, y_k)$.

Wir definieren die Orientierungsfunktion $\text{orient}: (\mathbb{Z}^2)^3 \to \{-1, 0, 1\}$ als das Vorzeichen der Determinante der Matrix, die die Vektoren $\vec{AB}$ und $\vec{AC}$ repräsentiert:
$$\text{orient}(\mathbf{a}, \mathbf{b}, \mathbf{c}) = \text{sgn}\left( (x_b - x_a)(y_c - y_a) - (y_b - y_a)(x_c - x_a) \right)$$
wobei $\text{sgn}(z)$ die Signum-Funktion ist:
$$\text{sgn}(z) = \begin{cases} 1 & \text{falls } z > 0 \\ -1 & \text{falls } z < 0 \\ 0 & \text{falls } z = 0 \end{cases}$$

Das Schnittpunkt-Prädikat $\mathcal{I}(S_1, S_2)$ ist eine boolesche Funktion, die $(\mathbb{Z}^2)^4 \to \{ \text{True, False} \}$ abbildet.

## 2. Algebraische Charakterisierung

Der Schnittpunkt zweier Segmente $S_1$ und $S_2$ ist definiert durch die Existenz eines Punktes $\mathbf{p}$, sodass $\mathbf{p} \in S_1 \cap S_2$. Geometrisch tritt dies genau dann ein, wenn die Endpunkte eines Segments auf gegenüberliegenden Seiten der Geraden liegen, die das andere Segment enthält, oder wenn die Segmente kollinear sind und sich überlappen.

Seien $o_1 = \text{orient}(\mathbf{p}_1, \mathbf{p}_2, \mathbf{p}_3)$, $o_2 = \text{orient}(\mathbf{p}_1, \mathbf{p}_2, \mathbf{p}_4)$, $o_3 = \text{orient}(\mathbf{p}_3, \mathbf{p}_4, \mathbf{p}_1)$ und $o_4 = \text{orient}(\mathbf{p}_3, \mathbf{p}_4, \mathbf{p}_2)$.

Die Segmente schneiden sich genau dann, wenn:
1. **Allgemeiner Fall:** Die Segmente überspannen einander:
   $$(o_1 \cdot o_2 < 0) \land (o_3 \cdot o_4 < 0)$$
2. **Kollinearer/Tangentialer Fall:** Ein Endpunkt liegt auf dem anderen Segment:
   $$\exists k \in \{1, 2, 3, 4\} \text{ sodass } o_i = 0 \text{ und } \mathbf{p}_k \in \text{BoundingBox}(S_j)$$
   wobei $\text{BoundingBox}((A, B)) = \{ (x, y) \in \mathbb{R}^2 \mid \min(x_A, x_B) \le x \le \max(x_A, x_B) \land \min(y_A, y_B) \le y \le \max(y_A, y_B) \}$.

Formal gibt der Algorithmus $\text{True}$ zurück, wenn:
$$\mathcal{I}(S_1, S_2) \iff ((o_1 \cdot o_2 < 0) \land (o_3 \cdot o_4 < 0)) \lor \bigvee_{i=1}^4 \text{is\_on\_segment}(S_i)$$
wobei $\text{is\_on\_segment}$ die Kollinearitäts- und Bounding-Box-Bedingung für jeden Endpunkt auswertet.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus besteht aus einer festen Sequenz arithmetischer Operationen:
1. **Orientierungsberechnungen:** Vier Aufrufe der Funktion `orient`. Jeder Aufruf umfasst 2 Subtraktionen, 2 Multiplikationen und 1 Subtraktion, was insgesamt $O(1)$ arithmetische Operationen ergibt.
2. **Vergleich und Logik:** Eine konstante Anzahl an Vergleichen ($<, =, \le$) sowie logischen Konjunktionen/Disjunktionen.
3. **Bounding-Box-Prüfungen:** Bis zu vier Prüfungen, von denen jede 4 Vergleiche und 2 logische Konjunktionen umfasst, insgesamt $O(1)$.

Da die Anzahl der Operationen $N_{ops}$ unabhängig von den Koordinatenwerten ist (unter der Annahme von Integer-Arithmetik mit fester Breite) und die Anzahl der Segmente auf zwei festgelegt ist, beträgt die gesamte Zeitkomplexität:
$$T(n) = \Theta(1)$$

### Platzkomplexität
Der Algorithmus benötigt Speicherplatz für vier Koordinatenpaare $(\mathbf{p}_1, \dots, \mathbf{p}_4)$ und vier Orientierungsskalare $(o_1, \dots, o_4)$.
- Eingabespeicher: $O(1)$ (feste Größe).
- Hilfsspeicher: $O(1)$ (eine konstante Anzahl an Integer-Variablen).

Somit beträgt die gesamte Platzkomplexität:
$$S(n) = \Theta(1)$$