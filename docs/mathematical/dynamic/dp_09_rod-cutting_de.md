# Formale mathematische Spezifikation: Rod Cutting

## 1. Definitionen und Notation
Stablänge $n$. Preise $p_1 \dots p_n$. Maximierung des Gesamterlöses $\sum p_i$.

## 2. Algebraische Charakterisierung (Rekursionsgleichung)
Sei $R(n)$ der maximale Erlös für die Länge $n$. $$ R(n) = \begin{cases} 0 & \text{if } n = 0 \\ \max_{1 \leq i \leq n} (p_i + R(n - i)) & \text{if } n > 0 \end{cases} $$

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** $O(n^2)$.
- **Platzkomplexität:** $O(n)$.