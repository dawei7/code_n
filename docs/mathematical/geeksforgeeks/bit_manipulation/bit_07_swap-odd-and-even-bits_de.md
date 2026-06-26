# Formale mathematische Spezifikation: Vertauschen von ungeraden und geraden Bits

## 1. Definitionen und Notation

Sei $W \in 2\mathbb{N}$ die Wortbreite der Maschinenrepräsentation (typischerweise $W = 32$ oder $W = 64$). Wir definieren den Bereich der $W$-Bit vorzeichenlosen Ganzzahlen als den Ring der Ganzzahlen modulo $2^W$, bezeichnet als $\mathbb{Z}_{2^W}$.

Jedes Element $x \in \mathbb{Z}_{2^W}$ kann eindeutig in seine Binärdarstellung zerlegt werden:
$$x = \sum_{i=0}^{W-1} b_i 2^i$$
wobei $b_i \in \mathbb{B} = \{0, 1\}$ für alle $i \in I = \{0, 1, \dots, W-1\}$ gilt. Wir bezeichnen die Bitvektor-Repräsentation von $x$ als $\mathbf{b} = (b_{W-1}, b_{W-2}, \dots, b_1, b_0) \in \mathbb{B}^W$ unter Verwendung der standardmäßigen **LSB-0-Indizierungskonvention**, bei der das Least Significant Bit (LSB) am Index $0$ liegt.

Wir partitionieren die Indexmenge $I$ in zwei disjunkte Teilmengen, die die geraden und ungeraden Bitpositionen repräsentieren:
- **Gerade Indizes:** $I_e = \{2k \mid 0 \le k < \frac{W}{2}\}$
- **Ungerade Indizes:** $I_o = \{2k + 1 \mid 0 \le k < \frac{W}{2}\}$

Offensichtlich gilt $I = I_e \cup I_o$ und $I_e \cap I_o = \emptyset$.

### Die Vertauschungspermutation
Das Ziel des Algorithmus ist es, eine Permutation $\pi: I \to I$ auf die Bitindizes von $x$ anzuwenden. Die Permutation $\pi$ ist definiert als:
$$\pi(i) = \begin{cases} 
i + 1 & \text{falls } i \in I_e \\ 
i - 1 & \text{falls } i \in I_o 
\end{cases}$$

Äquivalent dazu, unter Verwendung des bitweisen exklusiven ODER-Operators (XOR) $\oplus$:
$$\pi(i) = i \oplus 1$$

Die Zielfunktion $f: \mathbb{Z}_{2^W} \to \mathbb{Z}_{2^W}$ ist definiert als:
$$f(x) = \sum_{i=0}^{W-1} b_{\pi(i)} 2^i$$

---

## 2. Algebraische Charakterisierung

Um $f(x)$ effizient in $O(1)$-Zeit zu implementieren, drücken wir die Bitpermutation mithilfe bitweiser algebraischer Operatoren über dem Ring $\mathbb{Z}_{2^W}$ aus.

### Bitweise Operatoren
Für beliebige $u, v \in \mathbb{Z}_{2^W}$ mit Binärdarstellungen $u = \sum u_i 2^i$ und $v = \sum v_i 2^i$:
1. **Bitweises AND ($\wedge$):** 
   $$u \wedge v = \sum_{i=0}^{W-1} (u_i \cdot v_i) 2^i$$
2. **Bitweises OR ($\vee$):** 
   $$u \vee v = \sum_{i=0}^{W-1} (u_i + v_i - u_i \cdot v_i) 2^i$$
3. **Logischer Linksshift um 1 ($\ll 1$):** 
   $$u \ll 1 = (u \cdot 2) \pmod{2^W} = \sum_{i=1}^{W-1} u_{i-1} 2^i$$
4. **Logischer Rechtsshift um 1 ($\gg 1$):** 
   $$u \gg 1 = \lfloor u / 2 \rfloor = \sum_{i=0}^{W-2} u_{i+1} 2^i$$

### Definitionen der Bitmasken
Wir definieren zwei konstante Masken, $M_e$ und $M_o$, um die geraden bzw. ungeraden Bits zu isolieren:
- **Gerade Maske ($M_e$):**
  $$M_e = \sum_{i \in I_e} 2^i = \sum_{k=0}^{\frac{W}{2}-1} 2^{2k}$$
  Für $W = 32$ gilt $M_e = \text{0x55555555}_{16}$.
  
- **Ungerade Maske ($M_o$):**
  $$M_o = \sum_{i \in I_o} 2^i = \sum_{k=0}^{\frac{W}{2}-1} 2^{2k+1}$$
  Für $W = 32$ gilt $M_o = \text{0xAAAAAAAA}_{16}$.

Beachten Sie, dass $M_e \wedge M_o = 0$ und $M_e \vee M_o = 2^W - 1$ gilt.

### Theorem (Korrektheit der algebraischen Formulierung)
Die Zielfunktion $f(x)$ kann über die folgende algebraische Identität berechnet werden:
$$f(x) = ((x \wedge M_e) \ll 1) \vee ((x \wedge M_o) \gg 1)$$

