# Formale mathematische Spezifikation: Erstes nicht-wiederholtes Zeichen in einem Stream

## 1. Definitionen und Notation

Sei $\Sigma$ ein endliches Alphabet (z. B. $\Sigma = \{a, b, \dots, z\}$). Ein Stream wird als eine Sequenz $S = (s_1, s_2, \dots, s_n)$ dargestellt, wobei $s_i \in \Sigma$ gilt.

Wir definieren die folgenden Strukturen, um den Zustand des Streams am Index $k$ zu verwalten:
*   **Frequency Map:** Eine Funktion $f_k: \Sigma \to \mathbb{N}_0$, wobei $f_k(c) = |\{i \in \{1, \dots, k\} : s_i = c\}|$.
*   **Chronological Queue:** Eine geordnete Sequenz $Q_k = (q_1, q_2, \dots, q_m)$, die Elemente $c \in \Sigma$ enthält, für die $f_k(c) = 1$ gilt. Die Elemente in $Q_k$ sind nach ihrem ersten Erscheinen im Stream $S$ sortiert.
*   **Output Function:** Eine Abbildung $O: \{1, \dots, n\} \to \Sigma \cup \{\#\}$, definiert als:
    $$O(k) = \begin{cases} q_1 & \text{falls } Q_k \neq \emptyset \\ \# & \text{falls } Q_k = \emptyset \end{cases}$$

## 2. Algebraische Charakterisierung

Der Zustandsübergang von $k-1$ nach $k$ beinhaltet das Eintreffen des Zeichens $s_k$. Die Aktualisierungsregeln sind wie folgt definiert:

1.  **Frequency Update:**
    $$f_k(c) = f_{k-1}(c) + \delta_{c, s_k}$$
    wobei $\delta_{i,j}$ das Kronecker-Delta ist.

2.  **Queue Evolution:**
    Sei $Q'_k$ die intermediäre Queue nach dem Anhängen von $s_k$, falls $f_k(s_k) = 1$:
    $$Q'_k = \begin{cases} Q_{k-1} \cdot (s_k) & \text{falls } f_k(s_k) = 1 \\ Q_{k-1} & \text{falls } f_k(s_k) > 1 \end{cases}$$
    
    Die finale Queue $Q_k$ wird erhalten, indem alle Elemente vom Anfang von $Q'_k$ entfernt werden, die nicht mehr eindeutig sind:
    $$Q_k = \text{dropwhile}(c \in Q'_k \mid f_k(c) > 1)$$
    Formal ausgedrückt: $Q_k = (q_j, q_{j+1}, \dots, q_m)$, wobei $j$ der kleinste Index ist, für den $f_k(q_j) = 1$ gilt. Existiert kein solches $j$, so ist $Q_k = \emptyset$.

**Schleifeninvariante:** Zu jedem Schritt $k$ enthält die Queue $Q_k$ exakt die Menge der Zeichen $\{c \in \Sigma : f_k(c) = 1\}$, sortiert nach ihrem ersten Auftretensindex $i = \min \{t : s_t = c\}$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Sei $T(n)$ die gesamte Zeitkomplexität für einen Stream der Länge $n$. Der Algorithmus führt $n$ Iterationen durch. In jeder Iteration $k$:
1.  Die Aktualisierung von $f_k$ benötigt $O(1)$ Zeit.
2.  Das Anhängen an die Queue benötigt $O(1)$ Zeit.
3.  Die `while`-Schleife entfernt Elemente vom Anfang der Queue.

Um die amortisierten Kosten abzuleiten, verwenden wir die Aggregationsmethode. Jedes Zeichen $s_i$ wird höchstens einmal zur Queue hinzugefügt (wenn $f_i(s_i)=1$) und höchstens einmal aus der Queue entfernt (wenn $f_k(s_i) > 1$). Sei $N_{push}$ die Gesamtzahl der `push`-Operationen und $N_{pop}$ die Gesamtzahl der `pop`-Operationen.
$$\sum_{k=1}^n (\text{Kosten der Iteration } k) = \sum_{k=1}^n (O(1) + \text{Kosten der pops}_k)$$
Da $N_{push} = n$ und $N_{pop} \leq n$ gilt, beträgt die Gesamtlaufzeit $O(n)$. Somit ist die amortisierte Zeitkomplexität pro Zeichen:
$$\frac{O(n)}{n} = O(1)$$

### Platzkomplexität
Die Platzkomplexität wird durch die Speicherung der Frequency Map und der Queue bestimmt.
*   **Frequency Map:** Speichert höchstens $|\Sigma|$ Einträge.
*   **Queue:** Speichert höchstens $|\Sigma|$ Einträge, da sie nur eindeutige Zeichen enthält.

Da $|\Sigma|$ eine Konstante ist (z. B. 256 für erweitertes ASCII), ist die zusätzliche Platzkomplexität:
$$S(n) = O(|\Sigma|) = O(1)$$
Die gesamte Platzkomplexität, einschließlich der Eingabe- und Ausgabespeicherung, beträgt $O(n)$. Der für den Zustand des Algorithmus erforderliche zusätzliche Speicherplatz ist jedoch strikt durch die Größe des Alphabets begrenzt und unabhängig von der Stream-Länge $n$.