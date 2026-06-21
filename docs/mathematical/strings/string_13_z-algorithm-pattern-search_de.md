# Formale mathematische Spezifikation: Z-Algorithmus Mustererkennung

## 1. Definitionen und Notation
Sei $T$ ein Text der Länge $n$, $W$ ein Muster der Länge $m$. Sei $\$$ ein Sentinel-Zeichen, sodass $\$ \notin \Sigma$.
Konstruiere $S = W \cdot \$ \cdot T$ mit der Länge $n + m + 1$.

## 2. Algebraische Charakterisierung
Wende den Z-Algorithmus (aus `string_07`) auf $S$ an. Für jeden Index $i > m+1$, wenn $Z[i] = m$, impliziert dies, dass $S[i \dots i+m-1] = S[1 \dots m] = W$. Somit existiert eine gültige Verschiebung am Index $i - (m + 1)$ in $T$.

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** Die Konstruktion des Z-Arrays auf $S$ benötigt strikt $O(n + m)$.
- **Platzkomplexität:** Die Aufrechterhaltung des Z-Arrays für $S$ erfordert $O(n + m)$ Platz.