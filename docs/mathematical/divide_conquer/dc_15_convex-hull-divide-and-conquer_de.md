# Formale mathematische Spezifikation: Konvexe Hülle (Divide and Conquer)

## 1. Definitionen und Notation

Sei $P = \{p_1, p_2, \dots, p_n\}$ eine Menge von $n$ Punkten in der euklidischen Ebene $\mathbb{R}^2$, wobei jeder Punkt $p_i = (x_i, y_i)$ ist.

*   **Konvexe Hülle:** Die konvexe Hülle von $P$, bezeichnet als $\text{CH}(P)$, ist das eindeutige minimale konvexe Polygon, sodass $P \subseteq \text{CH}(P)$ gilt. Formal ist $\text{CH}(P) = \{ \sum_{i=1}^n \alpha_i p_i \mid \sum \alpha_i = 1, \alpha_i \ge 0 \}$, die konvexe Kombination aller Punkte in $P$.
*   **Orientierungsfunktion:** Für ein geordnetes Tripel von Punkten $(a, b, c)$ definieren wir die Orientierungsfunktion $\Omega: (\mathbb{R}^2)^3 \to \{-1, 0, 1\}$ als:
    $$\Omega(a, b, c) = \text{sgn}((b_x - a_x)(c_y - a_y) - (b_y - a_y)(c_x - a_x))$$
    wobei $\Omega > 0$ eine Drehung gegen den Uhrzeigersinn, $\Omega < 0$ eine Drehung im Uhrzeigersinn und $\Omega = 0$ Kollinearität bezeichnet.
*   **Tangenten:** Gegeben seien zwei disjunkte konvexe Polygone $L$ und $R$, die durch eine vertikale Linie getrennt sind. Die **obere Tangente** ist ein Liniensegment $\overline{u_L u_R}$ (wobei $u_L \in L, u_R \in R$), sodass alle Punkte in $L \cup R$ unterhalb oder auf der Geraden liegen, die $\overline{u_L u_R}$ enthält. Die **untere Tangente** ist analog definiert, sodass alle Punkte oberhalb oder auf der Geraden liegen.

## 2. Algebraische Charakterisierung

Der Algorithmus basiert auf der rekursiven Zerlegung der Menge $P$. Seien $P_L$ und $P_R$ die Teilmengen von $P$, die durch die mediane $x$-Koordinate partitioniert wurden.

### Rekursionsgleichung
Die Zeitkomplexität $T(n)$ wird durch das Master-Theorem bestimmt. Der Merge-Schritt erfordert das Finden der oberen und unteren Tangenten. Da die Eckpunkte der konvexen Hüllen in zyklischer Reihenfolge gespeichert sind, benötigt das Finden der Tangenten mittels eines "Walking"-Verfahrens (Springen zwischen $L$ und $R$) eine Zeit, die proportional zur Anzahl der Eckpunkte $k$ in den Hüllen ist, wobei $k \le n$ gilt. Somit ist der Merge-Schritt $O(n)$.
$$T(n) = 2T\left(\frac{n}{2}\right) + O(n)$$
Nach dem Master-Theorem (Fall 2), wobei $a=2, b=2, f(n)=O(n^1)$, erhalten wir:
$$T(n) = \Theta(n \log n)$$

### Merge-Invariante
Seien $L$ und $R$ die konvexen Hüllen von $P_L$ und $P_R$. Der Merge-Schritt erhält die Invariante aufrecht, dass die resultierende Menge von Eckpunkten $V_{merged}$ folgende Bedingung erfüllt:
$$V_{merged} = (L \setminus \text{interior\_arc}_L) \cup (R \setminus \text{interior\_arc}_R) \cup \{\overline{u_L u_R}, \overline{l_L l_R}\}$$
wobei $\text{interior\_arc}$ die Kette von Eckpunkten repräsentiert, die durch das Hinzufügen der neuen Tangentenbrücken $\overline{u_L u_R}$ (oben) und $\overline{l_L l_R}$ (unten) konkav oder intern werden.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus verläuft in drei Phasen:
1.  **Preprocessing:** Das Sortieren von $P$ nach der $x$-Koordinate benötigt $O(n \log n)$.
2.  **Divide:** Die Menge wird in $O(1)$ Zeit in zwei Teilmengen der Größe $n/2$ partitioniert (bei sortierter Eingabe).
3.  **Conquer:** Der Merge-Schritt beinhaltet das Finden der oberen und unteren Tangenten. Da die Hüllen konvex sind, bewegen sich die "Walking"-Pointer nur monoton um die Eckpunkte herum. Im Schlechtesten Fall durchlaufen die Pointer den gesamten Umfang der Hüllen, was $O(n)$ entspricht.
    Summiert man den Aufwand über den Rekursionsbaum:
    $$\sum_{i=0}^{\log n} 2^i \cdot O\left(\frac{n}{2^i}\right) = \sum_{i=0}^{\log n} O(n) = O(n \log n)$$

### Platzkomplexität
*   **Zusätzlicher Speicherplatz:** Die Tiefe des Rekursions-Stacks beträgt $\log n$. Auf jeder Ebene der Rekursion speichern wir die Pointer auf die aktuellen Hüllen.
*   **Gesamtspeicherplatz:** Wenn der Algorithmus so implementiert ist, dass er für jede Hülle neue Arrays zurückgibt, beträgt die Platzkomplexität $O(n)$ aufgrund der Speicherung der Eckpunkte auf jeder Ebene. Wenn der Algorithmus jedoch mit Indizes oder Pointern auf das ursprüngliche sortierte Array arbeitet, beträgt die zusätzliche Platzkomplexität $O(\log n)$, um den Rekursions-Stack zu verwalten. Somit ist der Algorithmus in Standardimplementierungen $O(n)$, aber $O(\log n)$ ist bei sorgfältiger Pointer-Verwaltung erreichbar.