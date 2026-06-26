# Formale mathematische Spezifikation: Division zweier Ganzzahlen ohne Divisionsoperator

## 1. Definitionen und Notation

Dieser Abschnitt definiert die mathematischen Entitäten, ihre Definitionsbereiche und die in der gesamten Spezifikation verwendete Notation.

*   **Eingabebereich:**
    *   Sei $D \in \mathbb{Z}$ der Dividend.
    *   Sei $S \in \mathbb{Z}$ der Divisor.
    *   Der Definitionsbereich für $D$ und $S$ ist die Menge der 32-Bit vorzeichenbehafteten Ganzzahlen, bezeichnet als $\mathcal{I} = [-2^{31}, 2^{31}-1]$.
    *   **Bedingung:** $S \neq 0$.
*   **Ausgabebereich:**
    *   Sei $Q \in \mathbb{Z}$ der Quotient.
    *   Die Ausgabe $Q$ muss ebenfalls innerhalb von $\mathcal{I}$ liegen, unter Beachtung einer spezifischen Regel für den Überlauf.
*   **Konstanten:**
    *   $\text{BIT\_WIDTH} = 32$: Die Anzahl der Bits, die für die Ganzzahldarstellung verwendet werden.
    *   $\text{MAX\_SIGNED\_INT} = 2^{31}-1$: Der Maximalwert für eine 32-Bit vorzeichenbehaftete Ganzzahl.
    *   $\text{MIN\_SIGNED\_INT} = -2^{31}$: Der Minimalwert für eine 32-Bit vorzeichenbehaftete Ganzzahl.
*   **Interne Zustandsvariablen:**
    *   $N \in \{\text{true}, \text{false}\}$: Ein boolescher Flag, der angibt, ob der endgültige Quotient negativ sein sollte.
    *   $a \in \mathbb{N}_0$: Der aktuelle Absolutwert des verbleibenden Dividenden.
    *   $b \in \mathbb{N}_0$: Der Absolutwert des Divisors.
    *   $q \in \mathbb{N}_0$: Der akkumulierte absolute Quotient.
    *   $p \in \mathbb{N}_0$: Ein Bit-Shift-Potenzzähler, der $2^p$ repräsentiert.

## 2. Algebraische Charakterisierung

Der Algorithmus berechnet die Ganzzahldivision $D/S$ (mit Rundung gegen Null), indem er zuerst das Vorzeichen des Ergebnisses bestimmt, dann den Absolutwert des Quotienten mittels Bit-Shifts und Subtraktionen berechnet und schließlich das korrekte Vorzeichen anwendet sowie einen potenziellen Überlauf behandelt.

**2.1. Vorverarbeitung und Vorzeichenbestimmung:**
1.  **Vorzeichenbestimmung:** Ein boolescher Flag $N$ wird auf $\text{true}$ gesetzt, wenn $D$ und $S$ unterschiedliche Vorzeichen haben, andernfalls auf $\text{false}$. Dies kann formal ausgedrückt werden als:
    $N = (D < 0) \oplus (S < 0)$, wobei $\oplus$ die exklusive ODER-Operation (XOR) bezeichnet.
2.  **Initialisierung der Absolutwerte:** Der Algorithmus arbeitet mit den Absolutwerten von Dividend und Divisor, um die Kernlogik der Division zu vereinfachen.
    $a_0 = |D|$
    $b_0 = |S|$
    *Hinweis: In einer strikten 32-Bit-Umgebung (z. B. C/Java) würde die Berechnung von $|-2^{31}|$ zu einem Überlauf führen. Die Python-Implementierung von `abs()` handhabt dies, indem implizit größere Ganzzahltypen verwendet werden. Für diese Spezifikation nehmen wir an, dass $|D|$ wohldefiniert ist und in einen ausreichend großen vorzeichenlosen Ganzzahltyp für Zwischenberechnungen passt.*
3.  **Initialisierung des Quotienten-Akkumulators:**
    $q_0 = 0$
4.  **Initialisierung des Potenzzählers:**
    $p_{init} = \text{BIT\_WIDTH}-1 = 31$.

**2.2. Bestimmung der initialen maximalen Potenz ($P_{max}$):**
Der Algorithmus identifiziert zuerst die größte Ganzzahl $P_{max}$, sodass $b_0 \cdot 2^{P_{max}} \le a_0$. Dies wird durch iteratives Dekrementieren von $p$ ausgehend von $p_{init}$ erreicht:
Sei $p_{curr} \leftarrow p_{init}$.
Solange $b_0 \cdot 2^{p_{curr}} > a_0$:
  $p_{curr} \leftarrow p_{curr} - 1$.
