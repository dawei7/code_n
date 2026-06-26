# Formale mathematische Spezifikation: Implementierung einer Queue mittels Stacks

## 1. Definitionen und Notation

Sei $\Sigma$ die Menge aller möglichen Elemente, die in der Queue gespeichert werden können. Wir definieren den Zustand des Systems als ein Paar von Stacks, $S = (S_{in}, S_{out})$, wobei jeder Stack eine geordnete Sequenz von Elementen aus $\Sigma$ darstellt.

*   **Stack-Definition:** Ein Stack $S$ ist eine endliche Sequenz $(s_1, s_2, \dots, s_k)$, wobei $s_k$ das oberste Element ist. Wir definieren die Operationen:
    *   $\text{push}(S, x) = (s_1, \dots, s_k, x)$
    *   $\text{pop}(S) = (s_1, \dots, s_{k-1})$ mit Rückgabewert $s_k$
    *   $\text{peek}(S) = s_k$
    *   $\text{empty}(S) \iff |S| = 0$

*   **Queue-Zustand:** Die logische Queue $Q$ wird durch die Konkatenation der Elemente in $S_{in}$ und der Umkehrung von $S_{out}$ repräsentiert. Speziell gilt: Wenn $S_{in} = (i_1, i_2, \dots, i_n)$ und $S_{out} = (o_1, o_2, \dots, o_m)$, dann ist die logische Queue:
    $$Q = (o_m, o_{m-1}, \dots, o_1, i_1, i_2, \dots, i_n)$$

*   **Operationen:**
    *   $\text{Push}(x)$: $S_{in} \leftarrow \text{push}(S_{in}, x)$
    *   $\text{Pop}()$: Wenn $S_{out}$ leer ist, $S_{out} \leftarrow \text{reverse}(S_{in})$ und $S_{in} \leftarrow \emptyset$. Danach wird $\text{pop}(S_{out})$ zurückgegeben.

## 2. Algebraische Charakterisierung

Die Korrektheit der Implementierung beruht auf der Invariante, dass die logische Queue $Q$ über alle Operationen hinweg erhalten bleibt.

**Invariante:** Zu jedem Zeitpunkt $t$ ist die Sequenz der Elemente in der Queue durch die Abbildung $\mathcal{M}: (S_{in}, S_{out}) \to Q$ gegeben, definiert als:
$$\mathcal{M}(S_{in}, S_{out}) = \text{reverse}(S_{out}) \cdot S_{in}$$
wobei $\cdot$ die Konkatenation von Sequenzen bezeichnet.

**Übergangsregeln:**
1.  **Push:** Für ein Element $x \in \Sigma$ erfüllt der neue Zustand $(S'_{in}, S'_{out})$:
    $$\mathcal{M}(S'_{in}, S'_{out}) = \text{reverse}(S_{out}) \cdot (S_{in} \cdot x) = \mathcal{M}(S_{in}, S_{out}) \cdot x$$
    Dies bestätigt die FIFO-Eigenschaft für das Einfügen.

2.  **Pop/Peek:** Sei $Q = (q_1, q_2, \dots, q_k)$.
    *   Wenn $S_{out} \neq \emptyset$, dann ist $q_1 = \text{peek}(S_{out})$.
    *   Wenn $S_{out} = \emptyset$, dann ist $S_{in} = (q_k, q_{k-1}, \dots, q_1)$. Nach dem Transfer $S_{out} = \text{reverse}(S_{in}) = (q_1, q_2, \dots, q_k)$ ist das oberste Element von $S_{out}$ gleich $q_1$.
    In beiden Fällen ruft die Operation den Kopf der logischen Queue $q_1$ ab und aktualisiert den Zustand zu $Q' = (q_2, \dots, q_k)$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Wir verwenden die **Aggregatmethode** für die amortisierte Analyse. Sei $n$ die Gesamtzahl der Operationen.

*   **Push:** Jede `push`-Operation beinhaltet genau einen `push` auf $S_{in}$, was $O(1)$ entspricht.
*   **Pop/Peek:** Eine `pop`-Operation benötigt $O(1)$, falls $S_{out} \neq \emptyset$. Falls $S_{out} = \emptyset$, benötigt sie $O(k)$, wobei $k = |S_{in}|$.
*   **Amortisierte Kosten:** Jedes Element $x$ wird genau einmal auf $S_{in}$ gepusht, höchstens einmal von $S_{in}$ nach $S_{out}$ verschoben und höchstens einmal von $S_{out}$ gepoppt.
    Sei $c_i$ die Kosten der $i$-ten Operation. Die Gesamtkosten $T(n)$ betragen:
    $$T(n) = \sum_{i=1}^n c_i \leq n + 2n = 3n$$
    Die amortisierten Kosten pro Operation betragen $\frac{T(n)}{n} = O(1)$.

### Platzkomplexität
Die Platzkomplexität wird durch die Speicherung von $N$ Elementen über zwei Stacks bestimmt.
*   **Gesamtspeicher:** Da jedes Element $x$ zu jedem Zeitpunkt in genau einem der beiden Stacks $S_{in}$ oder $S_{out}$ existiert, ist der Gesamtspeicher:
    $$|S_{in}| + |S_{out}| = N$$
*   **Zusätzlicher Speicher:** Der Algorithmus benötigt $O(N)$ Speicherplatz, um die Elemente zu verwalten, was für eine Queue der Größe $N$ optimal ist.