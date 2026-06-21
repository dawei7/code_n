# Formale mathematische Spezifikation: Prüfung auf balancierte Bäume

## 1. Definitionen und Notation
Ein Binärbaum $T$ ist höhenbalanciert, wenn und nur wenn für jeden Knoten $x \in V$ die Höhendifferenz zwischen seinen Teilbäumen um höchstens 1 begrenzt ist.

## 2. Algebraische Charakterisierung
Wir werten das Prädikat $\mathcal{B}(T) \in \{\text{True}, \text{False}\}$ aus:
$$ \mathcal{B}(T) \iff \forall x \in V, |\mathcal{H}(x_L) - \mathcal{H}(x_R)| \leq 1 $$

Sei $f: \mathcal{T} \to \mathbb{Z}$ eine Funktion, die die Höhe eines balancierten Baumes berechnet und $-1$ zurückgibt, falls der Baum nicht balanciert ist:
$$ f(T) = \begin{cases}
0 & \text{falls } T = \emptyset \\
-1 & \text{falls } f(T_L) = -1 \lor f(T_R) = -1 \\
-1 & \text{falls } |f(T_L) - f(T_R)| > 1 \\
1 + \max(f(T_L), f(T_R)) & \text{andernfalls}
\end{cases} $$

Dann gilt $\mathcal{B}(T) \iff f(T) \neq -1$.

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** Da $f(T)$ sowohl die Höhe als auch den Balancierungsstatus gleichzeitig in einem einzigen Post-Order-Durchlauf berechnet, ist die Zeitkomplexität strikt $O(|V|)$.
- **Platzkomplexität:** $O(\mathcal{H}(T))$.