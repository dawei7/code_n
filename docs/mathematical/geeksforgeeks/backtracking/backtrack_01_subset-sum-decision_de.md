# Formale mathematische Spezifikation: Teilmengen (Potenzmenge)

## 1. Definitionen und Notation

Sei $S$ eine endliche Menge von $N$ verschiedenen Elementen, wobei $N = |S| \in \mathbb{N}_0$. Um die algorithmische Indizierung zu erleichtern, legen wir eine beliebige totale Ordnung auf $S$ fest, um sie als indizierte Sequenz darzustellen:

$$\mathbf{s} = (s_0, s_1, \dots, s_{N-1}) \in \mathcal{X}^N$$

wobei $\mathcal{X}$ die zugrunde liegende Domäne der Elemente ist.

### Die Potenzmenge
Die Potenzmenge von $S$, bezeichnet als $\mathcal{P}(S)$ oder $2^S$, ist die Menge aller Teilmengen von $S$:

$$\mathcal{P}(S) = \{ A \mid A \subseteq S \}$$

Die Kardinalität der Potenzmenge ist gegeben durch $|\mathcal{P}(S)| = 2^N$.

### Zustandsraumdarstellung
Der Backtracking-Algorithmus exploriert systematisch den Entscheidungsraum der Teilmengenkonstruktionen. Wir modellieren diesen Entscheidungsraum als einen gerichteten, bewurzelten, vollständigen Binärbaum $T = (V, E)$ der Höhe $N$:

*   **Knoten ($V$):** Jeder Knoten $v \in V$ entspricht einer partiellen Entscheidungssequenz $\mathbf{b} = (b_0, b_1, \dots, b_{i-1}) \in \{0, 1\}^i$ der Länge $i \in \{0, \dots, N\}$, die die für die ersten $i$ Elemente von $\mathbf{s}$ getroffenen Entscheidungen repräsentiert.
    *   Der Wurzelknoten $r \in V$ entspricht der leeren Sequenz $\epsilon$ (wobei $i = 0$).
    *   Die Blattknoten $L \subset V$ entsprechen vollständigen Entscheidungssequenzen der Länge $N$, d. h. $L = \{0, 1\}^N$.
*   **Kanten ($E$):** Für jeden internen Knoten $v$, der $\mathbf{b} \in \{0, 1\}^i$ mit $i < N$ repräsentiert, existieren genau zwei ausgehende gerichtete Kanten:
    1.  Eine Kante zu $v_{\text{include}}$, die $(\mathbf{b}, 1)$ repräsentiert und die Inklusion von $s_i$ anzeigt.
    2.  Eine Kante zu $v_{\text{exclude}}$, die $(\mathbf{b}, 0)$ repräsentiert und die Exklusion von $s_i$ anzeigt.

### Die Ausbildungsabbildung
Wir definieren eine Bijektion $\phi: \{0, 1\}^N \to \mathcal{P}(S)$, die jeden Blattknoten (vollständiger Entscheidungspfad) auf seine entsprechende Teilmenge abbildet:

$$\phi(\mathbf{b}) = \{ s_i \in S \mid b_i = 1 \}$$

Das Ziel des Algorithmus ist die Konstruktion der Mengen-Familie:

$$\mathcal{R} = \{ \phi(\mathbf{b}) \mid \mathbf{b} \in \{0, 1\}^N \}$$

---

## 2. Algebraische Charakterisierung

### Rekursive Formulierung
Sei $f: \{0, \dots, N\} \times \mathcal{P}(S) \to \mathcal{P}(\mathcal{P}(S))$ eine mengenwertige Funktion, die rekursiv wie folgt definiert ist:

$$f(i, A) = \begin{cases}
\{ A \} & \text{falls } i = N \\
f(i+1, A \cup \{s_i\}) \cup f(i+1, A) & \text{falls } 0 \le i < N
\end{cases}$$

wobei $i$ den aktuellen Entscheidungsindex repräsentiert und $A \subseteq \{s_0, \dots, s_{i-1}\}$ die akkumulierte Teilmenge darstellt.

### Beweis der Korrektheit
Wir beweisen durch vollständige Induktion über die verbleibende Tiefe $d = N - i$, dass für jedes $i \in \{0, \dots, N\}$ und jede Teilmenge $A \subseteq \{s_0, \dots, s_{i-1}\}$ gilt:

