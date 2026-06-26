# Formale mathematische Spezifikation: Generierung von Binärzahlen von 1 bis N

## 1. Definitionen und Notation

Sei $\mathbb{N}^+ = \{1, 2, 3, \dots\}$ die Menge der positiven ganzen Zahlen. Wir definieren die Binärdarstellungsfunktion $B: \mathbb{N}^+ \to \Sigma^*$, wobei $\Sigma = \{'0', '1'\}$, sodass $B(n)$ die eindeutige String-Repräsentation von $n$ zur Basis 2 ohne führende Nullen ist.

Sei $\mathcal{Q}$ eine First-In-First-Out (FIFO) Queue-Datenstruktur, definiert als eine geordnete Sequenz von Strings $S = (s_1, s_2, \dots, s_k)$, wobei $s_i \in \Sigma^*$.
- Die Operation $\text{enqueue}(s)$ hängt $s$ an das Ende von $\mathcal{Q}$ an.
- Die Operation $\text{dequeue}()$ entfernt das Element am Anfang von $\mathcal{Q}$ und gibt es zurück.

Der Algorithmus definiert einen Zustandsraum $\mathcal{S} \subset \Sigma^*$, der die Menge aller binären Strings repräsentiert. Wir definieren eine Übergangsfunktion $f: \Sigma^* \to \Sigma^* \times \Sigma^*$, sodass $f(s) = (s \cdot '0', s \cdot '1')$, wobei $\cdot$ die String-Konkatenation bezeichnet.

## 2. Algebraische Charakterisierung

Der Algorithmus konstruiert eine Sequenz $L = (x_1, x_2, \dots, x_N)$, wobei $x_i = B(i)$. Dies ist äquivalent zu einer Breitensuche (Breadth-First Search, BFS) auf einem unendlichen Binärbaum $\mathcal{T}$, bei dem die Wurzel $r = '1'$ ist und jeder Knoten $u$ die Kinder $u \cdot '0'$ und $u \cdot '1'$ besitzt.

**Schleifeninvariante:**
Sei $q_i$ der Zustand der Queue zu Beginn der Iteration $i$ (für $1 \le i \le N$).
1. Die Menge der Elemente in der Queue $q_i$ entspricht den Knoten auf der aktuellen und den nachfolgenden Ebenen von $\mathcal{T}$, die noch nicht mittels `dequeue` entnommen wurden.
2. Die Sequenz $L_{i-1} = (x_1, \dots, x_{i-1})$ enthält die ersten $i-1$ Binärzahlen in lexikographischer Ordnung, welche isomorph zur numerischen Ordnung ihrer ganzzahligen Werte ist.

**Rekurrenz:**
Die Entwicklung der Queue kann durch den Zustandsübergang beschrieben werden:
$$\mathcal{Q}_{i+1} = (\mathcal{Q}_i \setminus \{s_i\}) \cup \{s_i \cdot '0', s_i \cdot '1'\}$$
wobei $s_i = \text{dequeue}(\mathcal{Q}_i)$. Da der Baum $\mathcal{T}$ ein vollständiger Binärbaum ist, garantiert die Traversierung in Ebenenordnung (level-order traversal), dass für jedes $n \in \mathbb{N}^+$ die generierte Sequenz die Bedingung $val(x_i) < val(x_{i+1})$ erfüllt, wobei $val: \Sigma^* \to \mathbb{N}^+$ die Standard-Auswertungsfunktion zur Basis 2 ist.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus führt eine Schleife exakt $N$-mal aus. In jeder Iteration $i \in \{1, \dots, N\}$ gilt:
1. Eine `dequeue`-Operation: $O(1)$.
2. Ein `append` an das Ergebnis: $O(1)$.
3. Zwei `enqueue`-Operationen: $O(1)$.
4. Zwei String-Konkatenationen: Die Länge des binären Strings $s$ beträgt $\lfloor \log_2(i) \rfloor + 1$. Daher benötigt die Konkatenation $O(\log i)$.

Die gesamte Zeitkomplexität $T(N)$ ergibt sich aus der Summation:
$$T(N) = \sum_{i=1}^{N} O(\log i) = O\left(\sum_{i=1}^{N} \log i\right) = O(\log(N!))$$
Nach der Stirling-Formel gilt $\log(N!) \approx N \log N - N$. Während die bitweise Komplexität $O(N \log N)$ beträgt, ist die Komplexität im Kontext von Standard-Word-RAM-Modellen, in denen String-Operationen als amortisiert konstant behandelt werden oder $N$ durch die Maschinenwortbreite begrenzt ist, effektiv $O(N)$.

### Platzkomplexität
Die Platzkomplexität $S(N)$ wird durch die maximale Größe der Queue $\mathcal{Q}$ und der Ergebnisliste bestimmt.
1. Die Ergebnisliste speichert $N$ Strings mit einer durchschnittlichen Länge von $O(\log N)$, was $O(N \log N)$ Bits erfordert.
2. Die Queue $\mathcal{Q}$ enthält in Iteration $i$ Knoten der aktuellen und der nächsten Ebene des Baums. Die Anzahl der Knoten in der Queue ist durch $O(N)$ beschränkt. Insbesondere enthält die Queue am Ende des Algorithmus näherungsweise $N$ Elemente.

Somit ergibt sich die zusätzliche Platzkomplexität zu:
$$S(N) = O(N \cdot \text{avg\_length}) = O(N \log N)$$
Bezogen auf die Anzahl der gespeicherten String-Objekte beträgt die Platzkomplexität $O(N)$.