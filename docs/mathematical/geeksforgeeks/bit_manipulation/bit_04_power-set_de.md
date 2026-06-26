# Formale mathematische Spezifikation: Potenzmenge (Bitweise Optimierung)

## 1. Definitionen und Notation

Sei $A = (a_0, a_1, \dots, a_{n-1})$ ein geordnetes $n$-Tupel eindeutiger Elemente aus einem Universum $\mathcal{U}$, wobei $n = |A| \in \mathbb{N}_0$. Wir bezeichnen die zugrunde liegende Menge der Elemente in $A$ als:
$$S_A = \{a_i \mid 0 \le i < n\}$$

Das Ziel des Algorithmus ist die Konstruktion der Potenzmenge von $S_A$, bezeichnet als $\mathcal{P}(S_A)$, welche die Menge aller Teilmengen von $S_A$ ist:
$$\mathcal{P}(S_A) = \{ X \mid X \subseteq S_A \}$$

Nach der elementaren Kombinatorik beträgt die Kardinalität der Potenzmenge $|\mathcal{P}(S_A)| = 2^n$.

### Die Bitmask-Domäne
Sei $\mathbb{B} = \{0, 1\}$ die boolesche Domäne. Wir definieren die Menge der $n$-Bit-Ganzzahlen (oder Bitmasks) als:
$$\mathcal{M}_n = \{0, 1, \dots, 2^n - 1\}$$

Für jede Ganzzahl $m \in \mathcal{M}_n$ existiert eine eindeutige Binärdarstellung der Länge $n$, bezeichnet durch die Bitfolge $(b_{n-1}, \dots, b_1, b_0)_2$, sodass gilt:
$$m = \sum_{i=0}^{n-1} b_i 2^i \quad \text{wobei} \quad b_i \in \mathbb{B}$$

Wir definieren die Projektionsfunktion $\beta: \mathcal{M}_n \times \{0, \dots, n-1\} \to \mathbb{B}$, welche das $i$-te Bit von $m$ extrahiert:
$$\beta(m, i) = \left\lfloor \frac{m}{2^i} \right\rfloor \bmod 2$$

In Computersystemen, die das Zweierkomplement verwenden, wird diese Projektion mittels bitweisem Shift und bitweisen AND-Operationen implementiert:
$$\beta(m, i) = (m \gg i) \ \& \ 1 = \operatorname{sgn}(m \ \& \ (1 \ll i))$$
wobei $\gg$ der Rechts-Shift-Operator, $\ll$ der Links-Shift-Operator, $\&$ die bitweise Konjunktion und $\operatorname{sgn}(x)$ die Signum-Funktion ist.

---

## 2. Algebraische Charakterisierung

Die Korrektheit des bitweisen Algorithmus zur Generierung der Potenzmenge beruht auf der Etablierung eines Isomorphismus zwischen dem booleschen Hyperwürfel $\mathbb{B}^n$ (repräsentiert durch die Bitmasks $\mathcal{M}_n$) und der Potenzmenge $\mathcal{P}(S_A)$.

### Die charakteristische Abbildung
Wir definieren die Abbildung $\phi: \mathcal{M}_n \to \mathcal{P}(S_A)$ als:
$$\phi(m) = \{ a_i \in S_A \mid \beta(m, i) = 1 \}$$

#### Theorem 1 (Bijektivität von $\phi$)
*Die Abbildung $\phi: \mathcal{M}_n \to \mathcal{P}(S_A)$ ist eine Bijektion.*

**Beweis:**
1. **Injektivität:** Seien $m_1, m_2 \in \mathcal{M}_n$ mit $m_1 \neq m_2$. Aufgrund der Eindeutigkeit der Binärdarstellung existiert mindestens ein Index $j \in \{0, \dots, n-1\}$, sodass $\beta(m_1, j) \neq \beta(m_2, j)$. Ohne Beschränkung der Allgemeinheit nehmen wir an, dass $\beta(m_1, j) = 1$ und $\beta(m_2, j) = 0$. Nach Definition von $\phi$ gilt:
   $$a_j \in \phi(m_1) \quad \text{und} \quad a_j \notin \phi(m_2)$$
   Somit ist $\phi(m_1) \neq \phi(m_2)$, was die Injektivität beweist.

