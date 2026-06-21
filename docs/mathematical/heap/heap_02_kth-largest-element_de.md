# Formale mathematische Spezifikation: K-th Largest Element

## 1. Definitionen und Notation

Sei $A = \langle a_1, a_2, \dots, a_N \rangle$ eine Sequenz von $N$ Ganzzahlen, wobei $a_i \in \mathbb{Z}$. Wir definieren die sortierte Version von $A$ als eine nicht-fallende Sequenz $S = \langle s_1, s_2, \dots, s_N \rangle$, sodass $s_1 \le s_2 \le \dots \le s_N$ gilt. Das $k$-größte Element von $A$ ist definiert als das Element $s_{N-k+1}$.

Sei $\mathcal{H}$ eine Min-Heap-Datenstruktur, ein vollständiger Binärbaum, der die Heap-Eigenschaft erfüllt: Für jeden Knoten $u$ mit den Kindern $v_L$ und $v_R$ gilt $val(u) \le \min(val(v_L), val(v_R))$.
- Sei $|\mathcal{H}|$ die Anzahl der Elemente im Heap.
- Sei $top(\mathcal{H})$ das Element mit dem kleinsten Wert in $\mathcal{H}$, welches sich an der Wurzel befindet.
- Sei $push(\mathcal{H}, x)$ die Operation zum Einfügen von $x$ in $\mathcal{H}$ in $O(\log |\mathcal{H}|)$ Zeit.
- Sei $pop(\mathcal{H})$ die Operation zum Entfernen von $top(\mathcal{H})$ in $O(\log |\mathcal{H}|)$ Zeit.

## 2. Algebraische Charakterisierung

Der Algorithmus hält einen Zustand $\mathcal{H}_i$ nach der Verarbeitung des $i$-ten Elements von $A$ aufrecht. Die Invariante $\mathcal{I}$ ist wie folgt definiert:
$\mathcal{H}_i$ enthält die $k$ größten Elemente, die im Präfix $\langle a_1, \dots, a_i \rangle$ für $i \ge k$ angetroffen wurden.

**Übergangsfunktion:**
Für jedes $a_i \in A$:
1. Wenn $|\mathcal{H}| < k$:
   $$\mathcal{H}_{i} = \mathcal{H}_{i-1} \cup \{a_i\}$$
2. Wenn $|\mathcal{H}| = k$ und $a_i > top(\mathcal{H}_{i-1})$:
   $$\mathcal{H}_{i} = (\mathcal{H}_{i-1} \setminus \{top(\mathcal{H}_{i-1})\}) \cup \{a_i\}$$
3. Andernfalls:
   $$\mathcal{H}_{i} = \mathcal{H}_{i-1}$$

**Korrektheitsinvariante:**
Bei Beendigung des Algorithmus ($i=N$) erfüllt die Menge $\mathcal{H}_N$:
$$\forall x \in \mathcal{H}_N, \forall y \in \{A \setminus \mathcal{H}_N\}, x \ge y$$
Da $|\mathcal{H}_N| = k$ gilt, ist das kleinste Element dieser Menge das $k$-größte Element der ursprünglichen Sequenz $A$:
$$result = \min(\mathcal{H}_N) = s_{N-k+1}$$

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus führt einen einzigen Durchlauf über die Eingabesequenz $A$ der Länge $N$ aus. Für jedes Element $a_i$ führen wir höchstens eine $push$- und eine $pop$-Operation auf einem Heap der maximalen Größe $k$ aus.

Die Kosten jeder Heap-Operation sind durch $O(\log k)$ beschränkt. Die gesamte Zeitkomplexität $T(N, k)$ ergibt sich aus der Summe:
$$T(N, k) = \sum_{i=1}^{N} \text{cost}(op_i) \le \sum_{i=1}^{N} O(\log k) = O(N \log k)$$
Da die Heap-Operationen logarithmisch in Bezug auf die Größe des Heaps $k$ sind, ist die obere Schranke strikt $O(N \log k)$.

### Platzkomplexität
Die Platzkomplexität $S(N, k)$ wird durch den zusätzlichen Speicherbedarf für den Min-Heap $\mathcal{H}$ bestimmt.
- Der Heap ist auf eine maximale Größe von $k$ Elementen beschränkt.
- Jedes Element belegt $O(1)$ Speicherplatz.
- Somit beträgt die zusätzliche Platzkomplexität $O(k)$.

Die gesamte Platzkomplexität ist $O(k)$, was unabhängig von $N$ ist, wodurch dieser Ansatz optimal für Streaming-Daten ist, bei denen $N \gg k$ gilt.