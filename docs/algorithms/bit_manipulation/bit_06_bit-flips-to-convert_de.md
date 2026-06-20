# Minimale Anzahl von Bit-Flips zur Umwandlung einer Zahl

| | |
|---|---|
| **ID** | `bit_06` |
| **Kategorie** | bit_manipulation |
| **Komplexität (erforderlich)** | $O(K)$ Zeit, $O(1)$ Speicherplatz |
| **Schwierigkeitsgrad** | 2/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **LeetCode-Äquivalent** | [Minimale Anzahl von Bitumkehrungen zur Umwandlung einer Zahl](https://leetcode.com/problems/minimum-bit-flips-to-convert-number/) |

## Aufgabenstellung

Eine Bitumkehr einer Zahl `x` besteht darin, ein Bit in der binären Darstellung von `x` auszuwählen und es entweder von `0` in `1` oder von `1` in `0` um.
Gegeben sind zwei ganze Zahlen `start` und `goal`. Gib die minimale Anzahl an Bitumkehrungen zurück, um `start` in `goal` umzuwandeln.

**Eingabe:** Zwei ganze Zahlen `start` und `goal`.
**Ausgabe:** Eine ganze Zahl, die die minimale Anzahl der Bitumkehrungen angibt.

## Anwendungsfälle

- Zur Berechnung der **Hamming-Distanz** zwischen zwei ganzen Zahlen.
- Eine klassische, trivial einfache Kombination zweier grundlegender Techniken zur Bitmanipulation (XOR + Zählen der gesetzten Bits).

## Vorgehensweise

**1. Identifizieren der unterschiedlichen Bits:**
Wenn wir wissen wollen, wie viele Bits wir umdrehen müssen, um `A` in `B` umzuwandeln, müssen wir zunächst GENAU ermitteln, welche Bits sich bei `A` und `B` unterscheiden.
Welcher bitweise Operator gibt ein `1` aus, wenn zwei Bits unterschiedlich sind, und ein `0`, wenn sie gleich sind?
**XOR (`^`)!**
Wenn wir `difference = start ^ goal` berechnen, enthält die binäre Darstellung von `difference` an jeder Stelle, an der `start` und `goal` nicht übereinstimmten, und ein `0` dort, wo sie übereinstimmten.

**2. Zählen der unterschiedlichen Bits:**
Da wir nun eine Zahl (`difference`) haben, die alle Abweichungen repräsentiert, lautet das Problem buchstäblich nur noch: „Zähle die Anzahl der `1` Bits in dieser Ganzzahl“.
Das haben wir bereits mit Brian Kernighans Algorithmus (`bit_01`) gelöst!
Wir führen einfach wiederholt `difference = difference & (difference - 1)` aus und erhöhen einen Zähler, bis `difference` den Wert 0 erreicht.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for bit_06: Bit Flips to Convert.

Given two non-negative integers a and b, return
"""


def solve(a, b):
    """Return the number of bit flips to convert a to b (Hamming distance)."""
    return bin(a ^ b).count("1")
```

</details>

## Schritt-für-Schritt-Anleitung

`start = 10`(`1010`), `goal = 7`(`0111`).

1. **XOR berechnen:**
   - `difference = 1010 ^ 0111 = 1101`(`13`).
   - Die unterschiedlichen Bits sind durch die `1`s hervorgehoben.
2. **Set-Bits zählen (13 = 1101):**
   - Schleife 1: `difference > 0`. `flips = 1`.
 `difference = 1101 & 1100 = 1100`(`12`).
   - Schleife 2: `difference > 0`. `flips = 2`.
 `difference = 1100 & 1011 = 1000`(`8`).
   - Schleife 3: `difference > 0`. `flips = 3`.
 `difference = 1000 & 0111 = 0000`(`0`).
   - Schleife 4: `difference == 0`. Schleife endet.

Ergebnis `flips = 3`. ✓ (Die Bits 0, 1 und 3 mussten umgedreht werden).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(K)$ | $O(1)$ |
| **Schlechteste** | $O(K)$ | $O(1)$ |

*Dabei ist K die Anzahl der unterschiedlichen Bits (der Hamming-Abstand).*
Die XOR-Operation benötigt genau 1 CPU-Zyklus. Die Brian-Kernighan-Schleife benötigt K Iterationen, was $O(K)$ ergibt.
Bei Verwendung integrierter Hardwarebefehle wie `.bit_count()` reduziert sich die Gesamtzeit auf genau $O(1)$.
Die Platzkomplexität beträgt genau $O(1)$.

## Varianten & Optimierungen

- **Hamming-Abstand zwischen Zeichenketten:** Wenn `start` und `goal` Zeichenketten gleicher Länge sind (z. B. DNA-Sequenzen `"GATTACA"` und `"GCATACG"`), kann man sie nicht direkt mit XOR verrechnen. Man muss die Strings Zeichen für Zeichen durchlaufen und `if start[i] != goal[i]` zählen. Dies dauert $O(N)$ Zeit.

## Praktische Anwendungen

- **Fehlerkorrekturcodes:** In der Telekommunikation (wie WLAN oder 5G) berechnet der Hamming-Abstand genau, wie viel Rauschen/Verfälschung während der Paketübertragung aufgetreten ist, was darüber entscheidet, ob eine Vorwärtsfehlerkorrektur (wie ein Reed-Solomon-Code) die Daten wiederherstellen kann oder ob eine erneute Übertragung erforderlich ist.
- **Klassifizierung im maschinellen Lernen:** Ermittlung der K-nächsten Nachbarn (KNN) in kategorialen Räumen durch Messung der Hamming-Distanz zwischen kategorialen, One-Hot-kodierten Bitvektoren.

## Verwandte Algorithmen in cOde(n)

- **[bit_01 – Set-Bits zählen](bit_01_count-set-bits.md)** — Der hier verwendete grundlegende Kernalgorithmus.
- **[bit_03 – Einzelzahl (XOR)](bit_03_single-number-xor.md)** — Weitere Untersuchung der XOR-Eigenschaften.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde
und sich an der kanonischen Struktur orientiert, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
