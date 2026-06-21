# Formale mathematische Spezifikation: Kachelproblem (2 x N Brett)

## 1. Definitionen und Notation

Sei $N \in \mathbb{N}_0$ die Breite eines Brettes der Dimension $2 \times N$. Wir definieren die Menge aller gültigen Kachelungen eines $2 \times N$ Brettes als $\mathcal{T}_N$. Das Ziel ist es, die Kardinalität dieser Menge zu bestimmen, bezeichnet als $f(N) = |\mathcal{T}_N|$.

Die verfügbaren Kacheln haben die Dimension $2 \times 1$ (Dominosteine). Eine Kachelung ist eine Partition des $2 \times N$ Gitters in $N$ disjunkte Mengen von Zellen, wobei jede Menge dem Bereich entspricht, der von einer einzelnen Kachel bedeckt wird.

Wir definieren den Definitionsbereich unserer Funktion wie folgt:
- $N \in \{0, 1, 2, \dots\}$
- $f: \mathbb{N}_0 \to \mathbb{N}_1$
- Modulo-Arithmetik: Alle Berechnungen werden im Ring $\mathbb{Z}_m$ durchgeführt, wobei $m = 10^9 + 7$.

## 2. Algebraische Charakterisierung

Das Problem weist eine optimale Substruktur auf, die es uns erlaubt, $f(N)$ über eine lineare homogene Rekursionsgleichung mit konstanten Koeffizienten zu definieren.

Betrachten wir die linke Spalte eines $2 \times N$ Brettes. Es gibt zwei sich gegenseitig ausschließende und erschöpfende Möglichkeiten, die Zellen $(1,1)$ und $(2,1)$ zu bedecken:

1. **Vertikale Platzierung:** Eine einzelne $2 \times 1$ Kachel bedeckt sowohl $(1,1)$ als auch $(2,1)$. Der verbleibende Bereich ist ein $2 \times (N-1)$ Brett, das auf $f(N-1)$ Arten gekachelt werden kann.
2. **Horizontale Platzierung:** Zwei $2 \times 1$ Kacheln werden horizontal platziert und bedecken $(1,1), (1,2)$ sowie $(2,1), (2,2)$. Der verbleibende Bereich ist ein $2 \times (N-2)$ Brett, das auf $f(N-2)$ Arten gekachelt werden kann.

Dies ergibt die Rekursionsgleichung:
$$f(N) = f(N-1) + f(N-2), \quad \forall N \ge 2$$

Mit den Induktionsanfängen:
- $f(0) = 1$ (Die leere Menge ist die eindeutige Kachelung eines $2 \times 0$ Brettes).
- $f(1) = 1$ (Nur eine vertikale Kachel ist möglich).

Dies ist isomorph zur Fibonacci-Folge $F_{n+1}$, wobei $F_0=0, F_1=1, F_2=1, F_3=2, \dots$. Somit gilt $f(N) = F_{N+1}$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus verwendet einen iterativen Ansatz, um das $N$-te Glied der Folge zu berechnen. Sei $T(N)$ die Anzahl der Operationen.
Der Algorithmus führt eine einzelne Schleife von $i = 2$ bis $N$ aus. Innerhalb jeder Iteration führen wir eine konstante Anzahl von Additionen und Zuweisungen in $\mathbb{Z}_m$ durch.

Der Gesamtaufwand ergibt sich aus der Summe:
$$T(N) = c_1 + \sum_{i=2}^{N} c_2 = \Theta(N)$$
wobei $c_1$ die Initialisierung und $c_2$ die arithmetischen Operationen konstanter Zeit pro Iteration repräsentiert. Somit ist die Zeitkomplexität $O(N)$.

### Platzkomplexität
Der Algorithmus verwaltet eine feste Anzahl von skalaren Variablen, um den Zustand der Rekursion zu speichern: $a$ (repräsentiert $f(i-2)$) und $b$ (repräsentiert $f(i-1)$).

Sei $S(N)$ die zusätzliche Platzkomplexität. Da der Speicherverbrauch unabhängig von der Eingabegröße $N$ ist, gilt:
$$S(N) = O(1)$$
Die Platzkomplexität ist strikt konstant, da wir unabhängig von der Größe von $N$ nur Speicher für zwei Ganzzahlen benötigen.