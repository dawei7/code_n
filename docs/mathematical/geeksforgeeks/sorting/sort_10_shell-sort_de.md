# Formale mathematische Spezifikation: Shell Sort

## 1. Definitionen und Notation

Sei $A = (a_0, a_1, \dots, a_{n-1})$ eine Sequenz von $n$ Elementen aus einer total geordneten Menge $(\mathcal{X}, \le)$. Das Ziel des Shell-Sort-Algorithmus ist es, eine Permutation $A'$ von $A$ zu erzeugen, sodass $a'_0 \le a'_1 \le \dots \le a'_{n-1}$ gilt.

Wir definieren eine **Gap-Sequenz** $H = (h_k, h_{k-1}, \dots, h_1)$ als eine streng monoton fallende Folge positiver ganzer Zahlen, wobei $h_1 = 1$ und $h_k < n$ gilt.

Für ein festes Gap $h \in H$ definieren wir eine **$h$-sortierte Sequenz** als eine Sequenz, bei der jede Teilsequenz von Elementen an den Indizes $\{i, i+h, i+2h, \dots\}$ für alle $0 \le i < h$ sortiert ist.

## 2. Algebraische Charakterisierung

Shell Sort arbeitet durch die Durchführung einer Sequenz von $h$-Sortierungen für abnehmende Werte von $h \in H$. Der Algorithmus hält die folgende Schleifeninvariante aufrecht:

**Invariante:** Nach Abschluss eines $h$-Sortierdurchlaufs mit dem Gap $h_m$ ist das Array $A$ $h_m$-sortiert.

Der Übergang zwischen den Zuständen wird durch das Insertion-Sort-Verfahren gesteuert, das auf $h$-verschachtelte Teilsequenzen angewendet wird. Für ein gegebenes Gap $h$ transformiert der Algorithmus $A$ in ein $h$-sortiertes Array unter Verwendung der folgenden Aktualisierungsregel für jedes $i \in \{h, h+1, \dots, n-1\}$:

Sei $temp = a_i$. Wir finden den größten Index $j \in \{i, i-h, i-2h, \dots\}$ derart, dass $j \ge h$ und $a_{j-h} > temp$. Wir führen dann die Verschiebung durch:
$$a_j \leftarrow a_{j-h}$$
Dieser Prozess wiederholt sich, bis die Bedingung $a_{j-h} \le temp$ oder $j < h$ erfüllt ist; an diesem Punkt setzen wir $a_j = temp$.

Die Korrektheit des Algorithmus beruht auf dem **Shell-Metzner-Theorem**, welches besagt, dass eine Sequenz, die $h_i$-sortiert und anschließend $h_j$-sortiert wurde, $h_i$-sortiert bleibt, falls $h_i$ ein Vielfaches von $h_j$ ist. Da das finale Gap $h_1 = 1$ ein Teiler aller ganzen Zahlen ist, garantiert der letzte Durchlauf, dass das Array $1$-sortiert ist, was äquivalent dazu ist, vollständig sortiert zu sein.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität $T(n)$ reagiert sehr empfindlich auf die Wahl der Gap-Sequenz $H$.

1. **Schlechtester Fall (Worst-Case):** Für die ursprüngliche Shell-Sequenz $h_i = \lfloor n/2^i \rfloor$ beträgt die Komplexität im schlechtesten Fall $\Theta(n^2)$. Dies geschieht, weil die Gaps nicht teilerfremd sind, was zu einem unzureichenden Informationsaustausch zwischen den Teilsequenzen führt.
2. **Hibbard-Sequenz:** Bei Verwendung von $H = \{2^k - 1 \mid 2^k - 1 < n\}$ ist die Komplexität durch $O(n^{3/2})$ beschränkt.
3. **Sedgewick-Sequenz:** Bei Verwendung von $H = \{4^k + 3 \cdot 2^{k-1} + 1\}$ beträgt die Komplexität $O(n^{4/3})$.

Der Gesamtaufwand $W$ ist die Summe der Arbeit, die bei jedem Gap $h$ verrichtet wird:
$$T(n) = \sum_{h \in H} W_h$$
Wobei $W_h$ die Kosten für das $h$-Sortieren sind. Für ein nahezu sortiertes Array gilt $W_h \approx O(n)$, aber im allgemeinen Fall ist $W_h$ durch die Anzahl der Inversionen in den $h$-verschachtelten Teilsequenzen beschränkt. Die Effizienz ergibt sich daraus, dass das $h$-Sortieren die Anzahl der Inversionen signifikant reduziert, sodass der letzte Durchlauf ($h=1$) auf einer Sequenz mit $O(n)$ Inversionen operiert, was eine Zeitkomplexität von $O(n)$ für den letzten Schritt ergibt.

### Platzkomplexität
Der Algorithmus arbeitet strikt in-place. Der Zustandsraum $\mathcal{S}$ besteht aus dem Eingabe-Array $A$ und einer konstanten Anzahl an Hilfsvariablen (dem aktuellen Gap $h$, den Schleifenindizes $i, j$ und dem temporären Speicher $temp$).

Die zusätzliche Platzkomplexität $S(n)$ beträgt:
$$S(n) = O(1)$$
Da der Speicherbedarf nicht mit der Eingabegröße $n$ skaliert, wird Shell Sort als ein Algorithmus mit $O(1)$ zusätzlichem Platzbedarf klassifiziert.