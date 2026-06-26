# Formale mathematische Spezifikation: Sieb des Eratosthenes

## 1. Definitionen und Notation

Sei $\mathbb{N} = \{0, 1, 2, \dots\}$ die Menge der natürlichen Zahlen. Gegeben eine Zielzahl $N \in \mathbb{N}$, definieren wir das Ziel als die Identifikation der Menge der Primzahlen $\mathcal{P}_N \subseteq \{2, 3, \dots, N\}$, sodass gilt:
$$\mathcal{P}_N = \{p \in \mathbb{N} : 2 \le p \le N \land \forall a, b \in \mathbb{N}, p = ab \implies a=1 \lor b=1\}$$

Wir definieren einen Zustandsraum $\mathcal{S} = \{0, 1\}^{N+1}$, repräsentiert durch einen booleschen Vektor $\mathbf{v} = (v_0, v_1, \dots, v_N)$, wobei $v_i = 1$ bedeutet, dass $i$ ein Primzahlkandidat ist, und $v_i = 0$ bedeutet, dass $i$ zusammengesetzt ist. Der Algorithmus fungiert als Transformation $T: \mathcal{S} \to \mathcal{S}$, die die Menge der Kandidaten iterativ verfeinert.

## 2. Algebraische Charakterisierung

Der Algorithmus beruht auf dem Fundamentalsatz der Arithmetik, welcher impliziert, dass jede zusammengesetzte Zahl $n \le N$ einen Primfaktor $p \le \sqrt{N}$ besitzen muss.

**Initialisierung:**
Der Anfangszustand $\mathbf{v}^{(0)}$ ist definiert als:
$$v_i^{(0)} = \begin{cases} 1 & \text{if } i \ge 2 \\ 0 & \text{if } i < 2 \end{cases}$$

**Iterative Verfeinerung:**
Sei $\mathcal{P}_{\sqrt{N}} = \{p \in \mathbb{N} : p \le \sqrt{N}, v_p^{(k)} = 1\}$ die Menge der Primzahlen, die bis zur Schranke $\lfloor \sqrt{N} \rfloor$ identifiziert wurden. Für jedes $p \in \mathcal{P}_{\sqrt{N}}$ definieren wir den Sieb-Operator $\sigma_p$, der auf den Zustandsvektor $\mathbf{v}$ wirkt:
$$\sigma_p(\mathbf{v})_i = \begin{cases} 0 & \text{if } i \in \{kp : k \in \mathbb{N}, k \ge p\} \\ v_i & \text{otherwise} \end{cases}$$

Der Endzustand $\mathbf{v}^*$ ist die Komposition dieser Operatoren:
$$\mathbf{v}^* = \left( \prod_{p \le \sqrt{N}, p \in \mathcal{P}} \sigma_p \right) \mathbf{v}^{(0)}$$
Die Menge der Primzahlen wird dann als $\mathcal{P}_N = \{i \in \{0, \dots, N\} : v_i^* = 1\}$ rekonstruiert.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Gesamtzahl der Operationen $T(N)$ ist proportional zur Anzahl der Ausführungen der inneren Schleife. Für jede Primzahl $p \le \sqrt{N}$ führt die innere Schleife $\frac{N}{p} - p + 1$ Zuweisungen durch. Summiert über alle Primzahlen $p \le \sqrt{N}$ ergibt sich:
$$T(N) = \sum_{p \le \sqrt{N}} \left( \frac{N}{p} \right) = N \sum_{p \le \sqrt{N}} \frac{1}{p}$$

Nach dem zweiten Mertensschen Theorem ist die Summe der Kehrwerte der Primzahlen bis $x$ gegeben durch:
$$\sum_{p \le x} \frac{1}{p} = \ln(\ln x) + M + O\left(\frac{1}{\ln x}\right)$$
wobei $M$ die Meissel-Mertens-Konstante ist. Durch Einsetzen von $x = \sqrt{N}$ erhalten wir:
$$T(N) = N \left( \ln(\ln \sqrt{N}) + M \right) = N \left( \ln\left(\frac{1}{2} \ln N\right) + M \right)$$
Da $\ln(\frac{1}{2} \ln N) = \ln(\ln N) - \ln 2$, ist der führende Term $N \ln(\ln N)$. Somit gilt $T(N) = O(N \log \log N)$.

### Platzkomplexität
Der Algorithmus verwaltet ein boolesches Array der Größe $N+1$. Jedes Element $v_i$ benötigt konstanten Speicherplatz $O(1)$ (typischerweise 1 Bit oder 1 Byte, abhängig von der Implementierung).
$$S(N) = \sum_{i=0}^{N} \text{space}(v_i) = (N+1) \cdot O(1) = O(N)$$
Der zusätzliche Speicherbedarf wird durch den booleschen Vektor dominiert, was zu einer gesamten Platzkomplexität von $O(N)$ führt.