# Formale mathematische Spezifikation: Word Break

## 1. Definitionen und Notation
String $S$, Wörterbuch $\mathcal{D}$. Gebe True zurück, falls $S$ in Wörter $\in \mathcal{D}$ segmentiert werden kann.

## 2. Algebraische Charakterisierung (Rekursionsgleichung)
$$ W(i) = \bigvee_{j=0}^{i-1} \left( W(j) \land (S[j+1 \dots i] \in \mathcal{D}) \right) $$

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** $O(n^3)$ im Schlechtesten Fall für String-Slicing, $O(n^2)$ mit Trie.
- **Platzkomplexität:** $O(n)$.