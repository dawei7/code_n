# Formale mathematische Spezifikation: Multiplikation zweier Ganzzahlen ohne Multiplikationsoperator (Russische Bauernmultiplikation)

## 1. Definitionen und Notation

Seien $a, b \in \mathbb{Z}$ die beiden ganzzahligen Eingaben für den Algorithmus.
Der Algorithmus berechnet eine Ganzzahl $P \in \mathbb{Z}$, sodass $P = a \cdot b$ gilt.

Der Zustand des Algorithmus ist zu jedem Zeitpunkt durch ein Tupel von Variablen $(s, x, y, R)$ definiert, wobei:
*   $s \in \{0, 1\}$ ein boolesches Flag ist, das das Vorzeichen des finalen Produkts angibt. $s=1$, falls das Produkt negativ sein soll, andernfalls $s=0$.
*   $x \in \mathbb{N}_0$ der aktuelle Multiplikand ist, der eine skalierte Version von $|a|$ darstellt.
*   $y \in \mathbb{N}_0$ der aktuelle Multiplikator ist, der eine schrittweise reduzierte Version von $|b|$ darstellt.
*   $R \in \mathbb{N}_0$ das akkumulierte Teilprodukt ist.

**Anfangszustand:**
Der Algorithmus initialisiert seine Zustandsvariablen basierend auf den Eingaben $a$ und $b$:
*   $s_0 = 1$, falls $(a < 0 \land b \ge 0) \lor (a \ge 0 \land b < 0)$, ansonsten $s_0 = 0$. Dies kann als $s_0 = (a < 0) \oplus (b < 0)$ ausgedrückt werden.
*   $x_0 = |a|$.
*   $y_0 = |b|$.
*   $R_0 = 0$.

**Operationen:**
Der Algorithmus verwendet die folgenden Operationen:
*   $|z|$: Absolutbetrag einer Ganzzahl $z$.
*   $z \pmod 2$: Der Rest bei Division von $z$ durch 2 (äquivalent zu bitweisem AND mit 1, $z \text{ & } 1$).
*   $z \leftarrow z + w$: Ganzzahlige Addition.
*   $z \leftarrow 2z$: Linker Bit-Shift (äquivalent zu $z \text{ << } 1$).
*   $z \leftarrow \lfloor z/2 \rfloor$: Ganzzahlige Division durch 2 (äquivalent zu rechtem Bit-Shift, $z \text{ >> } 1$).

## 2. Algebraische Charakterisierung

Der Algorithmus berechnet das Produkt $P' = |a| \cdot |b|$ durch iterative Zerlegung des Multiplikators $y$ in seine Binärdarstellung. Sei $y_0 = \sum_{i=0}^{m-1} c_i 2^i$, wobei $c_i \in \{0, 1\}$ die Binärziffern von $y_0$ sind und $m = \lfloor \log_2 y_0 \rfloor + 1$ (falls $y_0 > 0$). Das Zielprodukt $P'$ kann wie folgt ausgedrückt werden:
$$P' = x_0 \cdot y_0 = x_0 \cdot \sum_{i=0}^{m-1} c_i 2^i = \sum_{i=0}^{m-1} (x_0 \cdot c_i \cdot 2^i)$$

Der Algorithmus erhält eine Schleifeninvariante aufrecht, die die Korrektheit sicherstellt. Seien $(x_k, y_k, R_k)$ die Zustandsvariablen zu Beginn der Iteration $k$ der Hauptschleife.

**Schleifeninvariante:**
Zu Beginn jeder Iteration $k$ (bevor die Schleifenbedingung $y_k > 0$ ausgewertet wird), gilt die folgende Invariante:
$$P' = x_k \cdot y_k + R_k$$

**Beweis der Invariante:**
*   **Induktionsanfang (k=0):**
    Aus dem Anfangszustand folgt $x_0 = |a|$, $y_0 = |b|$ und $R_0 = 0$.
    Einsetzen in die Invariante ergibt: $x_0 \cdot y_0 + R_0 = |a| \cdot |b| + 0 = P'$.
    Die Invariante gilt für $k=0$.

