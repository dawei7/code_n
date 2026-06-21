# Minimum Bit Flips to Convert Number

| | |
|---|---|
| **ID** | `bit_06` |
| **Category** | bit_manipulation |
| **Complexity (required)** | $O(K)$ Time, $O(1)$ Space |
| **Difficulty** | 2/10 |
| **Interview relevance** | 8/10 |
| **LeetCode Equivalent** | [Minimum Bit Flips to Convert Number](https://leetcode.com/problems/minimum-bit-flips-to-convert-number/) |

## Problem statement

Ein Bit-Flip einer Zahl `x` besteht darin, ein Bit in der Binärdarstellung von `x` auszuwählen und es entweder von `0` auf `1` oder von `1` auf `0` zu invertieren.
Gegeben sind zwei Ganzzahlen `start` und `goal`. Geben Sie die minimale Anzahl an Bit-Flips zurück, die erforderlich sind, um `start` in `goal` umzuwandeln.

**Input:** Zwei Ganzzahlen `start` und `goal`.
**Output:** Eine Ganzzahl, die die minimale Anzahl an Bit-Flips repräsentiert.

## Wann ist es zu verwenden

- Zur Messung der **Hamming-Distanz** zwischen zwei Ganzzahlen.
- Eine klassische, trivial einfache Kombination zweier grundlegender Bit-Manipulations-Techniken (XOR + Zählen gesetzter Bits).

## Ansatz

**1. Identifizierung der unterschiedlichen Bits:**
Wenn wir wissen wollen, wie viele Bits wir flippen müssen, um `A` in `B` umzuwandeln, müssen wir zuerst exakt identifizieren, welche Bits zwischen `A` und `B` unterschiedlich sind.
Welcher bitweise Operator liefert eine `1`, wenn zwei Bits unterschiedlich sind, und eine `0`, wenn sie gleich sind?
**XOR (`^`)!**
Wenn wir `difference = start ^ goal` berechnen, hat die Binärdarstellung von `difference` an jeder Position eine `1`, an der `start` und `goal` nicht übereinstimmten, und eine `0`, wo sie übereinstimmten.

**2. Zählen der unterschiedlichen Bits:**
Da wir nun eine Zahl (`difference`) haben, die alle Unterschiede repräsentiert, besteht das Problem buchstäblich nur noch darin, die Anzahl der `1`-Bits in dieser Ganzzahl zu zählen.
Dies haben wir bereits mit dem Algorithmus von Brian Kernighan (`bit_01`) gelöst!
Wir führen einfach wiederholt `difference = difference & (difference - 1)` aus und erhöhen einen Zähler, bis `difference` den Wert 0 erreicht.

## Algorithmus

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for bit_06: Bit Flips to Convert.

Given two non-negative integers a and b, return
"""


def solve(a, b):
    """Return the number of bit flips to convert a to b (Hamming distance)."""
    return bin(a ^ b).count("1")
```

</details>

## Walk-through

`start = 10` (`1010`), `goal = 7` (`0111`).

1. **Berechnung von XOR:**
   - `difference = 1010 ^ 0111 = 1101` (`13`).
   - Die unterschiedlichen Bits sind durch die `1`en hervorgehoben.
2. **Zählen der gesetzten Bits (13 = 1101):**
   - Schleife 1: `difference > 0`. `flips = 1`.
     `difference = 1101 & 1100 = 1100` (`12`).
   - Schleife 2: `difference > 0`. `flips = 2`.
     `difference = 1100 & 1011 = 1000` (`8`).
   - Schleife 3: `difference > 0`. `flips = 3`.
     `difference = 1000 & 0111 = 0000` (`0`).
   - Schleife 4: `difference == 0`. Schleife terminiert.

Ergebnis `flips = 3`. ✓ (Die Bits 0, 1 und 3 mussten geflippt werden).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(K)$ | $O(1)$ |
| **Schlechtester Fall** | $O(K)$ | $O(1)$ |

*Wobei K die Anzahl der unterschiedlichen Bits ist (die Hamming-Distanz).*
Das XOR benötigt exakt 1 CPU-Zyklus. Die Schleife nach Brian Kernighan benötigt K Iterationen, was zu $O(K)$ führt.
Bei Verwendung eingebauter Hardware-Instruktionen wie `.bit_count()` reduziert sich die Gesamtlaufzeit auf strikt $O(1)$.
Die Platzkomplexität ist strikt $O(1)$.

## Varianten & Optimierungen

- **Hamming-Distanz zwischen Strings:** Wenn `start` und `goal` Strings gleicher Länge sind (z. B. DNA-Sequenzen `"GATTACA"` und `"GCATACG"`), können diese nicht direkt mit XOR verknüpft werden. Man muss über die Strings Zeichen für Zeichen iterieren und `if start[i] != goal[i]` zählen. Dies benötigt $O(N)$ Zeit.

## Anwendungen in der Praxis

- **Fehlerkorrekturcodes:** In der Telekommunikation (wie Wi-Fi oder 5G) berechnet die Hamming-Distanz exakt, wie viel Rauschen bzw. Korruption während der Paketübertragung aufgetreten ist. Dies bestimmt, ob eine Vorwärtsfehlerkorrektur (wie ein Reed-Solomon-Code) die Daten wiederherstellen kann oder ob eine erneute Übertragung erforderlich ist.
- **Klassifizierung im maschinellen Lernen:** Finden der K-Nächsten-Nachbarn (KNN) in kategorialen Räumen durch Messung der Hamming-Distanz zwischen kategorialen One-Hot-kodierten Bit-Vektoren.

## Verwandte Algorithmen in cOde(n)

- **[bit_01 - Count Set Bits](bit_01_count-set-bits.md)** — Der grundlegende Kernalgorithmus, der hier verwendet wird.
- **[bit_03 - Single Number (XOR)](bit_03_single-number-xor.md)** — Weitere Untersuchung der XOR-Eigenschaften.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*