# Ungerade und gerade Bits vertauschen

| | |
|---|---|
| **ID** | `bit_07` |
| **Kategorie** | bit_manipulation |
| **Komplexität (erforderlich)** | $O(1)$ Zeit, $O(1)$ Speicherplatz |
| **Schwierigkeitsgrad** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **GeeksForGeeks-Äquivalent** | [Alle ungeraden und geraden Bits vertauschen](https://www.geeksforgeeks.org/swap-all-odd-and-even-bits/) |

## Aufgabenstellung

Gegeben sei eine vorzeichenlose Ganzzahl `N`. Vertausche alle ungeraden Bits mit den geraden Bits.
Ist die gegebene Zahl beispielsweise `23`(`00010111`), soll sie in `43`(`00101011`) umgewandelt werden. Jedes Bit an einer geraden Position wird mit dem benachbarten Bit auf der rechten Seite (ungerade Position) vertauscht, und jedes Bit an einer ungeraden Position wird mit dem benachbarten Bit auf der linken Seite vertauscht.

**Eingabe:** Eine vorzeichenlose 32-Bit-Ganzzahl `N`.
**Ausgabe:** Eine Ganzzahl, die die vertauschten Bits darstellt.

## Anwendungsfälle

- Um Kenntnisse im Umgang mit der absoluten **Bitmaskierung** unter Beweis zu stellen.
- Wenn Sie bestimmte sich wiederholende Bitmuster über eine gesamte Ganzzahl hinweg gleichzeitig sauber isolieren müssen.

## Vorgehensweise

**1. Die Logik des Vertauschens:**
Anstatt zu versuchen, irgendwie ein Bitpaar auszuwählen, es zu vertauschen und zum nächsten Paar überzugehen (was eine Schleife erfordern würde), können wir dies sofort erledigen!
Wenn wir alle geraden Bits (0, 2, 4...) mit allen ungeraden Bits (1, 3, 5...) vertauschen wollen, können wir dies in zwei unabhängige Schritte unterteilen:
1. Alle geraden Bits isolieren. Da wir möchten, dass sie zu ungeraden Bits werden, verschieben wir sie einfach alle um eine Position nach rechts! (`>> 1`)
2. Alle ungeraden Bits isolieren. Da sie zu geraden Bits werden sollen, verschieben wir sie einfach alle um eine Position nach links! (`<< 1`)
Schließlich kombinieren wir die beiden Hälften einfach wieder mit dem bitweisen ODER (`|`).

**2. Erstellen der Masken:**
Wie isolieren wir NUR die geraden Bits? Wir benötigen eine Binärzahl, die an jeder geraden Position `1`s und an allen anderen Stellen `0`s enthält:
`1010 1010 1010 1010 1010 1010 1010 1010`
Im Hexadezimalformat ist `1010` gleich `A`. Die 32-Bit-Maske lautet also `0xAAAAAAAA`.

Wie isolieren wir NUR die ungeraden Bits? Wir benötigen eine Binärzahl, die an jeder ungeraden Position `1` enthält:
`0101 0101 0101 0101 0101 0101 0101 0101`
Im Hexadezimalformat ist `0101` gleich `5`. Die 32-Bit-Maske lautet also `0x55555555`.

**3. Die Ausführung:**
- Gerade Bits extrahieren: `even_bits = n & 0xAAAAAAAA`.
- Ungerade Bits extrahieren: `odd_bits = n & 0x55555555`.
- Die geraden Bits an ungerade Stellen verschieben: `even_bits >>= 1`.
- Die ungeraden Bits an gerade Stellen verschieben: `odd_bits <<= 1`.
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

## Schritt-für-Schritt-Anleitung

`n = 23`(`00010111`).
(Der Übersichtlichkeit halber zeigen wir nur die untersten 8 Bits. Die Maske von `A` ist `10101010`, die Maske von `5` ist `01010101`).

1. **Gerade Bits extrahieren:**
   - `00010111 & 10101010` = `00000010`
2. **Ungerade Bits extrahieren:**
   - `00010111 & 01010101` = `00010101`
3. **Gerade Bits verschieben:**
   - `00000010 >> 1` = `00000001`
4. **Ungerade Bits verschieben:**
   - `00010101 << 1` = `00101010`
5. **Wieder zusammenfügen (ODER):**
   - `00000001 | 00101010` = `00101011`(`43`).

Das Ergebnis ist `43`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(1)$ | $O(1)$ |
| **Schlechtester Fall** | $O(1)$ | $O(1)$ |

Der Algorithmus führt genau zwei UND-Operationen, zwei Verschiebungen und eine ODER-Operation durch. Er wird in konstanten $O(1)$ CPU-Zyklen ausgeführt, unabhängig von der Größe oder dem Wert von N.
Die Platzkomplexität beträgt streng $O(1)$.

## Varianten und Optimierungen

- **64-Bit-Ganzzahlen:** Wenn die Eingabe eine 64-Bit-Ganzzahl anstelle einer 32-Bit-Ganzzahl ist, verdoppelt sich die Länge der Masken einfach. `0xAAAAAAAAAAAAAAAA` und `0x5555555555555555`.
- **Endianness/Architektur:** In Python haben Ganzzahlen beliebige Genauigkeit. Wenn Sie `(n & 0xAAAAAAAA) >> 1` ausführen, übernimmt Python die Verschiebung sicher. In C++/Java MUSS jedoch, wenn die Ganzzahl vorzeichenbehaftet und negativ ist, anstelle einer arithmetischen Rechtsverschiebung `>>` eine logische Rechtsverschiebung `>>>` verwendet werden, da sich sonst das Vorzeichenbit verdoppelt und den obersten Teil der Ganzzahl zerstört!

## Praktische Anwendungen

- **Umkehrung der Netzwerk-Endianness:** Das Vertauschen von 16-Bit- oder 32-Bit-Hälften von Ganzzahlen bei der Datenübertragung über ein Netzwerk (Netzwerk-Byte-Reihenfolge vs. Host-Byte-Reihenfolge) nutzt genau dieselbe Maskierungs- und Verschiebungsstrategie, nur mit größeren Masken wie `0xFF00FF00`!

## Verwandte Algorithmen in cOde(n)

- **[bit_12 – Bits umkehren](bit_12_reverse-bits.md)** — Wenn du die GESAMTE 32-Bit-Zeichenkette umkehren möchtest, wendest du genau diese Vertauschungslogik rekursiv an! Zuerst vertauschst du benachbarte 1-Bit-Paare (wie bei diesem Algorithmus), dann vertauschst du benachbarte 2-Bit-Blöcke, dann 4-Bit-Blöcke …

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
in Anlehnung an die kanonische Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
