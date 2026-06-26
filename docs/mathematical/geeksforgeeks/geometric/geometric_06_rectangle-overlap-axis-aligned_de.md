# Formale mathematische Spezifikation: Rechteck-Überlappung (achsparallel)

## 1. Definitionen und Notation

Sei $\mathcal{R}$ die Menge aller achsparallelen Rechtecke in der euklidischen Ebene $\mathbb{R}^2$. Ein Rechteck $R \in \mathcal{R}$ ist eindeutig definiert durch seine untere linke Koordinate $(x_1, y_1)$ und seine obere rechte Koordinate $(x_2, y_2)$, wobei $x_1 < x_2$ und $y_1 < y_2$ gilt. Wir bezeichnen ein Rechteck als geordnetes Tupel:
$$R = \langle x_1, y_1, x_2, y_2 \rangle \in \mathbb{R}^4 \mid x_1 < x_2, y_1 < y_2$$

Das Innere eines Rechtecks $R$, bezeichnet als $\text{int}(R)$, ist die offene Menge:
$$\text{int}(R) = \{ (x, y) \in \mathbb{R}^2 \mid x_1 < x < x_2 \land y_1 < y < y_2 \}$$

Das Problem besteht darin, die Existenz einer nicht-leeren Schnittmenge zwischen den Inneren zweier Rechtecke $R_A$ und $R_B$ zu bestimmen. Wir definieren das Überlappungsprädikat $\Phi: \mathcal{R} \times \mathcal{R} \to \{0, 1\}$ als:
$$\Phi(R_A, R_B) = \begin{cases} 1 & \text{falls } \text{int}(R_A) \cap \text{int}(R_B) \neq \emptyset \\ 0 & \text{sonst} \end{cases}$$

## 2. Algebraische Charakterisierung

Um $\Phi(R_A, R_B)$ zu charakterisieren, nutzen wir die Eigenschaft, dass der Schnitt zweier achsparalleler Rechtecke selbst ein achsparalleles Rechteck (oder leer) ist. Die Schnittmenge $\mathcal{I} = \text{int}(R_A) \cap \text{int}(R_B)$ ist genau dann nicht leer, wenn die Projektionen der Rechtecke auf die $x$-Achse und die $y$-Achse beide nicht-leere Schnittmengen aufweisen.

Seien $I_x(R) = (x_1, x_2)$ und $I_y(R) = (y_1, y_2)$ die offenen Intervalle, die die Projektionen von $R$ auf die Koordinatenachsen darstellen. Der Schnitt zweier offener Intervalle $(a, b)$ und $(c, d)$ ist genau dann nicht leer, wenn $\max(a, c) < \min(b, d)$ gilt.

Somit gilt $\Phi(R_A, R_B) = 1$ genau dann, wenn:
$$\max(x_{A,1}, x_{B,1}) < \min(x_{A,2}, x_{B,2}) \quad \land \quad \max(y_{A,1}, y_{B,1}) < \min(y_{A,2}, y_{B,2})$$

Durch Anwendung der De Morganschen Gesetze auf die Negation der Überlappungsbedingung definieren wir die Nicht-Überlappungsbedingung $\neg \Phi(R_A, R_B)$. Die Rechtecke sind disjunkt, wenn eine der folgenden Bedingungen erfüllt ist:
1. $R_A$ liegt links von $R_B$: $x_{A,2} \leq x_{B,1}$
2. $R_A$ liegt rechts von $R_B$: $x_{A,1} \geq x_{B,2}$
3. $R_A$ liegt unterhalb von $R_B$: $y_{A,2} \leq y_{B,1}$
4. $R_A$ liegt oberhalb von $R_B$: $y_{A,1} \geq y_{B,2}$

Formal gilt: $\Phi(R_A, R_B) = 1 \iff \neg (x_{A,2} \leq x_{B,1} \lor x_{A,1} \geq x_{B,2} \lor y_{A,2} \leq y_{B,1} \lor y_{A,1} \geq y_{B,2})$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus wertet einen booleschen Ausdruck aus, der aus einer festen Anzahl arithmetischer Vergleiche besteht. Sei $n$ die Anzahl der Rechtecke (hier $n=2$). Der Rechenaufwand $W$ ist definiert durch die Anzahl der primitiven Operationen:
$$W = \sum_{i=1}^{k} c_i$$
wobei $k=8$ (die Anzahl der Vergleiche in der Disjunktion) und $c_i$ die konstante Zeit ist, die für einen Gleitkomma- oder Ganzzahlvergleich benötigt wird. Da $k$ unabhängig von den Eingabewerten und der Anzahl der Rechtecke ist, beträgt die Zeitkomplexität:
$$T(n) \in O(1)$$

### Platzkomplexität
Der Algorithmus benötigt eine konstante Menge an zusätzlichem Speicher, um die Eingabekoordinaten und das boolesche Ergebnis der Vergleiche zu speichern. Es werden keine dynamischen Datenstrukturen oder rekursiven Aufrufe verwendet. Sei $S$ der benötigte Speicherplatz:
$$S = \text{const} \implies S \in O(1)$$
Die Platzkomplexität ist daher $O(1)$, da der Speicherbedarf nicht mit der Größe der Koordinaten oder der Eingabegröße skaliert.