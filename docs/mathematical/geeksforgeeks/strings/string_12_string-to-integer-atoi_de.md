# Formale Mathematische Spezifikation: String zu Integer (atoi)

## 1. Definitionen und Notation
Sei $S$ ein String. Sei $\sigma \in \{1, -1\}$ das Vorzeichen.
Sei $\mathcal{D} = S[i \dots j]$ die zusammenhängende Sequenz numerischer Ziffern $d_k \in \{0 \dots 9\}$.

## 2. Algebraische Charakterisierung
Die Integer-Repräsentation ist eine Polynom-Evaluation zur Basis 10:
$$ N = \sigma \sum_{k=0}^{|D|-1} d_{|D|-1-k} \cdot 10^k $$
Um einen Overflow zu verhindern, erfordert die iterative Evaluation $N_{k} = 10 \cdot N_{k-1} + d_k$ eine Überprüfung:
$$ N_{k-1} > \lfloor \frac{INT\_MAX}{10} \rfloor \implies \text{Overflow} $$

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** Das Parsen ist deterministisch $O(n)$.
- **Platzkomplexität:** $O(1)$.