$$f(i, A) = \{ A \cup B \mid B \subseteq \{s_i, \dots, s_{N-1}\} \}$$

#### Induktionsanfang ($d = 0 \implies i = N$):
Per Definition gilt:

$$f(N, A) = \{ A \}$$

Da die einzige Teilmenge der leeren Menge $\emptyset$ die Menge $\emptyset$ selbst ist, erhalten wir:

$$\{ A \cup B \mid B \subseteq \emptyset \} = \{ A \cup \emptyset \} = \{ A \}$$

Somit ist der Induktionsanfang erfüllt.

#### Induktionsschritt:
Wir nehmen an, dass die Induktionsvoraussetzung für $d = k$ gilt, was dem Index $i+1$ entspricht (wobei $0 \le i < N$). Das heißt, für jedes $A' \subseteq \{s_0, \dots, s_i\}$ gilt:

$$f(i+1, A') = \{ A' \cup B' \mid B' \subseteq \{s_{i+1}, \dots, s_{N-1}\} \}$$

Wir evaluieren $f(i, A)$ für $A \subseteq \{s_0, \dots, s_{i-1}\}$:

$$f(i, A) = f(i+1, A \cup \{s_i\}) \cup f(i+1, A)$$

Durch Anwendung der Induktionsvoraussetzung auf beide Terme der rechten Seite erhalten wir:

1.  Für $A' = A \cup \{s_i\}$:
    $$f(i+1, A \cup \{s_i\}) = \{ A \cup \{s_i\} \cup B' \mid B' \subseteq \{s_{i+1}, \dots, s_{N-1}\} \}$$
2.  Für $A' = A$:
    $$f(i+1, A) = \{ A \cup B' \mid B' \subseteq \{s_{i+1}, \dots, s_{N-1}\} \}$$

Die Kombination dieser beiden Mengen-Familien ergibt:

$$f(i, A) = \{ A \cup C \mid C \in \mathcal{C} \}$$

wobei $\mathcal{C} = \{ \{s_i\} \cup B' \mid B' \subseteq \{s_{i+1}, \dots, s_{N-1}\} \} \cup \{ B' \mid B' \subseteq \{s_{i+1}, \dots, s_{N-1}\} \}$. 

