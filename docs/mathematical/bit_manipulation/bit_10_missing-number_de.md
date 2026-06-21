# Formale mathematische Spezifikation: Fehlende Zahl

## 1. Definitionen und Notation

Sei $A$ das Eingabe-Array, dargestellt als eine Folge von Ganzzahlen $A = (a_0, a_1, \ldots, a_{n-1})$.
Die Länge des Arrays ist $n \in \mathbb{N}$, wobei $n \ge 0$.

Das Problem spezifiziert die folgenden Eigenschaften für die Eingabe:
*   Die Elemente $a_i$ sind paarweise verschiedene Ganzzahlen.
*   Der Wertebereich dieser Ganzzahlen ist $[0, n]$, was bedeutet, dass $a_i \in \{0, 1, \ldots, n\}$ für alle $i \in \{0, 1, \ldots, n-1\}$ gilt.
*   Es gibt $n$ verschiedene Zahlen im Array $A$, die aus der Menge der $n+1$ Ganzzahlen $\{0, 1, \ldots, n\}$ ausgewählt wurden. Folglich fehlt genau eine Zahl aus dieser Menge in $A$.

Sei $S_{expected}$ die vollständige Menge der Ganzzahlen im spezifizierten Bereich:
$S_{expected} = \{k \in \mathbb{Z} \mid 0 \le k \le n\} = \{0, 1, \ldots, n\}$.

Sei $S_{actual}$ die Menge der Ganzzahlen, die im Eingabe-Array $A$ vorhanden sind:
$S_{actual} = \{a_i \mid i \in \{0, 1, \ldots, n-1\}\}$.

Die Ausgabe des Algorithmus ist die eindeutige Ganzzahl $m$, die im Array $A$ fehlt. Formal ist $m$ definiert als:
$m = S_{expected} \setminus S_{actual}$.
Gemäß der Problemstellung ist garantiert, dass $m$ ein einzelnes Element ist.

Wir verwenden die folgende Notation für die bitweise XOR-Operation: $\oplus$.
Der Algorithmus verwendet eine Akkumulatorvariable, bezeichnet als $R$, die mit $n$ initialisiert wird.
Der Schleifenindex ist $i \in \{0, 1, \ldots, n-1\}$.
Das Element am Index $i$ im Array ist $a_i$.

## 2. Algebraische Charakterisierung

Die Korrektheit des Algorithmus beruht auf den fundamentalen Eigenschaften der bitweisen XOR-Operation:
1.  **Kommutativität:** Für beliebige Ganzzahlen $x, y$ gilt $x \oplus y = y \oplus x$.
2.  **Assoziativität:** Für beliebige Ganzzahlen $x, y, z$ gilt $(x \oplus y) \oplus z = x \oplus (y \oplus z)$.
3.  **Neutrales Element:** Für jede Ganzzahl $x$ gilt $x \oplus 0 = x$.
4.  **Selbstinversität:** Für jede Ganzzahl $x$ gilt $x \oplus x = 0$.

Der Algorithmus initialisiert einen Akkumulator $R$ mit dem Wert $n$.
$R_0 = n$.

Anschließend iteriert er durch das Array $A$ von $i=0$ bis $n-1$ und aktualisiert $R$ in jedem Schritt:
$R_{i+1} = R_i \oplus i \oplus a_i$.

Der Endwert des Akkumulators, $R_f$, nach $n$ Iterationen kann als XOR-Summe aller Terme ausgedrückt werden:
$R_f = n \oplus \left( \bigoplus_{i=0}^{n-1} i \right) \oplus \left( \bigoplus_{i=0}^{n-1} a_i \right)$.

Analysieren wir jede Komponente dieser XOR-Summe:
*   Der Term $n$ ist der Initialwert.
*   Der Term $\bigoplus_{i=0}^{n-1} i$ repräsentiert die XOR-Summe aller Indizes von $0$ bis $n-1$.
*   Der Term $\bigoplus_{i=0}^{n-1} a_i$ repräsentiert die XOR-Summe aller Elemente, die im Eingabe-Array $A$ vorhanden sind.

Kombiniert man den Initialwert $n$ mit der XOR-Summe der Indizes, erhält man die XOR-Summe aller Zahlen im erwarteten Bereich $S_{expected}$:
$\bigoplus_{k=0}^{n} k = n \oplus \left( \bigoplus_{i=0}^{n-1} i \right)$.

Daher kann der finale Akkumulatorwert $R_f$ umgeschrieben werden als:
$R_f = \left( \bigoplus_{k=0}^{n} k \right) \oplus \left( \bigoplus_{i=0}^{n-1} a_i \right)$.

