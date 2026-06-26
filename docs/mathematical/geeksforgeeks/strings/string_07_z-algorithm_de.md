# Formale mathematische Spezifikation: Z-Algorithmus

## 1. Definitionen und Notation
Sei $S \in \Sigma^*$ ein String der Länge $n$.
Definiere das Z-Array $Z : \{1, \dots, n\} to \mathbb{N}$, wobei $Z[i]$ die Länge des längsten gemeinsamen Präfixes von $S[1 \dots n]$ und $S[i \dots n]$ ist.
Mathematisch:
$$ Z[i] = \max \{ k \mid S[1 \dots k] = S[i \dots i+k-1] \} $$
mit $Z[1] = n$.

## 2. Algebraische Charakterisierung (Die Z-Box)
Der Algorithmus verwaltet eine „Z-Box“ $[L, R]$, welche das Intervall mit dem maximalen $R$ darstellt, sodass $S[L \dots R]$ mit $S[1 \dots R-L+1]$ übereinstimmt.
Für die Berechnung von $Z[i]$ haben wir zwei primäre Fälle, basierend darauf, ob $i$ innerhalb der aktuellen Z-Box liegt ($i \leq R$):
1. **$i > R$**: Es sind keine historischen Informationen verfügbar. Wir müssen $S[i+k]$ explizit mit $S[1+k]$ für $k \ge 0$ abgleichen.
2. **$i \leq R$**: Der Substring $S[i \dots R]$ stimmt mit $S[i-L+1 \dots R-L+1]$ überein. Sei $k = i - L + 1$. Wir betrachten das zuvor berechnete $Z[k]$:
   - Wenn $Z[k] < R - i + 1$, dann gilt exakt $Z[i] = Z[k]$.
   - Wenn $Z[k] \geq R - i + 1$, dann ist $Z[i]$ mindestens $R - i + 1$, und wir müssen Zeichen beginnend ab $R+1$ explizit abgleichen.

## 3. Formalisierung des Algorithmus
1. Initialisiere $L = 0, R = 0$.
2. Für $i = 2 \dots n$:
   - Wenn $i > R$: Setze $L = i, R = i$; solange $R \leq n$ und $S[R - L + 1] = S[R]$, inkrementiere $R$. $Z[i] = R - L$, dekrementiere $R$.
   - Wenn $i \leq R$: Sei $k = i - L + 1$.
     - Wenn $Z[k] < R - i + 1$: $Z[i] = Z[k]$.
     - Wenn $Z[k] \geq R - i + 1$: Setze $L = i$; solange $R \leq n$ und $S[R - L + 1] = S[R]$, inkrementiere $R$. $Z[i] = R - L$, dekrementiere $R$.

## 4. Komplexitätsanalyse
- **Zeitkomplexität:** Der Wert von $R$ wächst streng monoton von $0$ auf $n$. Explizite Zeichenvergleiche finden nur statt, wenn Positionen jenseits von $R$ ausgewertet werden, und jeder erfolgreiche Vergleich inkrementiert $R$. Folglich gibt es höchstens $O(n)$ erfolgreiche Vergleiche. Der Overhead der Schleife beträgt $O(n)$. Die gesamte Zeitkomplexität ist strikt $O(n)$.
- **Platzkomplexität:** Der Algorithmus benötigt ein Array $Z$ der Größe $n$. Die Platzkomplexität ist $O(n)$.