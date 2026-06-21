# Formale mathematische Spezifikation: Knuth-Morris-Pratt-Algorithmus

## 1. Definitionen und Notation
Sei $T \in \Sigma^*$ ein Text der Länge $n$ und $W \in \Sigma^*$ ein Wort (Muster) der Länge $m$.
Wir suchen die Menge aller gültigen Verschiebungen $s$, sodass $0 \leq s \leq n - m$ und $T[s+1 \dots s+m] = W[1 \dots m]$.

## 2. Die Präfixfunktion (Failure-Array)
Definiere die Präfixfunktion $\pi : \{1, \dots, m\} \to \mathbb{N}$ als die Länge des längsten echten Präfixes von $W[1 \dots q]$, das auch ein echtes Suffix von $W[1 \dots q]$ ist.
Mathematisch:
$$ \pi(q) = \max \{ k < q \mid W[1 \dots k] = W[q - k + 1 \dots q] \} $$
mit $\pi(1) = 0$.

## 3. Algebraische Charakterisierung
Wenn ein Mismatch bei $T[i] \neq W[q+1]$ auftritt, nachdem $q$ Zeichen übereingestimmt haben (d. h. $T[i-q \dots i-1] = W[1 \dots q]$), muss die nächste mögliche gültige Verschiebung mit mindestens $\pi(q)$ Zeichen übereinstimmen.
Der KMP-Algorithmus garantiert, dass kein potenzieller Treffer übersprungen wird, indem das Muster um genau $q - \pi(q)$ Positionen verschoben wird.

## 4. Formalisierung des Algorithmus
**Phase 1: Berechne $\pi$**
Zustand $k$ bezeichnet die Länge des aktuell übereinstimmenden Präfixes.
Für $q = 2 \dots m$:
1. Solange $k > 0 \land W[k+1] \neq W[q]$, aktualisiere $k \leftarrow \pi(k)$.
2. Wenn $W[k+1] = W[q]$, aktualisiere $k \leftarrow k + 1$.
3. Setze $\pi(q) = k$.

**Phase 2: Abgleich mit $T$**
Zustand $q$ bezeichnet die Anzahl der übereinstimmenden Zeichen.
Für $i = 1 \dots n$:
1. Solange $q > 0 \land W[q+1] \neq T[i]$, aktualisiere $q \leftarrow \pi(q)$.
2. Wenn $W[q+1] = T[i]$, aktualisiere $q \leftarrow q + 1$.
3. Wenn $q = m$, wurde eine gültige Verschiebung bei $i - m$ gefunden. Aktualisiere $q \leftarrow \pi(q)$.

## 5. Komplexitätsanalyse
- **Zeitkomplexität:** In beiden Phasen erhöht sich der Wert von $k$ (oder $q$) in jeder Iteration der äußeren Schleife um höchstens 1. Da $k$ nach unten strikt durch 0 beschränkt ist, kann die Gesamtzahl der Dekrementierungen (die `while`-Schleifen) die Gesamtzahl der Inkrementierungen nicht überschreiten. Folglich betragen die amortisierten Kosten der inneren Schleifen $O(1)$. Die Gesamtzeit ist mathematisch strikt durch $O(n + m)$ beschränkt.
- **Platzkomplexität:** Der Algorithmus verwaltet das Präfixfunktion-Array $\pi$ der Größe $m$. Die Platzkomplexität ist exakt $O(m)$.