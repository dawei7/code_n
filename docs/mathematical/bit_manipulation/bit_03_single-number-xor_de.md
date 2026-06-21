# Formale mathematische Spezifikation: Single Number (XOR)

## 1. Definitionen und Notation

Um eine rigorose Grundlage für den Algorithmus zu schaffen, definieren wir die mathematischen Domänen, algebraischen Strukturen und Ein-Ausgabe-Räume.

### 1.1 Mathematische Domänen
* Sei $W \in \mathbb{N}^+$ die Wortbreite der Maschinenarchitektur (typischerweise $W = 32$ oder $W = 64$).
* Sei $\mathbb{B} = \{0, 1\}$ die boolesche Domäne.
* Sei $\mathbb{F}_2^W$ der $W$-dimensionale Vektorraum über dem Galois-Feld mit zwei Elementen, $\mathbb{F}_2$. Ein Element $x \in \mathbb{F}_2^W$ wird als Bitvektor dargestellt:
  $$x = (x_{W-1}, x_{W-2}, \dots, x_0), \quad \text{wobei } x_k \in \mathbb{B} \text{ für } 0 \le k < W$$
* Es existiert eine bijektive Abbildung $\phi: \mathbb{F}_2^W \to \mathbb{Z}_{2^W}$, die jeden Bitvektor auf seine vorzeichenlose Ganzzahldarstellung abbildet:
  $$\phi(x) = \sum_{k=0}^{W-1} x_k 2^k$$

### 1.2 Eingabespezifikation
Die Eingabe ist eine endliche Sequenz (Array) $A = (a_1, a_2, \dots, a_N)$ der Länge $N \in \mathbb{N}^+$, wobei $a_i \in \mathbb{F}_2^W$ für alle $i \in \{1, \dots, N\}$ gilt.

Für die Sequenz $A$ ist garantiert, dass sie die **Single Number Partition Property** erfüllt:
Es existiert eine ungerade Ganzzahl $N = 2M + 1$ (für $M \in \mathbb{N}$) und eine Partition der Indexmenge $I = \{1, 2, \dots, N\}$ in ein Singleton $\{i^*\}$ und $M$ disjunkte Paare $P_j = \{u_j, v_j\}$ für $j \in \{1, \dots, M\}$:
$$I = \{i^*\} \cup \left( \bigcup_{j=1}^M \{u_j, v_j\} \right)$$
sodass gilt:
1. $a_{i^*} = x^*$ (das eindeutige einzelne Element).
2. $\forall j \in \{1, \dots, M\}, \quad a_{u_j} = a_{v_j} = y_j$.
3. $x^* \neq y_j$ für alle $j \in \{1, \dots, M\}$, und $y_j \neq y_k$ für alle $j \neq k$.

### 1.3 Ausgabespezifikation
Die Ausgabe des Algorithmus ist das eindeutige Element $x^* \in \mathbb{F}_2^W$, das die Eingabepartitionseigenschaft erfüllt.

### 1.4 Zustandsraum
Der Zustand des Algorithmus zum Schritt $i$ wird durch eine Akkumulatorvariable $s_i \in \mathbb{F}_2^W$ repräsentiert. Der Zustandsraum des Algorithmus ist:
$$\mathcal{S} = \mathbb{F}_2^W$$

---

## 2. Algebraische Charakterisierung

Die Korrektheit des Algorithmus beruht auf den algebraischen Eigenschaften des bitweisen Exclusive-OR ($\text{XOR}$)-Operators, bezeichnet als $\oplus$.

### 2.1 Die algebraische Struktur $(\mathbb{F}_2^W, \oplus, \mathbf{0})$
Der Operator $\oplus: \mathbb{F}_2^W \times \mathbb{F}_2^W \to \mathbb{F}_2^W$ ist bitweise definiert. Für $x, y \in \mathbb{F}_2^W$ ist das $k$-te Bit von $x \oplus y$:
$$(x \oplus y)_k = x_k \oplus y_k = (x_k + y_k) \pmod 2$$

