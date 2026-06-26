# Erweiterter Euklidischer Algorithmus

| | |
|---|---|
| **ID** | `math_07` |
| **Kategorie** | math |
| **Komplexität (erforderlich)** | $O(log(min(A, B)$)) Zeit, $O(log(min(A, B)$)) Platz |
| **Schwierigkeit** | 7/10 |
| **Relevanz für Vorstellungsgespräche** | 3/10 |
| **Wikipedia** | [Erweiterter euklidischer Algorithmus](https://de.wikipedia.org/wiki/Erweiterter_euklidischer_Algorithmus) |

## Problemstellung

Gegeben sind zwei ganze Zahlen A und B. Bestimmen Sie deren größten gemeinsamen Teiler (ggT).
Finden Sie zusätzlich die ganzzahligen Koeffizienten x und y, sodass gilt:
A \cdot x + B \cdot y = \text{GCD}(A, B)
(Diese Gleichung ist als Bézout-Identität bekannt).

**Eingabe:** Zwei ganze Zahlen `a` und `b`.
**Ausgabe:** Ein Tupel aus drei ganzen Zahlen `(gcd, x, y)`.

## Anwendung

- Sie verwenden diesen Algorithmus fast nie nur zur Bestimmung des ggT.
- Er wird spezifisch eingesetzt, wenn Sie die Koeffizienten x und y benötigen, um lineare diophantische Gleichungen zu lösen oder das multiplikative Inverse modulo n (`math_08`) zu finden.

## Ansatz

**1. Die rekursive Grundlage des ggT:**
Erinnern Sie sich an den Standard-Euklidischen Algorithmus (`math_01`): \text{GCD}(A, B) = \text{GCD}(B, A \pmod B).
Der Basisfall tritt ein, wenn B = 0 ist. In diesem Fall gilt \text{GCD}(A, 0) = A.
Setzen wir diesen Basisfall in die Bézout-Identität ein:
A \cdot x + 0 \cdot y = A.
Offensichtlich ist diese Gleichung gelöst, wenn **x = 1** und **y = 0** ist!
Dies liefert uns unsere Koeffizienten für den Basisfall.

**2. Die mathematische Herleitung (der "erweiterte" Teil):**
Angenommen, unser rekursiver Aufruf `extended_gcd(B, A % B)` liefert erfolgreich das Tupel `(gcd, x1, y1)` zurück.
Das bedeutet, wir wissen mathematisch, dass gilt:
B \cdot x_1 + (A \pmod B) \cdot y_1 = \text{GCD}

Wir möchten diese Gleichung so umschreiben, dass sie die Form A \cdot x + B \cdot y annimmt.
Wie können wir (A \pmod B) umschreiben?
In der Ganzzahl-Arithmetik gilt A \pmod B = A - B \cdot \lfloor \frac{A}{B} \rfloor.
Setzen wir dies in die Gleichung ein:
B \cdot x_1 + (A - B \cdot \lfloor \frac{A}{B} \rfloor) \cdot y_1 = \text{GCD}

Expandieren und gruppieren Sie nach A und B:
B \cdot x_1 + A \cdot y_1 - B \cdot \lfloor \frac{A}{B} \rfloor \cdot y_1 = \text{GCD}
A \cdot (y_1) + B \cdot (x_1 - \lfloor \frac{A}{B} \rfloor \cdot y_1) = \text{GCD}

Betrachten Sie die Gruppierung! Wir haben exakt das Format A \cdot x + B \cdot y erreicht!
Daher sind die neuen Koeffizienten, die wir im Rekursionsbaum nach oben weitergeben:
- x = y_1
- y = x_1 - \lfloor \frac{A}{B} \rfloor \cdot y_1

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for math_07: Extended Euclidean Algorithm.

Given two non-negative integers a and b (not both
"""


def solve(a, b):
    """Extended Euclidean: a*x + b*y = gcd(a, b)."""
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    return old_r, old_s, old_t
```

</details>

## Durchlauf

`A = 30`, `B = 20`.

1. `extended_gcd(30, 20)`:
   - Ruft `extended_gcd(20, 30 % 20)` -> `extended_gcd(20, 10)` auf.
2. `extended_gcd(20, 10)`:
   - Ruft `extended_gcd(10, 20 % 10)` -> `extended_gcd(10, 0)` auf.
3. `extended_gcd(10, 0)`:
   - Basisfall! `b == 0`.
   - Gibt `(10, 1, 0)` zurück. (gcd=10, x1=1, y1=0).
4. Rücklauf zu `extended_gcd(20, 10)`:
   - `a = 20`, `b = 10`. `x1 = 1`, `y1 = 0`.
   - `x = y1 = 0`.
   - `y = x1 - (a // b) * y1` -> `1 - (20 // 10) * 0` -> `1 - 2 * 0 = 1`.
   - Gibt `(10, 0, 1)` zurück.
5. Rücklauf zu `extended_gcd(30, 20)`:
   - `a = 30`, `b = 20`. `x1 = 0`, `y1 = 1`.
   - `x = y1 = 1`.
   - `y = x1 - (a // b) * y1` -> `0 - (30 // 20) * 1` -> `0 - 1 * 1 = -1`.
   - Gibt `(10, 1, -1)` zurück.

Ergebnis: `gcd = 10`, `x = 1`, `y = -1`.
Überprüfung der Bézout-Identität: 30 \cdot (1) + 20 \cdot (-1) = 30 - 20 = 10. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(\log(\min(A, B)$)) | $O(\log(\min(A, B)$)) |
| **Schlechtester Fall** | $O(\log(\min(A, B)$)) | $O(\log(\min(A, B)$)) |

Die Anzahl der rekursiven Aufrufe ist exakt identisch mit dem Standard-Euklidischen Algorithmus, was bedeutet, dass die Zeitkomplexität durch $O(log(\min(A,B)$)) begrenzt ist.
Da der Algorithmus von unten nach oben abgewickelt wird, ist er nativ rekursiv implementiert, was eine Platzkomplexität von $O(log(\min(A,B)$)) für die Tiefe des Call-Stacks erfordert.
*(Er kann iterativ implementiert werden, um $O(1)$ Platz zu erreichen, aber die Logik ist deutlich schwerer zu merken).*

## Varianten & Optimierungen

- **Lineare diophantische Gleichungen:** Wenn Sie aufgefordert werden, IRGENDEINE ganzzahlige Lösung (X, Y) für die Gleichung A \cdot X + B \cdot Y = C zu finden:
  1. Berechnen Sie `gcd, x, y = extended_gcd(A, B)`.
  2. Wenn C nicht ohne Rest durch `gcd` teilbar ist, existiert mathematisch KEINE ganzzahlige Lösung!
  3. Wenn es teilbar ist, lautet die Antwort X = x \cdot (C / \text{gcd}) und Y = y \cdot (C / \text{gcd}).

## Anwendungen in der Praxis

- **Public-Key-Kryptographie:** Absolut essenziell für die Berechnung des privaten Schlüssels `d` im RSA-Algorithmus, wobei `d` das multiplikative Inverse von `e` modulo \phi(n) ist.

## Verwandte Algorithmen in cOde(n)

- **[math_01 - GCD Euclidean](math_01_gcd-euclidean.md)** — Der einfachere Standard-ggT-Algorithmus.
- **[math_08 - Modular Multiplicative Inverse](math_08_modular-multiplicative-inverse.md)** — Der Hauptgrund, warum der erweiterte euklidische Algorithmus in der Informatik gelehrt wird.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den enzyklopädischen Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*