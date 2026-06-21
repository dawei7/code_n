# Multiplikation zweier Ganzzahlen ohne Multiplikationsoperator (Russische Bauernmultiplikation)

| | |
|---|---|
| **ID** | `bit_09` |
| **Kategorie** | bit_manipulation |
| **Komplexität (erforderlich)** | $O(\log N)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 5/10 |
| **GeeksForGeeks Äquivalent** | [Russian Peasant Multiplication](https://www.geeksforgeeks.org/russian-peasant-multiply-two-numbers-using-bitwise-operators/) |

## Problemstellung

Gegeben sind zwei Ganzzahlen `a` und `b`. Multiplizieren Sie diese, ohne den `*` Operator zu verwenden.
Sie dürfen Addition, Subtraktion und bitweise Operatoren verwenden.

**Eingabe:** Zwei Ganzzahlen `a` und `b`.
**Ausgabe:** Eine Ganzzahl, die `a * b` repräsentiert.

## Wann ist dies anzuwenden?

- Ein klassisches Rätsel zur Bit-Manipulation, das oft als **Russische Bauernmultiplikation** oder **Ägyptische Multiplikation** bezeichnet wird.
- Demonstriert, wie mathematische Multiplikation physisch in Hardware-ALUs mittels Bit-Shifts und Addierern implementiert wird.

## Ansatz

**1. Die mathematische Grundlage:**
Multiplikation ist lediglich wiederholte Addition. a x b bedeutet, a insgesamt b-mal zu sich selbst zu addieren.
Wenn b = 13 ist, dann ist a x 13 = a + a + a \dots (13-mal). Dies entspricht $O(b)$ Operationen.
Wir können b jedoch in Zweierpotenzen zerlegen (Binärdarstellung)!
13 ist binär `1101` (8 + 4 + 1).
Daher ist a x 13 = a x (8 + 4 + 1) = (a x 8) + (a x 4) + (a x 1).

**2. Der bitweise Shift:**
Wie multiplizieren wir a mit 8? Wir verschieben es einfach 3-mal nach links! `a << 3`.
Woher wissen wir, WELCHE Zweierpotenzen wir addieren müssen? Wir betrachten einfach die binären Bits von b!
Wenn das niederwertigste Bit von b `1` ist, addieren wir unser aktuell skaliertes a zum Gesamtergebnis.
Anschließend entfernen wir physisch das niederwertigste Bit von b durch einen Rechts-Shift (`b >> 1`) und verdoppeln gleichzeitig a durch einen Links-Shift (`a << 1`).
Wir wiederholen dies, bis b den Wert 0 erreicht.

**3. Randfälle & Vorzeichen:**
Genau wie bei der Division (`bit_08`) gilt: Wenn die Zahlen unterschiedliche Vorzeichen haben, ist das Ergebnis negativ. Wir entfernen die Vorzeichen, führen die bitweise Logik auf den positiven Zahlen aus und wenden das Vorzeichen am Ende wieder an.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for bit_09: Multiply Without *.

Compute a * b using only addition and shifts. For
"""


def solve(a, b):
    """Return a * b without using *."""
    negative = (a < 0) != (b < 0)
    x = abs(a)
    y = abs(b)
    result = 0
    while y > 0:
        if y & 1:
            result += x
        x <<= 1
        y >>= 1
    if negative:
        result = -result
    return result
```

</details>

## Durchlauf

`a = 5`, `b = 13`. (`13` ist `1101`).

1. **Schleife 1:** `b = 13`.
   - `b & 1` -> `13 & 1 == 1`. Wahr!
   - `result += 5`. `result = 5`.
   - `a = 5 << 1 = 10`.
   - `b = 13 >> 1 = 6` (`0110`).
2. **Schleife 2:** `b = 6`.
   - `b & 1` -> `6 & 1 == 0`. Falsch!
   - `result = 5`.
   - `a = 10 << 1 = 20`.
   - `b = 6 >> 1 = 3` (`0011`).
3. **Schleife 3:** `b = 3`.
   - `b & 1` -> `3 & 1 == 1`. Wahr!
   - `result += 20`. `result = 25`.
   - `a = 20 << 1 = 40`.
   - `b = 3 >> 1 = 1` (`0001`).
4. **Schleife 4:** `b = 1`.
   - `b & 1` -> `1 & 1 == 1`. Wahr!
   - `result += 40`. `result = 65`.
   - `a = 40 << 1 = 80`.
   - `b = 1 >> 1 = 0`.
5. **Schleife 5:** `b = 0`. Abbruch.

Das Ergebnis ist `65`. ✓ (5 x 13 = 65).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(log B)$ | $O(1)$ |
| **Schlechtester Fall** | $O(log B)$ | $O(1)$ |

*Wobei B der Wert des Multiplikators ist.*
Die `while`-Schleife läuft exakt so oft, wie b Bits besitzt. Wenn b eine 32-Bit-Ganzzahl ist, läuft die Schleife maximal 32-mal. Dies macht die Zeitkomplexität logarithmisch beschränkt $O(log B)$, was für Ganzzahlen fester Breite effektiv $O(1)$ entspricht.
Die Platzkomplexität ist strikt $O(1)$.

## Varianten & Optimierungen

- **Optimierte Wahl des Multiplikators:** Da a x b = b x a gilt, läuft der Algorithmus signifikant schneller, wenn die `while`-Schleife an die KLEINERE der beiden Zahlen gebunden ist! Z. B. benötigt 10000 x 2 zwei Iterationen, wenn b=2, aber 14 Iterationen, wenn b=10000. Fügen Sie einfach `if a < b: a, b = b, a` am Anfang hinzu!

## Anwendungen in der Praxis

- **Kryptographie (Modulare Exponentiation):** Bei der RSA-Verschlüsselung müssen extrem große Exponenten wie x^{1024} \pmod N berechnet werden. Man kann x nicht 1024-mal mit sich selbst multiplizieren. Der Algorithmus der "Exponentiation durch Quadrieren", der hierfür verwendet wird, ist mathematisch IDENTISCH mit der Russischen Bauernmultiplikation, wobei lediglich `+` durch `*` und `*` durch `^` ersetzt wird!

## Verwandte Algorithmen in cOde(n)

- **[bit_08 - Divide Without Division](bit_08_divide-without.md)** — Die inverse Operation unter Verwendung identischer Skalierungslogik.
- **[math_02 - Fast Exponentiation](../math/math_02_fast-exponentiation.md)** — Derselbe Algorithmus angewandt auf Potenzen anstelle von Multiplikation.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*