# Anzahl der gesetzten Bits (Algorithmus von Brian Kernighan)

| | |
|---|---|
| **ID** | `bit_01` |
| **Kategorie** | Bitmanipulation |
| **Komplexität (erforderlich)** | $O(K)$ Zeit, $O(1)$ Speicherplatz |
| **Schwierigkeitsgrad** | 3/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Anzahl der 1-Bits](https://leetcode.com/problems/number-of-1-bits/) |

## Aufgabenstellung

Schreiben Sie eine Funktion, die eine vorzeichenlose Ganzzahl entgegennimmt und die Anzahl der darin enthaltenen „1“-Bits zurückgibt (auch als Hamming-Gewicht bekannt).

**Eingabe:** Eine vorzeichenlose Ganzzahl `n`.
**Ausgabe:** Eine Ganzzahl, die die Anzahl der „1“-Bits in `n` angibt.

## Wann man sie verwendet

- Um die gesetzten Bits (1en) einer Zahl optimal zu zählen.
- Sie bildet die absolute Grundlage für fast alle Aufgaben zur Bitmanipulation.

## Vorgehensweise

**1. Der naive Ansatz:**
Wir könnten wiederholt das niedrigstwertige Bit (LSB) mit `n & 1` überprüfen und die Zahl anschließend nach rechts verschieben `n >>= 1`. Dies erfordert bei einer 32-Bit-Ganzzahl genau 32 Iterationen, unabhängig davon, ob sie ein `1` Bit oder dreißig `1` Bits enthält.

**2. Brian Kernighans Algorithmus:**
Können wir direkt von einem `1`-Bit zum nächsten springen und dabei alle `0`-Bits überspringen? Ja!
Betrachten wir die mathematische Operation `n - 1`. Was bewirkt die Subtraktion von 1 im Binärsystem?
Es kehrt alle Bits um, beginnend mit dem `1`-Bit ganz rechts bis zum Ende der Zahl!
Beispielsweise, wenn `n = 12` (`1100` im Binärsystem):
`n - 1 = 11` (`1011` im Binärsystem).
Beachte, dass das rechteste `1` in `n` (an der 2er-Stelle) in ein `0` umgedreht wurde und alle `0` rechts davon in `1` umgedreht wurden.

Wenn wir eine bitweise UND-Verknüpfung zwischen `n` und `n - 1` durchführen:
`n & (n - 1)`
`1100 & 1011 = 1000`.
Das Bit `1` ganz rechts wurde vollständig gelöscht!

**3. Die Strategie:**
Wir führen `n = n & (n - 1)` einfach in einer Schleife aus. Jedes Mal, wenn wir diese Zeile ausführen, wird genau ein `1`-Bit gelöscht. Dabei erhöhen wir jedes Mal einen Zähler.
Wenn `n` den Wert 0 erreicht, wird die Schleife beendet!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for bit_01: Count Set Bits.

Count the number of 1-bits in the binary
"""


def solve(n):
    """Count the 1-bits in n (Hamming weight)."""
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
```

</details>

## Schritt-für-Schritt-Anleitung

`n = 14` (Binär: `1110`). `count = 0`.

1. **Schleife 1:**
   - `n != 0`. `count = 1`.
   - `n - 1` = `13`(`1101`).
   - `n = 1110 & 1101 = 1100`(`12`). (Die 1 ganz rechts wurde gelöscht!)
2. **Schleife 2:**
   - `n != 0`. `count = 2`.
   - `n - 1` = `11`(`1011`).
   - `n = 1100 & 1011 = 1000`(`8`).
3. **Schleife 3:**
   - `n != 0`. `count = 3`.
   - `n - 1` = `7`(`0111`).
   - `n = 1000 & 0111 = 0000`(`0`).
4. **Schleife 4:**
   - `n == 0`. Die Schleife endet.

Ergebnis: `count = 3`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(K)$ | $O(1)$ |
| **Schlechtester Fall** | $O(K)$ | $O(1)$ |

*Dabei ist K die Anzahl der „1“-Bits in der Ganzzahl.*
Im absolut schlimmsten Fall (eine Zahl wie `0xFFFFFFFF`) sind für eine 32-Bit-Ganzzahl 32 Iterationen erforderlich, was technisch gesehen $O(1)$ im Verhältnis zur Größe der Eingabezahl entspricht. Asymptotisch gesehen ist die Anzahl der Iterationen jedoch streng auf $O(K)$ begrenzt, was diesen Ansatz bei spärlichen Bitmasken dem naiven $O(log n)$-Verschiebungsansatz weit überlegen macht.
Der Speicherbedarf beträgt streng $O(1)$.

## Varianten & Optimierungen

- **Integrierte Funktionen:** Die meisten modernen Sprachen verfügen hierfür über hardwarebeschleunigte Befehle. Verwenden Sie in Python `n.bit_count()`. In C++ verwenden Sie `__builtin_popcount(n)`. In Java verwenden Sie `Integer.bitCount(n)`. Diese werden zu einem einzigen CPU-Befehl kompiliert (wie `POPCNT` auf x86) und in buchstäblich einem CPU-Zyklus ausgeführt.
- **Das niedrigstwertige gesetzte Bit extrahieren:** Wenn Sie das niedrigstwertige gesetzte Bit nur *isolieren* und nicht löschen möchten, verwenden Sie `n & -n`. Für `n = 12`(`1100`) ergibt `n & -n` `4`(`0100`). Dies wird häufig in Fenwick-Bäumen (`fenwick_01`) verwendet!

## Praktische Anwendungen

- **Kryptografie / Hashing:** Berechnung des Hamming-Abstands zwischen zwei Hashes, um Bit-Rot, Fehlerverfälschungen oder Bildähnlichkeit zu erkennen (z. B. Perzeptuelles Hashing).
- **Schachengines (Bitboards):** Sofortige Berechnung der Anzahl zulässiger Züge einer Figur durch Zählen der `1`s auf einer 64-Bit-Ganzzahl-Darstellung des Bretts.

## Verwandte Algorithmen in cOde(n)

- **[bit_02 – Power-of-Two-Prüfung](bit_02_power-of-two-check.md)** – Verwendet genau denselben `n & (n - 1)`-Trick, wertet ihn jedoch ohne Schleife aus!
- **[fenwick_01 – Binärindizierter Baum](../fenwick/fenwick_01_binary-indexed-tree.md)** – Stützt sich auf die Extraktion des niedrigsten gesetzten Bits (`n & -n`), um die Offsets im Baum-Array zu berechnen.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde
und sich an der kanonischen Struktur orientiert, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
