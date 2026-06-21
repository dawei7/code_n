# Formale mathematische Spezifikation: Randomisierte binäre Suche

## 1. Definitionen und Notation

Sei $A = [a_0, a_1, \dots, a_{n-1}]$ eine Sequenz von $n$ verschiedenen Ganzzahlen, sodass $a_i < a_{i+1}$ für alle $0 \le i < n-1$ gilt. Sei $x \in \mathbb{Z}$ der Zielwert.

Wir definieren den Zustand des Algorithmus in der Iteration $k$ durch das Tupel $\mathcal{S}_k = (L_k, R_k)$, welches das inklusive Suchintervall $[L_k, R_k] \subseteq \{0, 1, \dots, n-1\}$ repräsentiert.
- **Anfangszustand:** $\mathcal{S}_0 = (0, n-1)$.
- **Zufallsvariable:** Sei $P_k$ eine diskrete gleichverteilte Zufallsvariable, sodass $P_k \sim \mathcal{U}\{L_k, R_k\}$.
- **Abbruchbedingung:** Der Algorithmus terminiert bei Schritt $T$, wenn $L_T > R_T$ (Fehlschlag) oder $a_{P_T} = x$ (Erfolg).

## 2. Algebraische Charakterisierung

Der Algorithmus definiert einen stochastischen Prozess auf der Größe des Suchraums $N_k = R_k - L_k + 1$. Die Übergangsfunktion $\Phi: \mathcal{S}_k \to \mathcal{S}_{k+1}$ ist definiert als:

$$
\mathcal{S}_{k+1} = 
\begin{cases} 
(L_k, P_k - 1) & \text{if } a_{P_k} > x \\
(P_k + 1, R_k) & \text{if } a_{P_k} < x \\
\text{terminate} & \text{if } a_{P_k} = x 
\end{cases}
$$

**Schleifeninvariante:** Für alle $k \ge 0$ gilt: Wenn $x \in A$, dann erfüllt der Index $i$, für den $a_i = x$ gilt, die Bedingung $L_k \le i \le R_k$. 
*Beweisskizze:* Durch vollständige Induktion: Der Induktionsanfang gilt für $\mathcal{S}_0$. Gegeben $a_{P_k} \neq x$, stellt die Sortierung von $A$ sicher, dass wenn $a_{P_k} < x$, dann für alle $j \le P_k$ gilt $a_j < x$, folglich $i \notin [L_k, P_k]$. Das symmetrische Argument gilt für $a_{P_k} > x$.

## 3. Komplexitätsanalyse

### Zeitkomplexität

Sei $T(n)$ die erwartete Anzahl an Vergleichen, um $x$ in einem Array der Größe $n$ zu finden. In jedem Schritt wählen wir ein Pivot-Element $P \in \{0, \dots, n-1\}$ mit Wahrscheinlichkeit $\frac{1}{n}$. Die Größe des verbleibenden Teilproblems ist $P$ (falls wir links suchen) oder $n-1-P$ (falls wir rechts suchen).

Die Rekurrenz für die erwartete Zeit lautet:
$$E[T(n)] = 1 + \frac{1}{n} \sum_{i=0}^{n-1} \max(E[T(i)], E[T(n-1-i)])$$

Zur Vereinfachung betrachten wir den durchschnittlichen Fall, in dem das Pivot-Element das Array in zwei Segmente der Größe $i$ und $n-1-i$ teilt. Da die erwartete Größe des verbleibenden Segments näherungsweise $n/2$ beträgt, beobachten wir:
$$E[T(n)] \approx 1 + E[T(n/2)]$$
Durch das Master-Theorem (oder die Expansion der Rekurrenz) ergibt sich:
$$E[T(n)] = \Theta(\log n)$$

**Schlechtester Fall:** Der schlechteste Fall tritt ein, wenn das zufällige Pivot-Element konsistent als Randelement gewählt wird (z. B. $P_k = L_k$ oder $P_k = R_k$). In diesem Szenario reduziert sich der Suchraum pro Iteration nur um 1 Element:
$$T(n) = 1 + T(n-1) \implies T(n) = O(n)$$
Die Wahrscheinlichkeit, das Randelement $k$-mal hintereinander auszuwählen, beträgt jedoch $2^k / n^k$, was für $n \to \infty$ gegen Null konvergiert.

### Platzkomplexität

Der Algorithmus verwaltet nur eine konstante Anzahl an skalaren Variablen: $L, R, P$ und $target$. 
- **Zusätzlicher Speicherplatz:** $O(1)$, da der Zustand $\mathcal{S}_k$ in-place ohne Rekursion oder zusätzliche Datenstrukturen aktualisiert wird.
- **Gesamtspeicherplatz:** $O(n)$ zur Speicherung des Eingabe-Arrays $A$, aber $O(1)$ in Bezug auf die Ausführungslogik des Algorithmus.