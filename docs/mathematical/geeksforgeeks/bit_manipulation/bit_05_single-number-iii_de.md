# Formale mathematische Spezifikation: Single Number III

## 1. Definitionen und Notation

Um eine rigorose Grundlage für den Single Number III-Algorithmus zu schaffen, modellieren wir die Operationen auf Wortebene des Computers sowohl unter Verwendung von Vektorräumen über endlichen Körpern als auch von Ringen der modularen Arithmetik.

### 1.1. Mathematische Domänen
Sei $w \in \mathbb{N}$ die Wortbreite der Maschine (typischerweise $w = 32$ oder $w = 64$). Wir definieren zwei isomorphe Repräsentationen eines Computerwortes:

1. **Die Vektorraum-Repräsentation**: Sei $\mathcal{V} = \mathbb{F}_2^w$ der $w$-dimensionale Vektorraum über dem Galois-Körper mit zwei Elementen $\mathbb{F}_2 = (\{0, 1\}, +, \cdot)$. Ein Element $\mathbf{x} \in \mathcal{V}$ wird als Spaltenvektor dargestellt:
   $$\mathbf{x} = \begin{pmatrix} x_0 \\ x_1 \\ \vdots \\ x_{w-1} \end{pmatrix}$$
   wobei $x_i \in \mathbb{F}_2$ das $i$-te Bit des Wortes repräsentiert und $x_0$ das niederwertigste Bit (LSB) ist.

2. **Die Ring-Repräsentation**: Sei $\mathcal{R} = \mathbb{Z} / 2^w\mathbb{Z}$ der Ring der ganzen Zahlen modulo $2^w$. 

Wir definieren die bijektive Kodierungsfunktion $\phi: \mathcal{V} \to \mathcal{R}$, die einen Bitvektor auf sein äquivalentes vorzeichenloses Integer abbildet:
$$\phi(\mathbf{x}) = \sum_{i=0}^{w-1} x_i 2^i \pmod{2^w}$$

### 1.2. Bitweise Operatoren
Wir definieren formal die bitweisen Operatoren über unseren Domänen:
* **Bitweises XOR ($\oplus$)**: Dies entspricht exakt der Vektoraddition im Vektorraum $\mathcal{V}$:
  $$\mathbf{x} \oplus \mathbf{y} \triangleq \mathbf{x} + \mathbf{y} = \begin{pmatrix} x_0 + y_0 \pmod 2 \\ \vdots \\ x_{w-1} + y_{w-1} \pmod 2 \end{pmatrix}$$
* **Bitweises AND ($\wedge$)**: Dies entspricht der komponentenweisen Multiplikation von Vektoren:
  $$\mathbf{x} \wedge \mathbf{y} \triangleq \begin{pmatrix} x_0 \cdot y_0 \\ \vdots \\ x_{w-1} \cdot y_{w-1} \end{pmatrix}$$
* **Arithmetische Negation ($-$)**: Definiert über die Ring-Repräsentation $\mathcal{R}$, um das Verhalten des Zweierkomplements abzubilden:
  $$-\mathbf{x} \triangleq \phi^{-1}\left( -\phi(\mathbf{x}) \pmod{2^w} \right)$$

### 1.3. Eingabe- und Ausgabespezifikationen
* **Eingabe**: Eine endliche Sequenz $A = (a_1, a_2, \dots, a_N)$ der Länge $N$, wobei $a_i \in \mathcal{V}$ für alle $i \in \{1, \dots, N\}$.
* **Multiplizitätsfunktion**: Sei $m_A: \mathcal{V} \to \mathbb{N}_0$ die Multiplizität eines Elements in $A$:
  $$m_A(\mathbf{x}) = \sum_{i=1}^N \mathbb{I}(a_i = \mathbf{x})$$
  wobei $\mathbb{I}$ die Indikatorfunktion ist.
* **Constraints**:
  1. Es existieren genau zwei verschiedene Elemente $\mathbf{u}, \mathbf{v} \in \mathcal{V}$ mit $\mathbf{u} \neq \mathbf{v}$, sodass $m_A(\mathbf{u}) = 1$ und $m_A(\mathbf{v}) = 1$.
  2. Für alle anderen Elemente $\mathbf{x} \in \mathcal{V} \setminus \{\mathbf{u}, \mathbf{v}\}$ gilt: wenn $m_A(\mathbf{x}) > 0$, dann ist $m_A(\mathbf{x}) = 2$.
  3. Die Gesamtlänge der Sequenz ist $N = 2k + 2$ für ein $k \in \mathbb{N}_0$.
