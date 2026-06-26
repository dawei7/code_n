# Formale Mathematische Spezifikation: Counting Sort

## 1. Definitionen und Notation

Sei $A = [a_1, a_2, \dots, a_n]$ eine Eingabesequenz von $n$ ganzen Zahlen, wobei jedes Element $a_i \in \mathbb{Z}_{\ge 0}$ ist. Sei $k = \max(A)$ der maximale Wert in der Sequenz. Der Definitionsbereich der Eingabeelemente ist die Menge $\mathcal{D} = \{0, 1, \dots, k\}$.

Wir definieren die folgenden Hilfsstrukturen:
*   **Frequency Array:** Eine Abbildung $C: \mathcal{D} \to \{0, 1, \dots, n\}$, wobei $C[v]$ die Kardinalität der Menge $\{a_i \in A \mid a_i = v\}$ darstellt.
*   **Prefix Sum Array:** Eine Abbildung $P: \mathcal{D} \to \{0, 1, \dots, n\}$, definiert als die kumulative Verteilungsfunktion der Frequenzen:
    $$P[j] = \sum_{i=0}^{j} C[i]$$
*   **Output Array:** Eine Sequenz $B = [b_1, b_2, \dots, b_n]$, die eine Permutation von $A$ ist, sodass $b_1 \le b_2 \le \dots \le b_n$ gilt.

## 2. Algebraische Charakterisierung

Die Korrektheit von Counting Sort beruht auf der Transformation von Frequenzen in Positionsindizes. Der Algorithmus durchläuft drei formale Phasen:

**Phase 1: Frequenzzählung**
Das Frequency Array $C$ wird so konstruiert, dass:
$$C[v] = \sum_{i=1}^{n} \mathbb{I}(a_i = v)$$
wobei $\mathbb{I}(\cdot)$ die Indikatorfunktion ist.

**Phase 2: Präfixsummation**
Das Array $P$ wird über die Rekurrenz berechnet:
$$P[j] = \begin{cases} C[0] & \text{if } j = 0 \\ P[j-1] + C[j] & \text{if } 0 < j \le k \end{cases}$$
Für jeden Wert $v$ repräsentiert $P[v]$ die Gesamtzahl der Elemente in $A$, die kleiner oder gleich $v$ sind. Folglich belegen die Elemente, die gleich $v$ sind, die Indizes im Bereich $(P[v-1], P[v]]$ im sortierten Output Array $B$ (unter Verwendung von 1-basierter Indizierung).

**Phase 3: Stabile Platzierung**
Um Stabilität zu gewährleisten, iterieren wir durch die Eingabe $A$ in umgekehrter Reihenfolge ($i = n$ absteigend bis $1$). Für jedes $a_i$ wird das Element in $B$ an der Position platziert, die durch die aktuelle Präfixsumme bestimmt wird:
$$B[P[a_i]] = a_i$$
Nach der Platzierung wird die Präfixsumme dekrementiert, um die belegte Position zu berücksichtigen:
$$P[a_i] \leftarrow P[a_i] - 1$$
Die Schleifeninvariante, die bei jedem Schritt $t$ (wobei $t$ die Anzahl der platzierten Elemente ist) aufrechterhalten wird, besagt, dass die Elemente $\{b_{P[v]-t+1}, \dots, b_{P[v]}\}$ genau die bisher verarbeiteten Instanzen des Wertes $v$ sind, wobei ihre relative Reihenfolge aus $A$ erhalten bleibt.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus besteht aus drei separaten linearen Durchläufen:
1.  **Zählung:** Ein einzelner Durchlauf über $A$ zur Befüllung von $C$, der $\sum_{i=1}^n 1 = n$ Operationen erfordert.
2.  **Präfixsummen:** Ein einzelner Durchlauf über $C$ der Größe $k+1$, der $\sum_{j=0}^k 1 = k+1$ Operationen erfordert.
3.  **Platzierung:** Ein einzelner Durchlauf über $A$ (in umgekehrter Reihenfolge), der $n$ Operationen erfordert.

Die gesamte Zeitkomplexität $T(n, k)$ ist gegeben durch:
$$T(n, k) = \Theta(n) + \Theta(k) + \Theta(n) = \Theta(n + k)$$
Da der Algorithmus keine Vergleiche zwischen Elementen durchführt, umgeht er die untere Schranke von $\Omega(n \log n)$, die für vergleichsbasierte Sortiermodelle festgelegt wurde.

### Platzkomplexität
Der Algorithmus benötigt Hilfsplatz für das Frequency/Prefix-Sum Array $C$ und das Output Array $B$.
*   **Hilfsplatz:** Das Array $C$ benötigt $k+1$ Speichereinheiten.
*   **Output-Platz:** Das Array $B$ benötigt $n$ Speichereinheiten.

Die gesamte Platzkomplexität $S(n, k)$ ist:
$$S(n, k) = \Theta(n + k)$$
Dies demonstriert einen Raum-Zeit-Kompromiss: Der Algorithmus erreicht eine lineare Zeitkomplexität auf Kosten von Speicher, der proportional zum Wertebereich der Eingabewerte ist. Wenn $k \gg n$, wird die Platzkomplexität zur dominierenden Einschränkung, was den Algorithmus ineffizient macht.