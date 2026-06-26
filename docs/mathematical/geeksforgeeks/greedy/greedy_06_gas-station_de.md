# Formale mathematische Spezifikation: Tankstellen-Problem (Circular Tour)

## 1. Definitionen und Notation

Sei $N \in \mathbb{Z}^+$ die Anzahl der Tankstellen. Wir definieren die kreisförmige Route als eine Menge von Indizes $I = \{0, 1, \dots, N-1\}$. 
Der Input besteht aus zwei Sequenzen:
- Eine Sequenz der Treibstoffverfügbarkeit $G = \{g_0, g_1, \dots, g_{N-1}\}$, wobei $g_i \in \mathbb{R}_{\ge 0}$.
- Eine Sequenz der Kosten $C = \{c_0, c_1, \dots, c_{N-1}\}$, wobei $c_i \in \mathbb{R}_{\ge 0}$.

Wir definieren den Nettogewinn an Station $i$ als $d_i = g_i - c_i$. Die kumulative Gewinnfunktion, ausgehend vom Index $s$ nach $k$ Schritten, ist definiert als:
$$f(s, k) = \sum_{j=0}^{k-1} d_{(s+j) \pmod N}$$

Ein Startindex $s \in I$ ist **gültig** genau dann, wenn für alle $k \in \{1, 2, \dots, N\}$ gilt:
$$f(s, k) \ge 0$$

Das Ziel ist es, ein $s^* \in I$ zu finden, sodass $s^*$ gültig ist, oder $-1$ zurückzugeben, falls kein solches $s^*$ existiert.

## 2. Algebraische Charakterisierung

### Existenzbedingung
Eine notwendige und hinreichende Bedingung für die Existenz eines gültigen Startindex $s^*$ ist, dass der gesamte Nettogewinn über den gesamten Rundkurs nicht-negativ ist:
$$\sum_{i=0}^{N-1} d_i \ge 0$$
Wenn $\sum_{i=0}^{N-1} d_i < 0$, dann gilt für jedes $s \in I$, dass $f(s, N) < 0$, was impliziert, dass der Tank leer sein wird, bevor der Rundkurs vollendet ist.

### Die Greedy-Invariante
Sei $T_i$ der Zustand des Tanks zum Schritt $i$ während eines linearen Durchlaufs. Wir definieren den Übergang:
$$T_{i+1} = \max(0, T_i + d_i)$$
Um jedoch den Startindex zu identifizieren, führen wir eine laufende Summe $S_i$ und einen Kandidaten für den Start $s$ mit:
1. Sei $S_i = \sum_{j=s}^{i} d_j$.
2. Wenn $S_i < 0$, dann kann für alle $k \in \{s, \dots, i\}$ der Pfad, der bei $k$ beginnt, $i+1$ nicht erreichen. Daher setzen wir $s = i+1$ und setzen $S = 0$ zurück.

**Theorem:** Wenn $\sum_{i=0}^{N-1} d_i \ge 0$, ist der Index $s$, der aus dem Greedy-Durchlauf in einem einzigen Durchgang resultiert, der eindeutige gültige Startindex.
*Beweisskizze:* Angenommen, der Algorithmus setzt am Index $i$ zurück. Dies impliziert $\sum_{j=s}^i d_j < 0$. Jeder Startpunkt $k \in (s, i]$ würde eine Teilsumme $\sum_{j=k}^i d_j \le \sum_{j=s}^i d_j < 0$ ergeben, was die Gültigkeitsbedingung verletzt. Somit ist das Zurücksetzen sicher.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus führt einen einzigen linearen Durchlauf der Input-Arrays $G$ und $C$ durch.
Sei $W(N)$ der gesamte geleistete Arbeitsaufwand. Der Algorithmus führt aus:
- Eine Summation zur Überprüfung der Existenzbedingung: $\sum_{i=0}^{N-1} (g_i + c_i) \implies O(N)$.
- Eine Schleife mit $N$ Iterationen, wobei jede Iteration eine konstante Anzahl an arithmetischen Operationen (Addition, Vergleich, Zuweisung) durchführt: $\sum_{i=0}^{N-1} c \implies O(N)$.

Die gesamte Zeitkomplexität beträgt:
$$T(N) = O(N) + O(N) = O(N)$$
Da der Algorithmus jedes Element genau einmal besucht, ist die Komplexität $\Theta(N)$.

### Platzkomplexität
Der Algorithmus verwendet eine feste Menge an Hilfsvariablen:
- `tank` (Skalar, $\mathbb{R}$)
- `start` (Skalar, $\mathbb{Z}$)
- `i` (Schleifenindex, $\mathbb{Z}$)
- `total_gas`, `total_cost` (Skalare, $\mathbb{R}$)

Der zusätzliche Platzbedarf $S(N)$ ist unabhängig von der Inputgröße $N$:
$$S(N) = O(1)$$
Die gesamte Platzkomplexität, einschließlich der Speicherung des Inputs, beträgt $O(N)$, aber die zusätzliche Platzkomplexität (auxiliary space complexity) ist strikt $O(1)$.