Die algebraische Struktur $(\mathbb{F}_2^W, \oplus, \mathbf{0})$ bildet eine **elementare abelsche 2-Gruppe** (isomorph zur additiven Gruppe des Vektorraums $\mathbb{F}_2^W$), welche die folgenden Axiome garantiert:

1. **Abgeschlossenheit:** $\forall x, y \in \mathbb{F}_2^W, \quad x \oplus y \in \mathbb{F}_2^W$.
2. **Assoziativität:** $\forall x, y, z \in \mathbb{F}_2^W, \quad (x \oplus y) \oplus z = x \oplus (y \oplus z)$.
3. **Neutrales Element:** Der Nullvektor $\mathbf{0} = (0, 0, \dots, 0)$ fungiert als neutrales Element:
   $$\forall x \in \mathbb{F}_2^W, \quad x \oplus \mathbf{0} = \mathbf{0} \oplus x = x$$
4. **Selbstinversität (Involution):** Jedes Element ist sein eigenes Inverses:
   $$\forall x \in \mathbb{F}_2^W, \quad x \oplus x = \mathbf{0}$$
5. **Kommutativität:** $\forall x, y \in \mathbb{F}_2^W, \quad x \oplus y = y \oplus x$.

### 2.2 Zustandsübergang und Rekurrenz
Die Ausführung des Algorithmus kann als diskretes dynamisches System über dem Zustandsraum $\mathcal{S}$ modelliert werden. Sei $s_i$ der Zustand nach der Verarbeitung des $i$-ten Elements der Sequenz $A$:

$$\begin{aligned}
s_0 &= \mathbf{0} \\
s_i &= s_{i-1} \oplus a_i, \quad \text{für } 1 \le i \le N
\end{aligned}$$

Durch Auflösen der Rekurrenz ergibt sich der Endzustand $s_N$ als die $n$-äre bitweise Summe der gesamten Sequenz:
$$s_N = \bigoplus_{i=1}^N a_i = a_1 \oplus a_2 \oplus \dots \oplus a_N$$

### 2.3 Schleifeninvariante
Um die Korrektheit formal zu beweisen, definieren wir die Schleifeninvariante $\mathcal{L}(i)$ für die Schleifenvariable $i \in \{0, \dots, N\}$:
$$\mathcal{L}(i): \left( s_i = \bigoplus_{k=1}^i a_k \right)$$

#### Beweis der Schleifeninvariante durch vollständige Induktion:
* **Induktionsanfang ($i = 0$):** Vor Eintritt in die Schleife ist $s_0 = \mathbf{0}$. Die leere XOR-Summe ist als das neutrale Element $\mathbf{0}$ definiert. Somit gilt $\mathcal{L}(0)$.
* **Induktionsschritt:** Angenommen, $\mathcal{L}(i-1)$ gilt für ein $1 \le i \le N$, was bedeutet $s_{i-1} = \bigoplus_{k=1}^{i-1} a_k$. In der $i$-ten Iteration aktualisiert der Zustandsübergang den Akkumulator:
  $$s_i = s_{i-1} \oplus a_i$$
  Einsetzen der Induktionsvoraussetzung:
  $$s_i = \left( \bigoplus_{k=1}^{i-1} a_k \right) \oplus a_i = \bigoplus_{k=1}^i a_k$$
  Somit gilt $\mathcal{L}(i)$. Durch vollständige Induktion gilt die Schleifeninvariante für alle $i \in \{0, \dots, N\}$.

### 2.4 Beweis der Korrektheit
Nach Beendigung der Schleife ist $i = N$. Gemäß der Schleifeninvariante $\mathcal{L}(N)$ ist der Endzustand:
$$s_N = \bigoplus_{i=1}^N a_i$$

Unter Verwendung der in Abschnitt 1.2 definierten **Single Number Partition Property** partitionieren wir die Indexmenge der Summation:
$$s_N = a_{i^*} \oplus \left( \bigoplus_{j=1}^M (a_{u_j} \oplus a_{v_j}) \right)$$

