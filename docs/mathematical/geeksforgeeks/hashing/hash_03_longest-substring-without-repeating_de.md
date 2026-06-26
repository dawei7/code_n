# Formale mathematische Spezifikation: Längster Substring ohne wiederholte Zeichen

## 1. Definitionen und Notation

Sei $\Sigma$ ein endliches Alphabet (z. B. ASCII oder Unicode). Ein String $s$ der Länge $n$ ist definiert als eine Sequenz von Zeichen $s = (s_0, s_1, \dots, s_{n-1})$, wobei $s_i \in \Sigma$.

*   **Substring:** Ein Substring $s[i..j]$ ist eine zusammenhängende Teilsequenz von $s$, die am Index $i$ beginnt und am Index $j$ endet, wobei $0 \le i \le j < n$. Die Länge des Substrings beträgt $L = j - i + 1$.
*   **Eigenschaft der Eindeutigkeit:** Ein Substring $s[i..j]$ ist genau dann als *eindeutig* definiert, wenn die Abbildung $f: \{i, i+1, \dots, j\} \to \Sigma$, definiert durch $f(k) = s_k$, injektiv ist. Das bedeutet: $\forall p, q \in \{i, \dots, j\}, p \neq q \implies s_p \neq s_q$.
*   **Zielsetzung:** Wir suchen den Wert $\mathcal{L} = \max \{ j - i + 1 \mid 0 \le i \le j < n \text{ und } s[i..j] \text{ ist eindeutig} \}$.
*   **Zustandsraum:** Sei $\mathcal{M}: \Sigma \to \mathbb{Z} \cup \{-\infty\}$ eine Hash Map (oder partielle Funktion), wobei $\mathcal{M}(c)$ den letzten Index $k$ speichert, für den $s_k = c$ gilt. Sei $L \in \{0, \dots, n-1\}$ die linke Grenze des Sliding Window.

## 2. Algebraische Charakterisierung

Der Algorithmus verwaltet ein Sliding Window $[L, R]$, sodass der Substring $s[L..R]$ stets eindeutig ist. Wir definieren den Zustandsübergang bei jedem Schritt $R \in \{0, \dots, n-1\}$ wie folgt:

1.  **Update-Regel für $L$:**
    Wenn das Zeichen $s_R$ betrachtet wird und bereits zuvor am Index $k = \mathcal{M}(s_R)$ aufgetreten ist, muss das Fenster verkleinert werden, um die Eigenschaft der Eindeutigkeit zu wahren. Die neue linke Grenze $L_{R}$ ist definiert durch:
    $$L_R = \max(L_{R-1}, \mathcal{M}(s_R) + 1)$$
    wobei $L_{-1} = 0$. Falls $s_R \notin \text{domain}(\mathcal{M})$, setzen wir $\mathcal{M}(s_R) = -1$.

2.  **Update-Regel für $\mathcal{M}$:**
    Nach der Verarbeitung von $s_R$ wird die Map aktualisiert:
    $$\mathcal{M}_{R}(c) = \begin{cases} R & \text{if } c = s_R \\ \mathcal{M}_{R-1}(c) & \text{otherwise} \end{cases}$$

3.  **Schleifeninvariante:**
    Am Ende jeder Iteration $R$ gilt die folgende Invariante:
    $$\forall x, y \in \{L_R, \dots, R\}, x \neq y \implies s_x \neq s_y$$
    Die maximale Länge $\mathcal{L}$ wird aktualisiert als:
    $$\mathcal{L}_R = \max(\mathcal{L}_{R-1}, R - L_R + 1)$$

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus iteriert genau einmal durch den String $s$, wobei $R$ von $0$ bis $n-1$ läuft.
*   In jeder Iteration werden folgende Operationen durchgeführt:
    1.  Ein Hash Map Lookup: $\mathcal{M}(s_R)$, was im Durchschnitt $O(1)$ entspricht.
    2.  Ein Vergleich und eine Zuweisung: $O(1)$.
    3.  Ein Map-Update: $\mathcal{M}[s_R] \leftarrow R$, was im Durchschnitt $O(1)$ entspricht.
*   Die gesamte Zeitkomplexität ist die Summe der Arbeit über $n$ Schritte:
    $$T(n) = \sum_{R=0}^{n-1} O(1) = O(n)$$
Somit ist der Algorithmus linear in Bezug auf die Eingabelänge $n$.

### Platzkomplexität
Die Platzkomplexität wird durch den Speicherbedarf der Hash Map $\mathcal{M}$ bestimmt.
*   Die Map $\mathcal{M}$ speichert höchstens einen Eintrag für jedes eindeutige Zeichen, das im String $s$ vorkommt.
*   Sei $\sigma = |\Sigma|$ die Größe des Alphabets. Die Anzahl der Einträge in $\mathcal{M}$ ist durch $\min(n, \sigma)$ beschränkt.
*   Daher beträgt die zusätzliche Platzkomplexität $O(\min(n, \sigma))$. Im Kontext fester Alphabete (z. B. ASCII, wobei $\sigma = 128$) ist dies effektiv $O(1)$. Im allgemeinen Fall ist sie $O(\sigma)$.