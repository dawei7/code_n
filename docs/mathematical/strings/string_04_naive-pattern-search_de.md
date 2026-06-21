# Formale mathematische Spezifikation: Naive Mustersuche

## 1. Definitionen und Notation
Sei $T \in \Sigma^*$ ein Text der Länge $n$ und $W \in \Sigma^*$ ein Muster der Länge $m$.
Wir suchen alle Verschiebungen $s \in \{0, \dots, n-m\}$, sodass $T[s+1 \dots s+m] = W[1 \dots m]$ gilt.

## 2. Zielfunktion
Definiere eine Indikatorfunktion $\mathcal{I}(s)$ für eine gültige Verschiebung:
$$ \mathcal{I}(s) = \prod_{j=1}^m \mathbb{I}(T[s+j] = W[j]) $$
Das Ziel ist es, die Menge $\mathcal{S} = \{ s \mid \mathcal{I}(s) = 1 \}$ zu finden.

## 3. Formalisierung des Algorithmus
Für jedes $s \in \{0, 1, \dots, n-m\}$:
1. Initialisiere $j = 1$.
2. Solange $j \leq m$ und $T[s+j] = W[j]$:
   - $j \leftarrow j + 1$.
3. Falls $j = m + 1$, füge $s$ zu $\mathcal{S}$ hinzu.

## 4. Komplexitätsanalyse
- **Zeitkomplexität:** Im schlechtesten Fall (z. B. $T = a^{n}$, $W = a^{m-1}b$) wird die innere Schleife für jede der $n-m+1$ möglichen Verschiebungen genau $m$-mal ausgeführt. Die mathematische Zeitkomplexität im schlechtesten Fall beträgt $O((n - m + 1)m)$. Wenn $m \ll n$ gilt, verhält sich dies asymptotisch wie $O(nm)$.
- **Platzkomplexität:** Der Algorithmus benötigt nur die skalaren Indexvariablen $s$ und $j$. Der Platzbedarf ist strikt $O(1)$.