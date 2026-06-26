# Formale mathematische Spezifikation: Fibonacci-Folge

## 1. Definitionen und Notation
Sei $F : \mathbb{N} \to \mathbb{N}$ die Fibonacci-Folge.

## 2. Algebraische Charakterisierung (Rekursionsgleichung)
$$ F(n) = \begin{cases} n & \text{if } n \in \{0, 1\} \\ F(n-1) + F(n-2) & \text{if } n > 1 \end{cases} $$

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** Unter Verwendung von dynamischer Programmierung mit Memoization oder Tabulation wird die Rekursionsgleichung exakt $n$ mal ausgewertet. $O(n)$.
- **Platzkomplexität:** $O(n)$ für eine vollständige Tabelle, optimierbar auf $O(1)$, da der Zustand $F(n)$ nur von $F(n-1)$ und $F(n-2)$ abhängt.