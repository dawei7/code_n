# Formale mathematische Spezifikation: Longest Palindromic Subsequence

## 1. Definitionen und Notation

Sei $\Sigma$ ein endliches Alphabet. Sei $s = s_0s_1\dots s_{n-1}$ ein String der Länge $n$ über $\Sigma$, wobei $s_i \in \Sigma$. 
Eine Subsequence von $s$ ist ein String $z$, der durch das Löschen von null oder mehr Zeichen aus $s$ erhalten wird. Formal ist $z$ eine Subsequence, wenn eine streng monoton steigende Folge von Indizes $0 \le i_1 < i_2 < \dots < i_k < n$ existiert, sodass $z_j = s_{i_j}$ für alle $1 \le j \le k$ gilt.

Ein String $z$ ist ein Palindrom, wenn $z = z^R$ gilt, wobei $z^R$ die Umkehrung von $z$ bezeichnet. 
Wir definieren die Menge $\mathcal{P}(s)$ als die Menge aller palindromischen Subsequences von $s$. Das Ziel ist es, die Länge der längsten solchen Subsequence zu finden:
$$LPS(s) = \max_{z \in \mathcal{P}(s)} |z|$$

Wir definieren den Zustandsraum $\mathcal{S}$ als eine zweidimensionale Matrix $D \in \mathbb{Z}^{n \times n}$, wobei jeder Eintrag $D_{i,j}$ die Länge der längsten palindromischen Subsequence des Substrings $s[i \dots j]$ darstellt, definiert für $0 \le i, j < n$.

## 2. Algebraische Charakterisierung

Das Problem weist eine optimale Substruktur und überlappende Teilprobleme auf, was eine rekursive Formulierung ermöglicht. Für jeden Substring $s[i \dots j]$ mit $i \le j$:

**Basisfälle:**
1. Wenn $i = j$, ist der Substring ein einzelnes Zeichen, welches ein Palindrom der Länge 1 ist:
   $$D_{i,i} = 1$$
2. Wenn $i > j$, ist der Substring leer, was eine Länge von 0 ergibt:
   $$D_{i,j} = 0$$

**Rekursionsschritt:**
Für $i < j$ wird der Wert $D_{i,j}$ durch die Beziehung zwischen den Randzeichen $s_i$ und $s_j$ bestimmt:
1. Wenn $s_i = s_j$, können die Zeichen $s_i$ und $s_j$ in das Palindrom aufgenommen werden, wodurch die längste palindromische Subsequence des inneren Substrings $s[i+1 \dots j-1]$ um 2 erweitert wird:
   $$D_{i,j} = D_{i+1, j-1} + 2$$
2. Wenn $s_i \neq s_j$, muss die längste palindromische Subsequence entweder in $s[i+1 \dots j]$ oder in $s[i \dots j-1]$ enthalten sein:
   $$D_{i,j} = \max(D_{i+1, j}, D_{i, j-1})$$

Die endgültige Lösung ist gegeben durch $D_{0, n-1}$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus berechnet die Einträge der $n \times n$ Matrix $D$. Die Berechnung erfolgt durch Erhöhung der Länge des Substrings $L = j - i + 1$, wobei $L$ von $2$ bis $n$ reicht. 

Für jede Länge $L$ beträgt die Anzahl der möglichen Startpositionen $i$ genau $n - L + 1$. Die Gesamtzahl der berechneten Zustände ist:
$$\sum_{L=2}^{n} (n - L + 1) = \sum_{k=1}^{n-1} k = \frac{n(n-1)}{2}$$
Da jeder Zustand $D_{i,j}$ in $O(1)$ Zeit unter Verwendung der Rekurrenz berechnet wird, ergibt sich die gesamte Zeitkomplexität zu:
$$T(n) = \sum_{L=2}^{n} O(n - L + 1) = O(n^2)$$

### Platzkomplexität
Der Algorithmus benötigt ein zweidimensionales Array $D$ der Größe $n \times n$, um die Ergebnisse der Teilprobleme zu speichern. 
- **Zusätzlicher Speicherplatz:** Der für die DP-Tabelle benötigte Speicherplatz beträgt $n^2$ Integer-Werte. Somit ist die Platzkomplexität $O(n^2)$.
- **Gesamtspeicherplatz:** Die gesamte Platzkomplexität beträgt $O(n^2)$, da der Eingabestring $O(n)$ und die DP-Tabelle $O(n^2)$ belegt. 

*Hinweis:* Obwohl der Speicherplatz auf $O(n)$ optimiert werden kann, indem man beobachtet, dass die Berechnung der Länge $L$ nur Werte der Längen $L-1$ und $L-2$ erfordert, verwendet die hier bereitgestellte Standardimplementierung $O(n^2)$ zur besseren Übersichtlichkeit und einfacheren Rekonstruktion.