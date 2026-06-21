# Formale mathematische Spezifikation: Job Sequencing Problem

## 1. Definitionen und Notation

Sei $\mathcal{J} = \{J_1, J_2, \dots, J_N\}$ eine Menge von $N$ Jobs. Jeder Job $J_i$ ist definiert als ein Tripel $(id_i, d_i, p_i)$, wobei:
*   $id_i \in \mathbb{Z}^+$ der eindeutige Identifikator ist.
*   $d_i \in \{1, 2, \dots, D_{max}\}$ die Deadline ist, die den spätesten Zeitpunkt darstellt, bis zu dem der Job abgeschlossen sein muss.
*   $p_i \in \mathbb{R}^+$ der mit dem Abschluss des Jobs $J_i$ verbundene Gewinn ist.

Sei $\mathcal{T} = \{1, 2, \dots, D_{max}\}$ die Menge der diskreten Zeitfenster, wobei jedes Zeitfenster $t \in \mathcal{T}$ eine Kapazität von einem Job hat. Ein Zeitplan ist eine partielle injektive Abbildung $\sigma: \mathcal{J}' \to \mathcal{T}$, wobei $\mathcal{J}' \subseteq \mathcal{J}$ die Teilmenge der eingeplanten Jobs ist, sodass für jeden Job $J_i \in \mathcal{J}'$ die Bedingung $\sigma(J_i) \leq d_i$ erfüllt ist.

Das Ziel ist es, eine Teilmenge $\mathcal{J}^* \subseteq \mathcal{J}$ und eine gültige Abbildung $\sigma^*$ zu finden, welche den Gesamtgewinn maximiert:
$$\text{Maximiere } \sum_{J_i \in \mathcal{J}^*} p_i$$

## 2. Algebraische Charakterisierung

Der Algorithmus basiert auf der **Matroid Greedy Property**. Insbesondere bildet die Menge aller planbaren Teilmengen von Jobs ein *Forest Matroid* (oder allgemeiner ein *Transversal Matroid*), was garantiert, dass eine Greedy-Strategie eine optimale Lösung liefert.

### Die Greedy-Choice-Eigenschaft
Seien die Jobs so sortiert, dass $p_{(1)} \geq p_{(2)} \geq \dots \geq p_{(N)}$ gilt. Der Algorithmus konstruiert die optimale Menge $\mathcal{J}^*$ iterativ. Sei $\mathcal{S}_k$ die Menge der belegten Zeitfenster nach Betrachtung der ersten $k$ Jobs. Für einen Job $J_{(k)}$ mit Deadline $d_{(k)}$ wird der Job genau dann zu $\mathcal{J}^*$ hinzugefügt, wenn ein Zeitfenster $t \in \mathcal{T}$ existiert, sodass $t \leq d_{(k)}$ und $t \notin \mathcal{S}_{k-1}$.

Um die Verfügbarkeit von Zeitfenstern für zukünftige Jobs mit potenziell engeren Deadlines zu maximieren, wählt der Algorithmus das spätestmögliche Zeitfenster:
$$\sigma(J_{(k)}) = \max \{t \in \mathcal{T} \mid t \leq d_{(k)} \land t \notin \mathcal{S}_{k-1}\}$$
Falls die Menge $\{t \in \mathcal{T} \mid t \leq d_{(k)} \land t \notin \mathcal{S}_{k-1}\}$ leer ist, wird der Job $J_{(k)}$ verworfen.

### Schleifeninvariante
Zu Beginn jeder Iteration $k$ (wobei $k$ der Index der sortierten Jobs ist) repräsentiert die Menge der belegten Zeitfenster $\mathcal{S}_{k-1}$ die optimale Belegung der bisher betrachteten Jobs mit dem höchsten Gewinn. Die Greedy-Entscheidung stellt sicher, dass für jede Teilmenge von Jobs $\mathcal{J}' \subseteq \{J_{(1)}, \dots, J_{(k)}\}$ der Gewinn $\sum_{J \in \mathcal{J}'} p_J$ unter Berücksichtigung der Deadline-Beschränkungen maximiert wird.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die gesamte Zeitkomplexität $T(N)$ ist die Summe aus der Sortierphase und der Planungsphase.

1.  **Sortierung:** Das Sortieren von $N$ Jobs nach Gewinn benötigt $O(N \log N)$ Vergleiche.
2.  **Planung:** Wir iterieren durch $N$ Jobs. Für jeden Job führen wir einen linearen Scan des `slots` Array durch. Im schlechtesten Fall können wir für jeden Job $J_i$ $O(D_{max})$ Zeitfenster scannen.
    $$T(N) = O(N \log N) + \sum_{i=1}^{N} O(\min(d_i, N)) = O(N \log N + N \cdot \min(N, D_{max}))$$
    Da $D_{max}$ in praktischen Instanzen oft durch $N$ begrenzt ist, beträgt die Komplexität im schlechtesten Fall $O(N^2)$. Unter Verwendung einer Disjoint Set Union (DSU) Datenstruktur zur Suche nach dem nächsten verfügbaren Zeitfenster reduziert sich die Planungsphase jedoch auf $O(N \alpha(N))$, wobei $\alpha$ die inverse Ackermann-Funktion ist. Somit ergibt sich eine optimierte Komplexität von $O(N \log N)$.

### Platzkomplexität
Der Algorithmus benötigt:
1.  **Speicher für Jobs:** $O(N)$ zum Speichern der Job-Objekte.
2.  **Slots Array:** $O(D_{max})$ zur Verwaltung des booleschen Status der Zeitfenster.

Die gesamte zusätzliche Platzkomplexität beträgt $O(N + D_{max})$. In Szenarien, in denen $D_{max} \gg N$, ist der effektive Speicherbedarf auf $O(N)$ begrenzt, indem nur die im Input vorhandenen, unterschiedlichen Deadlines berücksichtigt werden.