# Formale mathematische Spezifikation: Distinct Subsequences

## 1. Definitionen und Notation

Sei $\Sigma$ ein endliches Alphabet. Gegeben sind zwei Strings $s \in \Sigma^M$ und $t \in \Sigma^N$, wobei $M = |s|$ und $N = |t|$. Wir bezeichnen das $i$-te Zeichen von $s$ als $s_i$ (für $1 \le i \le M$) und das $j$-te Zeichen von $t$ als $t_j$ (für $1 \le j \le N$).

Wir definieren den Zustandsraum $\mathcal{S}$ als die Menge aller Paare von Indizes $(i, j)$, sodass $0 \le i \le M$ und $0 \le j \le N$. Sei $f(i, j)$ eine Funktion $f: \mathcal{S} \to \mathbb{N}_0$, die die Anzahl der verschiedenen Teilfolgen (Subsequences) des Präfixes $s[1 \dots i]$ repräsentiert, die gleich dem Präfix $t[1 \dots j]$ sind.

Das Ziel ist die Berechnung von $f(M, N)$.

## 2. Algebraische Charakterisierung

Die Funktion $f(i, j)$ ist durch die folgende Rekursionsgleichung definiert, die aus dem Prinzip der Inklusion-Exklusion bezüglich der Entscheidung, das Zeichen $s_i$ einzuschließen oder auszuschließen, abgeleitet wurde:

**Basisfälle:**
1. $f(i, 0) = 1$ für alle $0 \le i \le M$: Ein leerer Ziel-String $t[1 \dots 0]$ ist genau einmal eine Teilfolge jedes Präfixes von $s$ (durch Löschen aller Zeichen).
2. $f(0, j) = 0$ für alle $1 \le j \le N$: Ein nicht-leerer Ziel-String kann nicht aus einem leeren Quell-String gebildet werden.

**Rekursionsschritt:**
Für $i \ge 1$ und $j \ge 1$:
$$f(i, j) = \begin{cases} f(i-1, j) + f(i-1, j-1) & \text{falls } s_i = t_j \\ f(i-1, j) & \text{falls } s_i \neq t_j \end{cases}$$

**Platzoptimierte Formulierung:**
Sei $dp_j^{(i)}$ der Wert von $f(i, j)$. Da $dp_j^{(i)}$ nur von Werten der vorherigen Iteration $i-1$ abhängt, können wir den Zustand auf ein 1D-Array $dp[j]$ reduzieren. Um die Korrektheit bei einer In-Place-Aktualisierung zu wahren, iterieren wir $j$ in absteigender Reihenfolge ($N$ bis $1$):
$$dp[j] \leftarrow \begin{cases} dp[j] + dp[j-1] & \text{falls } s_i = t_j \\ dp[j] & \text{falls } s_i \neq t_j \end{cases}$$
Die Schleifeninvariante, die zu Beginn jeder Iteration $i$ aufrechterhalten wird, ist $dp[j] = f(i-1, j)$. Nach der Aktualisierung gilt $dp[j] = f(i, j)$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus besteht aus einer verschachtelten Schleifenstruktur. Die äußere Schleife iteriert über den Quell-String $s$ der Länge $M$, und die innere Schleife iteriert über den Ziel-String $t$ der Länge $N$.

Die Gesamtzahl der Operationen $T(M, N)$ ergibt sich aus der Summe:
$$T(M, N) = \sum_{i=1}^{M} \sum_{j=1}^{N} \Theta(1) = \Theta(M \cdot N)$$
Da jede Iteration eine konstante Anzahl an Vergleichen und Additionen durchführt, beträgt die Zeitkomplexität $O(M \cdot N)$.

### Platzkomplexität
Der Algorithmus verwendet ein 1D-Array $dp$ der Größe $N+1$, um die Anzahl der Teilfolgen zu speichern.

1. **Zusätzlicher Speicherplatz:** Der für die DP-Tabelle benötigte Speicherplatz beträgt $O(N)$.
2. **Gesamtspeicherplatz:** Unter Einbeziehung der Eingabe-Strings $s$ und $t$ beträgt die Platzkomplexität $O(M + N)$. Im Kontext des zusätzlichen Speicherplatzes für dynamische Programmierung ist die Komplexität jedoch strikt $O(N)$.

Die Platzoptimierung ist zulässig, da die Aktualisierung $dp[j] = dp[j] + dp[j-1]$ den Wert von $dp[j-1]$ aus der *vorherigen* Iteration ($i-1$) benötigt. Durch die Iteration von $j$ von $N$ abwärts bis $1$ stellen wir sicher, dass $dp[j-1]$ für das aktuelle $i$ noch nicht aktualisiert wurde, wodurch der Zustand $f(i-1, j-1)$ effektiv erhalten bleibt.