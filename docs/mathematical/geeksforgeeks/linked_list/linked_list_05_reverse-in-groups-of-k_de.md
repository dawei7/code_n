# Formale mathematische Spezifikation: Reverse Nodes in k-Group

## 1. Definitionen und Notation

Sei $L$ eine einfach verkettete Liste, definiert als eine Folge von Knoten $N = \{n_1, n_2, \dots, n_m\}$. Jeder Knoten $n_i$ ist ein Tupel $(v_i, p_i)$, wobei $v_i$ der Datenwert und $p_i \in N \cup \{\text{null}\}$ der Pointer auf den Nachfolgeknoten ist. Die Liste wird durch die geordnete Folge von Knoten $(n_1, n_2, \dots, n_m)$ repräsentiert, sodass $p(n_i) = n_{i+1}$ für $1 \le i < m$ und $p(n_m) = \text{null}$ gilt.

Sei $k \in \mathbb{Z}^+$ der Gruppierungsparameter. Wir definieren die Partitionierung von $L$ in zusammenhängende Segmente $S_j$ der Länge $k$:
$S_j = (n_{(j-1)k+1}, \dots, n_{jk})$ für $1 \le j \le \lfloor m/k \rfloor$.
Sei $R$ das Restsegment $R = (n_{\lfloor m/k \rfloor \cdot k + 1}, \dots, n_m)$, wobei $R = \emptyset$ gilt, falls $m \equiv 0 \pmod k$.

Die Transformationsfunktion $f: L \to L'$ bildet die ursprüngliche Liste auf eine modifizierte Liste $L'$ ab, in der jedes Segment $S_j$ umgekehrt wird, bezeichnet als $S_j^R = (n_{jk}, n_{jk-1}, \dots, n_{(j-1)k+1})$, während $R$ invariant bleibt. Die resultierende Liste $L'$ ist die Konkatenation:
$L' = S_1^R \oplus S_2^R \oplus \dots \oplus S_{\lfloor m/k \rfloor}^R \oplus R$.

## 2. Algebraische Charakterisierung

Der Algorithmus unterhält einen Zustand, der durch das Tupel $\sigma = (\text{prev\_tail}, \text{curr\_head}, \text{next\_group\_start})$ definiert ist.

**Schleifeninvariante:**
Zu Beginn jeder Iteration $j \in \{1, \dots, \lfloor m/k \rfloor\}$ ist die Liste in drei Segmente partitioniert:
1. Ein verarbeiteter Präfix $P_{j-1} = \bigoplus_{i=1}^{j-1} S_i^R$.
2. Ein unverarbeitetes Segment $U_j = S_j \oplus \dots \oplus S_{\lfloor m/k \rfloor} \oplus R$.
3. Die Invariante $\text{prev\_tail}$ zeigt auf den letzten Knoten von $S_{j-1}^R$.

**Übergangsfunktion:**
Für ein Segment $S_j = (a_1, a_2, \dots, a_k)$ ist die Umkehroperation $\rho(S_j)$ durch die Aktualisierung der Nachfolge-Pointer $p$ definiert:
$$\forall i \in \{2, \dots, k\}: p(a_i) = a_{i-1}$$
Die Verknüpfungsoperation im Schritt $j$ ist definiert als:
$$p(\text{prev\_tail}) = a_k$$
$$p(a_1) = \text{head}(S_{j+1})$$
wobei $\text{head}(S_{j+1})$ der erste Knoten des nachfolgenden Segments ist. Dies stellt sicher, dass die globale Konnektivität der Liste unter der lokalen Umkehrung von $S_j$ erhalten bleibt.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Sei $T(m)$ die Zeit, die zur Verarbeitung einer Liste der Länge $m$ benötigt wird. Der Algorithmus führt pro Knoten zwei verschiedene Operationen aus:
1. **Traversal:** Das Finden des $k$-ten Knotens erfordert $k$ Schritte. Dies wird $\lfloor m/k \rfloor$ Mal durchgeführt. Gesamtkosten: $\sum_{j=1}^{\lfloor m/k \rfloor} k = O(m)$.
2. **Umkehrung:** Das Umkehren von $k$ Pointern wird $\lfloor m/k \rfloor$ Mal durchgeführt. Gesamtkosten: $\sum_{j=1}^{\lfloor m/k \rfloor} k = O(m)$.

Die gesamte Zeitkomplexität beträgt:
$$T(m) = \sum_{j=1}^{\lfloor m/k \rfloor} (k + k) + |R| = 2 \cdot \lfloor m/k \rfloor \cdot k + (m \pmod k) = \Theta(m)$$
Da $m = N$, ist die Zeitkomplexität $O(N)$.

### Platzkomplexität
Der Algorithmus verwendet eine feste Menge an Pointern: $\{\text{dummy}, \text{prev\_group\_tail}, \text{kth}, \text{prev}, \text{curr}, \text{next\_node}\}$.
Sei $S_{aux}$ der zusätzliche Speicherplatz. Da die Anzahl der Pointer unabhängig von $N$ und $k$ ist:
$$S_{aux} = \sum_{i=1}^{c} \text{sizeof}(\text{pointer}) = O(1)$$
Der Algorithmus arbeitet in-place und modifiziert nur die existierenden Pointer-Felder $p_i$ der Knoten $n_i$. Somit beträgt die gesamte zusätzliche Platzkomplexität $O(1)$.