2. **Surjektivität:** Sei $Y \in \mathcal{P}(S_A)$ eine beliebige Teilmenge. Konstruiere eine Ganzzahl $m_Y$ wie folgt:
   $$m_Y = \sum_{i=0}^{n-1} \mathbb{I}(a_i \in Y) \cdot 2^i$$
   wobei $\mathbb{I}$ die Indikatorfunktion ist. Da $Y \subseteq S_A$, gilt $0 \le m_Y \le 2^n - 1$, was bedeutet, dass $m_Y \in \mathcal{M}_n$. Durch Konstruktion gilt $\beta(m_Y, i) = 1 \iff a_i \in Y$. Somit ist $\phi(m_Y) = Y$, was die Surjektivität beweist.

Da $\phi$ sowohl injektiv als auch surjektiv ist, handelt es sich um eine Bijektion. Folglich garantiert das Iterieren über alle $m \in \mathcal{M}_n$ und das Berechnen von $\phi(m)$ die Generierung jeder Teilmenge von $S_A$ exakt einmal.

### Schleifeninvarianten
Sei $\mathcal{R}^{(k)}$ der Zustand der akkumulierten Liste von Teilmengen nach der Verarbeitung von $k$ Iterationen der äußeren Schleife, wobei $k \in \{0, \dots, 2^n\}$.

* **Initialisierung ($k = 0$):**
  $$\mathcal{R}^{(0)} = \emptyset$$
  Die Relation gilt trivialerweise, da noch keine Masken verarbeitet wurden.

* **Aufrechterhaltung ($k \to k+1$):**
  Während der $k$-ten Iteration berechnet der Algorithmus die Teilmenge, die der Maske $m = k$ entspricht:
  $$\text{subset}^{(k)} = \{ a_i \in S_A \mid (k \ \& \ (1 \ll i)) \neq 0 \}$$
  Nach Definition der bitweisen Operationen gilt $\text{subset}^{(k)} = \phi(k)$. Der Zustandsübergang ist definiert durch:
  $$\mathcal{R}^{(k+1)} = \mathcal{R}^{(k)} \cup \{ \phi(k) \}$$
  Unter der Annahme, dass die Invariante für $k$ gilt, erhalten wir:
  $$\mathcal{R}^{(k+1)} = \{ \phi(m) \mid 0 \le m < k \} \cup \{ \phi(k) \} = \{ \phi(m) \mid 0 \le m \le k \}$$

* **Terminierung ($k = 2^n$):**
  Die Schleife terminiert, wenn $k = 2^n$. Der Endzustand ist:
  $$\mathcal{R}^{(2^n)} = \{ \phi(m) \mid 0 \le m < 2^n \} = \phi(\mathcal{M}_n)$$
  Da $\phi$ eine Bijektion ist, gilt $\phi(\mathcal{M}_n) = \mathcal{P}(S_A)$. Dies beweist die algebraische Korrektheit des Algorithmus.

---

## 3. Komplexitätsanalyse

### Zeitkomplexität

Um die Zeitkomplexität abzuleiten, analysieren wir die Gesamtzahl der elementaren Operationen, die durch die verschachtelte Schleifenstruktur ausgeführt werden. Sei $T(n)$ die Laufzeit des Algorithmus bei einer Eingabegröße $n$.

Die äußere Schleife wird exakt $2^n$ Mal ausgeführt, entsprechend dem Bereich der Bitmask $m \in [0, 2^n - 1]$. Für jede Maske $m$ wird die innere Schleife exakt $n$ Mal ausgeführt, entsprechend dem Index $i \in [0, n - 1]$.

Innerhalb der inneren Schleife führt der Algorithmus folgende Schritte aus:
1. Einen bitweisen Links-Shift: $1 \ll i$
2. Ein bitweises AND: $m \ \& \ (1 \ll i)$
3. Einen Vergleich mit Null: $\neq 0$
4. Eine bedingte Array-Append-Operation: $\text{subset.append}(a_i)$