Aufgrund der fundamentalen Eigenschaften von Potenzmengen enthält jede Teilmenge $B \subseteq \{s_i, \dots, s_{N-1}\}$ entweder $s_i$ (in diesem Fall ist $B = \{s_i\} \cup B'$ für ein $B' \subseteq \{s_{i+1}, \dots, s_{N-1}\}$) oder sie enthält $s_i$ nicht (in diesem Fall ist $B = B'$). Somit gilt $\mathcal{C} = \mathcal{P}(\{s_i, \dots, s_{N-1}\})$.

Daher folgt:

$$f(i, A) = \{ A \cup B \mid B \subseteq \{s_i, \dots, s_{N-1}\} \}$$

Dies schließt den Induktionsbeweis ab.

#### Korollar:
Für den initialen Aufruf, bei dem $i = 0$ und $A = \emptyset$:

$$f(0, \emptyset) = \{ \emptyset \cup B \mid B \subseteq \{s_0, \dots, s_{N-1}\} \} = \{ B \mid B \subseteq S \} = \mathcal{P}(S)$$

Dies beweist formal, dass die rekursive Formulierung die exakte Potenzmenge von $S$ berechnet.

### Zustandsübergang und Backtracking-Mutation
Um die Platzkomplexität zu optimieren, vermeidet der Algorithmus das Kopieren der Teilmenge $A$ bei jedem rekursiven Schritt. Stattdessen verwaltet er einen einzelnen veränderbaren Stack $\mathbf{a}$, der den aktuellen Zustand repräsentiert. 

Sei $\mathbf{a}^{(t)}$ der Zustand des Stacks zum Zeitpunkt $t$. Der Übergang vom Zustand $(i, \mathbf{a}^{(t)})$ zu seinen Teilproblemen ist durch die folgende Sequenz von Operationen charakterisiert:

1.  **Inklusionszweig:**
    $$\mathbf{a}^{(t+1)} \leftarrow \mathbf{a}^{(t)} \mathbin{\Vert} s_i$$
    wobei $\Vert$ die Append-Operation bezeichnet. Der Algorithmus rekursiert dann zum Zustand $(i+1, \mathbf{a}^{(t+1)})$.
2.  **Backtracking (Wiederherstellung des Zustands):**
    $$\mathbf{a}^{(t+2)} \leftarrow \text{pop}(\mathbf{a}^{(t+1)}) = \mathbf{a}^{(t)}$$
3.  **Exklusionszweig:**
    Der Algorithmus rekursiert zum Zustand $(i+1, \mathbf{a}^{(t+2)})$, ohne den Stack zu modifizieren.

---

## 3. Komplexitätsanalyse

### Zeitkomplexität
Sei $W(N)$ der gesamte Rechenaufwand (Zeitkomplexität), der erforderlich ist, um die Potenzmenge einer Menge der Größe $N$ zu generieren. 

Die Ausführung des Backtracking-Algorithmus entspricht einer Tiefensuche im vollständigen Binärbaum $T$. Die Gesamtzahl der Knoten in einem vollständigen Binärbaum der Höhe $N$ beträgt:

$$\sum_{i=0}^{N} 2^i = 2^{N+1} - 1$$

Wir unterteilen die an diesen Knoten geleistete Arbeit in zwei Kategorien:

1.  **Interne Knoten ($i < N$):** An jedem der $2^N - 1$ internen Knoten führt der Algorithmus $O(1)$ Operationen aus (Index-Inkrementierung, Stack-Push/Pop-Operationen und Overhead für rekursive Aufrufe).
2.  **Blattknoten ($i = N$):** Es gibt genau $2^N$ Blattknoten. An jedem Blattknoten muss der Algorithmus den aktuellen Zustand des Stacks $\mathbf{a}$ in die Ausgabekollektion kopieren. Da die Größe der Teilmenge an einem Blattknoten bis zu $N$ betragen kann, benötigt das Kopieren der Teilmenge $\Theta(|\mathbf{a}|) = O(N)$ Zeit.

Somit ist die Gesamtarbeit $W(N)$ beschränkt durch:

$$W(N) = \sum_{i=0}^{N-1} 2^i \cdot \Theta(1) + 2^N \cdot \Theta(N)$$

$$W(N) = \Theta(2^N) + \Theta(N \cdot 2^N) = \Theta(N \cdot 2^N)$$

Daher beträgt die Zeitkomplexität des Algorithmus im Bestfall, durchschnittlichen Fall und Schlechtesten Fall exakt $\Theta(N \cdot 2^N)$.

### Platzkomplexität

#### Hilfsplatzbedarf
Der Hilfsplatzbedarf ist der zusätzliche Speicherplatz, der vom Algorithmus verwendet wird, exklusive des Speichers, der für die endgültige Ausgabe reserviert ist.

1.  **Rekursions-Stack:** Die maximale Tiefe des Rekursionsbaums beträgt $N$. Folglich enthält der System-Call-Stack zu jedem Zeitpunkt höchstens $N + 1$ aktive Stack-Frames. Jeder Frame benötigt $O(1)$ Platz, um lokale Variablen (wie den Index $i$) zu speichern. Dies trägt $O(N)$ zum Platzbedarf bei.
2.  **Zustandsrepräsentation:** Der veränderbare Stack $\mathbf{a}$, der zur Speicherung der aktuellen Teilmenge verwendet wird, enthält höchstens $N$ Elemente von $\mathcal{X}$. Dies trägt $O(N)$ zum Platzbedarf bei.

Somit ist die Komplexität des Hilfsplatzbedarfs:

$$\text{Space}_{\text{aux}}(N) = O(N)$$

#### Gesamtplatzbedarf
Der Gesamtplatzbedarf beinhaltet den Speicher, der zur Speicherung der endgültigen Ausgabe $\mathcal{R}$ erforderlich ist. 

Die Ausgabe besteht aus $2^N$ Teilmengen. Die durchschnittliche Größe einer Teilmenge in der Potenzmenge ergibt sich aus dem Erwartungswert der Binomialverteilung für $p = 0.5$:

$$\mathbb{E}[|A|] = \frac{1}{2^N} \sum_{k=0}^{N} \binom{N}{k} k = \frac{1}{2^N} \left( N 2^{N-1} \right) = \frac{N}{2}$$

Der gesamte Speicherbedarf zur Speicherung aller generierten Teilmengen ist:

$$\text{Space}_{\text{total}}(N) = 2^N \cdot \Theta(N) = \Theta(N \cdot 2^N)$$