# Karatsuba-Multiplikation

| | |
|---|---|
| **ID** | `dc_04` |
| **Kategorie** | divide_conquer |
| **Komplexität (erforderlich)** | $O(N^1.58)$ Zeit, $O(N)$ Platz |
| **Schwierigkeit** | 8/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **Wikipedia** | [Karatsuba-Algorithmus](https://en.wikipedia.org/wiki/Karatsuba_algorithm) |

## Problemstellung

Gegeben sind zwei extrem große Zahlen `X` und `Y`, die als Strings (oder massive Integer-Arrays) dargestellt sind. Multiplizieren Sie diese. Nehmen Sie an, dass die Zahlen N Stellen haben und nicht in Standard-64-Bit-Integer-Variablen passen.
Geben Sie das Produkt zurück.

**Eingabe:** Zwei Integer (oder Strings) `x` und `y`.
**Ausgabe:** Deren Produkt.

## Wann man es verwendet

- Um außergewöhnlich große Zahlen (BigInts) schneller zu multiplizieren als mit der traditionellen "Schriftlichen Multiplikation" (Grade School Method).
- Ein klassisches Problem der theoretischen Informatik, das demonstriert, wie Algebra mathematisch rekursive Aufrufe eliminieren kann, um sub-quadratische Zeitschranken zu erreichen.

## Ansatz

**1. Der Ansatz der schriftlichen Multiplikation ($O(N^2)$):**
Wenn wir zwei N-stellige Zahlen von Hand multiplizieren, multiplizieren wir jede Ziffer der oberen Zahl mit jeder Ziffer der unteren Zahl. Für zwei 4-stellige Zahlen erfordert dies 4 x 4 = 16 einstellige Multiplikationen. Dies entspricht einer Zeitkomplexität von fest $O(N^2)$.

**2. Naives Divide and Conquer ($O(N^2)$):**
Teilen wir beide Zahlen in zwei Hälften.
Wenn X = 1234, können wir es schreiben als 12 x 10^2 + 34.
Sei X = a x 10^{N/2} + b
Sei Y = c x 10^{N/2} + d

Wenn wir sie algebraisch multiplizieren:
X x Y = (a \cdot 10^{N/2} + b) x (c \cdot 10^{N/2} + d)
X x Y = ac \cdot 10^N + (ad + bc) \cdot 10^{N/2} + bd

Um diese Gleichung zu lösen, müssen wir 4 separate rekursive Multiplikationen berechnen: ac, ad, bc und bd.
Gemäß dem Master-Theorem evaluiert T(N) = 4T(N/2) + $O(N)$ zu exakt $O(N^2)$. Wir haben die Geschwindigkeit überhaupt nicht verbessert!

**3. Der Karatsuba-Trick ($O(N^{1.58})$):**
Im Jahr 1960 erkannte Anatoly Karatsuba, dass wir ad und bc gar nicht separat berechnen müssen!
Beachten Sie, dass:
(a + b) x (c + d) = ac + ad + bc + bd

Wenn wir ac und bd von diesem Ergebnis subtrahieren, bleibt genau (ad + bc) übrig!
(ad + bc) = (a + b)(c + d) - ac - bd

Warum ist das revolutionär?
Weil wir ac und bd ohnehin für die äußeren Teile der Hauptgleichung berechnen MÜSSEN!
Anstatt 4 rekursiver Multiplikationen (ac, ad, bc, bd) benötigt Karatsuba nur **3** rekursive Multiplikationen:
1. Z_0 = ac
2. Z_1 = bd
3. Z_2 = (a+b) x (c+d)

Der mittlere Term ist dann einfach Z_2 - Z_0 - Z_1.
Die neue Rekursionsgleichung lautet T(N) = 3T(N/2) + $O(N)$.
Nach dem Master-Theorem beträgt die Zeitkomplexität $O(N^{log_2(3)})$, was ungefähr $O(N^{1.585})$ entspricht!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dc_04: Karatsuba Multiplication.

Multiply two non-negative integers using Karatsuba's
"""


def solve(x, y, n):
    """Karatsuba multiplication: x * y.

    Recursive 3-way multiplication beats the schoolbook 4-way
    multiplication by trading one extra add/subtract for one
    fewer recursive product.
    """
    if x < 10 or y < 10:
        return x * y
    m = max(len(str(x)), len(str(y)))
    half = m // 2
    pow10 = 10 ** half
    a, b = divmod(x, pow10)
    c, d = divmod(y, pow10)
    ac = solve(a, c, n)
    bd = solve(b, d, n)
    ad_bc = solve(a + b, c + d, n) - ac - bd
    return ac * 10 ** (2 * half) + ad_bc * 10 ** half + bd
```

</details>

## Durchlauf

`x = 1234`, `y = 5678`.
`n = 4`, `m = 2`.
`a = 12`, `b = 34`.
`c = 56`, `d = 78`.

1. **Berechne Z_0 = a x c:**
   `z0 = karatsuba(12, 56)`. *(Rekursion bis zu einstelligen Zahlen, ergibt 672)*.
2. **Berechne Z_1 = b x d:**
   `z1 = karatsuba(34, 78)`. *(Ergibt 2652)*.
3. **Berechne Z_2 = (a+b) x (c+d):**
   `z2 = karatsuba(46, 134)`. *(Ergibt 6164)*.

4. **Berechne den mittleren Term (ad + bc):**
   `middle_term = z2 - z0 - z1` = 6164 - 672 - 2652 = 2840.
   *(Überprüfung: 12 x 78 + 34 x 56 = 936 + 1904 = 2840. Die Rechnung stimmt perfekt!)*

5. **Zusammenbau:**
   `Result` = z_0 x 10^4 + middle\_term x 10^2 + z_1
   `Result` = 672 x 10000 + 2840 x 100 + 2652
   `Result` = 6720000 + 284000 + 2652 = 7006652.

Das Ergebnis ist `7006652`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N^1.58)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N^1.58)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N^1.58)$ | $O(N)$ |

Der Algorithmus führt 3 rekursive Aufrufe mit Eingaben der halben Größe durch.
Nach dem Master-Theorem gilt T(N) = 3T(N/2) + $O(N)$ -> $O(N^{log_2(3)})$ ~= $O(N^{1.585})$.
Die Platzkomplexität beträgt $O(\log N)$ für die Rekursionstiefe, aber da das Erstellen neuer massiver Integer/Strings auf jeder Ebene $O(N)$ Platz benötigt, ist die gesamte Platzkomplexität eng auf $O(N)$ begrenzt.

## Varianten & Optimierungen

- **Basisschwellenwert:** Bei sehr kleinen Zahlen (z. B. N < 32) ist der Overhead durch Rekursion, Funktionsaufrufe und Aufteilung tatsächlich *langsamer* als die hardwarebeschleunigte schriftliche $O(N^2)$-Multiplikation! Moderne BigInt-Bibliotheken (wie die von Python) verwenden die schriftliche Methode für kleine Zahlen, wechseln für mittlere Zahlen zu Karatsuba und für Zahlen mit Millionen von Stellen zu Toom-Cook oder Schönhage-Strassen (FFT).
- **Binäre Aufteilung:** Anstatt nach Zehnerpotenzen aufzuteilen, teilen reale Implementierungen nach Zweierpotenzen (oder 2^{32}) auf, um blitzschnelle bitweise Verschiebungen (`>>`) anstelle von teurer Division (`//`) und Modulo (`%`) zu verwenden.

## Anwendungen in der Praxis

- **Kryptographie & BigInt-Bibliotheken:** Fast alle Standardbibliotheksimplementierungen für Integer mit beliebiger Genauigkeit (wie Pythons `int` oder Javas `BigInteger`) verwenden bei der Multiplikation extrem großer Zahlen automatisch die Karatsuba-Logik im Hintergrund.

## Verwandte Algorithmen in cOde(n)

- **[dc_06 - Strassen-Matrixmultiplikation](dc_06_strassen-matrix-multiplication.md)** — Das exakt gleiche Konzept der "algebraischen Eliminierung eines rekursiven Aufrufs", jedoch angewendet auf 2D-Matrizen, um $O(N^3)$ auf $O(N^{2.8})$ zu reduzieren.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*