# Formale mathematische Spezifikation: Infix-zu-Postfix-Konvertierung

## 1. Definitionen und Notation

Sei $\Sigma$ ein endliches Alphabet, das aus drei disjunkten Mengen besteht:
1. $\mathcal{O} = \{+, -, *, /\}$ (die Menge der binären Operatoren).
2. $\mathcal{P} = \{(, )\}$ (die Menge der Gruppierungssymbole).
3. $\mathcal{A} = \{a, b, c, \dots\}$ (die Menge der Operanden).

Ein Infix-Ausdruck $E$ ist ein String $E \in (\mathcal{A} \cup \mathcal{O} \cup \mathcal{P})^*$. Wir definieren eine Präzedenzfunktion $\rho: \mathcal{O} \to \mathbb{Z}^+$, sodass:
$$\rho(op) = \begin{cases} 1 & \text{if } op \in \{+, -\} \\ 2 & \text{if } op \in \{*, /\} \end{cases}$$

Sei $S$ ein Stack, definiert als eine Sequenz $S = \langle s_1, s_2, \dots, s_k \rangle$, wobei $s_k$ das oberste Element (Top-Element) ist. Sei $\Phi$ der Ausgabe-String (die Postfix-Repräsentation). Der Algorithmus definiert eine Zustandsübergangsfunktion $f: (\Sigma, S, \Phi) \to (S', \Phi')$.

## 2. Algebraische Charakterisierung

Die Korrektheit des Shunting-Yard-Algorithmus beruht auf der Aufrechterhaltung einer Invariante bezüglich der Operatorpräzedenz. Für zwei beliebige Operatoren $op_1, op_2 \in \mathcal{O}$, wobei sich $op_1$ aktuell an der Spitze des Stacks befindet und $op_2$ der eingehende Operator ist, erzwingt der Algorithmus den folgenden Übergang:

Wenn auf $op_2$ gestoßen wird, poppen wir $op_1$ von $S$ nach $\Phi$ genau dann, wenn:
$$\rho(op_1) \geq \rho(op_2) \land op_1 \neq '('$$

Dies stellt sicher, dass der Postfix-String $\Phi$ die Eigenschaft erfüllt, dass für jeden Teilausdruck der Operator mit der höchsten Präzedenz vor Operatoren mit niedrigerer Präzedenz auf seine Operanden angewendet wird, wodurch die Semantik des ursprünglichen Infix-Ausdrucks $E$ erhalten bleibt.

Formal sei $E = e_1 e_2 \dots e_n$. Der Algorithmus verarbeitet jedes $e_i$ gemäß den folgenden Übergangsregeln:
1. **Operand:** Wenn $e_i \in \mathcal{A}$, dann ist $\Phi_{i} = \Phi_{i-1} \cdot e_i$.
2. **Linke Klammer:** Wenn $e_i = '(',$ dann ist $S_{i} = S_{i-1} \cdot ('(')$.
3. **Rechte Klammer:** Wenn $e_i = ')',$ dann wird $S_i$ reduziert, indem alle $op \in \mathcal{O}$, für die $\rho(op)$ definiert ist, gepoppt und an $\Phi$ angehängt werden, bis $S_{top} = '('.$
4. **Operator:** Wenn $e_i \in \mathcal{O}$, sei $S_{top}$ das oberste Element des Stacks. Solange $S_{top} \neq '('$ und $\rho(S_{top}) \geq \rho(e_i)$, führe $\Phi \leftarrow \Phi \cdot \text{pop}(S)$ aus. Pushe schließlich $e_i$ auf $S$.

Der finale Postfix-Ausdruck ist $\Phi_n \cdot \text{pop}(S)^k$, wobei $k = |S|$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Sei $N$ die Länge des Eingabe-Strings $E$. Wir definieren die gesamte Zeitkomplexität $T(N)$ als die Summe der Operationen, die für jedes Zeichen $e_i \in E$ ausgeführt werden.

Jedes Zeichen $e_i$ wird höchstens einmal auf den Stack $S$ gepusht und höchstens einmal vom Stack gepoppt. 
- Für Operanden ist die Operation $O(1)$.
- Für Operatoren sei $k_i$ die Anzahl der Operatoren, die für ein gegebenes $e_i$ vom Stack gepoppt werden. Die Gesamtzeit beträgt:
$$T(N) = \sum_{i=1}^{N} (1 + k_i)$$
Da jeder Operator genau einmal gepusht wird, ist die Gesamtzahl der Pops über die gesamte Ausführung hinweg durch $N$ beschränkt. Somit gilt $\sum_{i=1}^{N} k_i \leq N$.
Daher gilt $T(N) = O(N) + O(N) = O(N)$.

### Platzkomplexität
Die Platzkomplexität $S(N)$ wird durch den Hilfsspeicher bestimmt, der für den Stack $S$ und den Ausgabe-String $\Phi$ benötigt wird.
- Der Ausgabe-String $\Phi$ hat die Länge $N$, was $O(N)$ Platz erfordert.
- Der Stack $S$ kann im schlechtesten Fall höchstens $N$ Elemente enthalten (z. B. bei einem Ausdruck mit geschachtelten Klammern oder steigender Präzedenz).
- Somit beträgt die gesamte Platzkomplexität:
$$S(N) = \text{Space}(\Phi) + \text{Space}(S) = O(N) + O(N) = O(N)$$
Der Algorithmus ist sowohl in Bezug auf die Zeit als auch auf den Platz streng linear zur Eingabegröße $N$.