# Formale mathematische Spezifikation: Maximale Züge für Halte

## 1. Definitionen und Notation

Sei $\mathcal{T} = \{t_1, t_2, \dots, t_N\}$ die Menge von $N$ Zügen. Jeder Zug $t_i$ ist definiert als ein Tripel $t_i = (a_i, d_i, p_i)$, wobei:
*   $a_i \in \mathbb{R}_{\ge 0}$ die Ankunftszeit ist.
*   $d_i \in \mathbb{R}_{\ge 0}$ die Abfahrtszeit ist, unter der Bedingung $a_i < d_i$.
*   $p_i \in \{1, 2, \dots, P\}$ der Index des Bahnsteigs ist.

Sei $\mathcal{P}_j = \{t_i \in \mathcal{T} \mid p_i = j\}$ die Teilmenge der Züge, die dem Bahnsteig $j$ zugewiesen sind, für $j \in \{1, \dots, P\}$. Beachten Sie, dass die Sammlung $\{\mathcal{P}_1, \mathcal{P}_2, \dots, \mathcal{P}_P\}$ eine Partition von $\mathcal{T}$ bildet, sodass $\bigcup_{j=1}^P \mathcal{P}_j = \mathcal{T}$ und $\mathcal{P}_j \cap \mathcal{P}_k = \emptyset$ für $j \neq k$ gilt.

Eine Teilmenge von Zügen $\mathcal{S}_j \subseteq \mathcal{P}_j$ wird als *zulässig* betrachtet, wenn für zwei beliebige verschiedene Züge $t_u, t_v \in \mathcal{S}_j$ die Intervalle $[a_u, d_u]$ und $[a_v, d_v]$ sich nicht überschneiden, spezifisch:
$$\forall t_u, t_v \in \mathcal{S}_j, u \neq v \implies d_u \le a_v \lor d_v \le a_u$$

Das Ziel ist es, die Kardinalität der maximalen zulässigen Teilmenge $\mathcal{S} = \bigcup_{j=1}^P \mathcal{S}_j^*$ zu finden, wobei $\mathcal{S}_j^*$ die maximale zulässige Teilmenge von $\mathcal{P}_j$ ist. Die Gesamtzahl der Züge ist gegeben durch:
$$\text{MaxTrains} = \sum_{j=1}^P |\mathcal{S}_j^*|$$

## 2. Algebraische Charakterisierung

Das Problem zerlegt sich in $P$ unabhängige Instanzen des **Activity Selection Problem**. Sei für einen festen Bahnsteig $j$ die Menge $\mathcal{P}_j$ so indiziert, dass ihre Abfahrtszeiten nicht abnehmend sind: $d_{(1)} \le d_{(2)} \le \dots \le d_{(|\mathcal{P}_j|)}$.

Die Greedy-Choice-Eigenschaft für die Aktivitätsauswahl besagt, dass die Auswahl der Aktivität mit der frühesten Endzeit die maximal mögliche Zeit für nachfolgende Aktivitäten lässt. Sei $f(j, \tau)$ die maximale Anzahl an Zügen, die auf Bahnsteig $j$ geplant werden können, unter der Voraussetzung, dass der Bahnsteig zum Zeitpunkt $\tau$ verfügbar ist. Die Rekursionsgleichung lautet:

$$f(j, \tau) = \max \begin{cases} f(j, \tau) & \text{if } a_i < \tau \\ 1 + f(j, d_i) & \text{if } a_i \ge \tau \end{cases}$$

Für jeden Bahnsteig $j$ definieren wir die Greedy-Auswahlsequenz $S_j = \{s_1, s_2, \dots, s_k\}$, wobei:
1. $s_1 = \text{argmin}_{t \in \mathcal{P}_j} \{d_t\}$
2. $s_{m+1} = \text{argmin}_{t \in \mathcal{P}_j, a_t \ge d_{s_m}} \{d_t\}$

Die Optimalität dieser Greedy-Strategie wird durch das Austauschargument garantiert: Wenn eine optimale Lösung $\mathcal{O}_j$ nicht den Zug mit der frühesten Endzeit enthält, kann man den ersten Zug in $\mathcal{O}_j$ durch den am frühesten endenden Zug ersetzen, ohne die Zulässigkeitsbedingung zu verletzen, wodurch die Optimalität gewahrt bleibt.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus verläuft in drei Phasen:
1. **Bucketing:** Das Verteilen von $N$ Zügen in $P$ Listen benötigt $O(N)$ Zeit.
2. **Sortieren:** Für jeden Bahnsteig $j$ sortieren wir die Züge nach der Abfahrtszeit. Sei $n_j = |\mathcal{P}_j|$. Die Gesamtzeit für das Sortieren beträgt $\sum_{j=1}^P O(n_j \log n_j)$. Da $\sum n_j = N$ und $n_j \log n_j \le n_j \log N$ gilt, ist die Gesamtzeit beschränkt durch:
   $$\sum_{j=1}^P O(n_j \log N) = O(N \log N)$$
3. **Auswahl:** Das Iterieren durch die sortierten Listen benötigt $O(n_j)$ pro Bahnsteig, insgesamt $O(\sum n_j) = O(N)$.

Somit ergibt sich die gesamte Zeitkomplexität zu $O(N) + O(N \log N) + O(N) = O(N \log N)$.

### Platzkomplexität
1. **Zusätzlicher Speicher:** Wir speichern die Züge in einer 2D-Struktur (ein Array von Listen). Die Gesamtzahl der gespeicherten Elemente ist $N$, und die Struktur selbst benötigt $O(P)$ Pointer/Referenzen.
2. **Gesamtspeicher:** Die Platzkomplexität beträgt $O(N + P)$. Im Kontext von $N \ge P$ entspricht dies effektiv $O(N)$.