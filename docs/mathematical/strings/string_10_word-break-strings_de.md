# Formale mathematische Spezifikation: Word Break

## 1. Definitionen und Notation
Sei $S \in \Sigma^*$ ein String der Länge $n$ und $\mathcal{D} \subset \Sigma^*$ ein Wörterbuch.
Wir definieren ein Prädikat $W(i)$, das angibt, ob das Präfix $S[1 \dots i]$ in eine durch Leerzeichen getrennte Sequenz aus einem oder mehreren Wörtern des Wörterbuchs segmentiert werden kann.

## 2. Algebraische Charakterisierung
Basisfall: $W(0) = \text{True}$ (der leere String ist trivialerweise gültig).
Für $1 \leq i \leq n$ lautet die Rekursionsgleichung:
$$ W(i) = \bigvee_{j=0}^{i-1} \Big( W(j) \land (S[j+1 \dots i] \in \mathcal{D}) \Big) $$

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** Die Auswertung von $W(i)$ für alle $i$ erfordert das Iterieren über $j < i$. Es gibt $n(n-1)/2$ Zustandsauswertungen. Die Überprüfung von $S[j+1 \dots i] \in \mathcal{D}$ über ein Hash-Set benötigt eine Zeit proportional zur Substring-Länge $O(i-j)$. Die mathematisch strikte obere Schranke ist $O(n^3)$. (Wenn Substring-Hashing oder ein Trie verwendet wird, kann dies auf $O(n^2)$ reduziert werden).
- **Platzkomplexität:** Das boolesche Array $W$ erfordert $O(n)$ Platz. Das Wörterbuch $\mathcal{D}$ wird extern gespeichert, was $O(\sum_{w \in \mathcal{D}} |w|)$ Platz erfordert.