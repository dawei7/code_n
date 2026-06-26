# Formale mathematische Spezifikation: Median aus einem Datenstrom finden

## 1. Definitionen und Notation

Sei $\mathcal{S} = \{x_1, x_2, \dots, x_n\}$ eine Folge von Ganzzahlen, die aus einem Datenstrom eintreffen, wobei $n$ die Anzahl der zum Zeitpunkt $t$ verarbeiteten Elemente bezeichnet. Sei $\mathcal{S}_{(1)} \le \mathcal{S}_{(2)} \le \dots \le \mathcal{S}_{(n)}$ die geordnete Permutation der Multimenge $\mathcal{S}$.

Der Median $M$ der Multimenge $\mathcal{S}$ ist definiert als:
$$M = \begin{cases} \mathcal{S}_{(\frac{n+1}{2})} & \text{falls } n \text{ ungerade ist} \\ \frac{1}{2} \left( \mathcal{S}_{(\frac{n}{2})} + \mathcal{S}_{(\frac{n}{2} + 1)} \right) & \text{falls } n \text{ gerade ist} \end{cases}$$

Wir definieren zwei disjunkte Mengen, $L$ (die "untere" Hälfte) und $R$ (die "obere" Hälfte), sodass $L \cup R = \mathcal{S}$ und $L \cap R = \emptyset$. Diese Mengen werden über zwei Priority Queues verwaltet:
1. $H_{max}$: Ein Max-Heap, der Elemente von $L$ speichert, wobei $\forall l \in L, l \le \max(L)$.
2. $H_{min}$: Ein Min-Heap, der Elemente von $R$ speichert, wobei $\forall r \in R, r \ge \min(R)$.

## 2. Algebraische Charakterisierung

Die Korrektheit des Algorithmus wird durch die folgenden drei Invarianten bestimmt, die nach jeder Operation aufrechterhalten werden:

**I. Werteintegrität:**
$$\forall l \in L, \forall r \in R : l \le r$$
Dies impliziert, dass $\max(L) \le \min(R)$.

**II. Größenbalance:**
Die Kardinalität der Mengen muss folgende Bedingung erfüllen:
$$|L| = |R| \quad \text{oder} \quad |L| = |R| + 1$$
Dies stellt sicher, dass der Median jederzeit über die Wurzeln der Heaps zugänglich ist.

**III. Median-Extraktion:**
Unter Berücksichtigung der Invarianten wird der Median $M$ wie folgt berechnet:
$$M = \begin{cases} \text{root}(H_{max}) & \text{falls } |L| > |R| \\ \frac{\text{root}(H_{max}) + \text{root}(H_{min})}{2} & \text{falls } |L| = |R| \end{cases}$$

**Zustandsübergang für `addNum(x)`:**
Seien $L_i, R_i$ die Zustände vor dem Einfügen. Der Übergang folgt diesen Schritten:
1. Temporäres Einfügen: $L' \leftarrow L \cup \{x\}$ (falls $x \le \max(L)$), andernfalls $R \cup \{x\}$.
2. Ausbalancieren: Falls $|L'| > |R'| + 1$, verschiebe $\max(L')$ nach $R'$. Falls $|R'| > |L'|$, verschiebe $\min(R')$ nach $L'$.
Dies stellt sicher, dass die Invariante der Größenbalance in $O(\log n)$ Zeit wiederhergestellt wird.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Seien $T_{push}(k)$ und $T_{pop}(k)$ die Zeitkomplexität der Heap-Operationen für einen Heap der Größe $k$. Für einen binären Heap gilt $T_{push}, T_{pop} = \Theta(\log k)$.

Die `addNum`-Operation führt eine konstante Anzahl an Heap-Operationen aus (höchstens 2 Pushes und 2 Pops). Somit ergibt sich die gesamte Zeitkomplexität pro Einfügung zu:
$$T_{add} = O(\log |L|) + O(\log |R|) = O(\log n)$$
Die `findMedian`-Operation führt eine konstante Anzahl an Wurzelzugriffen aus:
$$T_{find} = \Theta(1)$$
Die amortisierte Zeitkomplexität über $N$ Operationen beträgt $O(N \log N)$.

### Platzkomplexität
Der Algorithmus speichert jedes Element des Datenstroms genau einmal, entweder in $H_{max}$ oder in $H_{min}$.
Sei $S_{heap}(k)$ der für einen Heap mit $k$ Elementen benötigte Speicherplatz, welcher $\Theta(k)$ beträgt.
Die gesamte Platzkomplexität ist:
$$S_{total} = S(H_{max}) + S(H_{min}) = \Theta(|L|) + \Theta(|R|) = \Theta(n)$$
wobei $n$ die Gesamtzahl der verarbeiteten Elemente ist. Der zusätzliche Speicherplatz (exklusive der Eingabespeicherung) beträgt ebenfalls $\Theta(n)$, da die Heaps persistieren müssen, um den Median-Zustand zu erhalten.