# Formale mathematische Spezifikation: 8-Puzzle (Branch and Bound)

## 1. Definitionen und Notation

Das 8-Puzzle sei definiert als ein Zustandsraumgraph $G = (\mathcal{S}, \mathcal{A})$, wobei:

*   **Zustandsraum ($\mathcal{S}$):** Eine Menge von Konfigurationen, die durch eine Bijektion $\sigma: \{1, \dots, 9\} \to \{0, 1, \dots, 8\}$ dargestellt werden, wobei $0$ das leere Feld bezeichnet. Die Kardinalität des Zustandsraums beträgt $|\mathcal{S}| = \frac{9!}{2} = 181.440$ (aufgrund von Paritätsbeschränkungen bei Permutationen).
*   **Aktionen ($\mathcal{A}$):** Eine Menge von Übergängen $a: \mathcal{S} \to \mathcal{S}$, definiert durch die Bewegung des leeren Feldes in eine benachbarte Position $(r, c) \in \{0, 1, 2\}^2$.
*   **Kostenfunktion ($g$):** Sei $g(s)$ die Pfadkosten vom Anfangszustand $s_0$ zum Zustand $s$, definiert als die Anzahl der Kanten im Pfad $P = (s_0, s_1, \dots, s_k = s)$, wobei $g(s) = k$.
*   **Heuristische Funktion ($h$):** Eine Funktion $h: \mathcal{S} \to \mathbb{N}_0$, die die minimalen Kosten zum Erreichen des Zielzustands $s_g$ schätzt. Für die Manhattan-Distanz sei $pos(i, s)$ die Koordinate $(r, c)$ des Feldes $i$ im Zustand $s$. Dann gilt:
    $$h(s) = \sum_{i=1}^{8} (|r_{i,s} - r_{i,g}| + |c_{i,s} - c_{i,g}|)$$
*   **Bewertungsfunktion ($f$):** Die geschätzten Gesamtkosten $f(s) = g(s) + h(s)$.

## 2. Algebraische Charakterisierung

Der Algorithmus arbeitet als Best-First-Suche auf dem Zustandsraumgraphen. Die Korrektheit des Algorithmus beruht auf den Eigenschaften der heuristischen Funktion $h(s)$.

### Zulässigkeit
Eine Heuristik $h$ ist **zulässig**, wenn für alle $s \in \mathcal{S}$ gilt:
$$h(s) \leq h^*(s)$$
wobei $h^*(s)$ die wahren optimalen Kosten von $s$ nach $s_g$ sind. Da jeder Zug die Manhattan-Distanz genau eines Feldes um exakt 1 ändert und der Zielzustand $h(s_g) = 0$ aufweist, stellt die Manhattan-Distanz eine untere Schranke für die Anzahl der erforderlichen Züge dar, was die Bedingung der Zulässigkeit erfüllt.

### Optimalitätsbedingung
Der Algorithmus verwaltet eine Priority Queue $Q$ der Grenzzustände (Frontier). Sei $C^*$ die Kosten des optimalen Pfades. Der Algorithmus terminiert, wenn $s_g$ aus $Q$ entnommen wird. 
Da $h$ zulässig ist, gilt für jeden Knoten $n$ in der Frontier: $f(n) = g(n) + h(n) \leq g(n) + h^*(n) = f^*(n)$. 
Da der Algorithmus immer den Knoten mit dem minimalen $f(n)$ expandiert, ist garantiert, dass bei der Auswahl von $s_g$ gilt: $g(s_g) = f(s_g) \leq f(n)$ für alle $n$ in der Frontier, was $g(s_g) = C^*$ sicherstellt.

### Zustandsübergänge
Der Übergang vom Zustand $s$ zum Zustand $s'$ durch die Aktion $a$ wird bestimmt durch:
$$g(s') = g(s) + 1$$
$$f(s') = g(s) + 1 + h(s')$$

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität wird durch die Anzahl der im Suchbaum expandierten Knoten bestimmt. 
*   **Schlechtester Fall:** In Abwesenheit einer effektiven Heuristik ($h(s) = 0$) verhält sich der Algorithmus wie der Dijkstra-Algorithmus. Die Anzahl der expandierten Knoten beträgt $O(b^d)$, wobei $b$ der Verzweigungsfaktor ist (durchschnittlich $b \approx 2,67$ für das 8-Puzzle) und $d$ die Tiefe der optimalen Lösung ist.
*   **Durchschnittlicher Fall:** Mit einer zulässigen Heuristik beträgt die Anzahl der expandierten Knoten $O(b^{\epsilon d})$, wobei $\epsilon < 1$ ein Faktor ist, der durch die Genauigkeit der Heuristik bestimmt wird. Die Operationen der Priority Queue (Einfügen und Entnehmen) tragen einen logarithmischen Faktor bei, was zu $O(b^d \log(b^d))$ führt.

### Platzkomplexität
Die Platzkomplexität wird durch die Speicherung der "Closed Set" (besuchte Zustände) und der "Open Set" (Priority Queue) dominiert.
*   **Gesamter Speicherbedarf:** $O(b^d)$.
Im schlechtesten Fall muss der Algorithmus alle generierten Zustände speichern, um Zyklen zu vermeiden und die Optimalität zu gewährleisten. Da der Zustandsraum endlich ist, ist die Platzkomplexität durch $O(|\mathcal{S}|)$ beschränkt, in der Praxis ist sie jedoch durch die Anzahl der Knoten begrenzt, die generiert werden, bevor das Ziel erreicht wird, was $O(b^d)$ entspricht.