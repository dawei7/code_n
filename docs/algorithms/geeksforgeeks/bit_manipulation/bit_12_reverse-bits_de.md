# Reverse Bits

| | |
|---|---|
| **ID** | `bit_12` |
| **Kategorie** | bit_manipulation |
| **Komplexität (erforderlich)** | $O(1)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 3/10 |
| **Relevanz für Vorstellungsgespräche** | 7/10 |
| **LeetCode-Äquivalent** | [Reverse Bits](https://leetcode.com/problems/reverse-bits/) |

## Problemstellung

Kehren Sie die Bits einer gegebenen 32-Bit vorzeichenlosen Ganzzahl (unsigned integer) um.

**Eingabe:** Eine vorzeichenlose 32-Bit-Ganzzahl `n`.
**Ausgabe:** Eine Ganzzahl, die den bit-umgekehrten Wert repräsentiert.

## Wann ist dies zu verwenden?

- Eine grundlegende Übung zur Bit-Manipulation, die beweist, dass Sie wissen, wie man Binärzahlen von Grund auf aufbaut.

## Ansatz

**1. Der Baustein-Ansatz:**
Stellen Sie sich vor, Sie nehmen einen Kartenstapel und bauen einen völlig neuen, umgekehrten Stapel auf.
Sie nehmen die oberste Karte vom ursprünglichen Stapel und legen sie unter den neuen Stapel.
Sie wiederholen dies, bis der ursprüngliche Stapel leer ist.
Genau das können wir mit Bits tun!

1. Erstellen Sie eine `result`-Variable, die mit `0` initialisiert wird.
2. Durchlaufen Sie eine Schleife exakt 32 Mal (da das Problem eine 32-Bit-Ganzzahl garantiert).
3. **Extrahieren** Sie das rechteste Bit von `n` mittels `n & 1`.
4. **Platzieren** Sie dieses Bit in unserem `result`! Aber wo kommt es hin? Da es das rechteste Bit der ursprünglichen Zahl ist, muss es zum LINKESTEN Bit der umgekehrten Zahl werden!
   Tatsächlich ist es einfacher, es einfach auf die rechte Seite von `result` zu schieben und dann sofort *`result` nach links zu verschieben*! Dies schiebt die frühen Bits im Verlauf der Schleife immer weiter nach links.
5. **Verschieben** Sie `n` nach rechts (`n >> 1`), um das nächste Bit freizulegen.

*Kritisches Detail:* Sie MÜSSEN `result` nach links verschieben, BEVOR Sie das extrahierte Bit hinzufügen, da sonst Ihr allererstes Bit am Ende der 32 Schleifendurchläufe um 1 Position zu weit verschoben wäre!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for bit_12: Reverse Bits.

Reverse the bits of a 32-bit unsigned integer n.
"""


def solve(n):
    """Reverse the bits of the 32-bit unsigned integer n."""
    result = 0
    for i in range(32):
        # Take bit i of n, place it at bit (31 - i) of result.
        if n & (1 << i):
            result |= 1 << (31 - i)
    return result
```

</details>

## Durchlauf

Lassen Sie uns eine 4-Bit-Simulation durchführen, um Platz zu sparen: `n = 13` (`1101`). Wir wollen `1011` (`11`). `result = 0`.

1. **Schleife 1 (i=0):**
   - `result = 0 << 1 = 0` (`0000`)
   - `bit = 1101 & 1 = 1`
   - `result = 0000 | 1 = 0001` (`1`)
   - `n = 1101 >> 1 = 110` (`6`)
2. **Schleife 2 (i=1):**
   - `result = 0001 << 1 = 0010` (`2`)
   - `bit = 110 & 1 = 0`
   - `result = 0010 | 0 = 0010` (`2`)
   - `n = 110 >> 1 = 11` (`3`)
3. **Schleife 3 (i=2):**
   - `result = 0010 << 1 = 0100` (`4`)
   - `bit = 11 & 1 = 1`
   - `result = 0100 | 1 = 0101` (`5`)
   - `n = 11 >> 1 = 1` (`1`)
4. **Schleife 4 (i=3):**
   - `result = 0101 << 1 = 1010` (`10`)
   - `bit = 1 & 1 = 1`
   - `result = 1010 | 1 = 1011` (`11`)
   - `n = 1 >> 1 = 0`

Das Ergebnis ist `11` (`1011`). ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(1)$ | $O(1)$ |
| **Schlechtester Fall** | $O(1)$ | $O(1)$ |

Die Schleife läuft exakt 32 Mal mit konstanten $O(1)$-Operationen innerhalb der Schleife. Die Zeitkomplexität ist strikt $O(1)$.
Die Platzkomplexität ist $O(1)$.

## Varianten & Optimierungen

- **Divide and Conquer Blocktausch:** Wenn Sie Bits millionenfach pro Sekunde umkehren müssen, ist eine Schleife mit 32 Verschiebungen tatsächlich zu langsam! Sie können die gesamte 32-Bit-Zeichenfolge in nur 5 $O(1)$-Operationen umkehren!
  1. Tausche benachbarte 1-Bit-Paare: `n = ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)`
  2. Tausche benachbarte 2-Bit-Blöcke: `n = ((n & 0xCCCCCCCC) >> 2) | ((n & 0x33333333) << 2)`
  3. Tausche benachbarte 4-Bit-Blöcke: `n = ((n & 0xF0F0F0F0) >> 4) | ((n & 0x0F0F0F0F) << 4)`
  4. Tausche benachbarte 8-Bit-Blöcke: `n = ((n & 0xFF00FF00) >> 8) | ((n & 0x00FF00FF) << 8)`
  5. Tausche benachbarte 16-Bit-Blöcke: `n = (n >> 16) | (n << 16)`
  Die Bits sind ohne Schleifen perfekt umgekehrt!

## Anwendungen in der Praxis

- **Digitale Signalverarbeitung (FFT):** Der Cooley-Tukey Fast Fourier Transform Algorithmus erfordert, dass auf Array-Elemente in "Bit-Reversed Order" zugegriffen wird. Diese physische Hardware-Bit-Umkehrung stellt sicher, dass die rekursive Signalaufteilung linear im Speicher erfolgt.

## Verwandte Algorithmen in cOde(n)

- **[bit_07 - Swap Odd and Even Bits](bit_07_swap-odd-and-even-bits.md)** — Die grundlegende Voraussetzung für die $O(1)$-Blocktausch-Variante.
- **[math_01 - Reverse Integer](../math/math_01_reverse-integer.md)** — Das Umkehren von Basis-10-Ziffern mittels `% 10` und `/ 10`, was das Extrahieren von Basis-2-Bits mittels `& 1` und `>> 1` perfekt widerspiegelt!

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*