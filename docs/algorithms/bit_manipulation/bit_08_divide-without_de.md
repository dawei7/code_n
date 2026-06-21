# Division zweier Ganzzahlen ohne Divisionsoperator

| | |
|---|---|
| **ID** | `bit_08` |
| **Kategorie** | bit_manipulation |
| **Komplexität (erforderlich)** | $O(\log N)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 8/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **LeetCode-Äquivalent** | [Divide Two Integers](https://leetcode.com/problems/divide-two-integers/) |

## Problemstellung

Gegeben sind zwei Ganzzahlen `dividend` und `divisor`. Dividieren Sie diese beiden Zahlen, ohne Multiplikations-, Divisions- oder Modulo-Operatoren zu verwenden.
Die Ganzzahldivision soll in Richtung Null runden, was bedeutet, dass der Nachkommateil verworfen wird. Geben Sie den Quotienten nach der Division von `dividend` durch `divisor` zurück.
*Einschränkung:* Gehen Sie davon aus, dass wir uns in einer Umgebung befinden, die nur Ganzzahlen innerhalb des 32-Bit-Bereichs mit Vorzeichen speichern kann: [-2^{31}, 2^{31} - 1]. Wenn der Quotient strikt größer als 2^{31} - 1 ist, geben Sie 2^{31} - 1 zurück.

**Eingabe:** Zwei Ganzzahlen, `dividend` und `divisor`.
**Ausgabe:** Eine Ganzzahl, die den Quotienten repräsentiert.

## Wann man es verwendet

- Das klassische Problem: "Implementierung grundlegender Arithmetik mittels Bit-Operationen".
- Um zu demonstrieren, wie Links-Shifting (`<<`) rechnerisch identisch mit einer Multiplikation mit 2 ist und wie wiederholte Subtraktion logarithmisch skaliert.

## Ansatz

**1. Der naive Ansatz:**
Wenn wir `10 / 3` berechnen wollen, können wir einfach wiederholt `3` von `10` subtrahieren, bis wir unter `3` fallen.
`10 - 3 = 7` (1. Mal)
`7 - 3 = 4` (2. Mal)
`4 - 3 = 1` (3. Mal). Stopp!
Der Quotient ist 3.
Dies benötigt $O(N)$ Zeit, wobei N der Quotient ist. Wenn wir 2^{31} / 1 berechnen, würde dies zwei Milliarden Mal durchlaufen und einen Time Limit Exceeded (TLE) Fehler auslösen.

**2. Die logarithmische Bit-Shift-Optimierung:**
Anstatt den Divisor einzeln zu subtrahieren, was passiert, wenn wir den Divisor durch Links-Shifts schnell verdoppeln?
Wir möchten das *größtmögliche Vielfache des Divisors* in einem einzigen Schritt vom Dividenden subtrahieren!
Beispiel: `dividend = 50`, `divisor = 3`.
- `3 << 0 = 3`
- `3 << 1 = 6`
- `3 << 2 = 12`
- `3 << 3 = 24`
- `3 << 4 = 48`  <-- Größtes Vielfaches! Wir subtrahieren 48 von 50.
Unser Quotient erhöht sich um 2^4 = 16.
Unser neuer `dividend` ist 50 - 48 = 2.
Da 2 < 3, stoppen wir. Der Gesamtquotient ist 16. Wir haben dies in $O(\log N)$ Schritten erreicht!

**3. Randfälle & Vorzeichen:**
- Wenn Dividend und Divisor unterschiedliche Vorzeichen haben, muss der endgültige Quotient negativ sein. Wir können die Vorzeichen extrahieren, beide Zahlen für den Algorithmus strikt positiv machen und das Vorzeichen am Ende wieder anwenden.
- Die 32-Bit-Ganzzahl-Einschränkung ist der schwierigste Teil. Der Absolutwert von `-2147483648` ist `+2147483648`, was einen 32-Bit-Integer mit Vorzeichen ÜBERLAUFEN lässt! Die meisten Standardlösungen schummeln, indem sie 64-Bit-Longs in Java/C++ verwenden. Der mathematisch saubere Weg besteht darin, beide Zahlen tatsächlich in NEGATIVE Werte umzuwandeln, da der negative Bereich eine Kapazität von einer Zahl mehr besitzt!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for bit_08: Divide Without /.

Compute dividend / divisor (integer division) using
"""


def solve(dividend, divisor):
    """Return dividend / divisor (integer division) without using /."""
    if divisor == 0:
        return 0
    if dividend == 0:
        return 0
    negative = (dividend < 0) != (divisor < 0)
    a = abs(dividend)
    b = abs(divisor)
    quotient = 0
    power = 32
    while (b << power) > a:
        power -= 1
    while power >= 0:
        if (b << power) <= a:
            a -= b << power
            quotient |= 1 << power
        power -= 1
    if negative:
        quotient = -quotient
    return quotient
```

</details>

## Durchlauf

`dividend = 29`, `divisor = 3`. Beide positiv. `quotient = 0`.

1. **Äußere Schleife 1:** `29 >= 3`.
   - `temp = 3`, `mult = 1`.
   - `29 >= (3<<1=6)`. `temp=6`, `mult=2`.
   - `29 >= (6<<1=12)`. `temp=12`, `mult=4`.
   - `29 >= (12<<1=24)`. `temp=24`, `mult=8`.
   - `29 >= (24<<1=48)` FALSCH. Schleife endet.
   - `dividend = 29 - 24 = 5`.
   - `quotient = 0 + 8 = 8`.
2. **Äußere Schleife 2:** `5 >= 3`.
   - `temp = 3`, `mult = 1`.
   - `5 >= (3<<1=6)` FALSCH. Schleife endet.
   - `dividend = 5 - 3 = 2`.
   - `quotient = 8 + 1 = 9`.
3. **Äußere Schleife 3:** `2 >= 3` FALSCH. Schleife endet.

Ergebnis `quotient = 9`. ✓ (29 / 3 = 9).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(\log N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(\log N)$ | $O(1)$ |

*Wobei N das Verhältnis von `dividend` zu `divisor` ist.*
Im absolut schlechtesten Fall (z. B. 2^{31} / 1) wird die innere Schleife genau 31 Mal shiften und die äußere Schleife genau einmal ausgelöst werden. Die Zeitkomplexität ist strikt durch die Anzahl der Bits in der Ganzzahl begrenzt, was sie zu $O(\log(\text{dividend}))$ macht, was für 32-Bit-Ganzzahlen effektiv eine $O(1)$-Schranke darstellt.
Die Platzkomplexität ist $O(1)$.

## Varianten & Optimierungen

- **Reine negative Skalierung (Kein Schummeln):** Der obige Python-Code verwendet `abs()`, was konzeptionell die strikten 32-Bit-Einschränkungen verletzt, wenn es in C/Java ausgeführt wird (da `abs(-2147483648)` überläuft). Die rein regelkonforme Lösung erzwingt `dividend = -abs(dividend)` und `divisor = -abs(divisor)` und kehrt die Logik der inneren Schleife zu `while dividend <= (temp_divisor << 1)` um! Dies garantiert, dass Sie niemals die Obergrenze des Absolutwerts überschreiten.

## Anwendungen in der Praxis

- **Eingebettete Systeme & ALUs:** Extrem stromsparende Mikrocontroller (wie ältere PIC- oder AVR-Chips) besitzen physikalisch keine Hardware-Divisionsschaltkreise (`DIV`-Befehle), um Siliziumfläche zu sparen! Der Compiler übersetzt `/`-Operationen direkt in Software-Bit-Shifting-Algorithmen, genau wie diesen hier.

## Verwandte Algorithmen in cOde(n)

- **[bit_09 - Multiply Without Multiplication](bit_09_multiply-without.md)** — Die exakte inverse Operation unter Verwendung derselben Bit-Shifting-Prinzipien.
- **[searching_01 - Binary Search](../searching/search_01_binary-search.md)** — Die Logik, in Zweierpotenzen zu springen, ist im Wesentlichen eine kontinuierliche binäre Suche über den Ganzzahlbereich!

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*