Sei $X_{expected} = \bigoplus_{k \in S_{expected}} k = \bigoplus_{k=0}^{n} k$.
Sei $X_{actual} = \bigoplus_{k \in S_{actual}} k = \bigoplus_{i=0}^{n-1} a_i$.

Somit gilt $R_f = X_{expected} \oplus X_{actual}$.

Per Definition ist $S_{expected} = S_{actual} \cup \{m\}$, wobei $m$ die eindeutige fehlende Zahl ist.
Aufgrund der Eigenschaften von XOR (Kommutativität und Assoziativität) kann die XOR-Summe über eine Menge zerlegt werden:
$X_{expected} = \left( \bigoplus_{k \in S_{actual}} k \right) \oplus m = X_{actual} \oplus m$.

Setzt man dies in den Ausdruck für $R_f$ ein:
$R_f = (X_{actual} \oplus m) \oplus X_{actual}$.

Unter Verwendung der Kommutativität und Assoziativität von XOR:
$R_f = (X_{actual} \oplus X_{actual}) \oplus m$.

Anwendung der Selbstinversität ($x \oplus x = 0$):
$R_f = 0 \oplus m$.

Schließlich, Anwendung der Eigenschaft des neutralen Elements ($x \oplus 0 = x$):
$R_f = m$.

Somit berechnet der Algorithmus korrekt die fehlende Zahl $m$.

## 3. Komplexitätsanalyse

### Zeitkomplexität

Sei $T(n)$ die Zeitkomplexität des Algorithmus für ein Eingabe-Array der Länge $n$.

1.  **Initialisierung:** Die Zuweisung `result = n` umfasst eine einzelne Operation mit konstanter Zeit. Dies trägt $O(1)$ zur Gesamtlaufzeit bei.
2.  **Schleifenausführung:** Die `for`-Schleife iteriert $n$-mal, für $i$ von $0$ bis $n-1$.
    *   In jeder Iteration liefert `enumerate(arr)` den Index $i$ und den Wert $v = a_i$. Dies ist eine Operation mit konstanter Zeit für jedes Element.
    *   Die Kernoperation `result ^= i ^ v` umfasst zwei bitweise XOR-Operationen. Unter der Annahme, dass Ganzzahlen in ein Maschinenwort passen, benötigt jede XOR-Operation konstante Zeit, $O(1)$.
    *   Daher benötigt jede Iteration der Schleife $O(1)$ Zeit.
3.  **Return-Anweisung:** Die `return result`-Anweisung ist eine Operation mit konstanter Zeit, $O(1)$.

Summiert man diese Beiträge, ergibt sich die gesamte Zeitkomplexität zu:
$T(n) = O(1) \text{ (Initialisierung)} + n \times O(1) \text{ (Schleifeniterationen)} + O(1) \text{ (Return)}$.
$T(n) = O(1) + O(n) + O(1) = O(n)$.

Formeller ausgedrückt existieren Konstanten $c_1, c_2, c_3 > 0$, sodass:
$T(n) = c_1 + n \cdot c_2 + c_3$.
Für $n \to \infty$ ist $T(n)$ asymptotisch proportional zu $n$.
Somit ist die Zeitkomplexität $\Theta(n)$, was $O(n)$ impliziert.

### Platzkomplexität

Sei $S(n)$ die zusätzliche Platzkomplexität (Auxiliary Space) des Algorithmus für ein Eingabe-Array der Länge $n$. Der zusätzliche Speicher bezieht sich auf den vom Algorithmus zusätzlich belegten Speicherplatz, exklusive der Eingabe selbst.

1.  **Variablen:** Der Algorithmus verwendet eine einzelne Ganzzahlvariable `result`, um die akkumulierte XOR-Summe zu speichern. Diese Variable belegt eine konstante Menge an Speicher, typischerweise ein Maschinenwort, unabhängig von der Eingabegröße $n$.
2.  **Schleifenvariablen:** Der Schleifenindex `i` und das aktuelle Array-Element `v` (aus `enumerate`) belegen ebenfalls konstanten Speicherplatz.
3.  **Keine zusätzlichen Datenstrukturen:** Der Algorithmus allokiert keine zusätzlichen Datenstrukturen (wie Listen, Dictionaries etc.), deren Größe von $n$ abhängt.

Daher ist der gesamte zusätzliche Speicherplatz, der vom Algorithmus verwendet wird, konstant:
$S(n) = O(1)$.