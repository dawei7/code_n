# Swap Odd and Even Bits

| | |
|---|---|
| **ID** | `bit_07` |
| **Kategorie** | bit_manipulation |
| **Komplexität (erforderlich)** | $O(1)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **GeeksForGeeks Äquivalent** | [Swap all odd and even bits](https://www.geeksforgeeks.org/swap-all-odd-and-even-bits/) |

## Problemstellung

Gegeben ist eine vorzeichenlose Ganzzahl `N`. Vertausche alle ungeraden Bits mit den geraden Bits.
Wenn die gegebene Zahl beispielsweise `23` (`00010111`) ist, sollte sie in `43` (`00101011`) umgewandelt werden. Jedes Bit an einer geraden Position wird mit dem benachbarten Bit rechts (ungerade Position) vertauscht, und jedes Bit an einer ungeraden Position wird mit dem benachbarten Bit links vertauscht.

**Eingabe:** Eine vorzeichenlose 32-Bit-Ganzzahl `N`.
**Ausgabe:** Eine Ganzzahl, die die vertauschten Bits repräsentiert.

## Anwendung

- Zur Demonstration von Kompetenz im Bereich absoluter **Bit Masking**.
- Wenn Sie spezifische, sich wiederholende Bitmuster über eine gesamte Ganzzahl hinweg gleichzeitig isolieren müssen.

## Ansatz

**1. Die Logik des Vertauschens:**
Anstatt zu versuchen, ein Bitpaar auszuwählen, es zu vertauschen und zum nächsten Paar überzugehen (was eine Schleife erfordern würde), können wir dies sofort erledigen!
Wenn wir alle geraden Bits (0, 2, 4...) mit allen ungeraden Bits (1, 3, 5...) vertauschen wollen, können wir dies in zwei unabhängige Schritte unterteilen:
1. Isoliere alle geraden Bits. Da sie zu ungeraden Bits werden sollen, verschieben wir sie einfach um 1 Position nach rechts! (`>> 1`)
2. Isoliere alle ungeraden Bits. Da sie zu geraden Bits werden sollen, verschieben wir sie einfach um 1 Position nach links! (`<< 1`)
Schließlich führen wir die beiden Hälften mittels bitweisem ODER (`|`) wieder zusammen.

**2. Erstellen der Masken:**
Wie isolieren wir NUR die geraden Bits? Wir benötigen eine Binärzahl, die an jeder geraden Position eine `1` und überall sonst eine `0` hat:
`1010 1010 1010 1010 1010 1010 1010 1010`
In Hexadezimalschreibweise ist `1010` gleich `A`. Die 32-Bit-Maske lautet also `0xAAAAAAAA`.

Wie isolieren wir NUR die ungeraden Bits? Wir benötigen eine Binärzahl, die an jeder ungeraden Position eine `1` hat:
`0101 0101 0101 0101 0101 0101 0101 0101`
In Hexadezimalschreibweise ist `0101` gleich `5`. Die 32-Bit-Maske lautet also `0x55555555`.

**3. Die Ausführung:**
- Extrahiere gerade Bits: `even_bits = n & 0xAAAAAAAA`.
- Extrahiere ungerade Bits: `odd_bits = n & 0x55555555`.
- Verschiebe gerade Bits auf ungerade Positionen: `even_bits >>= 1`.
- Verschiebe ungerade Bits auf gerade Positionen: `odd_bits <<= 1`.
- Zusammenführen: `return even_bits | odd_bits`.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for bit_07: Swap Odd and Even Bits.

Swap the odd and even bits of n. Bit 0 (LSB) goes
"""


def solve(n):
    """Swap the odd and even bits of n. Bit 0 (LSB) goes to bit 1, etc."""
    even_mask = 0x55555555
    odd_mask = 0xAAAAAAAA
    even_bits = (n & even_mask) >> 1
    odd_bits = (n & odd_mask) << 1
    return even_bits | odd_bits
```

</details>

## Durchlauf

`n = 23` (`00010111`).
(Zur Verdeutlichung zeigen wir nur die untersten 8 Bits. Die `A`-Maske ist `10101010`, die `5`-Maske ist `01010101`).

1. **Extrahiere gerade Bits:**
   - `00010111 & 10101010` = `00000010`
2. **Extrahiere ungerade Bits:**
   - `00010111 & 01010101` = `00010101`
3. **Verschiebe gerade Bits:**
   - `00000010 >> 1` = `00000001`
4. **Verschiebe ungerade Bits:**
   - `00010101 << 1` = `00101010`
5. **Zusammenführen (ODER):**
   - `00000001 | 00101010` = `00101011` (`43`).

Das Ergebnis ist `43`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(1)$ | $O(1)$ |
| **Schlechtester Fall** | $O(1)$ | $O(1)$ |

Der Algorithmus führt genau zwei UND-Operationen, zwei Verschiebungen und eine ODER-Operation aus. Er wird in konstanten $O(1)$ CPU-Zyklen ausgeführt, unabhängig von der Größe oder dem Wert von N.
Die Platzkomplexität ist strikt $O(1)$.

## Varianten & Optimierungen

- **64-Bit-Ganzzahlen:** Wenn die Eingabe eine 64-Bit-Ganzzahl anstelle einer 32-Bit-Ganzzahl ist, verdoppeln sich die Masken einfach in der Länge: `0xAAAAAAAAAAAAAAAA` und `0x5555555555555555`.
- **Endianness/Architektur:** In Python haben Ganzzahlen eine beliebige Präzision. Wenn Sie `(n & 0xAAAAAAAA) >> 1` verwenden, führt Python die Verschiebung sicher aus. In C++/Java hingegen MUSS bei einer vorzeichenbehafteten negativen Ganzzahl ein logischer Rechts-Shift `>>>` anstelle eines arithmetischen Rechts-Shifts `>>` verwendet werden, da sonst das Vorzeichenbit dupliziert wird und den oberen Teil der Ganzzahl zerstört!

## Anwendungen in der Praxis

- **Netzwerk-Endianness-Tausch:** Das Vertauschen von 16-Bit- oder 32-Bit-Hälften von Ganzzahlen bei der Datenübertragung über ein Netzwerk (Network Byte Order vs. Host Byte Order) verwendet genau diese identische Maskierungs- und Verschiebungsstrategie, nur mit gröberen Masken wie `0xFF00FF00`!

## Verwandte Algorithmen in cOde(n)

- **[bit_12 - Reverse Bits](bit_12_reverse-bits.md)** — Wenn Sie die GESAMTE 32-Bit-Zeichenfolge umkehren möchten, wenden Sie diese exakte Tauschlogik rekursiv an! Zuerst tauschen Sie benachbarte 1-Bit-Paare (wie in diesem Algorithmus), dann tauschen Sie benachbarte 2-Bit-Blöcke, dann 4-Bit-Blöcke...

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*