Auf einem Standard-Word-RAM-Berechnungsmodell, bei dem die Wortbreite $w \ge n$ ist, laufen grundlegende bitweise Operationen ($1 \ll i$ und $\&$) in $O(1)$ konstanter Zeit. Die bedingte Append-Operation benötigt amortisiert $O(1)$ Zeit.

Sei $c_1$ die konstanten Kosten der Schleifensteuerung und der bitweisen Auswertung, und sei $c_2$ die konstanten Kosten für das Anhängen eines Elements an die aktuelle Teilmenge. Die gesamte Zeitkomplexität kann wie folgt modelliert werden:
$$T(n) = \sum_{m=0}^{2^n-1} \left( \sum_{i=0}^{n-1} c_1 + c_2 \cdot \mathbb{I}(a_i \in \phi(m)) \right)$$

Wir teilen diese Doppelsumme in zwei Teile auf:
$$T(n) = \sum_{m=0}^{2^n-1} n \cdot c_1 + c_2 \sum_{m=0}^{2^n-1} |\phi(m)|$$

Der erste Term vereinfacht sich zu:
$$\sum_{m=0}^{2^n-1} n \cdot c_1 = c_1 \cdot n 2^n$$

Der zweite Term repräsentiert die Summe der Kardinalitäten aller Teilmengen in $\mathcal{P}(S_A)$. Unter Verwendung des Binomischen Lehrsatzes berechnen wir diese Summe als:
$$\sum_{m=0}^{2^n-1} |\phi(m)| = \sum_{k=0}^{n} \binom{n}{k} k$$

Unter Verwendung der Identität $k \binom{n}{k} = n \binom{n-1}{k-1}$ erhalten wir:
$$\sum_{k=1}^{n} n \binom{n-1}{k-1} = n \sum_{j=0}^{n-1} \binom{n-1}{j} = n 2^{n-1}$$

Setzen wir diese zurück in den Ausdruck für $T(n)$ ein:
$$T(n) = c_1 \cdot n 2^n + c_2 \cdot n 2^{n-1} = \left( c_1 + \frac{c_2}{2} \right) n 2^n$$

Somit ist die asymptotische Zeitkomplexität eng begrenzt:
$$T(n) = \Theta(n 2^n)$$

### Platzkomplexität

Wir analysieren die Platzkomplexität durch Unterscheidung zwischen Hilfsplatzbedarf und Gesamtplatzbedarf.

#### Hilfsplatzbedarf
Der Hilfsplatzbedarf bezieht sich auf den temporären Speicher, der vom Algorithmus zugewiesen wird, exklusive des Speichers, der für die Speicherung des Endergebnisses erforderlich ist.
* Die Schleifenvariablen $m$ und $i$ benötigen $O(1)$ Platz.
* Die temporäre Liste `subset` speichert zu jedem Zeitpunkt höchstens $n$ Elemente, bevor sie an die Ergebnisliste angehängt wird.
* Es wird kein rekursiver Aufruf-Stack verwendet, was bedeutet, dass die Tiefe des Aufruf-Stacks $O(1)$ beträgt.

Somit ist die Hilfsplatzkomplexität:
$$S_{\text{aux}}(n) = O(n)$$

Wenn der Algorithmus die generierten Teilmengen direkt in einen Ausgabestrom oder Puffer schreibt, ohne das zwischenzeitliche `subset`-Array im Speicher zu halten (z. B. mittels eines Generator-Musters), reduziert sich die Hilfsplatzkomplexität auf:
$$S_{\text{aux}}(n) = O(1)$$

#### Gesamtplatzbedarf
Die Gesamtplatzkomplexität beinhaltet den Speicher, der zur Repräsentation der Ausgabe $\mathcal{P}(S_A)$ erforderlich ist. Die Ausgabe besteht aus $2^n$ Listen. Die Gesamtzahl der über alle Listen gespeicherten Elemente beträgt:
$$\sum_{k=0}^{n} \binom{n}{k} k = n 2^{n-1}$$

Daher ist die Gesamtplatzkomplexität:
$$S_{\text{total}}(n) = \Theta(n 2^n)$$