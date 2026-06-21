# Formale mathematische Spezifikation: Partition Equal Subset Sum

## 1. Definitionen und Notation

Sei $A = \{a_1, a_2, \dots, a_n\}$ eine Multimenge von $n$ positiven ganzen Zahlen, wobei $a_i \in \mathbb{Z}^+$. Wir definieren die Gesamtsumme der Multimenge als $S = \sum_{i=1}^n a_i$.

Das Ziel ist es, die Existenz einer Partition von $A$ in zwei disjunkte Teilmengen $A_1, A_2 \subset A$ zu bestimmen, sodass $A_1 \cup A_2 = A$, $A_1 \cap A_2 = \emptyset$ und $\sum_{x \in A_1} x = \sum_{y \in A_2} y$ gilt.

Sei die Zielsumme $T = \frac{S}{2}$. Das Problem ist äquivalent zur Bestimmung der Existenz einer Teilmenge $A_1 \subseteq A$, sodass $\sum_{x \in A_1} x = T$ gilt.

Wir definieren den Zustandsraum $\mathcal{S} = \{0, 1, \dots, T\}$. Sei $dp[s]$ ein boolesches Prädikat, definiert als:
$$dp[s] = \begin{cases} 1 & \text{falls } \exists A' \subseteq \{a_1, \dots, a_i\} \text{ existiert, sodass } \sum_{x \in A'} x = s \\ 0 & \text{sonst} \end{cases}$$

## 2. Algebraische Charakterisierung

### Notwendige Bedingung
Damit eine Partition existieren kann, muss die Gesamtsumme $S$ gerade sein. Wenn $S \equiv 1 \pmod 2$, dann impliziert $\sum_{x \in A_1} x = \sum_{y \in A_2} y$, dass $2 \sum_{x \in A_1} x = S$ gilt, was für ganzzahlige Summen einen Widerspruch darstellt. Somit ist die Lösung $\bot$ (Falsch), falls $S$ ungerade ist.

### Rekursionsgleichung
Unter der Annahme, dass $S$ gerade ist, definieren wir den Übergang für die Einbeziehung des $i$-ten Elements $a_i$. Sei $dp_i[s]$ die Erreichbarkeit der Summe $s$ unter Verwendung einer Teilmenge der ersten $i$ Elemente. Die Rekursionsgleichung lautet:
$$dp_i[s] = dp_{i-1}[s] \lor dp_{i-1}[s - a_i]$$
wobei $dp_i[s] = 0$ gilt, falls $s < 0$. Der Induktionsanfang ist $dp_0[0] = 1$ und $dp_0[s] = 0$ für $s > 0$.

### Invariante
Der Algorithmus erhält die Invariante aufrecht, dass nach der Verarbeitung des $i$-ten Elements die Menge der erreichbaren Summen $\mathcal{R}_i = \{s \in \mathcal{S} \mid dp_i[s] = 1\}$ folgende Bedingung erfüllt:
$$\mathcal{R}_i = \mathcal{R}_{i-1} \cup \{s + a_i \mid s \in \mathcal{R}_{i-1}, s + a_i \leq T\}$$
Der Algorithmus terminiert mit einer Lösung, wenn $T \in \mathcal{R}_n$ gilt.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus iteriert über $n$ Elemente. Für jedes Element $a_i$ führen wir einen linearen Durchlauf (oder eine Mengenaktualisierung) über den Bereich $[0, T]$ durch. 
Die Gesamtzahl der Operationen ist beschränkt durch:
$$T(n) = \sum_{i=1}^n \sum_{s=0}^T 1 = O(n \cdot T)$$
Durch Einsetzen von $T = \frac{S}{2}$ ergibt sich die Komplexität $O(n \cdot S)$. Im Schlechtesten Fall, in dem $S$ proportional zu $n \cdot \max(A)$ ist, beträgt die Komplexität $O(n^2 \cdot \max(A))$.

### Platzkomplexität
Durch die Verwendung eines 1D-Array (oder eines Bitsets) der Größe $T+1$ zur Speicherung der Erreichbarkeit jeder Summe vermeiden wir den Platzbedarf von $O(n \cdot T)$ der naiven 2D-DP-Tabelle.
Der benötigte zusätzliche Speicherplatz beträgt:
$$S(n) = O(T) = O\left(\frac{\sum_{i=1}^n a_i}{2}\right)$$
Da $T$ der Maximalwert ist, den wir verfolgen müssen, ist die Platzkomplexität strikt $O(S)$. In Bezug auf die Eingabeparameter entspricht dies $O(n \cdot \bar{a})$, wobei $\bar{a}$ der Durchschnittswert der Elemente in $A$ ist.