* **Ausgabe**: Die Menge $Y = \{\mathbf{u}, \mathbf{v}\}$.

---

## 2. Algebraische Charakterisierung

Die Korrektheit des Single Number III-Algorithmus beruht auf den algebraischen Eigenschaften des Vektorraums $\mathcal{V}$ und der Interaktion zwischen Ringaddition und bitweisen Operationen.

### 2.1. Algebraische Eigenschaften von $(\mathcal{V}, \oplus)$
Die algebraische Struktur $(\mathcal{V}, \oplus)$ ist eine abelsche Gruppe vom Exponenten 2, die folgende Eigenschaften erfüllt:
1. **Identität**: $\mathbf{x} \oplus \mathbf{0} = \mathbf{x}$
2. **Selbstinvers**: $\mathbf{x} \oplus \mathbf{x} = \mathbf{0}$
3. **Kommutativität**: $\mathbf{x} \oplus \mathbf{y} = \mathbf{y} \oplus \mathbf{x}$
4. **Assoziativität**: $(\mathbf{x} \oplus \mathbf{y}) \oplus \mathbf{z} = \mathbf{x} \oplus (\mathbf{y} \oplus \mathbf{z})$

### 2.2. Phase 1: Die globale XOR-Summe
Sei $\mathbf{S} \in \mathcal{V}$ die kumulative XOR-Summe aller Elemente in $A$:
$$\mathbf{S} = \bigoplus_{i=1}^N a_i$$

Unter Verwendung der Kommutativität und Assoziativität von $\oplus$ partitionieren wir die Summe über die eindeutigen Elemente und die Paare:
$$\mathbf{S} = \mathbf{u} \oplus \mathbf{v} \oplus \left( \bigoplus_{\mathbf{x} \in \mathcal{V} \setminus \{\mathbf{u}, \mathbf{v}\}} \bigoplus_{j=1}^{m_A(\mathbf{x})} \mathbf{x} \right)$$

Da $m_A(\mathbf{x}) = 2$ für alle gepaarten Elemente gilt, haben wir:
$$\bigoplus_{j=1}^{m_A(\mathbf{x})} \mathbf{x} = \mathbf{x} \oplus \mathbf{x} = \mathbf{0}$$

Somit vereinfacht sich die globale Summe zu:
$$\mathbf{S} = \mathbf{u} \oplus \mathbf{v}$$

Da $\mathbf{u} \neq \mathbf{v}$, folgt daraus $\mathbf{S} \neq \mathbf{0}$.

### 2.3. Phase 2: Bit-Isolierung (LSB-Extraktion)
Da $\mathbf{S} \neq \mathbf{0}$, existiert mindestens ein Index $p \in \{0, \dots, w-1\}$, sodass $S_p = 1$. Dies impliziert $u_p \neq v_p$.

Um das niederwertigste gesetzte Bit von $\mathbf{S}$ zu isolieren, definieren wir den Maskenvektor $\boldsymbol{\delta} \in \mathcal{V}$:
$$\boldsymbol{\delta} = \mathbf{S} \wedge (-\mathbf{S})$$

#### Lemma 1 (LSB-Isolierung)
*Für jeden Vektor $\mathbf{x} \in \mathcal{V} \setminus \{\mathbf{0}\}$ sei $p = \min \{ i \in \{0, \dots, w-1\} \mid x_i = 1 \}$ der Index seines niederwertigsten gesetzten Bits. Dann gilt:*
$$\mathbf{x} \wedge (-\mathbf{x}) = \mathbf{e}^{(p)}$$
*wobei $\mathbf{e}^{(p)}$ der $p$-te Standardbasisvektor von $\mathbb{F}_2^w$ ist (d. h. $e^{(p)}_p = 1$ und $e^{(p)}_i = 0$ für alle $i \neq p$).*

