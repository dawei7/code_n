# Größter gemeinsamer Teiler (Euklidischer Algorithmus)

| | |
|---|---|
| **ID** | `math_01` |
| **Kategorie** | math |
| **Komplexität (erforderlich)** | $O(log(min(A, B)$)) Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 2/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **Wikipedia** | [Euklidischer Algorithmus](https://de.wikipedia.org/wiki/Euklidischer_Algorithmus) |

## Problemstellung

Gegeben sind zwei positive ganze Zahlen A und B. Bestimme deren größten gemeinsamen Teiler (ggT).
Der ggT ist die größte positive ganze Zahl, durch die sowohl A als auch B ohne Rest teilbar sind.

**Eingabe:** Zwei ganze Zahlen `A` und `B`.
**Ausgabe:** Eine ganze Zahl, die den ggT darstellt.

## Anwendungsbereiche

- Zur Vereinfachung von Brüchen (Zähler und Nenner durch ihren ggT teilen).
- Als grundlegender Baustein für das kleinste gemeinsame Vielfache (kgV), das modulare multiplikative Inverse und die RSA-Kryptographie.
- Einer der ältesten erhaltenen Algorithmen der Mathematik (beschrieben von Euklid um 300 v. Chr.).

## Ansatz

**1. Die grundlegende Subtraktionsregel:**
Wenn eine Zahl C sowohl A als auch B (wobei A > B) ohne Rest teilt, dann muss C auch deren Differenz (A - B) ohne Rest teilen!
Warum? Wenn A = X \cdot C und B = Y \cdot C, dann ist A - B = (X - Y) \cdot C.
Daher gilt: \text{GCD}(A, B) = \text{GCD}(A - B, B).
Wir könnten einfach fortlaufend die kleinere Zahl von der größeren subtrahieren, bis beide gleich sind. Diese Zahl ist dann der ggT!
*(Beispiel: \text{GCD}(20, 8) -> \text{GCD}(12, 8) -> \text{GCD}(4, 8) -> \text{GCD}(4, 4) = 4).*

**2. Die Modulo-Optimierung:**
Wiederholte Subtraktion ist sehr langsam, wenn A riesig und B winzig ist (z. B. A=1000000, B=2). Wir müssten 2 eine halbe Million Mal subtrahieren!
Wiederholte Subtraktion ist mathematisch identisch mit der **Modulo**-Operation!
Anstatt A - B - B - B zu rechnen, verwenden wir einfach A \pmod B, was uns sofort den Rest liefert, nachdem B so oft wie möglich subtrahiert wurde!
Daher lautet das Kerntheorem:
$\text{GCD}(A, B) = \text{GCD}(B, A \pmod B)

**3. Der Induktionsanfang (Basis):**
Wenn der Rest `0` wird, bedeutet dies, dass die kleinere Zahl die größere perfekt geteilt hat! Die Zahl, die an diesem Punkt ungleich null ist, ist unser finaler ggT!
\text{GCD}(X, 0) = X.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for math_01: GCD (Euclidean algorithm).

Repeatedly replace (a, b) with (b, a mod b) until b is 0; the
last non-zero a is the gcd. O(log min(a, b)) time.
"""


def solve(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a
```

</details>

## Durchlauf

`A = 48`, `B = 18`.

1. `b != 0` (18 != 0).
   - `remainder = 48 % 18 = 12`. (18 passt zweimal in 48, Rest 12).
   - `a = 18`.
   - `b = 12`.
2. `b != 0` (12 != 0).
   - `remainder = 18 % 12 = 6`.
   - `a = 12`.
   - `b = 6`.
3. `b != 0` (6 != 0).
   - `remainder = 12 % 6 = 0`. (6 passt genau zweimal in 12!).
   - `a = 6`.
   - `b = 0`.
4. `b == 0`. Die Schleife terminiert.
Rückgabe `a = 6`. ✓

*(Hinweis: Was passiert, wenn wir anfangs `A = 18, B = 48` übergeben? Der allererste Schritt berechnet `18 % 48 = 18`. Also `a=48` und `b=18`. Die Werte werden also in genau einem Schritt automatisch in die richtige Reihenfolge getauscht!)*

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(log(\min(A, B)$)) | $O(1)$ |
| **Schlechtester Fall** | $O(log(\min(A, B)$)) | $O(1)$ |

Gabriel Lamé bewies 1844, dass der Euklidische Algorithmus höchstens $5 \times \text{Anzahl der Stellen von } \min(A,B)$ Schritte benötigt.
Das absolute Worst-Case-Szenario tritt ein, wenn A und B aufeinanderfolgende Fibonacci-Zahlen sind.
Da der Rest alle zwei Schritte um mindestens die Hälfte abnimmt, ist die Zeitkomplexität strikt $O(\log(\min(A, B)))$.
Die Platzkomplexität beträgt $O(1)$ für den iterativen Ansatz. (Bei einer rekursiven Implementierung wird $O(\log(\min(A,B)))$ Platz auf dem Call-Stack benötigt).

## Varianten & Optimierungen

- **Erweiterter Euklidischer Algorithmus (`math_07`):** Findet nicht nur den ggT, sondern auch die ganzzahligen Koeffizienten x und y, sodass A \cdot x + B \cdot y = \text{GCD}(A, B) (Bézout-Identität). Dies ist absolut entscheidend für die Bestimmung des modularen multiplikativen Inversen.
- **Binärer ggT-Algorithmus (Steins Algorithmus):** Eine Optimierung, die den teuren Modulo-Operator `%` vollständig vermeidet und sich ausschließlich auf bitweise Verschiebungen `>> 1` und Subtraktion stützt. Er ist auf Hardware-Ebene schneller, wird aber in Coding-Interviews selten benötigt.

## Anwendungsbereiche in der Praxis

- **RSA Public-Key-Kryptographie:** Der ggT wird verwendet, um sicherzustellen, dass der öffentliche Exponent `e` teilerfremd zur Eulerschen Phi-Funktion \phi(N) ist, eine zwingend erforderliche mathematische Eigenschaft, damit die Verschlüsselung umkehrbar ist.

## Verwandte Algorithmen in cOde(n)

- **[math_07 - Erweiterter Euklidischer Algorithmus](math_07_extended-euclidean-algorithm.md)** — Die erweiterte Version, die Bézout-Koeffizienten berechnet.
- **[greedy_11 - Ägyptischer Bruch](../greedy/greedy_11_egyptian-fraction.md)** — Ein Algorithmus, der stark auf den ggT angewiesen ist, um Brüche zu vereinfachen und Integer-Überläufe zu verhindern.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) erstellt wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*