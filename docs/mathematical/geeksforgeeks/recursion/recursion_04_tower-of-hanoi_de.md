# Formale mathematische Spezifikation: Turm von Hanoi

## 1. Definitionen und Notation

Sei $N \in \mathbb{N}^+$ die Anzahl der Scheiben, wobei jeder Scheibe $d \in \{1, 2, \dots, N\}$ eine eindeutige Größe zugewiesen ist, sodass $d_i < d_j$ gilt, falls $i < j$.

Wir definieren den Zustandsraum $\mathcal{S}$ als die Menge aller gültigen Konfigurationen von Scheiben auf drei Stäben, bezeichnet durch die Menge $\mathcal{R} = \{S, D, A\}$ (Source, Destination, Auxiliary). Eine Konfiguration ist eine Abbildung $f: \{1, \dots, N\} \to \mathcal{R}$, sodass für jeden Stab $r \in \mathcal{R}$ die dem Stab $r$ zugewiesenen Scheiben nach Größe geordnet sind. Dies erfüllt die Bedingung, dass für $d_i, d_j \in r$ mit $i < j$ die Scheibe $d_i$ oberhalb von $d_j$ platziert sein muss.

- **Eingabe:** Eine Ganzzahl $N$ und eine Permutation der Stäbe $(src, dst, aux) \in \mathcal{R}^3$.
- **Ausgabe:** Eine Sequenz von Zügen $M = (m_1, m_2, \dots, m_k)$, wobei jeder Zug $m_i = (r_{from}, r_{to})$ den Transfer der obersten Scheibe vom Stab $r_{from}$ zum Stab $r_{to}$ darstellt.
- **Bedingung:** Für jeden Zug $(r_{from}, r_{to})$ muss die bewegte Scheibe $d_{top}$ die Bedingung $d_{top} < d_{target}$ erfüllen, wobei $d_{target}$ die aktuell oberste Scheibe auf $r_{to}$ ist (oder $d_{target} = \infty$, falls $r_{to}$ leer ist).

## 2. Algebraische Charakterisierung

Der Turm von Hanoi wird durch eine rekursive Funktionalgleichung bestimmt. Sei $H(n, src, dst, aux)$ die Sequenz von Zügen, die erforderlich ist, um einen Stack von $n$ Scheiben von $src$ nach $dst$ unter Verwendung von $aux$ als Hilfsstab zu transferieren.

Der Algorithmus ist durch die folgende rekursive Zerlegung definiert:

$$
H(n, src, dst, aux) = 
\begin{cases} 
\emptyset & \text{if } n = 0 \\
H(n-1, src, aux, dst) \oplus \{(src, dst)\} \oplus H(n-1, aux, dst, src) & \text{if } n > 0 
\end{cases}
$$

wobei $\oplus$ die Konkatenation von Zugsequenzen bezeichnet.

**Korrektheitsinvariante:**
Für jedes $n$ bewahrt die Sequenz $H(n, src, dst, aux)$ die Eigenschaft, dass zu keinem Zeitpunkt eine größere Scheibe auf eine kleinere Scheibe gelegt wird. Durch vollständige Induktion gilt: Wenn $H(n-1)$ gültig ist, dann ist auch $H(n)$ gültig, da:
1. Die $n-1$ Scheiben nach $aux$ bewegt werden, wodurch Scheibe $n$ (die größte) frei wird.
2. Scheibe $n$ nach $dst$ bewegt wird, welcher leer ist oder nur Scheiben $> n$ enthält.
3. Die $n-1$ Scheiben von $aux$ nach $dst$ bewegt werden, wo sie auf Scheibe $n$ platziert werden, wodurch die Invariante der Größenordnung gewahrt bleibt.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Sei $T(n)$ die Anzahl der Züge, die erforderlich sind, um das Problem für $n$ Scheiben zu lösen. Aus der in Abschnitt 2 definierten Rekursionsgleichung erhalten wir die lineare inhomogene Rekurrenz:
$$T(n) = 2T(n-1) + 1, \quad T(1) = 1$$

Unter Verwendung der Iterationsmethode oder der charakteristischen Gleichung ergibt sich:
$$T(n) + 1 = 2(T(n-1) + 1)$$
Sei $S(n) = T(n) + 1$. Dann gilt $S(n) = 2S(n-1)$ mit $S(1) = 2$.
Dies ist eine geometrische Folge $S(n) = 2^n$.
Daraus folgt $T(n) = 2^n - 1$.

Da jeder Zug konstante Zeit $O(1)$ für die Ausgabe oder Speicherung benötigt, ist die gesamte Zeitkomplexität:
$$T(n) = \Theta(2^n) = O(2^n)$$

### Platzkomplexität
Die Platzkomplexität wird durch die maximale Tiefe des Rekursions-Stacks bestimmt.
- **Stack-Platz:** Die Funktion $H(n, \dots)$ ruft $H(n-1, \dots)$ auf, bevor sie zurückkehrt. Die Tiefe des Rekursionsbaums beträgt $N$. Somit ist der zusätzliche Stack-Platz $O(N)$.
- **Ausgabe-Platz:** Wenn die Sequenz der Züge im Speicher gespeichert wird, beträgt der benötigte Platz $O(2^N)$, um die $2^N - 1$ Züge zu halten. In der Standard-Algorithmenanalyse betrachten wir jedoch den zusätzlichen Platz, der für die Ausführung des Algorithmus erforderlich ist, welcher $O(N)$ beträgt.

Daher ist die zusätzliche Platzkomplexität $O(N)$.