# Formale mathematische Spezifikation: Freivalds-Algorithmus (Matrixprodukt-Prüfung)

## 1. Definitionen und Notation

Sei $n \in \mathbb{N}$ die Dimension der quadratischen Matrizen. Gegeben sind drei Matrizen $A, B, C \in \mathbb{F}^{n \times n}$, wobei $\mathbb{F}$ ein Körper ist (typischerweise $\mathbb{R}$ oder ein endlicher Körper $\mathbb{Z}_p$).

Das Ziel ist es, das Prädikat $P: A \cdot B = C$ zu entscheiden.

Wir definieren Folgendes:
*   **Zufallsvektorraum:** Sei $\mathcal{R} = \{0, 1\}^n$ die Menge aller möglichen Spaltenvektoren der Länge $n$ mit Einträgen aus $\{0, 1\}$.
*   **Stichprobenentnahme:** Sei $\mathbf{r} \in \mathcal{R}$ ein Zufallsvektor, der gleichverteilt aus $\mathcal{R}$ gewählt wird, sodass $\mathbb{P}(\mathbf{r} = \mathbf{v}) = 2^{-n}$ für jedes $\mathbf{v} \in \mathcal{R}$ gilt.
*   **Zustandsraum:** Der Algorithmus operiert auf dem Zustandsraum $\mathcal{S} = \mathbb{F}^n$, welcher die Zwischenvektoren repräsentiert, die aus Matrix-Vektor-Produkten resultieren.
*   **Versuchsparameter:** Sei $k \in \mathbb{N}$ die Anzahl der unabhängigen Iterationen, die durchgeführt werden, um das Vertrauen in das Ergebnis zu verstärken.

## 2. Algebraische Charakterisierung

Die Korrektheit des Algorithmus beruht auf der Assoziativität der Matrixmultiplikation und den Eigenschaften der Differenzmatrix $D = A \cdot B - C$.

**Theorem (Korrektheit):**
1. Wenn $A \cdot B = C$, dann gilt für jedes $\mathbf{r} \in \mathcal{R}$ die Gleichung $A(B\mathbf{r}) = C\mathbf{r}$. Dies folgt aus dem Distributivgesetz: $A(B\mathbf{r}) - C\mathbf{r} = (AB - C)\mathbf{r} = \mathbf{0}\mathbf{r} = \mathbf{0}$.
2. Wenn $A \cdot B \neq C$, sei $D = AB - C$. Da $D \neq \mathbf{0}$, existiert mindestens eine Zeile in $D$, die nicht der Nullvektor ist. Das Lemma von Freivalds besagt, dass für einen Vektor $\mathbf{r}$, der gleichverteilt aus $\{0, 1\}^n$ gewählt wird, gilt:
   $$\mathbb{P}(D\mathbf{r} = \mathbf{0} \mid D \neq \mathbf{0}) \leq \frac{1}{2}$$

**Beweisskizze:**
Sei $d_i$ eine von Null verschiedene Zeile von $D$. Die Bedingung $D\mathbf{r} = \mathbf{0}$ impliziert $d_i \cdot \mathbf{r} = 0$. Sei $d_{ij} \neq 0$ ein von Null verschiedener Eintrag in $d_i$. Wir können $r_j$ im Skalarprodukt isolieren:
$$r_j = -\frac{1}{d_{ij}} \left( \sum_{k \neq j} d_{ik} r_k \right)$$
Für jede feste Belegung der anderen $n-1$ Variablen gibt es höchstens einen Wert für $r_j$, der die Gleichung erfüllt. Da $r_j$ aus $\{0, 1\}$ gewählt wird, ist die Wahrscheinlichkeit, dass das gewählte $r_j$ diese Gleichung erfüllt, höchstens $1/2$.

**Fehlerwahrscheinlichkeit:**
Durch $k$-fache Wiederholung des Tests mit unabhängigen Vektoren $\mathbf{r}_1, \dots, \mathbf{r}_k$ ist die Wahrscheinlichkeit eines falsch-positiven Ergebnisses (Ausgabe von `True`, obwohl $A \cdot B \neq C$) wie folgt beschränkt:
$$\mathbb{P}(\text{False Positive}) \leq \left( \frac{1}{2} \right)^k = 2^{-k}$$

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus führt $k$ Iterationen durch. In jeder Iteration berechnen wir:
1. $\mathbf{v}_1 = B\mathbf{r}$
2. $\mathbf{v}_2 = A\mathbf{v}_1$
3. $\mathbf{v}_3 = C\mathbf{r}$

Jede Matrix-Vektor-Multiplikation umfasst $n^2$ skalare Multiplikationen und $n(n-1)$ Additionen. Die Komplexität eines Matrix-Vektor-Produkts beträgt $\Theta(n^2)$.
Die gesamte Zeitkomplexität $T(n, k)$ ergibt sich zu:
$$T(n, k) = \sum_{i=1}^{k} \Theta(n^2) = \Theta(k \cdot n^2)$$
Da $k$ im Verhältnis zu $n$ eine Konstante ist, erreicht der Algorithmus eine Zeitkomplexität von $O(n^2)$, was deutlich effizienter ist als die für eine explizite Matrixmultiplikation erforderlichen $O(n^3)$.

### Platzkomplexität
Der Algorithmus benötigt Speicherplatz für die Eingabematrizen ($O(n^2)$) sowie zusätzlichen Speicher für die Vektoren $\mathbf{r}, \mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3$. Jeder Vektor benötigt $O(n)$ Speicherplatz.
Die zusätzliche Platzkomplexität beträgt:
$$S(n) = O(n)$$
Somit ist der Algorithmus sehr speichereffizient und benötigt neben dem Speicher für die Eingabedaten nur linearen zusätzlichen Speicherplatz.