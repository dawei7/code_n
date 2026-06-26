# Formale mathematische Spezifikation: Treppensteigen (Climbing Stairs)

## 1. Definitionen und Notation
Sei $C(n)$ die Anzahl der verschiedenen Möglichkeiten, $n$ Treppenstufen zu erklimmen, wobei Schritte $s \in \{1, 2\}$ möglich sind.

## 2. Algebraische Charakterisierung (Rekursionsgleichung)
$$ C(n) = \begin{cases} 1 & \text{if } n \in \{0, 1\} \\ C(n-1) + C(n-2) & \text{if } n > 1 \end{cases} $$

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** $O(n)$, identisch mit der Berechnung der Fibonacci-Folge.
- **Platzkomplexität:** $O(1)$ Platz bei Verwendung von Zustandsreduktion.