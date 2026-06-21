# Formale mathematische Spezifikation: Min Cost Path

## 1. Definitionen und Notation
Gitter $C$ der Größe $m \times n$ mit Kosten. Bewegungen sind nach unten, rechts oder diagonal möglich.

## 2. Algebraische Charakterisierung (Rekursionsgleichung)
$$ M(i, j) = C[i, j] + \min(M(i-1, j), M(i, j-1), M(i-1, j-1)) $$

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** $O(nm)$.
- **Platzkomplexität:** $O(n)$.