Der Wert von $p_{curr}$ nach Beendigung dieser Schleife ist $P_{max}$. Wenn $b_0 > a_0$, dann wird $P_{max}$ kleiner als $0$ sein, was korrekt zu einem absoluten Quotienten von $0$ führt.

**2.3. Iterative Subtraktion und Quotienten-Akkumulation:**
Die Kernlogik der Division subtrahiert iterativ Vielfache von $b_0$ (speziell $b_0 \cdot 2^p$) vom verbleibenden Dividenden $a$ und akkumuliert die entsprechenden Potenzen von 2 in $q$.
Seien $a^{(p)}$ und $q^{(p)}$ die Werte von $a$ und $q$ zu Beginn einer Iteration, in der der Potenzzähler $p$ ist.
Die Schleife läuft für $p$ von $P_{max}$ abwärts bis $0$:
Für $p \in \{P_{max}, P_{max}-1, \dots, 0\}$:
  Falls $b_0 \cdot 2^p \le a^{(p)}$:
    $a^{(p-1)} = a^{(p)} - (b_0 \cdot 2^p)$
    $q^{(p-1)} = q^{(p)} + 2^p$
  Sonst:
    $a^{(p-1)} = a^{(p)}$
    $q^{(p-1)} = q^{(p)}$
Der endgültige absolute Quotient ist $Q_{abs} = q^{(-1)}$.

**Schleifeninvariante für die iterative Subtraktionsschleife:**
Zu Beginn jeder Iteration gelten für eine gegebene Potenz $p \in \{P_{max}, \dots, 0\}$ die folgenden Bedingungen:
1.  **Zerlegung des Dividenden:** Der initiale absolute Dividend $a_0$ kann ausgedrückt werden als die Summe aus dem akkumulierten Quotienten multipliziert mit dem Divisor, dem aktuellen Rest und dem Beitrag der noch zu bestimmenden Bits des Quotienten:
    $a_0 = (q^{(p)} + \sum_{j=p+1}^{P_{max}} \delta_j \cdot 2^j) \cdot b_0 + a^{(p)}$,
    wobei $\delta_j \in \{0,1\}$ die Bits des Quotienten für Potenzen $j > p$ sind.
2.  **Schranke für den Rest:** Der aktuelle Rest $a^{(p)}$ ist nicht-negativ und strikt kleiner als der nächste potenzielle Subtraktionsterm $b_0 \cdot 2^{p+1}$:
    $0 \le a^{(p)} < b_0 \cdot 2^{p+1}$.
3.  **Quotienten-Akkumulation:** Der akkumulierte Quotient $q^{(p)}$ repräsentiert die Summe der Potenzen von 2, die den bereits bestimmten Bits des Quotienten für Potenzen größer als $p$ entsprechen:
    $q^{(p)} = \sum_{j=p+1}^{P_{max}} \delta_j \cdot 2^j$.

**Terminierung:**
Die Schleife terminiert, wenn $p < 0$. An diesem Punkt ist $p=-1$.
Aus Invariante 1 folgt: $a_0 = Q_{abs}^{(-1)} \cdot b_0 + a^{(-1)}$, wobei $Q_{abs}^{(-1)}$ der endgültige akkumulierte Quotient ist.
Aus Invariante 3 folgt: $Q_{abs}^{(-1)} = \sum_{j=0}^{P_{max}} \delta_j \cdot 2^j$. Dies ist der endgültige absolute Quotient $Q_{abs}$.
Aus Invariante 2 folgt: $0 \le a^{(-1)} < b_0 \cdot 2^0 = b_0$. Dies bestätigt, dass $a^{(-1)}$ der Rest $R_{abs}$ ist, sodass $0 \le R_{abs} < b_0$.
Daher gilt $Q_{abs} = \lfloor a_0 / b_0 \rfloor$ und $R_{abs} = a_0 \pmod{b_0}$.

