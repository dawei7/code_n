# Formale Mathematische Spezifikation: Punktaktualisierung

## 1. Definitionen und Notation

Sei $A = [a_0, a_1, \dots, a_{N-1}]$ ein Array von $N$ Elementen, wobei $a_i \in \mathbb{R}$. Ein Segment Tree $\mathcal{T}$ ist ein verwurzelter binärer Baum, der eine Partition des Indexbereichs $[0, N-1]$ darstellt.

*   **Baumstruktur:** Jeder Knoten $v$ in $\mathcal{T}$ entspricht einem Intervall $[L_v, R_v] \subseteq [0, N-1]$.
*   **Zustandsraum:** Der Baum $\mathcal{T}$ wird durch ein Array $T$ der Größe $4N$ dargestellt. Für einen Knoten $v$ bezeichne $T[v]$ den an diesem Knoten gespeicherten Wert, definiert durch den assoziativen binären Operator $\oplus$ (z.B. Summation):
    $$T[v] = \bigoplus_{i=L_v}^{R_v} a_i$$
*   **Blattknoten:** Ein Knoten $v$ ist ein Blatt, wenn $L_v = R_v = i$, in welchem Fall $T[v] = a_i$.
*   **Innere Knoten:** Für einen Nicht-Blattknoten $v$ mit Kindern $u_{left}$ und $u_{right}$, die $[L_v, M]$ bzw. $[M+1, R_v]$ abdecken, wobei $M = \lfloor (L_v + R_v) / 2 \rfloor$:
    $$T[v] = T[u_{left}] \oplus T[u_{right}]$$
*   **Aktualisierungsoperation:** Gegeben eine Position $p \in \{0, \dots, N-1\}$ und einen neuen Wert $x \in \mathbb{R}$, modifiziert die `update`-Funktion $\text{update}(v, p, x)$ das Array $A$ so, dass $a_p \leftarrow x$, und aktualisiert alle $T[v]$, sodass $p \in [L_v, R_v]$.

## 2. Algebraische Charakterisierung

Die Korrektheit des Point Update Algorithmus wird durch die rekursive Definition der Baumknoten bestimmt. Sei $T^{(t)}$ der Zustand des Baumes zum Zeitpunkt $t$. Die Aktualisierungsoperation ist durch die folgende Rekursionsgleichung für einen Knoten $v$, der $[L_v, R_v]$ abdeckt, definiert:

1.  **Basisfall (Blatt):** Wenn $L_v = R_v = p$, dann gilt:
    $$T^{(t+1)}[v] = x$$
2.  **Rekursiver Schritt (Intern):** Wenn $L_v \leq p \leq R_v$ und $L_v < R_v$:
    Sei $M = \lfloor (L_v + R_v) / 2 \rfloor$.
    Wenn $p \leq M$, dann gilt $T^{(t+1)}[v] = T^{(t+1)}[u_{left}] \oplus T^{(t)}[u_{right}]$.
    Wenn $p > M$, dann gilt $T^{(t+1)}[v] = T^{(t)}[u_{left}] \oplus T^{(t+1)}[u_{right}]$.

**Invariante:** Für jeden Knoten $v$, sodass $p \notin [L_v, R_v]$, gilt $T^{(t+1)}[v] = T^{(t)}[v]$. Die Aktualisierungsoperation bewahrt die Invariante, dass für alle $v \in \mathcal{T}$, $T[v]$ das Ergebnis der assoziativen Operation $\oplus$ bleibt, angewendet auf die Elemente in seinem Bereich $[L_v, R_v]$ unter dem modifizierten Array $A'$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus durchläuft einen Pfad von der Wurzel zu einem Blatt. Sei $H$ die Höhe des Baumes. Da der Baum ein balancierter binärer Baum ist, der über $N$ Elementen konstruiert wird, beträgt die Höhe $H = \lceil \log_2 N \rceil$.

Auf jeder Ebene $k \in \{0, 1, \dots, H\}$ führt der Algorithmus eine konstante Anzahl von Operationen aus:
1.  Vergleich von $p$ mit $M$.
2.  Rekursiver Aufruf (oder Basisfallzuweisung).
3.  Die Merge-Operation $T[v] = T[u_{left}] \oplus T[u_{right}]$ während der Backtracking-Phase.

Die Gesamtarbeit $W(N)$ ist durch die Rekurrenz gegeben:
$$W(N) = W(N/2) + O(1)$$
Nach dem Master-Theorem, wobei $a=1, b=2, f(n)=O(1)$, erhalten wir $W(N) = O(\log N)$. Somit beträgt die Zeitkomplexität $\Theta(\log N)$.

### Platzkomplexität
*   **Hilfsspeicherplatz:** Der Algorithmus verwendet einen rekursiven Aufruf-Stack. Da die Rekursionstiefe der Höhe des Baumes entspricht, beträgt die maximale Tiefe des Stacks $H = \lceil \log_2 N \rceil$. Daher beträgt die Hilfsspeicherplatzkomplexität $O(\log N)$.
*   **Gesamtplatzbedarf:** Die Baumstruktur selbst belegt $O(N)$ Platz (typischerweise $4N$ Knoten, um die Heap-ähnliche Indizierung zu ermöglichen). Die Aktualisierungsoperation wird in-place durchgeführt, wobei $O(1)$ zusätzlicher Platz über den Rekursions-Stack hinaus benötigt wird. Somit beträgt die Gesamtplatzkomplexität $O(N)$.