#### Beweis:
Sei $T_1 = (x \wedge M_e) \ll 1$ und $T_2 = (x \wedge M_o) \gg 1$. Wir analysieren die bitweisen Komponenten von $T_1$ und $T_2$.

1. **Analyse von $T_1$:**
   Der Term $x \wedge M_e$ isoliert die geraden Bits von $x$:
   $$x \wedge M_e = \sum_{k=0}^{\frac{W}{2}-1} b_{2k} 2^{2k}$$
   Anwendung des logischen Linksshifts:
   $$T_1 = (x \wedge M_e) \ll 1 = \sum_{k=0}^{\frac{W}{2}-1} b_{2k} 2^{2k+1}$$
   Somit ist das $i$-te Bit von $T_1$, bezeichnet als $(T_1)_i$:
   $$(T_1)_i = \begin{cases} 
   b_{i-1} & \text{falls } i \in I_o \\ 
   0 & \text{falls } i \in I_e 
   \end{cases}$$

2. **Analyse von $T_2$:**
   Der Term $x \wedge M_o$ isoliert die ungeraden Bits von $x$:
   $$x \wedge M_o = \sum_{k=0}^{\frac{W}{2}-1} b_{2k+1} 2^{2k+1}$$
   Anwendung des logischen Rechtsshifts:
   $$T_2 = (x \wedge M_o) \gg 1 = \sum_{k=0}^{\frac{W}{2}-1} b_{2k+1} 2^{2k}$$
   Somit ist das $i$-te Bit von $T_2$, bezeichnet als $(T_2)_i$:
   $$(T_2)_i = \begin{cases} 
   b_{i+1} & \text{falls } i \in I_e \\ 
   0 & \text{falls } i \in I_o 
   \end{cases}$$

3. **Synthese mittels bitweisem OR:**
   Sei $y = T_1 \vee T_2$. Da $(T_1)_i \cdot (T_2)_i = 0$ für alle $i \in I$ gilt, vereinfacht sich das bitweise OR zu einer direkten Addition der Bitwerte:
   $$y_i = (T_1)_i + (T_2)_i$$
   
   Wir werten $y_i$ für beide Indexpartitionen aus:
   - Falls $i \in I_e$:
     $$y_i = 0 + b_{i+1} = b_{i+1} = b_{\pi(i)}$$
   - Falls $i \in I_o$:
     $$y_i = b_{i-1} + 0 = b_{i-1} = b_{\pi(i)}$$

   Daher gilt für alle $i \in I$, $y_i = b_{\pi(i)}$, was impliziert:
   $$y = \sum_{i=0}^{W-1} b_{\pi(i)} 2^i = f(x)$$
   $\blacksquare$

### Pädagogischer Hinweis zu Indizierungskonventionen
Falls eine Architektur oder Programmiersprache die **MSB-0-Indizierungskonvention** verwendet (wobei Index $0$ das Most Significant Bit ist), kehrt sich die Richtung der Shifts relativ zur Indexarithmetik um. Unter MSB-0 gilt:
- Gerade Bits müssen nach *rechts* verschoben werden, um ungerade Positionen zu erreichen: $(x \wedge M_e) \gg 1$.
- Ungerade Bits müssen nach *links* verschoben werden, um gerade Positionen zu erreichen: $(x \wedge M_o) \ll 1$.

Dies erklärt, warum manche Implementierungen die Shift-Richtungen abhängig vom zugrunde liegenden Bit-Ordnungsmodell vertauschen.

---

## 3. Komplexitätsanalyse

### Zeitkomplexität
Sei $W$ die Wortbreite des Prozessors. Unter dem **Word-RAM-Berechnungsmodell** wird jede primitive bitweise Operation (AND, OR, logische Shifts) auf einem $W$-Bit-Register in $O(1)$-Zeit ausgeführt.

Der Algorithmus führt eine streng begrenzte Sequenz von Operationen aus:
1. Zwei bitweise AND-Operationen: $a = x \wedge M_e$ und $b = x \wedge M_o$.
2. Ein logischer Linksshift: $c = a \ll 1$.
3. Ein logischer Rechtsshift: $d = b \gg 1$.
4. Eine bitweise OR-Operation: $y = c \vee d$.

Die Gesamtzahl der Operationen beträgt exakt $5$. Somit ist die Zeitkomplexität:
$$T(W) = \Theta(1)$$

Im Bit-Komplexitätsmodell (bei dem Operationen auf der Ebene einzelner Bits analysiert werden) beträgt die Komplexität $\Theta(W)$, da jede bitweise Operation die Verarbeitung von $W$ Bits erfordert.

### Platzkomplexität
Der Algorithmus arbeitet vollständig in-place innerhalb der Prozessorregister.
- **Zusätzlicher Speicherplatz:** Der Algorithmus benötigt Speicher für eine konstante Anzahl an Zwischenvariablen ($T_1, T_2$) und die Masken ($M_e, M_o$). Dies erfordert $O(1)$ zusätzliche Register.
- **Gesamtspeicherplatz:** Die gesamte Platzkomplexität, einschließlich der Eingabe $x$, beträgt:
$$S(W) = \Theta(1) \text{ zusätzliche Register (oder } \Theta(W) \text{ Bits)}$$