**2.4. Konstruktion des Endergebnisses und Überlaufbehandlung:**
Sei $Q_{abs}$ der endgültige Wert von $q$, der aus der iterativen Subtraktion gewonnen wurde.
Der rohe Quotient $Q_{raw}$ wird durch Anwendung des Vorzeichens bestimmt:
$Q_{raw} = \begin{cases} -Q_{abs} & \text{falls } N = \text{true} \\ Q_{abs} & \text{falls } N = \text{false} \end{cases}$
Schließlich muss der Algorithmus die Bereichsbeschränkung für 32-Bit vorzeichenbehaftete Ganzzahlen einhalten. Die endgültige Ausgabe $Q_{final}$ ist definiert als:
$Q_{final} = \begin{cases} \text{MAX\_SIGNED\_INT} & \text{falls } Q_{raw} > \text{MAX\_SIGNED\_INT} \\ Q_{raw} & \text{sonst} \end{cases}$
Dies behandelt den spezifischen Fall, in dem $D = \text{MIN\_SIGNED\_INT}$ und $S = -1$, was $Q_{raw} = 2^{31}$ ergeben würde, was $\text{MAX\_SIGNED\_INT}$ überschreitet.

## 3. Komplexitätsanalyse

**3.1. Zeitkomplexität:**
Sei $\text{BIT\_WIDTH}$ die Anzahl der Bits, die die Ganzzahlen repräsentieren (z. B. 32).
Sei $Q_{abs} = \lfloor |D|/|S| \rfloor$ der Absolutwert des Quotienten.

1.  **Vorverarbeitung:** Operationen zur Vorzeichenbestimmung und Initialisierung der Absolutwerte sind in konstanter Zeit, $O(1)$.
2.  **Bestimmung der initialen maximalen Potenz:** Die erste `while`-Schleife iteriert und dekrementiert $p$ von $\text{BIT\_WIDTH}-1$ bis $b_0 \cdot 2^p \le a_0$. Im Schlechtesten Fall nimmt $p$ von $\text{BIT\_WIDTH}-1$ bis auf etwa $\lfloor \log_2(a_0/b_0) \rfloor$ ab. Die Anzahl der Iterationen ist durch $\text{BIT\_WIDTH}$ beschränkt. Somit benötigt diese Phase $O(\text{BIT\_WIDTH})$ Zeit.
3.  **Iterative Subtraktion und Quotienten-Akkumulation:** Die zweite `while`-Schleife iteriert $p$ von $P_{max}$ abwärts bis $0$. Der Wert von $P_{max}$ ist höchstens $\text{BIT\_WIDTH}-1$. Daher führt diese Schleife höchstens $\text{BIT\_WIDTH}$ Iterationen durch. Jede Iteration beinhaltet einen Bit-Shift, einen Vergleich, eine Subtraktion und eine bitweise ODER-Operation. Für Ganzzahlen fester Breite sind dies alles $O(1)$-Operationen. Somit benötigt auch diese Phase $O(\text{BIT\_WIDTH})$ Zeit.
4.  **Konstruktion des Endergebnisses:** Die Anwendung des Vorzeichens und die Überprüfung auf Überlauf sind $O(1)$-Operationen.

Zusammengefasst ergibt sich die gesamte Zeitkomplexität zu $O(1) + O(\text{BIT\_WIDTH}) + O(\text{BIT\_WIDTH}) + O(1) = O(\text{BIT\_WIDTH})$.
Da $\text{BIT\_WIDTH}$ eine Konstante ist (z. B. 32 für 32-Bit-Ganzzahlen), kann die Zeitkomplexität in Bezug auf die Wortgröße der Maschine als $O(1)$ betrachtet werden.
Genauer gesagt steht die Anzahl der Iterationen in der Hauptschleife in direktem Zusammenhang mit der Anzahl der Bits im absoluten Quotienten $Q_{abs}$. Die Anzahl der Bits in $Q_{abs}$ ist $\lfloor \log_2 Q_{abs} \rfloor + 1$.
Daher ist die Zeitkomplexität $O(\log Q_{abs})$. Da $Q_{abs} \le 2^{31}$, ist dies durch $O(\log 2^{31}) = O(31)$ beschränkt, was konstant ist.

**3.2. Platzkomplexität:**
Der Algorithmus verwendet eine feste Anzahl von Variablen: $D, S, N, a, b, q, p$. Jede dieser Variablen speichert einen einzelnen Ganzzahlwert, dessen Größe durch die Wortgröße der Maschine (z. B. 32 Bit) beschränkt ist. Es werden keine zusätzlichen Datenstrukturen (wie Arrays, Listen oder ein Rekursions-Stack) allokiert, deren Speicherbedarf mit der Größe der Eingabeganzzahlen wächst.
Daher ist die zusätzliche Platzkomplexität $O(1)$. Die gesamte Platzkomplexität, einschließlich des Speichers für die Eingaben, ist ebenfalls $O(1)$.