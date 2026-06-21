# Formale mathematische Spezifikation: Erweiterter Euklidischer Algorithmus

## 1. Definitionen und Notation

Sei $\mathbb{Z}$ die Menge der ganzen Zahlen. Wir definieren den Eingabebereich als ein Paar $(a, b) \in \mathbb{Z}_{\ge 0} \times \mathbb{Z}_{\ge 0}$, wobei $(a, b) \neq (0, 0)$.

Der Algorithmus berechnet ein Triplett $(g, x, y) \in \mathbb{Z} \times \mathbb{Z} \times \mathbb{Z}$, sodass:
1. $g = \gcd(a, b)$, wobei $\gcd(a, b)$ die eindeutige nicht-negative ganze Zahl ist, die folgende Bedingungen erfüllt:
   - $g \mid a$ und $g \mid b$.
   - Für jedes $d \in \mathbb{Z}$ gilt: Wenn $d \mid a$ und $d \mid b$, dann $d \mid g$.
2. Das Triplett erfüllt die Bézout-Identität: $ax + by = g$.

Der Zustandsraum $\mathcal{S}$ der iterativen Implementierung ist durch das Tupel $(r_i, s_i, t_i)$ definiert, welches den Rest und die Koeffizienten im Schritt $i$ repräsentiert, sodass $r_i = a s_i + b t_i$ gilt.

## 2. Algebraische Charakterisierung

Der Algorithmus basiert auf dem euklidischen Divisionssatz. Für beliebige $a, b \in \mathbb{Z}$ mit $b > 0$ existieren eindeutige $q, r \in \mathbb{Z}$, sodass $a = bq + r$ und $0 \le r < b$ gilt.

### Rekurrenz
Der $\gcd$ erfüllt die Rekurrenz:
$\gcd(a, b) = \gcd(b, a \pmod b)$
Mit dem Induktionsanfang $\gcd(a, 0) = a$.

Um die Koeffizienten $(x, y)$ so zu erhalten, dass $ax + by = \gcd(a, b)$ gilt, betrachten wir den Übergang vom rekursiven Schritt. Sei $(g, x_1, y_1)$ die Lösung für $(b, a \pmod b)$, sodass:
$b x_1 + (a \pmod b) y_1 = g$

Durch Einsetzen von $a \pmod b = a - \lfloor \frac{a}{b} \rfloor b$ ergibt sich:
$b x_1 + (a - \lfloor \frac{a}{b} \rfloor b) y_1 = g$
$a(y_1) + b(x_1 - \lfloor \frac{a}{b} \rfloor y_1) = g$

Somit lautet die Aktualisierungsregel für die Koeffizienten:
$x = y_1$
$y = x_1 - \lfloor \frac{a}{b} \rfloor y_1$

### Schleifeninvariante
Für die iterative Implementierung seien $(r_0, r_1) = (a, b)$, $(s_0, s_1) = (1, 0)$ und $(t_0, t_1) = (0, 1)$. In jeder Iteration $i$ gelten die folgenden Invarianten:
1. $r_i = a s_i + b t_i$
2. $\gcd(r_i, r_{i+1}) = \gcd(a, b)$

Der Algorithmus terminiert beim Index $k$, an dem $r_{k+1} = 0$ gilt, was $r_k = \gcd(a, b)$ liefert.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität wird durch die Anzahl der durchgeführten Divisionen bestimmt, welche identisch mit der des Standard-Euklid-Algorithmus ist. Nach dem Satz von Lamé ist die Anzahl der Schritte $n$, die zur Berechnung von $\gcd(a, b)$ erforderlich sind, durch die Anzahl der Ziffern der kleineren Eingabe beschränkt. Insbesondere gilt für $a > b \ge 1$, dass die Anzahl der Iterationen $O(\log b)$ beträgt.

Da jede Iteration eine konstante Anzahl an arithmetischen Operationen (Division, Multiplikation, Subtraktion) umfasst, ergibt sich die gesamte Zeitkomplexität zu:
$T(a, b) = O(\log(\min(a, b)))$

### Platzkomplexität
- **Rekursive Implementierung:** Der Algorithmus benötigt einen Call Stack mit einer Tiefe, die der Anzahl der rekursiven Schritte entspricht. Da die Anzahl der Schritte $O(\log(\min(a, b)))$ beträgt, ist die zusätzliche Platzkomplexität $O(\log(\min(a, b)))$.
- **Iterative Implementierung:** Der Algorithmus verwaltet eine konstante Anzahl an Variablen $(r, s, t, q)$, unabhängig von der Eingabegröße. Daher beträgt die zusätzliche Platzkomplexität $O(1)$.

Die bereitgestellte Implementierung ist iterativ und belegt $O(1)$ zusätzlichen Speicherplatz, obwohl in der Problemstellung angemerkt wird, dass die rekursive Logik aufgrund ihrer mathematischen Eleganz häufig verwendet wird.