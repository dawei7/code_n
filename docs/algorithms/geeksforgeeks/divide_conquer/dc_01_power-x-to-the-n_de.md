# Pow(x, n) (Schnelle Exponentiation)

| | |
|---|---|
| **ID** | `dc_01` |
| **Kategorie** | divide_conquer |
| **Komplexität (erforderlich)** | $O(\log N)$ Zeit, $O(\log N)$ Platz |
| **Schwierigkeit** | 3/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **LeetCode-Äquivalent** | [Pow(x, n)](https://leetcode.com/problems/powx-n/) |

## Problemstellung

Implementieren Sie `pow(x, n)`, welches `x` hoch `n` (d. h. x^n) berechnet.

**Eingabe:** Eine Fließkommazahl `x` und eine Ganzzahl `n`.
**Ausgabe:** Eine Fließkommazahl, die x^n repräsentiert.

## Wann man es verwendet

- Um Exponentialwerte sicher zu berechnen, ohne einen $O(N)$ Time Limit Exceeded (TLE) Fehler zu provozieren.
- Es ist der absolute Grundalgorithmus von **Divide and Conquer**, der das Kernkonzept vermittelt, einen Problemraum mathematisch statt physisch zu halbieren.

## Ansatz

**1. Der Fehler der $O(N)$ Multiplikation:**
Die naive Art, 2^{10} zu berechnen, ist `2 * 2 * 2 ...` (10-mal).
Wenn n = 2147483647 (die maximale 32-Bit-Ganzzahl), wird diese Schleife 2 Milliarden Mal durchlaufen und die Anwendung zum Einfrieren bringen!

**2. Divide and Conquer (Exponentiation by Squaring):**
Wie berechnen wir x^{10} schneller?
Beachten Sie, dass x^{10} = x^5 x x^5 ist.
Wenn wir x^5 kennen, multiplizieren wir es einfach mit sich selbst! Wir halbieren den Arbeitsaufwand strikt!
Aber Moment, wie berechnen wir x^5? 5 ist eine ungerade Zahl.
x^5 = x^2 x x^2 x x.
Indem wir den Exponenten kontinuierlich halbieren, reduzieren wir die Anzahl der erforderlichen Multiplikationen von N auf log_2(N)!
Die Berechnung von 2^{2147483647} benötigt nun exakt **31 Operationen** statt 2 Milliarden!

**3. Die rekursiven Regeln:**
- **Induktionsanfang (Basis):** Wenn n == 0, gib `1.0` zurück. (Alles hoch 0 ist 1).
- **Gerader Exponent:** Wenn n gerade ist, x^n = (x^{n/2}) x (x^{n/2}).
- **Ungerader Exponent:** Wenn n ungerade ist, x^n = x x (x^{(n-1)/2}) x (x^{(n-1)/2}).

**4. Randfälle:**
- Was ist, wenn n negativ ist? (z. B. 2^{-3}).
  Ein negativer Exponent bedeutet lediglich die Bildung des Kehrwerts! x^{-n} = 1 / x^n.
  Wenn n < 0 ist, berechnen wir also einfach rekursiv `pow(x, -n)` und geben `1.0 / result` zurück.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dc_01: Power(x, n).

Recursive halving: x^n = (x^(n//2))^2, with an extra x when
n is odd. Handle negative n by computing the reciprocal. O(log n).
"""


def solve(x, n):
    if n == 0:
        return 1
    # Use absolute exponent, then take reciprocal at the end if needed.
    abs_n = -n if n < 0 else n
    result = 1.0
    base = float(x)
    while abs_n > 0:
        if abs_n & 1:
            result *= base
        abs_n >>= 1
        if abs_n:
            base *= base
    if n < 0:
        return 1.0 / result
    return result
```

</details>

## Durchlauf

`x = 2.0`, `n = 5`.

1. `fast_pow(2.0, 5)`:
   - `exp` ist ungerade (5).
   - `half = fast_pow(2.0, 2)`:
     - `exp` ist gerade (2).
     - `half = fast_pow(2.0, 1)`:
       - `exp` ist ungerade (1).
       - `half = fast_pow(2.0, 0)` -> **Gibt 1.0 zurück (Induktionsanfang)**
       - Zurück zu `exp=1`: gibt `1.0 * 1.0 * 2.0` zurück -> **Gibt 2.0 zurück**
     - Zurück zu `exp=2`: gibt `2.0 * 2.0` zurück -> **Gibt 4.0 zurück**
   - Zurück zu `exp=5`: gibt `4.0 * 4.0 * 2.0` zurück -> **Gibt 32.0 zurück**

Das Ergebnis ist `32.0`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(\log N)$ | $O(\log N)$ |
| **Durchschnittlicher Fall** | $O(\log N)$ | $O(\log N)$ |
| **Schlechtester Fall** | $O(\log N)$ | $O(\log N)$ |

*Wobei N der Exponent ist.*
Bei jedem Schritt wird der Exponent durch 2 geteilt (Ganzzahldivision). Die Rekursion endet, wenn N=0 erreicht ist. Daher gibt es exakt log_2(N) rekursive Aufrufe.
Die Zeitkomplexität beträgt $O(\log N)$.
Die Platzkomplexität beträgt $O(\log N)$ aufgrund der Tiefe des rekursiven Aufruf-Stacks.

## Varianten & Optimierungen

- **Iterativer Ansatz (Bit-Manipulation):** Sie können den rekursiven Aufruf-Stack vollständig eliminieren (und den Platzbedarf auf $O(1)$ senken), indem Sie die exakt gleiche Logik wie bei der Russischen Bauernmultiplikation (`bit_09`) verwenden! Konvertieren Sie `n` einfach in Binärform. `while n > 0`: wenn `n & 1 == 1`, multiplizieren Sie Ihr `result` mit `x`. Quadrieren Sie dann blind `x` (`x = x * x`) und verschieben Sie `n` nach rechts (`n >>= 1`). Dies ist die branchenübliche Art, wie mathematische Bibliotheken `pow()` implementieren.
- **Modulare Exponentiation:** Wenn das Problem nach `pow(x, n) % M` fragt (weil das Ergebnis zu groß für den Speicher ist), wenden Sie einfach den Modulo-Operator bei JEDEM Multiplikationsschritt an! `half = (half * half) % M`.

## Anwendungen in der Praxis

- **RSA-Kryptographie:** Das Verschlüsseln und Entschlüsseln von Nachrichten erfordert die Berechnung von C = M^e \pmod N. Da der Verschlüsselungsschlüssel e oft eine riesige 2048-Bit-Ganzzahl ist, ist die naive Berechnung von M hoch einer 2048-Bit-Zahl physisch unmöglich, bevor das Universum endet. Die schnelle Exponentiation berechnet dies in Millisekunden.

## Verwandte Algorithmen in cOde(n)

- **[bit_09 - Multiply Without Multiplication](../bit_manipulation/bit_09_multiply-without.md)** — Die exakt gleiche "Halbierungslogik", angewendet auf Addition statt Multiplikation.
- **[math_02 - Modular Arithmetic](../math/math_02_modular-arithmetic.md)** — Wie man diesen Algorithmus anwendet, wenn eine Modulo-Einschränkung vorliegt.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*