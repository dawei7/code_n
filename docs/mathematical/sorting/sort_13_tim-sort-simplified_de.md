# Formale mathematische Spezifikation: Tim Sort (vereinfacht)

## 1. Definitionen und Notation

Sei $A = [a_0, a_1, \dots, a_{n-1}]$ eine Sequenz von $n$ Elementen aus einer total geordneten Menge $(\mathcal{X}, \le)$. Das Ziel ist die Erzeugung einer Permutation $A'$ von $A$, sodass $a'_0 \le a'_1 \le \dots \le a'_{n-1}$ gilt.

*   **Run:** Eine zusammenhängende Teilsequenz $R_{i,j} = [a_i, a_{i+1}, \dots, a_j]$, wobei $0 \le i \le j < n$.
*   **Sortierter Run:** Ein Run $R_{i,j}$ ist sortiert, wenn $\forall k \in [i, j-1], a_k \le a_{k+1}$ gilt.
*   **MinRun:** Ein Parameter $M \in \mathbb{Z}^+$, typischerweise $M \approx 32$, der die Mindestlänge eines Runs definiert, der in der Merge-Phase verarbeitet wird.
*   **Zustandsraum:** Der Algorithmus operiert auf dem Zustand $\mathcal{S} = (A, \mathcal{R})$, wobei $A$ das aktuelle Array ist und $\mathcal{R} = \{[i_0, j_0], [i_1, j_1], \dots, [i_k, j_k]\}$ eine Partition der Indizes darstellt, sodass $\bigcup_{m=0}^k [i_m, j_m] = [0, n-1]$ gilt und jeder $R_{i_m, j_m}$ ein sortierter Run ist.

## 2. Algebraische Charakterisierung

Der Algorithmus verläuft in zwei distinkten Phasen: der **Run-Generierungsphase** und der **Merge-Phase**.

### Phase 1: Run-Generierung
Für jeden Index $i \in \{0, \dots, n-1\}$ identifizieren wir einen maximalen sortierten Run $R_{i,j}$. Wenn $j - i + 1 < M$, erweitern wir den Run auf die Länge $\min(i+M, n)$ und wenden einen Insertion-Sort-Operator $\mathcal{I}: \mathcal{X}^m \to \mathcal{X}^m$ an, der eine unsortierte Sequenz auf ihre sortierte Permutation abbildet. Die aufrechterhaltene Invariante lautet:
$$\forall [i, j] \in \mathcal{R}, \quad \text{length}(R_{i,j}) \ge M \lor j = n-1$$

### Phase 2: Merge-Phase
Sei $\mathcal{R}_t$ die Menge der Runs in Iteration $t$. Der Merge-Operator $\mathcal{M}: \mathcal{X}^{n_1} \times \mathcal{X}^{n_2} \to \mathcal{X}^{n_1+n_2}$ ist als die Standard-Merge-Operation für zwei sortierte Sequenzen definiert. Der Algorithmus wendet $\mathcal{M}$ iterativ auf benachbarte Runs an:
$$\mathcal{R}_{t+1} = \{ \mathcal{M}(R_{2k}, R_{2k+1}) \mid k = 0, \dots, \lfloor |\mathcal{R}_t|/2 \rfloor - 1 \} \cup \{ \text{verbleibende Runs} \}$$
Der Prozess terminiert, wenn $|\mathcal{R}_t| = 1$ gilt. Die Korrektheit wird durch die Eigenschaft garantiert, dass $\mathcal{M}(R_a, R_b)$ sortiert ist, sofern $R_a$ und $R_b$ sortiert sind.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die gesamte Zeitkomplexität $T(n)$ ist die Summe aus der Zeit für die Run-Generierung $T_g(n)$ und der Merge-Zeit $T_m(n)$.

1.  **Run-Generierung:** Für jeden Block der Größe $M$ benötigt Insertion Sort $O(M^2)$. Da es $n/M$ Blöcke gibt, gilt $T_g(n) = O(\frac{n}{M} \cdot M^2) = O(nM)$. Da $M$ eine Konstante ist, gilt $T_g(n) = O(n)$.
2.  **Merge-Phase:** Der Merge-Prozess bildet einen Binärbaum der Höhe $\lceil \log_2(n/M) \rceil$. Auf jeder Ebene des Baums ist jedes Element des Arrays an genau einer Merge-Operation beteiligt, was $O(n)$ Arbeit pro Ebene entspricht.
    $$T_m(n) = \sum_{h=1}^{\log_2(n/M)} O(n) = O(n \log(n/M))$$
Da $M$ konstant ist, gilt $T(n) = O(n) + O(n \log n) = O(n \log n)$.
*   **Bestfall:** Wenn das Array bereits sortiert ist, gilt $T_g(n) = O(n)$ und die Merge-Phase erkennt die sortierte Eigenschaft (oder führt triviale Merges durch), was zu $T(n) = \Omega(n)$ führt.

### Platzkomplexität
Der Algorithmus benötigt zusätzlichen Speicherplatz für die Merge-Operation. Während des Merges zweier Runs $R_1$ und $R_2$ wird ein temporärer Puffer benötigt, um die Elemente zu speichern, bevor sie in das ursprüngliche Array zurückgeschrieben werden.
*   **Zusätzlicher Speicher:** Im schlechtesten Fall benötigt die Merge-Operation $O(n)$ Speicherplatz, um die gemergten Elemente aufzunehmen.
*   **Gesamter Speicher:** $S(n) = O(n)$ für das Eingabe-Array plus $O(n)$ für den zusätzlichen Puffer, was eine gesamte Platzkomplexität von $O(n)$ ergibt.