# Formale mathematische Spezifikation: Two Sum

## 1. Definitionen und Notation

Sei $A = (a_0, a_1, \dots, a_{n-1})$ eine Folge von Ganzzahlen der Länge $n \in \mathbb{N}$, wobei $a_i \in \mathbb{Z}$ für alle $i \in \{0, 1, \dots, n-1\}$ gilt. Sei $T \in \mathbb{Z}$ die Zielsumme (Target Sum).

Wir definieren die Lösungsmenge $\mathcal{S}$ als die Menge der Indexpaare $(i, j)$, für die gilt:
$$\mathcal{S} = \{ (i, j) \in \mathbb{N}^2 \mid 0 \le i < j < n \land a_i + a_j = T \}$$

Das Problem garantiert die Existenz einer eindeutigen Lösung, sodass $|\mathcal{S}| = 1$ gilt. Sei $(i^*, j^*)$ das eindeutige Element von $\mathcal{S}$.

Wir definieren eine partielle Abbildung $M_k: \mathbb{Z} \to \{0, 1, \dots, k-1\}$, die den Zustand der Hash Map nach $k$ Iterationen des Algorithmus repräsentiert, wobei $M_k(v) = i$ gilt, falls $a_i = v$ und $i < k$. Falls kein solches $i$ existiert, ist $M_k(v)$ undefiniert.

## 2. Algebraische Charakterisierung

Der Algorithmus iteriert über den Index $k \in \{0, \dots, n-1\}$. In jedem Schritt $k$ definieren wir das Komplement $c_k = T - a_k$. Der Algorithmus erhält die folgende Schleifeninvariante aufrecht:

**Invariante:** Zu Beginn der Iteration $k$ enthält die Map $M_k$ alle Elemente $\{a_0, a_1, \dots, a_{k-1}\}$, sodass für jedes $v \in \{a_0, \dots, a_{k-1}\}$ gilt: $M_k(v) = \max \{i \mid a_i = v, i < k\}$.

Die Übergangsfunktion für den Zustand $M$ ist definiert als:
$$M_{k+1}(v) = 
\begin{cases} 
k & \text{falls } v = a_k \\
M_k(v) & \text{sonst}
\end{cases}$$

Der Algorithmus terminiert beim kleinsten Index $j^*$, für den ein $i^* < j^*$ existiert, das $a_{i^*} + a_{j^*} = T$ erfüllt. Formal gibt der Algorithmus $(i^*, j^*)$ zurück, wobei:
$$j^* = \min \{ k \in \{0, \dots, n-1\} \mid (T - a_k) \in \text{dom}(M_k) \}$$
$$i^* = M_{j^*}(T - a_{j^*})$$

Da das Problem eine eindeutige Lösung garantiert, ist die Existenz von $j^*$ durch die Existenz von $(i^*, j^*) \in \mathcal{S}$ gesichert.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus führt einen einzigen Durchlauf über das Eingabe-Array $A$ aus. Für jeden Index $k \in \{0, \dots, n-1\}$ führt der Algorithmus folgende Operationen aus:
1. Eine Subtraktion: $T - a_k$ (konstante Zeit, $O(1)$).
2. Ein Hash Map Lookup: $M_k(c_k)$ (erwartet $O(1)$).
3. Eine bedingte Einfügung: $M_{k+1}(a_k) \leftarrow k$ (erwartet $O(1)$).

Die gesamte Zeitkomplexität $T(n)$ ergibt sich aus der Summation:
$$T(n) = \sum_{k=0}^{j^*} O(1) = O(j^*) \subseteq O(n)$$
Im Schlechtesten Fall, in dem sich das Lösungspaar am Ende des Arrays befindet, gilt $j^* = n-1$, was eine scharfe Schranke von $\Theta(n)$ ergibt.

### Platzkomplexität
Die Platzkomplexität $S(n)$ wird durch den zusätzlichen Speicherbedarf der Hash Map $M$ bestimmt. Im Schlechtesten Fall kann der Algorithmus $n-1$ Elemente speichern, bevor das Komplement gefunden wird.

Die Platzkomplexität beträgt:
$$S(n) = \text{space}(\text{map}) + O(1) = O(n)$$
wobei die Map höchstens $n-1$ Schlüssel-Wert-Paare $(a_i, i)$ speichert. Somit beträgt die zusätzliche Platzkomplexität $\Theta(n)$.