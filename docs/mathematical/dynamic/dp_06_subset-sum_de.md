# Formale mathematische Spezifikation: Subset Sum

## 1. Definitionen und Notation
Menge $A = \{a_1 \dots a_n\}$. Zielwert $S$. Rückgabe eines booleschen Wertes $\exists B \subseteq A, \sum_{x \in B} x = S$.

## 2. Algebraische Charakterisierung (Rekursionsgleichung)
Sei $P(i, s) \in \{\text{True}, \text{False}\}$ ein Indikator dafür, ob die Summe $s$ unter Verwendung einer Teilmenge von $A[1 \dots i]$ erreicht werden kann. $$ P(i, s) = \begin{cases} \text{True} & \text{falls } s = 0 \\ \text{False} & \text{falls } i = 0 \land s > 0 \\ P(i-1, s) \lor P(i-1, s - a_i) & \text{sonst (unter der Annahme } a_i \leq s \text{)} \end{cases} $$

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** $O(nS)$.
- **Platzkomplexität:** $O(S)$ durch Platzoptimierung.