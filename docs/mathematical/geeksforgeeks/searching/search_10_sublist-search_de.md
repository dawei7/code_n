# Formale mathematische Spezifikation: Sublist Search

## 1. Definitionen und Notation

Sei $L$ eine einfach verkettete Liste, definiert als eine geordnete Sequenz von Knoten $N = \{n_0, n_1, \dots, n_{n-1}\}$, wobei jeder Knoten $n_i$ einen Wert $v_i \in \Sigma$ (wobei $\Sigma$ ein endliches Alphabet ist) und einen Pointer auf den Nachfolgeknoten $n_{i+1}$ enthält. Wir bezeichnen die Länge der Hauptliste als $n = |L|$ und die Länge der Sublist $S$ als $m = |S|$, wobei $S = \{s_0, s_1, \dots, s_{m-1}\}$.

- **Eingabebereich:** Die Menge aller Paare $(L, S)$, sodass $L$ und $S$ einfach verkettete Listen sind.
- **Ausgabebereich:** Die boolesche Menge $\mathbb{B} = \{True, False\}$.
- **Zustandsraum:** Die Konfiguration des Algorithmus zu einem beliebigen Schritt $k$ ist definiert durch das Tupel $\mathcal{S}_k = (p_{first}, p_{main}, p_{sub})$, wobei $p_{first} \in L \cup \{\text{null}\}$, $p_{main} \in L \cup \{\text{null}\}$ und $p_{sub} \in S \cup \{\text{null}\}$.
- **Matching-Prädikat:** Wir definieren eine Übereinstimmung der Länge $m$, beginnend am Index $i$ in $L$, als die Bedingung:
  $$\forall j \in \{0, \dots, m-1\} : \text{val}(n_{i+j}) = \text{val}(s_j)$$

## 2. Algebraische Charakterisierung

Der Algorithmus bestimmt die Existenz einer zusammenhängenden Teilsequenz durch Auswertung des Prädikats $P(L, S)$:
$$P(L, S) \iff \exists i \in \{0, \dots, n-m\} \text{ s.t. } \bigwedge_{j=0}^{m-1} (\text{val}(n_{i+j}) = \text{val}(s_j))$$

### Schleifeninvarianten
Sei $i$ der Index des Knotens, auf den $p_{first}$ zeigt. Zu Beginn jeder Iteration der äußeren Schleife gilt die folgende Invariante:
1. **Fortschrittsinvariante:** Für alle $k < i$ ist die Sublist $S$ kein Präfix der Sublist von $L$, die bei $n_k$ beginnt.
2. **Abbruchbedingung:** Der Algorithmus terminiert, wenn $i > n - m$ (Rückgabe von $False$) oder wenn die innere Schleife $\forall j \in \{0, \dots, m-1\}, \text{val}(n_{i+j}) = \text{val}(s_j)$ erfüllt (Rückgabe von $True$).

Die Übergangsfunktion für die Pointer ist definiert als:
- **Äußerer Schritt:** $p_{first} \leftarrow \text{next}(p_{first})$
- **Innerer Schritt:** Wenn $\text{val}(p_{main}) = \text{val}(p_{sub})$, dann $(p_{main}, p_{sub}) \leftarrow (\text{next}(p_{main}), \text{next}(p_{sub}))$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität $T(n, m)$ wird durch die verschachtelte Traversierung der Listen bestimmt. Im Schlechtesten Fall führt die innere Schleife für jede Startposition $i \in \{0, \dots, n-m\}$ $m$ Vergleiche durch, bevor sie fehlschlägt.

Die Gesamtzahl der Operationen $W$ ergibt sich aus der Summation:
$$W = \sum_{i=0}^{n-m} \sum_{j=0}^{m-1} \mathbb{I}(\text{match}) \leq \sum_{i=0}^{n-m} m = (n - m + 1) \cdot m$$

Asymptotisch, für $n, m \to \infty$:
$$T(n, m) = O((n-m+1) \cdot m) = O(n \cdot m)$$
Der Bestfall tritt ein, wenn der erste Knoten von $L$ mit dem ersten Knoten von $S$ übereinstimmt und die Übereinstimmung entweder sofort gefunden wird oder an der ersten Position fehlschlägt, was je nach Implementierung $\Omega(m)$ oder $\Omega(1)$ ergibt.

### Platzkomplexität
Der Algorithmus verwaltet eine konstante Anzahl von Pointern ($p_{first}, p_{main}, p_{sub}$), unabhängig von der Eingabegröße $n$ oder $m$.

Sei $S_{aux}$ der zusätzliche Speicherplatz:
$$S_{aux} = \mathcal{O}(1)$$
Da keine zusätzlichen Datenstrukturen (wie Hash Maps oder Rekursions-Stacks) verwendet werden, die mit der Eingabe skalieren, beträgt die Platzkomplexität strikt $O(1)$.