# Formale mathematische Spezifikation: Top K Frequent Elements

## 1. Definitionen und Notation

Sei $A = [a_1, a_2, \dots, a_N]$ eine Sequenz von $N$ Integern aus einer Domäne $\mathcal{D} \subset \mathbb{Z}$.
Sei $U = \{u_1, u_2, \dots, u_M\}$ die Menge der eindeutigen Elemente in $A$, wobei $M = |U| \leq N$ gilt.

Wir definieren die Häufigkeitsfunktion $f: U \to \mathbb{Z}^+$ als:
$$f(u) = \sum_{i=1}^{N} \mathbb{I}(a_i = u)$$
wobei $\mathbb{I}(\cdot)$ die Indikatorfunktion ist.

Das Ziel ist es, eine Teilmenge $S \subset U$ zu identifizieren, sodass $|S| = k$ (für $1 \leq k \leq M$) und die Bedingung erfüllt ist, dass für alle $u \in S$ und $v \in U \setminus S$ gilt: $f(u) \geq f(v)$.

Das Ergebnis ist eine Menge $S = \{s_1, s_2, \dots, s_k\}$, welche die $k$ Elemente mit den höchsten Häufigkeiten in $A$ repräsentiert.

## 2. Algebraische Charakterisierung

### Häufigkeitsabbildung
Der Algorithmus konstruiert zunächst die Häufigkeits-Map $\mathcal{M} = \{(u, f(u)) \mid u \in U\}$. Dies ist eine bijektive Abbildung von der Menge der eindeutigen Elemente auf ihre jeweiligen Anzahlen.

### Heap-basierte Selektion (Min-Heap-Invariante)
Für den Heap-basierten Ansatz verwalten wir eine Min-Priority Queue $\mathcal{H}$ der Größe $k$. Sei $\mathcal{H}_i$ der Zustand des Heaps nach der Verarbeitung von $i$ eindeutigen Elementen. Der Heap speichert Paare $(f(u), u)$. Die aufrechterhaltene Invariante lautet:
$$\forall (f_a, u_a) \in \mathcal{H}, \forall (f_b, u_b) \in (\mathcal{M} \setminus \mathcal{H}), f_a \geq \min_{(f, u) \in \mathcal{H}} f \implies f_b \leq f_a$$
Nach Abschluss enthält $\mathcal{H}$ die $k$ Elemente mit den größten Werten von $f(u)$.

### Bucket-Sort-Formulierung
Wir definieren eine Sammlung von Buckets $\mathcal{B} = \{B_0, B_1, \dots, B_N\}$, wobei jeder Bucket $B_i$ eine Menge ist:
$$B_i = \{u \in U \mid f(u) = i\}$$
Der Algorithmus konstruiert $\mathcal{B}$ so, dass $\bigcup_{i=0}^N B_i = U$ und $B_i \cap B_j = \emptyset$ für $i \neq j$ gilt. Die Ergebnismenge $S$ wird durch Konkatenation der Elemente aus $B_i$ in absteigender Reihenfolge des Index $i$ konstruiert:
$$S = \bigcup_{i=N}^{1} B_i \quad \text{s.t. } |S| = k$$

## 3. Komplexitätsanalyse

### Zeitkomplexität
**Heap-Ansatz:**
1. **Häufigkeitszählung:** Das Iterieren durch $A$ benötigt $O(N)$ Zeit.
2. **Heap-Operationen:** Wir führen $M$ Einfügungen in einen Heap der maximalen Größe $k$ durch. Jede Einfüge-/Löschoperation benötigt $O(\log k)$. Die Gesamtzeit beträgt:
   $$T(N) = O(N) + \sum_{i=1}^{M} O(\log k) = O(N + M \log k)$$
   Da $M \leq N$ gilt, ist die Komplexität $O(N \log k)$.

**Bucket-Sort-Ansatz:**
1. **Häufigkeitszählung:** $O(N)$.
2. **Bucket-Befüllung:** Das Iterieren über $M$ eindeutige Elemente, um sie in Buckets einzuordnen, benötigt $O(M)$.
3. **Bucket-Durchlauf:** Das Iterieren durch $N+1$ Buckets benötigt $O(N)$.
   $$T(N) = O(N) + O(M) + O(N) = O(N)$$
   Der Algorithmus ist strikt linear, da die Anzahl der Buckets durch die Eingabegröße $N$ begrenzt ist.

### Platzkomplexität
Die Platzkomplexität wird durch die Speicherung der Häufigkeits-Map und der Hilfsstrukturen (Heap oder Buckets) dominiert.
1. **Häufigkeits-Map:** Speichert $M$ eindeutige Elemente, was $O(M)$ Platz erfordert.
2. **Heap/Buckets:** 
   - Der Heap speichert $k$ Elemente: $O(k)$.
   - Die Buckets speichern $M$ Elemente über $N+1$ Listen hinweg: $O(N + M)$.
   
Unter der Annahme $M \leq N$ und $k \leq N$ ist die gesamte zusätzliche Platzkomplexität:
$$S(N) = O(N + M) = O(N)$$
Somit arbeitet der Algorithmus mit linearem Platzbedarf relativ zur Eingabegröße.