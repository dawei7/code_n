# Formale mathematische Spezifikation: Min-Stack

## 1. Definitionen und Notation

Sei $\mathcal{V} \subseteq \mathbb{Z}$ der Wertebereich der Werte, die im Stack gespeichert werden können. Wir definieren den Zustand des Min-Stacks als eine Folge von Paaren $S = \langle (v_1, m_1), (v_2, m_2), \dots, (v_k, m_k) \rangle$, wobei $k \in \mathbb{N}_0$ die aktuelle Anzahl der Elemente im Stack bezeichnet.

- **Zustandsraum:** Der Zustandsraum $\mathcal{S}$ ist definiert als die Menge aller endlichen Folgen von Paaren in $\mathcal{V} \times \mathcal{V}$.
- **Haupt-Stack ($M$):** Eine Projektion auf die erste Komponente, $M = \langle v_1, v_2, \dots, v_k \rangle$, die die LIFO-Reihenfolge der Elemente darstellt.
- **Min-Stack ($N$):** Eine Projektion auf die zweite Komponente, $N = \langle m_1, m_2, \dots, m_k \rangle$, wobei $m_i$ den minimalen Wert im Präfix des Haupt-Stacks bis zum Index $i$ darstellt.
- **Operationen:**
    - $\text{push}: \mathcal{S} \times \mathcal{V} \to \mathcal{S}$
    - $\text{pop}: \mathcal{S} \to \mathcal{S}$
    - $\text{top}: \mathcal{S} \to \mathcal{V}$
    - $\text{getMin}: \mathcal{S} \to \mathcal{V}$

## 2. Algebraische Charakterisierung

Die Korrektheit des Min-Stacks wird durch die induktive Definition des Minimalwerts bei jeder Tiefe $k$ bestimmt.

**Induktionsanfang:**
Für einen leeren Stack $S_0 = \langle \rangle$ sind die Operationen undefiniert (oder geben einen Fehler zurück).

**Induktionsschritt:**
Gegeben sei ein Stack $S_k = \langle (v_1, m_1), \dots, (v_k, m_k) \rangle$:

1. **Push-Operation:** Für einen Wert $x \in \mathcal{V}$ ist der neue Zustand $S_{k+1}$:
   $$S_{k+1} = S_k \oplus (x, m_{k+1}) \quad \text{where} \quad m_{k+1} = \min(x, m_k)$$
   (Mit $m_0 = \infty$ für den Anfangszustand).

2. **Pop-Operation:** Der Zustand $S_{k-1}$ wird durch das Abschneiden der Folge erhalten:
   $$S_{k-1} = \langle (v_1, m_1), \dots, (v_{k-1}, m_{k-1}) \rangle$$

3. **Top-Operation:**
   $$\text{top}(S_k) = v_k$$

4. **GetMin-Operation:**
   $$\text{getMin}(S_k) = m_k$$

**Invariante:**
Für alle $i \in \{1, \dots, k\}$ erfüllt der Wert $m_i$:
$$m_i = \min_{1 \le j \le i} \{v_j\}$$
Diese Invariante wird durch die Definition von $m_{k+1} = \min(v_{k+1}, m_k)$ aufrechterhalten, was effektiv das globale Minimum des Präfixes $\{v_1, \dots, v_{k+1}\}$ an die Spitze des Hilfs-Stacks propagiert.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Sei $T_{op}$ die Zeitkomplexität einer Operation.
- **Push:** Die Operation beinhaltet einen Vergleich $\min(x, m_k)$ und ein Anhängen an zwei Folgen. Da dies $O(1)$-Operationen in einem dynamischen Array (amortisiert) sind, gilt $T_{\text{push}} = O(1)$.
- **Pop:** Die Operation beinhaltet das Entfernen vom Ende zweier Folgen. $T_{\text{pop}} = O(1)$.
- **Top/GetMin:** Diese Operationen beinhalten einen einzelnen Indexzugriff auf das Ende der Folge (z. B. $S[k]$). Folglich gilt $T_{\text{top}} = O(1)$ und $T_{\text{getMin}} = O(1)$.

Da alle Operationen unabhängig von der Gesamtzahl der Elemente $n$ sind, die sich aktuell im Stack befinden, beträgt die Gesamtzeitkomplexität für eine Sequenz von $m$ Operationen $O(m)$.

### Platzkomplexität
Die Platzkomplexität wird durch die Speicherung der Folgen $M$ und $N$ bestimmt.
- **Gesamtplatz:** Wir speichern $k$ Paare von Integern. Der benötigte Platz beträgt $S(k) = 2k \cdot \text{sizeof}(\text{int})$.
- **Asymptotischer Platz:** Wenn $k$ auf $n$ anwächst (die maximale Anzahl der gepushten Elemente), beträgt die Platzkomplexität $O(n)$.
- **Hilfsplatz:** Der Algorithmus benötigt $O(n)$ Hilfsplatz, um den `min_stack` neben dem `main_stack` zu verwalten. Selbst wenn er auf einen einzelnen Stack von Tupeln optimiert wird, bleibt der Platzbedarf bei $\Theta(n)$, um den Verlauf der Minima zu bewahren, der für ein $O(1)$-Rollback erforderlich ist.