# Formale mathematische Spezifikation: Jump Game (I und II)

## 1. Definitionen und Notation

Sei $A = [a_0, a_1, \dots, a_{n-1}]$ ein Array aus nicht-negativen Ganzzahlen, wobei $n \in \mathbb{Z}^+$. Jeder Index $i \in \{0, 1, \dots, n-1\}$ repräsentiert eine Position in einem diskreten Zustandsraum $\mathcal{S} = \{0, 1, \dots, n-1\}$.

Für jede Position $i$ ist die Menge der in einem einzigen Sprung erreichbaren Positionen durch folgende Menge definiert:
$$\mathcal{R}(i) = \{j \in \mathcal{S} \mid i < j \le i + a_i\}$$

**Jump Game I (Entscheidungsproblem):** Definiere ein Erreichbarkeitsprädikat $P(k)$, welches wahr ist, wenn eine Sequenz von Indizes $(i_0, i_1, \dots, i_m)$ existiert, sodass $i_0 = 0$, $i_m = k$ und $i_{t+1} \in \mathcal{R}(i_t)$ für alle $0 \le t < m$ gilt. Das Problem verlangt die Bestimmung des Wahrheitswertes von $P(n-1)$.

**Jump Game II (Optimierungsproblem):** Sei $\mathcal{P}$ die Menge aller gültigen Sequenzen $(i_0, i_1, \dots, i_m)$, sodass $i_0 = 0$ und $i_m = n-1$. Wir suchen den Wert:
$$\min \{m \mid (i_0, \dots, i_m) \in \mathcal{P}\}$$

## 2. Algebraische Charakterisierung

### Jump Game I: Erreichbarkeitsinvariante
Definiere $M_k$ als den maximal erreichbaren Index nach Betrachtung aller Elemente bis zum Index $k$:
$$M_k = \max_{0 \le i \le k} (i + a_i)$$
Der Algorithmus erhält die Invariante aufrecht, dass bei jedem Schritt $k$, falls $k > M_{k-1}$ gilt, $P(n-1)$ falsch ist, da die Menge der erreichbaren Indizes durch $M_{k-1} < k$ begrenzt ist. Die Bedingung für die Erreichbarkeit lautet:
$$\forall k \in \{0, \dots, n-1\}, k \le M_k \implies P(n-1) \text{ ist wahr, falls } M_{n-1} \ge n-1$$

### Jump Game II: Greedy-Rekurrenz
Sei $J_k$ die minimale Anzahl an Sprüngen, um den Index $k$ zu erreichen. Sei $E_m$ der maximale Index, der mit genau $m$ Sprüngen erreichbar ist. Wir definieren den Zustandsübergang als:
$$E_m = \max_{0 \le i \le E_{m-1}} (i + a_i)$$
wobei $E_0 = 0$. Die minimale Anzahl an Sprüngen $m^*$ ist das kleinste $m$, für das $E_m \ge n-1$ gilt.

Der Algorithmus berechnet dies durch die Verwaltung eines "Fensters" $[L_m, E_m]$, wobei $L_m$ der Beginn des Bereichs ist, der in $m$ Sprüngen erreichbar ist. Die Greedy-Eigenschaft gilt, da für jedes $i \in [L_m, E_m]$ die Wahl von $i$, welche $i + a_i$ maximiert, alle anderen Möglichkeiten im aktuellen Fenster zur Erweiterung der Reichweite auf $E_{m+1}$ strikt dominiert.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus führt einen einzelnen linearen Durchlauf über das Array $A$ aus. An jedem Index $i \in \{0, \dots, n-2\}$ führt der Algorithmus eine konstante Anzahl an Operationen aus: eine Addition, einen Vergleich für die `max`-Funktion und eine bedingte Prüfung.

Die Gesamtarbeit $W(n)$ ergibt sich aus der Summe:
$$W(n) = \sum_{i=0}^{n-2} c = c(n-1)$$
wobei $c$ die konstante Zeit ist, die für die Operationen innerhalb der Schleife benötigt wird. Da $W(n) = c(n-1)$, folgern wir:
$$W(n) \in \Theta(n)$$
Somit ist die Zeitkomplexität $O(n)$.

### Platzkomplexität
Der Algorithmus verwendet eine feste Menge an Hilfsvariablen: `jumps`, `current_end`, `farthest` und den Schleifeniterator `i`.
Sei $S_{aux}$ der Speicherplatz, der für diese Variablen benötigt wird. Da jede Variable eine primitive Ganzzahl ist (typischerweise 32-Bit oder 64-Bit), ist der benötigte Speicherplatz unabhängig von der Eingabegröße $n$:
$$S_{aux} = \text{sizeof}(\text{int}) \times 4 \in O(1)$$
Das Eingabe-Array $A$ belegt $O(n)$ Speicherplatz, aber die zusätzliche Platzkomplexität ist strikt:
$$S(n) \in O(1)$$