**Beweis**:
Sei $X = \phi(\mathbf{x})$. Da $p$ der LSB-Index von $\mathbf{x}$ ist, können wir $X$ schreiben als:
$$X = 2^p + q \cdot 2^{p+1} = 2^p(1 + 2q)$$
für ein $q \in \mathbb{Z}$.

Im Ring $\mathcal{R} = \mathbb{Z}/2^w\mathbb{Z}$ ist das additive Inverse von $X$:
$$-X \equiv 2^w - X \equiv 2^w - 2^p(1 + 2q) \equiv 2^p(2^{w-p} - 1 - 2q) \pmod{2^w}$$

Unter Verwendung der Identität $2^{w-p} - 1 = \sum_{j=0}^{w-p-1} 2^j$ beobachten wir:
$$-X = 2^p \left( 1 + 2k' \right)$$
für ein $k' \in \mathbb{Z}$. Dies impliziert, dass die Binärdarstellung von $-X$, bezeichnet als $\mathbf{y} = \phi^{-1}(-X)$, ebenfalls ihr erstes gesetztes Bit am Index $p$ hat. Somit gilt:
* Für $i < p$: $x_i = 0$ und $y_i = 0 \implies x_i \cdot y_i = 0$.
* Für $i = p$: $x_p = 1$ und $y_p = 1 \implies x_p \cdot y_p = 1$.
* Für $i > p$: Die Negation im Zweierkomplement garantiert, dass für jede Bitposition $i > p$ gilt: $y_i = 1 - x_i$ (die Bits sind invertiert). Somit ist $x_i \cdot y_i = x_i \cdot (1 - x_i) = 0$.

Daher ergibt das bitweise AND:
$$\mathbf{x} \wedge (-\mathbf{x}) = \mathbf{e}^{(p)}$$
$\blacksquare$

Durch Anwendung von Lemma 1 auf unsere globale Summe $\mathbf{S}$ erhalten wir:
$$\boldsymbol{\delta} = \mathbf{e}^{(p)}$$
wobei $p$ der niedrigste Index ist, an dem sich $\mathbf{u}$ und $\mathbf{v}$ unterscheiden.

### 2.4. Phase 3: Partitionierung und Projektion
Wir definieren einen Projektionsoperator $\pi_p: \mathcal{V} \to \mathbb{F}_2$, der die $p$-te Koordinate eines Vektors extrahiert:
$$\pi_p(\mathbf{x}) = \mathbf{x} \wedge \boldsymbol{\delta} = \begin{pmatrix} 0 \\ \vdots \\ x_p \\ \vdots \\ 0 \end{pmatrix}$$

Wir partitionieren die Eingabesequenz $A$ basierend auf dieser Projektion in zwei disjunkte Teilsequenzen $A_0$ und $A_1$:
$$A_0 = (a_i \in A \mid \pi_p(a_i) = \mathbf{0})$$
$$A_1 = (a_i \in A \mid \pi_p(a_i) = \boldsymbol{\delta})$$

#### Theorem 1 (Korrektheit der Partitionierung)
*Die Partitionierung von $A$ in $A_0$ und $A_1$ trennt $\mathbf{u}$ und $\mathbf{v}$ in verschiedene Teilsequenzen, während alle identischen Paare innerhalb derselben Teilsequenz verbleiben.*

**Beweis**:
1. **Trennung von $\mathbf{u}$ und $\mathbf{v}$**: Nach Definition von $p$ gilt $u_p \neq v_p$. Ohne Beschränkung der Allgemeinheit nehmen wir an, $u_p = 1$ und $v_p = 0$. Dann gilt:
   $$\pi_p(\mathbf{u}) = \boldsymbol{\delta} \implies \mathbf{u} \in A_1$$
   $$\pi_p(\mathbf{v}) = \mathbf{0} \implies \mathbf{v} \in A_0$$
2. **Kohärenz der Paare**: Seien $\mathbf{x}, \mathbf{x}$ ein Paar identischer Elemente in $A$. Da sie identisch sind, sind ihre $p$-ten Bits identisch:
   $$\pi_p(\mathbf{x}) = \pi_p(\mathbf{x})$$
   Somit werden beide Instanzen von $\mathbf{x}$ auf dieselbe Teilsequenz abgebildet (entweder beide auf $A_0$ oder beide auf $A_1$).
$\blacksquare$

### 2.5. Phase 4: Finale Reduktion
Wir berechnen die unabhängigen XOR-Summen der Partitionen $A_0$ und $A_1$:
$$\mathbf{a} = \bigoplus_{\mathbf{x} \in A_1} \mathbf{x}, \quad \mathbf{b} = \bigoplus_{\mathbf{y} \in A_0} \mathbf{y}$$

Durch Anwendung der Selbstinvers-Eigenschaft von $(\mathcal{V}, \oplus)$ auf die gepaarten Elemente in jeder Partition erhalten wir:
$$\mathbf{a} = \mathbf{u} \oplus \left( \bigoplus_{\mathbf{x} \in A_1 \setminus \{\mathbf{u}\}} \mathbf{x} \right) = \mathbf{u} \oplus \mathbf{0} = \mathbf{u}$$
$$\mathbf{b} = \mathbf{v} \oplus \left( \bigoplus_{\mathbf{y} \in A_0 \setminus \{\mathbf{v}\}} \mathbf{y} \right) = \mathbf{v} \oplus \mathbf{0} = \mathbf{v}$$

Somit konvergieren die finalen Zustandsvariablen $\mathbf{a}$ und $\mathbf{b}$ exakt zu den eindeutigen Elementen $\mathbf{u}$ und $\mathbf{v}$.

---

## 3. Komplexitätsanalyse

### 3.1. Zeitkomplexität
Sei $N$ die Anzahl der Elemente in der Eingabesequenz $A$. Die Ausführung des Algorithmus kann in drei sequentielle Schleifen zerlegt werden:

1. **Globale XOR-Summierung**:
   $$T_1(N) = \sum_{i=1}^N c_{\oplus}$$
   wobei $c_{\oplus}$ die konstante Zeit für eine bitweise XOR-Operation auf Wortebene ist. Somit gilt $T_1(N) = \Theta(N)$.

2. **Bit-Isolierung**:
   $$T_2 = c_{\text{neg}} + c_{\wedge}$$
   wobei $c_{\text{neg}}$ und $c_{\wedge}$ die konstanten Zeiten für die Negation und das bitweise AND auf Wortebene sind. Im Word-RAM-Modell gilt $T_2 = \Theta(1)$.

3. **Partitionierte XOR-Summierung**:
   $$T_3(N) = \sum_{i=1}^N \left( c_{\text{cond}} + c_{\oplus} \right)$$
   wobei $c_{\text{cond}}$ die konstante Zeit für die Auswertung der Projektionsbedingung $\pi_p(a_i)$ ist. Somit gilt $T_3(N) = \Theta(N)$.

Die gesamte Zeitkomplexität $T(N)$ ist die Summe dieser Komponenten:
$$T(N) = T_1(N) + T_2 + T_3(N) = \Theta(N) + \Theta(1) + \Theta(N) = \Theta(N)$$

Diese lineare Zeitkomplexität ist optimal, da jeder Algorithmus, der dieses Problem löst, alle $N$ Elemente mindestens einmal lesen muss, was eine untere Schranke von $\Omega(N)$ begründet.

### 3.2. Platzkomplexität
Der Algorithmus arbeitet durch die Aktualisierung einer festen Menge von Zustandsvariablen in-place:
$$\mathcal{S} = \{ \mathbf{S}, \boldsymbol{\delta}, \mathbf{a}, \mathbf{b} \} \subset \mathcal{V}^4$$

* **Zusätzlicher Speicherplatz**: Die Größe des Zustandsraums $|\mathcal{S}|$ ist unabhängig von der Eingabegröße $N$. Die Partitionierung von $A$ in $A_0$ und $A_1$ erfolgt implizit und "on-the-fly", ohne physischen Speicher für die Teilsequenzen zu allokieren. Daher ist die zusätzliche Platzkomplexität:
  $$S_{\text{aux}}(N) = \Theta(1)$$
* **Gesamtspeicherplatz**: Unter Einbeziehung der schreibgeschützten Eingabesequenz $A$ beträgt die gesamte Platzkomplexität:
  $$S_{\text{total}}(N) = \Theta(N)$$