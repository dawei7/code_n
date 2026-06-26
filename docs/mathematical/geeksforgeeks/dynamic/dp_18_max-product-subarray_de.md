# Formale mathematische Spezifikation: Maximum Product Subarray

## 1. Definitionen und Notation
Folge $A = (a_1 \dots a_n)$. Finde ein zusammenhängendes Subarray, das das Produkt maximiert.

## 2. Algebraische Charakterisierung (Rekursionsgleichung)
Um negative Zahlen zu behandeln, werden das maximale und minimale Produkt beibehalten: $$ \text{Max}(i) = \max(A[i], \text{Max}(i-1)A[i], \text{Min}(i-1)A[i]) $$ $$ \text{Min}(i) = \min(A[i], \text{Max}(i-1)A[i], \text{Min}(i-1)A[i]) $$

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** $O(n)$.
- **Platzkomplexität:** $O(1)$, da nur der vorherige Zustand gespeichert wird.