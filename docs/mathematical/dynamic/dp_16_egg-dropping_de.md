# Formale mathematische Spezifikation: Eierwurf-Problem (Egg Dropping Puzzle)

## 1. Definitionen und Notation
$E$ Eier, $F$ Stockwerke. Bestimme die minimale Anzahl an Versuchen im Schlechtesten Fall, um das kritische Stockwerk zu finden.

## 2. Algebraische Charakterisierung (Rekursionsgleichung)
$$ D(e, f) = \begin{cases} f & \text{if } e = 1 \\ 0 & \text{if } f = 0 \\ 1 & \text{if } f = 1 \\ 1 + \min_{1 \leq x \leq f} \max(D(e-1, x-1), D(e, f-x)) & \text{otherwise} \end{cases} $$

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** $O(e f^2)$ (kann durch binäre Suche auf $O(e f \log f)$ optimiert werden).
- **Platzkomplexität:** $O(ef)$.