*   **Induktionsschritt:**
    Angenommen, die Invariante gilt zu Beginn der Iteration $k$: $P' = x_k \cdot y_k + R_k$.
    Wir müssen zeigen, dass sie zu Beginn der Iteration $k+1$ gilt, d. h. $P' = x_{k+1} \cdot y_{k+1} + R_{k+1}$.

    Innerhalb der Schleife sind die Aktualisierungen der Zustandsvariablen wie folgt:
    1.  Falls $y_k \pmod 2 = 1$ (d. h. das niederwertigste Bit von $y_k$ ist 1):
        $R_{k+1}' = R_k + x_k$.
    2.  Sonst ($y_k \pmod 2 = 0$):
        $R_{k+1}' = R_k$.
    3.  $x_{k+1} = 2x_k$.
    4.  $y_{k+1} = \lfloor y_k/2 \rfloor$.

    Sei $y_k = 2q + c_0$, wobei $c_0 = y_k \pmod 2$. Dann ist $y_{k+1} = q = (y_k - c_0)/2$.
    Die Aktualisierung von $R$ kann kompakt als $R_{k+1}' = R_k + c_0 x_k$ geschrieben werden.

    Nun setzen wir diese aktualisierten Werte in die Invariante für $k+1$ ein:
    $$x_{k+1} \cdot y_{k+1} + R_{k+1}' = (2x_k) \cdot \left(\frac{y_k - c_0}{2}\right) + (R_k + c_0 x_k)$$
    $$= x_k (y_k - c_0) + R_k + c_0 x_k$$
    $$= x_k y_k - c_0 x_k + R_k + c_0 x_k$$
    $$= x_k y_k + R_k$$
    Nach der Induktionsvoraussetzung gilt $x_k y_k + R_k = P'$.
    Daher gilt $x_{k+1} \cdot y_{k+1} + R_{k+1}' = P'$. Die Invariante gilt für $k+1$.

**Terminierung:**
Die Schleife terminiert, wenn $y_k = 0$. An diesem Punkt wird die Invariante $P' = x_k \cdot y_k + R_k$ zu $P' = x_k \cdot 0 + R_k = R_k$.
Somit enthält die Variable $R_k$ den Wert des absoluten Produkts $P'$.
Das Endergebnis $P$ wird dann durch Anwendung des anfänglichen Vorzeichen-Flags $s_0$ bestimmt:
$$P = (-1)^{s_0} \cdot R_k$$
Dies vervollständigt den Korrektheitsbeweis.

## 3. Komplexitätsanalyse

### Zeitkomplexität

Die primäre Rechenarbeit des Algorithmus wird innerhalb der `while`-Schleife verrichtet.
Sei $y_0 = |b|$ der Anfangswert des Multiplikators (oder $\min(|a|, |b|)$, falls optimiert).
In jeder Iteration der Schleife wird der Wert von $y$ durch $y \leftarrow \lfloor y/2 \rfloor$ aktualisiert. Diese Operation entfernt effektiv das niederwertigste Bit von $y$.
Die Schleife läuft, solange $y > 0$.
Die Anzahl der Iterationen entspricht genau der Anzahl der Bits, die zur Darstellung von $y_0$ erforderlich sind (ohne führende Nullen), bzw. $\lfloor \log_2 y_0 \rfloor + 1$ für $y_0 > 0$. Falls $y_0 = 0$, wird die Schleife 0-mal ausgeführt.
Somit ist die Anzahl der Iterationen proportional zu $\log_2 y_0$.

Innerhalb jeder Iteration werden folgende Operationen durchgeführt:
*   Bitweises AND (`y & 1`): $O(1)$
*   Addition (`result += x`): $O(1)$
*   Linker Bit-Shift (`x <<= 1`): $O(1)$
*   Rechter Bit-Shift (`y >>= 1`): $O(1)$

Diese Operationen werden unter der Standardannahme von Ganzzahltypen fester Breite (z. B. 32-Bit oder 64-Bit Ganzzahlen) als konstante Zeit $O(1)$ betrachtet.
Daher ist die gesamte Zeitkomplexität das Produkt aus der Anzahl der Iterationen und der Zeit pro Iteration:
$$T(y_0) = (\lfloor \log_2 y_0 \rfloor + 1) \cdot O(1) = O(\log y_0)$$
Falls der Algorithmus dahingehend optimiert ist, das Minimum von $|a|$ und $|b|$ als Multiplikator zu verwenden, sei $N = \min(|a|, |b|)$. Die Zeitkomplexität beträgt dann $O(\log N)$.

### Platzkomplexität

Der Algorithmus verwendet eine feste Anzahl an Variablen: `negative` ($s$), `x`, `y` und `result` ($R$).
Diese Variablen speichern ganzzahlige Werte. Unter der Annahme von Ganzzahltypen fester Breite ist der für jede Variable benötigte Speicherplatz konstant, unabhängig von der Größe der Eingabezahlen $a$ und $b$.
Es werden keine zusätzlichen Datenstrukturen (wie Arrays, Listen oder rekursive Aufruf-Stacks) verwendet, die mit der Eingabegröße wachsen würden.
Daher ist die zusätzliche Platzkomplexität $O(1)$.
Die gesamte Platzkomplexität ist ebenfalls $O(1)$.