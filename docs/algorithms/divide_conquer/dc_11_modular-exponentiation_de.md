# Modulare Potenzierung

| | |
|---|---|
| **ID** | `dc_11` |
| **Kategorie** | divide_conquer |
| **Komplexität (erforderlich)** | $O(log Y)$ Zeit, $O(1)$ Speicherplatz |
| **Schwierigkeitsgrad** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **GeeksForGeeks-Äquivalent** | [Modulare Potenzierung](https://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/) |

## Aufgabenstellung

Gegeben sind drei Zahlen `x`, `y` und `p`, berechne (x^y) \pmod p.
*Einschränkungen:* `y` kann sehr groß sein, und x^y kann die Speichergrenze des physikalischen Universums überschreiten. Sie müssen den Modulo berechnen, ohne dass der Zwischenwert jemals die Standardgrenzen für Ganzzahlen überschreitet.

**Eingabe:** Drei ganze Zahlen `x`, `y` (der Exponent) und `p` (der Modulus).
**Ausgabe:** Eine ganze Zahl, die den berechneten Modulo-Exponenten darstellt.

## Wann man es verwendet

- Um riesige Potenzen in der Kryptografie oder im Wettbewerbsprogrammieren sicher zu berechnen.
- Veranschaulicht, wie sich die Modulo-Arithmetik perfekt auf die Multiplikation verteilt.

## Vorgehensweise

**1. Der Fehler bei der Post-Modulo-Methode:**
Wenn Sie versuchen, `(x ** y) % p` direkt zu berechnen, führt x^y sofort zu einem Speicherüberlauf. Selbst in Python (das über beliebige Genauigkeit verfügt) führt die Berechnung von 10^{10^9} dazu, dass die CPU einfriert und der gesamte Arbeitsspeicher aufgebraucht wird, bevor der `% p`-Operator überhaupt angewendet werden kann!

**2. Die Verteilungsregel des Modulo:**
Die Mathematik garantiert, dass gilt:
(A x B) \pmod P = [ (A \pmod P) x (B \pmod P) ] \pmod P
Das bedeutet, dass wir den Modulo-Operator BEI JEDEM EINZELNEN MULTIPLIKATIONSSCHRITT anwenden können und das Endergebnis identisch sein wird! Die Zahl wird NIEMALS größer als P^2 werden.

**3. Teile und herrsche (iterative schnelle Potenzierung):**
Wir kombinieren diese Modulo-Eigenschaft mit der **Potenzierung durch Quadrieren** (`dc_01`).
Anstelle einer Rekursion führen wir dies iterativ unter Verwendung der binären Darstellung durch (ähnlich wie bei der russischen Bauernmultiplikation).
- `res = 1` initialisieren.
- Aktualisiere `x = x % p` (nur für den Fall, dass die Basis bereits größer als p ist).
- Schleife, solange `y > 0`:
  - Wenn das niedrigste Bit von `y` 1 ist (`y & 1`), multipliziere `res` mit `x` und berechne sofort den Rest modulo `p`!
  - `x` quadrieren (`x = x * x`), und sofort modulo `p` berechnen!
  - Verschiebe `y` nach rechts (`y >>= 1`).

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

## Schritt-für-Schritt-Anleitung

`x = 2`, `y = 5`, `p = 13`.
Berechne (2^5) \pmod{13}.
`res = 1`. `x = 2 % 13 = 2`.

1. **Schleife 1:** `y = 5`(`101`).
   - `y & 1 == 1`. (Wahr).
   - `res = (1 * 2) % 13 = 2`.
   - `y = 5 >> 1 = 2`(`010`).
   - `x = (2 * 2) % 13 = 4`.
2. **Schleife 2:** `y = 2`.
   - `y & 1 == 1`. (Falsch).
   - `y = 2 >> 1 = 1`(`001`).
   - `x = (4 * 4) % 13 = 16 % 13 = 3`. *(Entscheidender Schritt! Der Wert ist nicht auf 16 gestiegen, sondern wieder auf 3 gesunken!)*
3. **Schleife 3:** `y = 1`.
   - `y & 1 == 1`. (Wahr).
   - `res = (2 * 3) % 13 = 6`.
   - `y = 1 >> 1 = 0`.
   - `x = (3 * 3) % 13 = 9`.
4. **Schleife 4:** `y = 0`. Beenden.

Das Ergebnis `res` ist `6`. ✓
*(Überprüfung: 2^5 = 32. 32 \pmod{13} = 6. Die Rechnung geht auf!)*

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(log Y)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(log Y)$ | $O(1)$ |
| **Schlechtester Fall** | $O(log Y)$ | $O(1)$ |

Die Schleife läuft genau so oft, wie `y` Bits enthält. Die Zeitkomplexität beträgt genau $O(log Y)$.
Durch die iterative Vorgehensweise vermeiden wir den rekursiven Aufrufstapel. Die Platzkomplexität beträgt streng $O(1)$.
Der zu jedem Zeitpunkt in einer Variablen gespeicherte Maximalwert beträgt genau (P-1) × (P-1), wodurch garantiert wird, dass es zu keinem 64-Bit-Ganzzahlüberlauf kommt, sofern P in eine 32-Bit-Ganzzahl passt.

## Varianten & Optimierungen

- **Fermats kleiner Satz (modulare Inverse):** Was ist, wenn der Exponent `y` negativ ist? Modulo-Arithmetik mit Brüchen ist nicht möglich! Man muss mit der **modularen multiplikativen Inversen** multiplizieren. Ist `p` eine Primzahl, besagt der Satz von Fermat: X^{-1} \pmod P \equiv X^{P-2} \pmod P. Man ruft buchstäblich einfach genau diesen Algorithmus erneut auf: `modular_exponentiation(x, p - 2, p)`!

## Anwendungen in der Praxis

- **RSA-Public-Key-Verschlüsselung:** Das absolute Rückgrat der Internetsicherheit (HTTPS). Ein verschlüsselter Chiffretext `C` wird mithilfe des privaten Schlüssels `d` des Empfängers über die Formel M = C^d \pmod N wieder in die ursprüngliche Nachricht `M` mit dem privaten Schlüssel des Empfängers `d` mithilfe der Formel M = C^d \pmod N entschlüsselt. Sowohl `d` als auch `N` sind in der Regel 2048-Bit-Zahlen. Dieser Algorithmus ist der Motor, der diese Entschlüsselung ausführt.

## Verwandte Algorithmen in cOde(n)

- **[dc_01 - Pow(x, n)](dc_01_power-x-to-the-n.md)** — Die rekursive Version dieses Algorithmus ohne die Modulo-Eigenschaft.
- **[bit_09 – Multiplizieren ohne Multiplikation](../bit_manipulation/bit_09_multiply-without.md)** – Identische Bitverschiebungs-Schleifenstruktur, jedoch auf Addition statt auf Multiplikation angewendet.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
in Anlehnung an die kanonische Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
