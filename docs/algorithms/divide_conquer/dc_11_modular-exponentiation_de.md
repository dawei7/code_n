# Modulare Exponentiation

| | |
|---|---|
| **ID** | `dc_11` |
| **Kategorie** | divide_conquer |
| **Komplexität (erforderlich)** | $O(log Y)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **GeeksForGeeks Äquivalent** | [Modular Exponentiation](https://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/) |

## Problemstellung

Gegeben sind drei Zahlen `x`, `y` und `p`. Berechne (x^y) \pmod p.
*Constraints:* `y` kann extrem groß sein und x^y kann das Speicherlimit des physischen Universums überschreiten. Du musst das Modulo berechnen, ohne dass der Zwischenwert jemals die Standard-Integer-Grenzen überschreitet.

**Eingabe:** Drei Integer `x`, `y` (der Exponent) und `p` (der Modulus).
**Ausgabe:** Ein Integer, der die berechnete modulare Potenz darstellt.

## Wann man es verwendet

- Zur sicheren Berechnung riesiger Potenzen in der Kryptographie oder in der wettbewerbsorientierten Programmierung (Competitive Programming).
- Demonstriert, wie sich die modulare Arithmetik perfekt über die Multiplikation verteilt.

## Ansatz

**1. Der Fehler des Post-Modulo:**
Wenn du versuchst, `(x ** y) % p` direkt zu berechnen, wird x^y sofort den Speicher überlaufen lassen. Selbst in Python (das über beliebige Präzision verfügt), würde die Berechnung von 10^{10^9} die CPU einfrieren und den gesamten RAM erschöpfen, bevor es überhaupt dazu kommt, den `% p` Operator anzuwenden!

**2. Das Distributivgesetz des Modulo:**
Die Mathematik garantiert:
(A x B) \pmod P = [ (A \pmod P) x (B \pmod P) ] \pmod P
Das bedeutet, dass wir den Modulo-Operator BEI JEDEM EINZELNEN MULTIPLIKATIONSSCHRITT anwenden können und das Endergebnis identisch bleibt! Die Zahl wird NIEMALS größer als P^2.

**3. Divide and Conquer (Iterative schnelle Exponentiation):**
Wir kombinieren diese Modulo-Eigenschaft mit **Exponentiation durch Quadrieren** (`dc_01`).
Anstatt Rekursion verwenden wir einen iterativen Ansatz unter Nutzung der Binärdarstellung (ähnlich der russischen Bauernmultiplikation).
- Initialisiere `res = 1`.
- Aktualisiere `x = x % p` (nur für den Fall, dass die Basis bereits größer als p ist).
- Schleife solange `y > 0`:
  - Wenn das niedrigste Bit von `y` 1 ist (`y & 1`), multipliziere `res` mit `x` und wende sofort Modulo `p` an!
  - Quadriere `x` (`x = x * x`) und wende sofort Modulo `p` an!
  - Verschiebe `y` um eine Stelle nach rechts (`y >>= 1`).

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dc_11: Modular Exponentiation.

Compute (x ** n) % m for non-negative integers x, n
"""


def solve(x, n, m):
    """Return (x ** n) % m via binary exponentiation."""
    result = 1
    base = x % m
    exp = n
    while exp > 0:
        if exp & 1:
            result = (result * base) % m
        exp >>= 1
        if exp:
            base = (base * base) % m
    return result
```

</details>

## Schritt-für-Schritt-Beispiel

`x = 2`, `y = 5`, `p = 13`.
Berechne (2^5) \pmod{13}.
`res = 1`. `x = 2 % 13 = 2`.

1. **Schleife 1:** `y = 5` (`101`).
   - `y & 1 == 1`. (Wahr).
   - `res = (1 * 2) % 13 = 2`.
   - `y = 5 >> 1 = 2` (`010`).
   - `x = (2 * 2) % 13 = 4`.
2. **Schleife 2:** `y = 2`.
   - `y & 1 == 1`. (Falsch).
   - `y = 2 >> 1 = 1` (`001`).
   - `x = (4 * 4) % 13 = 16 % 13 = 3`. *(Entscheidender Schritt! Es wuchs nicht auf 16 an, sondern fiel auf 3 zurück!)*
3. **Schleife 3:** `y = 1`.
   - `y & 1 == 1`. (Wahr).
   - `res = (2 * 3) % 13 = 6`.
   - `y = 1 >> 1 = 0`.
   - `x = (3 * 3) % 13 = 9`.
4. **Schleife 4:** `y = 0`. Abbruch.

Das Ergebnis `res` ist `6`. ✓
*(Verifizierung: 2^5 = 32. 32 \pmod{13} = 6. Die Mathematik funktioniert!)*

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(log Y)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(log Y)$ | $O(1)$ |
| **Schlechtester Fall** | $O(log Y)$ | $O(1)$ |

Die Schleife läuft exakt so oft, wie `y` Bits hat. Die Zeitkomplexität ist exakt $O(log Y)$.
Durch die iterative Umsetzung vermeiden wir den rekursiven Aufruf-Stack. Die Platzkomplexität ist strikt $O(1)$.
Der Maximalwert, der zu jedem Zeitpunkt in einer Variable gespeichert wird, ist exakt (P-1) x (P-1), was garantiert, dass kein 64-Bit-Integer-Überlauf auftritt, sofern P in einen 32-Bit-Integer passt.

## Varianten & Optimierungen

- **Kleiner Fermatscher Satz (Modulares Inverses):** Was ist, wenn der Exponent `y` negativ ist? Man kann keine Modulo-Arithmetik mit Brüchen durchführen! Du musst mit dem **modularen multiplikativen Inversen** multiplizieren. Wenn `p` eine Primzahl ist, besagt der Satz von Fermat, dass X^{-1} \pmod P \equiv X^{P-2} \pmod P. Du rufst buchstäblich einfach wieder genau diesen Algorithmus auf: `modular_exponentiation(x, p - 2, p)`!

## Anwendungen in der Praxis

- **RSA Public-Key-Verschlüsselung:** Das absolute Rückgrat der Internetsicherheit (HTTPS). Ein verschlüsselter Geheimtext `C` wird mit dem privaten Schlüssel `d` des Empfängers über die Formel M = C^d \pmod N zurück in die ursprüngliche Nachricht `M` entschlüsselt. Sowohl `d` als auch `N` sind üblicherweise 2048-Bit-Zahlen. Dieser Algorithmus ist die Engine, die diese Entschlüsselung ausführt.

## Verwandte Algorithmen in cOde(n)

- **[dc_01 - Pow(x, n)](dc_01_power-x-to-the-n.md)** — Die rekursive Version dieses Algorithmus ohne die Modulo-Eigenschaft.
- **[bit_09 - Multiply Without Multiplication](../bit_manipulation/bit_09_multiply-without.md)** — Identische Bit-Shift-Schleifenstruktur, jedoch angewendet auf Addition statt auf Multiplikation.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für wettbewerbsorientierte Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*