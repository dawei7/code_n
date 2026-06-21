# Formale mathematische Spezifikation: Floyd-Warshall (Dynamische Programmierung)

## 1. Definitionen und Notation

Sei $G = (V, E)$ ein gerichteter, gewichteter Graph, wobei $V = \{0, 1, \dots, n-1\}$ die Menge der $n$ Knoten ist. Sei $w: E \to \mathbb{R}$ eine Gewichtsfunktion, die jeder Kante einen reellen Wert zuweist. Wir definieren die Adjacency Matrix $W \in (\mathbb{R} \cup \{\infty\})^{n \times n}$ wie folgt:

$$
W_{ij} = 
\begin{cases} 
0 & \text{falls } i = j \\
w(i, j) & \text{falls } (i, j) \in E \\
\infty & \text{falls } i \neq j \text{ und } (i, j) \notin E 
\end{cases}
$$

Wir definieren den Zustandsraum $\mathcal{S}$ als eine Folge von Matrizen $D^{(k)} \in (\mathbb{R} \cup \{\infty\})^{n \times n}$ für $k \in \{-1, 0, \dots, n-1\}$. Jeder Eintrag $D^{(k)}_{ij}$ repräsentiert das Gewicht des kürzesten Pfades vom Knoten $i$ zum Knoten $j$ unter Verwendung von ausschließlich Zwischenknoten aus der Menge $V_k = \{0, 1, \dots, k\}$.

## 2. Algebraische Charakterisierung

Der Algorithmus basiert auf dem Optimalitätsprinzip. Wir definieren die Rekursionsgleichung für die kürzeste Pfaddistanz $D^{(k)}_{ij}$ wie folgt:

**Induktionsanfang ($k = -1$):**
Der kürzeste Pfad ohne Verwendung von Zwischenknoten ist einfach das direkte Kantengewicht:
$$D^{(-1)}_{ij} = W_{ij}$$

**Induktionsschritt ($k \geq 0$):**
Für jedes $k \in \{0, \dots, n-1\}$ ist der kürzeste Pfad von $i$ nach $j$ unter Verwendung von Zwischenknoten in $V_k$ das Minimum aus dem kürzesten Pfad, der den Knoten $k$ nicht verwendet, und dem kürzesten Pfad, der durch den Knoten $k$ verläuft:
$$D^{(k)}_{ij} = \min\left( D^{(k-1)}_{ij}, D^{(k-1)}_{ik} + D^{(k-1)}_{kj} \right)$$

**Korrektheitsinvariante:**
Der Algorithmus erhält die Invariante aufrecht, dass $D^{(k)}_{ij}$ nach der $k$-ten Iteration das Gewicht des kürzesten Pfades von $i$ nach $j$ enthält, wobei nur Knoten aus $\{0, \dots, k\}$ als Zwischenknoten verwendet werden. Durch vollständige Induktion repräsentiert $D^{(n-1)}_{ij}$ für $k = n-1$ den kürzesten Pfad zwischen allen Paaren $(i, j)$ in $G$, vorausgesetzt, es existieren keine Zyklen mit negativem Gewicht. Falls ein Zyklus mit negativem Gewicht existiert, liefert der Algorithmus $D^{(n-1)}_{ii} < 0$ für mindestens ein $i$.

**Platzoptimierung:**
Da $D^{(k)}_{ij}$ nur von Werten aus $D^{(k-1)}$ abhängt, können wir das Update in-place durchführen. Sei $D$ die Matrix $D^{(k-1)}$. Das Update $D_{ij} \leftarrow \min(D_{ij}, D_{ik} + D_{kj})$ ist gültig, weil:
1. $D_{ik}$ und $D_{kj}$ während der $k$-ten Iteration unverändert bleiben (da $D_{ik} = D^{(k-1)}_{ik} = D^{(k)}_{ik}$ und $D_{kj} = D^{(k-1)}_{kj} = D^{(k)}_{kj}$).
2. Die Werte $D_{ik}$ und $D_{kj}$ Pfade repräsentieren, die $k$ nicht als Zwischenknoten verwenden, was die Anforderung für die Rekursionsgleichung erfüllt.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus besteht aus drei verschachtelten Schleifen, die jeweils über die Menge der Knoten $V$ iterieren. Die Gesamtzahl der Operationen wird durch die dreifache Summation bestimmt:
$$T(n) = \sum_{k=0}^{n-1} \sum_{i=0}^{n-1} \sum_{j=0}^{n-1} \Theta(1)$$
Auswertung dieser Summation:
$$T(n) = \sum_{k=0}^{n-1} \sum_{i=0}^{n-1} n = \sum_{k=0}^{n-1} n^2 = n^3$$
Somit beträgt die Zeitkomplexität $O(V^3)$.

### Platzkomplexität
Der Algorithmus verwaltet zwei primäre $n \times n$ Matrizen: die Distanzmatrix $D$ und die Vorgängermatrix $nxt$.
- Die Distanzmatrix $D$ benötigt $O(V^2)$ Platz.
- Die Vorgängermatrix $nxt$ benötigt $O(V^2)$ Platz.
- Hilfsvariablen (Schleifenindizes, temporäre Skalare) benötigen $O(1)$ Platz.

Die gesamte Platzkomplexität beträgt $O(V^2 + V^2) = O(V^2)$. Die In-place-Optimierung stellt sicher, dass wir nicht den $O(V^3)$ Platz benötigen, der durch das Speichern des vollständigen 3D-Tensors $D^{(k)}_{ij}$ erforderlich wäre.