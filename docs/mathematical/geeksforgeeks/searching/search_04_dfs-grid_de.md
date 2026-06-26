# Formale mathematische Spezifikation: Tiefensuche (DFS) auf einem Gitter

## 1. Definitionen und Notation

Sei das Gitter durch eine Matrix $G \in \{0, 1\}^{R \times C}$ repräsentiert, wobei $R$ die Anzahl der Zeilen und $C$ die Anzahl der Spalten ist. Die Menge aller Zellen ist definiert als $\mathcal{V} = \{ (r, c) \mid 0 \le r < R, 0 \le c < C \}$.

Wir definieren eine Zusammenhangsrelation $\sim$ auf $\mathcal{V}$, sodass zwei Zellen $u = (r_1, c_1)$ und $v = (r_2, c_2)$ genau dann benachbart sind, wenn $|r_1 - r_2| + |c_1 - c_2| = 1$ gilt. Eine Insel ist definiert als eine Zusammenhangskomponente des Teilgraphen, der durch die Menge der Landzellen $\mathcal{L} = \{ v \in \mathcal{V} \mid G_v = 1 \}$ induziert wird.

Sei $\mathcal{I} = \{I_1, I_2, \dots, I_k\}$ die Partition von $\mathcal{L}$ in disjunkte Zusammenhangskomponenten. Das Ziel ist es, die Kardinalität der Menge der Komponenten, $k = |\mathcal{I}|$, zu berechnen.

Der Zustand des Algorithmus zu einem beliebigen Zeitpunkt $t$ ist durch das Tupel $(G_t, \mathcal{V}_{visited})$ definiert, wobei $G_t$ das modifizierte Gitter und $\mathcal{V}_{visited} \subseteq \mathcal{V}$ die Menge der bereits verarbeiteten Zellen ist.

## 2. Algebraische Charakterisierung

Der Algorithmus beruht auf der Eigenschaft, dass die Anzahl der Zusammenhangskomponenten $k$ in einem ungerichteten Graphen durch die Anzahl der Male bestimmt werden kann, die eine Traversierung (DFS) von einem unbesuchten Knoten aus initiiert wird.

Sei $f: \mathcal{V} \to \{0, 1\}$ die Indikatorfunktion für Landzellen. Wir definieren den rekursiven DFS-Operator $\Phi$, der auf eine Zelle $u \in \mathcal{L}$ wirkt:
$$\Phi(u) = \{u\} \cup \bigcup_{v \in Adj(u), G_v=1} \Phi(v)$$
wobei $Adj(u) = \{v \in \mathcal{V} \mid \|u - v\|_1 = 1\}$. 

Um die Terminierung sicherzustellen und Zyklen zu vermeiden, erzwingt der Algorithmus einen Zustandsübergang $G_{t+1} = G_t \setminus \{u\}$ (wobei $G_u = 0$ gesetzt wird), sobald $u$ besucht wird. Die Gesamtzahl der Inseln $k$ ergibt sich aus der Summe:
$$k = \sum_{r=0}^{R-1} \sum_{c=0}^{C-1} \mathbb{I}(G_{(r,c)}^{(initial)} = 1 \land \text{is\_start}(r, c))$$
wobei $\mathbb{I}$ die Indikatorfunktion ist und $\text{is\_start}(r, c)$ genau dann wahr ist, wenn die Zelle $(r, c)$ durch die Hauptschleife erreicht wird, bevor sie durch einen rekursiven Aufruf $\Phi$ erreicht wurde.

Die während der gesamten Ausführung aufrechterhaltene Schleifeninvariante lautet:
$$\text{Count} + \text{Components}(\mathcal{L} \setminus \mathcal{V}_{visited}) = k$$
wobei $\text{Count}$ die Anzahl der bisher identifizierten Inseln ist.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität leitet sich aus der Gesamtzahl der auf dem Gitter durchgeführten Operationen ab. 
1. Die Hauptschleife iteriert über jede Zelle $(r, c) \in \mathcal{V}$, was zu $R \times C$ Iterationen führt.
2. Die DFS-Traversierung $\Phi$ wird nur aufgerufen, wenn $G_{(r,c)} = 1$. 
3. Jede Zelle $v \in \mathcal{L}$ wird genau einmal durch die DFS besucht, da sie unmittelbar nach dem Besuch auf $0$ gesetzt wird. 
4. Für jede besuchte Zelle untersuchen wir ihre 4 Nachbarn.

Der Gesamtaufwand $W$ beträgt:
$$W = \sum_{v \in \mathcal{V}} (\text{konstanter Aufwand}) + \sum_{v \in \mathcal{L}} (\text{degree}(v) \times \text{konstanter Aufwand})$$
Da $\sum_{v \in \mathcal{L}} \text{degree}(v) \le 4|\mathcal{L}| \le 4(R \times C)$, ist die gesamte Zeitkomplexität:
$$T(R, C) = O(R \times C)$$

### Platzkomplexität
Die Platzkomplexität wird maßgeblich durch den Rekursions-Stack (oder den expliziten Stack bei einer iterativen Implementierung) bestimmt.
1. **Zusätzlicher Speicherplatz:** Im Schlechtesten Fall ist das Gitter eine einzige Zusammenhangskomponente (z. B. ein schlangenförmiger Pfad, der alle $R \times C$ Zellen abdeckt). Die Tiefe des Rekursionsbaums beträgt $O(R \times C)$.
2. **Gesamtspeicherplatz:** Da wir das Gitter in-place modifizieren, beträgt der Speicherbedarf für das Gitter $O(R \times C)$. Der zusätzliche Stack-Speicherplatz beträgt $O(R \times C)$.

Somit ist die gesamte Platzkomplexität:
$$S(R, C) = O(R \times C)$$
Im Bestfall, wenn das Gitter kein Land enthält, beträgt die Platzkomplexität $O(1)$ zuzüglich des Eingabespeichers.