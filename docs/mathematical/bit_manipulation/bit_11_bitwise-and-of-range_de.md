# Formale mathematische Spezifikation: Bitweises AND eines Zahlenbereichs

## 1. Definitionen und Notation

Sei $\mathbb{Z}_{\ge 0}$ die Menge der nicht-negativen ganzen Zahlen. Wir definieren den Eingabebereich als ein Paar $(L, R) \in \mathbb{Z}_{\ge 0}^2$, sodass $0 \le L \le R \le 2^{31} - 1$ gilt.

Sei $b_k(n) \in \{0, 1\}$ das $k$-te Bit der Binärdarstellung von $n$, sodass $n = \sum_{k=0}^{30} b_k(n) \cdot 2^k$ gilt.

Das Ziel ist die Berechnung der Funktion $f: \mathbb{Z}_{\ge 0}^2 \to \mathbb{Z}_{\ge 0}$, die durch den bitweisen AND-Operator ($\land$) definiert ist:
$$f(L, R) = \bigwedge_{i=L}^{R} i$$
wobei das bitweise AND einer Menge von ganzen Zahlen bitweise definiert ist:
$$b_k(f(L, R)) = \prod_{i=L}^{R} b_k(i)$$
wobei das Produkt $\prod$ über der booleschen Domäne $\{0, 1\}$ gebildet wird (äquivalent zum logischen AND).

## 2. Algebraische Charakterisierung

**Theorem:** Das bitweise AND des Bereichs $[L, R]$ entspricht dem Wert, der durch das Maskieren aller Bits rechts vom höchstwertigen Bit, an dem sich $L$ und $R$ unterscheiden, erhalten wird.

**Beweisskizze:**
Betrachten wir die Binärdarstellungen von $L$ und $R$. Sei $k_{max}$ der größte Index, für den $b_{k_{max}}(L) \neq b_{k_{max}}(R)$ gilt. Für jedes $k > k_{max}$ gilt $b_k(L) = b_k(R) = c_k$. Da $L \le R$ gilt, muss $b_{k_{max}}(L) = 0$ und $b_{k_{max}}(R) = 1$ sein.

Für jedes $k \le k_{max}$ existiert mindestens eine ganze Zahl $x \in [L, R]$, sodass $b_k(x) = 0$ ist. Insbesondere enthält der Bereich $[L, R]$ einen Übergangspunkt, an dem das $k$-te Bit von $1$ auf $0$ oder umgekehrt wechselt. Folglich gilt $\prod_{i=L}^{R} b_k(i) = 0$ für alle $k \le k_{max}$.

Somit ergibt sich:
$$f(L, R) = \sum_{k=k_{max}+1}^{30} c_k \cdot 2^k$$

**Schleifeninvariante:**
Sei $(L_t, R_t, s_t)$ der Zustand in Iteration $t$.
1. Initialisierung: $L_0 = L, R_0 = R, s_0 = 0$.
2. Übergang: Wenn $L_t < R_t$, dann $L_{t+1} = \lfloor L_t / 2 \rfloor$, $R_{t+1} = \lfloor R_t / 2 \rfloor$ und $s_{t+1} = s_t + 1$.
3. Terminierung: Die Schleife terminiert bei $T$, wenn $L_T = R_T$ gilt.
4. Invariante: $f(L, R) = L_T \cdot 2^{s_T}$.

Diese Invariante gilt, da das Rechts-Shiften von $L$ und $R$ um $s$ Positionen äquivalent zur Division durch $2^s$ ist. Der Prozess entfernt effektiv die Bits, die nicht in $L$ und $R$ gemeinsam vorhanden sind.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus führt eine Sequenz von Rechts-Shift-Operationen durch. Die Anzahl der Iterationen $T$ wird durch die Position des höchstwertigen Bits bestimmt, an dem sich $L$ und $R$ unterscheiden.
Da $L, R < 2^{31}$ gilt, ist die maximale Anzahl an Bits $W = 31$. Die Schleifenbedingung $L < R$ ist höchstens $W$-mal erfüllt.
Der Aufwand pro Iteration beträgt $O(1)$ (ein bitweiser Shift und eine Inkrementierung). Somit ergibt sich die gesamte Zeitkomplexität zu:
$$T(W) = \sum_{t=1}^{T} O(1) = O(W)$$
Da $W$ eine feste Konstante ist (die Wortbreite der Architektur), beträgt die Komplexität $O(1)$.

### Platzkomplexität
Der Algorithmus verwaltet eine konstante Anzahl an Integer-Variablen: `left`, `right` und `shift`.
Der benötigte Speicher ist unabhängig von der Größe der Eingabewerte $L$ und $R$.
$$S(L, R) = \Theta(1)$$
Somit beträgt die zusätzliche Platzkomplexität $O(1)$.