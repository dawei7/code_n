# Formale mathematische Spezifikation: Longest Consecutive Sequence

## 1. Definitionen und Notation

Sei $A = \{a_1, a_2, \dots, a_n\}$ eine Multimenge von Ganzzahlen, wobei $n = |A|$. Wir definieren den Diskursbereich als $\mathbb{Z}$.

*   **Eingabe:** Eine ungeordnete Sequenz (oder Multimenge) $A \subset \mathbb{Z}$.
*   **Hash Set:** Sei $S = \{x \mid x \in A\}$ die Menge der eindeutigen Elemente in $A$. Die Konstruktion von $S$ bildet $A$ auf seine charakteristische Mengenrepräsentation ab.
*   **Konsekutive Sequenz:** Eine Teilmenge $C \subseteq S$ ist eine konsekutive Sequenz, wenn es ein $k \in \mathbb{Z}$ und ein $m \in \mathbb{N}$ gibt, sodass $C = \{k, k+1, \dots, k+m-1\}$.
*   **Ziel:** Bestimmung der maximalen Kardinalität einer solchen Teilmenge $C$, die eine Teilmenge von $S$ ist. Formal suchen wir:
    $$\mathcal{L} = \max \{ |C| : C \subseteq S \land \exists k \in \mathbb{Z}, \forall i \in \{0, \dots, |C|-1\}, (k+i) \in S \}$$

## 2. Algebraische Charakterisierung

Um eine Effizienz von $O(N)$ zu gewährleisten, definieren wir ein Prädikat $\text{is\_starter}(x)$ für jedes $x \in S$:
$$\text{is\_starter}(x) \iff (x - 1) \notin S$$

Dieses Prädikat partitioniert $S$ in disjunkte Mengen von Sequenzen. Wenn für ein $x \in S$ das Prädikat $\text{is\_starter}(x)$ wahr ist, dann ist $x$ das eindeutige minimale Element einer maximalen konsekutiven Sequenz $C_x \subseteq S$. Wir definieren die bei $x$ beginnende Sequenz als:
$$C_x = \{x + i \mid i \in \mathbb{N}_0, x+i \in S, \forall j < i, x+j \in S\}$$

Die Länge der bei $x$ beginnenden Sequenz ist durch die Funktion $f(x) = |C_x|$ gegeben. Das globale Maximum ist:
$$\mathcal{L} = \max_{x \in S, \text{is\_starter}(x)} f(x)$$

**Schleifeninvariante:**
Sei $S_i$ die Menge der Elemente, die nach $i$ Iterationen der äußeren Schleife verarbeitet wurden. Sei $L_i$ die maximale Länge, die unter allen Sequenzen gefunden wurde, die mit einem $x \in S_i$ beginnen. Bei jedem Schritt $i$ erhält der Algorithmus Folgendes aufrecht:
$$L_i = \max \{ f(x) : x \in S_i \land \text{is\_starter}(x) \}$$
Der Algorithmus terminiert, wenn $S_i = S$, was $L_n = \mathcal{L}$ ergibt.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus besteht aus zwei Phasen:
1.  **Set-Konstruktion:** Die Abbildung von $A$ auf $S$ erfordert $n$ Einfügungen in eine Hash Table. Unter der Annahme einer gleichmäßigen Hash-Funktion ist jede Einfügung im Durchschnitt $O(1)$. Gesamte Zeit: $O(n)$.
2.  **Sequenz-Durchlauf:** Wir iterieren durch jedes $x \in S$. Die innere `while`-Schleife wird nur ausgeführt, wenn $\text{is\_starter}(x)$ wahr ist. 
    Sei $T$ die Gesamtzahl der Operationen. Wir können $T$ wie folgt ausdrücken:
    $$T = \sum_{x \in S} \mathbb{I}(\text{is\_starter}(x)) \cdot |C_x| + O(n)$$
    wobei $\mathbb{I}$ die Indikatorfunktion ist. Da jedes Element $y \in S$ zu genau einer maximalen konsekutiven Sequenz $C_x$ gehört, ist die Summe der Längen aller disjunkten Sequenzen genau $|S| \leq n$:
    $$\sum_{x \in S, \text{is\_starter}(x)} |C_x| = |S| \leq n$$
    Somit ist die gesamte Zeitkomplexität $O(n) + O(n) = O(n)$.

### Platzkomplexität
Der Algorithmus erfordert die Speicherung der Menge $S$. Im Schlechtesten Fall, in dem alle Elemente in $A$ verschieden sind, gilt $|S| = n$.
*   **Zusätzlicher Speicher:** Das Hash Set $S$ speichert $n$ Ganzzahlen.
*   **Gesamtspeicher:** $O(n)$ zur Aufrechterhaltung der Menge $S$ und $O(1)$ für Hilfsvariablen (`best`, `cur`).
Die Platzkomplexität beträgt strikt $O(n)$.