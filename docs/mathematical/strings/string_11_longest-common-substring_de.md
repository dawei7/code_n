# Formale mathematische Spezifikation: Längster gemeinsamer Teilstring (Horizontales Scannen)

*(Hinweis: `string_11` deckt den längsten gemeinsamen Teilstring über dieselben Mechanismen ab wie `string_05`, stellt aber möglicherweise einen alternativen Ansatz wie das horizontale Scannen für den längsten gemeinsamen Präfix (LCP) dar. Aufgrund typischer Probleme mit doppelten Benennungen wird hier von LCP ausgegangen.)*

## 1. Definitionen und Notation
Es sei $\mathcal{A} = \{S_1, S_2, \dots, S_N\}$ eine Menge von $N$ Strings.
Es bezeichne $\text{LCP}(S_a, S_b)$ den längsten gemeinsamen Präfix zweier Strings.
Das Ziel ist es, $\text{LCP}(\mathcal{A}) = \bigcap_{k=1}^N S_k[1 \dots c]$ für ein maximales $c$ zu finden.

## 2. Algebraische Charakterisierung
Die LCP-Operation ist assoziativ und kommutativ:
$$ \text{LCP}(\mathcal{A}) = \text{LCP}(S_1, \text{LCP}(S_2, \dots \text{LCP}(S_{N-1}, S_N))) $$

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** Das iterative Akkumulieren des LCP über alle $N$ Strings beschränkt die Zeichenvergleiche auf die Länge des kürzesten Strings: $O(N \cdot \min |S_i|)$.
- **Platzkomplexität:** $O(1)$ über das Eingabe-Array hinaus.