# Formale mathematische Spezifikation: Balancierte Klammern

## 1. Definitionen und Notation

Sei $\Sigma = \{'(', ')', '[', ']', '{', '}'\}$ das Alphabet der Klammerzeichen. Wir definieren die Menge der öffnenden Klammern als $\Sigma_{open} = \{'(', '[', '{'\}$ und die Menge der schließenden Klammern als $\Sigma_{close} = \{')', ']', '\}'\}$. 

Wir definieren eine Bijektion $\mu: \Sigma_{close} \to \Sigma_{open}$, die die Paarungsbeziehung darstellt:
$$\mu(')') = '(', \quad \mu(']') = '[', \quad \mu('\}') = '\{'$$

Sei $s = s_1 s_2 \dots s_n$ ein String der Länge $n$ mit $s_i \in \Sigma$. 
Der Zustand des Algorithmus wird durch einen Stack $\sigma \in \Sigma_{open}^*$ repräsentiert, wobei $\Sigma_{open}^*$ die Menge aller endlichen Sequenzen (Strings) über $\Sigma_{open}$ ist. Wir bezeichnen den leeren Stack als $\epsilon$. Die Operation $\text{push}(\sigma, c)$ bezeichnet die Konkatenation $\sigma \cdot c$ und $\text{pop}(\sigma)$ bezeichnet den Präfix $\sigma'$, sodass $\sigma = \sigma' \cdot x$ für ein $x \in \Sigma_{open}$ gilt.

Der Algorithmus definiert eine Funktion $f: \Sigma^* \to \{0, 1\}$, wobei $1$ einen gültigen (balancierten) String und $0$ einen ungültigen String bezeichnet.

## 2. Algebraische Charakterisierung

Die Gültigkeit des Strings $s$ wird durch die Zustandsübergangsfunktion $\delta: (\Sigma_{open}^*, \Sigma) \to \Sigma_{open}^* \cup \{\bot\}$ bestimmt, wobei $\bot$ einen ungültigen Zustand darstellt. Für ein Zeichen $c \in \Sigma$ und einen Stack $\sigma$:

$$\delta(\sigma, c) = 
\begin{cases} 
\sigma \cdot c & \text{if } c \in \Sigma_{open} \\
\sigma' & \text{if } c \in \Sigma_{close}, \sigma = \sigma' \cdot \mu(c) \\
\bot & \text{otherwise}
\end{cases}$$

**Schleifeninvariante:**
Sei $\sigma_i$ der Zustand des Stacks nach der Verarbeitung des Präfixes $s_{1 \dots i}$. Der Algorithmus ist korrekt genau dann, wenn:
1. Für alle $i \in \{1, \dots, n\}$ gilt $\sigma_i \neq \bot$.
2. $\sigma_n = \epsilon$.

Dies kann als ein Reduktionsprozess auf einer Dyck-Sprache $D_k$ betrachtet werden. Der String $s$ ist balanciert, wenn er zu der Sprache gehört, die durch die kontextfreie Grammatik $G = (V, \Sigma, R, S)$ mit $V=\{S\}$, $R=\{S \to SS, S \to (S), S \to [S], S \to \{S\}, S \to \epsilon\}$ erzeugt wird. Der Stack-basierte Algorithmus führt effektiv ein Bottom-Up-Parsing des Strings durch, um die Zugehörigkeit zu $L(G)$ zu überprüfen.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus verarbeitet jedes Zeichen $s_i$ im Eingabe-String genau einmal. Für jedes $s_i$ führt der Algorithmus folgende Schritte aus:
1. Einen Zugehörigkeitstest in $\Sigma_{open}$ oder $\Sigma_{close}$, was bei einer festen Alphabetgröße von $|\Sigma| = 6$ in $O(1)$ erfolgt.
2. Eine Stack-Operation ($\text{push}$ oder $\text{pop}$), was in einer standardmäßigen Array-basierten oder Linked List-Implementierung in $O(1)$ erfolgt.
3. Einen Dictionary-Lookup für $\mu(c)$, was in $O(1)$ erfolgt.

Die gesamte Zeitkomplexität $T(n)$ ist durch die Summe gegeben:
$$T(n) = \sum_{i=1}^{n} \Theta(1) = \Theta(n)$$
Somit ist der Algorithmus strikt $O(n)$.

### Platzkomplexität
Die Platzkomplexität $S(n)$ wird durch die maximale Tiefe des Stacks $\sigma$ bestimmt. Im schlechtesten Fall besteht der Eingabe-String ausschließlich aus öffnenden Klammern (z. B. $s = ('^n$), was erfordert, dass der Stack $n$ Elemente speichert. 

Der zusätzliche Speicherbedarf ist:
$$S(n) = \max_{0 \le i \le n} |\sigma_i|$$
Da $|\sigma_i| \le i$ gilt, haben wir $S(n) = O(n)$. 

Im besten Fall, in dem der String sofort ungültig ist (z. B. $s_1 \in \Sigma_{close}$), beträgt die Platzkomplexität $O(1)$. Die asymptotische obere Schranke bleibt jedoch $O(n)$, um den schlechtesten Fall zu berücksichtigen.