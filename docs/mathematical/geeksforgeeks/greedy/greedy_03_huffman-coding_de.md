# Formale mathematische Spezifikation: Huffman-Kodierung

## 1. Definitionen und Notation

Sei $\Sigma = \{c_1, c_2, \dots, c_n\}$ ein endliches Alphabet von $n$ eindeutigen Symbolen. Jedem Symbol $c_i \in \Sigma$ ist eine Wahrscheinlichkeit oder Häufigkeit $f_i \in \mathbb{R}^+$ zugeordnet. Wir definieren die Eingabe als eine Menge von Paaren $S = \{(c_1, f_1), (c_2, f_2), \dots, (c_n, f_n)\}$.

Ein **binärer Code** ist eine Funktion $C: \Sigma \to \{0, 1\}^*$, wobei $\{0, 1\}^*$ die Menge aller binären Strings endlicher Länge ist. Die Länge des Codeworts für das Symbol $c_i$ wird mit $\ell_i = |C(c_i)|$ bezeichnet.

Das Ziel ist die Konstruktion eines **präfixfreien Codes** (oder unverzüglich dekodierbaren Codes), der die Kraft-Ungleichung erfüllt und die Bedingung, dass für beliebige $c_i, c_j \in \Sigma$ mit $i \neq j$, $C(c_i)$ kein Präfix von $C(c_j)$ ist. Dies wird durch einen Binärbaum $T$ dargestellt, wobei:
- Jeder Blattknoten genau einem $c_i \in \Sigma$ entspricht.
- Der Pfad von der Wurzel zum Blatt $c_i$ das Codewort $C(c_i)$ definiert, wobei ein linker Zweig '0' und ein rechter Zweig '1' entspricht.

Die **erwartete Codelänge** $L(T)$ ist definiert als:
$$L(T) = \sum_{i=1}^{n} f_i \cdot \ell_i$$
Das Ziel ist es, einen Baum $T^*$ zu finden, sodass $L(T^*) = \min_{T \in \mathcal{T}} L(T)$, wobei $\mathcal{T}$ die Menge aller möglichen Binärbäume mit $n$ Blättern ist.

## 2. Algebraische Charakterisierung

Der Huffman-Algorithmus konstruiert $T$ bottom-up unter Verwendung einer Greedy-Strategie basierend auf der folgenden Rekurrenz. Sei $\mathcal{F}$ ein Wald von Bäumen. Zu Beginn ist $\mathcal{F} = \{T_1, \dots, T_n\}$, wobei jeder $T_i$ ein einzelner Knoten mit dem Gewicht $w(T_i) = f_i$ ist.

**Greedy-Choice-Eigenschaft:**
In jedem Schritt wählen wir zwei Bäume $T_a, T_b \in \mathcal{F}$ aus, deren Gewichte minimal sind:
$$w(T_a) = \min_{T \in \mathcal{F}} w(T), \quad w(T_b) = \min_{T \in \mathcal{F} \setminus \{T_a\}} w(T)$$
Wir bilden einen neuen Baum $T_{new}$ mit den Kindern $T_a$ und $T_b$ und dem Gewicht:
$$w(T_{new}) = w(T_a) + w(T_b)$$
Die Aktualisierungsregel für den Wald lautet $\mathcal{F} \leftarrow (\mathcal{F} \setminus \{T_a, T_b\}) \cup \{T_{new}\}$. Dieser Prozess wiederholt sich, bis $|\mathcal{F}| = 1$.

**Optimalitätsinvariante:**
Der Huffman-Algorithmus erhält die Invariante aufrecht, dass der Wald $\mathcal{F}_k$ zu jedem Schritt $k$ aus optimalen präfixfreien Bäumen für die aktuelle Menge an Gewichten besteht. Nach dem **Huffman-Shannon-Fano-Theorem** ist die Greedy-Wahl, die zwei Knoten mit der geringsten Häufigkeit zu verschmelzen, optimal, da sie die gewichtete Pfadlänge des resultierenden Baums minimiert und die Rekurrenz erfüllt:
$$L(T_{new}) = L(T_a) + L(T_b) + w(T_a) + w(T_b)$$
wobei die zusätzlichen Kosten $w(T_a) + w(T_b)$ den Zuwachs der Pfadlänge für alle Blätter darstellen, die in den verschmolzenen Teilbäumen enthalten sind.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Ausführung des Algorithmus wird maßgeblich durch die Operationen der Priority Queue bestimmt.
1. **Initialisierung:** Der Aufbau des anfänglichen Min-Heaps aus $n$ Elementen benötigt $O(n)$ Zeit unter Verwendung des Heap-Konstruktionsalgorithmus von Floyd.
2. **Iteration:** Der Algorithmus führt $n-1$ Iterationen durch. In jeder Iteration:
   - Werden zwei `extract-min`-Operationen durchgeführt: $2 \cdot O(\log n) = O(\log n)$.
   - Wird eine `insert`-Operation durchgeführt: $O(\log n)$.
   - Der Gesamtaufwand pro Iteration beträgt $O(\log n)$.
3. **Gesamtzeit:** Die gesamte Zeitkomplexität $T(n)$ ergibt sich zu:
   $$T(n) = O(n) + \sum_{k=1}^{n-1} O(\log(n-k+1)) = O(n) + O(n \log n) = O(n \log n)$$

### Platzkomplexität
1. **Heap-Speicher:** Die Priority Queue speichert zu jedem Zeitpunkt höchstens $n$ Knoten, was $O(n)$ Platz erfordert.
2. **Baumstruktur:** Der resultierende Huffman-Baum enthält $n$ Blattknoten und $n-1$ innere Knoten, insgesamt $2n-1$ Knoten. Jeder Knoten speichert eine konstante Menge an Daten (Häufigkeit, Pointer), was $O(n)$ Platz erfordert.
3. **Ausgabe-Dictionary:** Das Speichern der Abbildung von $n$ Zeichen auf ihre jeweiligen binären Strings erfordert $O(n \cdot \bar{\ell})$ Platz, wobei $\bar{\ell}$ die durchschnittliche Codewortlänge ist. Da $\bar{\ell} \leq n$, ist der Platzbedarf im Schlechtesten Fall (ein degenerierter Baum) durch $O(n^2)$ begrenzt, typischerweise jedoch $O(n \log n)$ für balancierte Bäume. Bei der Standardimplementierung beträgt der zusätzliche Platzbedarf $O(n)$.