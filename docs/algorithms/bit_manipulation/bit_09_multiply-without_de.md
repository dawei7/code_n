# Zwei ganze Zahlen ohne Multiplikation multiplizieren (russischer Bauer)

| | |
|---|---|
| **ID** | `bit_09` |
| **Kategorie** | Bitmanipulation |
| **Komplexität (erforderlich)** | $O(\log N)$ Zeit, $O(1)$ Speicherplatz |
| **Schwierigkeitsgrad** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 5/10 |
| **GeeksForGeeks-Äquivalent** | [Multiplikation nach der russischen Bauernmethode](https://www.geeksforgeeks.org/russian-peasant-multiply-two-numbers-using-bitwise-operators/) |

## Aufgabenstellung

Gegeben sind zwei ganze Zahlen `a` und `b`. Multiplizieren Sie diese, ohne den Operator `*` zu verwenden.
Sie dürfen Addition, Subtraktion und bitweise Operatoren verwenden.

**Eingabe:** Zwei ganze Zahlen `a` und `b`.
**Ausgabe:** Eine ganze Zahl, die `a * b` darstellt.

## Wann man diese Aufgabe verwenden sollte

- Ein klassisches Rätsel zur Bitmanipulation, das oft als **„Russische Bauernmultiplikation“** oder **„Altägyptische Multiplikation“** bezeichnet wird.
- Veranschaulicht, wie die mathematische Multiplikation in Hardware-ALUs mithilfe von Bitverschiebungen und Addierern physikalisch umgesetzt wird.

## Vorgehensweise

**1. Die mathematische Grundlage:**
Multiplikation ist nichts anderes als wiederholte Addition. a × b bedeutet, a b-mal mit sich selbst zu addieren.
Wenn b = 13 ist, dann gilt: a × 13 = a + a + a \dots (13 Mal). Das sind $O(b)$ Rechenoperationen.
Wir können b jedoch in Zweierpotenzen zerlegen (binäre Darstellung)!
13 im Binärsystem ist `1101` (8 + 4 + 1).
Daher gilt: a × 13 = a × (8 + 4 + 1) = (a × 8) + (a × 4) + (a × 1).

**2. Die bitweise Verschiebung:**
Wie multiplizieren wir a mit 8? Wir verschieben es einfach dreimal nach links! `a << 3`.
Woher wissen wir, WELCHE 2-Potenzen wir addieren müssen? Wir schauen uns einfach die Binärbits von b an!
Wenn das niedrigste Bit von b `1` ist, addieren wir unser aktuell skaliertes a zum Gesamtergebnis.
Dann schneiden wir das niedrigste Bit von b durch Rechtsverschiebung (`b >> 1`) physisch ab und verdoppeln gleichzeitig a durch Linksverschiebung (`a << 1`).
Das wiederholen wir, bis b den Wert 0 erreicht.

**3. Randfälle & Vorzeichen:**
Genau wie bei der Division (`bit_08`) ist das Ergebnis negativ, wenn die Zahlen unterschiedliche Vorzeichen haben. Wir entfernen die Vorzeichen, führen die bitweise Logik auf positive Zahlen an und fügen das Vorzeichen am Ende wieder hinzu.

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

## Schritt-für-Schritt-Anleitung

`a = 5`, `b = 13`. (`13` ist `1101`).

1. **Schleife 1:** `b = 13`.
   - `b & 1` -> `13 & 1 == 1`. Richtig!
   - `result += 5`. `result = 5`.
   - `a = 5 << 1 = 10`.
   - `b = 13 >> 1 = 6`(`0110`).
2. **Schleife 2:** `b = 6`.
   - `b & 1` -> `6 & 1 == 0`. Falsch!
   - `result = 5`.
   - `a = 10 << 1 = 20`.
   - `b = 6 >> 1 = 3`(`0011`).
3. **Schleife 3:** `b = 3`.
   - `b & 1` -> `3 & 1 == 1`. Richtig!
   - `result += 20`. `result = 25`.
   - `a = 20 << 1 = 40`.
   - `b = 3 >> 1 = 1`(`0001`).
4. **Schleife 4:** `b = 1`.
   - `b & 1` -> `1 & 1 == 1`. Richtig!
   - `result += 40`. `result = 65`.
   - `a = 40 << 1 = 80`.
   - `b = 1 >> 1 = 0`.
5. **Schleife 5:** `b = 0`. Beenden.

Das Ergebnis ist `65`. ✓ (5 × 13 = 65).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(log B)$ | $O(1)$ |
| **Schlechtester Fall** | $O(log B)$ | $O(1)$ |

*Dabei ist B der Wert des Multiplikators.*
Die `while`-Schleife wird genau so oft durchlaufen, wie `b` Bits enthält. Ist `b` eine 32-Bit-Ganzzahl, wird die Schleife höchstens 32 Mal durchlaufen. Dadurch ist die Zeitkomplexität logarithmisch begrenzt $O(log B)$, effektiv $O(1)$ für Ganzzahlen fester Breite.
Die Platzkomplexität beträgt streng $O(1)$.

## Varianten & Optimierungen

- **Optimierte Wahl des Multiplikators:** Da a × b = b × a gilt, läuft der Algorithmus deutlich schneller, wenn die `while`-Schleife an die KLEINERE der beiden Zahlen gebunden ist! Beispielsweise benötigt 10000 × 2 bei b = 2 zwei Iterationen, bei b = 10000 jedoch 14 Iterationen. Füge einfach `if a < b: a, b = b, a` am Anfang hinzu!

## Praktische Anwendungen

- **Kryptografie (modulare Potenzierung):** Bei der RSA-Verschlüsselung müssen unglaublich große Exponenten wie x^{1024} \pmod N berechnet werden. Man kann x nicht einfach 1024 Mal mit sich selbst multiplizieren. Der zur Lösung dieses Problems verwendete Algorithmus „Potenzierung durch Quadrieren“ ist mathematisch IDENTISCH mit der russischen Bauernmultiplikation, lediglich `+` durch `*` und `*` durch `^` ausgetauscht wird!

## Verwandte Algorithmen in cOde(n)

- **[bit_08 – Teilen ohne Division](bit_08_divide-without.md)** — Die umgekehrte Operation unter Verwendung derselben Skalierungslogik.
- **[math_02 – Schnelle Potenzierung](../math/math_02_fast-exponentiation.md)** – Genau derselbe Algorithmus, der statt auf die Multiplikation auf Potenzen angewendet wird.

---

*Diese Dokumentation ist ein Originalbeitrag für cOde(n),
der sich an der kanonischen Struktur orientiert, die von Referenzseiten
zum Thema Wettbewerbsprogrammierung verwendet wird. Den kanonischen
Enzyklopädieeintrag finden Sie über den Wikipedia-Link oben auf der Seite.
Quell-Repository:
<https://github.com/dawei7/code_n>.*