Unter Anwendung der Eigenschaft, dass $a_{i^*} = x^*$ und $a_{u_j} = a_{v_j} = y_j$:
$$s_N = x^* \oplus \left( \bigoplus_{j=1}^M (y_j \oplus y_j) \right)$$

Durch die **Selbstinversitäts-Eigenschaft** von $(\mathbb{F}_2^W, \oplus, \mathbf{0})$ gilt $y_j \oplus y_j = \mathbf{0}$ für alle $j$:
$$s_N = x^* \oplus \left( \bigoplus_{j=1}^M \mathbf{0} \right)$$

Durch die **Neutralitäts-Eigenschaft** ist die $n$-äre Summe von $\mathbf{0}$ gleich $\mathbf{0}$:
$$s_N = x^* \oplus \mathbf{0}$$

Die erneute Anwendung der Neutralitäts-Eigenschaft ergibt:
$$s_N = x^*$$

Dies vervollständigt den Beweis, dass der Endzustand des Akkumulators exakt das eindeutige, nicht gepaarte Element ist. $\blacksquare$

---

## 3. Komplexitätsanalyse

### 3.1 Zeitkomplexität
Sei $T(N)$ die Rechenschrittkomplexität des Algorithmus für eine Eingabesequenz der Größe $N$. Unter dem Standard-**Word RAM-Modell** benötigen bitweise Operationen ($\oplus$) auf $W$-Bit-Wörtern $O(1)$ konstante Zeit.

Der Gesamtaufwand $T(N)$ kann als Summe der Initialisierungskosten und der Kosten der Schleifeniterationen ausgedrückt werden:
$$T(N) = T_{\text{init}} + \sum_{i=1}^N T_{\text{iter}}(i)$$

Wobei:
* $T_{\text{init}}$ die Kosten für die Initialisierung von $result = 0$ sind, was $O(1)$ entspricht.
* $T_{\text{iter}}(i)$ die Kosten der $i$-ten Iteration sind, bestehend aus:
  1. Array-Zugriff $a_i$: $O(1)$ Zeit.
  2. Bitweise XOR-Operation $s_{i-1} \oplus a_i$: $O(1)$ Zeit.
  3. Zustandszuweisung $s_i \leftarrow s_{i-1} \oplus a_i$: $O(1)$ Zeit.

Somit gilt $T_{\text{iter}}(i) = c$ für eine Konstante $c > 0$. Die Summation ergibt:
$$T(N) = c_0 + \sum_{i=1}^N c = c_0 + c \cdot N$$

Unter Verwendung der asymptotischen Notation:
$$T(N) \in \Theta(N)$$

Der Algorithmus läuft in strikt linearer Zeit, was sowohl den Schlechtesten Fall als auch den Bestfall abdeckt:
$$\Omega(N) \le T(N) \le O(N)$$

### 3.2 Platzkomplexität
Sei $S_{\text{aux}}(N)$ die zusätzliche Platzkomplexität des Algorithmus, welche den über das Eingabe-Array hinaus belegten Speicher repräsentiert.

Der Algorithmus alloziert Speicher für genau eine Zustandsvariable:
$$\text{Var} = \{s\} \subset \mathbb{F}_2^W$$

Der Speicherbedarf von $s$ ist konstant und unabhängig von der Eingabegröße $N$:
$$\text{Size}(s) = W \text{ Bits} = O(1) \text{ Wörter}$$

Da keine dynamische Speicherallokation, keine zusätzlichen Datenstrukturen und keine rekursiven Aufruf-Stacks verwendet werden, gilt:
$$S_{\text{aux}}(N) \in \Theta(1)$$

Die gesamte Platzkomplexität (einschließlich der schreibgeschützten Eingabesequenz der Größe $N$) ist:
$$S_{\text{total}}(N) = S_{\text{input}}(N) + S_{\text{aux}}(N) \in \Theta(N)$$